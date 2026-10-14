# mcp/src/agents_remember/observer/lifecycle_state.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`lifecycle_state.py` is the pure state vocabulary of the observable lifecycle:
the `State` and `Phase` literal types, the `LifecycleState` record, the typed
errors a signal raises, and the `coerce_phase` boundary validator. It has no I/O,
so the later projection reducer can import the types without pulling in the
ambient singleton's threading.

Since 260731-EFA-L4 the state vocabulary is **composed, not carved**: the module
declares a live half and a terminal half and builds `State` from them, so "which
states exist" and "which states are terminal" can no longer be two lists that
disagree.

## Code Commentary

### The state partition (260731-EFA-L4)

`State` is no longer a flat six-member literal with `TERMINAL_STATES` standing
beside it naming two of its members again. The two halves are where the names
live (cit:(["LiveState = Literal[", "EndOutcome = Literal[", "TerminalState = EndOutcome", "State = Literal[LiveState"], mcp/src/agents_remember/models/lifecycles/responses.py:16-16; mcp/src/agents_remember/models/lifecycles/responses.py:17-17; mcp/src/agents_remember/models/lifecycles/responses.py:18-18; mcp/src/agents_remember/models/lifecycles/responses.py:19-19)):

```python
LiveState = Literal["running", "paused", "blocked", "awaiting-developer"]   # L109
EndOutcome = Literal["completed", "abandoned"]                              # L117
TerminalState = EndOutcome                                                  # L118
State = Literal[LiveState, TerminalState]                                   # L120
```

`State` is composed from the live and terminal aliases, while `TERMINAL_STATES`
is derived from the terminal half rather than maintained as a second hand-written
list (cit:(["State = Literal[LiveState", "TerminalState = EndOutcome"], mcp/src/agents_remember/models/lifecycles/responses.py:19-19; mcp/src/agents_remember/models/lifecycles/responses.py:18-18); cit:(["TERMINAL_STATES: frozenset[str] = frozenset(vocabulary_names(TerminalState, label=\"TerminalState\"))"], mcp/src/agents_remember/observer/lifecycle_state.py:108-108)).

The derived constants (cit:([`STATES`, `LIVE_STATES`, `TERMINAL_STATES`, `DEFAULT_END_OUTCOME`, `INITIAL_PHASE`, `PHASES`], mcp/src/agents_remember/observer/lifecycle_state.py:102-108; mcp/src/agents_remember/observer/lifecycle_state.py:112-112; mcp/src/agents_remember/observer/lifecycle_state.py:114-115)) are all read back out of those declarations
rather than retyped:

- `STATES: tuple[State, ...]` — the whole vocabulary, produced by
  cit:([`STATES`, `check_state_partition`], mcp/src/agents_remember/observer/lifecycle_state.py:74-99; mcp/src/agents_remember/observer/lifecycle_state.py:102-104),
  which **runs at import**.
- cit:([`LIVE_STATES`, `TERMINAL_STATES`], mcp/src/agents_remember/observer/lifecycle_state.py:105-108) — each half is derived from its vocabulary, and
  cit:([`vocabulary_names`], mcp/src/agents_remember/observer/lifecycle_state.py:41-56) supplies the names rather than a second hand-written list.
- cit:([`PHASES`], mcp/src/agents_remember/observer/lifecycle_state.py:115-115) is now `vocabulary_names(Phase, label="Phase")`, not
  `get_args(Phase)`. cit:([`INITIAL_PHASE`], mcp/src/agents_remember/observer/lifecycle_state.py:114-114) is unchanged.
- cit:([`DEFAULT_END_OUTCOME`], mcp/src/agents_remember/observer/lifecycle_state.py:112-112) — deliberately *not*
  a classification but a **reducer policy**: an unknown or absent recorded `lifecycle.ended`
  outcome coerces to abandonment. The removed public lifecycle_end tool is not a current writer.

cit:([`vocabulary_names`, `_collect_names`], mcp/src/agents_remember/observer/lifecycle_state.py:41-56; mcp/src/agents_remember/observer/lifecycle_state.py:59-70) returns the strings a `Literal` declares, in declaration order. It
reads through every legal form: a flat `Literal[...]`, a composition of aliases
(flattened by PEP 586), and the union form `Literal[...] | Other` (which is *not*
flattened — `get_origin` is checked against `Literal`, `Union` **and**
`UnionType`). Anything that is not a string is refused by name. This is the
replacement for a bare `get_args`, which on the union form hands back `Literal`
*objects*: a set of those matches no event payload, and the first consumer to
call a string method on one dies with `AttributeError` at import of the whole
`agents_remember.observer` package.

cit:([`check_state_partition`], mcp/src/agents_remember/observer/lifecycle_state.py:73-98) verifies that `whole`
is exactly its two halves and returns its names. It raises
`LifecycleVocabularyError` for a state filed on **both** halves, a state declared
on `State` but filed on **neither** ("unfiled"), and a state filed but **absent**
from `State` ("orphans"). Because `State` is composed from the halves, the only
way to smuggle in an unfiled state is to append a bare literal to the
composition — and that is what the unfiled branch catches, at import, naming it.

cit:([`LifecycleVocabularyError`], mcp/src/agents_remember/observer/lifecycle_state.py:30-38) is the new typed error
for a malformed vocabulary *declaration*, distinct from `LifecycleError` (a
signal issued against an incompatible *state*).

cit:([`coerce_end_outcome`], mcp/src/agents_remember/observer/lifecycle_state.py:118-127) is the one owner of the
outcome → terminal-state rule. Because the terminal half **is** the
`lifecycle_end` outcome vocabulary, this is a membership test, not a mapping
table: a recognized outcome returns itself, and an unrecognized or missing one
returns `DEFAULT_END_OUTCOME` — never a completion. Its leniency is for the
**reducer**, which reads logs it did not write; the write side
(`ambient.AmbientLifecycle.end`) still refuses an unknown outcome outright rather
than defaulting it.

### Current module boundaries

`LiveState`, `TerminalState`, `State` and `Phase` are imported from the retained lifecycle response vocabulary. `check_state_partition` validates the complete live/terminal partition and supplies `STATES`; malformed vocabulary members fail by name rather than flowing into the reducer. `coerce_end_outcome` maps an unknown or absent outcome to abandonment, while `coerce_phase` raises `LifecycleError` for an unknown phase.

`LifecycleState` is frozen and holds `id`, `state`, `phase`, `fleeting`, `started_at`, `enclosure` and `repo_id`; `is_terminal` reads the declared terminal half. There is no `scope` field, `GuardedStartError`, session-signal transition or auto-resume-on-next-tool implementation here. The record/vocabulary remains usable by the retained worktree attribution and reducer; it does not restore the removed session lifecycle.

## Invariants And Boundaries

- Pure data + types: no I/O, no threading, no import from the ambient module —
  this is what lets the projection slice reuse the vocabulary cheaply.
- **The partition is checked at import, not at use.** `STATES` is assigned from
  `check_state_partition(...)`, so a state filed on neither half, on both, or
  filed-but-absent fails the import of `agents_remember.observer` by name. There
  is no runtime path on which a malformed vocabulary travels.
- **Terminality is structural, not a second opinion.** The terminal half *is* the
  `lifecycle_end` outcome vocabulary, so filing a state on it commits to the
  reducer reaching it through `lifecycle.ended` and to nothing else declaring it.
  `TERMINAL_STATES` is derived from that half; it is not a set standing beside
  `State`.
- **Filing decides two downstream things.** A state on the live half gets a
  `Metrics` bucket (`projection.ACTIVE_STATES` is `LIVE_STATES` verbatim); a
  state on the terminal half ends the lifecycle. That is why an unfiled state is
  refused rather than defaulted.
- `paused` has no signal; it is observed/inferred by the system, never declared.
- `awaiting-developer` remains in the declared live vocabulary, so `is_terminal` is false; no current model-signal writer or next-tool auto-resume mechanism is implemented.
- **Two different leniencies, deliberately.** `coerce_end_outcome` defaults an
  unknown outcome to `abandoned` because the reducer reads foreign logs;
  `ambient.end` raises `LifecycleError` on the same input because a session
  ending itself must not have a typo silently recorded as an abandonment.
- Frozen `LifecycleState`: transitions produce new values via `replace`.
- Boundary validation (`coerce_phase`) lives here. The removed blocked/awaiting signal methods are not current callers; retained recorded-event reduction consumes its actual typed phase/state inputs.

## Evidence

### Repo-Internal References

- The singleton that drives these states and raises these errors; its `end` signal now reads `TERMINAL_STATES` and converts through `coerce_end_outcome` instead of keeping its own accept-tuple and outcome→state conditional. [1]
- The typed-error family base (`AgentsRememberError`). [2]
- The response model reuses `State`/`Phase` so the wire contract matches. [3]
- `ACTIVE_STATES` is `LIVE_STATES` verbatim, and `STATE_COUNT_FIELDS` derives one `Metrics` bucket per live state — this is what makes the live/terminal filing load-bearing. [4]
- The reducer's `_STATES` is built from `STATES`, and `_ended_updates` routes through `coerce_end_outcome`. [5]
The design note is historical context only; current lifecycle behavior is owned by this module and its focused tests.
