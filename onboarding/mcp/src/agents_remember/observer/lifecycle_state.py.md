# mcp/src/agents_remember/observer/lifecycle_state.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `mcp/src/agents_remember/observer/lifecycle_state.py` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-07-31T00:00+02:00                               |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`           |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                        |

## Purpose

`lifecycle_state.py` is the pure state vocabulary of the observable lifecycle:
the `State` and `Phase` literal types, the `LifecycleState` record, the typed
errors a signal raises, and the `coerce_phase` boundary validator. It has no I/O,
so the later projection reducer can import the types without pulling in the
ambient singleton's threading.

## Code Commentary

`State = Literal["running","paused","blocked","awaiting-developer","completed",
"abandoned"]` — one at a time; `completed`/`abandoned` are terminal; `paused` is
system-owned (no model signal). `awaiting-developer` is the task-28
NOTIFY-AND-CONTINUE turn-end state: the model declares the turn complete and
stops — **non-terminal** (deliberately *not* added to `TERMINAL_STATES`),
auto-resumed by the next AR tool call (no gate, no wait), so it is a
notification, not a barrier. `Phase = Literal["request","trust-checkpoint","reframe-research",
"decide","build","close"]` — the session-lifecycle skill's heading vocabulary,
orthogonal to state. Derived constants: `TERMINAL_STATES`, `INITIAL_PHASE =
"request"`, and `PHASES = get_args(Phase)`.

`LifecycleError(AgentsRememberError)` is this domain's family base;
`GuardedStartError` names the active lifecycle in its message.
`LifecycleState` is a frozen dataclass (`id`, `state`, `phase`, `fleeting`,
`started_at`, plus the slice-2c persistence-binding fields `enclosure`,
`repo_id`, and `scope` — all `None` until the lifecycle is promoted) with an
`is_terminal` property — frozen so each transition is a new value (no
shared-mutable surprises across the request and heartbeat threads).
`coerce_phase(value)` validates a raw tool-boundary string into a `Phase` or
raises `LifecycleError`.

## Invariants And Boundaries

- Pure data + types: no I/O, no threading, no import from the ambient module —
  this is what lets the projection slice reuse the vocabulary cheaply.
- `paused` has no signal; it is observed/inferred by the system, never declared.
- `awaiting-developer` *is* model-declared (unlike `paused`) but stays
  non-terminal: it is not in `TERMINAL_STATES`, and `is_terminal` therefore stays
  `False` for it, so the next AR tool call can auto-resume it back to `running`.
- Frozen `LifecycleState`: transitions produce new values via `replace`.
- Boundary validation (`coerce_phase`) lives here; the ambient signal methods
  trust their already-typed `Phase`/`State` inputs.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The singleton that drives these states and raises these errors. | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The typed-error family base (`AgentsRememberError`). | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| The response models reuse `State`/`Phase` so the wire contract matches. | [models/lifecycle.py](agents-remember/mcp/src/agents_remember/models/lifecycle.py) |
| The design's state machine, signals, and phase axis (§1.2-1.4). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/observer/lifecycle_state.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 5 line(s), joining implicitly concatenated
  string literals back onto single lines. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): the `State`
  literal gained `"awaiting-developer"`, a non-terminal turn-end state
  (deliberately *not* added to `TERMINAL_STATES`, so `is_terminal` stays `False`).
  The model declares the turn complete and stops; the next AR tool call
  auto-resumes it to `running` (no gate, no wait). Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-13T18:45+02:00: Slice 2c — `LifecycleState` gained the persistence-binding
  fields `enclosure`/`repo_id`/`scope` (`None` until promotion) so a promoted
  lifecycle's events carry its contract anchor and landing-zone scope. Verification
  metadata is pinned until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00: Created for slice 2b — the lifecycle state/phase
  vocabulary, `LifecycleState`, the typed errors, and `coerce_phase`. Verification
  metadata is pinned until closeout stamps the 2b code commit.
