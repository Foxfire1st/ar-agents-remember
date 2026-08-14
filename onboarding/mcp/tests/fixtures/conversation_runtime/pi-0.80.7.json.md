# mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through installed Pi 0.80.7 discovery while
keeping structured messages/events/controls unverified. 260718-CHATS-L0E appends
`substrate-evidence/*` rows observed through the production evidence seam: live frames, the
`get_entries` native page, and submission provenance. 260718-CHATS-L2 flips
`locked-helper/list-listAll-resolve` to `observed`: the locked helper handshakes `ready` against
installed 0.80.7 and `SessionManager` list/branch-read/session-file resolution passed through the
production helper seam, with the exact `--session` open proven end-to-end. 260718-CHATS-L2E
appends three `control-plane/*` rows observed through the production control seam on the same
installed 0.80.7: the identity-guarded abort write/ack, the paged operation timeline, and the
base64 image asset submit — all `observed`, all evidence-not-enablement.

## Code Commentary

### Logic

The fixture records the matching runtime/helper tuple, safe model-count and selected-model/effort
presence from the production RPC adapter, and `not-exercised` observations for message/control
behavior. It fixes `enablesCapabilities` to false. The L0E rows record
`substrate-evidence/live-frames-page`, `substrate-evidence/native-page-get-entries`, and
`substrate-evidence/submission-provenance` — all `observed`, all shape descriptors only. The L2
row records `locked-helper/list-listAll-resolve` (`handshake/ready`, `SessionManager.list`,
`SessionManager.open+getBranch`, `resolve/sessionFile` shapes; the production gate passed and a
real end-to-end open proved exact catalog identity through the tracked opener) — `observed`,
evidence-not-enablement. The L2E rows record `control-plane/abort-write-ack` (RPC abort command,
accepted acknowledgement, active-operation identity on the result, stale `expectedOperationId`
refused-typed), `control-plane/operation-timeline` (item kind/source/sequence, `bridgeEpoch`),
and `control-plane/asset-image-submit` (prompt `images[{type,mimeType,data}]`, receipt raw
`assetIds`, spool sha256 verification) — all `observed`, all shape descriptors only.

### Conventions

Only allow-listed counts/field presence and safe reasons survive capture. Model/provider names,
session files, native ids, paths, raw frames, prompts, and secrets are discarded.

### Invariants And Boundaries

- The 0.80.7 dependency pin does not prove dormant session list/read/resume; the observed L2 row
  records the production-seam proof without enabling a capability.
- Messages, entries, cursors, tools, images, abort, stats, compaction, retry, steer, and follow-up
  remain independent production gates.
- Fixture presence never enables a capability.
- `substrate-evidence/*` rows retain only allow-listed counts, kinds, and field presence captured
  through the production adapter→bridge→IPC→client seam.
- The L2E `control-plane/*` rows retain only allow-listed field presence from the abort/timeline/
  image submissions; they never enable the interrupt write, the timeline read, or the asset
  channel, and the stale-identity refusal is recorded as a typed honesty boundary.

### Todos

Update remaining `not-exercised` observations only after the named Pi production seams pass with
the same redaction policy.

## Docs References

No Domain Documentation source is configured; the production-seam observation is the fixture's
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Foundation tests require this exact runtime/helper tuple, false enablement, and raw-free fixture set. | `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement` | mcp/tests/test_conversation_foundation.py:163-188 |
| The helper manifest pins the Pi package version named by this fixture. | "0.80.7" | mcp/native_helpers/conversation_library/package.json:15-15 |
| The fixture records the live-frames substrate evidence shape used by the installed evidence suite. | "substrate-evidence/live-frames-page" | mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json:40-40 |
| The opt-in installed evidence suite exercises and asserts the Pi production-seam shapes. | `PiInstalledEvidenceTests` | mcp/tests/test_harness_control_evidence_installed.py:281-352 |
| The fixture records the "locked-helper/list-listAll-resolve" operation with `result` set to `observed`. | "\"operation\": \"locked-helper/list-listAll-resolve\", \"shape\": [ \"handshake/ready\", \"SessionManager.list\", \"SessionManager.open+getBranch\", \"resolve/sessionFile\" ], \"result\": \"observed\"" | mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json:23-30 |
| The installed library suite verifies the live gate, list/read/resolve, and exact-identity open behavior. | `test_live_list_read_resolve` | mcp/tests/test_conversation_library_installed.py:233-263 |
| The fixture records the control-plane abort-write shape. | "control-plane/abort-write-ack" | mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json:72-72 |
| The installed control-plane suite exercises and asserts the corresponding Pi abort, timeline, and asset behavior. | `PiInstalledControlPlaneTests` | mcp/tests/test_harness_control_plane_installed.py:269-373 |

## Cross-Repo References

No neighboring repository is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residual D1 by binding the locked-helper operation and its structured `result: observed` value as pooled evidence, with no gate-field claim; rechecked this card through the locked exact-document fixer/check.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `mcp/tests/test_conversation_library_installed.py`. The live-helper-gate range is now L217-L263
  (`test_live_helper_gate_supports_pi_history` L217-L231, asserting the locked runtime and helper
  version 0.80.7, plus `test_live_list_read_resolve` L233-L263, which ends on the exact `--session`
  file proof), and the real-open range is now L366-L413
  (`test_open_real_pi_session_proves_exact_identity`); the old L360-L479 spilled into
  `CodexOpenEndToEndTests`.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the three appended
  `control-plane/*` rows (identity-guarded abort write/ack with the stale-identity typed refusal,
  the paged operation timeline, the base64 image asset submit); `enablesCapabilities` stays
  false, pre-existing rows are byte-preserved, and the fixture remains evidence-not-enablement.
  Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the flipped
  `locked-helper/list-listAll-resolve` row (`observed` through the locked-helper production gate
  plus the real end-to-end `--session` open); `enablesCapabilities` stays false and the fixture
  remains evidence-not-enablement. Verification metadata stays pinned until closeout stamps the
  candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the appended redacted
  `substrate-evidence/*` rows (live frames page, get_entries native page, submission provenance);
  `enablesCapabilities` stays false and no L1/L2 row flipped. Verification metadata stays pinned
  until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Pi installed-runtime fixture
  sidecar with explicit native-library and structured-control gates. Verification is blank until
  closeout commits and stamps the new source.
