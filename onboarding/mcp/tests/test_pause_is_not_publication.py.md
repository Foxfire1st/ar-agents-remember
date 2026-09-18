# mcp/tests/test_pause_is_not_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pause_is_not_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `d9becade1a373f2272501f7451746ccc259ca9ac` |
| lastVerifiedCommitDate | 2026-09-18T12:33:45+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The twelve modules the pause must not reach: ref transactions, landings, integrate, record-landing, landing-record, the closeout family and direct landing. | `PUBLICATION_MODULES` | mcp/tests/test_pause_is_not_publication.py:37-52 |
| The measurement: module index, dotted-name resolution, `TYPE_CHECKING`-skipping AST dependency walk, and the one-step direct-import reading. | `_module_files`; `_resolve`; `_is_type_checking`; `_dependencies`; `_runtime_imports_of` | mcp/tests/test_pause_is_not_publication.py:55-65; mcp/tests/test_pause_is_not_publication.py:68-76; mcp/tests/test_pause_is_not_publication.py:79-85; mcp/tests/test_pause_is_not_publication.py:88-106; mcp/tests/test_pause_is_not_publication.py:109-119 |
| The walk itself, whose docstring records that expanding a module is what counts and that discovery must not stop it. | `_runtime_import_closure` | mcp/tests/test_pause_is_not_publication.py:122-153 |
| The case: disjointness from every publication module, then the three non-vacuity checks and the two named witnesses. | `test_the_pause_cannot_reach_any_publication_module`; `_import_path` | mcp/tests/test_pause_is_not_publication.py:156-162; mcp/tests/test_pause_is_not_publication.py:165-202 |
| The method limits recorded in the module docstring: static AST graph, `TYPE_CHECKING` excluded, no dynamic imports, per-module rather than process-wide. | "What it measures is a STATIC, source-level graph" | mcp/tests/test_pause_is_not_publication.py:8-14 |
| The route this guard exists to keep the stop away from. | `worktree_checkpoint_landing` | mcp/src/agents_remember/mcp/registration/closeout.py:172-199 |
| The stop module whose closure is measured, and the release authority the closure is required to reach. | "def pause_result("; "def release_atomic_series_selection(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:31-31; mcp/src/agents_remember/worktrees/modules/pause.py:79-79 |
| The lane this module is registered in. | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:236-236 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned structural guard.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T09:46:27+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 8e3e09b7b677dec09df0166f3450a2d9625d30e9bcf243ce7027ad865fd26365; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_checkpoint_landing` repointed to mcp/src/agents_remember/mcp/registration/closeout.py:172-199. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def pause_result("; "def release_atomic_series_selection(" repointed to mcp/src/agents_remember/worktrees/modules/pause.py:79-79; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:31-31. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T20:42+02:00 — Citation repair only (uncommitted 260831-LOCR change set on
  `ar/260831_lifecycle-owned-completion-relay`): `pause.py` grew from 148 to 209 lines when the
  already-vacant stop was added, so the closure source row was repointed from
  `modules/pause.py:66-109` to `:80-128`, and the lane row from `test-evidence-lanes.toml:184-190` to
  `:191-191` after the new integration row shifted the architecture-fitness block. **No content
  impact**: the pause module's set of imported modules is unchanged — the added
  `observe_atomic_series` import comes from
  `agents_remember.worktrees.activation.atomic_series_activation`, which the module already imported
  for `AtomicSeriesActivationError` — so the measured 60 / 5 / 54 / 0-of-12 closure figures still
  describe this source. They were not re-measured in this pass, and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: created the card for the new architecture-fitness
  guard, against the **final** candidate and therefore against the repaired walker.
  `_runtime_import_closure` now marks a module expanded only when its own imports are read, so the
  closure is genuinely transitive: measured on the frozen candidate it holds 60 modules including the
  root, the pause's direct imports are 5, 54 modules lie beyond them, and 0 of 12 publication modules
  are reached. Recorded the three non-vacuity checks and the two named witnesses, and the mutation
  evidence: the former depth-1 walker returns 6 with 0 deeper modules, so it now fails the case instead
  of passing it. Recorded the method limits the docstring now states — static AST graph,
  `TYPE_CHECKING` branches excluded, function-local imports counted, dynamic imports not followed,
  per-module reachability rather than a process-wide `sys.modules` reading, and why a session-wide
  reading could not be this guard. The "73 modules" figure was retracted at its source (a scratch
  prototype with a different resolver) and is replaced here with the measured 60 / 5 / 54. An earlier
  draft of this card recorded the pre-repair depth-1 behaviour as the shipped behaviour; that reading
  was correct for the candidate it measured and is superseded — this entry is the whole history rather
  than two, because the card was never published in its pre-repair form. Verification metadata remains
  closeout-owned; no acceptance claim.
