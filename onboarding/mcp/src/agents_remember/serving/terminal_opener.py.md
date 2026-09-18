# mcp/src/agents_remember/serving/terminal_opener.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_opener.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T09:35+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Opens or reuses hosted occupants and persists their structural task-document-and-role binding. Runtime
launch mechanics remain plane-owned behind structural dispatch. Since 260915-CAPS-L5 it also carries
the admitted role capsule from the launch boundary onto the runner configuration, as an optional
value it transports but never derives; since **260915-CAPS-L15** it carries both of the harness
carriers that resolution can produce — Codex's instruction field and eve's binding environment — and
refuses a refusal defensively rather than spawning.

## Code Commentary

The catalog batch spans the complete read, liveness probe, ensure and upsert transaction. A live row returns through `_live_open_result` before any spawn path; its launch provenance cannot be rewritten by reopen. A dead replacement builds a new catalog entry with fresh process control metadata instead of retaining the departed process's session observations. Role/altitude and occupied-seat refusals occur before `host.ensure`. Dashboard and structural dispatch share this opener, and since the eve product-integration change set they ask it **two different launchability questions** through one request field.

### Logic

**Two questions, one field.** `TerminalLaunchRequest.session_backend` (145) states which question the
caller is asking, and `_require_launchable_harness` (299) answers it:

- **A terminal OPEN** (the default, `session_backend=False`) execs `argv[0]`, so what it needs is a
  program that **exists**. It consults `terminal_launch_detail` and refuses by name when the harness is
  detected but has no program to launch — which is exactly eve's case. The dashboard's terminal-open
  route deliberately does not set the field, so opening eve as a terminal refuses instead of silently
  resolving to an impossible command.
- **A session BACKEND spawn** (`session_backend=True`, set by the seat-spawning caller in
  `application/terminal_tools.py`) starts the control runner, which owns the harness's own runtime; the
  harness `argv` is data the runner carries to its adapter. The question there is detection: the
  runtime has to be *startable*, not be a PATH program — so it consults `is_detected`.

A harness kind always runs behind the control runner, so for a PATH TUI the two questions coincide;
they diverge only for a harness whose runtime is an application. Answering both with detection alone is
what let a detected eve row resolve to an argv whose program exists nowhere — a false affordance rather
than a launch.

**The capsule's two carrier halves (260915-CAPS-L5, extended by 260915-CAPS-L15).** The launch point
resolves one `LaunchCapsule` and passes it on `TerminalLaunchRequest.capsule`; the opener reads it and
**still derives nothing**:

- **Codex.** `_codex_capsule_delivery(launch)` returns the resolved capsule's `codex_delivery` when it
  has one, and otherwise falls back to the pre-existing caller field
  (`launch.control.capsule_delivery`, L5's own seam) — the resolution first, the caller field second, so
  there is one authority and a caller that supplied a capsule directly is still supported.
  `_session_command` copies the result onto `RunnerConfig.capsule_delivery`, one field, unchanged.
- **eve.** `_eve_capsule_env(launch)` returns the resolved capsule's `eve_env`, and
  `_open_terminal_transaction` folds it into the spawn environment (`spawn_env.update(...)`), which is
  where L7's loader already reads the binding from (`AR_BINDING_REF`, `AR_CAPSULE_PATH`,
  `AR_CAPSULE_DIGEST`, plus `AR_WORKSPACE_ROOT`). The names come from the carrier module, so the writer
  and the reader cannot drift into two spellings. A launch with no capsule contributes nothing, so every
  pre-existing path is byte-identical.

**A refusal never spawns, even if a caller bypassed the gate.** `open_terminal_session` opens with a
defensive check: a launch whose `capsule.is_refusal` returns
`OpenTerminalResult(status="launch-conflict", detail=capsule.explain())` before task binding, before
the occupied-seat check and before any catalog mutation. Every launch point already refuses a capsule it
could not supply *before* it builds a request, so this branch is reachable only by a caller that skipped
that gate — and refusing again is the only outcome that cannot start a role-configured session with no
instructions.

`open_terminal_session` validates launch and task binding, refuses an occupied singular seat, creates
the catalog row, and starts the hosted process. The opener scrubs inherited daemon identity before
seeding the new hosted environment; the structural application subsequently exact-pins the initial
brief. Existing live launch identity is never silently rewritten. Since 260821-ARSPAWN-L1
`SpawnProvenance` carries `spawned_by_kind` (`plane|ambient|unattributed`), the caller-kind half of
spawn provenance; `_opened_catalog_entry` maps it onto the catalog row write-once via `_preserved`,
and the sibling provenance writers (`conversation/library/open_service.py`,
`serving/_app_terminal_routes.py`) keep the `None` default.

Reviewer ownership is a separate, generation-bound provenance pair:
`structural_parent_task_document_ref` plus `structural_parent_role`. Admission validates the pair
against the review altitude before any process is created: a leaf reviewer belongs to its manager,
a master reviewer to that master's manager, and a sprint reviewer to either the architect plan seam
or orchestrator super-exit seam. A new reviewer without the complete explicit pair refuses before
tmux or catalog mutation; the opener never manufactures a parent from altitude alone. Unlike
historical spawn ancestry, a freshly opened generation
takes the newly admitted reviewer parent instead of preserving the departed generation's parent.
`_task_binding_refusal` delegates document, role, lineage, and parent validation to
`serving.task_binding.resolve_task_binding`; the opener retains a final admission read immediately
before host creation but owns no parallel policy.

### Conventions

Task reference and role arrive already authorized by the structural application for agent dispatch,
or through an operator API boundary.

### Invariants And Boundaries

- A new process cannot inherit its caller's ambient seat identity.
- Seat conflicts are task-document-and-role scoped.
- Reopening never mutates a live occupant's launch provenance.
- Reviewer parent document and role are supplied together, altitude-valid, and bound to one
  process generation; other structural roles cannot carry that pair.
- **Detection is not launchability for a terminal open.** A harness whose runtime is an application is
  detected and still must refuse this path by name; only a caller that states
  `session_backend=True` may resolve it, because that caller spawns the runner rather than the harness.
- This module allocates occupants; it does not define public seat addresses.
- **The capsule is transported, never derived.** The resolved value is read off the request and placed
  on the carrier its harness declares — `RunnerConfig.capsule_delivery` for Codex, the spawn environment
  for eve — and the opener never compiles, selects, renders or validates one. A launch with no capsule
  contributes nothing to either carrier, which is why every pre-existing path keeps the payload it
  always sent.
- **A refusal cannot be spawned.** A launch carrying a refused capsule returns `launch-conflict` before
  any side effect; this is the defensive second gate behind the launch points' own refusals, not a
  decision this module makes.
- **The eve binding environment is written only from the resolved capsule.** Its names come from
  `models/eve_capsule_carrier.py` through `serving/launch_capsule.py::eve_binding_env()`, so the writer
  and the runtime's own reader cannot drift.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Hosted launch strips inherited daemon identity. | `_scrub_daemon_identity_env` | mcp/src/agents_remember/serving/terminal_opener.py:502-522 |
| Binding conflict is checked before the transaction commits. | `_binding_conflict_owner` | mcp/src/agents_remember/serving/terminal_opener.py:669-692 |
| The request field that states which launchability question a caller is asking, and the launch's resolved capsule. | `TerminalLaunchRequest`; `session_backend`; `capsule` | mcp/src/agents_remember/serving/terminal_opener.py:137-192 |
| The two branches: terminal open asks for an existing program, session backend asks for a startable runtime. | `_require_launchable_harness`; `terminal_launch_detail`; `is_detected`; `harness_detection_detail` | mcp/src/agents_remember/serving/terminal_opener.py:317-337; mcp/src/agents_remember/serving/harnesses.py:93-107; mcp/src/agents_remember/serving/harnesses.py:110-124; mcp/src/agents_remember/serving/harnesses.py:127-153 |
| The seat-spawning caller that sets `session_backend=True` and resolves the capsule before this opener runs. | `_spawn_launch_request` | mcp/src/agents_remember/application/terminal_tools.py:740-784 |
| The cases: a terminal open of eve refuses by name and yields no argv, a session-backend spawn still resolves, and the path harnesses are unaffected in both modes. | `EveTerminalLaunchTests` | mcp/tests/test_eve_product_integration.py:751-859 |
| Open coordinates launch, binding refusal, and persistence, and refuses a refused capsule before any of them. | `open_terminal_session` | mcp/src/agents_remember/serving/terminal_opener.py:821-879 |
| Spawn provenance records caller kind write-once onto the catalog row. | `SpawnProvenance` | mcp/src/agents_remember/serving/terminal_opener.py:196-217 |
| The opener maps spawn provenance onto the durable row write-once. | `_opened_catalog_entry` | mcp/src/agents_remember/serving/terminal_opener.py:601-668 |
| Structural admission consumes the shared task-binding authority before process creation. | `_task_binding_refusal` | mcp/src/agents_remember/serving/terminal_opener.py:790-819 |
| The caller-facing capsule field (L5's own seam), and the one place the resolved delivery is copied onto the runner configuration — resolution first, caller field second. | `ControlRunnerRequest`; `capsule_delivery`; `_codex_capsule_delivery`; `_session_command` | mcp/src/agents_remember/serving/terminal_opener.py:113-133; mcp/src/agents_remember/serving/terminal_opener.py:542-554; mcp/src/agents_remember/serving/terminal_opener.py:564-598 |
| The eve half is written as the spawn environment the runtime's loader reads, with the names taken from the carrier module. | `_eve_capsule_env`; `eve_binding_env`; `_open_terminal_transaction` | mcp/src/agents_remember/serving/terminal_opener.py:556-562; mcp/src/agents_remember/serving/launch_capsule.py:325-334; mcp/src/agents_remember/serving/terminal_opener.py:695-788 |
| The runtime's own gate validates the carrier against the workspace it admits, which is why the launch's cwd and the carrier's `AR_WORKSPACE_ROOT` are one value. | `verify_capsule_binding` | mcp/src/agents_remember/serving/eve_runtime_launch.py:466-516 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Structural Spawn Admission

After role/document validation and before any host process side effect, a
structural open resolves ancestry from canonical task identity. Stale or
unavailable lineage returns a typed `OpenTerminalResult` with detail and the
strict projection; non-structural terminals retain their existing path.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `EveTerminalLaunchTests` repointed to mcp/tests/test_eve_product_integration.py:751-859. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T09:35+02:00 — 260915-CAPS-L15 curator: **the opener now carries both carrier halves and
  refuses a refusal.** `TerminalLaunchRequest.capsule` carries the launch point's resolved value;
  `_codex_capsule_delivery` returns the resolved delivery first and the pre-existing caller field
  (`launch.control.capsule_delivery`, L5's seam) second, so there is one authority and a direct caller is
  still supported; `_eve_capsule_env` supplies the binding environment
  `_open_terminal_transaction` folds into the spawn environment, with the names taken from the carrier
  module through `serving/launch_capsule.py::eve_binding_env()` so writer and reader cannot drift. Added
  the defensive refusal in `open_terminal_session`: a launch carrying a refused capsule returns
  `launch-conflict` before task binding, before the occupied-seat check and before any catalog mutation.
  **Superseded in place:** the invariant that said the capsule is only ever copied from
  `ControlRunnerRequest.capsule_delivery` — the opener still derives nothing, but the value now arrives on
  the launch request and reaches two carriers, one per harness. The "capsule's caller-facing half" Logic
  paragraph was rewritten rather than annotated, and every reference row this leaf's own insertions
  shifted was re-anchored (`TerminalLaunchRequest`, `_require_launchable_harness`,
  `_scrub_daemon_identity_env`, `_binding_conflict_owner`, `open_terminal_session`, `SpawnProvenance`,
  `_opened_catalog_entry`, `_task_binding_refusal`, the `ControlRunnerRequest` row) with three rows
  added for the two carrier readers and the runtime's own workspace gate. Verification metadata moves to
  this leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout stamps
  the real code commit and no hash or fingerprint was invented here.
- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: recorded the capsule's caller-facing half at this
  boundary — `ControlRunnerRequest.capsule_delivery` and its unchanged copy onto
  `RunnerConfig.capsule_delivery` in `_session_command` — with the rule that the opener transports an
  admitted value and never derives one. Re-anchored **nine** ranges in this card that this leaf's own
  addition shifted (`TerminalLaunchRequest`, `_require_launchable_harness`, `_scrub_daemon_identity_env`,
  `_binding_conflict_owner`, `open_terminal_session`, `SpawnProvenance`, `_opened_catalog_entry`,
  `_task_binding_refusal`, and the new capsule row), so L8's landed claims keep pointing at their
  constructs. Verification metadata stays at the current committed base `c1dbebf8`; closeout re-stamps.
- 2026-09-16T11:42:31+00:00: Generated citation repair: `_scrub_daemon_identity_env` repointed to mcp/src/agents_remember/serving/terminal_opener.py:484-503. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:42:31+00:00: Generated citation repair: `_task_binding_refusal` repointed to mcp/src/agents_remember/serving/terminal_opener.py:746-774. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **detection is not launchability, and the opener now
  asks the right question for its caller.** Added `TerminalLaunchRequest.session_backend` and the
  `_require_launchable_harness` split it drives: a terminal OPEN execs `argv[0]` and so needs a program
  that exists (`terminal_launch_detail`), while a session BACKEND spawn starts the control runner, which
  owns the harness's runtime, and so needs only detection (`is_detected`). The two questions coincide
  for a PATH TUI and diverge for a harness whose runtime is an application — which is exactly eve, where
  the old detection-only check resolved to an argv whose program exists nowhere. The inline `cit:(…)`
  prose citation in the Purpose section was converted to a reference row in the required
  `Finding | Anchor | Source` shape, and the Logic section rewritten around the two branches. Reference
  table extended with the field, both branches, the seat-spawning caller and the cases. Verification
  metadata moves to the leaf's synced base `ff97072c`; the candidate is deliberately uncommitted, so the
  governed closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-06T22:06:54+00:00 — Preserved source-verified runtime semantics from retired test onboarding; no removed coverage is claimed and verification pins are unchanged.
- 2026-08-31T12:00+02:00 — ARSPAWN-L5 A005 review repair removed the opener-local binding and
  reviewer-parent implementation; the opener now consumes the single `task_binding` authority and
  retains only result translation. Verification remains closeout-owned.

- 2026-08-31T04:59+02:00 — Tightened new reviewer admission: the exact structural parent pair is
  mandatory at every altitude and absence refuses before process creation. Verification remains
  closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded the exact
  altitude-specific reviewer-parent admission contract and why that parent is generation-bound
  rather than preserved across a retired review generation. Verification remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `SpawnProvenance.spawned_by_kind` (`plane|ambient|unattributed`) mapped onto the catalog row by `_opened_catalog_entry` write-once via `_preserved`; sibling provenance writers keep the `None` default. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-12T20:10+02:00 — L23 curator: recorded task-derived lineage admission before structural process creation; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `terminal_opener.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

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
