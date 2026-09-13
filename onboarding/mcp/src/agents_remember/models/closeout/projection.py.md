# mcp/src/agents_remember/models/closeout/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `9f0309447d6820d90e59279abc84f87f1ccbb3b3`|
| lastVerifiedCommitDate |  2026-09-13T22:28:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout projection models overview](overview.md)

## Purpose

Defines strict persisted models for disposable closeout scheduling projections and task-document projection effects.

## Code Commentary

### Logic

The models bound problem/reason populations, validate valid-built versus invalid-empty state, and serialize invalidation/rebuild effects without lifecycle fields. No bound limits how many candidates a projection may carry.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Invalid projection state is empty; projection records never own claims, commits, certification, integration, or terminal lifecycle evidence.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `MAX_CLOSEOUT_SOURCE_PROBLEMS` | mcp/src/agents_remember/models/closeout/projection.py:12-15 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `MAX_CLOSEOUT_SOURCE_PROBLEMS` | mcp/src/agents_remember/models/closeout/projection.py:12-15 |
| Persisted projection state carries an unbounded `members` list beside its bounded `sourceProblems`; membership uniqueness is enforced by validator, not by a population ceiling. | `members`; `sourceProblems`; `_condition_is_exact` | mcp/src/agents_remember/models/closeout/projection.py:59-85 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `MAX_CLOSEOUT_SOURCE_PROBLEMS` | mcp/src/agents_remember/models/closeout/projection.py:12-15 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
- 2026-09-13T22:55+02:00 — L6 (260913-LCA): re-anchored the three reference rows off the deleted `MAX_CLOSEOUT_CANDIDATES` onto `MAX_CLOSEOUT_SOURCE_PROBLEMS` and corrected the Logic claim that the models bound candidate populations; the candidate ceiling was removed with its two enforcement sites.
- 2026-09-13T22:22+02:00 — L6 (260913-LCA) curation close-out of this card: added the concrete repo-internal row for `CloseoutQueueState` — `members` is now `Field(default_factory=list)` with no `max_length` while `sourceProblems` keeps `MAX_CLOSEOUT_SOURCE_PROBLEMS`, and membership stays unique by the `_condition_is_exact` validator (source `mcp/src/agents_remember/models/closeout/projection.py:59-85`). The worker's `MAX_CLOSEOUT_CANDIDATES` re-anchor and Logic correction are preserved unchanged. Source is a read-only uncommitted change set; verification metadata remains closeout-owned and no stamp advanced.
