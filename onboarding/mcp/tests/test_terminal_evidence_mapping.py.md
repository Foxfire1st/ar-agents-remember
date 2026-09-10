# test_terminal_evidence_mapping.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_evidence_mapping.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T11:55:00+02:00 |
| lastVerifiedCommitHash | `5ee86646b27fef04b98bbd94198abb2ee315638d` |
| lastVerifiedCommitDate | 2026-09-10T12:52:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Protects the canonical native terminal-evidence lift at its no-claim boundary. The focused cases
keep malformed and open Pi frames from producing terminal evidence and prove that an unmappable
frame cannot hide a later canonically mapped terminal outcome.

## Code Commentary

### Logic

`CanonicalNativeTerminalMappingTests` builds the existing `NativeEvidenceFrame` and
`NativeEvidencePage` contracts and calls `latest_native_terminal_evidence` directly. The first
case combines a malformed native message with an assistant message that has no stop reason and
expects no projection. The second places the same malformed frame before a Pi `stop` message and
checks the later canonical projection's native identity, completed outcome, and stop reason.

### Conventions

The helpers keep native frame construction and Pi assistant payloads small and explicit. This
module tests the public terminal-evidence lift and its registered projector boundary; it does not
reimplement vendor mapping or the liveness sweeper.

### Invariants And Boundaries

- Unmappable and nonterminal native frames produce no terminal claim.
- A later canonical terminal frame remains observable after an earlier unmappable frame.
- The test does not add a parser, fallback, durable unknown-evidence row, cursor behavior, or
  lifecycle ownership claim; those remain with the existing mapper, LOCR-R20, and the assembled
  lifecycle candidate respectively.
- Focused host results are diagnostic evidence only; leaf acceptance and master review remain
  lifecycle-owned.

### Todos

Re-run this focused proof against the assembled observer candidate and preserve the separate R20
cursor proof before any master-level acceptance decision.

## Docs References

No configured domain documentation is needed for this repository-owned mapper regression.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was configured for this test contract. | N/A | N/A |

## Repo-Internal References

The test exercises the existing native-page lift and the registered Pi projector's terminal stop
mapping without changing production code.

| Finding | Anchor | Source |
| --- | --- | --- |
| The native lift skips `UnmappableShape`, ignores non-terminal mapper outputs, and retains the latest mapped projection. | `UnmappableShape` | mcp/src/agents_remember/serving/terminal_evidence.py:103-142 |
| A malformed or open frame makes no claim. | `test_unmappable_and_nonterminal_frames_make_no_terminal_claim` | mcp/tests/test_terminal_evidence_mapping.py:46-52 |
| A later Pi stop frame remains canonical and identifiable after an unmappable frame. | `test_unmappable_frame_does_not_hide_later_canonical_terminal_frame` | mcp/tests/test_terminal_evidence_mapping.py:54-66 |
| Pi `stop` maps to a completed terminal outcome through the registered projector. | `MappedTurnOutcome` | mcp/src/agents_remember/serving/conversation/projectors/pi.py:323-324 |

## Cross-Repo References

This test has no implementation boundary outside the agents-remember repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository references found. | N/A | N/A |

## Update History

- 2026-09-10T11:55:00+02:00 — Post-sync re-verification: `git diff 6096941f bb38d04e` touches only `mcp/tests/test-evidence-lanes.toml` and the newly landed `mcp/tests/test_terminal_liveness_deferred_work.py`, so every range cited below is unchanged between the two bases. The verification pin was advanced to the synced base `bb38d04e`. No acceptance or certification claim.
- 2026-09-10T09:57:27+02:00 — Curator re-verified this card's cited terminal-lift and Pi-projector ranges against the synced code base `6096941f` and moved the verification pin from the pre-sync base `8133b6a9` to that base; the two focused no-claim cases and production mapping are unchanged. No acceptance or certification claim.
- 2026-09-08T14:25+02:00 — Created the focused canonical native terminal-evidence mapping card for the new two-case regression. Production mapping remains unchanged; verification is pinned to the synced leaf base until closeout stamps the code commit, and this card does not claim acceptance.
