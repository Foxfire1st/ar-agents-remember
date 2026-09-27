# mcp/src/agents_remember/application/curator_family_authoring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_family_authoring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T00:16:25Z |
| lastVerifiedCommitHash | `c114deaca13555f3c5121a7f5b803233b6bd866c` |
| lastVerifiedCommitDate | 2026-09-27T02:50:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| One retained membership reference carries its exact ID and authored basis. | `FamilyMemberRetention` | mcp/src/agents_remember/application/curator_family_authoring.py:97-102 |
| A declaration carries the optional retention set beside its family identity and predecessors. | `FamilyGuarantee` | mcp/src/agents_remember/application/curator_family_authoring.py:105-122 |
| Read entry decisions and reject list-level declaration and retention conflicts. | `read_family_plane` | mcp/src/agents_remember/application/curator_family_authoring.py:184-225 |
| Retain/retire conflicts are detected across entries. | `_retention_conflicts` | mcp/src/agents_remember/application/curator_family_authoring.py:228-249 |
| Parse only exact membership IDs with nonblank bases and reject duplicate IDs. | `_read_retained_memberships` | mcp/src/agents_remember/application/curator_family_authoring.py:462-496 |
| Deliberate no-family is a distinct, justified outcome. | `_absent_assignment` | mcp/src/agents_remember/application/curator_family_authoring.py:276-296 |
| Member decisions may place or retire exact memberships. | `_member_assignment` | mcp/src/agents_remember/application/curator_family_authoring.py:299-341 |
| Stored references resolve against the selected dataset in the planner. | `_retained_memberships` | mcp/src/agents_remember/application/curator_family_planning.py:617-664 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-27T00:16:25Z — L39 W2: Reconciled the eligible-effect boundary and original-refusal preservation against the corrected frozen owner. W1 history remains; this is not a new invariant derived from the historical defect.


- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.

- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the family-authoring owner's cases moved to the extracted sibling (D54).** No behaviour of this owner changed; the test module that covered it was split and the module docstring/case names follow. **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the curator's authored family plane**. The stamp basis is honest rather
  than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the
  leaf's base commit and the verified basis is the working-tree delta on top of it — no commit contains
  what a stamp would otherwise claim to have verified. What a reader has to carry away is the **three
  outcomes the plane keeps apart**: an entry placed in families, an entry with a *deliberate* no-family
  outcome recorded with its basis, and an entry the curator never examined — the last being neither of
  the first two, and never reported as an empty family. The reading half also states the boundary a
  reader is most likely to misplace: whether a membership that names no declaration still resolves is
  **not** decided here, because only the candidate knows whether the stored revision exists, so it is
  answered once by `curator_family_planning.plan_entry_family`. No verification stamp beyond the leaf's
  base is advanced: the candidate is uncommitted and the governed closeout owns the real commit.
