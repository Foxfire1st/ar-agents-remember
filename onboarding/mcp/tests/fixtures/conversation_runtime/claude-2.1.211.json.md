# mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Records redacted allow-listed evidence observed through installed Claude 2.1.211 discovery while
keeping the locked SDK 0.3.207 history handshake/list/read/resume capability explicitly unverified.

## Code Commentary

### Logic

The fixture records the runtime/helper tuple, safe model-count/selected-field presence from the
production adapter, and two `not-exercised` gates covering locked-helper history and stream/control/
attachment behavior. It fixes `enablesCapabilities` to false.

### Conventions

Only allow-listed counts/field presence and safe reasons survive capture. Names, ids, paths, raw
frames, prompts, and secrets are discarded.

### Invariants And Boundaries

- Exact dependency locking is not installed-runtime interoperability proof.
- Claude history remains unverified until 2.1.211 plus SDK 0.3.207 list/read/resume passes.
- Partial frames, controls, and attachments remain independent capability gates.

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

## Cross-Repo References

No neighboring repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the Claude installed-runtime fixture
  sidecar with the explicit unverified helper-history gate. Verification is blank until closeout
  commits and stamps the new source.
