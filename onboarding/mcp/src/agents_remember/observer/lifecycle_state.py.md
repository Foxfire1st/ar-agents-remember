# mcp/src/agents_remember/observer/lifecycle_state.py

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `mcp/src/agents_remember/observer/lifecycle_state.py` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-08-01T10:40+02:00                               |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007`           |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
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
  a classification but a **policy**: `lifecycle_end` takes a free-form outcome
  string at the tool boundary, and anything that is not the affirmative
  completion is an abandonment.

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

cit:(["Phase = Literal["], mcp/src/agents_remember/models/lifecycles/responses.py:20-27) — the session-lifecycle skill's heading vocabulary,
orthogonal to state. cit:(["system-owned"], mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:159-159) binds the paused and
awaiting-developer classification: `paused` is system-owned (no model signal),
while `awaiting-developer` is the turn-end notification state on the live half.
cit:([`await_developer`, `resume_from_await`], mcp/src/agents_remember/observer/ambient.py:205-221; mcp/src/agents_remember/observer/ambient.py:223-241)
shows the ambient signal methods that enter and leave that state, and
cit:([`resume_from_await`], mcp/src/agents_remember/application/tool_response.py:42-42)
shows the next-tool auto-resume choke point for that notification path.

cit:([`LifecycleError`], mcp/src/agents_remember/observer/lifecycle_state.py:130-131) is this domain's family base;
cit:([`GuardedStartError`], mcp/src/agents_remember/observer/lifecycle_state.py:134-146) names the active lifecycle in its message.
cit:([`LifecycleState`], mcp/src/agents_remember/observer/lifecycle_state.py:156-179) is a frozen dataclass (`id`, `state`, `phase`,
`fleeting`, `started_at`, plus the slice-2c persistence-binding fields
`enclosure`, `repo_id`, and `scope` — all `None` until the lifecycle is promoted)
with an cit:([`is_terminal`], mcp/src/agents_remember/observer/lifecycle_state.py:177-179) that reads `TERMINAL_STATES` — frozen
so each transition is a new value (no shared-mutable surprises across the request
and heartbeat threads). cit:([`coerce_phase`], mcp/src/agents_remember/observer/lifecycle_state.py:149-153) validates a raw
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The singleton that drives these states and raises these errors; its `end` signal now reads `TERMINAL_STATES` and converts through `coerce_end_outcome` instead of keeping its own accept-tuple and outcome→state conditional. | `end` | mcp/src/agents_remember/observer/ambient.py:243-274 |
| The typed-error family base (`AgentsRememberError`). | `AgentsRememberError` | mcp/src/agents_remember/errors.py:13-14 |
| The response model reuses `State`/`Phase` so the wire contract matches. | `LifecycleResponse` | mcp/src/agents_remember/models/lifecycles/responses.py:30-35 |
| `ACTIVE_STATES` is `LIVE_STATES` verbatim, and `STATE_COUNT_FIELDS` derives one `Metrics` bucket per live state — this is what makes the live/terminal filing load-bearing. | `ACTIVE_STATES`; `STATE_COUNT_FIELDS` | mcp/src/agents_remember/observer/projection.py:241-241; mcp/src/agents_remember/observer/projection.py:287-287 |
| The reducer's `_STATES` is built from `STATES`, and `_ended_updates` routes through `coerce_end_outcome`. | `_STATES`; `_ended_updates` | mcp/src/agents_remember/observer/reducer.py:117-117; mcp/src/agents_remember/observer/reducer.py:382-384 |
| The partition, the vocabulary reader, and structural terminality are pinned by test. | `StatePartitionTests`; `TerminalityIsStructuralTests`; `StateVocabularyReaderTests` | mcp/tests/test_observer_projection_metrics.py:236-300; mcp/tests/test_observer_projection_metrics.py:303-420; mcp/tests/test_observer_projection_metrics.py:423-458 |
| The write side is pinned to hold no copy of the terminal vocabulary. | `EndSignalVocabularyTests` | mcp/tests/test_observer_ambient.py:157-185 |
| The design note is historical context only; current lifecycle behavior is owned by this module and its focused tests. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: split phase/state classification from ambient entry/exit and next-tool resume behavior, regenerated the operative extents, and narrowed unsupported pooled wording.

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the two
  `projection.py` pointers after a worker inserted ten lines above them. `ACTIVE_STATES` L217 →
  L227 (`ACTIVE_STATES: tuple[LiveState, ...] = LIVE_STATES`), `STATE_COUNT_FIELDS` L263 → L273
  (`STATE_COUNT_FIELDS: dict[str, str] = state_count_fields(ACTIVE_STATES)`). No body text changed.
- 2026-08-01T00:20+02:00 — 260731-EFA-L4 curator: the body described a flat six-member `State`
  literal with `TERMINAL_STATES` as a separate derived constant and `PHASES = get_args(Phase)`.
  Verified against the current source and rewrote it: `State` is now composed
  (`State = Literal[LiveState, TerminalState]`, cit:(["State = Literal[LiveState"], mcp/src/agents_remember/models/lifecycles/responses.py:19-19)) from cit:(["LiveState = Literal["], mcp/src/agents_remember/models/lifecycles/responses.py:16-16) and
`EndOutcome`/cit:(["def coerce_end_outcome(value: object) -> TerminalState:"], mcp/src/agents_remember/observer/lifecycle_state.py:118-118) is assigned from
  `check_state_partition` so the partition is enforced at **import**; cit:([`LIVE_STATES`], mcp/src/agents_remember/observer/lifecycle_state.py:105-107),
  cit:([`TERMINAL_STATES`], mcp/src/agents_remember/observer/lifecycle_state.py:108-108) and cit:([`PHASES`], mcp/src/agents_remember/observer/lifecycle_state.py:115-115) are all read back through the new
  cit:([`vocabulary_names`], mcp/src/agents_remember/observer/lifecycle_state.py:41-56) rather than declared or `get_args`-ed. Documented the three new
  public symbols the card never mentioned — cit:([`LifecycleVocabularyError`], mcp/src/agents_remember/observer/lifecycle_state.py:30-38),
  `vocabulary_names`/`_collect_names` (L41-L70, which handles the union form `get_args` would
  have returned `Literal` objects for), cit:([`check_state_partition`], mcp/src/agents_remember/observer/lifecycle_state.py:73-98) — plus
  cit:([`DEFAULT_END_OUTCOME`], mcp/src/agents_remember/observer/lifecycle_state.py:112-112) and cit:([`coerce_end_outcome`], mcp/src/agents_remember/observer/lifecycle_state.py:118-127). Reframed the
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
