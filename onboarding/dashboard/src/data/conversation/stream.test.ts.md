# dashboard/src/data/conversation/stream.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/stream.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

Regression coverage for conversation-stream boot retry, half-open liveness recovery, and honest
never-open escalation.

## Code Commentary

### Logic

`ControlledSource` simulates EventSource lifecycle events. Tests distinguish the fast pre-first-open
retry from established reconnects, verify resume cursors across quiet sleep/wake cycles, constrain idle
backstop cycles to one episode, and require an open deadline to signal a genuinely never-open stream.

### Conventions

Fake timers model suspended wall-clock time without inventing browser transport events.

### Invariants And Boundaries

A quiet recovery must not flash a disconnect, but a replacement subscribe that never opens must not retain
a live-looking state.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Stream lifecycle and watchdog behavior are covered with controlled sources. | `ControlledSource`; "boot-window reconnect backoff (260718-CHATS-L5I A3)"; "liveness watchdog (260723 sleep/wake + half-open wedge)" | dashboard/src/data/conversation/stream.test.ts:18-34; dashboard/src/data/conversation/stream.test.ts:55-130; dashboard/src/data/conversation/stream.test.ts:132-335 |
| The production EventSource controller consumes these callbacks. | `openConversationStream` | dashboard/src/data/conversation/stream.ts:86-242 |
| The `openWatched` harness supplies the watchdog replay cursor. | `openWatched` | dashboard/src/data/conversation/stream.test.ts:141-153 |
| The replay cursor is minted by the `eventCursor` brand constructor. | `eventCursor` | dashboard/src/test/fixtures/conversationWire.ts:58-60 |
| The first watchdog replay assertion requires the resumed URL to contain `after=evt-7`. | "expect(ControlledSource.instances).toHaveLength(2); // fresh subscribe, SAME cursor — no re-page expect(ControlledSource.instances[1].url).toContain(\"after=evt-7\")" | dashboard/src/data/conversation/stream.test.ts:173-174 |
| The established reconnect assertion requires the resumed URL to contain `after=evt-7`. | "vi.advanceTimersByTime(2_000); // established backoff, not the boot cadence expect(ControlledSource.instances).toHaveLength(3); expect(ControlledSource.instances[2].url).toContain(\"after=evt-7\")" | dashboard/src/data/conversation/stream.test.ts:187-189 |
| The watchdog backstop assertion requires the resumed URL to contain `after=evt-7`. | "vi.advanceTimersByTime(5_000); expect(ControlledSource.instances[0].closed).toBe(true); expect(ControlledSource.instances).toHaveLength(2); expect(ControlledSource.instances[1].url).toContain(\"after=evt-7\")" | dashboard/src/data/conversation/stream.test.ts:212-215 |
| The visibility-recovery assertion requires the resumed URL to contain `after=evt-7`. | "document.dispatchEvent(new Event(\"visibilitychange\")); expect(ControlledSource.instances).toHaveLength(2); expect(ControlledSource.instances[1].url).toContain(\"after=evt-7\")" | dashboard/src/data/conversation/stream.test.ts:235-237 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-04T14:59:10+02:00 — 260731-EFA-L6 S18-B12 curator: completed the whole-claim cursor audit by splitting the `openWatched` setup, `eventCursor` brand definition, and four exact `after=evt-7` replay assertions; scoped fixer generated the final ranges.
- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **corrected the assertion count
  in the 10:02 entry below.** It said "the two assertions that consume it … (L174, L189)". There are
  **four** `after=evt-7` assertions in the `liveness watchdog` describe — L174, L189, **L215** and
  **L237** — all four `expect(ControlledSource.instances[…].url).toContain("after=evt-7")` against the
  same unchanged literal (`grep -n "after=evt-7"` over the working tree returns exactly those four
  lines). The verdict is unaffected: `eventCursor` is a pure brand mint with no default and no
  transformation, so none of the four can move, and reading only two of them understated the coverage
  rather than the risk. Re-verified the surviving citations while here: `stream.test.ts` is 335 lines
  so `L11-L335` and the cross-repo `L1-L335` hold; `eventCursor` is at
  `../../test/fixtures/conversationWire.ts` L58; the conversion itself is at L149
  (`getResumeCursor: () => eventCursor("evt-7")`); and the eleven cases across the two describes
  (`boot-window reconnect backoff` L55 with four, `liveness watchdog` L132 with seven) are unchanged
  in name and order. Verification metadata untouched.

- 2026-08-01T10:02+02:00 — 260731-EFA-L4 curator: the watchdog harness supplies
  `getResumeCursor: () => eventCursor("evt-7")`, and the four `after=evt-7` assertions remain in
  place across the liveness cases; the current table carries the generated cursor and watchdog
  citations.
  The current-state cursor is a pure brand mint and the suite continues to exercise quiet sleep/wake
  recovery without changing the resumed URL.
- 2026-07-24T13:17:50Z — Created for boot-aware reconnect and half-open stream regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
