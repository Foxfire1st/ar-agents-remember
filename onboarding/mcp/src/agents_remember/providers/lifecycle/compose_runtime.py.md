# mcp/src/agents_remember/providers/lifecycle/compose_runtime.py

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

## Evidence

### Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

- No relevant external documentation source is configured for this file. [1]

### Repo-Internal References

- Compose rendering and execution use `docker compose --project-name <project> -f <base> -f -`, and `run_compose()` passes the rendered override through stdin. [2]
- Template helpers reject unresolved placeholders, JSON-quote YAML scalar/environment values, render `auto` host ports as Compose's empty published-port form, and require generated ownership labels before rendering provider resources. [3]
- `host_user()` uses `getattr()` plus `callable()` checks before reading POSIX uid/gid APIs, returning `None` on hosts that do not expose them. [4]
- Compose migration checks Docker Compose project labels before removing unmanaged pre-Compose containers or networks. [5]
- Removal command construction, dry-run payloads, and real command result formatting are split into focused helpers for containers and networks. [6]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is required beyond Docker/Compose runtime execution.
