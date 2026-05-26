# mcp/src/agents_remember/providers/lifecycle/compose_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/compose_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-27T00:25+02:00                     |
| lastVerifiedCommitHash | `767790a0a90c9cdc97eb3e291d42622aced82a14` |
| lastVerifiedCommitDate | 2026-05-27T01:14:04+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`compose_runtime.py` owns the shared Docker Compose adapter used by provider
lifecycle modules. It keeps the stable Compose assets package-owned while
feeding dynamic override YAML to Compose through stdin.

## Code Commentary

### Logic

`ComposeRender` carries the Compose project name, base file path, and rendered
override YAML, and derives the override SHA-256 for debug/status payloads.
Asset helpers locate committed provider runtime assets under
`agents_remember/package_data/runtime/providers`. `compose_command()`,
`run_compose()`, and `compose_plan()` build or execute `docker compose` with the
package base file plus `-f -` for the rendered override. Template helpers fill
`@PLACEHOLDER@` tokens, JSON-quote scalar YAML values, render environment maps,
render Compose port mappings, and produce optional YAML lines. Auto host ports
render as an empty published-port segment (`host::container`) so Compose can
parse the service while Docker chooses a port. Unmanaged migration helpers now
cover containers and networks: both inspect Compose project labels, produce
dry-run removal payloads, and remove only resources that do not already belong
to the expected Compose project.

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

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Compose rendering and execution use `docker compose --project-name <project> -f <base> -f -`, and `run_compose()` passes the rendered override through stdin. | L41-L67 | [compose_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |
| Template helpers reject unresolved placeholders, JSON-quote YAML scalar/environment values, and render `auto` host ports as Compose's empty published-port form. | L81-L112 | [compose_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |
| Compose migration checks Docker Compose project labels before removing unmanaged pre-Compose containers or networks. | L115-L157; L206-L243 | [compose_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |
| Removal command construction, dry-run payloads, and real command result formatting are split into focused helpers for containers and networks. | L160-L203 | [compose_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/compose_runtime.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond Docker/Compose runtime execution. | n/a | n/a |

## Update History

- 2026-05-27T00:25+02:00: Updated after auto host ports began rendering as
  `host::container` and unmanaged Compose network migration joined container
  migration.
- 2026-05-27T00:06+02:00: Updated after unmanaged Compose container removal was split into focused helpers to resolve touched-file Radon pressure.
- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
