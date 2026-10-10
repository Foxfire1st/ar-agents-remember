# mcp/src/agents_remember/models/knowledge/review_staleness.py

## Governing Overview

[models route overview](../overview.md)
## Purpose

The review surface's state about its displayed inputs: ReviewStaleness, the source-bound v2 ReviewSyncMovement and the display-only ReviewSubmission boundary. These values describe a comparison's currency and measured movement; they do not author judgments or execute recovery.
## Code Commentary

### Logic
ReviewStaleness has current, stale, not_compared and not-measured states. A stale comparison must retain the actual previous_comparison_ref it labels; no other state may carry one. not_compared is task context with no knowledge comparison. not-measured means no currency observation could be established and is neither current nor an invented movement. Submission is disabled by the stale rule, not merely by absence of a measurement.

ReviewSyncMovement carries movement_version v2, the complete retained ReviewTreeComparisonRecord, its digest and exact reviewed code/memory trees. A non-unavailable measurement must carry its source comparison. Whenever one is carried, the digest and both reviewed trees must agree with that complete record.

The binding_state is current, stale, not-measured or unavailable. A named moved input requires stale, and stale requires moved identities plus at least one resolved identity. Resolved code head/tree and memory tree travel only for stale movement; matching, unmeasured and unavailable channels do not invent resolved values. Absence states require a reason while measured states carry none. record_readable is false exactly for unavailable. reuse_permitted remains a separate fact and reinterpreted_for_new_inputs is always false.

ReviewSubmission states unavailable or disabled_stale, its reason and next action, proposed dispositions and none_is_approval. No serving route in this vocabulary publishes an assessment; an advertised disposition grants no publication approval.
**`ReviewStaleness` labels a previous input rather than losing it.** The state is the four-member union
`current` / `stale` / `not_compared` / `not-measured`, `statement` is required prose,
`previous_comparison_ref` is optional and `moved` is a tuple of moved identities. The
`after` validator `_require_the_previous_input_to_be_labelled` (`:74-82`) enforces both directions: a
`stale` state without a previous ref is refused, and any non-stale state carrying one is refused, so a
label that names nothing and a current comparison with a "previous" both fail at construction.
`not_compared` is the task-context state and not a third flavour of current: a review opened
from the task alone compared no knowledge operand, so there is no comparison binding that could be current
or stale, and the response says that instead of borrowing the word for either. `not-measured` is the
fourth state and deliberately not a softer `current`: the boundary could not take its comparison at all —
a checkout that left its declared branch, a gone recorded object, an unreadable generation (ICR-R23@v1) —
so the surface carries the movement's own sentence instead of asserting currency, and submission stays
enabled. The class docstring names the four possible causes of a `stale` state and says the statement
names which one it is — a carried comparison identity that no longer matches (ICR-R17@v1), a recorded
managed sync that moved the reviewed inputs of the generation this leaf published (ICR-R22@v1, which
`ReviewSyncMovement` reports beside it), a raw Git operation that replaced a declared identity
(ICR-R23@v1), or some combination.
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

`__all__` publishes the three classes and the state alias in one alphabetical list. The module
imports only what the three models need: `Literal` from `typing`, `Field` and `model_validator`
from pydantic, and five names from the knowledge base vocabulary — `KnowledgeModel`, `PROSE_MAX_LENGTH`,
`REFERENCE_MAX_LENGTH`, `SHA256_PATTERN` and `GIT_OBJECT_PATTERN`. Every constrained field
names its bound from that shared vocabulary rather than a local number: the digests are `SHA256_PATTERN`,
the git objects are `GIT_OBJECT_PATTERN`, `previous_comparison_ref` is `REFERENCE_MAX_LENGTH`
and every prose field is `PROSE_MAX_LENGTH`. Cross-field rules are `@model_validator(mode="after")` methods
returning `self`, so no route can construct an invalid value — not even by
`model_validate` on a dict, which is how the cases forge one. `ReviewSyncMovementState` is a module-level
`Literal` alias rather than an enum, which is how the sibling rebinding vocabulary spells its own
unions (`models/knowledge/review_sync_rebinding.py:88-96`).
### Invariants And Boundaries

- Previous-input labels and current displayed inputs are separate identities; a stale label never points at an invented previous record.
- A complete comparison, binding digest and exact reviewed trees must agree; another record's digest or tree is refused.
- Absence is named and explained, never defaulted to agreement or zero movement.
- The value validates its own measured facts and writes no comparison or assessment.
- review.py re-exports these models; one implementation owns their rules rather than duplicated payload declarations.
- **Display-only, in all three models.** No field holds a conclusion, a severity, a score or an approval;
  `none_is_approval` is the statement of that boundary carried as data rather than as a comment, and the
  submission model's two states are both unfavourable.
- **An absence is named, never defaulted favourably.** `current` is the only movement state that claims
  agreement; `not_compared` is not a flavour of `current`; and both movement states that report an absence
  must carry the reason behind them.
- **The stale rule is bilateral.** A `stale` comparison with no previous input is refused, and a non-stale
  comparison carrying one is refused: the field may never label an identity nobody held, and a current
  comparison has no previous input to label.
- **One implementation of each rule, reached through the payload module.** `models/knowledge/review.py`
  re-exports all three names and defines none of them (`:61-64`, with the `__all__` entries at `:116`,
  `:119` and `:121`), so existing importers and tests keep their import site; the payload's own fields still
  name these types (`:1019-1026`).
- **Boundary: the extraction moved the declarations, not the payload.** `KnowledgeReviewPayload` is still
  declared in `models/knowledge/review.py` and nothing here assembles a payload; the v2 movement carries
  no generation identity and no dataset identity (former UUIDs and digests retired — see the MIK-R26
  historical boundary below), and `ReviewStaleness`'s docstring gained the not-measured paragraph.
### Todos

None recorded.
### Historical boundary — MIK-R26

The former movement carried generation UUIDs and dataset logical digests. Those are not fields of v2. A retained historical dataset rebinding is decoded under its legacy shape and rendered unavailable for tree-pair coverage, without reinterpreting the original judgment or manufacturing an exact reviewed memory tree.
## Evidence

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole content is the statement that no
entries are configured — so there is no external or domain documentation source to consult, and no
documentation row is recorded here. Every statement on this card is grounded in the repository's own
source, docstrings and cases, and the paragraphs above are backed by the table below.

### Repo-Internal References

Every claim on this card is checkable in the module's own declarations and validators, in the payload
module that re-exports them, in the owners that produce each value, and in the cases that drive them. The
three details a reader should carry: **the movement's state follows from what was measured, never from a
two-way reading of the channel matches**; **an absence state must name the reason behind it while a
measurement may not carry one**; and **`review.py` still publishes all three names**, so the extraction
changed a home and not an import site.


- The three retained review display/currentness models. [1]

- The imports the three models need, and the `after` validator machinery they are built on. [2]
- The published surface: three models and the state alias, in one alphabetical list. [3]

- The movement-state Literal distinguishes measurements from explained absences. [4]


- Staleness includes task-context and not-measured states. [5]


- Only a stale comparison labels an actual previous comparison. [6]


- The v2 movement carries its complete source comparison and exact code/memory tree facts. [7]


- Movement state, source binding, absence and resolved identities are self-validated. [8]


- Submission remains a display-only boundary, with no approval disposition. [9]

- The shared bounds, patterns and base model every field is constrained from. [10]
- **The re-export that made the extraction invisible to importers, and the payload vocabulary's own `__all__` entries for the three names.** [11]
- **The payload that still declares the staleness, submission and movement fields, and the comment distinguishing "no sync has reported" from "a sync reported agreement".** [12]
- **The R17 producer that builds a current or carried-mismatch staleness, and the fold that replaces it when a sync measured movement.** [13]
- The task-context producer that uses the `not_compared` state because no knowledge operand was compared. [14]
- The display-only submission producer, whose two states are the model's own members. [15]
- **The projection whose output this model's validator accepts, and the record vocabulary the movement's three states are read from.** [16]

- The current forgery sweep verifies measured movement and complete source-record binding. [17]


- Unreadable or forged rebinding is unavailable and never current. [18]


### Cross-Repo References

No cross-repository behavior is implemented in this module. It declares value shapes only: it reads no
store, resolves no path and touches no repository, and every identity its fields carry — a comparison
binding digest, a git object id, a dataset logical digest — is a value another owner in this same
repository resolved. The relocation and dataset-ownership boundaries that follow from those identities
belong to the owners that produce them (the generation store and the knowledge store), not to this
vocabulary. No cross-repo reference row is recorded here because no cited range proves a repository or
external-system boundary.
- **The module's own statement of the three questions it owns, why it is its own module, and the one-implementation rule.** [19]
- **The four measured states declared once, with `current` as the only one that claims agreement.** [20]
- **The bilateral previous-input rule: a stale comparison must label one, and no other state may carry one.** [21]
- **The `after` validator that refuses every false movement shape — state against moved identities, absence against reason, and `record_readable` against `unavailable`.** [22]
- **The submission boundary carried as data: two unfavourable states, and `none_is_approval`.** [23]
