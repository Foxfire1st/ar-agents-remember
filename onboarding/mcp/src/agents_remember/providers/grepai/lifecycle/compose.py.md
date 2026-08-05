# mcp/src/agents_remember/providers/grepai/lifecycle/compose.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/compose.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[GrepAI Lifecycle Overview](overview.md)

## Purpose

`compose.py` renders the GrepAI Docker Compose override from MCP-derived
provider settings, runtime layout, and runner/backend settings. It keeps
Postgres, Ollama, and watcher dynamic values out of Python `docker run`
assembly while still letting lifecycle code choose ports and paths.

## Code Commentary

### 260731-EFA-L2 Published Ports As One Value

`grepai_compose_render(provider_settings, layout, runner, backend, ports=UNRESOLVED_SERVICE_PORTS)`
takes the two published dependency ports as one `GrepaiServicePorts` (from
`grepai/lifecycle/core.py`) instead of the `postgres_port=` / `ollama_port=` keywords.
`UNRESOLVED_SERVICE_PORTS` is the module-level empty instance meaning **nothing published yet**,
which is what makes the existing fallback read honestly: `ports.postgres or
backend["postgresHostPort"]` and `ports.ollama or embedder["httpHostPort"]` — an unpublished port
falls back to the configured host port, exactly as before. The rendered compose files and their
hashes are unchanged.

### Logic

`grepai_compose_render()` derives Ollama embedder settings, chooses caller
provided or configured host ports, fills Postgres and Ollama images,
containers, ports, and data volumes, points the runner build context at the
committed GrepAI Docker asset, injects runner version/architecture build args,
and renders watcher runtime/log mounts plus a read-write bind-mount of each live
memory root at `/grepai/roots/<project_id>` (`WATCHER_ROOT_VOLUMES`), environment,
workspace name, and network name into the package override template. Port mappings go through the
shared Compose helper so configured `auto` host ports render as Compose's empty
published-port syntax instead of the literal string `auto`. The watcher
environment is rendered from container-local runtime paths, and the Compose
override includes a host UID/GID user block on POSIX hosts so watcher-created
runtime artifacts stay removable by the developer user.
`grepai_compose_summary()` returns the project, package base file, override
hash, and stdin override mode. GrepAI Compose rendering requires generated
`instance.labels` from MCP/provider settings and fails instead of rendering
legacy unlabeled provider resources.

### Invariants And Boundaries

- GrepAI override values must come from provider settings, lifecycle layout, and
  runner/backend derivation, not arbitrary tool input.
- Rendered overrides are fed to Compose through stdin by shared lifecycle
  helpers; this module only renders and summarizes.
- `auto` host ports must remain valid Compose input because every `docker
  compose` invocation parses the whole provider project, even when only one
  service is targeted.
- The watcher uses package-owned runner build assets and mounted runtime/log
  directories from the resolved provider layout.
- The watcher must not receive host-path `HOME`/XDG environment values inside
  the container; GrepAI discovers its workspace config through the mounted
  `/grepai/runtime/home/.grepai` tree.
- GrepAI Docker resources must render with generated Agents Remember ownership
  labels; missing `instance.labels` is an invalid settings shape.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `grepai_compose_render()` fills the package override template and shared port mapping values. | `grepai_compose_render` | mcp/src/agents_remember/providers/grepai/lifecycle/compose.py:42-99 |
| The watcher user block is supplied by `host_user_block()`. | "host_user_block(" | mcp/src/agents_remember/providers/grepai/lifecycle/compose.py:79-79 |
| The summary reports Compose project, package base file, override SHA-256, and stdin override mode. | `grepai_compose_summary` | mcp/src/agents_remember/providers/grepai/lifecycle/compose.py:102-108 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is required beyond mounted runtime roots configured by provider settings. | n/a | n/a |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: anchored compose rendering, watcher user,
  and summary claims to exact symbols; removed the unsupported source-free documentation claim and
  narrowed the helper row to the cited call.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 self-file line citations that shifted when `grepai_compose_render` took the `ports: GrepaiServicePorts` argument. `grepai_compose_render` is now L42-L99 (was L40-L97) and the `WATCHER_USER_BLOCK: host_user_block()` value is now L79 (was L76); both read back and confirmed.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `grepai_compose_render`'s `postgres_port` / `ollama_port` keywords became one
  `ports: GrepaiServicePorts` argument defaulting to `UNRESOLVED_SERVICE_PORTS`. Rendered compose
  output is unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-02T01:15+02:00 — `grepai_compose_render()` now bind-mounts each live memory root read-write at `/grepai/roots/<project_id>` (`WATCHER_ROOT_VOLUMES`) so the watcher indexes the real repos in place instead of a mirror under the runtime mount.
- 2026-05-31T12:30+02:00 — Fixed Repo-Internal citation: local `grepai_user()`/`grepai_user_block()` replaced by shared `host_user_block()` helper; refreshed line ranges (1.0.0 review remediation).
- 2026-05-28T14:21:08+02:00: Updated after GrepAI Compose label rendering began
  rejecting provider settings without generated `instance.labels`.
- 2026-05-27T00:41+02:00: Updated after GrepAI watcher Compose rendering
  switched to container-local env paths and POSIX UID/GID execution.
- 2026-05-27T00:25+02:00: Updated after GrepAI Compose port mappings switched
  to shared `auto`-safe rendering.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
