# mcp/src/agents_remember/providers/grepai/context/workspace.py

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

## Evidence

### Repo-Internal References

- The layout module supplies the workspace name, output path, and normalized project roots. [1]
- GrepAI lifecycle actions write the workspace config before starting or synchronizing the Docker-owned runner. [2]
