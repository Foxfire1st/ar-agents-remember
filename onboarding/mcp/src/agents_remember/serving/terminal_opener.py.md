# mcp/src/agents_remember/serving/terminal_opener.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_opener.py`    |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b`              |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal_opener.py` is the **shared hosted-session opener**: the ONE spawn path both the dashboard
`POST /api/terminal/{session}` route and the agent-facing `spawn_agent_session` MCP tool compose over.
Slice L2 (agent-facing dispatch) extracted the leaf-claim + tmux-ensure + catalog-upsert sequence that
used to live inline in `app.py`'s opener handler so neither call path duplicates it — the invariant is
**no parallel spawn path**. It mirrors `terminal_leaf_assignment.assign_terminal_session_to_leaf`: a
serving-layer policy helper reused by both transports instead of a route-local copy.

## Code Commentary

### 260707-HFX2-L17 Spawn Pair Arbitration

The opener derives the binding role from persisted binding state, the current
`AR_SPAWN_ROLE`, or legacy transport fallback, then liveness-checks only the same leaf-role owner.
A dead same-role holder is marked exited and routine replacement proceeds; a live same-role holder
still returns `leaf-taken`, while different roles coexist. The opened catalog row persists
`seat_role` and returns it in the result. Reviewer O3 is intentional current behavior: when an
existing session id is reopened with a different role env, its persisted binding outranks the new
env; role changes use attach/rebind, and normal spawning uses fresh ids.

### Logic

**260707-HFX2-L15 opener provenance.** `open_terminal_session` accepts and preserves an optional
`replacement_for_leaf`, settings-resolved model/effort, and any existing session-log binding while
building the catalog row. These are provenance fields only: `replacement_for_leaf` does not claim
the occupied leaf, and reopening must not discard an established log binding.

`OpenTerminalStatus` is the `Literal["opened", "leaf-taken", "bad-kind"]` outcome tag and
`OpenTerminalResult` is the small frozen result object — an upserted `entry`, the resolved `kind`, a
conflicting `owner_session_id`, or a `detail` string for a bad kind. The opener is transport-agnostic:
`app.py` maps the result to an HTTP `JSONResponse` (200 / 409 / 400) and the MCP tool maps it to a
validated tool payload.

`resolve_terminal_launch(kind, *, workspace_root, shell, harness, which, model, effort, launch_args,
harnesses)` resolves a launch `kind` to `(cwd, argv)` server-side — the server owns the command,
never the wire. `terminal` spawns `shell` at the workspace root; `harness` spawns the TUI harness by
**id** against the EFFECTIVE registry (`harnesses` = builtin table merged with
`orchestration.harnesses`, `None` = builtin only), rejecting an absent id, an id known nowhere (the
`unknown_harness_detail` teach-it-via-settings refusal), or an uninstalled CLI; every other kind
raises `ValueError`. Since 260703-L16 it is ALSO the knob-application point: `model`/`effort` are
validated first (`invalid_model_detail`/`invalid_effort_detail` — an out-of-vocabulary effort raises
naming the harness and both value sets instead of letting the CLI warn-and-silently-degrade), then
mapped onto the harness's flags via `knob_argv` (session-vocabulary values stay off the flag;
env-only harnesses get no flags), and `launch_args` is appended VERBATIM (the free-form escape —
never validated). A plain `terminal` spawn ignores the knobs.

`open_terminal_session(*, catalog, host, session_id, kind, workspace_root, shell, harness, label,
lifecycle_id, leaf_key, env, launch_args, prompt_keywords, session_commands, spawn_level,
spawn_level_source, spawned_by_session, spawned_by_lifecycle, which, harnesses)` is the composition.
It resolves the launch — passing `env["AR_SPAWN_MODEL"]`/`env["AR_SPAWN_EFFORT"]` into the knob
mapping while the env keeps riding for session-start visibility (a `ValueError` becomes `bad-kind`
with the detail) — computes the role-scoped
`leaf_conflict_owner` **before** any spawn (a taken leaf returns `leaf-taken` WITHOUT ensuring tmux or
mutating the catalog — the server-authoritative uniqueness check), calls `host.ensure(...)` seeding
`env` at spawn (the L2 knob-injection seam) with `suspend_unsafe=(kind == "harness")`, then upserts a
`TerminalCatalogEntry`. The entry preserves an existing row's `created_at`/`label`/`leaf_key` on
re-open and sets `spawned_by_session`/`spawned_by_lifecycle` **once at first spawn** (a re-open keeps
the original provenance, never clobbers it with `None`). Since L14 the same rule covers the role:
the opener reads `AR_SPAWN_ROLE` out of the caller's `env` (the value the dispatch seam already rides
into tmux) and records it as the row's `spawn_role`, preserving an existing value across a role-less
re-open — a hand-opened session (no env role) records `None`. L16 extends the same
write-once-preserve rule to the free-form spawn provenance (`launch_args`/`prompt_keywords`/
`session_commands`, recorded verbatim, never validated) and the resolved dispatch level
(`spawn_level` + `spawn_level_source` — the rolesPerLevel resolution input).

### Conventions

This file sits in `serving/` because the durable catalog, tmux host, and launch resolution are
serving-layer runtime state. MCP tools call it, but response shaping stays in `mcp/tools/terminal.py`
and Pydantic modeling stays in `models/terminal.py`. `env` is a `Mapping[str, str]` seam threaded into
`TerminalHost.ensure`; the settings-rung knob RESOLUTION (role/level → model/effort/free-form) is
the caller's job (`mcp/tools/terminal.py`) — the opener consumes the resolved env values and applies
them at the argv boundary.

### 260713-PHA-L1 control bridge metadata

Harness opens derive additive control metadata from the exact harness id and existing catalog row:
control state, private endpoint, and protocol version. An unregistered harness adapter is reported
as `unsupported`; the opener does not substitute pane, regex, or log timing. Existing catalog rows
retain their metadata on re-open.

### Invariants And Boundaries

- Leaf uniqueness is **server-arbitrated and role-scoped** (`leaf_conflict_owner` over
  `catalog.active_for_leaf`): a taken leaf returns `leaf-taken` and the caller surfaces it, never
  overrides it. The check runs immediately before the ensure/upsert in the single-process app + atomic
  JSON store, so check-then-write is effectively atomic (the client guard stays advisory).
- `leaf-taken` and `bad-kind` are no-spawn, no-mutation outcomes.
- Provenance is write-once: set at first spawn, preserved across a re-open, never nulled — the L14
  `spawn_role` (from env `AR_SPAWN_ROLE`) follows the same rule as the spawned-by pair.
- The opener resolves a harness **id** to its fixed argv — never a wire-supplied command (no injection
  surface, the 6d posture); knob values ride as discrete argv elements, and argv customization exists
  ONLY through the fail-loud `orchestration.harnesses` settings family.
- Effort/model vocabulary enforcement is duplicated here as defense in depth (the MCP tool
  pre-validates for the named `effort-invalid`/`model-invalid` statuses; the opener's `ValueError`
  → `bad-kind` covers any residual caller so the warn-and-degrade path can never be reached).

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation defines this local opener policy; the same-repository
catalog, host, route, tool, and tests are the source of truth.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this local hosted-session opener composition. | L84-L174 | [terminal_opener.py](terminal_opener.py) |

## Repo-Internal References

The opener is intentionally shared by the dashboard HTTP route and the agent-facing MCP tool.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The dashboard opener route delegates the whole spawn composition to `open_terminal_session` and maps its status to 400/409/200. | L579-L620 | [app.py](app.py) |
| The agent-facing `spawn_agent_session` tool composes the same opener, then an echo-confirmed paste. | L82-L189 | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| `TerminalHost.ensure` seeds the L2 `env` at `tmux new-session -e KEY=VALUE` and is inert on a re-attach. | L370-L410 | [terminal.py](terminal.py) |
| Role-scoped `leaf_conflict_owner` over `catalog.active_for_leaf` is the reused uniqueness probe. | L28-L42 | [terminal_leaf_assignment.py](terminal_leaf_assignment.py) |
| The catalog row carries the migration-safe `leaf_key` + spawned-by provenance columns the opener writes. | L47-L54; L108-L111 | [terminal_catalog.py](terminal_catalog.py) |
| Opener unit tests cover opened+provenance+env, leaf-taken-without-spawn, bad-kind, and undetected-harness against a fake host. | L89-L149 | [../../../tests/test_terminal_opener.py](../../../tests/test_terminal_opener.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This helper spawns tmux + mutates only the local dashboard terminal catalog. | — | — |

### 260713-PHA-L5 Bridge-Backed Launch

New Claude, Codex, and Pi hosted sessions launch one bridge runner with exact catalog identity and
private endpoint. Custom/settings-only ids are unsupported, existing raw-TUI rows remain legacy,
and ordinary shell terminals retain direct launch/input behavior.

## Update History
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
