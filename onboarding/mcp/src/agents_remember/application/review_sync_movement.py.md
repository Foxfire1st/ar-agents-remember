# mcp/src/agents_remember/application/review_sync_movement.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Render managed-sync measurements of one retained tree comparison on a live leaf review. This is exact code/memory candidate currentness, not an intent verdict.

## Code Commentary

### Logic

`_measured` selects through `select_review_comparison` and reads that comparison's rebinding. No comparison or no measurement yields no movement; an unreadable selection, unreadable record or record naming another comparison is unavailable. `_project` maps recorded `current`, `moved` and `unmeasured` verdicts to `current`, `stale` and `not-measured`, preserving the exact moved code and memory tree identities.

### Invariants And Boundaries

Only a rebinding equal to the retained tree comparison supplies measurement. Missing memory proof is not agreement; a historical dataset generation cannot supply an exact memory tree. The read changes no worktree, review verdict or transaction authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole content is the statement that no
entries are configured — so there is no external or domain documentation source to consult, and no
documentation row is recorded here. Every statement on this card is grounded in the repository's own
source, docstrings and cases, and the paragraphs above are backed by the table below.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstrings and functions, in the owners it
consumes, and in the cases that drive the shipped review read. The three details a reader should carry:
**the state is the record's verdict, never a re-derivation from the two channel matches** (the G1 defect);
**`unavailable` is a third fact, not a flavour of absence or of measurement**; and **only a `stale`
movement is folded into the staleness the review publishes**, while an absence stays visible beside it.

- **The module's own statement of the requirement, the read-half gap it closes, and the "measures, owns no verdict" boundary.** [1]
- The published surface: exactly the two operations, and the routing that keeps the R17 fold callable beside the movement read. [2]
- The two channels a moved identity can belong to, and the `channel:identity` spelling. [3]
- **The verdict-to-state mapping stated as a table, and the comment that records why a two-way channel reading would promote `unmeasured` to agreement (G1).** [4]
- The remedy stated once: the successor generation the record itself names, not an action this module performs. [5]
- **The never-raising read: no leaf contract, or any store read error, answers `None` so the live review read cannot fail on a measurement.** [6]
- **The three outcomes and the middle one's own reason for existing — an unusable record is neither an absence nor a measurement.** [7]
- The `unavailable` value: its own state, `record_readable=False`, the reason, and the absence sentence. [8]
- The reviewed dataset identity read off the generation's own after side, or `None` when it retained none. [9]
- **The projection: the state taken from the record's verdict, moved identities named only on a moving channel, resolved identities only where one moved.** [10]
- **The absence reason built from the record's own values, including the location's own state and sentence.** [11]
- **One sentence per state, with the agreement sentence reachable only from `current`.** [12]
- The agreement clause that names only the channels actually compared and matched. [13]
- **The fold: a `stale` movement outranks the reader's carried identity, and the previous input is always one somebody held.** [14]

- Selection of the exact retained tree comparison, with explicit unavailable and historical-limit states. [15]

- **The record read as a state rather than an exception, with its three read states.** [16]
- **The check that a record describes *this* generation, which is what makes a foreign record `unavailable` instead of a measurement.** [17]
- The record's own three verdicts, and the seven channel matches the projection reads for identity naming only. [18]
- The sealed manifest this module reads and never rewrites, its knowledge sides, and the binding each side reports. [19]
- The resolution whose `contract` decides whether a generation can be resolved at all. [20]
- **The movement model whose validator the projection must satisfy, and the clause that ties `record_readable` to `unavailable`.** [21]
- **The live read that consumes both operations and folds the movement into the staleness it publishes.** [22]
- The payload field the movement is published on, beside the staleness it is folded into. [23]
- **The reopen channel reading the same durable record for itself, with the same location-then-generation order.** [24]
- The sync tool's projection point, where the write half is attached after the Git work has finished. [25]

- The live review labels the exact memory input a sync moved. [26]


- Unreadable or forged rebinding is unavailable and never current. [28]


- Contradictory sync-movement fields are refused. [30]


### Cross-Repo References

No cross-repository behavior is implemented in this module. It resolves a comparison generation under the
task root its worktree contract names, reads the durable rebinding record from the same task root's reports
area, and reads a dataset identity the leaf's own sealed manifest retained; every one of those is inside the
same repository and coordination-root boundary, and the relocation boundary that follows from a recorded
absolute task root is the one ICR-R12/R13 own for the generation record and ICR-R21 owns for the receipt.
No cross-repo reference row is recorded here because no cited range proves a repository or external-system
boundary.
