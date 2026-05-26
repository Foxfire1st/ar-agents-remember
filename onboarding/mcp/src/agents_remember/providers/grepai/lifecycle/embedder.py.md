# mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `45214435fd2de65765a8230ceb1dcfe188d1944d` |
| lastVerifiedCommitDate | 2026-05-27T00:09:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`embedder.py` owns the managed GrepAI Ollama Docker embedder.

## Code Commentary

### Logic

The module starts or reuses an `ollama/ollama` container, keeps model data under
provider-managed data roots, connects the container to the shared GrepAI Docker
network, waits for `ollama list`, detects whether the configured model is
present, pulls the model when needed, reports status, and writes the embedder
image lock.

### Invariants And Boundaries

- GrepAI must not require a host Ollama installation.
- The embedder container must be reachable from the GrepAI runner through the
  managed Docker network.
- Model readiness is part of lifecycle health, not an optional follow-up.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Embedder settings and container endpoint are derived in GrepAI core. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| GrepAI install/start composes backend, embedder, and runner lifecycle steps. | [actions.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/actions.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from GrepAI Ollama embedder lifecycle extracted out of provider lifecycle.
