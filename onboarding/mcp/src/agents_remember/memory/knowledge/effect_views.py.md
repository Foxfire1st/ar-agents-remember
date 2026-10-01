# mcp/src/agents_remember/memory/knowledge/effect_views.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The authored-effect record group's derived views: pure functions of the stored rows, and nothing else.
The strongest way to hold "a view is disposable and never an authority" is not to store a view at all,
and this module stores none — deleting a view changes no claim, no question and no change set, because
there is nothing to delete.

## Code Commentary

### Logic

**Four jobs, and each is where a requirement's *state* becomes readable rather than a refusal.**

- **Membership is computed.** Which effect claims, preservation claims and open questions belong to a
  change set is read out of each member's own stored `change_set_id`. Nothing is inferred from a
  payload's content, and an empty member list means exactly that no member declares this change set.
  This is the membership fact the design allows code to compute, and it is the only thing computed here.
- **An unresolved assessment reference is reported, never filled in.** `ASSESSMENT_ABSENT_DETAIL`
  states the reason as a boundary rather than as a lookup failure: no assessment record kind exists in
  this substrate yet, so every stored assessment reference is unresolved **by construction**. It is
  never a refused write, never a placeholder, and never presented as an assessment that happened.
- **An unresolved requirement-revision reference is reported, never resolved.**
  `REQUIREMENT_REFERENCE_DETAIL` states that the reference is stored verbatim under the opaque-reference
  clause and that this record group holds no requirement authority: no code path here parses it,
  canonicalises it, splits it on a separator, infers a requirement identity from it, or resolves it
  against prose.
- **An unresolved preservation subject is reported, never substituted.** `SUBJECT_UNRESOLVED_DETAIL`
  reports that nothing of the declared kind is stored under that identity in this namespace. The check
  itself is a per-kind existence lookup against the table that would hold the subject — `_SUBJECT_EXISTS`
  is keyed by the subject's declared kind, and the `semantic_change_set` kind additionally filters on
  the record kind — so resolution is a lookup and never a guess, and a subject that resolves to nothing
  is reported rather than refused or re-pointed. The same shape covers a change set's named realization
  claims through `realization_claim_resolves`.

**`effect_scope` is the one builder, and it is a pure function of the rows it is handed.** It collects
the three member kinds, the change sets, the computed membership and the stored precedence, then builds
each view and returns one `AuthoredEffectScope`. The scope-level `unresolved_references` list is the
**union of the per-record lists**, in the order the scope's own fields declare their groups, so a caller
can reconcile the two planes without a second ordering rule and no reference is reported at one plane
and not the other.

**The views are also where the forbidden set is proven absent, at the stored plane.** Every view is
built from a **validated payload model**, so a stored row carrying a truth verdict, a severity, a
generated summary or a preservation flag could not have been decoded into one at all — the absence is
enforced by the decoder rather than asserted here.

### Conventions

Each view builder narrows the decoded payload with an `isinstance` check and raises
`KnowledgeStorageError` if the envelope's kind and the payload's shape disagree — a branch marked
unreachable in practice, because the decoder resolved the shape from the registry by kind. So a
"registry-typed" mismatch is reported as a damaged store rather than as a schema error.

`_lifecycle` returns the **stored** value rather than a constant, which keeps the read honest about what
the row says instead of about what this leaf expects; a value outside the shipped `proposed|accepted`
vocabulary is reported as a damaged store rather than coerced into one, because a third lifecycle state
is exactly what the requirement forbids this record group to mint.

`UnresolvedField` mirrors the view model's own closed field set, so the builder cannot report an
unresolved fact under a field the model would refuse. `_MEMBER_KINDS` fixes the order the scope reports
the member groups in.

### Invariants And Boundaries

- **Nothing here is stored.** There is no view table, no cache and no materialised list; every builder
  returns a value built from rows the caller's store already holds, and a rebuild over unchanged rows is
  byte-identical.
- **The only thing computed is membership.** No meaning is derived: no label, no severity, no ordering,
  no summary. A card that read this module as deriving an effect from a diff would be describing a
  capability the codebase deliberately does not have.
- **An unresolved reference is a state, not a failure.** None of the three unresolved families raises,
  refuses the read, or mutates a row; each is reported with its holder and its verbatim text.
- **A resolution is an existence lookup, never a parse.** `subject_resolves` and
  `realization_claim_resolves` ask the table that would hold the identity; nothing infers an identity
  from reference text.
- **The scope's detail sentence counts what the read produced**, so it describes the read rather than
  the store's expectations.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one builder: the member groups, the change sets, the computed membership and the stored precedence, assembled into one derived scope. [1]
- The membership fact, read out of each member's own stored `change_set_id` — the only thing this module computes. [2]
- The stored predecessor identities keyed by successor, which make a superseded change set addressable rather than overwritten. [3]
- The change set's view, carrying all six declared parts plus its computed membership, its stored predecessors and its unresolved references. [4]
- The stored lifecycle returned rather than a constant, with a third state reported as a damaged store. [5]
- The per-kind existence lookups that make subject resolution a lookup and never a guess. [6]
- The closed field set an unresolved fact may be reported under, mirroring the view model so the builder cannot report one the model would refuse. [7]
- The three unresolved reasons, each stated as a boundary rather than as a lookup failure. [8]
- The row readers the views are built from, which keep the views pure functions of stored rows. [9]
- The derived scope and unresolved-reference models these builders produce. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A view is a function of one namespace's own
stored rows.

No meaningful cross-repo references found.
