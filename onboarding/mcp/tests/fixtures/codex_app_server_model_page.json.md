# mcp/tests/fixtures/codex_app_server_model_page.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/codex_app_server_model_page.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:15+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

**One captured real `model/list` page**, added by `260915-CAPS-L5` so the live-native case can resolve
the model it opens its thread with without inventing vendor rows. It holds a single row
(`gpt-5.6-sol`, with its `description` and `supportedReasoningEfforts`) and `nextCursor: null`, which
is exactly the shape the session's own model reader requires.

The leaf's first fixture drafts were **hand-written** and were rejected by the production parser
(`L5-EV1`/`L5-EV2`: an invented `userAgent` and rows missing the `description` the reader requires).
The durable answer was to capture the vendor's real replies and pin those, which is why this file
exists as a verbatim page rather than a plausible-looking one.

## Code Commentary

### Conventions

Pinned to the installed CLI version with the instruction-channel fixture; regenerate by capturing a
real `model/list` response. Read by the test, never imported from the module under test.

### Invariants And Boundaries

- The fixture is an *expiry* artifact: the next installed app-server version change invalidates it.
- It carries no credential, no prompt and no user data — only vendor catalog metadata.
- It proves the reader accepts a real page; it is not evidence about which model a caller should pick.

### Todos

Regenerate on the next pinned-CLI change.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The captured page is a single complete row with a null cursor, the shape the session's model reader validates. | "\"data\"" | mcp/tests/fixtures/codex_app_server_model_page.json:2-2 |
| The live case opens its thread with the model this page describes. | `test_live_app_server_observes_instruction_sources_and_accepts_the_capsule` | mcp/tests/test_codex_capsule_delivery.py:1208-1256 |

## Cross-Repo References

Captured from the external Codex CLI app-server `model/list` method.

| Finding | Anchor | Source |
| --- | --- | --- |
| The row carries the vendor's own model id, display name and reasoning-effort list. | "\"displayName\"" | mcp/tests/fixtures/codex_app_server_model_page.json:9-9 |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: created onboarding for the captured `model/list`
  page, recording why a captured page replaced the hand-written draft the production parser rejected,
  its single-row/null-cursor shape, and its expiry contract. `governingOverview` is `../overview.md`
  (the route-local `mcp/tests/overview.md` the census names as this source's nearest governing route).
  Verification metadata stays pinned to the last committed source (`c1dbebf8`).
