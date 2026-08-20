# mcp/tests/test_topology_publication_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_topology_publication_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Proves task-document edits cannot convert live work branches into protected refs or invalidate live series/leaf ownership.

## Code Commentary

Preview and apply traverse production publication guards for atomic nature removal, sprint
detachment, orphan targets, shared supers, cleaned atomic membership, live-leaf sibling/symlink
escape, and foreign-repository candidate overrides.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `TopologyPublicationAuthorityTests` | mcp/tests/test_topology_publication_authority.py:36-234 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-16T05:27+02:00 — L4 exact-review forcing: production task publication now proves
  sibling-master traversal, symlink escape, and a not-yet-written foreign-repository leaf override
  all refuse in preview and apply with task/contract bytes unchanged.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created topology publication authority forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
