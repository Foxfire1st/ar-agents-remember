# mcp/src/agents_remember/observer/lifecycle_state.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `mcp/src/agents_remember/observer/lifecycle_state.py` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-08-01T10:40+02:00                               |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`           |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                        |

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
live (L109-L120):

```python
LiveState = Literal["running", "paused", "blocked", "awaiting-developer"]   # L109
EndOutcome = Literal["completed", "abandoned"]                              # L117
TerminalState = EndOutcome                                                  # L118
State = Literal[LiveState, TerminalState]                                   # L120
```

PEP 586 flattens a `Literal` of `Literal` aliases, so `State` is the *identical*
runtime object and the identical type it was before — nothing downstream had to
change. What is gone is the second hand-written list.

The derived constants (L133-L146) are all read back out of those declarations
rather than retyped:

- `STATES: tuple[State, ...]` (L133-L135) — the whole vocabulary, produced by
  `check_state_partition(live=LiveState, terminal=TerminalState, whole=State)`,
  which **runs at import**.
- `LIVE_STATES: tuple[LiveState, ...]` (L136-L138) and
  `TERMINAL_STATES: frozenset[str]` (L139) — each half, via `vocabulary_names`.
  `TERMINAL_STATES` is unchanged in value and in type; it is simply now *derived*
  from the half instead of being a literal set.
- `PHASES` (L146) is now `vocabulary_names(Phase, label="Phase")`, not
  `get_args(Phase)`. `INITIAL_PHASE = "request"` (L145) is unchanged.
- `DEFAULT_END_OUTCOME: TerminalState = "abandoned"` (L143) — deliberately *not*
  a classification but a **policy**: `lifecycle_end` takes a free-form outcome
  string at the tool boundary, and anything that is not the affirmative
  completion is an abandonment.

`vocabulary_names(spec, *, label)` (L41-L56, recursing through `_collect_names`
at L59-L70) returns the strings a `Literal` declares, in declaration order. It
reads through every legal form: a flat `Literal[...]`, a composition of aliases
(flattened by PEP 586), and the union form `Literal[...] | Other` (which is *not*
flattened — `get_origin` is checked against `Literal`, `Union` **and**
`UnionType`). Anything that is not a string is refused by name. This is the
replacement for a bare `get_args`, which on the union form hands back `Literal`
*objects*: a set of those matches no event payload, and the first consumer to
call a string method on one dies with `AttributeError` at import of the whole
`agents_remember.observer` package.

`check_state_partition(*, live, terminal, whole)` (L73-L98) verifies that `whole`
is exactly its two halves and returns its names. It raises
`LifecycleVocabularyError` for a state filed on **both** halves, a state declared
on `State` but filed on **neither** ("unfiled"), and a state filed but **absent**
from `State` ("orphans"). Because `State` is composed from the halves, the only
way to smuggle in an unfiled state is to append a bare literal to the
composition — and that is what the unfiled branch catches, at import, naming it.

`LifecycleVocabularyError(AgentsRememberError)` (L30-L38) is the new typed error
for a malformed vocabulary *declaration*, distinct from `LifecycleError` (a
signal issued against an incompatible *state*).

`coerce_end_outcome(value) -> TerminalState` (L149-L158) is the one owner of the
outcome → terminal-state rule. Because the terminal half **is** the
`lifecycle_end` outcome vocabulary, this is a membership test, not a mapping
table: a recognized outcome returns itself, and an unrecognized or missing one
returns `DEFAULT_END_OUTCOME` — never a completion. Its leniency is for the
**reducer**, which reads logs it did not write; the write side
(`ambient.AmbientLifecycle.end`) still refuses an unknown outcome outright rather
than defaulting it.

### The rest of the module (unchanged)

`Phase = Literal["request","trust-checkpoint","reframe-research","decide","build",
"close"]` (L124-L131) — the session-lifecycle skill's heading vocabulary,
orthogonal to state. `paused` is system-owned (no model signal).
`awaiting-developer` is the task-28 NOTIFY-AND-CONTINUE turn-end state: the model
declares the turn complete and stops — filed on the **live** half, auto-resumed
by the next AR tool call (no gate, no wait), so it is a notification, not a
barrier.

`LifecycleError(AgentsRememberError)` (L161) is this domain's family base;
`GuardedStartError` (L165-L177) names the active lifecycle in its message.
`LifecycleState` (L187-L210) is a frozen dataclass (`id`, `state`, `phase`,
`fleeting`, `started_at`, plus the slice-2c persistence-binding fields
`enclosure`, `repo_id`, and `scope` — all `None` until the lifecycle is promoted)
with an `is_terminal` property (L208-L210) that reads `TERMINAL_STATES` — frozen
so each transition is a new value (no shared-mutable surprises across the request
and heartbeat threads). `coerce_phase(value)` (L180-L184) validates a raw
tool-boundary string into a `Phase` or raises `LifecycleError`.

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
- `awaiting-developer` *is* model-declared (unlike `paused`) but is filed on the
  **live** half, so `is_terminal` stays `False` for it and the next AR tool call
  can auto-resume it back to `running`.
- **Two different leniencies, deliberately.** `coerce_end_outcome` defaults an
  unknown outcome to `abandoned` because the reducer reads foreign logs;
  `ambient.end` raises `LifecycleError` on the same input because a session
  ending itself must not have a typo silently recorded as an abandonment.
- Frozen `LifecycleState`: transitions produce new values via `replace`.
- Boundary validation (`coerce_phase`) lives here; the ambient signal methods
  trust their already-typed `Phase`/`State` inputs.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The singleton that drives these states and raises these errors; its `end` signal now reads `TERMINAL_STATES` and converts through `coerce_end_outcome` instead of keeping its own accept-tuple and outcome→state conditional. | `AmbientLifecycle.end` | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The typed-error family base (`AgentsRememberError`). | — | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| The response models reuse `State`/`Phase` so the wire contract matches. | — | [models/lifecycle.py](agents-remember/mcp/src/agents_remember/models/lifecycle.py) |
| `ACTIVE_STATES` is `LIVE_STATES` verbatim, and `STATE_COUNT_FIELDS` derives one `Metrics` bucket per live state — this is what makes the live/terminal filing load-bearing. | `ACTIVE_STATES` L227; `STATE_COUNT_FIELDS` L273 | [projection.py](projection.py) |
| The reducer's `_STATES` is built from `STATES`, and `_ended_updates` routes through `coerce_end_outcome`. | `_STATES` L75; `_ended_updates` L405-L407 | [reducer.py](reducer.py) |
| The partition, the vocabulary reader, and structural terminality are pinned by test. | `StatePartitionTests` L1725-L1789; `TerminalityIsStructuralTests` L1792-L1909; `StateVocabularyReaderTests` L1912-L1947 | [test_observer_projection.py](../../../tests/test_observer_projection.py) |
| The write side is pinned to hold no copy of the terminal vocabulary. | `EndSignalVocabularyTests` L157-L185 | [test_observer_ambient.py](../../../tests/test_observer_ambient.py) |
| The design's state machine, signals, and phase axis (§1.2-1.4). | — | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Update History

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the two
  `projection.py` pointers after a worker inserted ten lines above them. `ACTIVE_STATES` L217 →
  L227 (`ACTIVE_STATES: tuple[LiveState, ...] = LIVE_STATES`), `STATE_COUNT_FIELDS` L263 → L273
  (`STATE_COUNT_FIELDS: dict[str, str] = state_count_fields(ACTIVE_STATES)`). No body text changed.
- 2026-08-01T00:20+02:00 — 260731-EFA-L4 curator: the body described a flat six-member `State`
  literal with `TERMINAL_STATES` as a separate derived constant and `PHASES = get_args(Phase)`.
  Verified against the current source and rewrote it: `State` is now composed
  (`State = Literal[LiveState, TerminalState]`, L120) from `LiveState` (L109) and
  `EndOutcome`/`TerminalState` (L117-L118); `STATES` (L133-L135) is assigned from
  `check_state_partition` so the partition is enforced at **import**; `LIVE_STATES` (L136-L138),
  `TERMINAL_STATES` (L139) and `PHASES` (L146) are all read back through the new
  `vocabulary_names` (L41-L56) rather than declared or `get_args`-ed. Documented the three new
  public symbols the card never mentioned — `LifecycleVocabularyError` (L30-L38),
  `vocabulary_names`/`_collect_names` (L41-L70, which handles the union form `get_args` would
  have returned `Literal` objects for), `check_state_partition` (L73-L98) — plus
  `DEFAULT_END_OUTCOME` (L143) and `coerce_end_outcome` (L149-L158). Reframed the
  `awaiting-developer` claim: it was "deliberately not added to `TERMINAL_STATES`", which is now
  a consequence rather than a decision — it is *filed on the live half*, and that filing is what
  earns it a `Metrics` bucket. Added invariants for import-time checking, structural terminality,
  and the deliberate split between `coerce_end_outcome`'s leniency (reducer, foreign logs) and
  `ambient.end`'s refusal (write side). Added five reference rows with verified citations.
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
