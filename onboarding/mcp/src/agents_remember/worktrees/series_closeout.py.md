# mcp/src/agents_remember/worktrees/series_closeout.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Prove completed atomic-master candidates and capture exact series refs for final closeout or a non-final checkpoint.

## Code Commentary

### Logic

The final route resolves canonical master/leaf task membership through `series_leaf_contracts.exact_atomic_leaf_contracts` and requires one exact enclosure per leaf that is not `abandoned`. An `abandoned` row is outside the landing chain: it needs no enclosure, and an enclosure it has whose integration is not completed is ignored. An `abandoned` row whose enclosure records a completed integration refuses by name, because a label never removes a landed leaf from the chain. A master whose rows are all `abandoned` has an empty chain, and the proof then checks that the master's line holds no commit of its own beyond its recorded base. The route verifies each non-abandoned leaf's repository, source branch, base-to-integrated edges, and recorded code/memory output identity, then orders the chain by the landings' own ancestry. It does not order from bases that a later sync legitimately advanced. Every refusal of the chain, the checkpoint capture and the master completion check names the master, the leaf or the contract cell it is about, and the action that clears it (for example `_unordered_leaves_detail` names the leaf pairs whose landings cannot be ordered and the `integrated_code_commit` and `integrated_memory_content_commit` cells to repair).

Without a recorded sync, the oldest leaf starts at the exact series base. With sync history, the origin is proved against the first sync's old bases and each leaf must remain on that line. The series spine must contain every landing and only admitted inter-leaf/source transitions. Memory-side history inspection excludes root memory.md content; the removed special ledger-recording commit exception is not an authority rule.

Every admitted spine step enumerates ordinary and merge commits with full history. A master's line may hold only landed-leaf history and reconciled parent positions. A recorded position lying inside a step may admit its reachable history; a later position outside the step cannot vacate an introduced commit. Merges additionally require a recorded managed-sync produced head, membership inside a landed leaf's own history, or parent-line origin. Older sync entries without produced-head metadata preserve their explicit compatibility admission. Every foreign commit is named with the remedy to move the change into a leaf rather than leaving it on the master line.

Final, checkpoint and recorded master landings invoke this proof over their own exact code/memory endpoints. Checkpoint and recorded routes omit unlanded leaves; an empty landed population may hold only recorded bases and reconciled parent history, never a free master workbench. Recorded landing does not replace its endpoints with mutable branch tips.

Both checkpoint capture and final memory recording use `series_memory_closeout`: re-read the exact code work ref, capture the actual memory work ref, and prove its recorded-base ancestry. They do not select an output from cached rows or require a fixed-point table. A code tip with no corresponding memory trailer can therefore still be captured without inventing attribution.

Final closeout and integration require the master complete. The checkpoint route deliberately does not, and instead refuses an already-completed master, requires an explicit captured `expected` pair, reloads the contract, and revalidates live tips before publication. It records no completed-task claim and reclaims nothing.

### Conventions

Closeout records existing refs rather than committing an ambient series workbench. Substantive dirty checkouts still refuse; memory.md alone is excluded. Checkpoint publication, stop-only pause, and finalization are distinct operations.

### Invariants And Boundaries

- Canonical task membership and exact repository/ref identity remain mandatory.
- A leaf that landed is always part of the chain proof, whatever its row says; an `abandoned` row never needs an enclosure or a landing.
- Order nonempty pairs only; empty pairs need an origin/sync/ordered pair. Duplicate nonempty pairs refuse.
- Cache rows, ordering, and fixed-point projection are never series completion or checkpoint gates.
- No agent-owned ledger-only commit is needed to record a reconciled code tip.
- The checkpoint's expected candidate is required and is re-read before publication.
- A spine step may add only a recorded official position, or a line that a recorded position lying inside that step reaches; a position descending from the step admits nothing.
- Preview and apply consume the same final-completion predicate.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Final closeout and series integration re-prove canonical completion. [1]
- Checkpoint capture retains code and applicable external-memory refs, and publication revalidates that explicit captured candidate. [2]


- Leaf membership, output identity, and ordering remain exact. [3]



- Recorded origins and admitted substantive history preserve reconciled series proof. [4]


- Series cleanliness and actual memory-ref capture exclude cache authority. [5]


- Recorded origins and admitted substantive history preserve reconciled series proof. [6]


### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

- The landing chain is built from the exact enclosures of the non-abandoned rows and then proved. [7]
- An unordered chain names the leaf pairs and the contract cells to repair. [8]

- An empty leaf chain skips leaf-origin validation; spine validation still proves the series ref from its recorded or pre-sync base and admitted source positions. [9]



- With no landed leaf, a spine side proves the series ref from the chain origin and still refuses commits that belong to no landed leaf and to no recorded position. [10]

- An incomplete master names itself, its status and the action that clears it. [11]
