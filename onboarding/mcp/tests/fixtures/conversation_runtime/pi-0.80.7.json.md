# mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash |  `ca9dd05a295ef5f24c479e2231fdcd174b372e04`|
| lastVerifiedCommitDate |  2026-07-19T10:04:45+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through installed Pi 0.80.7 discovery while
keeping dormant session discovery/resolution and structured messages/events/controls unverified.
260718-CHATS-L0E appends `substrate-evidence/*` rows observed through the production evidence
seam: live frames, the `get_entries` native page, and submission provenance.

## Code Commentary

### Logic

The fixture records the matching runtime/helper tuple, safe model-count and selected-model/effort
presence from the production RPC adapter, and `not-exercised` observations for native-library and
message/control behavior. It fixes `enablesCapabilities` to false. The L0E rows record
`substrate-evidence/live-frames-page` (transcript and `pi:message_update` frames with the full
`message_end` frame, bridge epoch, and `snapshot.raw.arEvidence` absent),
`substrate-evidence/native-page-get-entries` (typed native identity over durable entries), and
`substrate-evidence/submission-provenance` (cockpit source with epoch scoping) — all `observed`,
all shape descriptors only.

### Conventions

Only allow-listed counts/field presence and safe reasons survive capture. Model/provider names,
session files, native ids, paths, raw frames, prompts, and secrets are discarded.

### Invariants And Boundaries

- The 0.80.7 dependency pin does not prove dormant session list/read/resume.
- Messages, entries, cursors, tools, images, abort, stats, compaction, retry, steer, and follow-up
  remain independent production gates.
- Fixture presence never enables a capability.
- `substrate-evidence/*` rows retain only allow-listed counts, kinds, and field presence captured
  through the production adapter→bridge→IPC→client seam.

### Todos

Update observations only after the named Pi production seams pass with the same redaction policy.

## Docs References

No Domain Documentation source is configured; the production-seam observation is the fixture's
direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Foundation tests require this exact runtime/helper tuple, false enablement, and raw-free fixture set. | L102-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The helper manifest pins the Pi package version named by this fixture. | L13-L16 | [package.json](agents-remember/mcp/native_helpers/conversation_library/package.json) |
| The opt-in installed suite captures these `substrate-evidence/*` rows through the production seam and asserts their shapes. | L273-L340 | [test_harness_control_evidence_installed.py](agents-remember/mcp/tests/test_harness_control_evidence_installed.py) |

## Cross-Repo References

No neighboring repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the appended redacted
  `substrate-evidence/*` rows (live frames page, get_entries native page, submission provenance);
  `enablesCapabilities` stays false and no L1/L2 row flipped. Verification metadata stays pinned
  until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Pi installed-runtime fixture
  sidecar with explicit native-library and structured-control gates. Verification is blank until
  closeout commits and stamps the new source.
