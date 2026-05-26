# mcp/src/agents_remember/providers/grepai/context/workspace.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/workspace.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/workspace.py` renders and writes GrepAI workspace YAML for the provider-owned runtime home.

## Code Commentary

### Logic

It quotes YAML scalars through JSON string encoding, renders a Postgres-backed workspace with embedder provider/model/endpoint/dimensions, emits project entries for each normalized GrepAI root, and writes the final YAML to `layout.workspace_config_file`.

### Invariants And Boundaries

- The default embedder endpoint remains local to the runtime-visible service (`ollama` on `http://localhost:11434`, `lmstudio` on `http://127.0.0.1:1234`) unless settings override it.
- Known Ollama nomic embedder models default to 768 dimensions when settings do not provide dimensions.
- Project paths can be substituted for container-visible paths while the host-side layout remains provider-owned.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The layout module supplies the workspace name, output path, and normalized project roots. | [layout.py](layout.py.md) |
| GrepAI lifecycle actions write the workspace config before starting or synchronizing the Docker-owned runner. | [actions.py](../lifecycle/actions.py.md) |

## Update History

- 2026-05-25T19:33+02:00: Created when GrepAI workspace YAML rendering was split out of `grepai/core.py`.
