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

### Invariants And Boundaries

- Previous-input labels and current displayed inputs are separate identities; a stale label never points at an invented previous record.
- A complete comparison, binding digest and exact reviewed trees must agree; another record's digest or tree is refused.
- Absence is named and explained, never defaulted to agreement or zero movement.
- The value validates its own measured facts and writes no comparison or assessment.
- review.py re-exports these models; one implementation owns their rules rather than duplicated payload declarations.

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
