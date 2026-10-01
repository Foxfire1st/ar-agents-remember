# mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py

## Governing Overview

[Preparation overview](overview.md)

## Purpose

Guarded publication of the original code and memory-content outputs and canonical contract completion.

## Code Commentary

### Logic

The finalizer reopens the current worker, original preparation/certification objects, raw commit bytes, effective policy, task/source authority, route review, and approval. The complete five-terminal certificate prefix remains required by this explicit prepared route; it consumes selected originals rather than minting or rerunning them.

`_live` binds Gate 5 to the memory intent's cache-free tree, or to `existingMemoryProof.certifiedContentTree` for reused historical memory. `_physical_memory` independently proves the actual raw historical HEAD/tree through the typed binding. Code checks remain strict; only memory observations select the exact cache projection.

`_publication_intent` journals the original prestate, `_publish_leg` checks it before the expected-old CAS, and `_record_proof` accepts output only after physical/index/ref readback. All three snapshots select `memory_cache=True` only for the memory leg, so force-staged cache data cannot strand proof after a valid ref update. A created output's raw HEAD/tree still must equal its exact prepared object; new memory commits cannot contain the cache.

`_retain_existing_leg` records the actual unchanged code or memory commit without creating an empty commit. Finalization and resume require exactly code plus memory-content outputs; no ledger recovery classifier, ledger byte comparison, or third ref publication remains. `_closed_payload` proves the accepted pair and refreshes the consumer cache without making its availability transaction authority. The canonical contract is finalized only after the ordered output proofs.

### Conventions

Use the named source owners directly. The earlier introduction and verification records remain historical facts; the current uncommitted candidate changes the behavior described here. The existing commit-verification metadata is retained until its owner records a real committed source revision.

### Invariants And Boundaries

Prepared objects, selected evidence, publication, and approval remain separate facts. Raw historical HEAD/tree and certified memory content are independently bound and never substituted for each other. Memory cache filtering cannot weaken code checks or admit a cache-bearing new memory commit. Missing or changed non-cache content, moved refs, or changed selected ownership still refuse.

This card describes the explicit prepared-publication owner. It does not assert that the route has passed an end-to-end certification or that ordinary closeout must invoke this certification path.

### Todos

No additional source-local TODO is asserted by this maintenance pass.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

- Prepared output references and exact raw commit bytes are revalidated. [1]
- Live ownership, contract identity, and selected preparation remain bound. [2]
- Existing historical memory retains its raw tree while proving the separate certified content. [3]
- The fifth certificate is checked against the correct content subject and current authorities. [4]
- Post-publication proof uses a memory-only normalized snapshot and preserves actual HEAD/tree equality. [5]
- The original per-leg prestate is journaled with the same memory-domain snapshot semantics. [6]
- Publication checks original state, uses the exact CAS, and records its proof. [7]
- The accepted pair is proven before the best-effort cache refresh. [8]
- Only code and memory outputs are published before canonical contract completion. [9]
- Resume requires the same generation and exactly two selected output legs. [10]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.
