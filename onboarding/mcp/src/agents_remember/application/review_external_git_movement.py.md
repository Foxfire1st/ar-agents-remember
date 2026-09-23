# mcp/src/agents_remember/application/review_external_git_movement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_external_git_movement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T20:10:00+02:00 |
| lastVerifiedCommitHash | `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499` |
| lastVerifiedCommitDate | 2026-09-23T22:41:36+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The boundary measurement for identity movement caused *outside* managed sync, and the support matrix
that says in words which recovery routes exist (ICR-R23@v1).** `worktree_sync` is the one route that
moves a leaf's declared identities *under measurement*: it merges the official line into the work
branch, re-captures the candidate and writes a rebinding record naming what it moved (ICR-R22@v1,
`application/review_sync_movement.py`). Everything else that can move those identities is ordinary Git —
`git rebase`, `git cherry-pick`, `git revert`, `git checkout`, `git switch` — and none of it leaves the
repository a record of having done so. A reader holding only "a comparison generation was frozen"
therefore cannot tell a rewritten branch from an untouched one, which is the packet's non-conforming
example: attribution that is old shown as current solely because its manifest and database file still
exist.

This module resolves the generation the leaf published — through the owner that already selects and
reads it — and asks the repository the three questions a Git history can answer about the identities
the sealed manifest declared:

| Channel | The question asked |
| --- | --- |
| `code-work-branch` | is the worktree still on the branch the contract declared, and is the recorded work-branch head still an ancestor of that branch's tip? |
| `declared-source-branch` | is the code-base commit the capture was taken from still an ancestor of the declared source branch? |
| `memory-work-branch` | is the memory work branch's recorded base still an ancestor of the memory work branch? |

**It measures; it decides nothing.** The module's own docstring states the boundary plainly: no verdict
about a comparison, no clearance, no refusal to work. It runs no Git command that writes, mutates no
checkout, and the reviewed generation keeps every byte it had — the packet's boundary example, an exact
historic generation staying inspectable while live recovery is pending.

## Code Commentary

### Logic

**`GIT_TRANSITION_SUPPORT` is the support matrix, and it is the authority rather than a summary of one.**
Each `GitTransitionSupport` row carries the transition name, the *measured Git signature*, the boundary
state it renders in, whether this system reconciles it at all, and the step a person takes instead
(`:123-142`). The table holds six rows (`:143-236`): `unchanged`, `ordinary-append`, `rebase`,
`cherry-pick`, `revert` and `branch-switch`. Two of them are the shape NOT moved and the shape moved
forward normally — both `state="current"`, both `reconciliation="supported"` — and the other four are
the packet's named transitions, of which exactly one (`rebase`) is distinguishable by an ancestry check
alone and is therefore `stale`, while `cherry-pick`, `revert` and `branch-switch` are each
`reconciliation="unsupported"` with the recovery named in the row.

**`unchanged` is a state, not a transition, and it is why the control case cannot lie.** A branch
standing exactly at its recorded head has no Git event to name; publishing `ordinary-append` for it
would assert an advance that did not happen. The vocabulary in
`models/knowledge/review_external_movement.py:74-81` carries `unchanged` for precisely that measured
absence, and the agreement sentence has a clause for it separately from the advance clause
(`_agreement_statement`, `:843-868`).

**The recovery text is derived from the matrix, never restated.** `_recovery_actions` (`:99-116`) folds
the rows' own `recovery_action` values, and `unsupported_transitions()` (`:261-274`) derives the
unsupported list from the same table, so a report cannot name a verdict the matrix contradicts.
`supported_recovery(transition)` (`:242-260`) refuses an unknown transition with a `KeyError` naming the
matrix as the authority instead of answering with a permissive default — a silent fallback here would be
the over-claim the matrix exists to prevent.

**Three entry points, chosen by which owner is asking.** `external_git_movement(resolved, contract=None)`
(`:328-348`) is the review read's entry: it returns `None` for "no boundary to measure" — a resolution
naming no enclosure, a record reopened from a closed leaf, a contract that is not a leaf or declares no
work branch, or a leaf that published nothing — because the live review read must never fail because a
*measurement* was unavailable. A generation that exists and cannot be used (unreadable bytes, or a tie
of two generations claiming one index) is deliberately **not** one of those cases: it is `unavailable`,
carrying the selection's own detail (`:337-339`), because "never reviewed" and "the review record is
corrupt" are different facts. `external_git_movement_for_contract(contract)` (`:407-420`) is the
contract-only half the closeout and integration owners call, so there is still one implementation of the
comparison. `external_git_movement_result_block(contract, payload)` (`:421-456`) attaches the
measurement to a closeout or integration result and **never refuses anything**: a failed operation is
returned untouched and every absence becomes a typed block, so no review obligation becomes a gate on
the Git transaction the statement describes.

**One measurement, and each absence cause named by the arm that established it.** `_measure_contract`
(`:363-383`) decides what the contract *declares* — a contract that is not a leaf enclosure and a leaf
that names no work branch are two different causes and each gets its own sentence — and hands off to
`_measure_generation` (`:384-406`), which decides what the generation store *holds*: an unusable
generation is `unavailable` with the selection's detail, and a leaf recorded as having published nothing
carries the store's own `no-generation` detail rather than a paraphrase. Both are returned as
`_BoundaryAbsence` (`:351-360`), a frozen value carrying `detail`. It exists so the review read, which
reports the absence as `None`, and the closeout/integration block, which *publishes* it, read the **same
branch of the same function** instead of each re-deriving the cause: one sentence covering every cause
would say that *something* applies without saying which.

**The state is composed, not chosen.** `_state` (`:549-565`) ranks `stale` above `current` above
`not-measured`, and `current` is reachable only when **every** declared channel was compared (`_report`,
`:496-527`). `_ancestry` (`:642-698`) is the single ancestry decision, answering
`current` / `advanced` / `replaced` / `unavailable` per channel. `advanced` is a measurement of its own —
the recorded identity is still an ancestor, so the branch moved forward without replacing it — which is
how a rebase is told apart from a cherry-pick of the same content.

**Every sentence is built from measured fields.** `_statement` (`:803-828`) dispatches one sentence per
state; `_compared_clause` (`:829-842`) states what an absence *did* compare, and returns the
nothing-was-compared clause only when that is true; `_agreement_statement` (`:843-868`) keeps the
`unchanged` clause apart from the advance clause; `_movement_statement` (`:869-882`) names the replaced
channels and then the channels that still stood; `_replacement_clause` (`:883-895`) spells the
replacement from the values the check read rather than from a diagnosis; and `_reason` (`:789-802`) names
each unreadable channel with its own reason, because restoring a checkout and restoring a repository are
different acts.

**Every read that can fail keeps its failure as a state.** `_tip` (`:720-728`), `_object_readable`
(`:729-737`), `_related` (`:738-746`) and `_text` (`:747-755`) sit behind `_BranchTip` (`:321-327`),
whose `commit` is optional and whose `detail` carries why there is none; `_unreadable` (`:699-719`) and
`_unavailable` (`:472-495`) turn that into the reported absence rather than an exception.

### Conventions

`__all__` (`:68-76`) publishes the matrix, its row type, the three entry points, the renderer and the
named lookup, in one alphabetical list. The module imports only owners that already exist (`:39-66`):
the resolution and generation owners for the sealed identities, `select_review_generation` and
`read_manifest` for the generation, `KnowledgeStorageError` for the store failure it reports as a state,
the new value vocabulary, and three guarded Git reads — `branch_commit`, `current_branch`, `is_ancestor`
— from `worktrees/modules/git.py`. It defines no Git invocation of its own and no write path.

The transition names are a `Literal` in the model module rather than free strings, and the lookup
`_SUPPORT_BY_TRANSITION` (`:237-241`) is derived from the table, so a row added to the matrix is
reachable by name with no second list to keep in step. The docstring (`:1-37`) records the measured
split, why the transitions an ancestry check cannot identify are reported as unsupported rather than
implied supported, and the two boundaries the packet names — no silent fallback and no invented
identity.

### Invariants And Boundaries

- **Measuring is not deciding.** The module publishes which declared identities no longer appear and
  which recovery exists; it never re-freezes, reconciles, deletes, checks out a branch or mutates a
  checkout, and the successor generation remains the freeze owner's act.
- **An unrecognized transition cannot reuse stale assessment as current.** `rebase` earns `stale`
  because the recorded head is provably no longer an ancestor; the transitions an ancestry check cannot
  distinguish are reported as `current` **with `reconciliation="unsupported"` beside them**, so a reader
  cannot conclude from the state alone that a pick or a revert was handled.
- **No unfavourable fact is promoted into a claim.** `not-measured` and `unavailable` never become
  `stale`: promoting an absence into a movement would report a movement nobody observed.
- **An absence always names its reason and carries no observed identity.** A channel that could not be
  read reports `unavailable` and carries no observed value at all rather than a favourable default
  (`_report`, `:496-527`), and the unreadable-generation state invents no generation identity
  (`_unavailable`, `:472-495`). The cause itself is established once, in `_measure_contract` /
  `_measure_generation`, and travels as `_BoundaryAbsence.detail` rather than being re-derived by the
  caller that publishes it.
- **The closeout statement never gates.** `external_git_movement_result_block` (`:421-456`) attaches a
  typed block to a successful result and returns a failed result untouched; the closeout door's own
  source-lineage checks remain the only checks on that transaction.
- **Boundary: the four named transitions are documented as three unsupported plus one stale.**
  `cherry-pick` and `revert` move the branch *forward*, so the recorded commit is still in history and
  no ancestry check identifies either — the module's own docstring says so — and that measurement
  belongs to the owners that already take it (the managed-sync rebinding on the sync route, the reopen
  channel on the read route). The matrix says exactly that rather than implying support by silence.
- **Boundary: `branch-switch` is reported as `not-measured`, not as a replacement.** The checkout left
  the declared branch, so the work-branch comparison cannot be taken at all; the state carries the
  sub-fact rather than claiming an identity was replaced, and this system never checks a branch out on a
  reader's behalf.
- **Boundary: the authoring boundary has no natural owner.** The packet names review/authoring/closeout;
  the review read, the closeout and the integration owners are wired here, and the authoring boundary is
  recorded as an absence rather than given a synthetic owner.

### Todos

None recorded.

## Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so there is no external or domain
documentation source to consult and no documentation row is recorded here. The one documentation
artifact this leaf does touch — `docs/reference/worktrees-c09.md` — is not an external source: it is a
repository file whose new `## Raw Git Identity Boundary` section is *generated from* this module's
matrix, and the assertion that binds the two is filed under Repo-Internal References.

## Repo-Internal References

Every claim on this card is checkable in the module's own declarations, in the owners whose reads it
composes, and in the cases that drive them. The three details a reader should carry: **the matrix is the
authority on which transitions are supported, and three of the packet's four named transitions are
recorded as unsupported rather than implied supported**; **`unchanged` exists so the control state never
names an event that did not happen**; and **every entry point answers with a state, never with an
exception, because a measurement that could not be taken must not fail the read that needed it.**

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what is measured, what is not claimed, and that no ancestry check identifies a pick or a revert.** | "It measures; it decides nothing." | mcp/src/agents_remember/application/review_external_git_movement.py:1-37 |
| The owners this module composes, and the three guarded Git reads it borrows. | `is_ancestor` | mcp/src/agents_remember/application/review_external_git_movement.py:39-66 |
| The published surface: the matrix, its row type, the three entry points, the renderer and the lookup. | `__all__` | mcp/src/agents_remember/application/review_external_git_movement.py:68-76 |
| The four states this module may report, declared once as the read surface's own vocabulary. | `_MovementState` | mcp/src/agents_remember/application/review_external_git_movement.py:78-78 |
| **The recovery a generation that cannot be read names, kept apart from the successor generation a movement names.** | `_GENERATION_UNREADABLE_RECOVERY` | mcp/src/agents_remember/application/review_external_git_movement.py:80-91 |
| The recovery a boundary names when nothing could be compared at all. | `_UNCOMPARED_RECOVERY` | mcp/src/agents_remember/application/review_external_git_movement.py:92-98 |
| **The fold that derives every recovery sentence from the matrix rows rather than restating a verdict.** | `_recovery_actions` | mcp/src/agents_remember/application/review_external_git_movement.py:99-116 |
| The three declared channels, each named by the thing that moved rather than by the command that moved it. | `_CODE_CHANNEL` | mcp/src/agents_remember/application/review_external_git_movement.py:117-119 |
| One matrix row: the transition, its measured Git signature, the state it renders in, whether it is reconciled, and the step a person takes. | `GitTransitionSupport` | mcp/src/agents_remember/application/review_external_git_movement.py:122-142 |
| **The support matrix itself — six rows, one per shape, with `rebase` the only named transition an ancestry check can mark `stale`.** | `GIT_TRANSITION_SUPPORT` | mcp/src/agents_remember/application/review_external_git_movement.py:143-236 |
| The by-name lookup derived from the matrix, so a row added above is reachable below with no second list. | `_SUPPORT_BY_TRANSITION` | mcp/src/agents_remember/application/review_external_git_movement.py:237-241 |
| **The named lookup that refuses an unknown transition instead of answering with a default.** | `supported_recovery` | mcp/src/agents_remember/application/review_external_git_movement.py:242-260 |
| **The unsupported list derived from the matrix, which is what a report repeats where the reader is.** | `unsupported_transitions` | mcp/src/agents_remember/application/review_external_git_movement.py:261-274 |
| The Markdown renderer the documentation is asserted against, so the document is generated rather than transcribed. | `render_git_transition_support` | mcp/src/agents_remember/application/review_external_git_movement.py:275-292 |
| One channel's measurement, and the shape measured for it. | `_Finding` | mcp/src/agents_remember/application/review_external_git_movement.py:300-319 |
| A branch tip read from a repository, or the reason there is none to read. | `_BranchTip` | mcp/src/agents_remember/application/review_external_git_movement.py:321-327 |
| **The review read's entry point, whose `None` answers are all facts rather than failures, and whose unreadable generation is `unavailable` with the selection's own detail.** | `external_git_movement` | mcp/src/agents_remember/application/review_external_git_movement.py:328-348 |
| **The absence value: the cause in the words of the arm that established it, so the read and the published block share one branch.** | `_BoundaryAbsence` | mcp/src/agents_remember/application/review_external_git_movement.py:351-360 |
| **The declaration half of the measurement, where a non-leaf contract and a contract with no work branch are two different causes with two different sentences.** | `_measure_contract` | mcp/src/agents_remember/application/review_external_git_movement.py:363-383 |
| **The store half of the measurement, where an unusable generation is `unavailable` and a leaf that published nothing carries the store's own detail.** | `_measure_generation` | mcp/src/agents_remember/application/review_external_git_movement.py:384-406 |
| **The contract-only half the closeout and integration owners call, so one implementation serves every caller.** | `external_git_movement_for_contract` | mcp/src/agents_remember/application/review_external_git_movement.py:407-420 |
| **The closeout/integration statement that never refuses: a failed result is returned untouched and every absence becomes a typed block.** | `external_git_movement_result_block` | mcp/src/agents_remember/application/review_external_git_movement.py:421-456 |
| **The typed absence that repeats the matrix's unsupported transitions whether or not the boundary measured.** | `_absence_block` | mcp/src/agents_remember/application/review_external_git_movement.py:457-471 |
| **The state an unusable generation earns, with no generation identity claimed.** | `_unavailable` | mcp/src/agents_remember/application/review_external_git_movement.py:472-495 |
| **The state composition — `stale` over `current` over `not-measured`, with `current` requiring every channel compared.** | `_report` | mcp/src/agents_remember/application/review_external_git_movement.py:496-527 |
| The three declared channels turned into findings, in fixed order. | `_findings` | mcp/src/agents_remember/application/review_external_git_movement.py:566-586 |
| **The one ancestry decision: `current` / `advanced` / `replaced` / `unavailable`, where `advanced` is a measurement of its own.** | `_ancestry` | mcp/src/agents_remember/application/review_external_git_movement.py:642-698 |
| The failure state an unreadable channel or repository earns. | `_unreadable` | mcp/src/agents_remember/application/review_external_git_movement.py:699-719 |
| The reads that can fail, each keeping its failure as a state rather than raising. | `_object_readable` | mcp/src/agents_remember/application/review_external_git_movement.py:729-737 |
| The ancestry read that answers whether a recorded identity is still in a branch's history. | `_related` | mcp/src/agents_remember/application/review_external_git_movement.py:738-746 |
| The shape measured for one finding, never the command guessed. | `_transition` | mcp/src/agents_remember/application/review_external_git_movement.py:765-782 |
| The replaced identity spelled `channel:identity` for the value no longer in place. | `_moved_identity` | mcp/src/agents_remember/application/review_external_git_movement.py:783-788 |
| **The reason an absence carries, naming each unreadable channel with its own detail.** | `_reason` | mcp/src/agents_remember/application/review_external_git_movement.py:789-802 |
| **One sentence per state, with no state borrowing another's clause.** | `_statement` | mcp/src/agents_remember/application/review_external_git_movement.py:803-828 |
| **The clause stating what an absence did compare, false only when nothing was compared.** | `_compared_clause` | mcp/src/agents_remember/application/review_external_git_movement.py:829-842 |
| **The agreement sentence, whose `unchanged` clause never describes an advance.** | `_agreement_statement` | mcp/src/agents_remember/application/review_external_git_movement.py:843-868 |
| The movement sentence: the replaced channels first, then the channels that still stood. | `_movement_statement` | mcp/src/agents_remember/application/review_external_git_movement.py:869-882 |
| The replacement spelled from the values the check read rather than from a diagnosis. | `_replacement_clause` | mcp/src/agents_remember/application/review_external_git_movement.py:883-895 |
| **The value this module publishes, its four-state union and the validator that refuses every false shape.** | `ExternalGitMovement` | mcp/src/agents_remember/models/knowledge/review_external_movement.py:101-205 |
| **The transition vocabulary, including `unchanged` as the measured absence of a transition.** | `ExternalGitTransition` | mcp/src/agents_remember/models/knowledge/review_external_movement.py:74-81 |
| **The review read that calls this owner and carries the value on the payload.** | `external_git_movement` | mcp/src/agents_remember/application/knowledge_review.py:371-611 |
| The task-context review boundary, which takes the same measurement and refuses nothing on it. | `external_git_movement` | mcp/src/agents_remember/application/review_task_context.py:93-191 |
| **The fold that lets an external `stale` outrank a carried comparison identity and a recorded managed-sync rebinding.** | `review_staleness_with_external_movement` | mcp/src/agents_remember/application/review_sync_movement.py:311-355 |
| **The closeout preview, closeout apply and integration call sites that attach the statement.** | `external_git_movement_result_block` | mcp/src/agents_remember/application/worktree_tools.py:461-461 |
| The integration result block that carries the same statement. | `external_git_movement_result_block` | mcp/src/agents_remember/application/worktree_tools.py:1012-1016 |
| **The documented matrix, asserted to be the rendered production table rather than a transcription.** | "Raw Git Identity Boundary" | docs/reference/worktrees-c09.md:113-148 |
| **The cases that drive real Git through the shipped entry points and pin the states apart.** | `RawGitIdentityBoundaryTests` | mcp/tests/test_review_external_git_movement_read.py:53-61 |
| The case that pins the documented matrix and the published matrix as one table, with unknown names refusing. | `test_the_documented_matrix_and_the_published_matrix_are_one_table` | mcp/tests/test_review_external_git_movement_read.py:499-559 |
| The case that pins the validator's five false shapes against the real published value. | `test_the_movement_validator_refuses_each_false_shape` | mcp/tests/test_review_external_git_movement_read.py:560-633 |
| The case that pins the control state as the value every untouched leaf publishes. | `test_the_unchanged_value_is_the_one_the_control_state_publishes` | mcp/tests/test_review_external_git_movement_read.py:634-655 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. Every repository it touches is a checkout
this same repository's own contract resolved — the code worktree, the declared source branch and the
memory work branch all belong to the leaf whose enclosure contract was passed in — and the generation it
reads lives under the task root the same contract names. The three reads it performs are local Git
ancestry questions asked through `worktrees/modules/git.py`, and no remote, credential, network or
external system is involved. No cross-repo reference row is recorded here because no cited range proves
a repository or external-system boundary.

## Update History
- 2026-09-23T20:10:00+02:00 — 260921-ICR-L23 curator (uncommitted change set on `ar/260921-icr-l23`, base `473ad8242bb4c22bdabed5d5253767350381eb3e`): created this one-to-one card for the module this leaf introduced as **the boundary measurement for identity movement caused outside managed sync**, the owner of the support matrix the packet's Required Behavior asks for. It records what a consumer has to act on: `GIT_TRANSITION_SUPPORT` is the authority on which of the four named transitions this system reconciles, and exactly one of them (`rebase`) is `stale` because an ancestry check can prove the branch was rewritten, while `cherry-pick`, `revert` and `branch-switch` are `reconciliation="unsupported"` with the recovery each row names — the state alone never licenses the conclusion that a pick or a revert was handled, and the module's own docstring records that no ancestry check identifies either. `unchanged` exists so the control state publishes the measured absence of a transition instead of naming an event that did not happen. `external_git_movement`'s `None` answers are all facts (no enclosure, a closed leaf's record, no declared work branch, no published generation, a non-leaf contract), while a generation that exists and cannot be used is `unavailable` carrying the selection's own detail; `external_git_movement_result_block` attaches the statement to closeout and integration results and never refuses. The measurement establishes each absence cause once — `_measure_contract` decides what the contract declares, `_measure_generation` what the store holds, and both report through `_BoundaryAbsence.detail` — so the read that reports the absence as `None` and the block that publishes it share one branch instead of each re-deriving the cause. Two boundaries are carried as boundaries and not as defects: the authoring boundary the packet names has no natural owner and is recorded as an absence rather than given a synthetic one, and `branch-switch` is reported as `not-measured` because the comparison genuinely cannot be taken, with `not-measured` and `unavailable` never promoted into `stale`. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name this leaf's recorded base `473ad8242bb4c22bdabed5d5253767350381eb3e` because every construct cited here exists only in this leaf's uncommitted working tree — the file itself is untracked at that commit — so no commit contains the content a stamp would claim to have verified; what was actually read is that working tree (base commit plus the leaf's working-tree delta, re-read after the leaf's fix round 2), and the governing overview is `mcp/src/agents_remember/application/overview.md`.
