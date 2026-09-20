# mcp/tests/test_candidate_batch_commands.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_candidate_batch_commands.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T14:20+02:00 |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a`|
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**The focused behaviour of the candidate command union and its batch preconditions.** Each case protects one
consequential operation or failure: every command kind the union declares, the receipt that reports what was
written, a no-op that must leave no trace, an expectation that must match, and the payload shapes the closed
union refuses at its own boundary.

Constructor validation is deliberately **not** re-tested here. What is tested is that the union cannot express
something the operation must not do, and that the receipt describes what actually happened.

It is registered in `mcp/tests/test-evidence-lanes.toml` under **unit-regression**: the module is hermetic
(temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the
default unit lane is its behaviour-preserving classification.

## Code Commentary

### Logic

Nine nodes, all driven through the admitted destination (`CandidateHarness.batch` →
`change_knowledge_candidate`) rather than against the store directly:

- `test_every_declared_command_is_applied_and_read_back` — the union's coverage case: all twelve kinds applied in
  one batch and each written record read back through its owning module. It is the node that would fail if a
  command kind lost its apply step.
- `test_a_receipt_reports_the_rows_the_store_now_holds` — the receipt's fidelity: each entry's digest is the one
  the store computes now, in command order.
- `test_a_changed_receipt_must_name_at_least_one_touched_record` — the receipt model's own rule, pinned in both
  the shapes it must refuse: a `changed` state with no entry, once with an identical identity and once with a
  genuinely moved digest. The guard it protects is the one that makes "the ledger missed its own writes"
  unrepresentable rather than merely improbable.
- `test_an_empty_batch_commits_no_record_and_reports_no_change` — the empty batch reaches `state="no_change"`
  and writes no row, counter or timestamp.
- `test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed` — an insertion is never an upsert:
  restating a stored identity refuses `stale_precondition` even though the payload is identical, which is what
  distinguishes the batch path from the single-record operation's `no_change` confirmation.
- `test_an_expected_record_that_matches_permits_the_batch` — the expectation that *holds* is not an obstacle;
  this is the control for the expectation cases in the transaction module.
- `test_the_closed_union_refuses_an_unknown_field_and_an_unknown_command` — the boundary cases: an unknown field
  and an unknown command kind both fail at construction, so neither can reach the operation.
- `test_two_expectations_for_one_record_are_refused_at_the_boundary` — the batch model's own duplicate-expectation
  rule.
- `test_the_context_digest_seals_the_whole_resolved_context` — the model-level seal: a context whose fields were
  edited after resolution fails construction. The *operation-level* re-derivation is the transaction module's
  `test_a_context_smuggled_past_the_model_seal_is_refused_by_the_operation`, because a node that only asserts the
  model validator would not discriminate the in-transaction comparison.
- The five private digest helpers at the bottom read a row's digest through its owning module so a case asserts on
  the store's value rather than on a value it invented.

### Conventions

- The module imports the typed command models directly and builds payloads through the typed draft models, so a
  case's input fails at the same boundary a caller's would.
- Every assertion about "nothing was written" reads the store again; nothing is asserted from the returned result
  alone.
- Node names state the behaviour, not the implementation: a future refactor that preserves behaviour keeps the
  names meaningful.
- Registration: `mcp/tests/test-evidence-lanes.toml` `unit-regression`. An unregistered test module makes
  `load_lane_manifest` refuse the repository, which turns into a collection error — so the row is a precondition
  for the collection path, and classification only, never execution or acceptance evidence.

### Invariants And Boundaries

- **Focused, not exhaustive.** The module covers the union and the receipt; the transaction boundary, the lane
  rules and the precondition refusals belong to `test_candidate_batch_transaction.py`, and the standalone label
  guard to `test_knowledge_label_operations.py`. Do not duplicate a case across the three.
- **Construction tests test the boundary, not the shape twice.** Only the payloads the operation must not be able
  to express are asserted here.
- **The receipt claims are measured.** Each receipt case reads the stored rows back, so a receipt and the store
  cannot both be wrong in the same direction unnoticed.
- **Boundary.** This module owns the union's coverage and the receipt's fidelity. It writes no fixture of its own
  beyond the shared harness (contract `candidate-batch-case-harness`) and imports no other support module.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's scope statement: the union and the receipt, with constructor validation deliberately not re-tested. | "the union cannot express something" | mcp/tests/test_candidate_batch_commands.py:1-9 |
| The union's coverage case over all twelve kinds. | "test_every_declared_command_is_applied_and_read_back" | mcp/tests/test_candidate_batch_commands.py:118-239 |
| The receipt-fidelity case and the changed-receipt guard in both its shapes. | "test_a_receipt_reports_the_rows_the_store_now_holds"; "test_a_changed_receipt_must_name_at_least_one_touched_record" | mcp/tests/test_candidate_batch_commands.py:242-321; mcp/tests/test_candidate_batch_commands.py:324-348 |
| The no-op and the insertion-is-not-an-upsert cases. | "test_an_empty_batch_commits_no_record_and_reports_no_change"; "test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed" | mcp/tests/test_candidate_batch_commands.py:351-351; mcp/tests/test_candidate_batch_commands.py:373-373 |
| The held expectation and the two closed-union boundary cases. | "test_an_expected_record_that_matches_permits_the_batch"; "test_the_closed_union_refuses_an_unknown_field_and_an_unknown_command"; "test_two_expectations_for_one_record_are_refused_at_the_boundary" | mcp/tests/test_candidate_batch_commands.py:406-406; mcp/tests/test_candidate_batch_commands.py:441-441; mcp/tests/test_candidate_batch_commands.py:475-475 |
| The model-level seal case, whose operation-level twin lives in the transaction module. | "test_the_context_digest_seals_the_whole_resolved_context" | mcp/tests/test_candidate_batch_commands.py:492-492 |
| The unit-lane rows that make the module's classification explicit. | "mcp/tests/test_candidate_batch_commands.py" | mcp/tests/test-evidence-lanes.toml:19-19 |
|The shared harness this module drives and its registered contract.|"contract:candidate-batch-case-harness"| mcp/tests/evidence-lifecycle.toml:1241-1241 |
| The operation under test and the union it accepts. | `change_candidate`; "ProposedCommand = Annotated[" | mcp/src/agents_remember/memory/knowledge/candidate.py:64-83; mcp/src/agents_remember/models/knowledge/candidate.py:614-614 |
| The shared harness this module drives and its registered contract. | "contract:candidate-batch-case-harness" | mcp/tests/evidence-lifecycle.toml:1241-1241 |
| The operation under test and the union it accepts. | `change_candidate`; "ProposedCommand = Annotated[" | mcp/src/agents_remember/memory/knowledge/candidate.py:64-83; mcp/src/agents_remember/models/knowledge/candidate.py:614-614 |

## Cross-Repo References

No cross-repository behavior is involved in this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
| The shared harness this module drives and its registered contract. | "contract:candidate-batch-case-harness" | mcp/tests/evidence-lifecycle.toml:1241-1241 |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (deterministic-check clearance inside this leaf's change set, uncommitted on `ar/260915-ks-l43-ar`, code base `fb719f89`): **one `ruff format` reflow inside an existing case; no claim changed, and one class of pre-existing drift was measured and left alone.** In `test_a_receipt_reports_the_rows_the_store_now_holds` the `claim_draft(claim_id=…, revision_id=…)` call inside its `AddRealizationClaim` collapsed onto one line (old `:306-308` → new `:306`), so **every line after that span moved up by two**: the case itself is now `:242-321` (was `:244-323`), and the five single-line anchor citations this card carries are now `test_an_empty_batch_commits_no_record_and_reports_no_change` at `:351`, `test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed` at `:373`, `test_an_expected_record_that_matches_permits_the_batch` at `:406`, `test_the_closed_union_refuses_an_unknown_field_and_an_unknown_command` at `:441` and `test_two_expectations_for_one_record_are_refused_at_the_boundary` at `:475`, with `test_the_context_digest_seals_the_whole_resolved_context` at `:492`. **Two rows on this card were narrow at the cited lines and were repointed to their cases' own declaration extents**: `test_every_declared_command_is_applied_and_read_back` `:114-209` → `:118-239`, and `test_a_receipt_reports_the_rows_the_store_now_holds` `:210-254` → `:242-321`. Each replacement was read at its own declaration before it was written. **One pre-existing condition is reported rather than chased:** those two rows did not hold their quoted cases at the *base* commit either — at `fb719f89` those lines carry the tail of the preceding case — so that drift predates this leaf and was not introduced by the reformatting, which moved lines after `:306` by exactly two. This leaf's own fall-out is the five single-line cells listed above, and each was verified at its declaration in the reformatted tree. No claim wording, anchor or row was otherwise changed. **Stamp accounting:** no verification stamp was advanced, because no commit contains the body as it now stands and closeout owns the real stamp; `reviewedWorkingCandidate` names this leaf's candidate. No commit was made.
- 2026-09-20T01:23+02:00 — 260915-KS-L30 curator, final citation pass (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared this card's one enforced `citation_anchor_absent_from_range` row by RANGE REPAIR.** The row names `test_an_expected_record_that_matches_permits_the_batch` and cited `mcp/tests/test_candidate_batch_commands.py:337-371`, a window that has moved off the case and now holds the tail of `test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed`; the construct is declared at `408`, so that citation was repointed to `mcp/tests/test_candidate_batch_commands.py:408-408`, which is the row's own shape for a case (`:443-443`, `:477-477` are its siblings and were already right). Read at the source before the write: `def test_an_expected_record_that_matches_permits_the_batch(` is at line 408. No claim wording, anchor or other citation was added, removed or re-worded, and nothing outside this row was touched. **Stamp position:** unchanged — this repair re-cites an anchor that already resolved; no verification stamp was advanced and no commit hash was written.
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 5 enforced citation rows this card carried (citation_anchor_absent_from_range): every flagged range was hand-read against mcp/tests/test_candidate_batch_commands.py and already held the anchor its claim names (`test_a_changed_receipt_must_name_at_least_one_touched_record`, `test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed`, `test_an_empty_batch_commits_no_record_and_reports_no_change`, `test_the_closed_union_refuses_an_unknown_field_and_an_unknown_command`, `test_two_expectations_for_one_record_are_refused_at_the_boundary`), so no range was changed; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 5 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_a_changed_receipt_must_name_at_least_one_touched_record`; `test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed`; `test_an_empty_batch_commits_no_record_and_reports_no_change`; `test_the_closed_union_refuses_an_unknown_field_and_an_unknown_command`; `test_two_expectations_for_one_record_are_refused_at_the_boundary`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "test_the_context_digest_seals_the_whole_resolved_context" repointed to mcp/tests/test_candidate_batch_commands.py:494-494. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1241-1241. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:64-83; mcp/src/agents_remember/models/knowledge/candidate.py:614-614. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1241-1241. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:64-83; mcp/src/agents_remember/models/knowledge/candidate.py:614-614. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1241-1241. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 3 enforced `citation_anchor_absent_from_range` rows in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1239-1239` → `mcp/tests/evidence-lifecycle.toml:1239-1240` (rows 113, 115, 125). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1239-1239. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1239-1239. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1239-1239. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1236-1236. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:611-611. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1236-1236. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:611-611. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1236-1236. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_candidate_batch_commands.py" repointed to mcp/tests/test-evidence-lanes.toml:19-19. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1232-1232. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1232-1232. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1232-1232. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:596-596. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:596-596. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:498-498. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1110-1110. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `change_candidate`; "ProposedCommand = Annotated[" repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:498-498. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand while resolving the memory sync** — `change_candidate`, `ProposedCommand = Annotated[`, `contract:candidate-batch-case-harness`, `ProposedCommand`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand** — `change_candidate`, `ProposedCommand`, `contract:candidate-batch-case-harness`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1103-1103` -> `mcp/tests/evidence-lifecycle.toml:1104-1104`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-batch command suite (nine nodes, unit-regression lane). It records what the suite does and does not cover — the union's coverage and the receipt's fidelity here, the transaction boundary in its sibling module, the standalone label guard in its own module — and why the model-level seal case does not replace the operation-level one. Verification metadata remains empty until closeout stamps the code commit.
