# mcp/tests/test_topology_publication_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_topology_publication_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:50+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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
| The focused suite owns this task-publication independence boundary. | `TopologyPublicationIndependenceTests` | mcp/tests/test_topology_publication_authority.py:42-335 |

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned topology-authority suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces task publication independence from landing serialization, live enclosure state, claimed operations, and queue projection state.

### Current Invariants

- Every intrinsically valid topology mutation publishes task truth.
- Landing/ref authority may protect its own mutation edge but cannot veto task authoring.
- Active or malformed source-pair activation cannot veto an otherwise valid task edit and is not
  healed/replaced by the task-doc tool.

## Update History

- 2026-08-26T08:50+02:00 — Rebound the suite-class reference to the frozen
  `TopologyPublicationIndependenceTests` owner.

- 2026-08-26T08:45+02:00 — Normalized the Docs heading and restored the canonical Cross-Repo
  reference section for this changed topology-publication suite card.

- 2026-08-26T03:37+02:00 — Added direct proof that active then deliberately malformed activation
  evidence neither blocks task authoring nor gets rewritten by it. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-16T05:27+02:00 — L4 exact-review forcing: production task publication now proves
  sibling-master traversal, symlink escape, and a not-yet-written foreign-repository leaf override
  all refuse in preview and apply with task/contract bytes unchanged.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created topology publication authority forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
