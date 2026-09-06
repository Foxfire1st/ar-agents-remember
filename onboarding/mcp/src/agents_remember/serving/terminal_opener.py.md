# mcp/src/agents_remember/serving/terminal_opener.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_opener.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T22:06:54+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Opens or reuses hosted occupants and persists their structural task-document-and-role binding. Runtime
launch mechanics remain plane-owned behind structural dispatch.

## Code Commentary

The catalog batch spans the complete read, liveness probe, ensure and upsert transaction. A live row returns through `_live_open_result` before any spawn path; its launch provenance cannot be rewritten by reopen. A dead replacement builds a new catalog entry with fresh process control metadata instead of retaining the departed process's session observations. Role/altitude and occupied-seat refusals occur before `host.ensure`. Dashboard and structural dispatch share this opener. cit:([`open_terminal_session`; `_open_terminal_transaction`; `_opened_catalog_entry`], mcp/src/agents_remember/serving/terminal_opener.py:742-795; mcp/src/agents_remember/serving/terminal_opener.py:619-708; mcp/src/agents_remember/serving/terminal_opener.py:525-590).

### Logic

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
- This module allocates occupants; it does not define public seat addresses.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Hosted launch strips inherited daemon identity. | `_scrub_daemon_identity_env` | mcp/src/agents_remember/serving/terminal_opener.py:437-475 |
| Binding conflict is checked before the transaction commits. | `_binding_conflict_owner` | mcp/src/agents_remember/serving/terminal_opener.py:578-602 |
| Open coordinates launch, binding refusal, and persistence. | `open_terminal_session` | mcp/src/agents_remember/serving/terminal_opener.py:742-795 |
| Spawn provenance records caller kind write-once onto the catalog row. | `SpawnProvenance` | mcp/src/agents_remember/serving/terminal_opener.py:160-179 |
| The opener maps spawn provenance onto the durable row write-once. | `_opened_catalog_entry` | mcp/src/agents_remember/serving/terminal_opener.py:519-575 |
| Structural admission consumes the shared task-binding authority before process creation. | `_task_binding_refusal` | mcp/src/agents_remember/serving/terminal_opener.py:711-739 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Structural Spawn Admission

After role/document validation and before any host process side effect, a
structural open resolves ancestry from canonical task identity. Stale or
unavailable lineage returns a typed `OpenTerminalResult` with detail and the
strict projection; non-structural terminals retain their existing path.

## Update History

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
