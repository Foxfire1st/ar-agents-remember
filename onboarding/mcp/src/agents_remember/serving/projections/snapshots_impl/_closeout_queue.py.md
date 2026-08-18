# mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py

| Field                  | Value                                                                        |
| ---------------------- | ---------------------------------------------------------------------------- |
| repository             | agents-remember                                                              |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py` |
| doc_type               | `file-level-onboarding`                                                      |
| lastUpdated            | 2026-08-18T00:00+02:00                                                       |
| lastVerifiedCommitHash | `2597ff98306ba7c7963005092ac597c4972e63ce`                                   |
| lastVerifiedCommitDate | 2026-08-18T15:45:32+02:00|
| governingOverview      | `../overview.md`                                                             |

## Governing Overview

[../overview.md](../overview.md)

## Purpose

Read-only serving-projection reader (L8 surface 14) that exposes the authoritative closeout queue to
the dashboard. It reads each sprint master's durable `closeout-candidates.json` artifact and projects
candidate states, grades, waiting reasons, the active atomic blocker, and the graph revision — never
re-deriving scheduling facts from task titles, numbering, labels, or open terminals. It does not re-run
the queue's contract/source/ledger revalidation; that is the queue tool's declaration-time job.

## Code Commentary

### Logic

`read_closeout_queues(coordination_root, now)` iterates task-document payloads, keeps masters with an
`executionGraph`, and projects each one's queue artifact. `_project_queue` parses the `CloseoutQueueState`
JSON, builds an `AtomicBlockerNode` when an active blocker is held, and maps each candidate via
`_candidate_node` (which derives the recorded `explicit-grade-required` and `atomic-blocker-held-by`
reasons from the artifact alone).

### Invariants And Boundaries

- Strictly read-only: it never mutates the queue, contracts, or task documents.
- Candidate facts are projected verbatim; the dashboard never infers readiness from labels.
- A missing or invalid queue artifact yields no queue node (the sprint is simply not projected).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Top-level reader keeps sprint masters with an execution graph. | `read_closeout_queues` | mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py:31-51 |
| Queue artifact parsed into candidate and blocker nodes. | `_project_queue` | mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py:52-80 |
| Candidate reasons derived from grade and blocker state. | `_candidate_node` | mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py:83-95 |

## Update History

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the read-only closeout-queue serving projection.
  Verification metadata pinned until closeout stamps the L8 commit.
