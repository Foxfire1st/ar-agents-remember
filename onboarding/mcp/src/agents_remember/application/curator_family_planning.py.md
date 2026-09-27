# mcp/src/agents_remember/application/curator_family_planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_family_planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T23:48:33Z |
| lastVerifiedCommitHash | `c114deaca13555f3c5121a7f5b803233b6bd866c` |
| lastVerifiedCommitDate | 2026-09-27T02:50:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

Resolves the authored family plane into exact identities and the existing family batch commands. It plans against the selected dataset and operation-local allocation journal; it does not write canonical knowledge itself.

## Code Commentary

### Logic

The allocation journal holds fresh family identity/revision pairs under the operation's retry scope. An unreadable journal refuses rather than minting over unknown progress. Existing family identities and predecessor revisions must resolve in the selected dataset, and each predecessor must belong to the named family.

`_declaration_digest` binds the family identity, display fields, guarantee and predecessors. A nonempty retention set adds sorted membership IDs and their authored bases. Reordering that set is the same request; changing the set or a basis under an allocated key is a content conflict. Absent and empty retention add no content to the existing digest.

`_retained_memberships` resolves each selected membership row to its exact predecessor-family and invariant-revision endpoints. The predecessor must be explicitly declared and belong to the same family. Unknown references and duplicate successor endpoints refuse. The new edge gets the existing deterministic membership identity derived from its new family revision and unchanged invariant revision, plus `retained_from_member_id` for reporting.

`plan_entry_family` combines the entry's own memberships with retained siblings from declarations owned by that entry, refusing duplication of its own endpoint. `family_commands` emits the existing AddFamily, AddFamilyRevision and AddFamilyMember commands only when their rows are not already stored. A retry reuses stored rows instead of issuing duplicate inserts. Explicit retirements retain the stored row digest for the existing RemoveFamilyMember command.

The candidate writer commits these plans as one admitted batch. Retention adds edges to the successor; it neither copies the predecessor roster implicitly nor creates invariant revisions for unchanged siblings.

### Conventions

Allocation keys are task-scoped; canonical family identities are not derived from keys or labels. Stored facts come from the selected dataset through the existing decoder. Membership identity is derived from exact endpoints, while guarantees have separately allocated revision identity.

### Invariants And Boundaries

- A family successor and its earlier revision remain separate recorded objects.
- Retention does not modify a stored sibling statement, scope, provenance, anchor or realization.
- References must be explicit, stored and in a declared same-family predecessor.
- Missing datasets remain distinct from datasets recording no families.
- Changed declaration content requires a new successor operation; exact retry preserves allocated identities.
- Planning produces commands; it does not create a second writer or select current heads.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| Read exact stored family and membership facts from the selected dataset. | `read_stored_family_facts` | mcp/src/agents_remember/application/curator_family_planning.py:252-299 |
| Allocate or recover a declaration and validate its stored references. | `_plan_declaration` | mcp/src/agents_remember/application/curator_family_planning.py:377-435 |
| The retry digest includes nonempty retention IDs and bases in stable order. | `_declaration_digest` | mcp/src/agents_remember/application/curator_family_planning.py:475-491 |
| Retained memberships resolve exact predecessor and invariant endpoints. | `_retained_memberships` | mcp/src/agents_remember/application/curator_family_planning.py:617-664 |
| Combine this entry’s own membership and retained sibling plans. | `plan_entry_family` | mcp/src/agents_remember/application/curator_family_planning.py:548-614 |
| Existing commands add only unstored family and membership rows. | `family_commands` | mcp/src/agents_remember/application/curator_family_planning.py:762-813 |
| A retirement uses the exact stored membership row and digest. | `_retirement_plans` | mcp/src/agents_remember/application/curator_family_planning.py:727-754 |
| Public successor behavior is exercised across separate leaf scopes. | `test_public_successor_retains_exact_siblings_and_publishes_across_leaf_scopes` | mcp/tests/test_curator_family_retention.py:147-199 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.


- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the resolution half of the curator's family plane**. The stamp basis is
  the leaf's base commit, because the module is untracked there and no commit contains what a stamp
  would otherwise claim to have verified. Two things a reader must carry away, because both were live
  defects during the leaf: **a family identity is allocated from the operation's own journal and never
  derived from the local key**, so the same key spelled by two tasks mints two families while a repeat
  of one operation finds its own pair, and the same key arriving with a *changed* guarantee is refused
  with `family_allocation_conflict` — the refusal names the successor shape rather than rewriting a
  revision an earlier membership still cites; and **the undeclared-key answer has exactly one
  implementation** (`_declarationfamily_refusal`), because a second copy in the read half answered a
  question that depends on the dataset. The unexamined case is a carried entry with nothing authored,
  never an absent entry, and a stored row contributes no command so an exact retry reports rather than
  re-inserts. No verification stamp beyond the leaf's base is advanced: the candidate is uncommitted
  and the governed closeout owns the real commit.
