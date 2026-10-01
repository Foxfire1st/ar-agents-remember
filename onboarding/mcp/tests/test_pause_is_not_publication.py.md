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

So the guard proves the boundary over statically declared imports. It does not prove that no dynamic
import could ever be added; it proves that none exists today and that the declared graph is clean and
deep.

### Invariants And Boundaries

- **Non-vacuity is the load-bearing half, and it is mutation-proof.** Measured on the frozen candidate:
  the closure holds **60** modules including the root, the pause module's own direct imports are **5**,
  and **54** modules lie beyond them, with **0 of 12** publication modules reached. The old defective
  walker — marking a module expanded when it is *discovered* rather than when it is *expanded* —
  reproduced here returns **6** (the root plus its five direct imports) with **0** deeper modules, so
  `len(deeper) >= len(direct)` is `0 >= 5` and the case **fails**. The regression is therefore
  detectable, where the same walker previously produced a green test.
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

None recorded. The depth-1 defect this card originally recorded was repaired inside the same leaf
(before its candidate was frozen), so the card documents the repaired walker and the mutation evidence
that keeps it repaired.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The twelve modules the pause must not reach: ref transactions, landings, integrate, record-landing, landing-record, the closeout family and direct landing. [1]
- The measurement: module index, dotted-name resolution, `TYPE_CHECKING`-skipping AST dependency walk, and the one-step direct-import reading. [2]
- The walk itself, whose docstring records that expanding a module is what counts and that discovery must not stop it. [3]
- The case: disjointness from every publication module, then the three non-vacuity checks and the two named witnesses. [4]
- The method limits recorded in the module docstring: static AST graph, `TYPE_CHECKING` excluded, no dynamic imports, per-module rather than process-wide. [5]
- The route this guard exists to keep the stop away from. [6]
- The stop module whose closure is measured, and the release authority the closure is required to reach. [7]
- The lane this module is registered in. [8]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned structural guard.
