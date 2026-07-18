# mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through installed Pi 0.80.7 discovery while
keeping dormant session discovery/resolution and structured messages/events/controls unverified.

## Code Commentary

### Logic

The fixture records the matching runtime/helper tuple, safe model-count and selected-model/effort
presence from the production RPC adapter, and `not-exercised` observations for native-library and
message/control behavior. It fixes `enablesCapabilities` to false.

### Conventions

Only allow-listed counts/field presence and safe reasons survive capture. Model/provider names,
session files, native ids, paths, raw frames, prompts, and secrets are discarded.

### Invariants And Boundaries

- The 0.80.7 dependency pin does not prove dormant session list/read/resume.
- Messages, entries, cursors, tools, images, abort, stats, compaction, retry, steer, and follow-up
  remain independent production gates.
- Fixture presence never enables a capability.

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

## Cross-Repo References

No neighboring repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Pi installed-runtime fixture
  sidecar with explicit native-library and structured-control gates. Verification is blank until
  closeout commits and stamps the new source.
