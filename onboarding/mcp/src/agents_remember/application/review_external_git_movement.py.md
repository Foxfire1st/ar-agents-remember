# mcp/src/agents_remember/application/review_external_git_movement.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Measure raw Git ancestry against the retained review tree record and publish the existing support matrix for recovery. The read mutates no checkout and records no comparison.

## Code Commentary

### Logic

The retained comparison names exact code/memory bases and any recorded candidate commits. Channels distinguish unchanged tips, ordinary advances, replaced history, switched branches and unreadable inputs. An uncommitted candidate has a tree pin without an observed work-branch HEAD; that channel is not measured and a current checkout supplies no historical proof.

The single support matrix supplies rendered documentation and recovery actions. Unsupported raw transitions remain unsupported; each compared and unread channel is named.

### Invariants And Boundaries

Source identities never become fabricated generation UUIDs. Corrupt content and an absent boundary remain distinct. Missing proof is neither current nor measured movement. The reading neither clears intent nor repairs transaction authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so there is no external or domain
documentation source to consult and no documentation row is recorded here. The one documentation
artifact this leaf does touch — `docs/reference/worktrees-c09.md` — is not an external source: it is a
repository file whose new `## Raw Git Identity Boundary` section is *generated from* this module's
matrix, and the assertion that binds the two is filed under Repo-Internal References.

### Repo-Internal References

Every claim on this card is checkable in the module's own declarations, in the owners whose reads it
composes, and in the cases that drive them. The three details a reader should carry: **the matrix is the
authority on which transitions are supported, and three of the packet's four named transitions are
recorded as unsupported rather than implied supported**; **`unchanged` exists so the control state never
names an event that did not happen**; and **every entry point answers with a state, never with an
exception, because a measurement that could not be taken must not fail the read that needed it.**

- **The module's own statement of what is measured, what is not claimed, and that no ancestry check identifies a pick or a revert.** [1]
- The owners this module composes, and the three guarded Git reads it borrows. [2]
- The published surface: the matrix, its row type, the three entry points, the renderer and the lookup. [3]
- The four states this module may report, declared once as the read surface's own vocabulary. [4]
- **The recovery a generation that cannot be read names, kept apart from the successor generation a movement names.** [5]
- The recovery a boundary names when nothing could be compared at all. [6]
- **The fold that derives every recovery sentence from the matrix rows rather than restating a verdict.** [7]
- The three declared channels, each named by the thing that moved rather than by the command that moved it. [8]
- One matrix row: the transition, its measured Git signature, the state it renders in, whether it is reconciled, and the step a person takes. [9]
- **The support matrix itself — six rows, one per shape, with `rebase` the only named transition an ancestry check can mark `stale`.** [10]
- The by-name lookup derived from the matrix, so a row added above is reachable below with no second list. [11]
- **The named lookup that refuses an unknown transition instead of answering with a default.** [12]
- **The unsupported list derived from the matrix, which is what a report repeats where the reader is.** [13]
- The Markdown renderer the documentation is asserted against, so the document is generated rather than transcribed. [14]
- One channel's measurement, and the shape measured for it. [15]
- A branch tip read from a repository, or the reason there is none to read. [16]
- **The review read's entry point, whose `None` answers are all facts rather than failures, and whose unreadable generation is `unavailable` with the selection's own detail.** [17]
- **The absence value: the cause in the words of the arm that established it, so the read and the published block share one branch.** [18]
- **The declaration half of the measurement, where a non-leaf contract and a contract with no work branch are two different causes with two different sentences.** [19]
- **The store half of the measurement, where an unusable generation is `unavailable` and a leaf that published nothing carries the store's own detail.** [20]
- **The contract-only half the closeout and integration owners call, so one implementation serves every caller.** [21]
- **The closeout/integration statement that never refuses: a failed result is returned untouched and every absence becomes a typed block.** [22]
- **The typed absence that repeats the matrix's unsupported transitions whether or not the boundary measured.** [23]
- **The state an unusable generation earns, with no generation identity claimed.** [24]
- **The state composition — `stale` over `current` over `not-measured`, with `current` requiring every channel compared.** [25]
- The three declared channels turned into findings, in fixed order. [26]
- **The one ancestry decision: `current` / `advanced` / `replaced` / `unavailable`, where `advanced` is a measurement of its own.** [27]
- The failure state an unreadable channel or repository earns. [28]
- The reads that can fail, each keeping its failure as a state rather than raising. [29]
- The ancestry read that answers whether a recorded identity is still in a branch's history. [30]
- The shape measured for one finding, never the command guessed. [31]
- The replaced identity spelled `channel:identity` for the value no longer in place. [32]
- **The reason an absence carries, naming each unreadable channel with its own detail.** [33]
- **One sentence per state, with no state borrowing another's clause.** [34]
- **The clause stating what an absence did compare, false only when nothing was compared.** [35]
- **The agreement sentence, whose `unchanged` clause never describes an advance.** [36]
- The movement sentence: the replaced channels first, then the channels that still stood. [37]
- The replacement spelled from the values the check read rather than from a diagnosis. [38]
- **The value this module publishes, its four-state union and the validator that refuses every false shape.** [39]
- **The transition vocabulary, including `unchanged` as the measured absence of a transition.** [40]
- **The review read that calls this owner and carries the value on the payload.** [41]
- The task-context review boundary, which takes the same measurement and refuses nothing on it. [42]
- **The fold that lets an external `stale` outrank a carried comparison identity and a recorded managed-sync rebinding.** [43]
- **The closeout preview, closeout apply and integration call sites that attach the statement.** [44]
- The integration result block that carries the same statement. [45]
- **The documented matrix, asserted to be the rendered production table rather than a transcription.** [46]

- Uncommitted records invent no observed HEAD, and history replacement retains source identity without fabricated UUIDs. [47]


- The documented matrix comes from the measured-operation table. [48]


- Contradictory boundary measurements are refused. [49]


- Untouched, advanced and rewritten history have distinct measured answers. [50]


### Cross-Repo References

No cross-repository behavior is implemented in this module. Every repository it touches is a checkout
this same repository's own contract resolved — the code worktree, the declared source branch and the
memory work branch all belong to the leaf whose enclosure contract was passed in — and the generation it
reads lives under the task root the same contract names. The three reads it performs are local Git
ancestry questions asked through `worktrees/modules/git.py`, and no remote, credential, network or
external system is involved. No cross-repo reference row is recorded here because no cited range proves
a repository or external-system boundary.
