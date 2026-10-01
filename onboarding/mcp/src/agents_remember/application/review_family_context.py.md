# mcp/src/agents_remember/application/review_family_context.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Composes comparison-bound family context beside the primary review: directly relevant family identities, each independently selected family revision’s own guarantee, and its exact bounded member roster, including unchanged siblings.

## Code Commentary

### Logic

The entry point requires a bound selected subject, opens the two sides through the existing roster-side owner and closes both. A missing selection, unavailable knowledge and measured no-family remain distinct outcomes.

For an invariant identity or exact invariant revision, `_applicable_invariant` reads only the policy’s frozen direct family identity set. `_compose` unions those identities across the bound snapshots; sibling rosters do not discover additional families. `_entry` then resolves each known identity on both snapshots through `_applicable_family`. A primary member absent on one side therefore cannot erase an independently recorded family or restrict its heads to a historical membership-bearing predecessor.

Family-identity composition considers every recorded revision of that family. `_heads` delegates to the existing authored predecessor/head rule. An explicitly requested family revision instead remains exact wherever recorded, with the family owner’s complete revision list retained for history. Competing or unresolved heads are not chosen by label, version or order: the selection and each candidate head’s own guarantee remain inspectable without an invented selected roster.

For a resolved pair or genuine one-sided family, `read_family_roster` supplies each selected revision’s own guarantee and exact memberships. The existing cursor is offered to before, then to after only if before did not bind it, so one continuation advances one existing walk. Partial/unreadable sides retain their reason and the roster owner’s counts; a completed multi-page walk does not imply that its final page contains all members.

The outcome counts membership rows and unique invariant revisions separately. Its supplemental context does not replace primary invariant statements, conditions, revision selection, evidence or the complete changed-source inventory. Guarantee text and mechanical source changes are not converted into semantic assessments.

### Conventions

Keep the existing comparison, family, authored-head, roster and source/evidence owners. This module's role is documented by its own source and the concrete references below; it introduces no alternate store, selection policy or publication authority.

### Invariants And Boundaries

- Direct invariant policy discovers family identities; independent family owners select their revision populations and heads.
- Membership absence, genuine family absence, memberless recorded families and unreadable scope are different facts.
- Retained old memberships cannot pin the family to a superseded head; exact family-revision requests remain exact.
- A family revision’s roster is its own explicitly recorded membership, never inherited from a predecessor.
- Ambiguous heads remain unresolved candidates, and no semantic guarantee verdict is inferred.
- Existing bounded continuation, primary operands and complete source inventory remain independently owned.

### Todos

No unrelated repair is assigned to this file. Installed product evidence and historical assessment loading remain separately reported outcomes, not conclusions of these source references.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources below.

### Repo-Internal References

These current owners and cases establish the stated behavior.

- Open and close the existing bound roster sides; retain named entry states. [1]
- Discover only the union supplied by the existing direct invariant policy. [2]
- Invariant discovery returns family identity keys, not a head-selection subset. [3]
- Family and exact-family-revision populations come from the existing family owner. [4]
- Resolve each discovered family independently on both snapshots, then read its own selected rosters. [5]
- Use the existing authored-head rule and only edges inside the population. [6]
- State genuine family or exact-revision absence, not primary membership absence. [7]
- Preserve compared, one-sided, ambiguous and unresolved selection outcomes. [8]
- Expose candidate heads’ own guarantees without inventing a selected roster. [9]
- Count exact member revisions separately from repeated membership rows. [10]

### Cross-Repo References

No sibling repository defines this file's behavior.

No meaningful cross-repository implementation dependency.
