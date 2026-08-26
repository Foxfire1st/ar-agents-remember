# mcp/tests/test_direct_landing_input_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing_input_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces the sanctioned direct-landing closeout input counterpart: verified-existing code is not applicable, external-memory and ledger messages are explicit, and malformed intent refuses before the landing lock or Git.

## Code Commentary

### Logic

The matrix covers omitted, empty, whitespace, and valid stripped memory/ledger messages in preview and apply. Spies prove the invalid cases never acquire landing authority or call Git. Successful preview/apply results carry the same `effectiveInput`, and dry-run refusal returns the corrected-call shape.

### Invariants And Boundaries

- Direct landing is one lock-serialized sequential mutation path; these tests do not call it atomic or crash durable.
- Code is verified-existing/not-applicable, so no code-commit message is accepted.
- Memory and ledger are separate enabled commits sharing the same explicit-input contract.
- L2-R11/L5-R15, not this suite, own memory-before-ledger crash durability.

## Docs References

See task `260821-CLIVE-L1` L1-R1 through L1-R3, L1-R5, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Invalid direct inputs refuse before lock and Git. | `test_enabled_message_matrix_refuses_before_lane_authority_or_git` | mcp/tests/test_direct_landing_input_boundary.py:30-73 |
| Preview and apply share stripped effective input. | `test_preview_and_apply_receive_the_same_stripped_effective_input` | mcp/tests/test_direct_landing_input_boundary.py:75-112 |

## Cross-Repo References

The operation mutates the configured external-memory repository after reading the code repository's verified branch tip.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_enabled_message_matrix_refuses_before_lane_authority_or_git`, `test_preview_and_apply_receive_the_same_stripped_effective_input`, `test_domain_uses_admitted_contract_not_the_raw_request_address`, `test_public_boundary_returns_the_structured_input_refusal`. The L2 additions force the root-journal generation, ordered memory/ledger mutation evidence, configured-contract reread, crash reconciliation, and same-generation recovery. Older statements that durable recovery is absent are superseded.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_enabled_message_matrix_refuses_before_lane_authority_or_git`, `test_preview_and_apply_receive_the_same_stripped_effective_input`, `test_domain_uses_admitted_contract_not_the_raw_request_address`, `test_public_boundary_returns_the_structured_input_refusal`. | `test_enabled_message_matrix_refuses_before_lane_authority_or_git`; `test_preview_and_apply_receive_the_same_stripped_effective_input`; `test_domain_uses_admitted_contract_not_the_raw_request_address`; `test_public_boundary_returns_the_structured_input_refusal` | mcp/tests/test_direct_landing_input_boundary.py:54-97; mcp/tests/test_direct_landing_input_boundary.py:99-136; mcp/tests/test_direct_landing_input_boundary.py:138-179; mcp/tests/test_direct_landing_input_boundary.py:181-209 |

## 260821-DAGQC-L2 Outcome/Recovery Separation

The input-boundary suite pins the exact three-member outcome enum, configured-contract refusals at
initial and mutation reads, and nested recovery evidence that cannot overwrite the public refused
state or status.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added exact outcome-vocabulary and authoritative-refusal merge regressions. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits closeout.
