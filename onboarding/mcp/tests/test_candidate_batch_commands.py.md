# mcp/tests/test_candidate_batch_commands.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_candidate_batch_commands.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4`|
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
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
| The module's scope statement: the union and the receipt, with constructor validation deliberately not re-tested. | "the union cannot express something the operation must not do" | mcp/tests/test_candidate_batch_commands.py:1-9 |
| The union's coverage case over all twelve kinds. | "test_every_declared_command_is_applied_and_read_back" | mcp/tests/test_candidate_batch_commands.py:114-209 |
| The receipt-fidelity case and the changed-receipt guard in both its shapes. | "test_a_receipt_reports_the_rows_the_store_now_holds"; "test_a_changed_receipt_must_name_at_least_one_touched_record" | mcp/tests/test_candidate_batch_commands.py:210-254; mcp/tests/test_candidate_batch_commands.py:255-281 |
| The no-op and the insertion-is-not-an-upsert cases. | "test_an_empty_batch_commits_no_record_and_reports_no_change"; "test_a_command_whose_effect_is_already_stored_is_refused_not_absorbed" | mcp/tests/test_candidate_batch_commands.py:282-303; mcp/tests/test_candidate_batch_commands.py:304-336 |
| The held expectation and the two closed-union boundary cases. | "test_an_expected_record_that_matches_permits_the_batch"; "test_the_closed_union_refuses_an_unknown_field_and_an_unknown_command"; "test_two_expectations_for_one_record_are_refused_at_the_boundary" | mcp/tests/test_candidate_batch_commands.py:337-371; mcp/tests/test_candidate_batch_commands.py:372-405; mcp/tests/test_candidate_batch_commands.py:406-422 |
| The model-level seal case, whose operation-level twin lives in the transaction module. | "test_the_context_digest_seals_the_whole_resolved_context" | mcp/tests/test_candidate_batch_commands.py:423-438 |
| The unit-lane rows that make the module's classification explicit. | "mcp/tests/test_candidate_batch_commands.py" | mcp/tests/test-evidence-lanes.toml:18-18 |
|The shared harness this module drives and its registered contract.|"contract:candidate-batch-case-harness"| mcp/tests/evidence-lifecycle.toml:1110-1110 |
| The operation under test and the union it accepts. | `change_candidate`; "ProposedCommand = Annotated[" | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:372-392 |

## Cross-Repo References

No cross-repository behavior is involved in this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
| The shared harness this module drives and its registered contract. | "contract:candidate-batch-case-harness" | mcp/tests/evidence-lifecycle.toml:1110-1110 |

## Update History
- 2026-09-18T05:29:42+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1110-1110. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1110-1110. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T04:55:18+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1106-1106. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1103-1103` -> `mcp/tests/evidence-lifecycle.toml:1104-1104`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `change_candidate`; `ProposedCommand` repointed to mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/models/knowledge/candidate.py:372-392. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "contract:candidate-batch-case-harness" repointed to mcp/tests/evidence-lifecycle.toml:1103-1103. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-batch command suite (nine nodes, unit-regression lane). It records what the suite does and does not cover — the union's coverage and the receipt's fidelity here, the transaction boundary in its sibling module, the standalone label guard in its own module — and why the model-level seal case does not replace the operation-level one. Verification metadata remains empty until closeout stamps the code commit.
