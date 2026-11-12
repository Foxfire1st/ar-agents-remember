# mcp/src/agents_remember/application/review_family_context.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Compose the selected subject’s comparison-bound family context through the existing family/roster owners: directly relevant identities, independent Before/After family selection, supplied guarantees and bounded exact member pages. This is composition over the supplied side inputs, not a new snapshot capturer, store or semantic acceptance authority.

## Code Commentary

### Entry and discovery

A missing selector produces `no_subject_selected`; an unsupported seed kind produces `unavailable` without substituting an identity. Supported invariant/family identity or revision seeds open the two roster sides and, once both are returned, compose under `try/finally` that closes them.

Invariant discovery uses the read policy’s `directly_containing_families` identity keys, not a page of sibling members as further discovery. `_compose` unions the two sides’ known identities. For an invariant selection, `_entry` then reselects each discovered family by **family identity on both sides**: missing primary membership cannot erase or pin an independent counterpart.

Family identity selection uses the family owner’s recorded revision list; an exact family-revision seed restricts its selected population to that named revision if recorded while keeping the owner’s full recorded list separately. `_applicable_family` now checks named family-file problems before asserting absence. Discovery checks the family scope’s indexed problems; `_Applicable.reason` means unread, distinct from its measured `absent` value.

### Heads and unread states

`_heads` still calls the shared `revision_heads` helper, which returns sorted supplied revisions. There is **no predecessor-edge lookup** in that helper. Old module comments/phrases about authored predecessor edges or cyclic lineage are not evidence of such an implementation. Removal of multi-head logic from the *primary* revision-selection entry point does not remove these distinct family/summary callers.

The family selection emits compared, added, removed or unresolved. Non-single-head populations now use the `unresolved` wire state, not an emitted `ambiguous` literal, even when explanatory prose calls the population ambiguous. No winner or selected roster is invented. Candidate heads’ readable guarantees remain inspectable.

The leaf adds per-side failure provenance: `_entry` forces unresolved when an applicable side was unread; `_unresolved_entry` preserves that side’s reason as unreadable and marks the entry unavailable when a side was unread or no candidates could be read. This is not a known-absent counterpart or an empty successful family.

### Roster continuation and counts

Resolved selections read each chosen revision through `read_family_roster`. A supplied cursor is offered to Before, then to After only when Before did not bind it; the existing owner controls cursor admission. Without a bound continuation, a requested cursor earns that owner’s refusal instead of a fabricated next page. Exact-revision absence is distinguished from absence of the family identity itself.

`_outcome` reports membership totals by summing the supplied side totals, while `_unique_members` counts distinct invariant revision IDs actually delivered in the composed member pages. Do not promote that latter page-union calculation into a complete-roster unique census or infer that a final page contains every member. Entry state remains partial for incomplete owner pages or `content_not_on_page`, and unavailable for unreadable sides. Its `recorded` state is a context-read state, not an authored guarantee verdict.

The candidate label is preferred when its identity is readable; otherwise the baseline label is retained. Primary invariant statement/judgment/proof composition and the complete source inventory remain separate owners. Current changes add indexed failure checks and explicit unresolved/unavailable provenance; unchanged head/roster bodies do not make the whole file unchanged.

## Evidence

No domain documentation source is configured. The entire922-line current module and actual BASE diff were read; current references below prove local source behavior, not a fresh test, served-build or MEMORY grade. The complete predecessor remains historical below.

- Missing/unsupported selectors and opened-side closure use the actual entry path. [11]
- Only the union of directly discovered family identities is composed. [12]
- Outcome totals, continuation/refusal and delivered-member uniqueness are distinct calculations. [13]
- Exact-revision absence and identity absence are explained separately. [14]
- Unread scope never becomes a measured no-family zero. [15]
- Family/invariant discovery records indexed family failures and independent populations. [16]
- Independent family selection, explicit unread-side override and owner-bound rosters are composed together. [17]
- The retained head helper and current four-state family selection choose no arbitrary winner. [18]
- The shared helper sorts supplied revisions without reading predecessor edges. [19]
- Unresolved candidates retain readable guarantees and each unread side’s reason. [20]
- Labels and recorded/partial/unavailable entry states use the actual side/page content. [21]

## Historical predecessor account

The complete prior account follows as provenance with nested headings and inert prose references. Its old authored-edge/ambiguous-wire wording is superseded; it is not an additional current claim.

### mcp/src/agents_remember/application/review_family_context.py

#### Governing Overview

[application route overview](overview.md)

#### Purpose

Composes comparison-bound family context beside the primary review: directly relevant family identities, each independently selected family revision’s own guarantee, and its exact bounded member roster, including unchanged siblings.

#### Code Commentary

##### Logic

The entry point requires a bound selected subject, opens the two sides through the existing roster-side owner and closes both. A missing selection, unavailable knowledge and measured no-family remain distinct outcomes.

For an invariant identity or exact invariant revision, `_applicable_invariant` reads only the policy’s frozen direct family identity set. `_compose` unions those identities across the bound snapshots; sibling rosters do not discover additional families. `_entry` then resolves each known identity on both snapshots through `_applicable_family`. A primary member absent on one side therefore cannot erase an independently recorded family.

Family-identity composition considers every recorded revision of that family. Heads are what the
head rule establishes over the selected revisions — every retained revision is a head, so several
retained revisions are several heads. An explicitly requested family revision instead remains exact wherever recorded, with the family owner’s complete revision list retained for history. Multiple heads are not chosen by label, version or order: the selection and each candidate head’s own guarantee remain inspectable without an invented selected roster.

For a resolved pair or genuine one-sided family, `read_family_roster` supplies each selected revision’s own guarantee and exact memberships. The existing cursor is offered to before, then to after only if before did not bind it, so one continuation advances one existing walk. Partial/unreadable sides retain their reason and the roster owner’s counts; a completed multi-page walk does not imply that its final page contains all members.

The outcome counts membership rows and unique invariant revisions separately. Its supplemental context does not replace primary invariant statements, conditions, revision selection, evidence or the complete changed-source inventory. Guarantee text and mechanical source changes are not converted into semantic assessments.

##### Conventions

Keep the existing comparison, family, authored-head, roster and source/evidence owners. This module's role is documented by its own source and the concrete references below; it introduces no alternate store, selection policy or publication authority.

##### Invariants And Boundaries

- Direct invariant policy discovers family identities; independent family owners select their revision populations and heads.
- Membership absence, genuine family absence, memberless recorded families and unreadable scope are different facts.
- Retained old memberships cannot pin the family to a superseded head; exact family-revision requests remain exact.
- A family revision’s roster is its own explicitly recorded membership, never inherited.
- Multiple heads remain unchosen candidates, and no semantic guarantee verdict is inferred.
- Existing bounded continuation, primary operands and complete source inventory remain independently owned.

##### Todos

No unrelated repair is assigned to this file. Installed product evidence and historical assessment loading remain separately reported outcomes, not conclusions of these source references.

#### Evidence

##### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources below.

##### Repo-Internal References

These current owners and cases establish the stated behavior.

- Open and close the existing bound roster sides; retain named entry states. (historical reference 1)
- Discover only the union supplied by the existing direct invariant policy. (historical reference 2)
- Invariant discovery returns family identity keys, not a head-selection subset. (historical reference 3)
- Family and exact-family-revision populations come from the existing family owner. (historical reference 4)
- Resolve each discovered family independently on both snapshots, then read its own selected rosters. (historical reference 5)
- Use the existing authored-head rule and only edges inside the population. (historical reference 6)
- State genuine family or exact-revision absence, not primary membership absence. (historical reference 7)
- Preserve compared, one-sided, ambiguous and unresolved selection outcomes. (historical reference 8)
- Expose candidate heads’ own guarantees without inventing a selected roster. (historical reference 9)
- Count exact member revisions separately from repeated membership rows. (historical reference 10)

##### Cross-Repo References

No sibling repository defines this file's behavior.

No meaningful cross-repository implementation dependency.
