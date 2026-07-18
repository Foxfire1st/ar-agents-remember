# mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through the installed Codex 0.144.5 production
discovery seam without claiming native history or active projector capability.

## Code Commentary

### Logic

The fixture identifies Codex 0.144.5, records only model/effort count and selected-field presence
from adapter discovery, marks native history list/read/resume and active projector items/events as
`not-exercised`, and fixes `enablesCapabilities` to false.

### Conventions

Runtime fixtures retain evidence shape/counts and safe reasons only. Model names, native ids, raw
frames, prompts, paths, credentials, and conversation material are discarded.

### Invariants And Boundaries

- Fixture presence never enables a capability.
- Installed version/count observations are evidence for this capture, not maintained product enums.
- History and active projection remain separately gated.

### Todos

Replace `not-exercised` observations only after later leaves pass the named production seams.

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

## Cross-Repo References

No neighboring repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Codex installed-runtime fixture
  sidecar. Verification is blank until closeout commits and stamps the new source.
