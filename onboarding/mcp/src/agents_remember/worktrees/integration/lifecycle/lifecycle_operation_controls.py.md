# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Task-addressed lifecycle controls derived from durable and live evidence.

## Code Commentary

### Logic

Recovery and resume validate the retained generation, exact door, and current code/memory input. The control owner no longer classifies or refuses a ledger byte/tree contradiction, and successor admission composes only code and memory messages. Real Git and publication contradictions still flow through the owning evidence checks.

The public surface is `LifecycleControlCommand`, `control_operation`. The control seam revalidates
the configured contract and generation under lease, reconciles worker exit and control mutations,
and dispatches cancel, retry, recover, resume, retire, or supersede from durable and live evidence.
Cancel terminates the exact worker and proves cancellable Git before publishing its cancelled
outcome and waiting successor. Public closeout resume accepts the fixed candidate and fresh
message fields, then starts at the first failed or stale gate while retaining the passing prefix;
integrate and direct-landing keep their independent recovery semantics.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `_resume` checks retained generation and exact publication evidence before worker relaunch. | `_resume` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:330-367 |
| `_resume_arguments` retains the admitted code/memory messages in the successor correction. | `_resume_arguments` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:916-941 |
| `_closeout_resume_admission` combines current candidate evidence with code/memory input for resume. | `_closeout_resume_admission` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:944-980 |

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `LifecycleControlCommand`; `control_operation` as its public seam. | `LifecycleControlCommand`; `control_operation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:162-222 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## CCR-R12@v5 Current Control Boundary

Lifecycle controls now resume a refused, cancelled, or failed closeout generation under a fresh
successor lease after rechecking current messages, candidate identity, and source provenance.
Resume/recovery is a transaction-control action: it does not imply a rerun of strict code quality,
memory quality, selected certification, curator coherence, or independent review. Explicit approval
and the current contract/door evidence remain required where the operation owner requires them.

## 260821-CLIVE Task-Addressed Control Semantics

Cancel, recover, retry, resume, retire, and supersede operate on canonical door+journal authority.
Cancel stops the worker, ignores retained private preparation as an approval prerequisite, and
publishes the reset/cancelled outcome with its waiting successor after exact worker-exit and Git
proof. Public closeout resume accepts the repaired fixed candidate and starts at the first failed or
stale gate while retaining the exact passing prefix; publication still revalidates the waiting door,
projection, and authority. Integrate and direct-landing retain their independent recovery semantics.
Missing initial doors and competing declarations refuse.

## Shared Control-Action Vocabulary

`LifecycleControlAction` is owned by `models/lifecycles/operation_kinds.py` alongside the closed
operation-kind vocabulary. This control module consumes that model; it no longer declares its own
action literal/enum or imports action identity from worker-termination evidence. Request parsing,
control classification, and public responses therefore share one exhaustive action type.

## CCR-R18@v1 Rebinding Controls And Previews

260831-CCR-L18 routed the control-layer projection rewrites through the envelope binders: `_preview_completed_supersede` now returns `bind_projection_result(operation_projection(record, contract=contract), {...})` for the `would-supersede` dry-run preview, and `_resume_closeout_successor` uses `bind_projection_result` with a `LifecycleRecommendedAction` (`apply-closeout-successor` → `worktree_closeout_apply`) plus guidance instead of mutating a `model_copy` projection. Every rewritten control projection therefore rebinds its component digests to the exact journal revision through the sole validator.

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=740300b6ebb97227bd77c4f696e7a1ae9c82109f3571ef25013d1e7fe7f4a601. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `LifecycleControlCommand`, `control_operation` repointed to mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:119-135, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:165-225. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: recorded the current closeout cancel/resume path: cancel stops the worker even during private preparation and proves no publication output; resume accepts the fixed candidate and fresh message, retains the passing prefix, and reruns from the failed gate onward while integrate/direct-landing keep independent recovery semantics.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=9da7ac9d20c873b7eb2783f3fed4366f4f6f6e8d2fd6dc5f37636f0f44a6c22b; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the supersede-preview and closeout-revision rewrites moving to `bind_projection_result` with a typed `LifecycleRecommendedAction`. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-26T10:44:52+02:00 — Reconciled lifecycle controls with the centralized `LifecycleControlAction` model and removal of the local action declaration.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled all task-addressed controls with canonical door/journal ownership. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
