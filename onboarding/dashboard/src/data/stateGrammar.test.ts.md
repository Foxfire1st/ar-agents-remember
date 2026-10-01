# dashboard/src/data/stateGrammar.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test. [1]
- The N1 agent-only-blocked pin (plural-only → awaiting-input; both slots → unchanged). [2]
- The renderer whose Panda literal the cross-surface suite pins to the same string. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
