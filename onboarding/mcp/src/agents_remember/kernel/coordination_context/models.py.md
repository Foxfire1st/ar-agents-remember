# mcp/src/agents_remember/kernel/coordination_context/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`models.py` owns the dataclasses and typed dictionaries returned or consumed by
the coordination-context resolver.

## Code Commentary

### Logic

The module defines missing-memory errors, storage/path-rule model types,
cross-repo allow state, coordination selection, and the final
`CoordinationContext` dataclass used by controllers and integrity tools.

### Invariants And Boundaries

- Models should stay behavior-light and importable by parser, resolver, and
  serialization modules.
- `MissingMemoryError` subclasses `AgentsRememberError` (imported from
  `agents_remember.errors`), so it joins the package's typed error family while
  staying catchable by existing `except ValueError` handlers. It keeps the
  checked internal and external memory paths so callers can report actionable
  initialization guidance, naming the skills in full — initialize memory with
  `c-00-initialize-memory-repo`, then run `c-03-repo-bootstrap`.

## Docs References

No external documentation is needed for these package-local data models.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `MissingMemoryError` subclasses the typed `AgentsRememberError` base instead of bare `ValueError`. | error base import | [errors.py](agents-remember-md/mcp/src/agents_remember/errors.py) |
| Resolver assembly returns `CoordinationContext` instances defined here. | resolver assembly | [resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |
| Serialization converts these models to JSON-safe dictionaries. | serialization | [serialize.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/serialize.py) |

## Cross-Repo References

No cross-repository evidence is needed for local model declarations.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T16:24+02:00 — Normalized skill references in the missing-memory guidance message to full lowercase skill names (`c-00-initialize-memory-repo`, then `c-03-repo-bootstrap`); previously abbreviated C-00/C-03. Reference-style normalization; behavior unchanged.
- 2026-05-31T12:50+02:00 — `MissingMemoryError` now subclasses `AgentsRememberError` (imported from `agents_remember.errors`) instead of the builtin `ValueError`; updated Invariants And Boundaries to state the typed-error-family base and `except ValueError` compatibility, and added the errors.py repo-internal reference (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting coordination-context model declarations from the monolithic resolver.
