# mcp/src/agents_remember/package_data/paseo_plugin/server/identity_mismatch.test.ts

## Governing Overview

[Native Paseo plugin](../overview.md)

## Purpose

Host-free Node test suite verifying `IDENTITY MISMATCH:` line extraction, immediate parent delivery without 60 s waiting or seat self-wakes across all leaf roles, in-turn parent holding and flushing, archived-parent Manager fallback, cancellation of prior declared waits, and preservation of normal silent-end behavior.

## Code Commentary

- Drives `extractIdentityMismatchLine`, `composeIdentityMismatchParentLine`, and `turn_ended.ts` (`createTurnEndedTracker`, `noteTurnEnded`, `noteTurnStarted`, `noteAgentArchived`, `openDeclaredWait`) using `turn_test_fakes.ts` (`endSeatTurn`, `fakeClock`, `hostState`, `makeSender`).
- Declares 8 `test(...)` calls (no `describe` blocks), including one `for` loop over `["worker", "reviewer", "curator"]`, producing 10 runtime test cases covering extraction edge cases, all three leaf roles, Markdown-wrapped lines, in-turn parent queuing/draining, archived-parent Manager fallback, cancellation of pending wakes/declared waits, and a normal silent-end control case.
- Pure host-free unit/decision tests; does not establish live Paseo plugin loading or SDK event delivery.

## Relationships

- **Runner:** `mcp/src/agents_remember/package_data/paseo_plugin/package.json` `test` script (`node --experimental-strip-types --test server/*.test.ts`).
- **Code under test:** `identity_mismatch.ts` and `turn_ended.ts`.
- **Support:** `turn_test_fakes.ts`.

## Evidence

- Extraction tests cover plain, trimmed, and Markdown-wrapped prefixes, interior backtick preservation, 300-character truncation, and lowercase, mid-line, empty, and unreadable rejections. [1]
- All three leaf roles (`worker`, `reviewer`, `curator`) deliver mismatch lines immediately to an idle parent with zero timers, zero seat wakes, unchanged `silentEnds`, and an `identity-mismatch` log row. [2]
- Wrapped mismatch lines strip symmetric outer quotes and backticks cleanly, preserve pre-existing `silentEnds`, and match `composeIdentityMismatchParentLine`. [3]
- Parent-routing cases verify hold-and-flush while the parent is in a turn, Manager fallback when the parent is archived, cancellation of an open declared wait, and intact 60 s silent-end handling. [4]
