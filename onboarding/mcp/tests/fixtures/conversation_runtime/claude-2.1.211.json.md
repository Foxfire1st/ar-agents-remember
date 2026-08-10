# mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through installed Claude 2.1.211 discovery while
keeping the locked SDK 0.3.207 history handshake/list/read/resume capability explicitly unverified.
260718-CHATS-L0E appends one honestly `not-exercised` `substrate-evidence/live-stream-frames` row
because the installed 2.1.214 mismatches the locked 2.1.211 gate. 260718-CHATS-L2 records the
implemented locked helper's shapes on that same row: the helper handshakes `incompatible` against
the installed 2.1.214 (locked 2.1.211), so the row stays `not-exercised` with the exact reason
while the list/read/resolve shapes are proven through the production helper seam.
260718-CHATS-L2E appends one honestly `not-exercised` `control-plane/interrupt-and-assets` row:
the installed 2.1.214 mismatches the locked gate and the bundle's interrupt/image contracts
remain unproven headless (CL-3), so the bridge-side typed refusal stays the honest posture.

## Code Commentary

### Logic

The fixture records the runtime/helper tuple, safe model-count/selected-field presence from the
production adapter, and two `not-exercised` gates covering locked-helper history and stream/control/
attachment behavior. It fixes `enablesCapabilities` to false. The L0E row records that live stream
frame and usage/cost forwarding through the production evidence seam remains unverified until a
locked 2.1.211 install exercises it — version honesty rather than a guessed observation. The L2
row records the implemented helper's `handshake/incompatible`, `listSessions`,
`getSessionMessages`, and `getSessionInfo` shapes: production-exercised against the installed
runtime, honestly failing the locked-version gate, capabilities unverified until a real installed
2.1.211 history passes the replay gate. The L2E row records `control-plane/interrupt-and-assets`
as `not-exercised` with the exact reason: installed 2.1.214 mismatches the locked 2.1.211 gate
and the bundle's interrupt/image contracts remain unproven headless (CL-3); the bridge-side
typed refusal is the honest posture until a locked install exercises the control-plane seam.

### Conventions

Only allow-listed counts/field presence and safe reasons survive capture. Names, ids, paths, raw
frames, prompts, and secrets are discarded.

### Invariants And Boundaries

- Exact dependency locking is not installed-runtime interoperability proof.
- Claude history remains unverified until 2.1.211 plus SDK 0.3.207 list/read/resume passes.
- Partial frames, controls, and attachments remain independent capability gates.
- The `substrate-evidence/live-stream-frames` row stays `not-exercised` with the exact
  version-mismatch reason; a mismatched installed version never produces an observation.
- The L2 helper row records shapes and the incompatible handshake only; `enablesCapabilities`
  stays false and the version-mismatch reason is exact.
- The L2E `control-plane/interrupt-and-assets` row stays `not-exercised` with the exact
  version-mismatch + CL-3 headless-unproven reason; a mismatched or unproven install never
  produces an observation.

### Todos

Update observations only from a later production-seam exercise with the same redaction policy.

## Docs References

No Domain Documentation source is configured; the production-seam observation is the fixture's
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Foundation tests require this exact runtime/helper tuple and explicitly assert the helper observation stays not-exercised/unverified. | `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement` | mcp/tests/test_conversation_foundation.py:163-188 |
| The helper manifest pins the Claude SDK version named by this fixture. | `test_helper_package_and_lock_select_only_the_exact_repository_dependencies` | mcp/tests/test_conversation_foundation.py:125-136 |
| The installed honesty test enforces the version-mismatch `not-exercised` reason on this row. | `ClaudeInstalledHonestyTests` | mcp/tests/test_harness_control_evidence_installed.py:379-402 |
| The L2 installed suite proves the implemented helper's incompatible handshake on the real machine. | `ClaudeGateHonestyTests` | mcp/tests/test_conversation_library_installed.py:587-622 |
| The L2E installed honesty test enforces the version-mismatch `not-exercised` reason on the `control-plane/interrupt-and-assets` row. | `ClaudeInstalledHonestyTests` | mcp/tests/test_harness_control_plane_installed.py:376-394 |

## Cross-Repo References

No neighboring repository is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 10 citation findings; scoped check passed.

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the appended
  `control-plane/interrupt-and-assets` row, kept honestly `not-exercised` with the exact
  version-mismatch + CL-3 headless-unproven reason (the bridge-side typed refusal is the honest
  posture); `enablesCapabilities` stays false and pre-existing rows are byte-preserved.
  Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the updated
  `locked-helper/handshake-list-read-resume` row: the implemented helper production-exercised its
  shapes and fails closed `incompatible` because installed 2.1.214 differs from the locked 2.1.211
  gate; the row stays `not-exercised`, `enablesCapabilities` stays false. Verification metadata
  stays pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the appended
  `substrate-evidence/live-stream-frames` row, kept honestly `not-exercised` because installed
  2.1.214 mismatches the locked 2.1.211 gate; `enablesCapabilities` stays false. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Claude installed-runtime fixture
  sidecar with the explicit unverified helper-history gate. Verification is blank until closeout
  commits and stamps the new source.
