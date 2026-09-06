# mcp/src/agents_remember/worktrees/modules/quality/certification_reuse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/certification_reuse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:15:01+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Validates a decoder’s zero-start gate row against the caller-selected original certificate, result and immutable publication before retaining that terminal.

## Code Commentary

### Logic

`record_retained` refuses an absent retained selection. A reused row must declare `started: false`, `zeroStart: true`, no newly executed rails, the exact original certificate/result digests and complete original publication payload. The selected certificate must name the row’s gate.

The owner validates the growing certificate chain against prepared admission, cross-binds original publication authority and physically reopens every result evidence/artifact. It obtains exact references from the existing certificate store and requires the loaded original objects to equal the caller-supplied objects, including provenance. Only then does it append the certificate and typed terminal to the in-flight publication. The returned dictionary is presentation of that retained result.

A typed certification refusal is rendered as a refused record; this path neither issues a new certificate nor replaces the original publication with the current decoder generation.

### Conventions

Pass explicit `RetainedGateExecution` values from the selected execution contract. The current pointer, a digest alone or an arbitrary history search cannot supply a missing selection.

### Invariants And Boundaries

- Reuse declares zero starts and retains exact originals; it never synthesizes new rail output.
- Catalog equality is necessary but insufficient without chain, publication, physical bytes and canonical store readback.
- In-flight accumulation is separate from operation-journal selection and its live-owner CAS.

### Todos

None recorded for this file's bounded responsibility.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reused row is matched, revalidated and accumulated only with its exact selected originals. | `record_retained` | mcp/src/agents_remember/worktrees/modules/quality/certification_reuse.py:28-89 |
| The decoder transport carries complete original certificate/result/publication objects. | `RetainedGateExecution` | mcp/src/agents_remember/worktrees/modules/quality/execution/models.py:28-38 |
| Typed terminals and the mutable per-publication accumulator remain separate. | `GateRecordPublication` | mcp/src/agents_remember/worktrees/modules/quality/certification_terminal.py:55-60 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |

## Update History

- 2026-09-06T15:15:01+00:00 — Created from the complete source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented the selected-original, terminal or transport responsibility and its actual neighboring owners. Source verification is not execution or acceptance evidence.
