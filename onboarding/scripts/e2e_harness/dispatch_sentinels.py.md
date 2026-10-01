# dispatch_sentinels.py

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Builds controlled malformed variants from the dispatch advertisement observed by real Codex and
proves each variant is rejected by the canonical product validator at its expected boundary.

## Code Commentary

### Logic

`dispatch_rejection_sentinels` accepts the live tool identity, description, and input schema. It
deep-copies the schema before removing `brief`, separately removes the required `ambient`
caller-boundary term, and sends both variants through `validate_dispatch_advertisement`. A sentinel
passes only when `PublicSurfaceViolation` carries the expected diagnostic; acceptance or rejection
at another boundary fails the scenario.

### Conventions

Sentinel names are stable evidence identities. The returned record names expected failure, actual
failure, and the canonical validator as owner; it does not claim that malformed input was a real
Codex advertisement.

### Invariants And Boundaries

- The unmodified live advertisement is validated by `responses_server.py` before these mutations.
- Input schemas are copied before mutation; no live request object is modified.
- Every sentinel must fail at the exact canonical product boundary and expected reason.
- No local schema vocabulary or compatibility validator is maintained here.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured. The observed real-Codex advertisement and canonical
repository validator are the authorities.

- The sentinel corpus is derived from the exact live description and schema. [1]

### Repo-Internal References

- Each malformed candidate must fail through the canonical validator with its expected diagnostic. [2]

### Cross-Repo References

No meaningful cross-repository reference applies.

- The module imports the candidate repository's canonical validator directly. [3]
