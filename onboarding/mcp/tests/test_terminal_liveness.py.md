# test_terminal_liveness.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Retains the liveness behavior at the sweeper boundary: transient failures stay within the hysteresis window, full catalog probes remain rate-limited by the configured interval, and starting rows use the one-second bounded path. Fake probes, snapshots, and a controlled clock model those boundaries. These tests do not claim lifecycle caller ownership or production wiring.
## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. The transient-failure case
keeps sessions running while the hysteresis window has not elapsed. The full-sweep case keeps the
configured ten-second admission gate intact. The starting-row case proves the one-second
eligibility boundary, four-row targeted cap, and persisted readiness transition for a fifth row on
the following tick. Earlier coverage claims in history describe prior populations and must not be
used to recreate removed tests or claim they still run.

The current evidence boundary is the source-listed behavior below. `_FakeHost` parks inside
`probe_session` on events so the first sweep holds the sweeper lock and the catalog batch while a
contender runs; `_RaisingHost` raises on its first probe to force the lock-release path. The
contended-full case asserts the contender returns before its 0.25 s join, that the host was probed
only once across both callers, and that a later `refresh()` probes again. The contended-starting
case drives the one-second starting fast path with the full-sweep rate limit in force and asserts
the first sweep was the only probe across both callers. The clean-hosted case wraps
`catalog._write_disk` and asserts one replacement on the first sweep and zero on an identical
second sweep. 
### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.
This inventory covers the composed module: siblings `260831-LOCR-L12` and `260831-LOCR-L21` and this
leaf `260831-LOCR-L22` have all landed on the LOCR master integration branch, so the rows above are
the module's complete retained case set and every cited range was derived from that composed file.
### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Keep full-sweep rate limiting inside `TerminalCatalogLivenessSweeper` and keep the
one-second starting-row path bounded at four rows; the lifecycle cadence and production wiring
remain owned by the assembled L01/R16/R18 candidate. Coverage percentages are diagnostic and
production CRAP 20 prompts review; neither implies an obligation to restore removed cases. Full
suites and whole-candidate review remain master-end work. This source inspection does not claim a
newly executed test or acceptance result.
### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Fake fixtures configure and drive the existing host/control-read seams [1]
- The raising probe double that forces the lock-release path [2]
- Host failures retain the count-plus-window gate, exit-mark and immediate pane-gone transition [3]
- Full sweeps remain rate-limited by the configured interval [4]
- Starting rows use the one-second path and four-row cap [5]
- Host failure evidence survives reload and clears after a successful probe [6]
- Connected bridge failures require three strikes across reload and reset on success [7]
- Alive starting rows remain eligible through delayed bridge reads [8]
- A contended full sweep returns without waiting and without a second probe [9]
- The sweep lock releases after an observation exception so a later cadence retries [10]
- A contended starting-row sweep reads the committed snapshot before any catalog list [11]
- A repeated clean hosted sweep performs zero physical replacements [12]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
