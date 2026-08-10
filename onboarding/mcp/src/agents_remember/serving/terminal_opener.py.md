# mcp/src/agents_remember/serving/terminal_opener.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_opener.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded` |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the single hosted-session opener shared by the dashboard terminal route and agent-facing spawn
tool. It resolves the server-owned base command, preserves role/lineage provenance, arbitrates one
live seat per leaf-role pair, and carries a typed native launch selection into the exact-session
control runner without creating a parallel spawn path. It also treats an already-live process as
immutable launch truth, so an idempotent reopen cannot rewrite model/effort or control provenance.
`resume_thread_id` (now `launch.control.resume_thread_id`) remains an optional codex-only selector
threaded into the runner payload.

## Code Commentary

### The two values one open is made of

One open is described by exactly two caller-supplied concepts plus the runtime it lands in. Both are
frozen dataclasses declared in this module and are what the internal chain passes down, so no layer
re-lists fields:

- **`TerminalLaunchRequest`** — *the process identity of a hosted session*: `kind`, `workspace_root`,
  `shell`, `harness`, `which` (installed-ness probe), `harnesses` (the EFFECTIVE registry ids resolve
  against), `env` (the spawn env / knob-injection seam and carrier of `AR_SPAWN_ROLE`), plus nested
  `knobs` and `control`, plus the `legacy_model`/`legacy_effort` compatibility seam. It is the value
  `resolve_terminal_launch` consumes AND the value a live row's recorded provenance is compared
  against, which is the point: the request IS the launch identity. Two derived properties carry the
  rules that used to be recomputed inline — `resolved_kind` (anything not an explicit `harness` is a
  plain `terminal`) and `is_controlled_harness` (a harness with an id, i.e. runs behind the bridge).
- **`SpawnProvenance`** — *what the dispatcher declares about the seat*, none of which ever reaches
  the argv: `label`, `lifecycle_id`, `leaf_key`, `replacement_for_leaf`, `spawned_by_session`,
  `spawned_by_lifecycle`, `spawn_level`, `spawn_level_source`. Every field is write-once across
  reopen (`_preserved`), which is only checkable because they travel as one value. The module
  constant `NO_SPAWN_PROVENANCE` is the opener's default and means "hand-opened seat: no dispatcher
  declared anything".

Three smaller values complete the vocabulary. **`SpawnKnobs`** (`launch_args`, `prompt_keywords`,
`session_commands`) is the settings-owned free-form escape hatch, recorded verbatim and never
validated — the three are one decision applied at three moments of the same launch (argv, pre-brief
runner commands, brief prefix), which is why they are no longer split across parameter lists.
**`ControlRunnerRequest`** (`resolved_launch`, `resume_thread_id`, `endpoint`, `endpoint_root`) is
the caller-supplied half of `RunnerConfig`; the rest is spawn identity the opener derives.
**`HostedSessionRuntime`** (from `hosted_session_runtime.py`) is the catalog+host pair the opener
reads and writes through — `open_terminal_session(runtime=..., session_id=..., launch=...,
provenance=...)` is the whole signature.

`resolve_terminal_launch(launch)` returns a **`LaunchCommand`** NamedTuple (`cwd`, `argv` tuple)
rather than a loose `(Path, list[str])`. `_reopen_state` returns a **`ReopenState`** (`existing`,
`created_at`, `tmux_name`), and `_opened_catalog_entry` takes a **`SpawnOutcome`** (`binding`,
`label`, `seat_role`, `attached_at`, `control_endpoint`) — what one open actually produced once tmux
is ensured and the seat resolved.

### Logic

The shared opener resolves and validates named-seat sprint provenance before ensuring tmux or
writing the catalog. Reopen accepts the same stored pair, rejects partial or conflicting supplied
scope, and inherits a proven parent binding for descendant command roles. These checks are shared
by dashboard open and agent spawn, so neither path can mint an unbound global orchestrator or
manager.

`resolve_terminal_launch` resolves a terminal shell or detected harness id to server-owned base argv.
For native Claude/Codex/Pi it leaves normalized model/effort to the typed `ResolvedLaunch` carried in
the runner payload; it applies the legacy model/effort pair only through an explicitly declared
settings-defined non-native mapping. Free-form `knobs.launch_args` remain verbatim provenance but
later adapter-owned conflicts are refused by the runner before discovery.

`open_terminal_session` resolves only the server-owned command before entering `TerminalCatalog.batch`.
The batch fences the complete durable read, live-process check, leaf-role arbitration,
`TerminalHost.ensure`, and catalog upsert across threads and processes. A live existing session is
checked before command or provenance mutation. A selectionless or identical-pair reopen returns the
actual retained row without calling `ensure`; changed kind, harness, cwd, or explicit pair returns
`launch-conflict` with that same actual row. A dead row starts a fresh process generation with a new
`createdAt`/control endpoint and does not inherit process-specific control, session-log, free-form,
role-origin, level, or resolved-pair state.

**`_live_open_result` is now the single place a live row is handled.** Everything past it is a
spawn — `existing` is either absent or dead — and the code now states that rather than re-deriving
it. Three consequences a future agent must not undo:

- `_reopen_state` no longer probes the host at all; it only decides which tmux name the replacement
  reuses (a first open mints one, a dead row lends its own).
- `_control_metadata` no longer carries prior control state/endpoint/protocol forward. The minted row
  starts at the adapter's advertised status, on `CONTROL_PROTOCOL_VERSION`, bound to the endpoint
  this open resolved. A plain terminal still gets no control columns at all.
- `_opened_catalog_entry` writes this spawn's own knobs, spawn role, resolved pair and level, and
  leaves the bridge observations (`control_activity`, `control_acceptance`, vendor session id,
  pending interaction, last event sequence, `control_raw`) and the session-log columns unset until
  the bridge reports them. Only the two things the departed process never owned survive: the
  write-once seat provenance (`_preserved` against the dead row) and the tmux identity on
  `ReopenState`.

`_launch_identity_conflict` is now a named function returning just the reason string (or `None`),
ordered coarsest identity first: what the session is, then where it runs, then the resolved launch it
was created with. A request carrying no `ResolvedLaunch` cannot disagree about model/effort and stops
after the cwd check. `_live_launch_conflict` still returns the immutable live row alongside it.

For a fresh generation, `_session_command` launches ordinary shells directly or wraps a controlled
harness in `harness_control_runner` with exact identity, cwd, base argv, session commands, and typed
launch, returning `(argv, endpoint)`. `TerminalHost.ensure` is now called with a
`TerminalSessionSpec` (cwd, command, lifecycle id, `suspend_unsafe`, env) rather than five keywords.
Different roles may coexist on one leaf; a live same-role owner returns `leaf-taken` without process
or catalog mutation.

`resume_thread_id` is a codex-only native-identity selector in the `launch_args` authority class:
`open_terminal_session` returns `bad-kind` before any spawn when the value targets a non-codex
harness/kind or is empty/outer-whitespace, and otherwise threads it unchanged through
`_open_terminal_transaction` → `_session_command` → `RunnerConfig`. The opener never validates or
authorizes the resume target; target authorization stays with the later re-authorization seam
before launch.

### Conventions

The opener consumes settings-resolved inputs but does not read or mutate settings. The namespaced
spawn environment still reaches tmux as provenance/runtime context, while the typed
`ResolvedLaunch` is the native initial-selection authority. HTTP and MCP response shaping stay in
their callers; this module returns `opened`, `launch-conflict`, `leaf-taken`, or `bad-kind`.

### Invariants And Boundaries

- Both dashboard and agent-facing spawn compose this same opener; there is no sibling launch path.
- Harness ids—not commands—cross the request boundary; argv remains registry/settings owned.
- A live process's kind, harness, cwd, command, model/effort, and control metadata are immutable
  reopen truth; losing or later callers cannot overwrite them with attempted values.
- The complete read/probe/ensure/upsert transaction is fenced by the catalog batch, not merely the
  final write.
- A live same leaf-role owner refuses before `TerminalHost.ensure` and catalog upsert.
- Role-based spawn, spawned-by lineage, replacement lineage, and the durable catalog survive the
  launch-capability addition unchanged.
- Native model/effort is not statically mapped or pasted here; it rides the typed runner payload and
  is validated/applied by the own adapter.
- Explicit session commands remain user/settings-authored free-form material and are not synthesized
  from normalized native model/effort.
- `resume_thread_id` refuses codex-incompatible kinds/harnesses and malformed shapes with `bad-kind`
  before `TerminalHost.ensure` or any spawn; it is never validated or authorized here.
- **There is no legacy pre-bridge respawn path in this module.** The old `legacy_running` branch —
  which re-spawned a live pre-bridge row's recorded argv and stamped it `control_state="unsupported"`
  / `control_activity="unknown"` / `control_raw={"detail": "legacy raw-TUI session has no protocol
  bridge"}` — was proven unreachable and deleted, because `_live_open_result` returns for every row
  whose tmux session is alive before that branch could ever be evaluated. Do not reintroduce a
  second live-row handler; add to `_live_open_result` instead.
- Every open past `_live_open_result` is a spawn. Any new code below that call may assume the prior
  row's process is gone, and must not read process-owned state off it.

### Todos

None known for the L4 shared opener boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The opener deliberately separates command/id resolution, role arbitration, typed runner startup,
and caller-specific response shaping.

| Finding | Anchor | Source |
| --- | --- | --- |
| The hosted runner decodes the typed launch, validates against dynamic advertise, applies native knobs, and persists exact failures. | `parse_runner_config`; `_prepare_controlled_launch`; `run_controlled_session` | mcp/src/agents_remember/serving/harness_control_runner.py:72-97; mcp/src/agents_remember/serving/harness_control_runner.py:143-189; mcp/src/agents_remember/serving/harness_control_runner.py:192-240 |
| Native launch selection and fail-loud duplicate/catalog validation are centralized in the launch module. | `validate_launch_selection`; `apply_launch_knobs` | mcp/src/agents_remember/serving/harness_launch.py:78-119; mcp/src/agents_remember/serving/harness_launch.py:173-206 |
| Role-scoped leaf arbitration resolves only the same-role owner and marks dead owners exited. | `assign_terminal_session_to_leaf` | mcp/src/agents_remember/serving/terminal_leaf_assignment.py:53-114 |
| The catalog row owns durable seat, lineage, resolved knob, free-form, and control metadata. | `TerminalCatalogEntry` | mcp/src/agents_remember/serving/terminal_catalog.py:80-510 |
| The catalog batch holds both the process lock and instance lock across the complete unit of work. | `batch` | mcp/src/agents_remember/serving/terminal_catalog.py:835-867 |
| The dashboard route maps actual-row success/conflict facts without duplicating spawn composition. | "def _open_terminal_response(" | mcp/src/agents_remember/serving/_app_terminal_routes.py:222-222 |
| The agent-facing spawn tool resolves role settings, calls this opener, and maps live launch conflict to its existing launch-selection refusal. | `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:769-842 |
| Regression tests pin selectionless/same/conflicting live reopen, dead replacement, cross-process race fencing, and preserved multi-role leaf sharing. | `test_live_reopen_preserves_actual_pair_command_and_endpoint`; `test_live_reopen_changed_pair_or_identity_conflicts_without_mutation`; `test_dead_replacement_uses_new_pair_and_fresh_control_generation`; `test_concurrent_different_pair_opens_keep_one_process_and_one_truth`; `test_different_roles_share_leaf_and_dead_same_role_is_replaced` | mcp/tests/test_terminal_opener.py:319-344; mcp/tests/test_terminal_opener.py:433-448; mcp/tests/test_terminal_opener.py:450-466; mcp/tests/test_terminal_opener.py:534-564; mcp/tests/test_terminal_opener.py:566-593 |
| Resume-channel contract tests pin the opener `bad-kind` refusals with zero host interactions and the codex pass-through into the runner payload. | `test_codex_resume_rides_opener_to_runner_payload`; `test_non_codex_resume_fails_closed_before_any_spawn`; `test_malformed_resume_fails_closed_before_any_spawn` | mcp/tests/test_harness_control_evidence_other.py:373-380; mcp/tests/test_harness_control_evidence_other.py:390-396; mcp/tests/test_harness_control_evidence_other.py:398-401 |

## Cross-Repo References

No external repository boundary is implemented. The helper mutates only local tmux and the local
dashboard terminal catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

The opener's parameter lists became named concepts and its one dead branch was deleted rather than
covered. `open_terminal_session` / `_open_terminal_transaction` now take `runtime`
(`HostedSessionRuntime`), `launch` (`TerminalLaunchRequest`, carrying `SpawnKnobs` and
`ControlRunnerRequest`) and `provenance` (`SpawnProvenance`, defaulting to `NO_SPAWN_PROVENANCE`);
`resolve_terminal_launch` takes the request and returns a `LaunchCommand`. Any caller still passing
the old flat keywords (`kind=`, `workspace_root=`, `label=`, `leaf_key=`, `launch_args=`,
`control_root=`, …) is calling a signature that no longer exists.

The legacy pre-bridge argv path is gone: `_live_open_result` is the single place a live row is
handled, `_reopen_state` no longer probes the host, and `_control_metadata` mints control columns
instead of inheriting them.

This entry supersedes any earlier description in this sidecar that conflicts with the current source
behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260718-CHATS-L5I Current Delta

Runner launch now propagates the daemon worktree's package root into the tmux-spawned harness environment. A worktree deployment therefore runs the code it was started to test instead of inheriting a stale main-checkout `PYTHONPATH` from the tmux server.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded pre-host sprint binding, parent inheritance,
  and reopen conflict refusal. Verification metadata remains pinned until closeout stamps the code
  commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: 260731-EFA-L7 changed this file (split/refactor); the card body remains accurate and this entry records the change. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 9 citation claims; scoped result 0 findings.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: rewrote Purpose/Logic/Invariants for the parameter-object
  signatures (`HostedSessionRuntime`, `TerminalLaunchRequest`, `SpawnProvenance`, `SpawnKnobs`,
  `ControlRunnerRequest`, `LaunchCommand`, `ReopenState`, `SpawnOutcome`, `TerminalSessionSpec`) and
  removed the now-false legacy raw-TUI reopen claim: that branch was proven dead and deleted, and
  `_live_open_result` is the single live-row handler. Verification metadata stays pinned until
  closeout.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive codex-only
  `resume_thread_id` pass-through — `bad-kind` refusal for non-codex/malformed values before any
  spawn, unchanged threading into the runner payload, the `launch_args`-class no-validation
  authority posture, and exact absent-parameter behavior preservation. Verification metadata stays
  pinned until closeout stamps the candidate commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented live-process launch truth,
  selectionless/same-pair idempotence, explicit conflicting-pair refusal, dead-generation reset,
  and the cross-thread/process batch fence around read, probe, ensure, and upsert.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented the typed `ResolvedLaunch` runner
  payload, native-vs-explicit-custom mapping boundary, preserved role/lineage/catalog provenance,
  and the rule that normalized native model/effort is never synthesized into a session paste.
  Final audit restored every earlier history entry byte-for-byte below this prepend.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed bridge-backed launch, built-in adapters, and unsupported legacy/custom behavior.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: documented exact-harness control metadata
  and explicit unsupported-adapter reporting in the opener path.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made spawn arbitration live and pair-scoped, persisted
  current seat identity, and documented reviewer O3's deliberate existing-binding precedence on
  the atypical same-id reopen path. Verification metadata remains pinned until closeout stamps the
  eventual L17 commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: threaded replacement-leaf, resolved-knob, and existing
  bound-log provenance through the shared terminal opener. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `resolve_terminal_launch` now
  applies the per-harness knob mapping (env `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` → registry flags via
  `knob_argv`; dispatch-time vocabulary refusal naming the harness and both value sets; verbatim
  `launch_args`) and resolves ids against an injected EFFECTIVE registry (`harnesses` param —
  builtin merged with `orchestration.harnesses`; unknown-everywhere ids get the manual-pointing
  refusal). `open_terminal_session` records the free-form escape hatch
  (`launch_args`/`prompt_keywords`/`session_commands`) and the resolved dispatch level
  (`spawn_level`/`spawn_level_source`) as write-once spawn provenance on the catalog row.
  Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:58:18+02:00 — 260703-L14 (visual hierarchy + chat grouping): `open_terminal_session`
  now records `env["AR_SPAWN_ROLE"]` onto the catalog row as `spawn_role` (write-once like the
  spawned-by pair; preserved across a role-less re-open; `None` for hand-opened sessions) — the
  Chats command tree groups command chats by this role provenance.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T11:10+02:00 — L2: created as the shared hosted-session opener. Extracted
  `resolve_terminal_launch` + the leaf-claim/ensure/upsert composition out of `app.py` so the dashboard
  route and the new agent-facing `spawn_agent_session` tool spawn through ONE opener (no parallel spawn
  path), and added the `env` knob-injection seam + write-once spawned-by provenance. Verification
  metadata pinned until closeout stamps the L2 commit.
