# mcp/src/agents_remember/application/curator_family_authoring.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Reads the curator-authored family plane before dataset planning. It distinguishes explicit membership, deliberate no-family with a basis, and unexamined coverage. Family guarantees remain independent authored statements; directories, labels and shared anchors never create a family.

## Code Commentary

### Logic

A membership either declares a guarantee, joins a local declared key, or names a stored family revision. Declaring and naming a stored revision together refuses. Local keys must be declared once; the dataset-dependent existence check belongs to the planner.

A successor declaration may carry `retain_memberships`, a list of exact stored membership UUIDs and nonblank authored bases. `FamilyMemberRetention` represents one reference. The parser requires exactly `member_id` and `basis`, rejects malformed or repeated IDs, and treats absence as an empty set. It does not resolve the membership or infer predecessor contents.

After per-entry parsing and declaration validation, `read_family_plane` removes refused assignments and declarations before selecting conflicts. Those entries keep their original refusal and contribute no retention or retirement effect. `_retention_conflicts` then rejects participating eligible entries when the same source membership is both retained and retired, including across entries. This preserves historical membership without blocking unrelated valid authoring or ordinary eligible retirement.

The parser reads family and predecessor identities but never allocates or writes them. A no-family basis is retained as a bounded condition on the invariant; an omitted family decision remains unexamined.

### Conventions

Typed frozen values carry the parsed vocabulary. Refusals are attached to the responsible entry and bounded by the shared model limits. The store, candidate and command vocabulary remain outside this parser.

### Invariants And Boundaries

- The producer's fields are not reinterpreted as family decisions; the curator authors the family plane.
- Guarantee text is independent of member statements. An entry can have multiple memberships.
- Retention is explicit and names stored membership identities; no roster is inherited.
- A retained historical membership cannot also be retired by this handoff.
- Missing family decisions are not deliberate no-family outcomes.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources cited below.

### Repo-Internal References

These references name the current owners and the behavior they establish.

- One retained membership reference carries its exact ID and authored basis. [1]
- A declaration carries the optional retention set beside its family identity and predecessors. [2]
- Read entry decisions and reject list-level declaration and retention conflicts. [3]
- Retain/retire conflicts are detected across entries. [4]
- Parse only exact membership IDs with nonblank bases and reject duplicate IDs. [5]
- Deliberate no-family is a distinct, justified outcome. [6]
- Member decisions may place or retire exact memberships. [7]
- Stored references resolve against the selected dataset in the planner. [8]

### Cross-Repo References

No sibling repository defines this file's contract.

No meaningful cross-repository implementation dependency.
