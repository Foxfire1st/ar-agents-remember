# mcp/src/agents_remember/testing/python_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/python_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Provides the parse-only candidate source graph, import bindings, and executable AST facts used by
collection and dependency closure.

## Code Commentary

`CandidatePythonGraph` loads repository files as AST without importing them, tracks the closure,
and resolves candidate-owned modules including `from package import submodule`. `ExecutableVisitor`
collects calls, imports, mutations, and dynamic declarations. Name/decorator helpers normalize AST
references without executing descriptors or decorators.

## Invariants And Boundaries

- Source loading is candidate-root confined and returns typed refusals on parse/path failure.
- Classification must never import candidate modules.
- Ambiguous symbols remain ambiguous; there is no “first match” fallback.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate modules are represented as parsed source plus bindings. | `SourceModule`; `CandidatePythonGraph` | mcp/src/agents_remember/testing/python_source.py:26-36; mcp/src/agents_remember/testing/python_source.py:99-201 |
| Executable facts are collected statically. | `ExecutableVisitor` | mcp/src/agents_remember/testing/python_source.py:45-97 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS; includes actual imported-submodule resolution.
