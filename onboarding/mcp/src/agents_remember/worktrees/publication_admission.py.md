# mcp/src/agents_remember/worktrees/publication_admission.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Decide whether one Git merge *is* the publication of a leaf's landing, and hand out the pair that
decision is made against: the recorded position `B` and the integrated landing commit `H`, read from
the authority the integration itself recorded.

## Code Commentary

### The merge rule

`publication_merge_is_admitted` is the whole rule in one place. A merge is admitted when the
repository lands by pull request, when it has exactly two parents, when the second parent is the
integrated landing commit `H` of a leaf this proof already admits on this side, and when the merge's
own tree equals `H`'s tree. The first parent is then `B` by construction rather than by inspection:
the pair test `base == first and integrated == second` is what refuses a merge of the wrong pair, and
it is why a contract whose base cell differs from the recorded authority cannot be used to admit its
own merge. Anything else - a contributor's merge, a squash, a rebase-merge, a merge carrying content
of its own - returns False and falls through to the refusal the proof has always made. [1]

`publication_merge_admitted` reads the merge before judging it: `rev-list --parents` for the parents
and `rev-parse <commit>^{tree}` for both trees. A merge whose parents or trees cannot be read raises
`PublicationMergeUnreadable` rather than returning False, because a merge that could not be read is
refused as an input - it is never admitted, and never condemned either. [2]

### Where `B` and `H` come from

`leaf_authority_range` reads one leaf's own pair from its immutable integration authority: the live
journal through the canonical locator, which cross-checks contract, locator and manifest before
reading. A leaf whose enclosure is already archived has no live journal, so `_archived_authority_range`
takes the same authority from the terminal archive - locator inspection, the cleanup-contract
authority, and the archived `integrate-operation.json`, whose bytes the archive has already digest- and
size-validated, parsed by the operation model. [1]

A store refusal is swallowed here, not propagated: the live read is attempted, its refusal falls
through to the archive, and an archive that cannot answer leaves `None`. The function therefore
reports absence of admission, never the store's typed reason - that reason belongs to whoever can act
on it, and the caller still lands on its own refusal for a merge no admission explains.

### What a missing authority means

`publication_ranges` collects the pairs of the leaves the proof already admits. A leaf whose authority
cannot be read contributes nothing, which is the difference between "no authority" and "a merge no
admission explains": the first grants no new admission, the second is the caller's refusal to make.
No pair is invented to fill the gap and no second route re-reads the record.

### The workflow gate

`landing_workflow` reads the one value that governs the repository's code and memory pair from that
pair's memory settings. A series whose memory worktree is unknown, absent or still on markdown
settings lands locally: a missing key means `local`, and this proof never invents a workflow.
