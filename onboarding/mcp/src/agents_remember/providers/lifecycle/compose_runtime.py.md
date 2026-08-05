# mcp/src/agents_remember/providers/lifecycle/compose_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/compose_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`compose_runtime.py` owns the shared Docker Compose adapter used by provider
lifecycle modules. It keeps the stable Compose assets package-owned while
feeding dynamic override YAML to Compose through stdin.

## Code Commentary

### 260731-EFA-L2 Backend Start Reconciliation

**`BackendStartReconciliation(network, migration=None, forced_remove=None)`** names what a backend
start already did to the host before bringing a container up. Every managed provider start
reconciles the host first: it adopts the compose-owned network, migrates containers and networks
left behind by an unmanaged project, and force-removes a container whose data mount no longer
matches the layout. All three land together in the start result's `network`/`commands` payload, so
they travel together. Both the CGC and GrepAI backend lifecycles import it.

### Logic

`ComposeRender` carries the Compose project name, base file path, and rendered
override YAML, and derives the override SHA-256 for debug/status payloads.
Asset helpers locate committed provider runtime assets under
`agents_remember/package_data/runtime/providers`. `compose_command()`,
`run_compose()`, and `compose_plan()` build or execute `docker compose` with the
package base file plus `-f -` for the rendered override. Template helpers fill
`@PLACEHOLDER@` tokens, JSON-quote scalar YAML values, render environment maps,
render Compose port mappings, and produce optional YAML lines. `host_user()`
returns the host `uid:gid` (or `None` when `os.getuid`/`os.getgid` are
unavailable, e.g. non-POSIX hosts), and `host_user_block()` renders it as an
optional `user:` YAML line so provider containers can run as the host user. Auto host ports
render as an empty published-port segment (`host::container`) so Compose can
parse the service while Docker chooses a port. Unmanaged migration helpers now
cover containers and networks: both inspect Compose project labels, produce
dry-run removal payloads, and remove only resources that do not already belong
to the expected Compose project. `required_ownership_labels()` is the shared
Compose boundary for provider Docker ownership labels; it rejects settings that
do not include non-empty string `instance.labels` instead of emitting fallback
or legacy labels.

Current-state note: `host_user()` resolves `os.getuid` and `os.getgid` with
`getattr()` and checks both values are callable before invoking them. Non-POSIX
hosts therefore return `None` without making POSIX-only `os` attributes part of
the Windows/Pyright contract.

### Invariants And Boundaries

- Rendered Compose override YAML is execution input and is passed through stdin;
  it is not persisted into coordination or model workspace state.
- Provider modules supply validated MCP-derived settings; this shared module
  must stay provider-agnostic.
- `overrideSha256` is a status/debug signal for the rendered input, not
  authority for a workspace-local override file.
- Unmanaged-container migration must not remove containers that already belong
  to the expected Compose project.
- Unmanaged-network migration must not remove networks that already belong to
  the expected Compose project.
- Compose-rendered provider resources must carry generated ownership labels;
  unlabeled provider settings are invalid.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | `# Sources` | system/sources.md:1-3 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Compose rendering and execution use `docker compose --project-name <project> -f <base> -f -`, and `run_compose()` passes the rendered override through stdin. | `run_compose` | mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:72-84 |
| Template helpers reject unresolved placeholders, JSON-quote YAML scalar/environment values, render `auto` host ports as Compose's empty published-port form, and require generated ownership labels before rendering provider resources. | `auto` | mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:98-141 |
| `host_user()` uses `getattr()` plus `callable()` checks before reading POSIX uid/gid APIs, returning `None` on hosts that do not expose them. | `host_user` | mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:151-156 |
| Compose migration checks Docker Compose project labels before removing unmanaged pre-Compose containers or networks. | `container_managed_by_project`; `network_managed_by_project` | mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:173-174; mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:202-203 |
| Removal command construction, dry-run payloads, and real command result formatting are split into focused helpers for containers and networks. | `remove_container_command`; `remove_network_command` | mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:206-207; mcp/src/agents_remember/providers/lifecycle/compose_runtime.py:210-211 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is required beyond Docker/Compose runtime execution. | n/a | n/a |

## Update History

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 5 citation items; scoped citation check now passes.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `BackendStartReconciliation` so the CGC and GrepAI backend starts report host
  reconciliation as one value. Additive; emitted payloads are unchanged. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-06T17:27+02:00 — Updated after `host_user()` switched to `getattr()` plus `callable()` checks so Windows/Pyright does not treat POSIX-only `os.getuid` and `os.getgid` as required attributes.
- 2026-05-31T12:30+02:00 — Documented new `host_user()`/`host_user_block()` helpers that render an optional `user: uid:gid` line so provider containers run as the host user (1.0.0 review remediation).
- 2026-05-28T14:21:08+02:00: Updated after Compose rendering began rejecting
  provider settings without generated `instance.labels`.
- 2026-05-27T00:25+02:00: Updated after auto host ports began rendering as
  `host::container` and unmanaged Compose network migration joined container
  migration.
- 2026-05-27T00:06+02:00: Updated after unmanaged Compose container removal was split into focused helpers to resolve touched-file Radon pressure.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
