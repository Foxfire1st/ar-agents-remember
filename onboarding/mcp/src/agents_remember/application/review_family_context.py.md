# mcp/src/agents_remember/application/review_family_context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_family_context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T02:21:35Z |
| lastVerifiedCommitHash | `c8d6ebe2289731c7693eb890b806a2f3490f3e97` |
| lastVerifiedCommitDate | 2026-09-27T04:55:05+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources below. | — | — |

## Repo-Internal References

These current owners and cases establish the stated behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| Open and close the existing bound roster sides; retain named entry states. | `review_family_context` | mcp/src/agents_remember/application/review_family_context.py:245-292 |
| Discover only the union supplied by the existing direct invariant policy. | `_compose` | mcp/src/agents_remember/application/review_family_context.py:295-330 |
| Invariant discovery returns family identity keys, not a head-selection subset. | `_applicable_invariant` | mcp/src/agents_remember/application/review_family_context.py:545-566 |
| Family and exact-family-revision populations come from the existing family owner. | `_applicable_family` | mcp/src/agents_remember/application/review_family_context.py:518-542 |
| Resolve each discovered family independently on both snapshots, then read its own selected rosters. | `_entry` | mcp/src/agents_remember/application/review_family_context.py:572-635 |
| Use the existing authored-head rule and only edges inside the population. | `_heads` | mcp/src/agents_remember/application/review_family_context.py:654-659 |
| State genuine family or exact-revision absence, not primary membership absence. | `_not_recorded_detail` | mcp/src/agents_remember/application/review_family_context.py:423-440 |
| Preserve compared, one-sided, ambiguous and unresolved selection outcomes. | `_selection` | mcp/src/agents_remember/application/review_family_context.py:677-722 |
| Expose candidate heads’ own guarantees without inventing a selected roster. | `_unresolved_entry` | mcp/src/agents_remember/application/review_family_context.py:797-822 |
| Count exact member revisions separately from repeated membership rows. | `_unique_members` | mcp/src/agents_remember/application/review_family_context.py:374-384 |

## Cross-Repo References

No sibling repository defines this file's behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-27T02:21:35Z — L40: Corrected the obsolete membership-based family selection axis to identity-only discovery followed by independent two-sided family composition. Earlier implementation/history remains attributable; this is the accepted R31 correction, not a new retrieval policy. Existing verification stamps and all prior history are preserved; working-source provenance is retained in task notes and actual commit stamping remains closeout-owned.


- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the composition `ICR-R31@v1` introduced as **the comparison-bound family review context**. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records what a consumer has to act on, including the leaf's one real defect and its fix, because a reader who takes only the shape away would repeat it: **a family selection's revision population is the family owner's own revision list and never a membership-derived one** (`_applicable_family`), since a family revision that cites no member is still a revision of its family — deriving the population from membership-bearing rows made the canonical memberless-successor shape look like a `compared` pair naming the superseded revision, printed `0 other recorded revision(s)` while the store recorded more, and rendered a guarantee-bearing memberless family as `no_family_recorded` with its guarantee dropped. The history sentence now measures the family owner on both snapshots and de-duplicates a revision both retain (`_selection_sentence`), the rejected-selection sentence names the axis it was made on, and several legitimate heads stay several with every head carried as an inspectable candidate and no guarantee presented as the family's own. Continuation remains one roster walk of one snapshot, served for the first page of every other family context.
