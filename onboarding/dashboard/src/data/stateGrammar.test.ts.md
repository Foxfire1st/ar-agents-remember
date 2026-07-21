# dashboard/src/data/stateGrammar.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/stateGrammar.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`       |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the seat-state grammar (260715-FEUI-L2 R14) — the spec §2.4 mapping and the
developer pulse ruling pinned as behavior. 260718-CHATS-L5F R9 adds the `liveTurnWorking`
display-preference pins: the projection-derived working signal overrides a lagging catalog
`turn-ended`, but slots BELOW the terminal/fault/blocked guards so it can never fake liveness over a
real end state.

## Code Commentary

### Logic

- **Mapping cases** — working = cyan SLOW PULSE; awaiting-input = STEADY amber (the
  blocked-on-human-never-flickers doctrine); waiting(reason) = STEADY muted-amber with the reason
  rendered into word AND chip; failed = alarm SLOW PULSE and outranks turn-state; ready/turn-ended
  = steady mint; landed/retired = dormant and outrank every live signal; starting = cyan steady;
  unclassified stays unclassified and stale stays stale (mirrors, never invents).
- **liveTurnWorking override (260718-CHATS-L5F R9)** — `seatVisualState({ turnState: "turn-ended",
  liveTurnWorking: true })` resolves to `working`: the sub-second projection signal is PREFERRED over
  the sweep-lagging catalog `turn-ended`.
- **liveTurnWorking never over an end state (R9 honesty pin)** — the signal slots BELOW the
  terminal/fault/blocked guards, so `liveTurnWorking: true` cannot resurrect a real end state:
  with `status: "terminated"` it stays `retired`, with `controlState: "failed"` it stays `failed`,
  and with a pending approval interaction it stays blocked. This is the guard-order proof that the
  display preference can never fake liveness over a genuine terminal/fault/blocked state.
- **The pulse ruling** — asserts `PULSE_ANIMATION` is the 2.4 s ease-in-out string and contains NO
  `steps(` — the reviewer additionally greps the diff for `steps(` additions at review time.

### Invariants And Boundaries

The ruling case pins constants exported for exactly this purpose; changing pulse timing or easing
must fail here first. Test-only.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L12-L106 | [stateGrammar.ts](stateGrammar.ts) |
| The renderer whose Panda literal the cross-surface suite pins to the same string. | L27-L33 | [../panels/session-cockpit/StateDot.tsx](../panels/session-cockpit/StateDot.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the two R9 `liveTurnWorking` pins —
  the projection working signal overrides a lagging catalog `turn-ended`, and the guard-order proof
  that it NEVER fakes liveness over a terminal/fault/blocked state. Verification stays pinned; the
  L5F change is uncommitted and closeout re-stamps.
- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R14/R11): the per-state mapping matrix,
  precedence checks, the rendered-ready waiting(reason) case, and the no-steps 2.4 s ease-in-out
  pulse-ruling pin. Verification metadata pinned to the leaf base until closeout stamps the L2
  code commit.
