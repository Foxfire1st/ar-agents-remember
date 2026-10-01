# mcp/src/agents_remember/worktrees/modules/quality/certification_reuse.py

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

## Evidence

### Docs References

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- The reused row is matched, revalidated and accumulated only with its exact selected originals. [1]
- The decoder transport carries complete original certificate/result/publication objects. [2]
- Typed terminals and the mutable per-publication accumulator remain separate. [3]

### Cross-Repo References

No separately configured cross-repository source is used for this card.

## CCR-L42 current candidate

`record_retained` now accepts retained certificate identities and passes them into certificate-chain validation. The selected gate still reuses the exact original certificate and publication with zero new starts.
