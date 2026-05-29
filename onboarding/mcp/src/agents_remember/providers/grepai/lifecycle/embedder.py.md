# mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`embedder.py` owns the managed GrepAI Ollama Docker embedder.

## Code Commentary

### Logic

The module starts or reuses an `ollama/ollama` container, keeps model data under
provider-managed data roots, reuses any already-running Compose-managed host
port mapping, starts Ollama through the package Compose project, waits for
`ollama list`, detects whether the configured model is present, pulls the model
when needed, reports status, and writes the embedder image lock. It shares the
GrepAI project migration helper so standalone embedder startup can clean
pre-Compose containers and networks before Compose owns them.
Status includes a normalized Docker container state summary so MCP provider
status can report embedder state and uptime.

### Invariants And Boundaries

- GrepAI must not require a host Ollama installation.
- The embedder container must be reachable from the GrepAI runner through the
  managed Compose network.
- Model readiness is part of lifecycle health, not an optional follow-up.
- Existing Compose-managed embedder port mappings are reused on repeated starts
  rather than reallocated from host socket availability.
- Embedder status should expose enough Docker state for current provider status
  without requiring callers to inspect containers themselves.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Embedder settings and container endpoint are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| GrepAI install/start composes backend, embedder, and runner lifecycle steps. | [actions.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py) |
| GrepAI project migration lives with backend startup and is reused here. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |

## Update History

- 2026-05-29T18:35+02:00: `grepai_embedder_dry_run_result` `commands` -> `list[dict[str, Any]]`; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after GrepAI embedder status began including normalized container-state summaries.
- 2026-05-27T00:25+02:00: Updated after Ollama startup began reusing existing
  Compose port mappings and shared GrepAI project migration.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI Ollama embedder lifecycle extracted out of provider lifecycle.
