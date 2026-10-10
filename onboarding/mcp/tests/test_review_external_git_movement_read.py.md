# mcp/tests/test_review_external_git_movement_read.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Raw Git movement is measured from retained commit evidence, with absent work-head proof kept unmeasured.

## Code Commentary

### Logic

An uncommitted candidate is a tree, not an observed branch head: the report remains not-measured, has no transition and fabricates no generation UUID. The live production read carries that measurement; historical comparisons carry no live movement. [5]

Commit-bound cases distinguish untouched, advanced and rewritten branches; source-history replacement, branch switch and unreadable channels retain distinct states. Validator forgeries use the real published value. [6] [7] [8] [14]

The shared TreeReceiptFixture constructs the enclosure and its exact comparison rather than the removed ReviewSyncFixture. [2]

### Invariants And Boundaries

- A tree cannot stand in for observed commit proof.
- Unavailable is neither movement nor agreement.

### Invariants And Boundaries

- **No prebuilt payload and no injected resolution.** Every case reaches the boundary through a real Git
  operation in a real enclosure and then reads the shipped entry point; a case that asserted a
  hand-built payload would prove nothing about the operation.
- **The documented matrix and the published matrix are one table.** `render_git_transition_support()`'s
  output must be a substring of `docs/reference/worktrees-c09.md`, so the document is generated from the
  production table rather than transcribed beside it.

### Todos

None recorded.

## Evidence

### Docs References



### Repo-Internal References

- Current shared enclosure fixture. [2]


- Uncommitted tree supplies no observed work-head proof. [5]


- Source replacement without fabricated UUID. [6]


- Leaving the declared branch is a switch. [7]


- Commit-bound ancestry states remain distinct. [8]


- Model rejects state contradictions. [14]


- Current managed-sync sibling cases. [25]

Every claim on this card is checkable in the module's own cases, in the fixtures it borrows from its
siblings, and in the manifests that govern its population. The three details a reader should carry:
**every case drives real Git and then reads a shipped entry point**; **the states that look similar each
have their own case**; and **the documented matrix is asserted to be the published one**, so the two
cannot drift apart silently.

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so no documentation row is recorded
here. The one document these cases read is a repository file rather than an external source:
`docs/reference/worktrees-c09.md`, whose `## Raw Git Identity Boundary` section the matrix case asserts
against, and that assertion is filed under Repo-Internal References.

- **The sibling fixture this module shares rather than rebuilds.** [26]
- **The lane registration that makes these cases part of the governed `integration` population.** [27]
- **A lifecycle consumer row that names this module, so the artifact census still counts it.** [28]
- **The documented section the matrix case asserts against, generated from the production table.** [29]

### Cross-Repo References

No cross-repository contract is established by this file.

No cross-repository behavior is implemented or exercised in this module. Every repository it drives is a
temporary enclosure this same repository's own fixture created under a temporary directory, and every
operation it performs is a local Git subprocess inside that enclosure. No remote, credential, network or
external system is involved, and no cited range proves a repository or external-system boundary, so no
cross-repo reference row is recorded here.
