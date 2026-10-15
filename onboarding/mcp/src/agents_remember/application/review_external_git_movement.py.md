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

### Invariants And Boundaries

- **Explicit unavailable findings are not themselves replacements.** They keep their reason and no observed tip. However `_related` converts an OSError/RuntimeError from `is_ancestor` to false, which `_ancestry` classifies as replaced/stale; this local failure fallback is not an implemented no-promotion guarantee.
- **An absence always names its reason and carries no observed identity.** A channel that could not be
  read reports `unavailable` and carries no observed value at all rather than a favourable default
  (`_report`, `:496-527`), and the unreadable-generation state invents no generation identity
  (`_unavailable`, `:472-495`). The cause itself is established once, in `_measure_contract` /
  `_measure_generation`, and travels as `_BoundaryAbsence.detail` rather than being re-derived by the
  caller that publishes it.
- **The closeout statement never gates.** `external_git_movement_result_block` (`:421-456`) attaches a
  typed block to a successful result and returns a failed result untouched; the transaction retains its existing closeout admission, approval, certification and source-lineage checks; this descriptive block adds none.
- **Boundary: all four named raw transitions are unsupported for reconciliation; rebase additionally reports stale.**
  `cherry-pick` and `revert` move the branch *forward*, so the recorded commit is still in history and
  no ancestry check identifies either. The matrix directs a successor tree comparison: managed-sync rebinding exists only after an actual carry/resolved pair, and the reopen channel measures comparison availability, not the pick or revert itself. The matrix says exactly that rather than implying support by silence.
- **Boundary: `branch-switch` is reported as `not-measured`, not as a replacement.** The checkout left
  the declared branch, so the work-branch comparison cannot be taken at all; the state carries the
  sub-fact rather than claiming an identity was replaced, and this system never checks a branch out on a
  reader's behalf.
- **Boundary: the authoring boundary has no natural owner.** The packet names review/authoring/closeout;
  the review read, the closeout and the integration owners are wired here, and the authoring boundary is
  recorded as an absence rather than given a synthetic owner.

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
composes, and in the cases that drive them. The three details a reader should carry: **the matrix is the authority: all four packet-named raw transitions have unsupported reconciliation, and rebase additionally has stale boundary state**; **`unchanged` exists so the control state never
names an event that did not happen**; and **caught expected Git/store failures are represented as states. Review measurement calls _report outside its read-error catches, so report-model validation can still raise; the named lookup deliberately raises KeyError for unknown transitions. This is not a universal never-raising guarantee.**

- **The value this module publishes, its four-state union and the validator that refuses every false shape.** [39]
- **The transition vocabulary, including `unchanged` as the measured absence of a transition.** [40]
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

The module measures multiple local code/source/memory repository identities selected by one leaf contract; it makes no remote, credential or network call. Every repository it touches is a checkout
this same repository's own contract resolved — the code worktree, the declared source branch and the
memory work branch all belong to the leaf whose enclosure contract was passed in — and the generation it
reads lives under the task root the same contract names. The three reads it performs are local Git
ancestry questions asked through `worktrees/modules/git.py`, and no remote, credential, network or
external system is involved. No cross-repo reference row is recorded here because no cited range proves
a repository or external-system boundary.

- **The module's own statement of what is measured, what is not claimed, and that no ancestry check identifies a pick or a revert.**  Anchor: "It measures; it decides nothing." [1]
- The owners this module composes, and the three guarded Git reads it borrows.  Anchor: `is_ancestor` [2]
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

- `_tip` preserves read failure as missing tip; `_object_readable` returns false on expected errors; `_related` also returns false on errors, which `_ancestry` treats as replacement, so not every failed read stays an unavailable state. [29]

- The ancestry read that answers whether a recorded identity is still in a branch's history. [30]
- The shape measured for one finding, never the command guessed. [31]
- The replaced identity spelled `channel:identity` for the value no longer in place. [32]
- **The reason an absence carries, naming each unreadable channel with its own detail.** [33]
- **One sentence per state, with no state borrowing another's clause.** [34]
- **The clause stating what an absence did compare, false only when nothing was compared.** [35]
- **The agreement sentence, whose `unchanged` clause never describes an advance.** [36]
- The movement sentence: the replaced channels first, then the channels that still stood. [37]
- The replacement spelled from the values the check read rather than from a diagnosis. [38]
- **The review read that calls this owner and carries the value on the payload.**  Anchor: `external_git_movement` [41]
