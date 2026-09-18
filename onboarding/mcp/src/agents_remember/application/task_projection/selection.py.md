# mcp/src/agents_remember/application/task_projection/selection.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/selection.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[application overview](../overview.md)

## Purpose

The explicit projection read plan: how much a bound seat reads, and which channels it gets. This
module is the single place where "a worker must not receive the sprint's whole decision history"
is encoded as declared data rather than as a filter applied after loading everything.

## Code Commentary

### Logic

Two declared tables carry the whole decision:

- **`_READ_ALTITUDES`** is keyed by `(own altitude, parent bucket)` and is **total** over the nine
  pairs, so there is no default branch and no pair that silently falls back to a wider read. The
  `_PARENT_BUCKETS` vocabulary is `master`/`sprint`/`none`, where `none` covers a standalone leaf,
  a standalone master and every sprint.
- **`_OPERATION_CHANNELS`** maps each of the eight frozen `CapsuleOperation` members to the channel
  set that operation's projection carries. `operation_channels` **raises**
  `projection-operation-unsupported` for an unknown operation rather than returning an empty tuple:
  an operation with no channels would be indistinguishable from a seat with no obligations.

One rule is load-bearing and must not be relaxed: **a leaf-altitude seat never reads a
sprint-altitude ancestor.** A leaf reads its own document plus its immediate parent when that parent
is a **master**; when the immediate parent is a sprint, the leaf reads its own document only and the
sprint is reached by expansion reference instead. Ancestor decision logs are *referenced with their
entry count* — never injected — so "the smallest complete task projection" cannot become "the whole
series".

`_PORTFOLIO_FACTS` says whether a seat admits its own document's portfolio facts (a sprint's
commanded masters, seats and execution topology, or a master's series index). A leaf never does.
`read_plan` then removes the `portfolio` channel from any seat that is not entitled to it, so a
declared channel and an admitted channel are separate facts.

`_LAUNCHER_CHANNELS` is the launcher seat's whole projection — `objective` and `scope` only. The
ambient launcher is a **seat kind, not a tenth role**: it carries no decision history, no
preservation dossier and no handoff obligation it does not have.

### Invariants And Boundaries

- `_READ_ALTITUDES` must stay total over `(altitude, bucket)`. Adding a "convenient" extra read
  there breaks the altitude rule; seeded mutations `M01`/`M03` in the leaf's falsifiability probe
  target exactly that.
- A leaf never reads a sprint ancestor. This is a structural property of the table, not a runtime
  filter — do not replace it with one.
- `_OPERATION_CHANNELS` has exactly one entry per member of `CAPSULE_OPERATIONS`. A new operation
  in the frozen vocabulary without a channel set is a refusal, not an empty projection.
- The `portfolio` channel is filtered by `_PORTFOLIO_FACTS`, never by the operation table alone.
- `read_plan` takes no defaults for `altitude` or `operation`; a caller must state the binding.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The two tables, the refusal that guards the operation vocabulary, and the enforcement point that
consumes the plan.

| Finding | Anchor | Source |
| --- | --- | --- |
| The total altitude table — the load-bearing rule that a leaf never reads a sprint. | `_READ_ALTITUDES`; `_PARENT_BUCKETS` | mcp/src/agents_remember/application/task_projection/selection.py:49-62; mcp/src/agents_remember/application/task_projection/selection.py:44-44 |
| Who admits portfolio facts, and the launcher's thin channel set. | `_PORTFOLIO_FACTS`; `_SEAT_KIND_CHANNELS` | mcp/src/agents_remember/application/task_projection/selection.py:88-95; mcp/src/agents_remember/application/task_projection/selection.py:100-103 |
| The per-operation channel table and the refusal that guards it. | `_OPERATION_CHANNELS`; `operation_channels` | mcp/src/agents_remember/application/task_projection/selection.py:77-112; mcp/src/agents_remember/application/task_projection/selection.py:114-133; mcp/src/agents_remember/application/task_projection/selection.py:149-168 |
| The plan builder that resolves the plan with no default branch. | `read_plan` | mcp/src/agents_remember/application/task_projection/selection.py:175-197 |
| The frozen operation and role vocabularies this table must cover exactly. | `CAPSULE_OPERATIONS`; `CAPSULE_ROLES` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:77-86; mcp/src/agents_remember/models/role_capsules/vocabulary.py:64-74; mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-108 |
| The single enforcement point that hands the projection only the planned documents. | `read_documents`; `referenced_documents` | mcp/src/agents_remember/application/task_projection/scope.py:376-391; mcp/src/agents_remember/application/task_projection/scope.py:394-405; mcp/src/agents_remember/application/task_projection/scope.py:420-435; mcp/src/agents_remember/application/task_projection/scope.py:438-449 |
| The case that proves sprint history reaches an orchestrator but never a leaf. | `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` | mcp/tests/test_task_projection.py:716-766 |
| The case that proves each frozen operation selects its own channels and its own document. | `test_each_frozen_operation_selects_its_own_channels_and_its_own_document` | mcp/tests/test_task_projection.py:774-794 |

## Cross-Repo References

No sibling-repository contract consumes this read plan.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `read_plan` repointed to mcp/src/agents_remember/application/task_projection/selection.py:175-197. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` repointed to mcp/tests/test_task_projection.py:716-766. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_each_frozen_operation_selects_its_own_channels_and_its_own_document` repointed to mcp/tests/test_task_projection.py:774-794. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the read-plan module of
  the task-context projection added by the scoped-task-context leaf (`CAPS-R03@v1`). Records both
  declared tables, the total-over-nine-pairs property, the load-bearing "a leaf never reads a
  sprint ancestor" rule, the refusal for an operation with no channel set, the launcher's thin
  channel set, and the enforcement point in `scope.py` that makes the plan binding rather than
  advisory. Verification metadata is left at the leaf base commit because the source is
  uncommitted — the governed closeout stamps the real code commit.
