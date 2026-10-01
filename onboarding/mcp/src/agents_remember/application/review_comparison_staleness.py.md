# mcp/src/agents_remember/application/review_comparison_staleness.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Whether the comparison a review renders is still the one its reader was shown (`ICR-R17@v1`). The module
owns exactly two responsibilities, and they are one: the identity a comparison declares
(`comparison_identity`) and the staleness state that identity earns when a **previous** binding identity
is carried beside it (`review_staleness`). It is the seam the over-limit review adapter's packet asked
for: the touched responsibility (the comparison's declared identity plus the move-detection rule) moved
out of [`application/knowledge_review.py`](knowledge_review.py.md) (1077 → 1041 lines) into a
purpose-named adjacent owner, and the adapter imports these two names and calls them.

**Nothing recomputes an identity.** `comparison_identity` reads the comparison operation's own
`binding`/`binding_digest`/`selector_digest` and copies them, with the comparison's `policy_version` and
both snapshots' own logical digests and code tree ids, into the payload's
[`ComparisonIdentity`](../models/knowledge/review.py.md). It hashes nothing, resolves nothing and
re-derives nothing: the digest an assessment was bound against is the one the comparison owner published,
and a second spelling of it here is how two readers come to compare two different generations. A page
result that declares no binding, no binding digest or no selector digest asserts rather than falling
back — a review of it could name no generation for a reader to hold on to, so the refusal is the honest
answer to "is this still the one you were shown".

**Staleness is a comparison of two identities, and one of them is the caller's.** The reader looking at a
displayed comparison carries **that** comparison's `binding_digest` on the next read
(`ReviewSurfaceRequest.previous_binding_digest`, supplied by the client's refresh control and admitted at
the route). When it disagrees with the comparison rendered now, the state is `stale`: the identity the
reader was looking at is retained as a **labelled previous input**
([`ReviewStaleness.previous_comparison_ref`](../models/knowledge/review.py.md)) and submission is
disabled against the new comparison, which is what stops a judgement made about inputs that have since
moved from being re-presented as a review of what is there now. When the digest agrees, **or when the
caller carried none**, the state is `current` — and the model itself refuses a `stale` state with no
previous reference, so this module cannot produce a stale claim that names nothing.

**The previous identity is evidence of what was displayed, not an authority.** It selects no dataset,
resolves no candidate and is never substituted for the identity the comparison declares; it is only ever
compared against it. A caller that carries an identity the current comparison does not match gets the
honest `stale` answer rather than a fallback: the review is still the candidate's own comparison,
rendered in full, with the mismatch stated. Which comparison is current is the owners' answer, not this
module's and not the transport's.

## Code Commentary

### Logic

**Two names are the whole public surface.** `__all__` publishes `comparison_identity` and
`review_staleness` and nothing else; `_MOVED_STATEMENT` and `_MOVED_FIELDS` stay private because the
sentence and the moved axis are this state's own rendering rather than a second vocabulary. The adapter
imports the two public names, so the over-limit module keeps only *that* it asks for an identity and
*where* it publishes the staleness it earns.

**The moved sentence is worded here, not at a render site.** `_MOVED_STATEMENT` is
`"Candidate changed — open a new comparison"` and `_MOVED_FIELDS` is `("comparison-binding",)`: the
sentence a reader sees beside a stale payload is the one the state itself publishes, so the state and the
sentence that explains it cannot drift. The `current` branch words its own statement beside it, in the
same function.

**Both call sites are in the adapter's composition, and the identity is computed once.**
`compose_review` calls `comparison_identity(comparison)` immediately after the comparison and the review
matrix answer, then `review_staleness(identity, request.previous_binding_digest)`, and reads
`staleness.state == "stale"` for the submission state **and** publishes the same `staleness` value on the
payload — one measurement, so "an assessment is never submitted against a comparison that has moved"
cannot be true of one field and false of the other. `read_knowledge_review` no longer takes a
`previous_binding_digest` keyword at all: the previous identity travels on the **request**, which is one
spelling of what was asked.

**Why it lives beside the adapter rather than inside it.** `knowledge_review.py` is at the repository's
file-size rail; the two helpers it used to define (`_comparison_identity`, `_staleness`) were private to
it, and nothing under `mcp/` imported them, so the move leaves **no alias and no re-export**: the
adapter's `__all__` is unchanged by this extraction and no importer had to learn a new home.

### Conventions

The module imports its vocabulary rather than declaring it — `KnowledgeDiffResult` from
`models/knowledge/diff.py` and `ComparisonIdentity`/`ReviewStaleness` from
[`models/knowledge/review.py`](../models/knowledge/review.py.md) — and declares no model, no constant a
client reads and no state of its own. Two module-private constants carry the moved sentence and its axis;
`__all__` names the two functions. It imports nothing from the adapter, so the dependency runs one way
(adapter → this module) and there is no cycle to suppress.

### Invariants And Boundaries

- **The identity is carried, never recomputed.** The three fields read are the comparison operation's own
  published ones; the module adds no hash, no digest and no fallback identity.
- **`stale` always names the previous input.** The state is built with
  `previous_comparison_ref=previous_binding_digest`, and `ReviewStaleness`'s own validator refuses a
  `stale` state with no reference and a `current` state that carries one — so the pairing is a property of
  the value, not a convention of this function.
- **No previous input means `current`, by construction rather than by assumption.** An absent digest is a
  read that replaces nothing (a first read, and every read of the leaf's own recorded generation), so
  there is no previous input to label.
- **The previous identity selects nothing.** It never reaches a dataset path, a candidate resolution or a
  comparison input; only the reported state and the labelled reference read it.
- **One rule, one implementation.** The moved pair has exactly one definition; the adapter calls these
  names and defines no second copy.

### Todos

None recorded. One honest limit belongs to the surface above this module and is recorded rather than
closed here: the request field cannot distinguish "a refresh" from "any read that carries a digest", so a
caller that carries one on a first read is answered `stale` about an identity it never displayed — which
is the honest answer to the question it asked, and grants no authority. Requiring "a previous read for
this subject actually happened" would be a session/state contract this surface does not hold.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring, the two
published names, the four-line constants block, the two functions and the adapter, model, route and test
sites that read them. Every anchor in a row occurs inside the range that row cites.

- **The module's own statement of its two responsibilities: the identity is carried and never recomputed, staleness compares two identities one of which is the caller's, and the previous identity is evidence of what was displayed rather than an authority.** [1]
- The published surface: exactly the two functions, one responsibility each. [2]
- **The moved sentence and its moved axis, worded where the state is built rather than at a render site.** [3]
- **The comparison's own declared identity: the operation's published binding, digest and selector digest copied verbatim with the policy version and both snapshots' own facts, and the assertion that a page declaring no identity is refused rather than given a fallback.** [4]
- **The staleness rule: agreement or an absent previous digest is `current`; disagreement is `stale` with the carried identity retained as the labelled previous input and the moved axis named.** [5]
- **The model validator that makes "a stale claim names its previous input" structural: a `stale` state with no reference and a `current` state carrying one are both unconstructible.** [6]
- **The request field the previous identity travels on, sha256-shaped and optional — the *previous* identity, never a substitute for the current one.** [7]
- **The adapter's delegation: the composition computes the identity once and reads one staleness value for both the published state and the submission state, and imports these names instead of defining them.** [8]
- **The transport's admission of the previous identity in the route's own vocabulary, shape-checked against the models' own digest pattern rather than raised out of the request model.** [9]
- **The cases that measure the rule through the real composition: the stale rule in both directions at the composition, and the new R17 case that drives the whole transport path — admission, forwarding on the request, `stale` with `previous_comparison_ref` and `disabled_stale`, `current` when nothing was carried, and a 400 naming a malformed spelling.** [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The module compares two identities of one
repository namespace's candidate and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
