# mcp/src/agents_remember/models/knowledge/review_staleness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_staleness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T17:15:00+02:00 |
| lastVerifiedCommitHash | `4c000b11c5243e4a8e77c08e87984fff00c1d94b` |
| lastVerifiedCommitDate | 2026-09-23T20:33:15+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The three display models the review surface publishes about its own inputs, and the one implementation
of each rule.** This module owns the review surface's own state *about* its inputs, which is a different
question from what a comparison *contains*: whether the comparison a reader is looking at is still the
candidate's comparison, whether a managed sync moved the reviewed inputs of the generation this leaf
published, and whether an assessment may be submitted against what is displayed.

| Model | Requirement | What it owns |
| --- | --- | --- |
| `ReviewStaleness` (`:51-82`) | ICR-R17@v1 | the identity a reader carried beside the comparison rendered now, and the labelled previous input a mismatch earns |
| `ReviewSyncMovement` (`:85-187`) | ICR-R22@v1 | what a leaf's own managed sync *measured* when it resolved the pair, read from the durable rebinding record and rendered on the live review read |
| `ReviewSubmission` (`:190-204`) | this increment's boundary | whether an assessment may be submitted against what is displayed — the display-only boundary: nothing here publishes an assessment |

**Why it is its own module.** `models/knowledge/review.py` — the payload vocabulary that re-exports these
three names — measured **1198 lines** against the repository's 1200-line hard rail at this leaf's base
commit, so adding the movement vocabulary there would have made it a new offender. The extraction the
file-size rule asks for is this one: one cohesive responsibility, moved whole, with the payload module
re-exporting every name so its importers and tests keep working. `review.py` measures **1164 lines** at
this candidate. There is one implementation of each rule, and it lives here.

## Code Commentary

### Logic

**`ReviewStaleness` labels a previous input rather than losing it.** The state is the three-member union
`current` / `stale` / `not_compared` (`:69`), `statement` is required prose (`:70`),
`previous_comparison_ref` is optional (`:71`) and `moved` is a tuple of moved identities (`:72`). The
`after` validator `_require_the_previous_input_to_be_labelled` (`:74-82`) enforces both directions: a
`stale` state without a previous ref is refused, and any non-stale state carrying one is refused, so a
label that names nothing and a current comparison with a "previous" both fail at construction.
`not_compared` is the task-context state and not a third flavour of current (`:58-60`): a review opened
from the task alone compared no knowledge operand, so there is no comparison binding that could be current
or stale, and the response says that instead of borrowing the word for either. The class docstring names
the three possible causes of a `stale` state and says the statement names which one it is — a carried
comparison identity that no longer matches (ICR-R17@v1), a recorded managed sync that moved the reviewed
inputs of the generation this leaf published (ICR-R22@v1, which `ReviewSyncMovement` reports beside it), or
both (`:62-66`).

**`ReviewSyncMovement` is four-valued because the record it reads is three-valued.**
`ReviewSyncMovementState` (`:45-48`) is declared once as
`Literal["current", "stale", "not-measured", "unavailable"]` because the vocabulary, the projection and the
sentence builder all switch on it: `current` is the only state that claims agreement, and `not-measured`
and `unavailable` are states that report an absence and carry the reason behind it. The field set
(`:111-129`) carries the generation that was measured (`generation_id`, `generation_index`), the comparison
identity it bound (`reviewed_binding_digest`, `reviewed_candidate_code_tree_id`,
`reviewed_knowledge_logical_digest`), the pair the sync resolved (`resolved_code_head`,
`resolved_candidate_code_tree_id`, `resolved_knowledge_logical_digest`), the moved identities, the reason,
the statement, the successor action, and the three boundary flags `record_readable`, `reuse_permitted` and
`reinterpreted_for_new_inputs`, which carry the same three facts ICR-R15@v1 carries (`:99-100`). The
`resolved_*` fields are present exactly when that channel was the one that moved: a channel that still
matches, was never compared, or could not be read has nothing to report there, and inventing a value for it
"would be the fabricated identity this vocabulary exists to refuse" (`:105-108`).

**The `after` validator is what makes a false movement unpublishable.** `_the_state_follows_from_what_was_measured`
(`:131-187`) checks every direction, and each wrong combination is a different false claim (`:133-142`): a
named moved input must be `stale` (`:144-150`); a `stale` state with nothing moved asserts movement nobody
observed (`:151-155`); the two absence states must carry a non-blank reason, while a measurement may carry
none (`:156-166`); `record_readable` is `False` exactly when the state is `unavailable`, because "only an
unusable record is unreadable, and every other state was read" (`:167-171`); and the three resolved
identities travel only with a movement — absent for every state that is not `stale`, and at least one named
for `stale`, since a stale movement without one "asserts movement without the value that moved it"
(`:172-186`).

**`ReviewSubmission` states the increment's boundary as data.** The state is the two-member union
`unavailable` / `disabled_stale` (`:200`), `reason` and `next_action` are required prose (`:201-202`),
`proposed_dispositions` publishes which judgements the existing authority accepts (`:203`) and
`none_is_approval` (`:204`) states the boundary the vocabulary itself enforces — none of the published
dispositions is publication approval (`:196-198`). The class docstring records that no serving route
publishes an assessment, so the surface reports the absence and names the existing authority that does
instead of leaving the state implicit (`:190-198`).

### Conventions

`__all__` (`:37-42`) publishes the three classes and the state alias in one alphabetical list. The module
imports only what the three models need (`:22-35`): `Literal` from `typing`, `Field` and `model_validator`
from pydantic, and six names from the knowledge base vocabulary — `KnowledgeModel`, `PROSE_MAX_LENGTH`,
`REFERENCE_MAX_LENGTH`, `SHA256_PATTERN`, `GIT_OBJECT_PATTERN` and `UUID_PATTERN`. Every constrained field
names its bound from that shared vocabulary rather than a local number: `generation_id` is `UUID_PATTERN`
(`:117`), the digests are `SHA256_PATTERN` (`:120`, `:122`, `:125`), the git objects are
`GIT_OBJECT_PATTERN` (`:121`, `:123`, `:124`), `previous_comparison_ref` is `REFERENCE_MAX_LENGTH` (`:71`)
and every prose field is `PROSE_MAX_LENGTH`. Cross-field rules are `@model_validator(mode="after")` methods
returning `self` (`:74-82`, `:131-187`), so no route can construct an invalid value — not even by
`model_validate` on a dict, which is how the cases forge one. `ReviewSyncMovementState` is a module-level
`Literal` alias rather than an enum (`:48`), which is how the sibling rebinding vocabulary spells its own
unions (`models/knowledge/review_sync_rebinding.py:88-96`).

### Invariants And Boundaries

- **Display-only, in all three models.** No field holds a conclusion, a severity, a score or an approval;
  `none_is_approval` is the statement of that boundary carried as data rather than as a comment, and the
  submission model's two states are both unfavourable.
- **An absence is named, never defaulted favourably.** `current` is the only movement state that claims
  agreement; `not_compared` is not a flavour of `current`; and both movement states that report an absence
  must carry the reason behind them.
- **The stale rule is bilateral.** A `stale` comparison with no previous input is refused, and a non-stale
  comparison carrying one is refused: the field may never label an identity nobody held, and a current
  comparison has no previous input to label.
- **The movement is one consistent value or it is not a value.** State, moved identities, `record_readable`
  and the resolved identities are checked against each other at construction, so no producer can hand a
  reader a movement whose parts disagree. The reader that produces these values is
  `application/review_sync_movement.py:165-213`; the four clauses a per-clause sweep found unpinned are
  pinned one forgery each at `mcp/tests/test_review_sync_movement_read.py:258-327`.
- **One implementation of each rule, reached through the payload module.** `models/knowledge/review.py`
  re-exports all three names and defines none of them (`:61-64`, with the `__all__` entries at `:116`,
  `:119` and `:121`), so existing importers and tests keep their import site; the payload's own fields still
  name these types (`:1019-1026`).
- **Boundary: the extraction moved the declarations, not the payload.** `KnowledgeReviewPayload` is still
  declared in `models/knowledge/review.py` (`:991-1084`) and nothing here assembles a payload; the
  `ReviewStaleness` and `ReviewSubmission` field sets and validators are byte-identical to the declarations
  that module carried before this leaf, with only `ReviewStaleness`'s docstring gaining the paragraph that
  names the third cause of a `stale` state.
- **Boundary: `record_readable` is `False` for both `unavailable` sub-cases**, so that one field cannot
  separate an unreadable artifact from a valid record that names another generation. The sub-fact is carried
  by `reason`; renaming the field or narrowing its documented meaning needs a production-byte change here
  and is **held for the master's ruling**, which the pinning case states in place
  (`mcp/tests/test_review_sync_movement_read.py:219-225`).
- **Boundary: `resolved_knowledge_logical_digest` is the dataset's logical digest, not a dataset identity.**
  A consumer that needs the resolved dataset's own `SnapshotIdentity` reads the record's own
  `resolved_knowledge.dataset`; this vocabulary carries only what the review surface renders, and the
  identity itself stays with the owner that captured it.
- **Boundary: the revoked movement state cannot be inferred from this module's fields.** Whether a record
  was usable at all, and by which of the two reasons it was not, is a fact the reader established; this
  module only requires the two to travel together.

### Todos

None recorded.

## Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole content is the statement that no
entries are configured — so there is no external or domain documentation source to consult, and no
documentation row is recorded here. Every statement on this card is grounded in the repository's own
source, docstrings and cases, and the paragraphs above are backed by the table below.

## Repo-Internal References

Every claim on this card is checkable in the module's own declarations and validators, in the payload
module that re-exports them, in the owners that produce each value, and in the cases that drive them. The
three details a reader should carry: **the movement's state follows from what was measured, never from a
two-way reading of the channel matches**; **an absence state must name the reason behind it while a
measurement may not carry one**; and **`review.py` still publishes all three names**, so the extraction
changed a home and not an import site.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three questions it owns, why it is its own module, and the one-implementation rule.** | "There is one implementation of each rule and it lives here." | mcp/src/agents_remember/models/knowledge/review_staleness.py:1-20 |
| The imports the three models need, and the `after` validator machinery they are built on. | `model_validator` | mcp/src/agents_remember/models/knowledge/review_staleness.py:22-35 |
| The published surface: three models and the state alias, in one alphabetical list. | `__all__` | mcp/src/agents_remember/models/knowledge/review_staleness.py:37-42 |
| **The four measured states declared once, with `current` as the only one that claims agreement.** | `ReviewSyncMovementState` | mcp/src/agents_remember/models/knowledge/review_staleness.py:45-48 |
| **The stale comparison, its three-member state union, and the three causes of a stale state the statement names.** | `ReviewStaleness` | mcp/src/agents_remember/models/knowledge/review_staleness.py:51-82 |
| **The bilateral previous-input rule: a stale comparison must label one, and no other state may carry one.** | `_require_the_previous_input_to_be_labelled` | mcp/src/agents_remember/models/knowledge/review_staleness.py:85-85 |
| **The measured movement: its field set, the resolved identities present exactly on the channel that moved, and the record_readable/reuse_permitted/reinterpreted_for_new_inputs flags.** | `ReviewSyncMovement` | mcp/src/agents_remember/models/knowledge/review_staleness.py:85-187 |
| **The `after` validator that refuses every false movement shape — state against moved identities, absence against reason, and `record_readable` against `unavailable`.** | `_the_state_follows_from_what_was_measured` | mcp/src/agents_remember/models/knowledge/review_staleness.py:131-187 |
| **The submission boundary carried as data: two unfavourable states, and `none_is_approval`.** | `ReviewSubmission` | mcp/src/agents_remember/models/knowledge/review_staleness.py:190-204 |
| The shared bounds, patterns and base model every field is constrained from. | `PROSE_MAX_LENGTH`; `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:18-27; mcp/src/agents_remember/models/knowledge/base.py:34-39 |
| **The re-export that made the extraction invisible to importers, and the payload vocabulary's own `__all__` entries for the three names.** | `review_staleness`; `ReviewSyncMovement` | mcp/src/agents_remember/models/knowledge/review.py:61-64; mcp/src/agents_remember/models/knowledge/review.py:62-65; mcp/src/agents_remember/models/knowledge/review.py:118-123 |
| **The payload that still declares the staleness, submission and movement fields, and the comment distinguishing "no sync has reported" from "a sync reported agreement".** | `KnowledgeReviewPayload`; `sync_movement` | mcp/src/agents_remember/models/knowledge/review.py:991-1084; mcp/src/agents_remember/models/knowledge/review.py:1019-1026 |
| **The R17 producer that builds a current or carried-mismatch staleness, and the fold that replaces it when a sync measured movement.** | `review_staleness`; `review_staleness_with_sync_movement` | mcp/src/agents_remember/application/review_comparison_staleness.py:76-97; mcp/src/agents_remember/application/review_sync_movement.py:357-382 |
| The task-context producer that uses the `not_compared` state because no knowledge operand was compared. | `ReviewStaleness` | mcp/src/agents_remember/application/review_task_context.py:152-159 |
| The display-only submission producer, whose two states are the model's own members. | `submission` | mcp/src/agents_remember/application/review_record_rendering.py:194-223 |
| **The projection whose output this model's validator accepts, and the record vocabulary the movement's three states are read from.** | `_project`; `ReviewSyncRebindingVerdict` | mcp/src/agents_remember/application/review_sync_movement.py:165-213; mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:97-103 |
| **The case that pins the four validator clauses one forgery each, with the real published movement as the accepted control.** | `test_the_movement_validator_refuses_each_false_shape` | mcp/tests/test_review_sync_movement_read.py:258-327 |
| **The case that pins the two `unavailable` sub-cases and records the `record_readable` hold in place.** | `test_a_record_that_cannot_be_used_is_reported_unavailable` | mcp/tests/test_review_sync_movement_read.py:169-226 |

## Cross-Repo References

No cross-repository behavior is implemented in this module. It declares value shapes only: it reads no
store, resolves no path and touches no repository, and every identity its fields carry — a comparison
binding digest, a git object id, a dataset logical digest — is a value another owner in this same
repository resolved. The relocation and dataset-ownership boundaries that follow from those identities
belong to the owners that produce them (the generation store and the knowledge store), not to this
vocabulary. No cross-repo reference row is recorded here because no cited range proves a repository or
external-system boundary.

## Update History
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **`ReviewStaleness` gained its fourth state, and this card's one enforced row was re-anchored.** `state` is now `Literal["current", "stale", "not_compared", "not-measured"]` (`:79`) and the docstring states what the new member is for and what it is not: the boundary could not take its comparison at all, so the surface may not claim currency — and it is not `stale`, because no movement was observed and submission is not disabled by it. The repaired row is the `ReviewSyncMovement` re-export and its two `__all__` entries (`:62-65`, `:118-123`). **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee`): created this one-to-one card for the module this leaf introduced as **the home of three display models extracted out of `models/knowledge/review.py`** so that module (1198 lines at this leaf's base, 1164 now) stayed under the repository's 1200-line hard rail. It records what a consumer has to act on: `ReviewStaleness` is ICR-R17@v1's and keeps the last displayed comparison as a *labelled previous input* under a bilateral validator; `ReviewSyncMovement` is ICR-R22@v1's, with the deliberately four-member `binding_state` (`current` / `stale` / `not-measured` / `unavailable`) whose `after` validator keeps the state, the moved identities, `record_readable` and the resolved identities consistent in every direction; and `ReviewSubmission` carries the increment's display-only boundary with no favourable member. `review.py` re-exports all three names, so one implementation of each rule lives here while importers and tests keep their import site, and the `ReviewStaleness` and `ReviewSubmission` field sets and validators are byte-identical to the declarations that module carried. One boundary is carried as a boundary and not as a defect: `record_readable` is `False` for both `unavailable` sub-cases, so one field cannot separate an unreadable artifact from a valid record naming another generation — the sub-fact lives in `reason`, and the field-level fix is **held for the master's ruling** exactly as the pinning case states it. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name this leaf's recorded base `e605822eb3bf83bf63a45963c5f51d5fc28859ee` because every construct cited here exists only in this leaf's uncommitted working tree — the file itself is untracked at that commit — so no commit contains the content a stamp would claim to have verified; what was actually read is that working tree, and the governed closeout owns the real stamp once its transaction creates the code commit.
