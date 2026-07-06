# mcp/src/agents_remember/serving/terminal_opener.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/terminal_opener.py`    |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-06T23:58:18+02:00                                  |
| lastVerifiedCommitHash | `278a7bf789ceca4378b0de44ba9fae4ec2f1d4b2`              |
| lastVerifiedCommitDate | 2026-07-06T13:30:12+02:00|
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

### Logic

`OpenTerminalStatus` is the `Literal["opened", "leaf-taken", "bad-kind"]` outcome tag and
`OpenTerminalResult` is the small frozen result object — an upserted `entry`, the resolved `kind`, a
conflicting `owner_session_id`, or a `detail` string for a bad kind. The opener is transport-agnostic:
`app.py` maps the result to an HTTP `JSONResponse` (200 / 409 / 400) and the MCP tool maps it to a
validated tool payload.

`resolve_terminal_launch(kind, *, workspace_root, shell, harness, which)` resolves a launch `kind` to
`(cwd, argv)` server-side — the server owns the command, never the wire. `terminal` spawns `shell` at
the workspace root; `harness` spawns the registered TUI harness by **id** (`find_harness` +
`is_detected`, `which` defaulting to `shutil.which`), rejecting an absent id, an unknown id, or an
uninstalled CLI; every other kind raises `ValueError`. It moved here verbatim from `app.py` so the
opener owns launch resolution and both callers share it without importing `app`.

`open_terminal_session(*, catalog, host, session_id, kind, workspace_root, shell, harness, label,
lifecycle_id, leaf_key, env, spawned_by_session, spawned_by_lifecycle, which)` is the composition. It
resolves the launch (a `ValueError` becomes `bad-kind` with the detail), computes the role-scoped
`leaf_conflict_owner` **before** any spawn (a taken leaf returns `leaf-taken` WITHOUT ensuring tmux or
mutating the catalog — the server-authoritative uniqueness check), calls `host.ensure(...)` seeding
`env` at spawn (the L2 knob-injection seam) with `suspend_unsafe=(kind == "harness")`, then upserts a
`TerminalCatalogEntry`. The entry preserves an existing row's `created_at`/`label`/`leaf_key` on
re-open and sets `spawned_by_session`/`spawned_by_lifecycle` **once at first spawn** (a re-open keeps
the original provenance, never clobbers it with `None`). Since L14 the same rule covers the role:
the opener reads `AR_SPAWN_ROLE` out of the caller's `env` (the value the dispatch seam already rides
into tmux) and records it as the row's `spawn_role`, preserving an existing value across a role-less
re-open — a hand-opened session (no env role) records `None`.

### Conventions

This file sits in `serving/` because the durable catalog, tmux host, and launch resolution are
serving-layer runtime state. MCP tools call it, but response shaping stays in `mcp/tools/terminal.py`
and Pydantic modeling stays in `models/terminal.py`. `env` is a `Mapping[str, str]` seam threaded into
`TerminalHost.ensure`; the model/effort → env mapping is the caller's job (`mcp/tools/terminal.py`).

### Invariants And Boundaries

- Leaf uniqueness is **server-arbitrated and role-scoped** (`leaf_conflict_owner` over
  `catalog.active_for_leaf`): a taken leaf returns `leaf-taken` and the caller surfaces it, never
  overrides it. The check runs immediately before the ensure/upsert in the single-process app + atomic
  JSON store, so check-then-write is effectively atomic (the client guard stays advisory).
- `leaf-taken` and `bad-kind` are no-spawn, no-mutation outcomes.
- Provenance is write-once: set at first spawn, preserved across a re-open, never nulled — the L14
  `spawn_role` (from env `AR_SPAWN_ROLE`) follows the same rule as the spawned-by pair.
- The opener resolves a harness **id** to its fixed argv — never a wire-supplied command (no injection
  surface, the 6d posture).

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

## Update History

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
