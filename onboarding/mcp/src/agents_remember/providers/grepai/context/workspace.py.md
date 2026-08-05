# mcp/src/agents_remember/providers/grepai/context/workspace.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/workspace.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The layout module supplies the workspace name, output path, and normalized project roots. | `GrepaiRuntimeLayout` | mcp/src/agents_remember/providers/grepai/context/layout.py:30-66 |
| GrepAI lifecycle actions write the workspace config before starting or synchronizing the Docker-owned runner. | `grepai_docker_workspace_state` | mcp/src/agents_remember/providers/grepai/lifecycle/actions.py:150-174 |

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 4 citation findings; scoped check passed.

- 2026-05-25T19:33+02:00: Created when GrepAI workspace YAML rendering was split out of `grepai/core.py`.
