# mcp/src/agents_remember/application/curator_family_planning.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources cited below.

### Repo-Internal References

These references name the current owners and the behavior they establish.

- Read exact stored family and membership facts from the selected dataset. [1]
- Allocate or recover a declaration and validate its stored references. [2]
- The retry digest includes nonempty retention IDs and bases in stable order. [3]
- Retained memberships resolve exact predecessor and invariant endpoints. [4]
- Combine this entry’s own membership and retained sibling plans. [5]
- Existing commands add only unstored family and membership rows. [6]
- A retirement uses the exact stored membership row and digest. [7]
- Public successor behavior is exercised across separate leaf scopes. [8]

### Cross-Repo References

No sibling repository defines this file's contract.

No meaningful cross-repository implementation dependency.
