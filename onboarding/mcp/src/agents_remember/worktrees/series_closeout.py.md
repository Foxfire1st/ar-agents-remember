# mcp/src/agents_remember/worktrees/series_closeout.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Prove completed atomic-master candidates and capture exact series refs for final closeout or a non-final checkpoint.

## Code Commentary

### Logic

The final route resolves canonical master/leaf task membership through `series_leaf_contracts.exact_atomic_leaf_contracts` and requires one exact enclosure per leaf that is not `abandoned`. An `abandoned` row is outside the landing chain: it needs no enclosure, and an enclosure it has whose integration is not completed is ignored. An `abandoned` row whose enclosure records a completed integration refuses by name, because a label never removes a landed leaf from the chain. A master whose rows are all `abandoned` has an empty chain, and the proof then checks that the master's line holds no commit of its own beyond its recorded base. The route verifies each non-abandoned leaf's repository, source branch, base-to-integrated edges, and recorded code/memory output identity, then orders the chain by the landings' own ancestry. It does not order from bases that a later sync legitimately advanced. Every refusal of the chain, the checkpoint capture and the master completion check names the master, the leaf or the contract cell it is about, and the action that clears it (for example `_unordered_leaves_detail` names the leaf pairs whose landings cannot be ordered and the `integrated_code_commit` and `integrated_memory_content_commit` cells to repair).

Without a recorded sync, the oldest leaf's position and the master's recorded base have to lie on one line, either direction (`_require_chain_origin_on_line`), and every other leaf must start at or after that origin. The origin is therefore the master's line rather than one exact commit: a leaf that landed, was reopened and landed again restarts its arc at the position its reopen handed it, which is a later commit on the same line, and requiring equality there would force a hand-edit of the leaf's recorded base to repair a state the product itself created. A position off that line still refuses `atomic-series-leaf-chain-invalid`, naming `worktree_integrate` on the leaf or `worktree_sync` on the master — never an edit of a contract cell. With sync history, the origin is proved against the first sync's old bases and each leaf must remain on that line. The series spine must contain every landing and only admitted inter-leaf/source transitions. Memory-side history inspection excludes root memory.md content; no ledger-recording commit is excepted from it.

The step proof (`_require_admitted_step`) and the merge admission it works from (`_merge_admission`, `_require_admitted_merges`) live in `series_merge_admission.py`; this file keeps the spine walk `_require_landing_spine_side` and its public seam. Every admitted spine step enumerates ordinary and merge commits with full history. A master's line may hold only landed-leaf history and reconciled parent positions. A recorded position lying inside a step may admit its reachable history, and a repository-default sync's source tip counts as such a position because its line enters the step from the side; a later position outside the step cannot vacate an introduced commit. Merges additionally require a recorded managed-sync produced head, membership inside a landed leaf's own history, parent-line origin, or the shape of a pull-request merge that published one recorded landing. Older sync entries without produced-head metadata preserve their explicit compatibility admission. Every foreign commit is named with the remedy to move the change into a leaf rather than leaving it on the master line.

A merge between two leaf landings is admitted by the publication rule rather than by this proof's own reading: `_landing_workflow` (in `series_merge_admission.py`) reads the repository's landing workflow, for a series from the memory work branch tip, and `_publication_merge_admitted` asks `publication_admission.publication_merge_admitted` about the one merge. Under `local` that rule admits nothing; under `pull-request` it admits only the merge with ordered parents `(B, H)` and tree `H`, where `B` and `H` come from the leaf's recorded integration authority. Separately, `_published_landing` admits a pull-request merge by its shape alone, with no workflow or authority record: exactly two parents, the second the landed commit `H` of a leaf in the exact landing chain, the first an ancestor of `H`, and the merge's tree equal to `H`'s tree, the leaf being found from the merge's own second parent. `_publication_merge_admits` admits a step whose end is such a merge when the step starts at `H`, or at the merge's first parent when that is the published leaf's recorded base, and `_require_admitted_merges` does not count it as a foreign merge. A merge with content of its own, a second parent that is not a recorded landing, or an octopus merge falls through to the refusals. The wrappers convert the shared module's failures into this proof's own refusals, so a workflow that cannot be read or names no implemented value refuses as `atomic-series-landing-workflow-invalid`, and a merge whose trees cannot be read refuses as `atomic-series-leaf-chain-invalid`; neither falls back to `local` and neither passes as a non-member.

Final, checkpoint and recorded master landings invoke this proof over their own exact code/memory endpoints. Checkpoint and recorded routes omit unlanded leaves; an empty landed population may hold only recorded bases and reconciled parent history, never a free master workbench. Recorded landing does not replace its endpoints with mutable branch tips.

Both checkpoint capture and final memory recording use `series_memory_closeout`: re-read the exact code work ref, capture the actual memory work ref, and prove its recorded-base ancestry. They do not select an output from cached rows or require a fixed-point table. A code tip with no corresponding memory trailer can therefore still be captured without inventing attribution.

Final closeout and integration require the master complete. The checkpoint route deliberately does not, and instead refuses an already-completed master, requires an explicit captured `expected` pair, reloads the contract, and revalidates live tips before publication. It records no completed-task claim and reclaims nothing.

### Conventions

Closeout records existing refs rather than committing an ambient series workbench. Substantive dirty checkouts still refuse; memory.md alone is excluded. Checkpoint publication, stop-only pause, and finalization are distinct operations.

### Invariants And Boundaries

- Canonical task membership and exact repository/ref identity remain mandatory.
- A leaf that landed is always part of the chain proof, whatever its row says; an `abandoned` row never needs an enclosure or a landing.
- Order nonempty pairs only; empty pairs need an origin/sync/ordered pair (every pair a sync entry records, a repository-default sync's source pair included). Duplicate nonempty pairs refuse.
- Cache rows, ordering, and fixed-point projection are never series completion or checkpoint gates.
- No agent-owned ledger-only commit is needed to record a reconciled code tip.
- The checkpoint's expected candidate is required and is re-read before publication.
- A spine step may add only a recorded official position, or a line that a recorded position lying inside that step reaches; a position descending from the step admits nothing. The one other addition is a pull-request merge that publishes one recorded landing, admitted by exact shape.
- Preview and apply consume the same final-completion predicate.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source rather than an invented external reference.

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
