# mcp/tests/test_pause_is_not_publication.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

This module is the **executable specification of the pause's boundary**: pausing a master must not be
able to publish, so the stop is excluded structurally rather than by a runtime condition.

It builds a static, source-level import graph out of the pause module — parsing each reached module's
own AST and following its `import`/`from ... import` statements — and asserts that graph is disjoint
from the twelve modules that can create a commit, move a protected ref, land a series, record a landing
or write a ledger row (`PUBLICATION_MODULES`, declared explicitly so the guard names what it guards
against). It then asserts the graph is **deep enough for that first assertion to mean anything**, and
names two witnesses, because a walker that stops at the direct imports also reaches no publication
module.

The regression it is written against is exact: reaching `worktree_checkpoint_landing` from the stop.
The pause/publication split exists because the two were one verb; a stop that could become the
publication is the defect.

## Code Commentary

### Logic

`_module_files()` indexes every `*.py` under `mcp/src/agents_remember` by dotted name, mapping a
package's `__init__.py` to the package's own name. `_resolve(name, files)` maps a dotted name to the
importable module it denotes by trimming trailing attribute names — `from x.y import Thing` records
both `x.y` and `x.y.Thing`, and only the first resolves.

`_dependencies(node, current, found)` walks one module's AST collecting `Import` aliases and
`ImportFrom` targets (resolving relative levels against the importing module), descending everywhere
**except** under an `if TYPE_CHECKING:` guard, because a type-only import never executes.

`_runtime_imports_of(module)` is the one-step reading: the modules that module itself imports.
`_runtime_import_closure(root)` is the walk, returning every reachable module mapped to the module that
first imports it. `_import_path(parent, target)` reconstructs the importer chain for the failure
message.

`test_the_pause_cannot_reach_any_publication_module()` computes the closure, asserts `reached == []`
with a message naming each publication module and its import path, and then runs the non-vacuity
checks.

### What The Walk Measures, And What It Does Not

The docstring states the method's limits rather than implying completeness, and memory must keep them:

- It is a **static, source-level** graph — imports *inside function bodies* are counted, so it is a
  superset of the runtime import graph in that direction.
- It does **not follow dynamic imports** (`importlib.import_module` and friends), so it is a subset in
  the other direction.
- It is **per-module reachability**, not a process-wide `sys.modules` reading. That is deliberate: a
  session-wide check would see publication modules that *other tests* imported and therefore could not
  be this guard.

The guard establishes this boundary over the statically declared imports its walker
follows. Dynamic imports are outside that measurement; the walk does not establish
that no dynamic-import path exists.

### Invariants And Boundaries

- **Non-vacuity is checked separately from publication disjointness.** Static AST
  inspection of code tree `96bf7343` reaches **95** modules: the pause root,
  **6** direct imports and **88** deeper modules, with **0 of 12** declared
  publication modules reached. A depth-one walk would retain the root and its
  six direct imports but no deeper module; the source's `len(deeper) >= len(direct)`
  assertion would then compare `0 >= 6`. These are static population and assertion
  readings, not a new execution of the test or of a mutant. The earlier card's
  60/5/54 and depth-one 6 figures belong to its superseded measurement account.
- The three checks are: `{PAUSE_MODULE} | direct ⊆ reachable`; `len(deeper) >= len(direct)`; and two
  **named witnesses** that are provably not direct imports — `agents_remember.worktrees.scheduling_mode`
  and `agents_remember.kernel.primitives.gate_vocab` — so the "transitive" claim is legible rather than
  only counted. A final assertion pins `worktree_contract` as one of the direct imports, so the direct
  set itself cannot silently empty.
- A test here must never import or execute the pause at runtime; the whole check is AST parsing plus
  path resolution, so it stays hermetic and cheap.
- The publication set is a `frozenset` literal in the test, not derived from a registry, so adding a
  publication module means editing the guard — the deliberate cost of a guard whose subject is "these
  specific planes must stay unreachable".
- The lane is `architecture-fitness` in `mcp/tests/test-evidence-lanes.toml`: a structural guard over
  the source tree, not a behavioral test of a running service.

### Todos

None recorded. The depth-one regression and the source's separate non-vacuity
assertions are described above; earlier mutation evidence remains evidence of its
original run rather than a fresh result for this code tree.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The twelve modules the pause must not reach: ref transactions, landings, integrate, record-landing, landing-record, the closeout family and direct landing. [1]
- The measurement: module index, dotted-name resolution, `TYPE_CHECKING`-skipping AST dependency walk, and the one-step direct-import reading. [2]
- The walk itself, whose docstring records that expanding a module is what counts and that discovery must not stop it. [3]
- The case: disjointness from every publication module, then the three non-vacuity checks and the two named witnesses. [4]
- The method limits recorded in the module docstring: static AST graph, `TYPE_CHECKING` excluded, no dynamic imports, per-module rather than process-wide. [5]

- The route this guard exists to keep the stop away from.

- The stop module whose closure is measured, and the release authority the closure is required to reach. [7]




> Retained earlier citation wording: - The lane this module is registered in. Source caption: "mcp/tests/test_pause_is_not_publication.py"




### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned structural guard.






- The route this guard exists to keep the stop away from. Anchor: `worktree_checkpoint_landing` [6]




- The lane this module is registered in. Source caption: "mcp/tests/test_pause_is_not_publication.py" [8]
