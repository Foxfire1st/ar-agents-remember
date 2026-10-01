# mcp/src/agents_remember/application/curator_family_coverage.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Reports the family plane measured by one curator ingest run: guarantees authored or examined, exact membership outcomes, deliberate no-family decisions, and unexamined or unresolved entries. It renders planned and stored facts; it authors no semantic decision.

## Code Commentary

### Logic

`family_coverage` combines per-entry plans with the post-batch stored facts. Its states stay distinct: recorded, projected and not-recorded. Counts remain null when no post-batch measurement exists.

A guarantee's text, version and identity come from the recorded revision when available. A reused guarantee is examined; a newly declared revision is authored only when recorded and otherwise projected. A retirement also prompts examination of its affected guarantee.

For each guarantee, `unchanged_sibling_members` is the recorded roster count minus newly added non-retained member endpoints. Explicitly retained sibling revisions therefore remain in the unchanged count even though their successor membership edges are new. An exact replay reports reused edges.

Each membership outcome carries exact family/invariant revision endpoints, the membership ID, its basis and optional `retained_from_member_id`. The marker identifies the historical edge that supplied an unchanged revision; it does not change added/reused edge state. Unexamined and unresolved remain different coverage facts.

### Conventions

Coverage consumes the existing plans and the existing stored-facts reader. It does not infer success from process exit, assign semantic acceptance, or turn null counts into zero.

### Invariants And Boundaries

- Projected or not-recorded coverage is not a dataset measurement.
- A new edge and a new invariant revision are different facts.
- Retained source membership identity is reported explicitly.
- A declared no-family basis is distinct from an unexamined entry.
- A membership change does not automatically rewrite the family guarantee.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources cited below.

### Repo-Internal References

These references name the current owners and the behavior they establish.

- The membership result carries its optional retention source. [1]
- Assemble outcomes from the measured run scope. [2]
- Count unchanged sibling revisions separately from newly added non-retained endpoints. [3]
- Report exact edge state and retained source membership. [4]
- The CLI exports these facts without adding authority. [5]

### Cross-Repo References

No sibling repository defines this file's contract.

No meaningful cross-repository implementation dependency.
