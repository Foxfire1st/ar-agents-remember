# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T15:05+02:00 |
| lastVerifiedCommitHash | `96bfe755d2b605d42a9d001714cc7d8eb592a073` |
| lastVerifiedCommitDate | 2026-09-14T15:15:20+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Classifies 202 retained test-shaped modules into explicit evidence categories: 114 unit-regression, 2 public-contract, 57 integration, 16 architecture-fitness and 13 provider-conformance; stress-durability and migration are empty. The focused terminal-evidence cursor suite `test_terminal_evidence_cursors.py` and the parked-external-await separation guard `test_parked_external_await_separation.py` are unit-regression members, and 260831-LOCR-L32 added `test_worktree_status_terminal_next_tool.py` to the **integration** lane (row 175; it drives real worktree services and a real repository under `tmp_path`), while 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py` to that same lane (row 132; it drives the public checkpoint/closeout operations over real temporary Git repositories), and 260831-LOCR-L36 added `test_cross_master_concurrency.py` to that lane as well (row 143; it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world), while 260831-LOCR-L37 added `test_pause_stop_only_end_to_end.py` to that same lane (row 159; it drives the public pause over one real temporary Git world holding two atomic masters and measures refs, object databases, coordination tree, worktrees and task documents before and after) **and** `test_pause_is_not_publication.py` to **architecture-fitness** (row 191; it is an AST-only import-closure guard that executes nothing), and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to **integration** (row 153; it plays the whole leaf-and-master lifecycle in order over one real temporary Git world and is the regression proof for the deleted child-admission seal). The 260913-LCA-L7 change set added one more integration member,
`test_closeout_projection_source_classification.py` (entry row 137) — it composes the real
`QueueFixture` over temporary Git repositories and drives the production graph admission and
projection path through `graph_context` and `capture_projection_source`, so that is its
behaviour-preserving lane — bringing the manifest to 205 rows. The insertions split the alphabetical run again, so the integration lane now carries 57 entries closing at entry row 182, architecture-fitness carries 16 entries at rows 185-200, provider-conformance 13 entries at rows 203-215, and stress-durability and migration remain empty. The population had earlier fallen below its historical peak because the de-entanglement cut deleted four integration modules — `test_integration_ref_transaction.py`, `test_worktree_integrate_quality_gate.py`, `test_closeout_memory_certification_reuse.py` and `test_prepared_publication_recovery.py` — and the 188 rows this manifest held before 260831-LOCR-L30 were that reduced set; the eight rows added by that leaf brought it to 196, L32's row to 197, L34's to 198, L36's to 199, and L37's two to 201. Every `mcp/tests/test_*.py` module on disk is listed exactly once and no path is duplicated — 202 modules, 202 manifest entries. File counts are not collected-case counts, and the lane bracket is the unit of accounting: unit-regression is the default delivery lane, while the integration lane is capped at 250 collected cases (`pyproject.toml:150`; 260831-LOCR-L37 raised it 200 -> 250 on explicit developer authorization, and both the 150 and the 200 figures recorded in earlier entries of this card are stale). The closeout auto-carry change registered one new module, `test_sync_parked_candidate.py`, in the existing `unit-regression` lane, and the L28 leaf registered its boundary-delivery module `test_state_signal_boundary_delivery.py` in that same lane; the per-lane counts above are the current source membership.

260831-LOCR-L30 registered eight members and, in doing so, repaired a manifest that could not load at
all. `load_lane_manifest` independently proves the declared population closed — it derives the
repository's actual test modules and refuses a manifest that omits one — so an unregistered module is
a **hard load failure**, not a silent gap. Seven tracked `test_*.py` modules (one of them,
`test_record_landing.py`, shipped by the immediately preceding leaf) had no lane row, which made every
manifest consumer fail rather than mis-classify. The eight rows are `test_checkpoint_landing.py`,
`test_closeout_kept_rules_pins.py`, `test_memory_scope_task_derivation.py`,
`test_post_integration_cleanup_guidance.py`, `test_record_landing.py`,
`test_retired_door_publication_fields.py` and `test_automatic_post_integration_cleanup.py` in the
existing lanes, plus `test_memory_quality_is_independent_of_the_closeout_plane.py` in
`architecture-fitness`. Each took its behaviour-preserving lane: the six new unit-regression rows are
hermetic focused suites and the integration lane is capped at 200 collected cases
(`pyproject.toml:135`; the "150" this card's earlier entries recorded is stale), so nothing was
moved into it beyond the one module that genuinely exercises an integration boundary.
## 260913-LCA-L4 Pending Lane Row (Open At L4, Resolved Since)

**Resolved — see the L5 section below.** At the L4 change set the manifest was one row short.

The L4 change set added `mcp/tests/test_memory_attribution_producers.py` and did **not** register it in
this manifest, so the closed population the `Logic` section below describes does not hold for that
change set. Measured at base `5bb124d4` plus that change set, by diffing the file list against the
manifest:

- 203 `mcp/tests/test_*.py` modules exist on disk; the manifest declares 202 (114 unit-regression, 2
  public-contract, 57 integration, 16 architecture-fitness, 13 provider-conformance, 0 stress-durability,
  0 migration).
- The single undeclared path is `mcp/tests/test_memory_attribution_producers.py` — the one file in the
  disk set with no manifest row — and there is no stale row naming a file that is gone.

This is not a documentation gap but the hard failure this card already records from 260831-LOCR-L30:
`load_lane_manifest` derives the repository's actual test modules and refuses a manifest that omits one.
The derivation reaches the new module — `testpaths = ["mcp/tests"]` in the repository-root
`pyproject.toml:155` puts it inside the test roots, and its `test_` prefix classifies it as a test module
— and `mcp/test_support/agents_remember_test_support/code_quality/check.py:677` is a manifest consumer, so
every consumer fails rather than mis-classifying. The lane the module belongs in is the builder's call and
is **not** asserted here: the module is hermetic except for its two cases that compose `QueueFixture` over
real temporary Git repositories. The row is recorded as pending so the next reader finds the gap rather
than a claim of completeness.

## 260913-LCA-L5 Lane Row (Declared)

**Superseding the L4 section above, the manifest is closed again.** Measured at base `52875e7a` by
diffing the disk file list against the manifest, the L4 module `test_memory_attribution_producers.py`
does have its lane row (line `:68`, `unit-regression`, added by the commit that landed L4), so the
203-modules/203-entries population held at this leaf's base and the open gap the L4 section records is
resolved.

The L5 change set adds `mcp/tests/test_leaf_doc_master_link_binding.py` **and** its row in the same
change, so the population stays closed at 204 modules on disk and 204 manifest entries. The row is
`mcp/tests/test-evidence-lanes.toml:152`, in the **integration** lane: it drives the real public
`worktree_start` over one disposable code repository and one external memory repository per case, so it
is a boundary executor rather than a hermetic unit — that is its behaviour-preserving lane.

Measured current brackets, by entry row: unit-regression 115 entries at rows 6-120, public-contract 2
at 123-124, integration 58 at 127-184, architecture-fitness 16 at 187-202, provider-conformance 13 at
205-217, stress-durability and migration empty. The Purpose paragraph above carries the pre-L4 counts
(202 modules, 114 unit-regression, 57 integration) and is superseded by these; the insertion at `:152`
shifted every integration entry after it and both later lane blocks by one.

## 260913-LCA-L7 Lane Row (Declared)

The L7 change set adds `mcp/tests/test_closeout_projection_source_classification.py` **and** its row in
the same change, so the manifest stays closed at 205 modules on disk and 205 manifest entries — the L5
population was 204 and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:137`, in the **integration** lane: the module composes the real
`QueueFixture` over temporary Git repositories and drives the production graph admission and projection
path, so it is a boundary executor rather than a hermetic unit — that is its behaviour-preserving lane.
The manifest is also a fail-closed input here, not a list of cases: `test_closeout_queue.py` is a
one-to-one sidecar source whose card describes a shared fixture with no retained standalone queue tests,
and this new module is a real consumer of that fixture rather than a rename or replacement of it. No
existing row moved and no existing row changed lane: the insertion at `:137` sits inside the
alphabetical integration run and pushes only the later line numbers down by one.

Measured current brackets, by entry row: unit-regression 115 entries at rows 5-120, public-contract 2
at 122-124, integration 59 at 126-185, architecture-fitness 16 at 187-203, provider-conformance 13 at
205-218, stress-durability and migration empty. The Purpose paragraph above carries the pre-L4 counts
(202 modules, 114 unit-regression, 57 integration) and the L5 section carries the 204-module brackets;
both are superseded by these measured ones. The insertion at `:137` sits before entries that this card
cites, so each of those rows is one line higher than the L5 section recorded it:
`test_leaf_doc_master_link_binding.py` `:152` → `:153`, `test_lifecycle_playthrough_end_to_end.py`
`:155` → `:156`, `test_pause_stop_only_end_to_end.py` `:161` → `:162`,
`test_worktree_status_terminal_next_tool.py` `:181` → `:182`, and
`test_pause_is_not_publication.py` `:193` → `:194`; the unit-lane
`test_memory_attribution_producers.py` row at `:68` and every row above the insertion are unchanged.

## 260913-LCA-L8 Lane Row (Declared)

The L8 change set adds `mcp/tests/test_terminal_blocker_reasons.py` **and** its row in the same
change, so the manifest stays closed at 206 modules on disk and 206 manifest entries — the L7
population was 205 and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:177`, in the **integration** lane: the module builds a real landed
leaf over disposable code and external-memory repositories, completes the integration through the
public `worktree_integrate_tool`, and drives the public `lifecycle_finalize_task_tool` plus a real
permission failure on the provider-runtime tree, so it is a boundary executor rather than a hermetic
unit — that is its behaviour-preserving lane.

Measured current brackets, by entry row: unit-regression 115 entries at rows 5-120, public-contract 2
at 122-124, integration 60 at 126-186, architecture-fitness 16 at 188-204, provider-conformance 13 at
206-219, stress-durability and migration empty. The L7 section above carries the 205-module brackets
and the Purpose paragraph carries the pre-L4 counts; both are superseded by these measured ones.

The insertion at `:177` also corrects three out-of-order entries that the earlier insertions had left
behind in the closeout-input consumer list: `test_cross_master_concurrency.py` moves after
`test_context_packet.py` (`:309` → `:312`), `test_lifecycle_finalize.py` after
`test_leaf_doc_master_link_binding.py` (`:315` → `:316`) and `test_memory_attribution_producers.py`
after `test_mcp_stdio_transport.py` (`:319` → `:320`). That is why the L5 row moves **up** one line
(`:316` → `:315`) while the L4 row moves down one (`:319` → `:320`). No existing row changed lane. Two
rows this card cites sit after the insertion and are one line higher than the L7 section recorded
them: `test_worktree_status_terminal_next_tool.py` `:182` → `:183` and
`test_pause_is_not_publication.py` `:194` → `:195`; `test_pause_stop_only_end_to_end.py` `:162`, the
playthrough `:156`, the L7 row `:137` and the L4 row's lane are unchanged.

## Code Commentary

### Logic



Paths are explicit and unique. The root conftest reads integration/stress membership once to avoid
integration imports in default unit runs and marks selected integration items. The
`test_terminal_evidence_cursors.py` row owns the focused deque-envelope, unsupported-harness,
bounded-Pi, and liveness-containment checks for the terminal-evidence lift. Other categories
retain their classification meaning without requiring separate copies or historical edge suites.
A test-shaped helper module may remain listed for dependency classification even when it contains
no test functions; importability is not a passing test.

`load_lane_manifest` independently proves the declared population closed: it derives the
repository's actual test modules and refuses a manifest that omits a module or declares a stale
row, so an unregistered module is a hard load failure rather than a silent gap. Three modules
created by the CCR transaction-only closeout reform (`test_review_state.py`,
`test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) were left
unregistered by the commit that created them, and the checking hooks that would have caught the
omission were later removed from closeout, so the gap survived until the manifest was explicitly
repaired. All three are registered as `unit-regression`, which is behaviour-preserving: they had
been running unmarked and therefore already counted as unit, and the integration lane sat at its
hard cap of 150 collected cases, so an `integration` row would have overflowed the cap and raised
during collection. Registration here is classification only; it is never execution or acceptance
evidence.

`test_dagger_registry_lock.py`, the registered activation/admission proof, the registered
route-review transport proof, and actual document/publication/durability boundaries are integration
members. The R28 `test_terminal_liveness_deferred_work.py` module is a unit-regression member: it is
hermetic (temporary catalogs, in-process `unittest` classes, no `worktree_services` use) even though
it exercises the real catalog/sweeper post-commit ordering and failure boundaries. The new diagnostic
quality, selected-case-budget and canonical terminal-evidence mapping tests are unit-regression members,
as is `test_sync_parked_candidate.py`. Three pre-existing CCR modules (`test_review_state.py`,
`test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) were created by `8885939e`
in the same change that edited this manifest, but their required rows were omitted; the missing
`unit-regression` rows were restored so the manifest loads and no retained module stays unclassified.
A full run previously collected all three unmarked, so `unit-regression` is their behaviour-preserving
lane. Adding the parked-candidate row shifted every later lane block, so its citations were re-derived.
The executable case budgets live in pyproject/conftest, not in this list. Coverage percentages are
diagnostic and cannot require restoring deleted entries.

The current manifest is complete and duplicate-free: every `mcp/tests/test_*.py` module on disk is
listed exactly once, and every listed path exists. Three formerly unlisted modules
(`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`)
were created by the CCR transaction-only delivery commit and omitted from this manifest in the same
change; they ran unmarked rather than in an explicit lane. They are registered in `unit-regression`,
which is the behaviour-preserving lane for an unmarked module, because moving them to `integration`
would push that lane past its 150-case cap. The same three rows also reached this series branch with
the LOCR-L28 landing. That repair is repo-hygiene and is not part of any LOCR requirement.

`test_cross_master_concurrency.py` (260831-LOCR-L36) is an **integration** member, and that is its
behaviour-preserving lane: it builds one real temporary Git world per case — disposable code and
external-memory repositories, real series/leaf contracts, a real ledger — and drives the public
activation, checkpoint-landing and integration operations against it, so it is a boundary executor
rather than a hermetic unit. It is the forcing module for the contract-scoped activation record: two
atomic masters commanded by one sprint share one protected source pair, so the module can prove both
progress independently and that a sibling's pause blocks nobody. Registration is classification only;
it is never execution or acceptance evidence.

### Invariants And Boundaries

- Unknown, duplicate or conflicting file classification must not silently acquire authority.
- Every current `mcp/tests/test_*.py` module holds exactly one explicit lane; an unlisted module is a
  manifest defect, and its behaviour-preserving lane is the default unit lane rather than the capped
  integration lane.
- Evidence class is separate from whether a test invokes a real external producer.
- Current source membership governs; old final-Codex executor/status-wait/deleted-edge lists do not.
- Host development pytest is supported; only explicit certification requires Dagger admission.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1000, `integration_case_budget` 250 — `pyproject.toml:149-150`; the 150 and 200 values in earlier entries of this card are stale). A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1000 and `integration_case_budget` 250 (root `pyproject.toml:149-150`), enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-120 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:126-186 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:188-204 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:206-219 |
| Empty former stress/migration populations | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:221-221; mcp/tests/test-evidence-lanes.toml:223-223 |
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:126-126 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:221-221 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:98-98 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:24-24 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 183 now, after the L4, seal-removal, L5, L7 and L8 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:183-183 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 133 now, after the L4, L5, L7 and L8 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:133-133 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 145 now, after the L4, L5 and L7 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:145-145 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 162 now, after the L4, seal-removal, L5 and L7 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:162-162 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 195 now, after the L4, seal-removal, L5, L7 and L8 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:195-195 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 156 now, after the L4, L5 and L7 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:156-156 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:68-68 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:153-153 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 137) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:137-137 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 177) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:177-177 |
| The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value. | "integration_case_budget = 250" | pyproject.toml:150-150 |
| The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-144 |
## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History
- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
  registered the change set's new `mcp/tests/test_terminal_blocker_reasons.py` in the **integration**
  lane (entry row 177) — it builds a real landed leaf over disposable code and external-memory
  repositories and drives the public landing, integration and `lifecycle_finalize_task` routes, so
  that is its behaviour-preserving lane — and reconciled the population and every lane bracket against
  the current manifest, measured rather than carried: 206 modules on disk and 206 manifest entries,
  115 unit-regression (5-120), 2 public-contract (122-124), 60 integration (126-186), 16
  architecture-fitness (188-204), 13 provider-conformance (206-219), with stress-durability and
  migration empty. The same change set also corrected three out-of-order consumer entries in
  `evidence-lifecycle.toml`, which moves the L5 row up one line (`:316` → `:315`) and the L4 row down
  one (`:319` → `:320`) without changing any lane. Two rows this card cites after the insertion are
  one line higher than the L7 entry recorded: `test_worktree_status_terminal_next_tool.py`
  `:182` → `:183` and `test_pause_is_not_publication.py` `:194` → `:195`; re-derived the bracket rows
  (`126-185` → `126-186`, `187-203` → `188-204`, `205-218` → `206-219`, the empty-lane keys
  `220-220`/`222-222` → `221-221`/`223-223`) and corrected two rows that were already one line short
  of their entries (`test_checkpoint_landing_end_to_end.py` `:132` → `:133` and
  `test_cross_master_concurrency.py` `:143` → `:145`). Classification only: lane membership is not
  execution or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-14T14:20+02:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  registered the change set's new `mcp/tests/test_closeout_projection_source_classification.py` in the
  **integration** lane (entry row 137) — it composes the real `QueueFixture` over temporary Git
  repositories and drives the production graph admission and projection path, so that is its
  behaviour-preserving lane — and reconciled the population and every lane bracket against the current
  manifest, measured rather than carried: 205 modules on disk and 205 manifest entries, 115
  unit-regression (5-120), 2 public-contract (122-124), 59 integration (126-185), 16 architecture-fitness
  (187-203), 13 provider-conformance (205-218), with stress-durability and migration empty. The single
  insertion sits before rows this card cites, so each of them is one line higher than the L5 entry
  recorded: `test_leaf_doc_master_link_binding.py` `:152` → `:153`, the playthrough `:155` → `:156`, the
  pause suite `:161` → `:162`, the L32 suite `:181` → `:182` and the pause architecture guard `:193` →
  `:194`, with the integration bracket `126-184` → `126-185`; added the L7 registration row and the
  reference row for it, and left every per-leaf section above as its own as-of record. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): registered the change set's new `mcp/tests/test_leaf_doc_master_link_binding.py` in the
  **integration** lane (entry row 152) — it drives the real public `worktree_start` over one disposable
  code repository and one external-memory repository per case, so that is its behaviour-preserving lane —
  and reconciled the population and every lane bracket against the current manifest, measured rather than
  carried from the previous entry: 204 modules on disk and 204 manifest entries, 115 unit-regression
  (entry rows 6-120), 2 public-contract (123-124), 58 integration (127-184), 16 architecture-fitness
  (187-202), 13 provider-conformance (205-217), with stress-durability and migration empty. **Also
  corrected the L4 section, which recorded an open gap that no longer exists**: measured at base
  `52875e7a`, `test_memory_attribution_producers.py` holds its lane row at `:68` in `unit-regression`, so
  the 203-modules/203-entries population held at this leaf's base and the fail-closed load failure the L4
  entry predicted was already repaired by the commit that landed L4. Re-derived every position this card
  cites against the current manifest by line number (integration `126-184`, architecture-fitness
  `186-202`, provider-conformance `204-217`, stress-durability `:219`, migration `:221`, the L38 row
  `:126`, `test_state_signal_boundary_delivery.py` `:98`, `test_worktree_status_terminal_next_tool.py`
  `:181`, the pause suite `:161`, the pause architecture guard `:193`, the playthrough `:155`) and added
  the L4 and L5 registration rows. The Purpose paragraph above carries pre-L4 counts and is superseded by
  the measured ones; classification only, lane membership is not execution or acceptance evidence, and
  the verification stamps remain closeout-owned.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`, base
  `5bb124d4`): **flagged an open gap rather than repairing it, because the file itself is unchanged and
  the repair is code work.** The change set added `mcp/tests/test_memory_attribution_producers.py` and
  declared no lane row for it, so the manifest's closed population no longer holds: measured by diffing
  the disk file list against the manifest, 203 `test_*.py` modules exist and 202 are declared, the one
  undeclared path being the new module, with no stale row pointing at a missing file. Because
  `load_lane_manifest` refuses a manifest that omits a module, this is the same hard load failure the
  card already records from 260831-LOCR-L30, and `code_quality/check.py:677` is a consumer. Recorded in
  a new section with the measurement method, the derivation path (`testpaths` in the repository-root
  `pyproject.toml:155`), the consumer that fails, and the explicit statement that the lane choice is the
  builder's and is not asserted here. The manifest file itself is **not** modified by this curator pass.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the change set's new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` in the **integration** lane (entry row 153) —
  it plays the whole leaf-and-master lifecycle in order over one real temporary Git world through the
  public master-level operations, so that is its behaviour-preserving lane — and reconciled the
  population and every lane bracket against the current manifest, measured rather than carried from the
  previous entry: 202 modules on disk and 202 manifest entries, 114 unit-regression (entry rows 6-119),
  2 public-contract (122-123), 57 integration (126-182), 16 architecture-fitness (185-200), 13
  provider-conformance (203-215), with stress-durability and migration empty. The insertion shifted the
  three later rows this card cites (`test_worktree_status_terminal_next_tool.py` 178 → 179, the pause
  boundary suite 158 → 159, the pause architecture guard 190 → 191) and every lane bracket after
  integration. Also corrected two stale invariant bullets that still declared
  `integration_case_budget` as 200 at `pyproject.toml:134-135`; the measured source reads 250 at
  `pyproject.toml:150`, which the L37 entry had already recorded for the reference row. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "stress-durability"; "migration" repointed to mcp/tests/test-evidence-lanes.toml:216-216; mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:178-178. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "integration_case_budget" repointed to pyproject.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
  projection): re-read the `integration_case_budget` claim against the current `pyproject.toml` and
  re-cited it to the key's own line, `pyproject.toml:150-150`, where the declared integration ceiling of
  250 now lives. The wording ("the integration lane's collected-case cap that constrains lane choice")
  holds: the cap is the reason the L37 additions and the L30/L34 restorations were classified as they
  were. The previous range arrived from a generated projection and is superseded by this curator
  confirmation.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: registered the leaf's two new modules —
  `mcp/tests/test_pause_stop_only_end_to_end.py` in the **integration** lane (entry row 158) because
  it drives the public pause over a real temporary Git world holding two atomic masters, and
  `mcp/tests/test_pause_is_not_publication.py` in **architecture-fitness** (entry row 190) because it
  is an AST-only import-closure guard that executes nothing. Reconciled the population and every lane
  bracket against the current manifest, measured rather than carried from the previous entry: 201
  modules on disk and 201 manifest entries, 114 unit-regression (entry rows 6-119), 2 public-contract
  (122-123), 56 integration (126-181), 16 architecture-fitness (184-199), 13 provider-conformance
  (202-214), with stress-durability and migration empty. Also corrected the stale cap sentence: the
  integration lane is capped at 250 collected cases (`pyproject.toml:150`), not 200. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.
- 2026-09-13T14:20:09+02:00 — 260831-LOCR-L36 curator: registered the leaf's new `mcp/tests/test_cross_master_concurrency.py` in the **integration** lane (row 143) — it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world, so that is its behaviour-preserving lane — and reconciled the population and every lane bracket against the current manifest: 199 modules, 114 unit-regression (5-120), 2 public-contract (121-124), 55 integration (125-181), 15 architecture-fitness (182-198), 13 provider-conformance (199-213), with stress-durability (214-215) and migration (216-217) empty. The insertion shifted the L32 row (176 → 177) and every bracket after the integration block, all re-cited here. Classification only: lane membership is not execution or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:12+00:00 — 260831-LOCR-L34 curator: registered the leaf's new
  `mcp/tests/test_checkpoint_landing_end_to_end.py` in the **integration** lane (row 132) — it drives
  the public checkpoint and closeout operations over real temporary Git repositories under
  `tmp_path`, so that is its behaviour-preserving lane — and re-derived the population and every lane
  bracket against the current manifest: 198 modules, 114 unit-regression (5-120), 2 public-contract
  (121-124), 54 integration (125-180), 15 architecture-fitness (181-197), 13 provider-conformance
  (198-212), with stress-durability (213-214) and migration (215-215) empty. The insertion shifted the
  L32 row (175 → 176) and every later lane bracket, all re-cited here; also replaced the last stale
  "150 collected cases" bound in the L30 paragraph with the measured 200. Classification only: lane
  membership is not execution, certification or acceptance evidence, and verification metadata remains
  closeout-owned.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: registered the leaf's new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` in the **integration** lane (row 175) — it
  drives real worktree services and a real repository under `tmp_path`, so that is its
  behaviour-preserving lane — and re-derived the population and every lane bracket against the
  current manifest: 197 modules, 114 unit-regression (5-120), 2 public-contract (121-124), 53
  integration (125-179), 15 architecture-fitness (180-196), 13 provider-conformance (197-211), with
  stress-durability (212-213) and migration (214-215) empty. Also corrected a stale bound rather than
  propagating it: `pyproject.toml:135` declares `integration_case_budget = 200`, not the 150 recorded
  in this card's earlier entries, so the two invariants and the purpose paragraph now cite the
  measured value. Classification only: lane membership is not execution, certification or acceptance
  evidence, and verification metadata remains closeout-owned.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: registered eight members
  (`test_checkpoint_landing.py`, `test_closeout_kept_rules_pins.py`,
  `test_memory_scope_task_derivation.py`, `test_post_integration_cleanup_guidance.py`,
  `test_record_landing.py`, `test_retired_door_publication_fields.py`,
  `test_automatic_post_integration_cleanup.py`, and
  `test_memory_quality_is_independent_of_the_closeout_plane.py`) and repaired a manifest that could
  not load: seven tracked modules — one of them shipped by the preceding leaf — declared no lane, and
  `load_lane_manifest` refuses an incomplete population. Re-derived the population to 196 (114
  unit-regression, 2 public-contract, 52 integration, 15 architecture-fitness, 13 provider-
  conformance) and every lane bracket citation. Classification only: lane membership is not
  execution, certification or acceptance evidence, and verification metadata remains closeout-owned.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `integration` repointed to mcp/tests/test-evidence-lanes.toml:119-119. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "unit-regression" repointed to mcp/tests/test-evidence-lanes.toml:5-5. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T15:06+02:00 — Parked-candidate lane registration: recorded the new `mcp/tests/test_sync_parked_candidate.py` row in the existing `unit-regression` lane and re-derived every lane-block citation shifted by it; reconciled the current population to 183 files (99 unit-regression, 55 integration). No case budget was raised. Verification metadata remains closeout-owned.
- 2026-09-10T12:23+02:00 — 260831-LOCR-L20 curator post-sync refresh: the leaf was synced forward to
  code `bb38d04e`, and the manifest union now holds 187 rows: 103 unit-regression, 2 public-contract,
  55 integration, 14 architecture-fitness and 13 provider-conformance (L28's landed
  `test_terminal_liveness_deferred_work.py` is the extra unit-regression row, inserted at line 104).
  This card's population prose and all six lane bracket citations were re-derived against the new tree,
  and the two synced conflicts were resolved hunk-by-hunk with the synced side authoritative for ranges
  and structure. One synced claim was **corrected rather than preserved**: that row described the
  integration population as "including the R28 deferred-work proof", but
  `test_terminal_liveness_deferred_work.py` registers in `unit-regression` at line 104, so the clause
  was dropped as contradicted by the current tree. Lane classification only; focused execution and any
  later acceptance remain separately owned.

- 2026-09-10T11:55:00+02:00 — Post-sync union curation for 260831-LOCR-L03: the landed LOCR master tip `bb38d04e` carried the sibling R28 registration and its own re-derivation of the authorized three-row CCR landing-debt repair, while this branch carried the L03 `test_terminal_evidence_mapping.py` row. Both rows are kept, sorted, and this card's population statement and all six lane citations were re-derived against the union to 187 declared modules (103 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). The sibling's two-range empty-population citation for stress-durability/migration and its R28 attribution were retained, with the R28 attribution moved to the unit-regression row it actually belongs to. Supersedes the 186-module figures recorded below. Classification only; no execution, certification or acceptance claim.

- 2026-09-10T11:53+02:00 — 260831-LOCR-L09 curator: resolved this card's sync merge and re-derived the whole lane account against the merged manifest — 187 modules, 103 unit-regression / 2 public-contract / 55 integration / 14 architecture-fitness / 13 provider-conformance, with stress-durability and migration empty. Corrected every lane bracket range to current line numbers, replaced the ambiguous `integration` anchor (three resolutions at the verified commit) with the unique `"integration = ["` literal, split the former combined L38 row into its two module paths, and recorded this leaf's boundary-delivery module plus the three pre-existing omitted-row repairs already carried by LOCR-L28. Verification metadata is the merged base `bb38d04e`; the real commit stamp remains closeout-owned.

- 2026-09-10T11:52:46+02:00 — 260831-LOCR-L25 curator: resolved the merge with landed LOCR-L28 (`e26b55db`) and re-derived every lane bracket and the population against the synced manifest: 187 modules — 103 unit-regression (`5-109`), 2 public-contract (`110-113`), 55 integration (`114-170`), 14 architecture-fitness (`171-186`), 13 provider-conformance (`187-201`), with stress-durability (`202-203`) and migration (`204-205`) empty; every row unique and present on disk. Supersedes the 186 / 102 figures recorded above by both leaves. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-10T11:25:00+02:00 — Authorized repair of a pre-existing manifest omission: `8885939e` created `test_review_state.py`, `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` in the same change that edited this manifest, but their required rows were omitted, so `load_lane_manifest` could not resolve them. The three rows were restored as `unit-regression` - their behaviour-preserving lane, since a full run had already collected them unmarked - and this card's population statement and all six lane citations were re-derived to 186 declared modules (102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). Registering them as `integration` was rejected because that lane sits at its 150-case cap and collection fails. Classification only; no execution, certification or acceptance claim.

- 2026-09-10T11:24+02:00 — 260831-LOCR-L28 curator: re-derived the manifest population and every lane range against the current tree after the authorized repair of three missing CCR landing-debt registrations, all three created by code commit 8885939e but omitted from this manifest. All three take the `unit-regression` lane because the integration lane is capped at 150 collected cases and registering them as integration raised a full-suite collection above that cap; in unit-regression the collection succeeds and the previously unmarked modules keep their existing behaviour. This leaf's own `test_terminal_liveness_deferred_work.py` row was corrected the same way, from integration to `unit-regression`: the module is hermetic and registering it as integration took that lane to 155 against the same 150 cap. Current population is 186 modules: 102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance; stress-durability and migration empty. Supersedes the 183-module account in this leaf's first entry. Classification metadata only; focused results and certification remain closeout-owned.

- 2026-09-10T11:22:48+02:00 — 260831-LOCR-L25 curator: corrected the lane split for the three restored CCR landing-debt rows. The first registration put `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` in `integration`, which pushed full-suite collection to 157 against the 150-case integration cap and raised `UsageError` at collection finish; because both modules previously ran unmarked (unit), the behaviour-preserving lane is `unit-regression`. All three restored rows (`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) are now `unit-regression`. Re-derived population: 102 unit-regression / 2 public-contract / **55** integration / 14 architecture-fitness / 13 provider-conformance = 186 files, superseding the 100 / 2 / 57 figures recorded at 11:04 on the same tree. Integration collects 150 (cap 150), unit collects 712 (cap 1000). The bracket ranges were re-measured (`integration` is again 113-169, `unit-regression` 5-108) and the cap consequence is recorded as a current invariant. Classification only: no execution or acceptance claim, and verification metadata remains closeout-owned.

- 2026-09-10T11:04:12+02:00 — 260831-LOCR-L25 curator: re-derived this card against the developer-authorized manifest repair that restored the three CCR landing-debt rows `8885939e` omitted (recorded here as `test_review_state.py` unit-regression; `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` integration; the three modules already had cards). All five lane bracket ranges and the L38 row were re-measured and the population was recorded as 100 unit-regression / 2 public-contract / 57 integration / 14 architecture-fitness / 13 provider-conformance = 186 files, replacing 99 / 2 / 55 / 14 / 13 = 183. **The 57-integration split in this entry was superseded by the 11:22 correction above; the total of 186 and the restored-row set remain correct.** Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-10T10:55+02:00 — 260831-LOCR-L20 curator manifest refresh: the developer authorized
  repairing the pre-existing registration omission, and three modules created by the CCR
  transaction-only closeout reform were restored to the closed population —
  `test_review_state.py`, `test_task_doc_review_public.py` and
  `test_transaction_only_worktree_delivery.py`, all in `unit-regression`. They had been running
  unmarked (counted as unit), and the integration lane already sat at its hard cap of 150 collected
  cases, so `integration` would have overflowed the cap; the unit lane is the behaviour-preserving
  classification. The manifest then held 186 rows: 102 unit-regression, 2 public-contract,
  55 integration, 14 architecture-fitness and 13 provider-conformance. `load_lane_manifest` refused
  the incomplete manifest before the repair and loads it now. This card's population prose and all
  six lane bracket citations were re-derived against the file as it stood; the preceding L20 entry's
  183 rows was the count before that restoration. This records lane classification only; focused
  execution and any later acceptance remain separately owned.

- 2026-09-10T10:06:31+02:00 — 260831-LOCR-L25 curator: registered the new separation-guard module `mcp/tests/test_parked_external_await_separation.py` in the `unit-regression` lane and re-derived every lane bracket and membership range against the current manifest on the leaf candidate base `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`. The recorded population (96 unit / 54 integration / 179 files) had already drifted from the manifest, which held 98 / 55 / 182 before this leaf's row; it is now recorded as 99 / 55 / 183. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.

- 2026-09-09T12:22:46+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the two registered public integration modules and reconciled the manifest population to 179 files (54 integration). Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-09-08T14:39+02:00 — 260831-LOCR-L20 curator reconciliation: registered the new
  `test_terminal_evidence_cursors.py` unit-regression member and reconciled the manifest
  population to its then-current 183 rows (99 unit-regression, 55 integration), adding the focused
  deque-envelope, unsupported-harness, bounded-Pi, and liveness-containment checks to this route's
  account, and re-anchored every lane citation in this card to the tree as it stood. This records lane
  classification only; focused execution and any later acceptance remain separately owned.

- 2026-09-08T14:35+02:00 — 260831-LOCR-L28 curator: registered the new `test_terminal_liveness_deferred_work.py` integration proof and re-derived the manifest population and every lane range against the current tree (183 modules: 98 unit-regression, 2 public-contract, 56 integration, 14 architecture-fitness, 13 provider-conformance; stress-durability and migration empty). The lane remains classification metadata; focused results and certification remain closeout-owned.

- 2026-09-08T14:30:38+02:00 — Added the canonical terminal-evidence mapping regression to the `unit-regression` inventory and reconciled the retained population to 183 modules (99 unit-regression, 55 integration) on the current base, re-deriving this card's lane citations after the new row shifted them. Lane membership controls selection/classification only; this candidate entry does not claim execution, certification or acceptance.

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Recorded the real transaction suite integration membership and shifted only exact affected lane citations; classification remains distinct from acceptance. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Added current retained-evidence, producer-publication and registry-lock lane assignments with explicit distinctions between classification and execution fidelity.

- 2026-09-05T06:14:14+00:00 — Reconciled all accumulated CCR lane additions and clarified that lane membership does not itself prove real production integration.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: recorded the five CCR-R14 final-codex contract suites (rows 64-68, `unit-regression`) and the executor plus diff-coverage closure suites (rows 291-292, `integration`) and re-anchored the manifest citations shifted by the new rows (fence 102, gate-certificate 77, doctrine 526-528, retry 157/427/529, kernel 150, future-code 303, pair 385, ARSPAWN 301/396/426/515, CCR-R01 nine suites 29-30/73/158-161/180-181). Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08`.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: recorded the six CCR-R17 measured-replay suites (rows 148-153, `unit-regression`) and re-anchored the manifest citations shifted by the new rows plus prior registrations (doctrine 525-527, retry 158/426/528, kernel 145, future-code 302, pair 384, ARSPAWN 300/395/425/514, fence 97, CCR-R01 nine suites 29-30/68/159-162/181-182, gate-certificate 72). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185`.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the three status-wait test modules added to the integration evidence lane.

- 2026-09-04T17:50+02:00 — 260831-CCR-L13 Gate-5 memory pass: recorded the four CCR-R13 diagnostic contract suites (rows 60-63, unit-regression) and the executor plus diff-coverage closure suites (rows 284-285, integration) and re-anchored the manifest citations shifted by the new rows (fence 97, doctrine 518-520, retry 152/420/521, kernel 145, future-code 296, pair 378, ARSPAWN 294/389/419/507, CCR-R01 29-30/68/153-156/175-176, gate-certificate 72). Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf`.

- 2026-09-04T17:15+02:00 - 260831-CCR-L20 Gate-5 memory pass (code commit `ce7f10b5`):
  registered the standalone CCR-R20 terminal rail-failure suite as explicit `integration`
  evidence (row 465) and re-anchored every manifest lane citation in this card to the committed
  tree positions (doctrine 513-515, retry 148/414/516, kernel 141, future-code 290, pair 372,
  ARSPAWN 288/383/413/502, fence 93, CCR-R01 nine suites 29-30/64/149-152/171-172) after
  intermediate registrations and the new row shifted the manifest. Verification stamp is the full
  leaf code commit `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5 memory pass: recorded the six new
  durable gate-and-rail telemetry suites (unit-regression lanes file rows 178-183) and re-anchored
  every manifest citation shifted by their rows (doctrine 512-514, retry 148/414/515, kernel 141,
  future-code 290, pair 372, ARSPAWN 288/383/413/501, fence 93, CCR-R01 nine suites
  29-30/64/149-152/171-172). Verification stamp advanced to the certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the explicit `integration` lane registration for the new host-authority suite `test_dagger_runtime_authority.py`.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the `test_generation_coherent_lifecycle_projection.py` unit-regression lane registration and the manifest line shift it causes. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: recorded the CCR-R08
  integration-lane registration of the five final full memory-coherence certification suites
  (rows 365-369) so each forcing suite enters the closed population exactly once. Verification
  metadata pinned to the owning commit 16d1a4d6.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: recorded the CCR-R10 lane registration of
  `mcp/tests/test_citation_deterministic_projection.py` as explicit `integration` evidence (toml row 223)
  and re-anchored every manifest citation shifted by that row (retry 147/401/501, ARSPAWN
  280/370/400/487, future-code 282, pair 364, doctrine 498-500). Verification pinned to the
  leaf code commit 709dd076.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `test_serving_requirements.py` integration-lane registration and re-anchored the manifest citations shifted by the new row (doctrine 498-500, ARSPAWN e2e 487, retry-coverage 501).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all 21 manifest lane citations to the exact current line numbers after the L21 gate-certificate registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500, kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all
  21 manifest lane citations to the exact current line numbers after the L21 gate-certificate
  registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500,
  kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine
  suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source
  history until closeout.

- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the new forcing suite enters the closed population exactly once. Verification is pinned to the owning commit.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of
  `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the
  new forcing suite enters the closed population exactly once. Verification is pinned to the
  owning commit.

- 2026-09-01T11:33+02:00 - CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the three focused certification edge suites and re-anchored every manifest citation shifted by those rows. Verification remains closeout-owned.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the
  three focused certification edge suites and re-anchored every manifest citation shifted by
  those rows. Verification remains closeout-owned.

- 2026-09-01T08:13+02:00 - Final CCR-R01 reconciliation: expanded the current lane account from six to all nine focused unit-regression suites, including the three coverage-edge companions, and regenerated every manifest citation shifted by their rows. The manifest supplies selection and cost classification only; verification remains closeout-owned.

- 2026-09-01T08:13+02:00 — Final CCR-R01 reconciliation: expanded the current lane account from
  six to all nine focused unit-regression suites, including the three coverage-edge companions, and
  regenerated every manifest citation shifted by their rows. The manifest supplies selection and
  cost classification only; verification remains closeout-owned.

- 2026-09-01T05:22+02:00 - 260831-CCR-L01 Attempt 9: added explicit `unit-regression` ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by those rows. The lane declaration governs selection/cost only; accepted task evidence remains reviewer-owned. Verification remains closeout-owned.

- 2026-09-01T05:22+02:00 — 260831-CCR-L01 Attempt 9: added explicit `unit-regression`
  ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by
  those rows. The lane declaration governs selection/cost only; accepted task evidence remains
  reviewer-owned. Verification remains closeout-owned.

- 2026-09-01T04:34+02:00 - Added explicit `unit-regression` ownership for the two certification contract suites and repaired every manifest citation shifted by those rows. The manifest remains fail-closed; no default, fallback, or alternate classification authority was introduced.

- 2026-09-01T04:34+02:00 — Added explicit `unit-regression` ownership for the two certification
  contract suites and repaired every manifest citation shifted by those rows. The manifest remains
  fail-closed; no default, fallback, or alternate classification authority was introduced.

- 2026-08-31T20:30+02:00 - 260831-DER: explicitly classified `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.

- 2026-08-31T20:30+02:00 — 260831-DER: explicitly classified
  `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.

- 2026-08-31T08:05+02:00 - Classified the four A003-unregistered ARSPAWN proof modules exactly once: three integration routes and one architecture-fitness selector-closure route.

- 2026-08-31T08:05+02:00 — Classified the four A003-unregistered ARSPAWN proof modules exactly
  once: three integration routes and one architecture-fitness selector-closure route.

- 2026-08-30T15:15:36+02:00 - Classified `test_public_surface_conformance.py` explicitly as integration evidence. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — Classified `test_public_surface_conformance.py` explicitly as
  integration evidence. Verification remains closeout-owned.

- 2026-08-30T04:54+02:00 - Added explicit integration-lane ownership for the exact code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified test file. No product or requirement semantics changed.

- 2026-08-30T04:54+02:00 — Added explicit integration-lane ownership for the exact
  code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified
  test file. No product or requirement semantics changed.

- 2026-08-29T08:52+02:00 - Added explicit integration classification for the structured curator-coherence forcing suite. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added explicit integration classification for the structured
  curator-coherence forcing suite. Verification remains closeout-owned.

- 2026-08-29T07:35+02:00 - Added explicit integration-lane ownership for the future-code candidate real-Git matrix and repaired exact manifest citations shifted by that row.

- 2026-08-29T07:35+02:00 — Added explicit integration-lane ownership for the future-code
  candidate real-Git matrix and repaired exact manifest citations shifted by that row.

- 2026-08-28T14:18+02:00 - Reconciled manifest citations against the committed PDLS candidate; the explicit-lane contract is unchanged.

- 2026-08-28T14:18+02:00 — Reconciled manifest citations against the committed PDLS candidate;
  the explicit-lane contract is unchanged.

- 2026-08-28T05:10+02:00 - Removed the two stale Candidate A test rows and retained the renamed kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.

- 2026-08-28T05:10+02:00 — Removed the two stale Candidate A test rows and retained the renamed
  kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.

- 2026-08-27T18:33+02:00 - Recorded explicit unit-regression membership for the retry coverage composition and quality child-environment suites.

- 2026-08-27T18:33+02:00 — Recorded explicit unit-regression membership for the retry coverage
  composition and quality child-environment suites.

- 2026-08-27T18:06+02:00 - Added explicit architecture-fitness membership for the M40-M45 Requirement Attempt Journal structural proof.

- 2026-08-27T18:06+02:00 — Added explicit architecture-fitness membership for the M40-M45
  Requirement Attempt Journal structural proof.

- 2026-08-27T17:19+02:00 - Added explicit unit-regression membership for the retry-selection forcing suite in the same change that introduced it.

- 2026-08-27T17:19+02:00 — Added explicit unit-regression membership for the retry-selection
  forcing suite in the same change that introduced it.

- 2026-08-27T13:32+02:00 - Added explicit architecture-fitness membership for M39 compilation doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.

- 2026-08-27T13:32+02:00 — Added explicit architecture-fitness membership for M39 compilation
  doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 - M38: created the manifest sidecar and recorded explicit registration of the acceptance-envelope structural test. Verification metadata remains empty until governed closeout stamps the PDLS code commit.

- 2026-08-27T12:43+02:00 — M38: created the manifest sidecar and recorded explicit registration
  of the acceptance-envelope structural test. Verification metadata remains empty until governed
  closeout stamps the PDLS code commit.
