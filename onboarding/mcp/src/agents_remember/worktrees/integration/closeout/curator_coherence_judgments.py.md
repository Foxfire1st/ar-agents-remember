# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns exact candidate-to-judgment set validation and lifecycle capture/revalidation of each cited
evidence file's digest.

## Code Commentary

### Logic

The publication owner copies admitted judgment evidence into its existing content-addressed task artifact root and stamps `evidenceArtifact` with path, SHA-256 and size. Authored `evidenceRef` and `evidenceSha256` remain unchanged. `read_judgment_evidence` validates that exact custody; an old explicit task citation can still be read at its durable address, while legacy code/memory without custody refuses rather than reading today's bytes. `require_recorded_judgments_current` separately rechecks original inputs for live readiness.

`exact_curator_judgments` rejects duplicates, missing tuples, and extra tuples, restores the
attestation's deterministic order, resolves every explicit evidence reference, and returns recorded
judgments with lifecycle-computed SHA-256 digests. `require_recorded_judgments_current` repeats the
digest observation inside the publication CAS window and refuses evidence races.

### Conventions

This module validates and binds agent-owned decisions; it never chooses a disposition or writes a
rationale. Evidence-read failures are translated into the coherence error family.

### Invariants And Boundaries

- Set equality is exact over all three candidate identity cells.
- Evidence content, not merely the path string, is candidate-bound.
- Missing or unreadable evidence fails publication; no alternate root is attempted.

### Todos

None recorded.

## Evidence

### Docs References

No configured external documentation applies.

This is a repository-owned evidence contract.

### Repo-Internal References

- Exact set coverage and lifecycle-computed digests are established together. [1]
- CAS revalidation catches task evidence that changes independently of candidate trees. [2]

The following declarations carry the changed boundary.

- Publication retains exact admitted bytes without rewriting their authored citation. [3]
- Historical reading uses recorded custody or the explicit legacy task address. [4]

### Cross-Repo References

No meaningful cross-repository reference applies.

- Evidence remains confined to contract-owned roots. [5]
