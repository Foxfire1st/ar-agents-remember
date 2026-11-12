# mcp/src/agents_remember/memory_quality/gate_five_rails.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Projects the memory domain's complete final catalog into deterministic R11 Gate-5 rail definitions for certification admission.

## Code Commentary

### Logic

gate_five_memory_rails creates one enforcing memory-quality rail per final-catalog item. Identity/version follow the catalog; ordering uses catalog position plus item id. Each rail belongs to memory-domain authority, assigns correction to memory-curator, selects the requested profile id, and declares bounded JSON evidence through the memory-final-certification adapter.

The default configuration digest binds final-catalog version, checker-registry version and the exact catalog population. Callers can supply an already-bound configuration digest explicitly. The function returns sorted definitions and performs no memory reads, mutation, coherence publication or certificate issuance.

### Conventions

Preserve the memory-domain owner and catalog-derived identities. Do not duplicate a hand-maintained final-catalog list in worktree code.

### Invariants And Boundaries

- Every definition is Gate 5 and enforcing.
- The checker registry and catalog changes invalidate the default configuration digest.
- The memory-checker URI is an execution/evidence identifier, not proof that the checker ran.
- No output artifact or green result is synthesized by deriving rails.

### Todos

The final-catalog execution and R21 Gate-5 publication still require a production caller; this file supplies only the definitions.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

- Catalog-to-rail projection and deterministic order [1]
- Configuration digest binds catalog and registry [2]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
