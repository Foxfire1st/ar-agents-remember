# mcp/src/agents_remember/application/review_sync_movement.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The read half of ICR-R22@v1's obligation: what this leaf's own managed syncs measured against the
comparison generation the leaf published, projected into the review's measured-currentness vocabulary.**
The requirement's Required Behavior is that a completed sync which carried the official line
**invalidates** the moved review inputs and binds the resolved pair, and its own non-conforming example is
the state where the old review stays current while its datasets lag the merged memory line. A durable
record that only the sync payload and the reopen channel read leaves that state standing on the surface a
reviewing agent is actually looking at, so this module resolves the measurement and reports it where the
review is read.

**It measures; it owns no verdict of its own.** The measurement is the durable rebinding record
(`application/review_sync_rebinding.py`), and the record is accepted here only when
`rebinding_names_the_generation` proves it describes the very generation this read selected. Nothing in
this module composes a comparison, decides a verdict, writes anything, or grants clearance: the remedy it
names is the successor generation the record already names.

Three outcomes, not two — and they are three facts rather than two:

| Outcome | Operation | What it answers |
| --- | --- | --- |
| `None` | `review_sync_movement` (`:87-105`), `_measured` (`:108-135`) | nothing has measured this generation: no leaf contract, no published generation, no record written for it, or any read error along the way |
| `unavailable` | `_unavailable` (`:138-155`) | a record exists for the generation and cannot be used — its bytes are not a readable record, or it is a valid record that names another generation |
| the measured movement | `_project` (`:165-213`) | the state **taken from the record's own verdict** (`current` / `stale` / `not-measured`), the moved identities, the resolved identities on the channel that moved, and one sentence |

## Code Commentary

### Logic

**Nothing here can fail a response, and every unmeasurable case is an answer.** `review_sync_movement`
(`:87-105`) returns `None` when the resolution carries no leaf contract — `contract is None or contract.kind
!= "leaf"` (`:99-101`) — and wraps the whole measurement in a `try` whose `except` names the four things a
store read can raise, `KnowledgeStorageError`, `OSError`, `RuntimeError` and `ValueError` (`:102-105`),
because the live review read must never fail because a *measurement* was unavailable. Its docstring states
the cases as facts rather than failures: no enclosure contract to resolve a generation under, no published
generation, no recorded rebinding for it, a rebinding that does not describe it, and any read error along
the way (`:90-97`).

**Three outcomes, and the middle one may not be collapsed into either neighbour.** `_measured`
(`:108-135`) selects the generation through `select_review_generation`, reads the selected ref's sealed
manifest, reads the rebinding record back for that generation, and then separates the cases: `None` when
the read says `not-recorded` — "nothing has measured this" (`:127-128`) — `unavailable` when the bytes are
unreadable (`:123-124`) or when a record is present and does not describe this generation (`:126-134`),
and otherwise the measured movement. Its own docstring records why the middle case is its own answer:
collapsing it "would either claim a measurement nobody made or deny one that exists and is broken"
(`:110-115`).

**The state is the record's own verdict, never a two-way reading of the channel matches.**
`_MOVEMENT_STATES` (`:70-79`) maps the record's three verdicts onto this vocabulary's measured states —
`current`→`current`, `moved`→`stale`, `unmeasured`→`not-measured` — and `_project` (`:165-213`) takes
`state = _MOVEMENT_STATES[record.state]` (`:180`). The comment above the table records the defect it
closes: the mapping exists as a table "rather than two comparisons on the channel matches because the
verdict IS the state", and reading "did any channel differ" would "promote the record's own `unmeasured` to
agreement" (`:70-74`). That was round 3's blocking finding **G1**, where deriving the state from the
matches silently rendered an uncompared dataset as agreement; `_project`'s own docstring restates the rule
and the reason (`:168-175`).

**A resolved identity is named exactly on the channel that moved.** In `_project`, `code_moved` and
`knowledge_moved` are read from the record's own channel matches (`:178-179`) and are used only for the
`moved_identities` tuple (`:181-188`) and the three `resolved_*` fields (`:203-211`). A channel that still
matches, was never compared, or could not be read carries `None`, because inventing a value for it is "the
fabricated identity this vocabulary refuses" (`:190-192`); the knowledge digest is additionally guarded by
`record.resolved_knowledge.dataset is not None` (`:207-211`). The moved identity itself is spelled
`channel:identity` from the two channel constants (`:64-68`), so a reader gets both the input that moved
and the exact value the review recorded for it.

**The absence states carry the record's own words, and re-diagnose nothing.** `_unmeasured_reason`
(`:216-234`) composes the reason from values the record already holds: when the generation's after side is
not `retained`, it says which state the generation recorded for its knowledge operand (`:224-229`);
otherwise it names the channel's own match, the declared publication location's own state and that
location's own sentence (`:230-234`), because the read route already said which of "no publication" and
"something unreadable" it found.

**One sentence per state, and the agreement sentence is reachable only from `current`.** `_statement`
(`:237-281`) branches on the state: `not-measured` publishes the generation, the reason, and the clause
that only the compared part is reported as measured (`:255-260`); `current` publishes the agreement clause
(`:261-265`); `stale` names the candidate tree the review captured against the tree the leaf now holds and
the dataset the review compared against the declared publication location, then appends the one
supersession sentence (`:266-281`). `_measured_clause` (`:284-306`) is careful in the same direction: it
always states the reviewed candidate tree, and then either reports the knowledge operand's non-retained
state or — only on `matches-reviewed-input` (`:301`) — states the dataset agreement, so a generation that
retained no knowledge operand "has no dataset to speak of" and the clause says exactly that instead of
borrowing an agreement about a comparison nobody made (`:286-289`).

**The fold: a measured movement outranks the reader's carried identity.**
`review_staleness_with_sync_movement` (`:309-334`) returns the reader's `ReviewStaleness` untouched unless
the movement's `binding_state` is `stale` (`:326-327`); otherwise it publishes `stale` with the movement's
own statement and moved identities, and the previous input is `carried or movement.reviewed_binding_digest`
(`:328-333`) — a real identity in both cases: the identity the reader carried when they carried a
mismatching one, and otherwise the comparison identity the reviewed generation bound, "never an identity
nobody held" (`:321-323`). Submission follows automatically because the payload's constructor refuses a
`stale` comparison offered for submission (`:317-319`). A movement that measured agreement (`current`) and
a movement that reports an absence (`not-measured`) both change nothing here: the absence is carried by the
movement field beside the staleness, not by a claim inside it.

**The live read is the consumer, and the reopen channel reads the same record independently.**
`application/knowledge_review.py` imports both names (`:143-146`); `compose_review` (`:357-557`) measures
the movement, folds it through this module's wrapper beside the R17 rule, and publishes the value on the
payload's own field (`:470-478`, `:534-537`). The field is `sync_movement` on
`models/knowledge/review.py:1019-1026`. The reopen owner reads the rebinding for itself as its own channel,
with the same "read the location, then check it against the generation" order
(`application/review_comparison_reopen.py:351-360`, `:367-392`), and the sync-side producer that writes the
record is reached from the sync tool (`application/worktree_tools.py:353-375`).

### Conventions

`__all__` (`:59-62`) publishes exactly the two operations. This module defines no dataclass of its own:
the value it returns is the models module's `ReviewSyncMovement`, and its input is the resolution owner's
`ReviewCandidateResolution`. The two channel names are spelled once as `_CODE_CHANNEL` and
`_KNOWLEDGE_CHANNEL` (`:64-68`) and a moved identity is written `channel:identity`, which the comment ties
to R15's `moved_identities` vocabulary in this review's own spelling. The remedy is stated once as
`_SUPERSESSION` (`:81-84`) and restated into every sentence rather than re-derived per branch: it is the
successor-generation route the rebinding record itself names. `_MOVEMENT_STATES` is a `Mapping` (`:34`,
`:75`) used as a dispatch table rather than an if/elif ladder, which is this repository's own complexity
guidance applied. Private helpers are `_`-prefixed and each carries one job — `_measured` (`:108-135`),
`_unavailable` (`:138-155`), `_reviewed_knowledge` (`:158-162`), `_project` (`:165-213`),
`_unmeasured_reason` (`:216-234`), `_statement` (`:237-281`), `_measured_clause` (`:284-306`). Every route
it needs is imported from its owner (`:36-57`) — `read_manifest` and `COMPARISON_MANIFEST_NAME` from the
generation owner, `select_review_generation` from the final-output receipt owner, `read_review_sync_rebinding`
and `rebinding_names_the_generation` from the rebinding owner, `KnowledgeStorageError` from the refusals
module, `WorktreeContract` from the worktree contract module — and none is re-implemented.

### Invariants And Boundaries

- **A read that cannot measure says so by omission, not by a false claim.** `None` is the answer for every
  unmeasurable case, and the caught exception tuple is exactly what a store read can raise; the live review
  read is not the sync, so nothing here can fail a response.
- **The verdict is carried, never derived.** The three-way dispatch table is the only mapping from record
  verdict to published state; the two channel matches decide only which identities are *named* as moved.
  Deriving the state from the matches is the G1 defect this leaf fixed.
- **A record naming another generation is no measurement of this one.** `rebinding_names_the_generation`
  (called at `:125`) compares the record's superseded generation id, index and binding digest, both
  reviewed code trees and the reviewed knowledge state and digest against the sealed manifest, so a
  valid-but-foreign record becomes `unavailable` with a reason naming the generation it does not describe
  (`:129-134`) — never `None`, because something *is* recorded at that location.
- **`unavailable` is a third outcome and neither neighbour.** It carries `record_readable=False` and a
  non-empty `reason`, and the movement validator in the models module requires exactly that: an absence
  state without a reason is refused, and a measurement carrying one is refused as well.
- **Only `stale` moves the fold.** Agreement and absence leave the reader's own staleness exactly as they
  found it, so a `not-measured` movement never renders as a movement and never as an agreement: it is a
  value beside the staleness field, not a claim inside it.
- **The previous input is always one somebody held.** `carried or movement.reviewed_binding_digest`; the
  fallback is the generation's own bound comparison identity, never a synthesized one.
- **No write, no clearance, no comparison, no supersession.** The module reads a task root and a leaf id and
  returns a value; performing the successor publication is `freeze_review_comparison`'s act.
- **Boundary: `record_readable` is `False` for both `unavailable` sub-cases**, so that one field cannot
  separate an unreadable artifact from a valid record that names another generation. The sub-fact is
  carried by `reason`, and the two reasons are distinguishable; the field-level fix — renaming it, or
  narrowing its documented meaning — needs a production-byte change in
  `models/knowledge/review_staleness.py` and is **held for the master's ruling**, which the case that pins
  the behaviour states in place rather than working around (`mcp/tests/test_review_sync_movement_read.py:169-226`,
  the hold recorded at `:219-225`).
- **Boundary: this module is the read half only.** The write half, the record's own vocabulary and the
  sync-tool projection live in `application/review_sync_rebinding.py` and
  `models/knowledge/review_sync_rebinding.py`; this module consumes them and owns neither their shape nor
  their durability.

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
- **The generation selection this module reads through, with its four states and its `ref`.** [15]
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
- **The case that renders a recorded movement through the shipped read, including absence, measured agreement and movement.** [26]
- **The G1 case: an uncompared knowledge channel renders as `not-measured` with the record's own reason, never as agreement.** [27]
- **Both unusable-record sub-cases render `unavailable`, with the two reasons distinguishable, and the `record_readable` hold recorded in place.** [28]
- The success conjunct that keeps a failed sync payload from being measured as a resolution. [29]
- The four movement-validator clauses pinned one forgery each, with the real published movement as the accepted control. [30]
- The shared read assertion every render case routes through. [31]

### Cross-Repo References

No cross-repository behavior is implemented in this module. It resolves a comparison generation under the
task root its worktree contract names, reads the durable rebinding record from the same task root's reports
area, and reads a dataset identity the leaf's own sealed manifest retained; every one of those is inside the
same repository and coordination-root boundary, and the relocation boundary that follows from a recorded
absolute task root is the one ICR-R12/R13 own for the generation record and ICR-R21 owns for the receipt.
No cross-repo reference row is recorded here because no cited range proves a repository or external-system
boundary.
