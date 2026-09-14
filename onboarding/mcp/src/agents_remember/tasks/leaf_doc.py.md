# mcp/src/agents_remember/tasks/leaf_doc.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/tasks/leaf_doc.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated | 2026-09-14T07:05+02:00 |
| lastVerifiedCommitHash | `dca949f3c1652d76edf277eef86c6399c4ab8404` |
| lastVerifiedCommitDate | 2026-09-14T10:26:38+02:00|
| governingOverview      | `overview.md`                               |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Leaf task-document lookup and lifecycle stamping (L11). A leaf's JSON-primary task
document is the lifecycle-keyed work content of its enclosure; this module makes that
binding survive restarts by explicit restamp — never by read-time heuristics. Since
260913-LCA-L5 it also owns the **derived master link** (`seriesContractPath`,
`enclosures[]`) for a document that was authored before its master's series contract
existed: authoring cannot stamp what does not exist yet, so start is the moment those
fields become writable and both planning paths here bind them.

## Code Commentary

### Logic

`find_leaf_doc(task_root, leaf_id)` scans the task root's `*.json` documents (skipping
masters and unparseable files) and returns the first whose authored `id`, any
`enclosures[]` ref `leafId`, or file stem equals the leaf id case-insensitively — the
same exact joins the observer projection uses, in the same order. The
case-insensitivity matters because doc ids are authored labels (`260628-L11`) while
enclosure leaf ids are lowercase directory names (`260628-l11`).
`plan_leaf_doc_lifecycle_restamp` (`:237-260`) plans the start/reopen write without mutating
bytes. It returns a candidate when the `lifecycleId` differs **or** when a derived field is
missing (`changed = doc.lifecycleId != lifecycle_id`; `bindings = _derived_leaf_bindings(...)`;
`if not changed and not bindings: return <no candidate>`), so a doc whose `lifecycleId` already
matches but whose master link is absent is a candidate rather than a silent no-op — that
omission was the defect. `restamp_leaf_doc_lifecycle` (`:263-292`) publishes that plan's
candidate through an injected writer, OVERWRITING any previous lifecycle stamp (the enclosure's
newest lifecycle IS the doc's binding), re-rendering the markdown via `write_task_docs`; it
returns a small `{docPath, lifecycleId, changed}` report, or `None` when the leaf has no doc yet
(a first start against an unstarted leaf authors the doc afterwards, already stamped by
`task_doc`).

**`restamp_leaf_doc_lifecycle` has no caller anywhere in `mcp/src` or `mcp/tests` — only its
definition.** The card previously implied it was the live repair path; it is not. Measured with
`grep -rn --include=*.py restamp_leaf_doc_lifecycle mcp/src mcp/tests`, which returns exactly one
line, `mcp/src/agents_remember/tasks/leaf_doc.py:263`. The live bind-at-start publisher is
`plan_leaf_doc_enclosure_registration` (`:332-391`) reached through
`worktrees/task_leaf_binding.py`'s `plan_current_leaf_enclosure_registration` (`:178-202`) from
`_publish_leaf_task_enclosure_binding` (`worktrees/modules/start.py:912-985`), and
`plan_leaf_doc_lifecycle_restamp` is itself reached from start only read-only, as
`_start_restamp_preflight`'s terminal-blocker check (`worktrees/modules/startup/start_contract.py:870-879`).

`_derived_bindings` (`:198-221`) and `_derived_leaf_bindings` (`:224-234`) compute only the ABSENT
derived fields, so an existing binding is never rewired: `seriesContractPath` is
`series_contract_path(task_root).as_posix()` (`task_root/series-contract.md`) and `enclosures` is
the single `{leafId, enclosurePath}` ref naming `leaf_enclosure_path(task_root, leaf_id)`
(`task_root/enclosures/<slugified leaf id>/series-contract.md`), bound only when the leaf id is
nonblank. `plan_leaf_doc_enclosure_registration`'s exact no-op now also requires the link to be
present (`if address_exact and not missing_link and (lifecycle_id is None or ...)`); otherwise its
candidate carries the missing bindings, and `_enclosure_registration_state` (`:312-329`) reports
the new `master-link-missing` state for an exact address whose derived link is absent, keeping
`lifecycle-mismatch` for a reopened leaf and `mismatched`/`missing` for the enclosure itself.

### Invariants And Boundaries

- **Still a pure task-domain module, after a defect that was found, measured and fixed.** The module
  imports `tasks.document`, `tasks.readiness`, `tasks.store` and — since 260913-LCA-L5 — `tasks.task_paths`
  (`leaf_enclosure_path`, `series_contract_path` at `:32-35`). An earlier revision of this same change set
  imported those two helpers from `agents_remember.worktrees.task_resolver` instead, and that import
  inverted the declared package order: `layers.toml` ranks `tasks` 9 below `worktrees` 10 with the rule "a
  module in package P may import package Q only when rank(Q) < rank(P)", and declares no baseline and no
  exception. The repository's own layering fitness function
  (`mcp/test_support/agents_remember_test_support/code_quality/layering.py`, run as
  `python -m agents_remember_test_support.code_quality.layering --project-root .`) reported
  `layering violation: tasks -> worktrees (mcp/src/agents_remember/tasks/leaf_doc.py:32)` and
  `layering cycle: tasks <-> worktrees`, and exited 1. The defect is recorded here rather than erased
  because it was found by measurement, and the measurement is what fixed it. The fix moved the path rules
  DOWN into the task domain (`tasks/task_paths.py`, see that card) and `worktrees/task_resolver.py` now
  re-exports them, so no `tasks -> worktrees` edge exists anywhere under `tasks/` (`grep -rn
  --include=*.py "from agents_remember.worktrees" mcp/src/agents_remember/tasks/` returns nothing) and the
  same checker reports 16 violations and 1 cycle — the `memory_quality <-> worktrees` cycle — with no
  tasks-related finding, which is exactly the base state. One honest qualification, kept from the
  measurement: the layering rail already failed at base (15 pre-existing `worktrees -> memory_quality`
  violations plus that cycle), so the defect added a violation to an already-red rail rather than turning
  a green one red, and the fix returns the rail to that same red, not to green.
- Restamp is idempotent (`changed: false` when the stamp already matches **and** no derived field
  is missing) and total (overwrites a stale finalized-lifecycle stamp — a reopened leaf's doc must
  follow the fresh lifecycle, not the old one). Idempotency is now conditional rather than
  absolute: a document that is missing its master link is deliberately *not* a no-op.
- The derived binding is additive by construction: `_derived_bindings` fills only fields that are
  absent, so a start can never rewire an existing `seriesContractPath` or `enclosures[]`, and a
  repair preserves the document's authored objective, requirements, steps and title.
- Since 260815-DAG-L16 `resolve_terminal_leaf_doc` names the missing binding and the recovery
  (L16-R9): a blank leaf id refuses with "the leaf has no stamped contract binding — re-stamp the
  series contract (series-contract.md) or use branch-addressed mode for direct execution" instead
  of the opaque "terminal leaf resolution requires a nonblank leaf id".
## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The atomic reopen plan clears the doc's stamp before the next start restamps it. | `_plan_leaf_doc_reset` | mcp/src/agents_remember/worktrees/reopen.py:427-468 |
| Post-contract start revalidates and publishes the lifecycle restamp through the task-first mutation owner. | `_create_start_enclosure` | mcp/src/agents_remember/worktrees/modules/start.py:686-718 |
| The start/attach publisher that actually binds a missing master link — the live repair path, since `restamp_leaf_doc_lifecycle` has no caller. | `_publish_leaf_task_enclosure_binding` | mcp/src/agents_remember/worktrees/modules/start.py:912-985 |
| The worktree-side wrapper that resolves the canonical parent row and delegates to this module's enclosure-registration planner. | `plan_current_leaf_enclosure_registration`; `require_current_leaf_enclosure_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:178-202; mcp/src/agents_remember/worktrees/task_leaf_binding.py:205-256 |
| Start's read-only restamp preflight, the one `plan_leaf_doc_lifecycle_restamp` caller in `mcp/src`. | `_start_restamp_preflight`; `_start_will_restamp` | mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:870-879; mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:862-867 |
| The two derived-field computations: absent-only binding, never a rewire. | `_derived_bindings`; `_derived_leaf_bindings` | mcp/src/agents_remember/tasks/leaf_doc.py:198-221; mcp/src/agents_remember/tasks/leaf_doc.py:224-234 |
| The start/reopen planner that now returns a candidate when only a derived field is missing, and the publisher it feeds. | `plan_leaf_doc_lifecycle_restamp`; `restamp_leaf_doc_lifecycle` | mcp/src/agents_remember/tasks/leaf_doc.py:237-260; mcp/src/agents_remember/tasks/leaf_doc.py:263-292 |
| The enclosure-registration planner whose exact no-op now requires the derived link, plus the candidate builder and the state classifier that names `master-link-missing`. | `plan_leaf_doc_enclosure_registration`; `_enclosure_registration_candidate`; `_enclosure_registration_state` | mcp/src/agents_remember/tasks/leaf_doc.py:332-391; mcp/src/agents_remember/tasks/leaf_doc.py:295-309; mcp/src/agents_remember/tasks/leaf_doc.py:312-329 |
| The path helpers this module imports — now from the task domain, which is what keeps the package order intact. | `series_contract_path`; `leaf_enclosure_path`; `leaf_enclosure_dir` | mcp/src/agents_remember/tasks/task_paths.py:31-34; mcp/src/agents_remember/tasks/task_paths.py:43-46; mcp/src/agents_remember/tasks/task_paths.py:37-40 |
| The worktrees-side re-export surface those helpers used to be imported from, and which still publishes them to its own callers. | `task_resolver.py` module surface | mcp/src/agents_remember/worktrees/task_resolver.py:21-49 |
| The package order this module's import direction must respect, with no baseline and no exception. | "a module in package P may import package Q only when rank(Q) < rank(P)" | layers.toml:25-25 |
| The armed rail step that runs the layering fitness function on every check — the measurement that found and then confirmed the fix. | `_layering_step` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:310-319 |
| The observer joins this lookup mirrors (doc id → enclosures[] refs → stem). | "def read_task_documents(" | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:126-126 |

## 260815-DAG-L3 Governed Lifecycle Restamp

`restamp_leaf_doc_lifecycle` now plans the same exact leaf-doc change but delegates publication to
an injected writer. Worktree start supplies the queue-governed task-fact publisher, so lifecycle
restamping cannot bypass an active sprint lane or atomic blocker; standalone tests can inject the
ordinary task-doc writer without duplicating policy.

## CCR-L42 current candidate

Leaf documents now include `LeafEnclosureRegistrationPlan` and exact parent-row registration planning. Missing or mismatched bindings produce typed task-document repair facts before closeout rather than sibling scans or path-name inference.

## 260913-LCA-L5 Derived-Binding And The Docstring Premise It Replaced

Planning a master necessarily authors its leaf documents **before** the master's first
`worktree_start` bootstraps the series contract, so at authoring time `task_doc` cannot stamp
`seriesContractPath` or `enclosures[]`, and this master's own first leaf was born with
`seriesContractPath: None` because of it. Nothing could repair it: `set_field` refused the field
name, `create` refused an existing document, and `plan_leaf_doc_lifecycle_restamp` returned no
candidate whenever `lifecycleId` already matched.

The change makes both planning paths in this module bind only the ABSENT derived fields, and
replaces the docstring premise that broke. The old text of `restamp_leaf_doc_lifecycle` said a
first start "finds the doc afterwards, already stamped by `task_doc`"; what actually holds is that
the doc may predate the series contract, so start binds the fields that could not exist at
authoring time. The corrected function docstring now says exactly that.

Two things a reader must not mis-take from this change:

1. **`restamp_leaf_doc_lifecycle` is dead code.** It has no caller in `mcp/src` or `mcp/tests`
   (one grep hit: its own definition). It was *not* the repair path before this change and it is
   not one now. The live publisher is `plan_leaf_doc_enclosure_registration`, reached from
   `_publish_leaf_task_enclosure_binding` through
   `plan_current_leaf_enclosure_registration`; the restamp planner is reached from start only as a
   read-only terminal-blocker preflight.
2. **A document with an exact enclosure address but no `seriesContractPath` now REFUSES closeout
   by name** (`task-enclosure-binding-master-link-missing`, raised by
   `worktrees/task_leaf_binding.py`) instead of passing silently. That is the intended,
   load-bearing half of the change — it is what forced the fixture corrections in
   `test_closeout_queue.py` and `test_transaction_only_worktree_delivery.py`, which had been
   modelling the damage state — and it is a deliberate consequence, not an accident to be
   documented away.

### The Layer Inversion This Change Set Introduced, And How It Was Resolved

The first revision of this change bound the derived fields by importing `leaf_enclosure_path` and
`series_contract_path` from `agents_remember.worktrees.task_resolver`. The curation pass measured the
repository's own layering fitness function against that revision and found `tasks -> worktrees
(tasks/leaf_doc.py:32)` plus a `tasks <-> worktrees` package cycle: 17 violations and 2 cycles, against
16 and 1 for the same tree with only those import lines deleted. `layers.toml` forbids the edge
(`tasks` rank 9, `worktrees` rank 10, no baseline, no exception) and the `layering` step is armed in the
ordered rail plan, so the finding was load-bearing rather than cosmetic.

The resolution moved the rules DOWN instead of having `tasks` reach up:

- `mcp/src/agents_remember/tasks/task_paths.py` is new and now holds the single definition of
  `SERIES_CONTRACT_FILENAME`, `ARCHIVE_DIR`, `ENCLOSURES_DIR`, `slugify`, `series_contract_path`,
  `leaf_enclosure_dir`, `leaf_enclosure_path`, `is_archived_path`, `is_enclosure_contract` and
  `iter_leaf_enclosure_contracts`. Verified structurally: each of those ten names has exactly one
  definition site in all of `mcp/src`, and it is in this file.
- `worktrees/task_resolver.py` imports all ten and re-exports them under an explicit `__all__` of 19
  names, redefining none of them, so it stays the published import site for its existing callers while
  the definition sits below `worktrees`.
- This module imports the two helpers from `tasks.task_paths`, so no `tasks -> worktrees` import remains
  anywhere under `tasks/`.

Re-measured after the fix with the same command from the leaf root: exit 1, **16 violations and 1
cycle** (`memory_quality <-> worktrees`), with no `tasks`-related finding at all — the base state, since
those 16 are pre-existing and the rail was already red before this change set existed. `layers.toml` is
untouched, and there is no `# noqa`, per-file ignore or widened limit anywhere in the resolution.

## Update History
- 2026-09-14T10:16+02:00 — 260913-LCA-L10 curator: re-anchored one citation into `snapshots_impl/_task_documents.py` after that file grew by 52–57 lines for the tolerant read edge (`read_task_documents` moved 69-69 → 126-126; the cited file changed, this card's own source did not). The observer join this row records is unchanged. Verification metadata unchanged; no verification stamp advanced.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): corrected the false premise this card carried and recorded the derived-binding fix. The
  Purpose, Logic and Invariants sections now state that planning authors leaf docs before the series
  contract exists, that both planning paths bind only the ABSENT derived fields, and that
  `plan_leaf_doc_lifecycle_restamp` returns a candidate when only a derived field is missing while
  `plan_leaf_doc_enclosure_registration`'s exact no-op now requires the link (new `master-link-missing`
  state). Stated plainly that `restamp_leaf_doc_lifecycle` has **no caller** in `mcp/src`/`mcp/tests` and
  is not the live repair path — the start/attach publisher is — because the previous text implied
  otherwise. Recorded the layer inversion this change set first introduced (`tasks -> worktrees` from
  `leaf_doc.py:32` plus a `tasks <-> worktrees` cycle, measured with the repository's own layering fitness
  function at 17 violations / 2 cycles against a 16/1 base) **and its resolution**, so the defect stays
  visible as history rather than being erased: the path rules moved down into the new
  `tasks/task_paths.py`, `worktrees/task_resolver.py` re-exports them, this module imports from
  `tasks.task_paths`, and the re-measured tree is back to 16 violations / 1 cycle with no tasks-related
  finding. Repaired the "pure task-domain module" invariant accordingly — it is true again, with
  `tasks.task_paths` added to the import list — and added eleven reference rows plus one pre-existing
  stale range repair (`_plan_leaf_doc_reset` 393-436 → 427-468). Verification metadata is **not**
  advanced: the code commit does not exist and closeout owns the stamp; no execution or acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_create_start_enclosure` repointed to mcp/src/agents_remember/worktrees/modules/start.py:686-718. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Leaf documents now include `LeafEnclosureRegistrationPlan` and exact parent-row registration planning. Missing or mismatched bindings produce typed task-document repair facts before closeout rather than sibling scans or path-name inference.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `resolve_terminal_leaf_doc` blank-id refusal now names
  the missing binding and the recovery (L16-R9: re-stamp the series contract / use
  branch-addressed mode). Verified at code commit a9d50e08.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented publisher injection for queue-governed
  leaf lifecycle restamping; verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: updated the reopen reference to the current atomic
  `_plan_leaf_doc_reset` owner; leaf lookup and restart stamping remain unchanged. Verification
  remains closeout-owned.
- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-03T00:30+02:00 — Created for L11: exact case-insensitive leaf-doc lookup plus the explicit
  lifecycleId restamp worktree_start applies after (re)creating a leaf whose doc already exists.
  Verification metadata pinned until closeout stamps the code commit.