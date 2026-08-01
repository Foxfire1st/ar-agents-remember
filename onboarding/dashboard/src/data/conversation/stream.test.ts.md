# dashboard/src/data/conversation/stream.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/stream.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stream lifecycle and watchdog behavior are covered with controlled sources. | L11-L335 | [stream.test.ts](stream.test.ts) |
| The production EventSource controller consumes these callbacks. | L1-L240 | [stream.ts](stream.ts) |
| The resume cursor the watchdog cases replay from is a minted brand, not an inline cast. | `eventCursor` | [../../test/fixtures/conversationWire.ts](../../test/fixtures/conversationWire.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests exercise this repository's conversation transport. | L1-L335 | [stream.test.ts](stream.test.ts) |

## Update History

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

- 2026-08-01T10:02+02:00 — 260731-EFA-L4 curator: No content impact: the whole diff against
  `abc7cbc` is two lines in the watchdog harness — the `type ActiveEventCursor` import became a
  value import of `test/fixtures/conversationWire.ts::eventCursor`, and
  `getResumeCursor: () => "evt-7" as ActiveEventCursor` became `() => eventCursor("evt-7")` (L149).
  The check that could have made this consequential: this card's claim is that the suite "verif[ies]
  resume cursors across quiet sleep/wake cycles", so the cursor VALUE is load-bearing here in a way
  it is not in the other converted files. I read the **four** assertions that consume it —
  `ControlledSource.instances[1].url` and `[2].url` must contain `after=evt-7` (L174, L189, L215,
  L237) — and
  the string is unchanged; `eventCursor` is a pure brand mint (`raw as ActiveEventCursor`) with no
  default and no transformation, so it cannot alter what the re-subscribe URL carries. Also verified
  all eleven cases across the two describes (`boot-window reconnect backoff` L55,
  `liveness watchdog` L132) are unchanged in name and order, that `ControlledSource` still models the
  EventSource lifecycle with fake timers, and that both citations still hold on the current
  335-line test and 242-line source. Added one reference row for the mint.

- 2026-07-24T13:17:50Z — Created for boot-aware reconnect and half-open stream regression coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.
