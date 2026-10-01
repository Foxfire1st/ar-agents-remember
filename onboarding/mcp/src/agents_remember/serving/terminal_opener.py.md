# mcp/src/agents_remember/serving/terminal_opener.py

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

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Hosted launch strips inherited daemon identity. [1]
- Binding conflict is checked before the transaction commits. [2]
- The request field that states which launchability question a caller is asking, and the launch's resolved capsule. [3]
- The two branches: terminal open asks for an existing program, session backend asks for a startable runtime. [4]
- The seat-spawning caller that sets `session_backend=True` and resolves the capsule before this opener runs. [5]
- The cases: a terminal open of eve refuses by name and yields no argv, a session-backend spawn still resolves, and the path harnesses are unaffected in both modes. [6]
- Open coordinates launch, binding refusal, and persistence, and refuses a refused capsule before any of them. [7]
- Spawn provenance records caller kind write-once onto the catalog row. [8]
- The opener maps spawn provenance onto the durable row write-once. [9]
- Structural admission consumes the shared task-binding authority before process creation. [10]
- The caller-facing capsule field (L5's own seam), and the one place the resolved delivery is copied onto the runner configuration — resolution first, caller field second. [11]
- The eve half is written as the spawn environment the runtime's loader reads, with the names taken from the carrier module. [12]
- The runtime's own gate validates the carrier against the workspace it admits, which is why the launch's cwd and the carrier's `AR_WORKSPACE_ROOT` are one value. [13]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Structural Spawn Admission

After role/document validation and before any host process side effect, a
structural open resolves ancestry from canonical task identity. Stale or
unavailable lineage returns a typed `OpenTerminalResult` with detail and the
strict projection; non-structural terminals retain their existing path.
