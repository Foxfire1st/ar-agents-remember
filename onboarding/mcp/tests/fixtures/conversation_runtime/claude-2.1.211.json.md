# mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash |  `ca9dd05a295ef5f24c479e2231fdcd174b372e04`|
| lastVerifiedCommitDate |  2026-07-19T10:04:45+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through installed Claude 2.1.211 discovery while
keeping the locked SDK 0.3.207 history handshake/list/read/resume capability explicitly unverified.
260718-CHATS-L0E appends one honestly `not-exercised` `substrate-evidence/live-stream-frames` row
because the installed 2.1.214 mismatches the locked 2.1.211 gate.

## Code Commentary

### Logic

The fixture records the runtime/helper tuple, safe model-count/selected-field presence from the
production adapter, and two `not-exercised` gates covering locked-helper history and stream/control/
attachment behavior. It fixes `enablesCapabilities` to false. The L0E row records that live stream
frame and usage/cost forwarding through the production evidence seam remains unverified until a
locked 2.1.211 install exercises it — version honesty rather than a guessed observation.

### Conventions

Only allow-listed counts/field presence and safe reasons survive capture. Names, ids, paths, raw
frames, prompts, and secrets are discarded.

### Invariants And Boundaries

- Exact dependency locking is not installed-runtime interoperability proof.
- Claude history remains unverified until 2.1.211 plus SDK 0.3.207 list/read/resume passes.
- Partial frames, controls, and attachments remain independent capability gates.
- The `substrate-evidence/live-stream-frames` row stays `not-exercised` with the exact
  version-mismatch reason; a mismatched installed version never produces an observation.

### Todos

Update observations only from a later production-seam exercise with the same redaction policy.

## Docs References

No Domain Documentation source is configured; the production-seam observation is the fixture's
direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Foundation tests require this exact runtime/helper tuple and explicitly assert the helper observation stays not-exercised/unverified. | L102-L123 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The helper manifest pins the Claude SDK version named by this fixture. | L13-L16 | [package.json](agents-remember/mcp/native_helpers/conversation_library/package.json) |
| The installed honesty test enforces the version-mismatch `not-exercised` reason on this row. | L340-L362 | [test_harness_control_evidence_installed.py](agents-remember/mcp/tests/test_harness_control_evidence_installed.py) |

## Cross-Repo References

No neighboring repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the appended
  `substrate-evidence/live-stream-frames` row, kept honestly `not-exercised` because installed
  2.1.214 mismatches the locked 2.1.211 gate; `enablesCapabilities` stays false. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Claude installed-runtime fixture
  sidecar with the explicit unverified helper-history gate. Verification is blank until closeout
  commits and stamps the new source.
