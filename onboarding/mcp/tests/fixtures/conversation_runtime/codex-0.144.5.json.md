# mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
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
real end-to-end codex open through the landed L0E channel.

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
replay, and leak-free retirement) — both `observed`, both evidence-not-enablement.

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

### Todos

Replace remaining `not-exercised` observations only after later leaves pass the named production
seams.

## Docs References

No Domain Documentation source is configured; the production-seam observation is the fixture's
direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Foundation tests parse this exact version tuple, require non-enablement, and scan all fixtures for raw secrets/paths/conversation material. | L102-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The runtime-fixture model requires allowlist-v1, at least one observation, and literal false enablement. | L1233-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The opt-in installed suite captures these `substrate-evidence/*` rows through the production seam and asserts their shapes. | L115-L273 | [test_harness_control_evidence_installed.py](agents-remember/mcp/tests/test_harness_control_evidence_installed.py) |
| The L2 installed-runtime suite produces the live gate and codex open evidence the `native-history/*` rows record. | L134-L214; L480-L539 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No neighboring repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
