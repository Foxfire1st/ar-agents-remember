# mcp/src/agents_remember/application/review_external_git_movement.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Measure declared local Git ancestry against the retained review tree comparison and expose the support matrix and recovery sentences. This is a read-only descriptive boundary, not a comparison recorder, Git repair, approval or new transaction gate.

## Code Commentary

### Observed wire shapes versus documented recovery

`GitTransitionSupport.transition` deliberately has a broader annotation than the report's `ExternalGitTransition`: it also admits cherry-pick and revert so the existing recovery matrix can describe them. The report wire union is unchanged, ordinary-append, rebase and branch-switch only. `_transition` emits branch-switch from the branch-left subfact, rebase from replaced ancestry and ordinary-append from advanced ancestry; `_shapes` supplies unchanged only when all declared channels were compared and none yielded a shape. An ancestry observation does not identify which Git command ran.

The matrix retains unchanged/ordinary-append supported rows and rebase/cherry-pick/revert/branch-switch unsupported recovery rows. A rewrite is stale; a branch switch is not-measured. Lookup refuses an unknown matrix name with `KeyError`. Recovery text, unsupported listings and the Markdown renderer derive from the table instead of restating another verdict. Narrowing the report's constructible transition values does not delete or promote the two documentation-only recovery rows.

### Retained comparison and absence

The live-review entry returns no measurement for absent enclosure, closed leaf or non-live tree inputs. The contract owner distinguishes a non-leaf, missing work branch and no recorded generation as separate `_BoundaryAbsence` details. An unusable retained comparison is unavailable, not never-reviewed. The measured v2 value carries the complete comparison and its canonical digest; an uncommitted candidate tree is not fabricated into an observed work-branch commit.

Findings ask the code work branch, declared source branch and supplied memory-work branch in order. Missing commit proof is unavailable for that channel, even though the tree pin remains known. `_state` reports stale if any identity was replaced, otherwise current only when all findings are available, otherwise not-measured. Its vocabulary and observed fields must not be read as independent verification that caller-supplied evidence is authentic.

### Failure and transaction boundaries

Expected store/Git errors are caught in the named read paths, not by a universal exception wrapper. In particular `_related` returns false on expected ancestry-read errors; `_ancestry` can consequently classify that result as replaced rather than unavailable. Do not promote the source comment about succeeded reads into a stronger no-false-replacement guarantee. `_measure_generation` calls `_report` outside its read-error catches, so report-model validation can still raise.

`external_git_movement_result_block` returns an unsuccessful payload untouched. On successful results it attaches the measurement or typed absence and catches its named expected measurement failures. It adds no transaction admission, source-lineage waiver or approval; existing closeout/integration checks remain independently owned. It neither mutates a checkout nor records a successor comparison.

The BASE-to-current application delta is the matrix row annotation's explicit cherry-pick/revert extension; the remainder of this module is byte-identical after reversing that one annotation. The focused model separately removes those two report literals. This is static source comparison, not a runtime or suite grade.

## Evidence

No domain documentation source is configured. Current evidence is the read application/model source; the prior detailed account and its old numeric hints are preserved historically below, not as current coordinates or additional promises.

- The support-row type retains the complete recovery matrix beyond the report wire union. [51]
- Recovery sentences, unknown-name refusal, unsupported listings and rendering share the matrix. [52]
- The wire transition union has four ancestry shapes, not cherry-pick or revert. [53]
- The live boundary distinguishes no measurement, retained-comparison read failure and source validation. [54]
- Successful result attachment and typed absence do not gate failed transactions. [55]
- Unavailable comparison values invent no retained source identity. [56]
- Report shape/state composition follows supplied findings and current shape extraction. [57]
- Declared channel findings distinguish uncommitted tree pins from observable commit ancestry. [58]
- Ancestry and expected-error fallbacks carry their actual limited behavior. [59]
- The branch-left subfact and actual observed ancestry determine emitted transitions. [60]
- Statements use measured clauses and preserve distinct unchanged, movement and absence explanations. [61]

## Historical predecessor account

The complete predecessor is retained as provenance. Its former line hints and prose markers are inert historical material; use the current ranges above for present source behavior.

### mcp/src/agents_remember/application/review_external_git_movement.py

#### Governing Overview

[application route overview](overview.md)

#### Purpose

Measure raw Git ancestry against the retained review tree record and publish the existing support matrix for recovery. The read mutates no checkout and records no comparison.

#### Code Commentary

##### Logic

The retained comparison names exact code/memory bases and any recorded candidate commits. Channels distinguish unchanged tips, ordinary advances, replaced history, switched branches and unreadable inputs. An uncommitted candidate has a tree pin without an observed work-branch HEAD; that channel is not measured and a current checkout supplies no historical proof.

The single support matrix supplies rendered documentation and recovery actions. Unsupported raw transitions remain unsupported; each compared and unread channel is named.

##### Invariants And Boundaries

Source identities never become fabricated generation UUIDs. Corrupt content and an absent boundary remain distinct. Missing proof is neither current nor measured movement. The reading neither clears intent nor repairs transaction authority.

##### Todos

None recorded.

##### Logic

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

##### Invariants And Boundaries

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

#### Evidence

##### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so there is no external or domain
documentation source to consult and no documentation row is recorded here. The one documentation
artifact this leaf does touch — `docs/reference/worktrees-c09.md` — is not an external source: it is a
repository file whose new `## Raw Git Identity Boundary` section is *generated from* this module's
matrix, and the assertion that binds the two is filed under Repo-Internal References.

##### Repo-Internal References

Every claim on this card is checkable in the module's own declarations, in the owners whose reads it
composes, and in the cases that drive them. The three details a reader should carry: **the matrix is the authority: all four packet-named raw transitions have unsupported reconciliation, and rebase additionally has stale boundary state**; **`unchanged` exists so the control state never
names an event that did not happen**; and **caught expected Git/store failures are represented as states. Review measurement calls _report outside its read-error catches, so report-model validation can still raise; the named lookup deliberately raises KeyError for unknown transitions. This is not a universal never-raising guarantee.**

- **The value this module publishes, its four-state union and the validator that refuses every false shape.** (historical reference 39)
- **The transition vocabulary, including `unchanged` as the measured absence of a transition.** (historical reference 40)
- The task-context review boundary, which takes the same measurement and refuses nothing on it. (historical reference 42)
- **The fold that lets an external `stale` outrank a carried comparison identity and a recorded managed-sync rebinding.** (historical reference 43)
- **The closeout preview, closeout apply and integration call sites that attach the statement.** (historical reference 44)
- The integration result block that carries the same statement. (historical reference 45)
- **The documented matrix, asserted to be the rendered production table rather than a transcription.** (historical reference 46)

- Uncommitted records invent no observed HEAD, and history replacement retains source identity without fabricated UUIDs. (historical reference 47)


- The documented matrix comes from the measured-operation table. (historical reference 48)


- Contradictory boundary measurements are refused. (historical reference 49)


- Untouched, advanced and rewritten history have distinct measured answers. (historical reference 50)


##### Cross-Repo References

The module measures multiple local code/source/memory repository identities selected by one leaf contract; it makes no remote, credential or network call. Every repository it touches is a checkout
this same repository's own contract resolved — the code worktree, the declared source branch and the
memory work branch all belong to the leaf whose enclosure contract was passed in — and the generation it
reads lives under the task root the same contract names. The three reads it performs are local Git
ancestry questions asked through `worktrees/modules/git.py`, and no remote, credential, network or
external system is involved. No cross-repo reference row is recorded here because no cited range proves
a repository or external-system boundary.

- **The module's own statement of what is measured, what is not claimed, and that no ancestry check identifies a pick or a revert.**  Anchor: "It measures; it decides nothing." (historical reference 1)
- The owners this module composes, and the three guarded Git reads it borrows.  Anchor: `is_ancestor` (historical reference 2)
- The published surface: the matrix, its row type, the three entry points, the renderer and the lookup. (historical reference 3)
- The four states this module may report, declared once as the read surface's own vocabulary. (historical reference 4)
- **The recovery a generation that cannot be read names, kept apart from the successor generation a movement names.** (historical reference 5)
- The recovery a boundary names when nothing could be compared at all. (historical reference 6)
- **The fold that derives every recovery sentence from the matrix rows rather than restating a verdict.** (historical reference 7)
- The three declared channels, each named by the thing that moved rather than by the command that moved it. (historical reference 8)
- One matrix row: the transition, its measured Git signature, the state it renders in, whether it is reconciled, and the step a person takes. (historical reference 9)
- **The support matrix itself — six rows, one per shape, with `rebase` the only named transition an ancestry check can mark `stale`.** (historical reference 10)
- The by-name lookup derived from the matrix, so a row added above is reachable below with no second list. (historical reference 11)
- **The named lookup that refuses an unknown transition instead of answering with a default.** (historical reference 12)
- **The unsupported list derived from the matrix, which is what a report repeats where the reader is.** (historical reference 13)
- The Markdown renderer the documentation is asserted against, so the document is generated rather than transcribed. (historical reference 14)
- One channel's measurement, and the shape measured for it. (historical reference 15)
- A branch tip read from a repository, or the reason there is none to read. (historical reference 16)
- **The review read's entry point, whose `None` answers are all facts rather than failures, and whose unreadable generation is `unavailable` with the selection's own detail.** (historical reference 17)
- **The absence value: the cause in the words of the arm that established it, so the read and the published block share one branch.** (historical reference 18)
- **The declaration half of the measurement, where a non-leaf contract and a contract with no work branch are two different causes with two different sentences.** (historical reference 19)
- **The store half of the measurement, where an unusable generation is `unavailable` and a leaf that published nothing carries the store's own detail.** (historical reference 20)
- **The contract-only half the closeout and integration owners call, so one implementation serves every caller.** (historical reference 21)
- **The closeout/integration statement that never refuses: a failed result is returned untouched and every absence becomes a typed block.** (historical reference 22)
- **The typed absence that repeats the matrix's unsupported transitions whether or not the boundary measured.** (historical reference 23)
- **The state an unusable generation earns, with no generation identity claimed.** (historical reference 24)
- **The state composition — `stale` over `current` over `not-measured`, with `current` requiring every channel compared.** (historical reference 25)
- The three declared channels turned into findings, in fixed order. (historical reference 26)
- **The one ancestry decision: `current` / `advanced` / `replaced` / `unavailable`, where `advanced` is a measurement of its own.** (historical reference 27)
- The failure state an unreadable channel or repository earns. (historical reference 28)

- `_tip` preserves read failure as missing tip; `_object_readable` returns false on expected errors; `_related` also returns false on errors, which `_ancestry` treats as replacement, so not every failed read stays an unavailable state. (historical reference 29)

- The ancestry read that answers whether a recorded identity is still in a branch's history. (historical reference 30)
- The shape measured for one finding, never the command guessed. (historical reference 31)
- The replaced identity spelled `channel:identity` for the value no longer in place. (historical reference 32)
- **The reason an absence carries, naming each unreadable channel with its own detail.** (historical reference 33)
- **One sentence per state, with no state borrowing another's clause.** (historical reference 34)
- **The clause stating what an absence did compare, false only when nothing was compared.** (historical reference 35)
- **The agreement sentence, whose `unchanged` clause never describes an advance.** (historical reference 36)
- The movement sentence: the replaced channels first, then the channels that still stood. (historical reference 37)
- The replacement spelled from the values the check read rather than from a diagnosis. (historical reference 38)
- **The review read that calls this owner and carries the value on the payload.**  Anchor: `external_git_movement` (historical reference 41)
