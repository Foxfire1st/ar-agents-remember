# mcp/src/agents_remember/tasks/leaf_doc.py

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
`plan_leaf_doc_lifecycle_restamp` (`:256-279`) plans the start/reopen write without mutating
bytes. It returns a candidate when the `lifecycleId` differs **or** when a derived field is
missing (`changed = doc.lifecycleId != lifecycle_id`; `bindings = _derived_leaf_bindings(...)`;
`if not changed and not bindings: return <no candidate>`), so a doc whose `lifecycleId` already
matches but whose master link is absent is a candidate rather than a silent no-op — that
omission was the defect. `restamp_leaf_doc_lifecycle` (`:282-311`) publishes that plan's
candidate through an injected writer, OVERWRITING any previous lifecycle stamp (the enclosure's
newest lifecycle IS the doc's binding), re-rendering the markdown via `write_task_docs`; it
returns a small `{docPath, lifecycleId, changed}` report, or `None` when the leaf has no doc yet
(a first start against an unstarted leaf authors the doc afterwards, already stamped by
`task_doc`).

**`restamp_leaf_doc_lifecycle` has no caller anywhere in `mcp/src` or `mcp/tests` — only its
definition.** The card previously implied it was the live repair path; it is not. Measured with
`grep -rn --include=*.py restamp_leaf_doc_lifecycle mcp/src mcp/tests`, which returns exactly one
line, `mcp/src/agents_remember/tasks/leaf_doc.py:282`. The live bind-at-start publisher is
`plan_leaf_doc_enclosure_registration` (`:351-410`) reached through
`worktrees/task_leaf_binding.py`'s `plan_current_leaf_enclosure_registration` (`:178-202`) from
`_publish_leaf_task_enclosure_binding` (`worktrees/modules/start.py:912-985`), and
`plan_leaf_doc_lifecycle_restamp` is itself reached from start only read-only, as
`_start_restamp_preflight`'s terminal-blocker check (`worktrees/modules/startup/start_contract.py:870-879`).

`_derived_bindings` (`:217-240`) and `_derived_leaf_bindings` (`:243-253`) compute only the ABSENT
derived fields, so an existing binding is never rewired: `seriesContractPath` is
`series_contract_path(task_root).as_posix()` (`task_root/series-contract.md`) and `enclosures` is
the single `{leafId, enclosurePath}` ref naming `leaf_enclosure_path(task_root, leaf_id)`
(`task_root/enclosures/<slugified leaf id>/series-contract.md`), bound only when the leaf id is
nonblank. `plan_leaf_doc_enclosure_registration`'s exact no-op now also requires the link to be
present (`if address_exact and not missing_link and (lifecycle_id is None or ...)`); otherwise its
candidate carries the missing bindings, and `_enclosure_registration_state` (`:331-348`) reports
the new `master-link-missing` state for an exact address whose derived link is absent, keeping
`lifecycle-mismatch` for a reopened leaf and `mismatched`/`missing` for the enclosure itself.

**`require_task_document_in_place(json_path, doc, refusal)` (`:140-156`, MIK-R38 review R1).** The store writes a
document to `json_path_for` its kind and slug, never back to the path it was read from, so a hand-made `light`
leaf saved as `01_x.json`, or a hand-made master saved as `other.json`, is written to the folder's `task.json`,
over the series master. This guard compares the two paths and raises the caller's own refusal type when they
differ, naming both paths and the document's kind and slug. The two terminal writers call it before any write, on
both documents they rewrite: finalize (`worktrees/modules/finalize.py`) on the leaf in `_resolve_task_targets` and
on every master in `_read_parent`, reported as `task-document-resolution-blocked`; reopen
(`worktrees/reopen.py`) on the leaf in `_plan_leaf_doc_reset` and on the master in `_plan_master_index_reset`,
reported as `blocked`. The guard covers every kind, so a `subTask` whose file name differs from its slug is refused
too; correctly placed documents pass unchanged (review R2's read-only sweep of the real task folders refused none of
557 sub-tasks and 39 masters). Rulings 2026-09-30T13:11:32 (leaf side) and 13:35:32 (master side).

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
- **No terminal task-document writer overwrites a document whose read path differs from the store's write target
  for it (MIK-R38).** Finalize and reopen refuse such a leaf or master before any write, through
  `require_task_document_in_place`; the guard reads only `tasks.store`, so the module stays in the task domain.
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
## Evidence

### Repo-Internal References

- The atomic reopen plan refuses a leaf the store would write to another file, then clears the doc's stamp before the next start restamps it. [1]
- The placement guard: the store's write target for the document must be the path it was read from, or the caller's refusal is raised. [2]
- Its four call sites: the leaf and every master in finalize, the leaf and the master in reopen. [3]
- Post-contract start revalidates and publishes the lifecycle restamp through the task-first mutation owner. [4]
- The start/attach publisher that actually binds a missing master link — the live repair path, since `restamp_leaf_doc_lifecycle` has no caller. [5]
- The worktree-side wrapper that resolves the canonical parent row and delegates to this module's enclosure-registration planner. [6]
- Start's read-only restamp preflight, the one `plan_leaf_doc_lifecycle_restamp` caller in `mcp/src`. [7]
- The two derived-field computations: absent-only binding, never a rewire. [8]
- The start/reopen planner that now returns a candidate when only a derived field is missing, and the publisher it feeds. [9]
- The enclosure-registration planner whose exact no-op now requires the derived link, plus the candidate builder and the state classifier that names `master-link-missing`. [10]
- The path helpers this module imports — now from the task domain, which is what keeps the package order intact. [11]
- The worktrees-side re-export surface those helpers used to be imported from, and which still publishes them to its own callers. [12]
- The package order this module's import direction must respect, with no baseline and no exception. [13]
- The armed rail step that runs the layering fitness function on every check — the measurement that found and then confirmed the fix. [14]
- The observer joins this lookup mirrors (doc id → enclosures[] refs → stem). [15]

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
