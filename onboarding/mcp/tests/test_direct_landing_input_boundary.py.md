# mcp/tests/test_direct_landing_input_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing_input_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
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
| Invalid direct inputs refuse before lock and Git. | `test_enabled_message_matrix_refuses_before_lane_authority_or_git` | mcp/tests/test_direct_landing_input_boundary.py:28-71 |
| Preview and apply share stripped effective input. | `test_preview_and_apply_receive_the_same_stripped_effective_input` | mcp/tests/test_direct_landing_input_boundary.py:72-109 |

## Cross-Repo References

The operation mutates the configured external-memory repository after reading the code repository's verified branch tip.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata awaits closeout.
