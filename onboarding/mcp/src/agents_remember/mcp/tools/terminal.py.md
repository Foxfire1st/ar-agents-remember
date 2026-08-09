# mcp/src/agents_remember/mcp/tools/terminal.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/mcp/tools/terminal.py`   |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `7463b97a560e39367b9e31a687f09ea3f4f6b9f6`|
| lastVerifiedCommitDate | 2026-08-09T04:22:51+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[mcp/tools overview](overview.md)

## Purpose

`terminal.py` contains MCP payload builders for dashboard terminal-session catalog operations. It
exposes the agent-facing path for moving an already-created hosted terminal/chat session to a durable
task leaf (`attach_terminal_session_to_leaf`), and — since L2 — `spawn_agent_session`, which
**creates** a role-configured, leaf-attached hosted session through the shared opener. The spawn
returns `spawned-unbriefed`; readiness and durable dispatch-brief delivery are explicit later phases,
not side effects of this call.

## Code Commentary

### 260731-EFA-L4 Session Statuses Typed At The Seam

The three session-status vocabularies this file writes are now typed where they
are *produced*, not only where they are validated. Every payload builder here
returns an untyped `dict[str, Any]` all the way to the MCP handler, so a status
the response model does not know becomes a pydantic `ValidationError` on a path
with no `except` for one. Annotating the producers moves that to a type error.

The aliases are imported from `models/terminal.py`
cit:([`SpawnAgentSessionStatus`, `SessionRetireStatus`, `SessionRenameStatus`], mcp/src/agents_remember/models/terminal.py:45-71; mcp/src/agents_remember/models/terminal.py:149-155; mcp/src/agents_remember/models/terminal.py:181-181)
rather than declared locally, deliberately — declaring them here would create the cycle, since
`models/terminal.py` is what `_tool_payload` validates against.

- `SpawnAgentSessionStatus` — `_spawn_refusal(status, harness, kind, *, detail)`
  cit:([`_spawn_refusal`], mcp/src/agents_remember/application/terminal_tools.py:880-905) takes it, and
  `_knob_refusal`'s check table is annotated
  `checks: tuple[tuple[SpawnAgentSessionStatus, str | None], ...]`
  cit:([`_knob_refusal`], mcp/src/agents_remember/application/terminal_tools.py:423-441), so
  every model/effort refusal in this module is checked at the producer.
- `SessionRetireStatus` — the new `_retire_payload(status, session_id, *, detail, closure)`
  cit:([`_retire_payload`], mcp/src/agents_remember/application/terminal_tools.py:914-941) is the single
  builder for all five `session_retire` results. A success reports the row's retirement provenance
  (`retiredAt`/`retiredBySession`/`retiredReason`/`retiredEdge`, from a
  `TerminalCatalogEntry`); a refusal reports the policy clause that fired
  (`detail`). Nothing carries both, which is why they are separate keyword
  arguments rather than one bundle. The module constant
  `_RETIRE_OK_STATUSES: frozenset[SessionRetireStatus] = frozenset({"retired",
  "already-retired"})`
  cit:([`_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:911-911)
  encodes `SessionRetireResponse.ok`'s own documented
  rule in one place — the two idempotent successes are true and every refusal is
  false — so a refusal status added later cannot arrive as `ok=True` from a fifth
  call site that forgot the rule. cit:([`session_retire_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:66-83) shrank to
  five `_retire_payload(...)` calls.
- `SessionRenameStatus` — `_rename_payload(status, session_id, *, label, renamed)`
  cit:([`_rename_payload`], mcp/src/agents_remember/application/terminal_tools.py:1004-1025)
  is the peer for `session_rename`. It reports the **requested** label
  on a refusal and the **stored** pair on success; `spawnedLabel` is added only
  when a row was actually renamed, because it is the frozen spawn-time label and
  there is no row to have frozen one when the session is unknown. `ok` is
  `status == "renamed"`.

**Two of the thirteen spawn statuses are produced outside this file.**
cit:([`SpawnAgentSessionStatus`], mcp/src/agents_remember/models/terminal.py:45-71) folds in
`LeafRefStatus`, which is declared in `worktrees/leaf_refs.py` — the only producer
is `LeafRefResolutionError.status`, and `leaf_ref_refusal_payload` copies it
verbatim into whichever tool refused. So `leaf-ref-not-found` and
`leaf-ref-ambiguous` are spawn statuses produced entirely outside the module
anyone enumerating spawn refusals would read.

That is also the one gap deliberately **not** closed here: the published
`spawn_agent_session` MCP tool docstring (in `mcp/registration/sessions.py`)
rosters ten statuses in its closing sentence plus `leaf-taken` named inline —
eleven of thirteen. The docstring IS the published tool description clients read,
so it is pinned by a test rather than edited:
`test_every_status_the_session_tools_roster_validates` asserts
`vocabulary - advertised == {"leaf-ref-not-found", "leaf-ref-ambiguous"}`, so the
gap cannot silently widen. `session_retire` and `session_rename` are asserted
*equal* to their model vocabularies in the same test.

### 260731-EFA-L2 Spawn Parameter Objects

`spawn_agent_session_payload`'s sixteen keyword arguments became four bundles, each with a named
default so an ordinary call reads as one:

```python
spawn_agent_session_payload(config, *, seat: SpawnSeat = DEFAULT_SPAWN_SEAT,
                            retired: RetiredSpawnInputs = NO_RETIRED_INPUTS,
                            spawned_by: SpawnedBy = UNATTRIBUTED_SPAWN,
                            overrides: SpawnOverrides = NO_SPAWN_OVERRIDES)
```

- **`SpawnSeat`** — what the caller legitimately declares: `kind`, `leaf_key`,
  `replacement_for_leaf`, `level`, `label`, `env` (the seat's `AR_SPAWN_ROLE` rides here).
- **`RetiredSpawnInputs`** — what it may no longer declare: `context`/`submit` (the retired one-call
  brief) plus `harness`, `model`, `effort`, `launch_args`, `prompt_keywords`, `session_commands`.
  These are accepted **only so they can be refused loudly** before any settings, catalog, or
  terminal side effect; a non-`None` value is a refusal, never a setting, which is why they travel
  as the one bundle `_caller_spend_override_refusal(seat, retired)` walks.
- **`SpawnedBy`** — the spawner's own `session_id` / `lifecycle_id`, recorded on the new row.
- **`SpawnOverrides`** — real collaborators a test may substitute: `session_id`, `host`, `paster`,
  `session_log`, `which`. Its docstring is explicit that this is **not** a hexagonal port bundle —
  the type was called `SpawnPorts` and the name implied a boundary the spawn talks to the domain
  through, which it is not. `paster` and `session_log` are kept precisely because the spawn path
  never reads them: a spawn delivers no brief and writes no session log, and a test hands in a fake
  to assert it was never called. Production always passes `NO_SPAWN_OVERRIDES`.

`_resolve_spawn_harness` was split into `_requested_harness` (the caller named one: known id AND
installed), `_preferred_harness` (settings named one: a configured-but-missing harness names its
source file) and `_first_detected_harness` (nothing asked or configured: first registry harness on
PATH). Same precedence, same refusals.

The published MCP tool keeps its flat sixteen-parameter signature — the packing happens in
`mcp/registration/sessions.py`, because a model-typed tool parameter would republish
`spawn_agent_session` as a nested object for every client.

### 260714-ACPUI-L2 Typed Native Launch Dispatch

Role-based native dispatch now resolves settings into one complete `ResolvedLaunch` and passes it
through `open_terminal_session` to the hosted runner. Missing model or effort refuses before tmux
as `launch-selection-invalid`; complete selections are validated later against the native
adapter's dynamic model-gated catalog before the configured vendor process starts. The
`AR_SPAWN_MODEL` and `AR_SPAWN_EFFORT` environment values remain provenance, not a second launch
authority, and normalized model/effort never becomes a synthesized session command.

The split is intentional. Built-in protocol harnesses (`claude`, `codex`, `pi`) use the typed
native path. Settings-defined non-native harnesses keep their explicit static flag/session mapping,
including `effort_session_commands`, because no normalized native adapter exists for them.
Roleless opens are owned by the serving request boundary. This tool remains the settings-owned role
path. If a repeated spawn targets an already-live session id whose process launch differs from the
newly resolved role selection, the shared opener returns `launch-conflict`; this builder maps it to
the existing `launch-selection-invalid` refusal. It does not retry, reconfigure, or enter another
spawn path, so the actual catalog/process pair remains authoritative.

### 260707-HFX2-L18 Strict-CRAP Decomposition

`spawn_agent_session_payload` keeps its application entry point contract while moving optional leaf-reference
normalization into `_resolve_spawn_leaf`. The helper accepts either the claimed leaf or declared
replacement leaf and returns the same `leaf-ref-not-found` / `leaf-ref-ambiguous` payload built from
the original unresolved ref. The application entry point still rejects caller spend overrides first,
performs harness dispatch only for `kind == "harness"`, opens through the shared opener, and projects
a `spawned-unbriefed` response. It writes no brief expectation, binds no session log, and delivers no
session command or task brief.

The non-harness path now initializes its resolved dispatch locals explicitly before the harness-only
branch. This is a behavior-preserving flattening: plain terminals still launch the configured shell
without harness metadata, while harness spawns retain settings-owned model/effort/free-form controls,
L17 `(leafKey, seatRole)` arbitration, and the same refusal/success payload fields. Independent review
confirmed the target CRAP score fell from `34.25` (CC `34`, coverage `94%`) to `23.02` (CC `23`,
coverage `96.4%`) without threshold/configuration changes or a displaced helper hotspot.

### 260707-HFX2-L17 MCP Pair-Binding Surface

Attach accepts an optional role, delegates live arbitration through `LeafAssignmentHost`, and
returns `seatRole` plus `previousSeatRole`. Spawn responses expose the derived seat role and write
routing provenance with that role; later durable dispatch-brief delivery owns any acknowledgement
expectation. Retire authority consumes current binding identity
rather than spawn provenance, so an explicitly typed hand-opened seat and an unbound failed
dispatch resolve through the same pair model.

### Logic

**Spawn/readiness/brief separation.** `spawn_agent_session` rejects retired one-call
`context`/`submit` inputs, creates the hosted seat, and returns `spawned-unbriefed`
(cit:([`spawn_agent_session_tool`, `"spawned-unbriefed"`], mcp/src/agents_remember/application/terminal_tools.py:769-842)).
The caller must then prove the exact session ready and send one durable `dispatch-brief` inbox entry;
the explicit refusal guidance records that sequence and never asks for a respawn
(cit:([`_brief_delivery_separate_refusal`, `"brief delivery is separate"`], mcp/src/agents_remember/application/terminal_tools.py:567-581)).

`attach_terminal_session_to_leaf_payload(config, session_id, leaf_key)` first normalizes the requested
leaf ref through `serving.leaf_ref_validation.resolve_catalog_leaf_key`. Accepted qualified refs, doc ids,
and unambiguous legacy stems/slugs persist as the canonical `repo/master/doc-id` catalog key; no-match or
ambiguous refs return a strict `leaf-ref-not-found` / `leaf-ref-ambiguous` refusal before opening or
mutating the catalog. On success it opens the dashboard terminal catalog at
`terminal_catalog_path(config.coordination_root)`, calls the serving-layer
`assign_terminal_session_to_leaf` helper, and returns the result through `_tool_payload` under the
`attach_terminal_session_to_leaf` operation. The payload reports `ok` only for `attached`, and always
includes the persisted canonical session/leaf plus optional `previousLeafKey`, `ownerSession`, and role.

`spawn_agent_session_payload` is now a thin MCP adapter over
`application.terminal_tools.spawn_agent_session_tool`. The application command accepts four bundles:
`SpawnSeat`, `RetiredSpawnInputs`, `SpawnedBy`, and `SpawnOverrides`. It refuses legacy one-call
`context`/`submit` and caller spend overrides before settings, catalog, or terminal side effects;
normalizes an optional leaf/replacement ref; resolves the settings-owned harness launch; and calls
the same `open_terminal_session` transaction as the dashboard route. `bad-kind`, `leaf-taken`,
unknown/undetected harness, invalid level/launch selection, and leaf-ref failures remain strict
`ok:false` response statuses rather than exceptions.

On success, the command returns `spawned-unbriefed` with catalog and launch provenance. It does not
paste task context, submit a prompt, write spawn expectation rows, bind a harness session log, or
report delivery booleans/captures. Settings-owned session commands are launch-phase configuration for
the opener/runner, never a task brief. The retained `paster` and `session_log` override fields are
negative-test seams: the application path deliberately never touches them.

The next phases are separate and explicit: prove the exact hosted session ready, then post one durable
`dispatch-brief` operator-inbox entry to that session. Delivery acceptance and acknowledgement belong
to the readiness/inbox surfaces, so absent proof leaves the seat pending without respawning it.

**Seat lifecycle (260707-HFX-L8, issues #12/#4)** adds two more agent-facing payload builders,
sharing this file's transport-thin posture — both delegate the actual mechanics to `serving/`.
`session_retire_payload(config, *, actor_session_id, session_id, reason="manual retire", host=None)`
cit:([`session_retire_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:66-83):
looks up target + actor rows via `TerminalCatalog.get` (`unknown-session`/`unknown-actor` `ok:
false` when either id has no catalog row); if the target is already `terminated` it short-circuits
to `already-retired` (`ok: true`, existing provenance echoed, never re-stamped — idempotent); else
it builds `SeatRef`s from each row's `spawn_role`/`leaf_key` (`master_of(leaf_key)` derives the
master identity) and calls `check_retire_authority` — a `RetirePolicyError` returns `ok: false`,
`status: "retire-refused"`, `detail` naming the exact clause (owner-never-self-retires /
manager-scoped-to-own-master / no-retire-authority); on success it calls `retire.retire_entry`
(kills the tmux session via `TerminalHost.terminate`, best-effort/idempotent against an
already-gone session, then `catalog.mark_retired`) and `seat_events.log_retire_event`, returning
`status: "retired"` plus the full retirement provenance. `session_rename_payload(config, *,
session_id, label)`
cit:([`session_rename_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:86-95):
`unknown-session` when the row is missing OR already terminated (a retired
seat cannot be renamed), else `catalog.set_label` + `log_rename_event`, returning the new `label`
and `spawnedLabel` (the frozen original, set on the first rename only). Both return through the
same `_tool_payload` envelope every other builder in this file uses.

Since 260731-EFA-L4 neither function writes its own payload dict: each result goes
through `_retire_payload` / `_rename_payload` (see the typed-seam section above),
so `ok` is computed from one rule per tool instead of being restated at each of
the five (retire) and two (rename) call sites. Every status, field and `ok` value
is unchanged.

Design note carried from the builder/reviewer record: `actor_session_id` is SELF-DECLARED by the
caller, mirroring `spawn_agent_session`'s `spawned_by_session` provenance pattern — there is no
ambient "who is calling me" session-id resolution anywhere in this codebase (`AR_SPAWN_ROLE` is
only ever read from an explicit `env` dict passed to a *child* at spawn, never the caller's own
env). This means `session_retire` trusts the caller's self-declaration for AUTHORITY, not merely
provenance; both the builder and the adversarial reviewer flagged and accepted this as a residual
risk for this leaf (recoverable action — transcripts preserved, seat re-spawnable; logged; existing
precedent in `spawn_agent_session`), worth a stronger identity-binding pass if/when an ambient
session-identity primitive is built.

### Conventions

Builders stay transport-thin: spawn orchestration lives in `application.terminal_tools` and
`serving.terminal_opener`, leaf reassignment in `serving.terminal_leaf_assignment`, response validation
is `_tool_payload` + `models/terminal.py`, and the `@server.tool()` declarations live in
`mcp/registration/sessions.py` (260731-EFA-L2 moved them out of `mcp/server.py`).

### Invariants And Boundaries

- These tools mutate the same dashboard catalog as the browser route; `attach` does not create a new
  terminal, and `spawn_agent_session` spawns tmux + upserts a catalog row directly (in-process, over
  the shared opener) rather than calling the running daemon — no HTTP hop, no daemon-reachability
  dependency, the same posture as `attach`.
- `leaf-taken` / `unknown-session` (attach) and `leaf-taken` / `harness-unknown` /
  `harness-not-detected` / `bad-kind` (spawn) are successful tool responses with `ok: false`; callers
  branch on `status`, not exceptions.
- **Statuses are typed at the producer, not only at `model_validate`**
  (260731-EFA-L4). Payload builders here hand an untyped dict to the MCP handler,
  which has no `except` for a `ValidationError`, so a status the response model
  does not know would surface as an unhandled exception rather than a refusal.
  `_spawn_refusal`, `_knob_refusal`'s check table, `_retire_payload` and
  `_rename_payload` all take the `models/terminal.py` alias. Import the alias; do
  not re-declare it here (that is the cycle those aliases exist to avoid).
- **`ok` has one owner per tool.**
  cit:([`_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:911-911) encodes
  `SessionRetireResponse.ok`'s documented rule, and `_rename_payload` computes
  `status == "renamed"`. A new refusal status must not be able to arrive as
  `ok=True` from a call site that restated the rule.
- **Two spawn statuses are produced outside this file.**
  `SpawnAgentSessionStatus` folds in `worktrees/leaf_refs.py::LeafRefStatus`, so
  `leaf-ref-not-found`/`leaf-ref-ambiguous` are reachable spawn refusals that no
  enumeration inside this module lists. The `spawn_agent_session` docstring
  rosters eleven of the thirteen; that gap is intentional and **pinned by test**
  rather than edited, because the docstring is the published MCP tool description.
- Leaf uniqueness stays server-arbitrated: `spawn_agent_session` surfaces `leaf-taken` (with the owning
  session) and never overrides it.
- Live same-id launch conflict maps to `launch-selection-invalid`; the tool never overwrites actual
  process provenance and has no expectation, log-binding, or brief-delivery phase to enter.
- Leaf keys written by attach/spawn are canonical qualified task-doc ids; legacy refs are accepted only
  when the task-tree resolver can prove one match.
- Spawned-by provenance (`spawnedBySession` + `spawnedByLifecycle`) is recorded on the catalog row so
  the dashboard can render the orchestration tree; the tool also carries it on its response. Since
  L14 the `spawned` payload also reports `spawnRole` — the `AR_SPAWN_ROLE` the opener persisted from
  the caller's `env` (omitted when the spawn carried no role), the Chats command-tree grouping key.
- The responses remain AR-owned and strict; provider-flexible models are not used here.
- Ordinary callers cannot select spend knobs: non-null legacy caller `harness`/`model`/`effort`,
  direct free-form launch/session controls, `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, and maintained
  harness-native spend/endpoint env keys refuse before any spawn or catalog write. The blocklist
  keeps the retained operational `env` surface from bypassing settings, but it must be maintained as
  harnesses add new spend-affecting env variables.
- Knob resolution precedence (HFX2-L10 over L16) is repo-local level override > global level override
  > repo-local role default > global role default > spawn preference > detection-gated default;
  settings are read PER-USE (an edit applies to the next spawn, no restart), and the resolved
  `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` env riding is preserved — L16 ADDS the argv application on top
  (per-harness flags via the effective registry; env-only harnesses unchanged at the argv).
- Settings-owned launch arguments and session commands belong to launch configuration; caller-supplied
  variants are retired/refused, and none is treated as or ordered against a task brief.
- Spawn success means `spawned-unbriefed`. Readiness proof and a durable `dispatch-brief` post are
  separate required operations; spawn never reports context-delivery booleans or captures.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; this is a local MCP wrapper around the dashboard
catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operation is defined by same-repository serving/catalog behavior rather than external documentation. | "def terminal_catalog_path(coordination_root: Path) -> Path:"; "def assign_terminal_session_to_leaf("; "def open_terminal_session(" | mcp/src/agents_remember/serving/terminal_catalog.py:588-588; mcp/src/agents_remember/serving/terminal_leaf_assignment.py:53-53; mcp/src/agents_remember/serving/terminal_opener.py:645-645 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The attach builder normalizes leaf refs before delegating durable assignment to the shared serving helper and returning previous leaf, owner, status, and role. | `attach_terminal_session_to_leaf_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:26-43 |
| The MCP spawn builder delegates to the application command and validates its response; it performs no context paste. | `spawn_agent_session_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:46-63 |
| The application spawn command normalizes refs, resolves settings-owned launch authority, calls the shared opener, and returns `spawned-unbriefed`. | `spawn_agent_session_tool`; `"spawned-unbriefed"` | mcp/src/agents_remember/application/terminal_tools.py:769-842 |
| Leaf-ref refusal payloads are shared by attach and spawn. | `leaf_ref_refusal_payload` | mcp/src/agents_remember/mcp/tools/leaf_ref.py:18-35 |
| The shared opener validates live launch identity and fences create, leaf claim, tmux ensure, and catalog upsert; both role and dashboard paths reuse it. | `open_terminal_session` | mcp/src/agents_remember/serving/terminal_opener.py:620-672 |
| Explicit REST pane input remains a separate serving concern; it is not part of spawn. | `TerminalPaster`; `paste`; `paste_dispatch` | mcp/src/agents_remember/serving/terminal_paste.py:206-511 |
| The harness detection helpers that gate a spawn before tmux, and the curated registry table whose order picks the detection-gated default (the table now lives in `kernel/harnesses.py`; `serving/harnesses.py` imports it and owns detection/launch only). | `find_harness`; `is_detected`; `HARNESSES` | mcp/src/agents_remember/serving/harnesses.py:61-70; mcp/src/agents_remember/serving/harnesses.py:86-93; mcp/src/agents_remember/kernel/harnesses.py:63-77 |
| The per-use agentic-settings loader supplying `spawn_harness` (registry-id validated). | `load_agentic_settings` | mcp/src/agents_remember/kernel/agentic_settings.py:217-252 |
| The public tool tuple advertises `attach_terminal_session_to_leaf` and `spawn_agent_session`. | `PUBLIC_TOOLS` | mcp/src/agents_remember/mcp/tools/base.py:10-69 |
| The facade re-exports all four payload builders. | `__all__` | mcp/src/agents_remember/mcp/tools/__init__.py:93-159 |
| The tool declarations for attach and spawn; the `spawn_agent_session` docstring is the one that states the HFX2-L10 settings-only authority rule, including `spend-override-unsupported` refusals for legacy spend fields and harness-native spend env keys. | `attach_terminal_session_to_leaf`; `spawn_agent_session` | mcp/src/agents_remember/mcp/registration/sessions.py:34-51; mcp/src/agents_remember/mcp/registration/sessions.py:57-137 |
| The strict response models are registered for conformance validation. | "attach_terminal_session_to_leaf": AttachTerminalSessionToLeafResponse,; "spawn_agent_session": SpawnAgentSessionResponse,; "session_retire": SessionRetireResponse,; "session_rename": SessionRenameResponse, | mcp/src/agents_remember/models/tool_registry.py:121-125 |
| `session_retire_payload`/`session_rename_payload` delegate the actual catalog/tmux mechanics to `retire_entry`/`TerminalCatalog.set_label` and the authority check to `check_retire_authority`/`SeatRef`/`master_of`. | `retire_entry`; `check_retire_authority` | mcp/src/agents_remember/serving/retire.py:37-71; mcp/src/agents_remember/serving/retire_policy.py:49-67 |
| Both new builders log observer events through the shared seat-events module. | `log_retire_event`; `log_rename_event` | mcp/src/agents_remember/serving/seat_events.py:24-45; mcp/src/agents_remember/serving/seat_events.py:71-89 |
| The status aliases the producers now take, and the strict response models these builders conform to. | `SpawnAgentSessionStatus`; `SessionRetireStatus`; `SessionRenameStatus` | mcp/src/agents_remember/models/terminal.py:45-71; mcp/src/agents_remember/models/terminal.py:149-155; mcp/src/agents_remember/models/terminal.py:181-181 |
| Failing-first tests for the retire policy matrix, idempotent retire, and rename provenance/role-immutability. | `RetirePolicyMatrixTests`; `test_retiring_an_already_retired_seat_is_idempotent`; `SessionRenameToolTests` | mcp/tests/test_seat_lifecycle.py:103-166; mcp/tests/test_seat_lifecycle.py:280-302; mcp/tests/test_seat_lifecycle.py:319-368 |
| The application refusal enforces the separate exact-session brief-delivery protocol. | `_brief_delivery_separate_refusal`; "brief delivery is separate" | mcp/src/agents_remember/application/terminal_tools.py:567-581 |
| The serving readiness check is performed by `hosted_session_readiness`. | `hosted_session_readiness` | mcp/src/agents_remember/serving/hosted_readiness.py:59-90 |
| The durable brief path uses the `dispatch-brief` message kind. | "DISPATCH_BRIEF_KIND = \"dispatch-brief\"" | mcp/src/agents_remember/serving/dispatch_brief.py:40-40 |
| `LeafRefStatus` — where two of the thirteen spawn statuses are actually declared and produced, outside any file enumerating spawn refusals. | `LeafRefStatus`; `VALID_LEAF_REF_STATUSES` | mcp/src/agents_remember/worktrees/leaf_refs.py:30-30; mcp/src/agents_remember/worktrees/leaf_refs.py:32-32 |
| The `spawn_agent_session` docstring whose eleven-of-thirteen roster is the published tool description — pinned, not edited. | `spawn_agent_session` | mcp/src/agents_remember/mcp/registration/sessions.py:57-137 |
| The test that pins the docstring gap to exactly the two leaf-ref refusals and asserts retire/rename roster equality. | `test_every_status_the_session_tools_roster_validates` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:67-89 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The tool operates on the local dashboard terminal catalog only. | - | - |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted ACPUI L4 candidate. The source still owns
the settings-resolved role spawn path and maps a shared-opener live launch conflict to the existing
launch-selection refusal without respawn. The older blanket claim that catalog readers remain
lock-free is superseded: the opener's same-instance transaction holds the catalog `RLock`, while
other instances may read the coherent last committed atomic-file snapshot.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the separate exact-session refusal protocol binding with the locked scoped fixer and inspected the complete generated function extent; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: replaced the declaration-only anchor with the refusal function and protocol-detail anchors, then returned the whole binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: removed the retired spawn-time paste/log/expectation protocol and documented the current spawned-unbriefed → readiness → durable dispatch-brief sequence; application ownership and new bindings remain provisional.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T01:22+02:00 — 260731-EFA-L4 curator: the card described `session_retire_payload` and
  `session_rename_payload` as building their own payload dicts and said nothing about status
  typing; both are now incomplete. Verified against the diff and the current source and added a
  typed-seam section: cit:([`_spawn_refusal`], mcp/src/agents_remember/application/terminal_tools.py:880-905)
  takes `SpawnAgentSessionStatus` and `_knob_refusal`'s check table is annotated with it
  cit:([`_knob_refusal`], mcp/src/agents_remember/application/terminal_tools.py:423-441); the new
  cit:([`_retire_payload`], mcp/src/agents_remember/application/terminal_tools.py:914-941)
  and cit:([`_rename_payload`], mcp/src/agents_remember/application/terminal_tools.py:1004-1025) are the
  single builders for their tools' results, so
  cit:([`session_retire_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:66-83) and
  cit:([`session_rename_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:86-95) no
  longer restate the shape at each call site;
  cit:([`_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:911-911) gives
  `SessionRetireResponse.ok` one owner. The aliases are imported from `models/terminal.py`
  cit:([`SpawnAgentSessionStatus`, `SessionRetireStatus`, `SessionRenameStatus`], mcp/src/agents_remember/models/terminal.py:45-71; mcp/src/agents_remember/models/terminal.py:149-155; mcp/src/agents_remember/models/terminal.py:181-181)
  to avoid the cycle. Recorded
  the finding that `SpawnAgentSessionStatus` folds in `worktrees/leaf_refs.py::LeafRefStatus`, so
  two of the thirteen spawn statuses are produced entirely outside any file enumerating spawn
  refusals — and that the `spawn_agent_session` docstring rosters only eleven of the thirteen, a
  gap pinned by `test_every_status_the_session_tools_roster_validates` rather than edited, because
  the docstring is the published MCP tool description. Every status, field and `ok` value is
  otherwise unchanged. Added three invariants and four reference rows. **Citation repairs** — all
  ten line ranges in the two reference tables were re-checked and none of the numeric ones landed
  on their claimed symbol: `terminal.py` L16-L42 (a docs row about serving behaviour) → the
  module's serving imports L1-L60; `terminal_opener.py` L170-L648 → `open_terminal_session`
  L620-L672; `terminal_paste.py` L133-L229 → `TerminalPaster` L206-L511; `harnesses.py` L41-L73 →
  `HARNESSES` L76-L103, `find_harness` L105-L114, `is_detected` L130-L137; `base.py` L18-L20 →
  `PUBLIC_TOOLS` L18-L77 (the two names sit at L23-L24, outside the old range);
  `mcp/tools/__init__.py` L86; L94 → imports L72-L75 and the `__all__` entries at L97/L143-L144/L146
  (and the row widened to four builders, since retire/rename are re-exported too);
  `tool_registry.py` L82-L88; L111-L114 → imports L83-L87, registry L121-L125 (and the row widened
  to name all four models). The two rows citing bare symbol names (`attach_terminal_session_to_leaf_payload`,
  `spawn_agent_session_payload`) gained verified ranges.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: `spawn_agent_session_payload` took the
  `seat`/`retired`/`spawned_by`/`overrides` parameter objects (`SpawnSeat`, `RetiredSpawnInputs`,
  `SpawnedBy`, `SpawnOverrides` — the last renamed from `SpawnPorts`, with the reason recorded on the
  type), and `_resolve_spawn_harness` split into `_requested_harness` / `_preferred_harness` /
  `_first_detected_harness`. `retire_entry` now takes a `SeatClosure`. Refusal vocabulary, precedence
  and every payload field are unchanged, and the published MCP signature stays flat. Verification
  metadata pinned until closeout stamps the L2 code commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented role-spawn conflict mapping,
  no alternate spawn or provenance rewrite, and corrected the inherited overbroad lock-free-reader
  statement while preserving settings-owned role dispatch.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented complete role selection,
  typed native launch carriage, runner-side dynamic validation, provenance-only spawn env, the
  no-synthesized-paste invariant, and the retained explicit non-native mapping path. Verification
  metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T21:05+02:00 — Super-exit curator correction: clarified that only session-command
  rows use `envelope=False`; the brief row uses `envelope=True` with its existing unique id envelope.

- 2026-07-10T18:30+02:00 — 260707-HFX2-L18: documented the behavior-preserving
  `_resolve_spawn_leaf` extraction and flat dispatch-local controller flow. The strict CRAP score for
  `spawn_agent_session_payload` fell from `34.25` to `23.02`; settings-owned spend protection, L17
  pair arbitration/log binding, public payloads, and threshold/configuration remain unchanged.
  Verification metadata remains pinned until closeout stamps the eventual L18 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: threaded seat role through attach/spawn payloads and
  expectation rows, and switched retirement checks to binding identity with replacement-leaf
  recovery. Verification metadata remains pinned until closeout stamps L17.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: replaced capture/turn-start spawn credit with bound-log
  user/command evidence, added targeted command reissue and catalog log binding, recorded resolved
  knobs plus `replacementForLeaf`, and extended expectation rows to declared replacements.
  Verification metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): `spawn_agent_session_payload`
  now rejects ordinary caller spend overrides before any side effect (`harness`/`model`/`effort`,
  direct launch/session controls, `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, and maintained Claude/Anthropic
  + Codex/OpenAI harness-native spend/env keys) with `spend-override-unsupported`. Harness/model/
  effort/free-form resolution is settings-only: repo-local level override > global level override >
  repo-local role default > global role default > spawn preference/detection. Documented the accepted
  reviewer note that the blocklist is maintained but not mathematically exhaustive. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L10 commit.
- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 (paste injector hardening, R3): `_deliver_spawn_pastes`
  gained `entry_id`/`harness` parameters and now builds session-command `DeliveryRow`s
  (`envelope=False`, raw text unchanged) plus a brief `DeliveryRow` (`envelope=True`, existing
  unique id envelope), all passed to `serving.injector.deliver` — the raw-spawn seam's separate delivery loop is
  retired; the SAME one path `serving/inbox_delivery.py` uses. `_SpawnDelivery`'s boolean fields keep
  their exact pre-existing meaning, mapped from the richer `DeliveryOutcome`. Every existing
  `test_spawn_agent_session.py` assertion (including exact `paster.calls[...]["text"]` equality)
  passes UNCHANGED. Verification metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `spawn_agent_session_payload` now atomically writes R2 expectation rows via `_write_spawn_expectation_rows` — always a `briefed-by` row, plus a `turn-report-by` row when the spawn claims a leaf (`leaf_key` set). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity): two new
  payload builders, `session_retire_payload` (authority-checked retire: unknown-session/
  unknown-actor/already-retired/retire-refused/retired statuses, kills the tmux session + persists
  retirement provenance, idempotent) and `session_rename_payload` (unknown-session/renamed,
  identity text only). Both delegate mechanics to the new `serving/retire.py` + `retire_policy.py` +
  `seat_events.py` modules and conform to the new `SessionRetireResponse`/`SessionRenameResponse`
  models. `actor_session_id` is self-declared (no ambient caller-identity resolution exists in this
  codebase) — an accepted residual risk per the leaf's builder/reviewer record. Verification
  metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 round 2: a False outcome never ships evidence-less —
  `_deliver_spawn_pastes` gained a `failed` flag and the explicit `"(empty pane capture)"` marker
  (wording aligned with `inbox_delivery`) so `deliveryCapture` is present on every failure, and the
  capture also attaches on submit-failure (not only undelivered).
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): `_deliver_spawn_pastes` returns
  the frozen `_SpawnDelivery` bundle — `contextDelivered`/`sessionCommandsDelivered` are `True` only
  from verified delivery, and `failure_capture` (the paster's final pane snapshot from the latest
  failed paste) rides `_spawned_payload` as `deliveryCapture` on any `False` outcome (omitted on
  full success). Closes the SF-1 blind seat: `contextDelivered: true` once masked a codex pane that
  booted clean with no payload. Verification metadata pinned until closeout stamps the HFX-L3
  commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: attach and spawn now normalize accepted leaf refs to
  canonical qualified task-doc ids before catalog writes/spawn provenance, and return strict
  `leaf-ref-not-found` / `leaf-ref-ambiguous` refusals with expected form plus candidates before any
  mutation. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application; four developer rulings 2026-07-07):
  the dispatch seam now RESOLVES role knobs from settings (`resolved_role_knobs(AR_SPAWN_ROLE,
  level)` — `rolesPerLevel` over flat `roles`; new `level` param leaf|master|portfolio with
  provenance), resolves harnesses against the EFFECTIVE registry (`orchestration.harnesses` — new
  ids add, builtin ids pre-customize; unknown-everywhere ids refuse pointing at the
  `docs/reference/harnesses.md` manual), VALIDATES model/effort per-harness before spawning
  (`effort-invalid`/`model-invalid`/`level-invalid` refusal statuses; claude's two-vehicle effort
  vocabulary with `ultracode` delivered as a post-launch `/effort` session command), and delivers
  the free-form escape hatch (`launch_args` verbatim argv; `session_commands` pasted+submitted
  before the brief; `prompt_keywords` prepended to the brief paste) — never validated, recorded in
  spawn provenance and echoed on the payload. Verification metadata pinned until closeout stamps
  the L16 commit.

- 2026-07-06T23:58:24+02:00 — 260703-L14 (visual hierarchy + chat grouping): the `spawned` payload now
  reports `spawnRole` (`entry.spawn_role` — the AR_SPAWN_ROLE the shared opener recorded on the
  catalog row from the caller's env; `_tool_payload` omits it when `None`). No builder logic
  changed. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T22:25+02:00 — 260703-L13 (settings unification): `harness` became optional —
  `_resolve_spawn_harness` implements explicit arg > repo-local settings > global settings >
  detection-gated default, reading the agentic settings per-use with the repo-local layer
  derived from the qualified leaf key (`_spawn_repo_root`); refusal payloads name the
  settings source; `_spawn_refusal` accepts a None harness. Verification metadata pinned
  until closeout stamps the L13 commit.
- 2026-07-04T11:10+02:00 — L2: added `spawn_agent_session_payload` (+ `_spawn_env` / `_ambient_lifecycle_id`
  / `_spawn_refusal` helpers) — the agent-facing dispatch tool that composes the shared serving opener
  (`terminal_opener.open_terminal_session`) plus an echo-confirmed context paste
  (`terminal_paste.TerminalPaster`). It validates the harness against the detection set before spawning,
  injects model/effort/env at spawn, records spawned-by provenance, surfaces server-arbitrated
  `leaf-taken` without override, and optionally submits so a worker auto-starts. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-02T17:04+02:00 — L9: created the agent-facing `attach_terminal_session_to_leaf` payload
  builder so agents can move their own hosted dashboard chats between task leaves without raw dashboard
  curl or browser clicks. Verification metadata pinned to the task base until closeout stamps the L9
  commit.
