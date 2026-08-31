# mcp/tests/test_non_leaf_reviewer_evidence_retention.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_non_leaf_reviewer_evidence_retention.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T08:31+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves topology-valid master and sprint reviewer reports enter bounded retention without mutating a
leaf task document.

## Code Commentary

### Logic

The suite registers non-leaf reviewer artifacts against real topology, observes TTL eviction and the
global hard cap, and verifies that task execution-registration lists remain unchanged. A direct
boundary matrix proves valid master/sprint admission, orphan and missing-source refusal, the
continued worker `task.json` refusal, and no-side-effect rejection when `task.json` falsely declares
itself a `subTask` with slug `task`.
Direct classifier forcing also rejects a non-leaf payload addressed through a leaf filename and an
impossible post-validation altitude instead of treating either as retainable evidence.

### Conventions

Retention classification is tested through the task-execution registration boundary, not by testing
the pruning helper in isolation.

### Invariants And Boundaries

- Non-leaf reviewer evidence is durable but irrelevant to leaf task mutation.
- TTL and hard-cap limits both apply.
- Malformed orphan evidence remains outside this acceptance path.
- Missing non-leaf authority blocks, and non-reviewer `task.json` references remain leaf-only refusals.
- Malformed filename/payload split-brain preserves both JSON and Markdown bytes and leaves the
  execution-registration list empty.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Master and sprint reports enter TTL without leaf mutation. | `test_master_and_sprint_reports_enter_ttl_without_task_mutation` | mcp/tests/test_non_leaf_reviewer_evidence_retention.py:109-136 |
| Reviewer-only addressing admits valid master/sprint topology and rejects orphan, missing, and worker cases. | `test_reviewer_only_non_leaf_addressing_is_fail_closed` | mcp/tests/test_non_leaf_reviewer_evidence_retention.py:138-183 |
| Non-leaf reports participate in the hard cap. | `test_master_and_sprint_reports_participate_in_the_hard_cap` | mcp/tests/test_non_leaf_reviewer_evidence_retention.py:252-279 |

## Cross-Repo References

No cross-repository implementation dependency governs this suite.

## Update History

- 2026-08-31T13:42+02:00 — A005 closeout repair covered misaddressed non-leaf payloads and the
  fail-closed unexpected-altitude classifier branch.

- 2026-08-31T08:31+02:00 — Extended the direct boundary matrix with the final review's malformed
  `kind=subTask`, `slug=task` forcing case and exact no-mutation assertions.

- 2026-08-31T08:05+02:00 — Added the direct fail-closed role/topology matrix beside the TTL and
  hard-cap forcing cases.

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
