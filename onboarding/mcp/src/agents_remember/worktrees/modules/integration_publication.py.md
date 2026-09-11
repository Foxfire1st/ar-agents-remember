# mcp/src/agents_remember/worktrees/modules/integration_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/integration_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T12:02+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Carries typed preflight state from integration planning into the irreversible publication step.

## CCR-R12@v5 Current Transaction Boundary

`IntegratePreview` and `IntegrationPublication` carry the source-pair, completion, handover, and
ref-safety facts that publication must recheck. They do not carry a planned normal-operation
quality gate or certification result. Integration applies the prepared pair with the existing
authority and compare-and-swap/ref-publication controls; full suites remain an explicit developer
request.

## Code Commentary

### Logic

`IntegratePreview` holds the evaluated seam guard and optional handover warning. `IntegrationPublication`
bundles every preflight fact the protected publication must re-verify: the contract, worktree args,
locked args, integration sources, integrated commits, and the handover warning.

The closeout-door cut (commit `fad9808e`) removed two members from this module: the
`intent: IntegrationPublicationIntent` field and the `publish_journaled_organizational_completion`
helper that consumed it. Integration no longer builds or publishes a completion intent, so this module
no longer imports `organizational_completion` and no longer publishes a master task document.

### Invariants And Boundaries

- These are dependency-light value types; each has exactly one implementation owner and is imported directly by `integrate.py`.
- No compatibility shim or implicit fallback exists.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Evaluated seam guard and planned quality gate for preview. | `IntegratePreview` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:16-21 |
| Every preflight fact the irreversible publication re-verifies. | `IntegrationPublication` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:24-33 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams are `IntegratePreview` and `IntegrationPublication` — two frozen value types
and nothing else. The `protected_integration_decision` seam named by the original L2 reconciliation
exists nowhere in the tree (the closeout-door cut removed it), and the same cut removed
`IntegrationPublication`'s `intent` field. Integration still transfers authority from the
waiting-door projection into the journal, revalidates configured contract and protected refs at the
mutation boundary, and records publication evidence; source-ref movement must reconcile or complete
the same generation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes two value types at this ownership boundary — `IntegratePreview` and `IntegrationPublication`. The earlier `protected_integration_decision` no longer exists anywhere in the tree, so the reconciliation that named it is superseded; the closeout-door cut (`fad9808e`) also removed `IntegrationPublication`'s `intent` field. | `IntegratePreview`; `IntegrationPublication` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:16-21; mcp/src/agents_remember/worktrees/modules/integration_publication.py:24-33 |

## Update History
- 2026-09-11T23:25:00+00:00: Completed the narrative pass the row repair left owed: the dated L2 section now states the two current seams and records that `protected_integration_decision` and `IntegrationPublication.intent` were removed, instead of describing the superseded three-seam snapshot. Content change, not a range repoint.
- 2026-09-11T23:05:00+00:00: The 260821-CLIVE-L2 reconciliation row claimed the module exposed `IntegratePreview`, `IntegrationPublication`, and `protected_integration_decision`, and cited three ranges that now run past a 33-line file. `protected_integration_decision` exists nowhere in the tree (the closeout-door cut removed the protected-decision seam) and the module now declares exactly two frozen dataclasses, so the row was rewritten as negative knowledge and repointed to their current definitions. The dated narrative above the table still describes the L2 snapshot and was left as history.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `IntegratePreview` repointed to mcp/src/agents_remember/worktrees/modules/integration_publication.py:16-21. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `IntegrationPublication` repointed to mcp/src/agents_remember/worktrees/modules/integration_publication.py:24-33. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that `IntegrationPublication` lost its `intent: IntegrationPublicationIntent` field, that `publish_journaled_organizational_completion` was deleted, and that the module is now imported only by `integrate.py`. Dropped the preflight organizational-completion presence from the bundled-facts claim. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `IntegrationPublication` repointed to mcp/src/agents_remember/worktrees/modules/integration_publication.py:37-47. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the integration publication typed state.
