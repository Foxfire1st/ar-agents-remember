# mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[queue overview](overview.md)

## Purpose

This file is the read-only adapter from per-contract atomic-series activation authority into
disposable closeout projection source facts. It gives the queue waiting reasons without granting it
selector mutation or lifecycle ownership.

## Code Commentary

### Logic

`project_series_activation(contract)` strictly observes that one series contract's own activation
record — never a shared per-source-pair slot. A valid observation returns its source fact plus zero
or one waiting reason, and the only surviving reason is `atomic-series-reconciling`: vacant and
active are never waiting states, and another master's state is never this contract's reason to wait.
A derivation/read failure becomes a bounded `ProjectionSourceProblem` with the contract or activation
address and an explicit repair through a selecting manager/start/attach operation. It never chooses a
winner, because there is no winner to choose.

### Conventions

`SeriesActivationProjection` is a frozen local carrier for source fact, waiting tuple, and optional
problem. The record it reflects is addressed by `contract_fingerprint`, the digest of the resolved
contract path, so two sprint-commanded masters that share one protected source pair hold independent
records. That holds for a graph-less sprint too: the sprint declares no dependencies, so nothing
serializes its masters and each contract's own observation reaches `active` with an empty `waiting`
tuple — the `atomic-sequential` default is the sprint's shape, not a serialization mechanism. Repair
guidance names the selecting transaction rather than an internal store edit.

### Invariants And Boundaries

- The queue observes activation; it cannot publish, release, or archive it.
- Multiple live series are valid, including several for one protected source pair; vacant and active
  are normal, not another contract's waiting reason.
- A record that is not this exact contract is refused as unreadable
  (`atomic-series-activation-contract-mismatch`), so a foreign master can never be adopted here.
- Malformed authority fails loud as a source problem; no stale row or census-order fallback exists.
- No claim, commit, certification, integration, or terminal evidence is projected here.

### Todos

Repair wording and claims are reconciled to the per-contract selector observer; verification metadata
awaits the real code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selector observation and waiting-reason derivation are owned outside the queue; the reader takes the contract and the reason is derived from the observation alone. | `observe_atomic_series`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-287 |
| The queue route is a disposable rebuild projection with task truth and lifecycle state outside it. | `## 260821-CLIVE Final Disposable Projection Route` | onboarding/mcp/src/agents_remember/worktrees/queue/overview.md:72-107 |
| Focused tests prove two masters sharing one protected source pair both project with no waiting reason, including the graph-less sprint where nothing serializes the masters. | "self.assertEqual(project_series_activation(series_a).waiting, ())" | mcp/tests/test_cross_master_concurrency.py:131-162 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-13T15:00:56+02:00 — Rebound the two-masters projection claim from the stale `126-146` range to `131-162` (the anchor `"self.assertEqual(project_series_activation(series_a).waiting, ())"` now sits at line 150; a second instance is at 523) — the earlier finding that the construct did not exist at the card's stamp no longer holds, because the two-masters case is present in this revision. Extended the claim wording and the Logic section so the graph-less sprint is covered too: nothing serializes its atomic masters and each contract's own observation reaches `active` with an empty `waiting` tuple. No verification-metadata change; no execution or acceptance claim.
- 2026-09-13T14:19+02:00 — Per-contract activation record curation: `project_series_activation` now takes only the contract and calls `activation_waiting_reason(activation)` with the observation alone, so the card no longer describes a source-pair snapshot or the "not selected / paused by another master" waiting reasons; the only surviving reason is `atomic-series-reconciling`, a foreign record is refused as `atomic-series-activation-contract-mismatch`, and the record key is `contract_fingerprint`. Rebound the observer/reason citations to atomic_series_activation.py:145-152 and :275-287 and replaced the retired source-alias test row with the two-masters-one-source-pair projection test. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound queue projection citations to the current selector observer and waiting-reason definitions; queue ownership is unchanged and no acceptance claim is made.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `AtomicSeriesActivationTests` repointed to mcp/tests/test_atomic_series_activation.py:96-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of selector observation and scoped
  invalid-empty projection behavior.

- 2026-08-26T02:55+02:00 — Drafted the activation-observer sidecar; final source freeze and
  verification remain open.
