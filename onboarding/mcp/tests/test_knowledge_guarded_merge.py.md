# mcp/tests/test_knowledge_guarded_merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_guarded_merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate | 2026-09-18T14:21:49+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The merge's whole contract in five cases**, in the unit-regression lane. The unit population is at its declared `unit_case_budget` ceiling, so this module carries the contract in five named nodes rather than one per scenario, and each node is the node a specific guard is mutation-checked against.

Every case asserts the **whole** outcome — the state, the identity, the refusal code, and that every input is byte-identical to what it was — rather than one field of it. That is the property the module exists to protect: a merge that refuses for the right reason while moving an input, or a merge that succeeds while dropping a side's work, fails here rather than in a downstream consumer.

## Code Commentary

### Logic

- `test_every_structural_violation_is_refused_before_a_session_exists` — compares each input against the declared manifest. `_structural_violations` builds six distinct classes (the set of canonical tables, an added column, a weakened NOT NULL, a wrong foreign key, a dropped trigger, changed table options) plus a reorder and a rename (`_reorder_invariant_columns`, `_rewrite_schema`), a weakened trigger body, a changed `user_version`, and an absent or unreadable input. Every edit is applied through `_edited`/`_mutate`. Fails if any comparison stops refusing.
- `test_an_incomplete_delta_applies_silently_and_is_caught_by_coverage_and_replay` — the **silent-omission class**, and the module's named unit-side guard. `_partial_delta` builds one delta whose session was told about only a subset of the canonical tables — the shape a missing `session.attach` produces in production, where the connection still holds every table and SQLite reports no error. The case asserts that SQLite accepts it and that the coverage comparison and the replay each refuse it. Fails if either comparison stops measuring, or if the not-supplied marker is conflated with a stored SQL `NULL`.
- `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` — the conforming case: both sides' own work is retained, the published file is closed, the coverage record is complete, and the outcome carries no verdict field. Fails if either side's work is dropped, if the published file is not closed, or if a publication that changed nothing is reported as a change. **This is the registered evidence node of `contract:common-base-merge-cases`.**
- `test_both_conflicting_edits_refuse_whole_and_preserve_every_input` — the refusal taxonomy: `_same_field_conflict`, `_shared_revision_shape` (two independent insertions under one identity, with equal payloads in the shape the case builds) and `_reference_case` (a removed row the other side's new reference depended on) in **both** orientations. Every refusal also names the row it refused — the exact key the engine handed the conflict callback — which is asserted here rather than left to the boundary module, so this node fails if a key is ever read from the wrong side of a change.
- `test_every_base_and_every_input_defect_refuses_without_moving_a_dataset` — base resolution and input integrity: the ancestry-proven and supplied claims, a history with no common base, a criss-cross history with two (built by `_merge_commit`), a relative repository root, an input that moved after admission, one file named as two roles, `_tamper` (a side that rewrote a sealed revision in place and restored the trigger that refused the write), and an input moved after resolution. Fails if a base is chosen rather than proven, or if an input defect is carried into a merge.

Shared helpers: `assert_refused_without_moving_any_input` (a refused outcome that published nothing and left all three inputs untouched), `assert_removal_orientation` (measures 0/0 anchors and claims on the removing side against 1/1 on the citing side, so the orientation is a measurement rather than a restatement of the parameter), and `assert_input_defects_refuse` (every input defect in one case refuses, and no refusal moves a dataset).

### Conventions

- The two committed artificial states are built through the real store operations or through explicit catalog edits, and every Git object is created by `_commit_on_top`/`_merge_commit` in a temporary repository this module's harness owns. `_git` runs the one scenario Git command through the package's own runner and refuses a failure.
- `_insert_revision` inserts a whole revision row directly, as two independent authors would, because the case is about the collision and not about the store's own path.
- `resolve`/`run`/`base_request` are per-case convenience readers over `merge_case_test_support`, so a case reads as its scenario rather than as its plumbing.

### Invariants And Boundaries

- **Five cases is a budget decision, not a coverage claim.** The module docstring says so, and the boundary scenarios that need their own world live in `test_knowledge_guarded_merge_boundaries.py` (integration lane) instead of being packed in here.
- **Each case asserts the whole outcome.** A node that checked one field would leave the input-preservation property unmeasured, which is the failure mode this leaf's review sealed twice.
- **Boundary.** This module holds the unit-side contract; it does not own the base-resolution or schema modules' internals, and it publishes only into private temporary destinations the harness creates.

### Todos

None recorded for this slice. The unit-population budget is exactly full (1000/1000 collected) after this leaf, which the owning seat reported as a standing decision rather than a defect in this module.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five-case contract, what each case fails on, and the budget statement. | "The unit population is at its declared ceiling" | mcp/tests/test_knowledge_guarded_merge.py:1-33 |
| The structural node and its six classes plus reorder, rename, weakened trigger and `user_version`. | "def test_every_structural_violation_is_refused_before_a_session_exists(" | mcp/tests/test_knowledge_guarded_merge.py:111-180 |
| The registered evidence node of `contract:common-base-merge-cases`. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:248-312 |
| The conflict node, including the exact conflict-key assertion. | "def test_both_conflicting_edits_refuse_whole_and_preserve_every_input(" | mcp/tests/test_knowledge_guarded_merge.py:468-536 |
| The base and input-defect node. | "def test_every_base_and_every_input_defect_refuses_without_moving_a_dataset(" | mcp/tests/test_knowledge_guarded_merge.py:542-636 |
| The partial delta that reproduces a missing `session.attach` and is accepted by SQLite. | `_partial_delta` | mcp/tests/test_knowledge_guarded_merge.py:902-932 |
| The measured orientation assertion that replaced a constant-true predicate. | `assert_removal_orientation` | mcp/tests/test_knowledge_guarded_merge.py:795-810 |
| The harness the cases are built on, and its real three-commit Git scenario. | `build_case`; `GitBranchWorld` | mcp/tests/merge_case_test_support.py:511-571; mcp/tests/merge_case_test_support.py:72-78 |
| The boundary module that carries the scenarios needing their own world. | "Boundary cases for the guarded merge: the conflict row identity and the final-integrity checks." | mcp/tests/test_knowledge_guarded_merge_boundaries.py:1-22 |
| **The lane manifest row that classifies the unit half — the lane header itself, not one of its member rows.** | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
|**The lane manifest row that classifies the integration half — the lane header itself.**|"integration"| mcp/tests/test-evidence-lanes.toml:114-182 |
|The governed-artifact registration of the support module these cases share.|"contract:common-base-merge-cases"| mcp/tests/evidence-lifecycle.toml:1273-1273 |
| The lane manifest rows that classify both modules. | `unit-regression`; `integration` | mcp/tests/test-evidence-lanes.toml:192-192 |
|  The governed-artifact registration of the support module these cases share. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1273-1273  |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
|  The governed-artifact registration of the support module these cases share. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1273-1273  |

## Update History
- 2026-09-18T12:07:24+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:192-192. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:170-170. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_provenance_invalid). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1159-1159. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand while resolving the memory sync** — `integration`, `contract:common-base-merge-cases`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `integration`, `_partial_delta`, `assert_removal_orientation`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``integration`` → `mcp/tests/test-evidence-lanes.toml:162-162`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:160-160` -> `mcp/tests/test-evidence-lanes.toml:161-161`; `mcp/tests/evidence-lifecycle.toml:1132-1152` -> `mcp/tests/evidence-lifecycle.toml:1153-1153`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read the card against the source and re-cited the one row whose range had been projected** — the lane-manifest row now cites `mcp/tests/test-evidence-lanes.toml:158-158` (the `integration` lane array's own name) instead of the two stale offsets `154` / `157`, so the row's anchor is the array the two modules are classified by rather than a neighbouring bracket. The same read changed one source fact this card's cases depend on: the two coverage assertions in `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` and `test_a_right_side_change_to_an_appended_table_merges_instead_of_aborting` now compare against `CURRENT_GENERATION.tables` rather than `GENERATION_2.tables`, and the `GENERATION_2` import left the module — a dataset this build creates is the newest registered generation, so a literal generation number would encode the single-generation assumption one generation later. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `integration` in the row 72 of this card from mcp/tests/test-evidence-lanes.toml:5-73 to mcp/tests/test-evidence-lanes.toml:154, the extent of the construct the claim is about (the checker named line(s) [154] as its live location)

- 2026-09-16T11:45:00+00:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new unit suite. It records the five-case contract, each case's named guard and what it fails on, the whole-outcome assertion rule that makes input preservation measured rather than assumed, and — the fact a successor most needs — that the register-time failure this leaf's review found twice was a *text claim outrunning its bytes*: the module docstring now names the nodes that exist, and `assert_removal_orientation` measures both orientations (0/0 against 1/1) instead of returning a constant-true predicate. It also records that the fifth case holds the conflict key to the engine's own operation, which is the regression guard for the corrected contract. Verification metadata remains empty until closeout stamps the code commit.
