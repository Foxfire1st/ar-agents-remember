# mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | N/A | N/A |

## Repo-Internal References

These source owners establish the behavior and boundaries above. Citation ranges were read from the current uncommitted candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| Prepared output references and exact raw commit bytes are revalidated. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |
| Live ownership, contract identity, and selected preparation remain bound. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |
| Existing historical memory retains its raw tree while proving the separate certified content. | `certified_tree` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:285-289 |
| The fifth certificate is checked against the correct content subject and current authorities. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |
| Post-publication proof uses a memory-only normalized snapshot and preserves actual HEAD/tree equality. | `_publication_intent` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:443-477 |
| The original per-leg prestate is journaled with the same memory-domain snapshot semantics. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |
| Publication checks original state, uses the exact CAS, and records its proof. | `_record_proof` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:356-387 |
| The accepted pair is proven before the best-effort cache refresh. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |
| Only code and memory outputs are published before canonical contract completion. | "code and memory outputs" | mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:534-534 |
| Resume requires the same generation and exactly two selected output legs. | n/a | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | N/A | N/A |

## Update History

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Removed the ledger publication/recovery account; recorded independent raw/certified memory proof, two-output finalization, all three normalized memory snapshots, and non-authoritative cache refresh. Source SHA-256 `5d5b77b235f8fa91080e88a14da1b13430ea8150b6104b31d4675da1c4edbf0d`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No content impact: this source behavior and source-to-card meaning remain unchanged while the shared sidecar and route body validators run independently. No acceptance claim is made.
- 2026-09-08T14:45:44+00:00: CCR-L24 preparation re-read `resume_prepared_closeout` and its finalization helpers against the current source; wording retained and ranges regenerated. Verification metadata remains pinned pending final pair composition.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_materialize_ledger` repointed to mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:433-468. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_publish_leg` repointed to mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:577-610. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_closed_payload` repointed to mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:613-630. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `finalize_prepared_closeout` repointed to mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:633-670. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `resume_prepared_closeout` repointed to mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:673-710. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T21:46:58+00:00 — Reconciled landed IAS helper ownership and source anchors. Verification pins and historical evidence remain unchanged; no certification or delivery is asserted.

### 2026-09-06T17:14:07+00:00 — Initial L34 implementation card

Recorded the released implementation without claiming tests, certification or acceptance.
