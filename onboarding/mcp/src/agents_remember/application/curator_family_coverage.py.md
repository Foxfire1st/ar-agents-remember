# mcp/src/agents_remember/application/curator_family_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_family_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T23:48:33Z |
| lastVerifiedCommitHash | `c114deaca13555f3c5121a7f5b803233b6bd866c` |
| lastVerifiedCommitDate | 2026-09-27T02:50:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| The membership result carries its optional retention source. | `MembershipOutcome` | mcp/src/agents_remember/application/curator_family_coverage.py:56-67 |
| Assemble outcomes from the measured run scope. | `family_coverage` | mcp/src/agents_remember/application/curator_family_coverage.py:117-157 |
| Count unchanged sibling revisions separately from newly added non-retained endpoints. | `_guarantee_outcomes` | mcp/src/agents_remember/application/curator_family_coverage.py:160-229 |
| Report exact edge state and retained source membership. | `_membership_outcome` | mcp/src/agents_remember/application/curator_family_coverage.py:269-279 |
| The CLI exports these facts without adding authority. | `_family_block` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:131-181 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.


- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the family plane's report half**. The stamp basis is the leaf's base
  commit, because the module is untracked there. The thing a reader must not lose: the coverage is
  assembled from **what the run measured**, so `recorded` means the batch committed and every count was
  read back from the candidate, `projected` means a planning run wrote nothing, and `not-recorded` names
  the run that wrote no family row — and a run that did not commit reports `None` for the two member
  counts rather than a zero that would read as a measured empty family. `unexamined` (a committed entry
  the curator authored no decision for) and `unresolved` (an entry whose outcome the run could not
  establish) are different facts and stay in different tuples. No verification stamp beyond the leaf's
  base is advanced: the candidate is uncommitted and the governed closeout owns the real commit.
