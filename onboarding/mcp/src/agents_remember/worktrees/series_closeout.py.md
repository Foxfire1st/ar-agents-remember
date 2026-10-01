# mcp/src/agents_remember/worktrees/series_closeout.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Prove completed atomic-master candidates and capture exact series refs for final closeout or a non-final checkpoint.

## Code Commentary

### Logic

The final route resolves canonical master/leaf task membership and requires one exact enclosure per leaf. It verifies each leaf's repository, source branch, base-to-integrated edges, and recorded code/memory output identity, then orders the chain by the landings' own ancestry. It does not order from bases that a later sync legitimately advanced.

Without a recorded sync, the oldest leaf starts at the exact series base. With sync history, the origin is proved against the first sync's old bases and each leaf must remain on that line. The series spine must contain every landing and only admitted inter-leaf/source transitions. Memory-side history inspection excludes root memory.md content; the removed special ledger-recording commit exception is not an authority rule.

Every step of that spine is proved by **enumerating** what it adds — `rev-list --no-merges --full-history <later> --not <earlier>`, the memory side additionally excluding `.` with `:(top,exclude)memory.md` — and admitting a commit only when it is an official position one of the chain's own contracts synced with, or when a recorded position that lies **inside that step** reaches it. The second clause is what stops the rule refusing the shape it names: when a step's endpoint is the merge of the previous landing with a synced position, the whole step *is* that position's own line. Measured on the 260915-KS master, the step is L5's landing `7db50f8f` to L6's recorded base `8dfc11b8`; `8dfc11b8` is the merge of `7db50f8f` with the synced super-line position `8dd62345`, every commit the step adds is reachable from `8dd62345`, and only the position itself used to be admitted (register row D-60). *Inside* means strictly after the step's start and at or before its end, so a position that merely descends **from** the step stays outside it and still cannot vacate a commit the step genuinely introduced. The admission stays bounded to the positions the call was given, and the step is never *subtracted* from the revision walk: removing a position's whole ancestry is what once made the check pass vacuously.

Both checkpoint capture and final memory recording use `series_memory_closeout`: re-read the exact code work ref, capture the actual memory work ref, and prove its recorded-base ancestry. They do not select an output from cached rows or require a fixed-point table. A code tip with no corresponding memory trailer can therefore still be captured without inventing attribution.

Final closeout and integration require the master complete. The checkpoint route deliberately does not, and instead refuses an already-completed master, requires an explicit captured `expected` pair, reloads the contract, and revalidates live tips before publication. It records no completed-task claim and reclaims nothing.

### Conventions

Closeout records existing refs rather than committing an ambient series workbench. Substantive dirty checkouts still refuse; memory.md alone is excluded. Checkpoint publication, stop-only pause, and finalization are distinct operations.

### Invariants And Boundaries

- Canonical task membership and exact repository/ref identity remain mandatory.
- Leaf order comes from real code and memory ancestry, including after source reconciliation.
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
- Checkpoint capture and publication revalidate an explicit two-output candidate. [2]
- Leaf membership, output identity, and ordering remain exact. [3]
- Recorded origins and admitted substantive history preserve reconciled series proof. [4]
- Series cleanliness and actual memory-ref capture exclude cache authority. [5]
- Recorded origins and admitted substantive history preserve reconciled series proof. [6]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
