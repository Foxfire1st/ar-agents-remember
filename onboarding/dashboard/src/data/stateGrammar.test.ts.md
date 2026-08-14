# dashboard/src/data/stateGrammar.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/stateGrammar.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the seat-state grammar — the spec §2.4 mapping and the
pulse ruling pinned as behavior. The `liveTurnWorking`
display-preference pins: the projection-derived working signal overrides a lagging catalog
`turn-ended`, but slots BELOW the terminal/fault/blocked guards so it can never fake liveness over a
real end state. The plural-pending pins: a seat blocked SOLELY on a
multiplexed sub-agent approval (singular slot absent, plural list non-empty) is awaiting-input, and
both-slots-present leaves the parent presentation unchanged.

## Code Commentary

### Logic

- **Mapping cases** — working = cyan SLOW PULSE; awaiting-input = STEADY amber (the
  blocked-on-human-never-flickers doctrine); waiting(reason) = STEADY muted-amber with the reason
  rendered into word AND chip; failed = alarm SLOW PULSE and outranks turn-state; ready/turn-ended
  = steady mint; landed/retired = dormant and outrank every live signal; starting = cyan steady;
  unclassified stays unclassified and stale stays stale (mirrors, never invents).
- **liveTurnWorking override** — `seatVisualState({ turnState: "turn-ended",
  liveTurnWorking: true })` resolves to `working`: the sub-second projection signal is PREFERRED over
  the sweep-lagging catalog `turn-ended`.
- **liveTurnWorking never over an end state (R9 honesty pin)** — the signal slots BELOW the
  terminal/fault/blocked guards, so `liveTurnWorking: true` cannot resurrect a real end state:
  with `status: "terminated"` it stays `retired`, with `controlState: "failed"` it stays `failed`,
  and with a pending approval interaction it stays blocked. This is the guard-order proof that the
  display preference can never fake liveness over a genuine terminal/fault/blocked state.
- **Plural pending = awaiting-input (N1)** — with the singular slot absent and the
  plural list carrying one sub-agent permission entry (adapter-bound `raw: { threadId, agentLabel }`),
  `seatVisualState` returns STEADY amber `awaiting-input` — the attention grammar must not go dark
  on an agent-only block. With BOTH slots present the parent presentation is unchanged (same
  awaiting-input, no new word/chip).
- **The pulse ruling** — asserts `PULSE_ANIMATION` is the 2.4 s ease-in-out string and contains NO
  `steps(` — the reviewer additionally greps the diff for `steps(` additions at review time.

### Invariants And Boundaries

The ruling case pins constants exported for exactly this purpose; changing pulse timing or easing
must fail here first. Test-only.

### 2026-07-24 Curator Delta

The state-grammar tests now pin the fresh-chat trajectory: starting remains visibly booting, while a
ready control with no turn claim is calm idle rather than stale or fabricated turn-ended.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `seatVisualState` | dashboard/src/data/stateGrammar.ts:101-125 |
| The N1 agent-only-blocked pin (plural-only → awaiting-input; both slots → unchanged). | `controlPendingInteractions` | dashboard/src/data/stateGrammar.test.ts:37-62 |
| The renderer whose Panda literal the cross-surface suite pins to the same string. | "pulseSlow 2.4s ease-in-out infinite" | dashboard/src/panels/session-cockpit/StateDot.tsx:27-33 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T17:45+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the three Repo-Internal
  citation rows — rebound the module under test to `seatVisualState`, the N1 agent-only-blocked pin
  to `controlPendingInteractions`, and the cross-surface pulse renderer row to the exact Panda
  literal, each with exact frozen-source ranges regenerated by the scoped fixer. No claim wording
  changed; evidence was already accurate.
- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the two N1 plural-pending pins — a seat
  blocked SOLELY on a multiplexed sub-agent approval (singular slot absent, plural non-empty, with
  adapter-bound `raw.agentLabel`) is awaiting-input, and both-slots-present keeps the parent
  presentation unchanged. Verification stays pinned; the L7 change is uncommitted and closeout
  re-stamps.

- 2026-07-24T13:17:50Z — Added fresh-chat state-honesty coverage. Verification hash/date remain
  pinned to the pre-commit source stamp.

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
