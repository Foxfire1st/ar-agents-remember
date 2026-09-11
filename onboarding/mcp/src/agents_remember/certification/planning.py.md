# mcp/src/agents_remember/certification/planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff`|
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Compiles one validated canonical registry into immutable, candidate-bound per-gate plans and
re-admits external plans only when they exactly equal that authoritative compilation.

## Code Commentary

### Logic

`compile_certification_plan` requires a clean exhaustive registry report and a declared profile,
then compiles every selected gate in order. Each gate carries earlier-gate prerequisites, exact
rail definitions, canonical waves, and its own digest; the enclosing plan binds the registry,
profile, candidate, and full gate catalog. `admit_certification_plan` reconstructs those exact
bytes and rejects any substitution.

### Conventions

Registry compilation, not caller-authored JSON, is plan authority. Rail ordering comes from the
canonical registry and wave ordering comes from the model's deterministic dependency algorithm.

### Invariants And Boundaries

- Invalid registries and unknown profiles fail before plan publication.
- Every gate selected by the profile is compiled; a certifying plan cannot delete a barrier.
- Registry digest, profile identity/kind, candidate identity, rail catalog, waves, and plan digest
  must all match canonical reconstruction.
- Admission has no compatibility or partial-plan fallback.
- This module plans work but does not execute adapters or select repository-specific rail content.

### Todos

Execution consumes admitted plans in a later owner.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Compilation rejects invalid registries and binds every selected gate to the exact candidate. | `compile_certification_plan` | mcp/src/agents_remember/certification/planning.py:24-67 |
| External plans are authorized only by byte-equivalent canonical reconstruction. | `admit_certification_plan` | mcp/src/agents_remember/certification/planning.py:70-98 |
| Each gate plan includes all earlier profile gates as barriers plus deterministic rails and waves. | `_compile_gate_plan` | mcp/src/agents_remember/certification/planning.py:101-122 |
| Compiled rails preserve ownership, authority, applicability, evidence, dependency, and artifact contracts. | `_compile_rail` | mcp/src/agents_remember/certification/planning.py:137-156 |

## Cross-Repo References

The selected profile is supplied by a repository consumer; no repository name or command is
embedded here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Planning selects generic profile-applicable declarations from the canonical registry. | `_selected_gate_definitions` | mcp/src/agents_remember/certification/planning.py:125-134 |

## Update History

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=f477c26880176315a7d75684b7de0ff371e36664a1b4df65daa291ed7f98b2c1; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-01T03:11+02:00 — Created for exact registry-owned certification plan authority.
  Verification remains closeout-owned until the source candidate is committed.
