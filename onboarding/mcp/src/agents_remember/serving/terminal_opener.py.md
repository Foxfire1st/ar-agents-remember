# mcp/src/agents_remember/serving/terminal_opener.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_opener.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the single hosted-session opener shared by the dashboard terminal route and agent-facing spawn
tool. It resolves the server-owned base command, preserves role/lineage provenance, arbitrates one
live seat per leaf-role pair, and carries a typed native launch selection into the exact-session
control runner without creating a parallel spawn path. It also treats an already-live process as
immutable launch truth, so an idempotent reopen cannot rewrite model/effort or control provenance.
260718-CHATS-L0E adds one additive optional `resume_thread_id` parameter threaded into the runner
payload for the codex harness only.

## Code Commentary

### Logic

`resolve_terminal_launch` resolves a terminal shell or detected harness id to server-owned base argv.
For native Claude/Codex/Pi it leaves normalized model/effort to the typed `ResolvedLaunch` carried in
the runner payload; it applies `legacy_model`/`legacy_effort` only through an explicitly declared
settings-defined non-native mapping. Free-form `launch_args` remain verbatim provenance but later
adapter-owned conflicts are refused by the runner before discovery.

`open_terminal_session` resolves only the server-owned command before entering `TerminalCatalog.batch`.
The batch fences the complete durable read, live-process check, leaf-role arbitration,
`TerminalHost.ensure`, and catalog upsert across threads and processes. A live existing session is
checked before command or provenance mutation. A selectionless or identical-pair reopen returns the
actual retained row without calling `ensure`; changed kind, harness, cwd, or explicit pair returns
`launch-conflict` with that same actual row. A dead row starts a fresh process generation with a new
`createdAt`/control endpoint and does not inherit process-specific control, session-log, free-form,
role-origin, level, or resolved-pair state.

For a fresh generation, `_session_command` launches ordinary shells directly or wraps the native
harness in `harness_control_runner` with exact identity, cwd, base argv, session commands, and typed
launch. The opened row retains leaf/lineage binding where appropriate and records process-specific
spawn role, free-form inputs, resolved model/effort, and endpoint from this generation. Different
roles may coexist on one leaf; a live same-role owner returns `leaf-taken` without process or
catalog mutation.

L0E's `resume_thread_id` is a codex-only native-identity selector in the `launch_args` authority
class: `open_terminal_session` returns `bad-kind` before any spawn when the value targets a
non-codex harness/kind or is empty/outer-whitespace, and otherwise threads it unchanged through
`_open_terminal_transaction` → `_session_command` → `RunnerConfig`. The opener never validates or
authorizes the resume target; target authorization stays with the later re-authorization seam
before launch. Omitting the parameter preserves the pre-L0E open behavior exactly.

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
- Legacy raw-TUI rows remain explicit legacy state; unsupported custom ids do not receive a native
  compatibility fallback.

### Todos

None known for the L4 shared opener boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The opener deliberately separates command/id resolution, role arbitration, typed runner startup,
and caller-specific response shaping.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The hosted runner decodes the typed launch, validates against dynamic advertise, applies native knobs, and persists exact failures. | L37-L191 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| Native launch selection and fail-loud duplicate/catalog validation are centralized in the launch module. | L17-L226 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| Role-scoped leaf arbitration resolves only the same-role owner and marks dead owners exited. | L32-L50 | [terminal_leaf_assignment.py](agents-remember/mcp/src/agents_remember/serving/terminal_leaf_assignment.py) |
| The catalog row owns durable seat, lineage, resolved knob, free-form, and control metadata. | L50-L120 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| The catalog batch holds both the process lock and instance lock across the complete unit of work. | L696-L727 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| The dashboard route maps actual-row success/conflict facts without duplicating spawn composition. | L946-L1049 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The agent-facing spawn tool resolves role settings, calls this opener, and maps live launch conflict to its existing launch-selection refusal. | L474-L628 | [terminal.py](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py) |
| Regression tests pin selectionless/same/conflicting live reopen, dead replacement, cross-process race fencing, and preserved multi-role leaf sharing. | L271-L407 | [test_terminal_opener.py](agents-remember/mcp/tests/test_terminal_opener.py) |
| Resume-channel contract tests pin the opener `bad-kind` refusals with zero host interactions and the codex pass-through into the runner payload. | L1409-L1460 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |

## Cross-Repo References

No external repository boundary is implemented. The helper mutates only local tmux and the local
dashboard terminal catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
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
