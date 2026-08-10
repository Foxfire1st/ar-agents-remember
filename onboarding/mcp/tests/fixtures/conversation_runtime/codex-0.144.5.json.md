# mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through the installed Codex 0.144.5 production
discovery seam without claiming active projector capability. 260718-CHATS-L0E appends
`substrate-evidence/*` rows observed through the production evidence seam: live frames, the
`thread/read` native page, the resume channel, and submission provenance. 260718-CHATS-L2 flips
`native-history/list-read-resume` to `observed` (the live production gate passed through the
direct app-server seam) and appends the `observed` `native-history/open-exact-resume` row for the
real end-to-end codex open through the landed L0E channel. 260718-CHATS-L2E appends four
`control-plane/*` rows observed through the production control seam on the same installed
0.144.5: the interrupt write/ack with interrupted settlement, the paged operation timeline, the
`localImage` asset submit, and the once-only withdrawal recovery — all `observed`, all
evidence-not-enablement.

## Code Commentary

### Logic

The fixture identifies Codex 0.144.5, records only model/effort count and selected-field presence
from adapter discovery, marks active projector items/events as `not-exercised`, and fixes
`enablesCapabilities` to false. The L0E rows record `substrate-evidence/live-frames-page`,
`substrate-evidence/native-page-thread-read`, `substrate-evidence/resume-thread-channel`, and
`substrate-evidence/submission-provenance` — all `observed`, all shape descriptors only. The L2
rows record `native-history/list-read-resume` (`thread/list`, `thread/read`,
`initialize/cliVersion`, `thread/resume-target` shapes; exact-locked-version gate passed;
historical tool/command completeness honestly partial) and `native-history/open-exact-resume`
(`open_terminal_session/resumeThreadId`, `thread/resume`, `catalog/vendorSessionId`,
`submission-authority/bridgeEpoch` shapes; the held-open fix round's real open, idempotent
replay, and leak-free retirement) — both `observed`, both evidence-not-enablement. The L2E rows
record `control-plane/interrupt-write-ack` (`turn/interrupt(threadId,turnId)`, accepted
acknowledgement, `vendorCorrelationId[turn]`, `turn/completed status[interrupted]`, settled
re-interrupt refused-typed), `control-plane/operation-timeline` (item kind/source/sequence,
`payloadDigestPresent`, `bridgeEpoch`), `control-plane/asset-local-image-submit` (`localImage`
input path, receipt raw `assetIds`, spool sha256 verification), and
`control-plane/withdrawal-recovery` (exact recovery text once, replay absent, tombstone timing
byte-preserved) — all `observed`, all shape descriptors only.

### Conventions

Runtime fixtures retain evidence shape/counts and safe reasons only. Model names, native ids, raw
frames, prompts, paths, credentials, and conversation material are discarded.

### Invariants And Boundaries

- Fixture presence never enables a capability.
- Installed version/count observations are evidence for this capture, not maintained product enums.
- Active projection remains separately gated.
- `substrate-evidence/*` rows retain only allow-listed counts, kinds, and field presence captured
  through the production adapter→bridge→IPC→client seam; ephemeral native-page refusal is recorded
  as a typed honesty boundary, not a failure.
- The L2 `native-history/*` rows record observed production-gate shapes only; `enablesCapabilities`
  stays false and capability support remains the live gate's decision.
- The L2E `control-plane/*` rows record observed interrupt/timeline/asset/recovery shapes only;
  they never enable the interrupt write, the timeline read, or the asset channel, and the settled
  re-interrupt refusal is recorded as a typed honesty boundary.

### Todos

Replace remaining `not-exercised` observations only after later leaves pass the named production
seams.

## Docs References

No Domain Documentation source is configured; the production-seam observation is the fixture's
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Foundation tests parse this exact version tuple, require non-enablement, and scan all fixtures for raw secrets/paths/conversation material. | `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement`; `test_runtime_fixtures_contain_no_raw_secret_path_or_conversation_material` | mcp/tests/test_conversation_foundation.py:163-188; mcp/tests/test_conversation_foundation.py:191-202 |
| The runtime-fixture model requires allowlist-v1, at least one observation, and literal false enablement. | "class RuntimeFixtureEvidence(WireModel):" | mcp/src/agents_remember/models/conversations/telemetry.py:89-89 |
| The opt-in installed suite captures these `substrate-evidence/*` rows through the production seam and asserts their shapes. | `test_live_evidence_family_and_resume_channel_through_production_seam` | mcp/tests/test_harness_control_evidence_installed.py:132-179 |
| The L2 installed-runtime suite produces the live gate and codex open evidence the `native-history/*` rows record. | `test_live_gate_supports_list_read_and_partial_completeness`; `test_open_real_codex_thread_proves_exact_identity` | mcp/tests/test_conversation_library_installed.py:136-153; mcp/tests/test_conversation_library_installed.py:495-551 |
| The L2E installed-runtime suite captures these `control-plane/*` rows through the production control seam and asserts their shapes. | `test_live_interrupt_timeline_assets_and_recovery` | mcp/tests/test_harness_control_plane_installed.py:142-266 |

## Cross-Repo References

No neighboring repository is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 5 citation rows with exact source anchors; scoped citation fixing regenerated their source ranges. No-domain and no-cross-repo placeholders remain explicit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `mcp/tests/test_conversation_library_installed.py`. Both halves had drifted across class
  boundaries. The live gate is `CodexInstalledTests` L136-L186
  (`test_live_gate_supports_list_read_and_partial_completeness` +
  `test_live_list_read_and_resolve_round_trip`), matching the range this repo's
  `library/codex.py.md` already carries; the codex open evidence is
  `CodexOpenEndToEndTests.test_open_real_codex_thread_proves_exact_identity` at L495-L551, whose
  end the old `L480-L539` cut off mid-replay-assertion. Read both ranges back.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the four appended
  `control-plane/*` rows (interrupt write/ack with interrupted settlement and the settled
  typed refusal, the paged operation timeline, the `localImage` asset submit, the once-only
  withdrawal recovery); `enablesCapabilities` stays false, pre-existing rows are byte-preserved,
  and the fixture remains evidence-not-enablement. Verification metadata stays pinned until
  closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the flipped
  `native-history/list-read-resume` row (`observed` through the direct app-server production
  gate with the exact locked CLI version) and the appended `native-history/open-exact-resume`
  row (the held-open fix round's real end-to-end codex open through the landed L0E resume
  channel); `enablesCapabilities` stays false and the fixture remains evidence-not-enablement.
  Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the appended redacted
  `substrate-evidence/*` rows (live frames page, thread/read native page with the typed ephemeral
  refusal, resume channel, submission provenance); `enablesCapabilities` stays false and no L1/L2
  row flipped. Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Codex installed-runtime fixture
  sidecar. Verification is blank until closeout commits and stamps the new source.
