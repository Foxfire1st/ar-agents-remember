# mcp/tests/fixtures/codex_app_server_model_page.json

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

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The captured page is a single complete row with a null cursor, the shape the session's model reader validates. [1]
- The live case opens its thread with the model this page describes. [2]

### Cross-Repo References

Captured from the external Codex CLI app-server `model/list` method.

- The row carries the vendor's own model id, display name and reasoning-effort list. [3]
