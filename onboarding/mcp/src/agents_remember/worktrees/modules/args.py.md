# mcp/src/agents_remember/worktrees/modules/args.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/args.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview      | `overview.md`                              |

## Purpose

Defines the typed cross-layer DTO that carries worktree operation inputs from
the MCP application entry points and the worktree CLI into the worktree domain functions.
`WorktreeArgs` replaces the loosely typed `argparse.Namespace` that previously
flowed across those layers (F17), giving every layer a single explicit field set
to read and write.

## Code Commentary

`WorktreeArgs` now carries an optional `quality_certification` field for the organizational full-gate proof, and (CCR-R22@v1, L22, commit `685f83c44055`) the optional `certification_profile: Path | None` field: the configured repository-relative certification profile reference forwarded by the application entry points and lifecycle worker into closeout/integration, which the quality gate resolves and admits before any code commit.

L23 adds worker-injected operation fingerprint, candidate-tree, and progress callback fields to `WorktreeArgs`; CLI namespaces cannot populate these plane-owned controls.

`WorktreeArgs` is a `@dataclass(frozen=True)`. Every field carries a default, so
any operation can construct just the subset it needs without supplying the rest;
fields are grouped by concern (coordination/repository resolution, start inputs,
provider setup, lifecycle flags, and closeout/integrate commit messages). The
frozen dataclass means callers that need a variant produce a new instance rather
than mutating an existing one.

`from_namespace` builds an instance from an `argparse.Namespace`, falling back to
the field defaults. It iterates the dataclass `fields`, copies only attributes
the namespace actually defines (`hasattr` guard), and applies them onto a default
instance via `replace`. This tolerates argparse subparsers that only populate the
arguments they declare and tests that construct partial namespaces, so any field
the namespace omits keeps its dataclass default rather than raising.

`retry_provider_setup: bool = False` (GitHub #53): on an existing contract,
worktree start relaunches background provider setup instead of attaching;
refused while a live setup heartbeat exists.

`stale_base_choice: str | None = None` (GitHub #54): the stale-base preflight
recovery selector for worktree start — `fast-forward` (ff stale local source
branches, then proceed) or `proceed-stale` (explicit override); `None` means
block when a source branch is behind/diverged from its upstream.

`memory_sync_choice: MemorySyncChoice | None` narrows the admitted memory plan to
`merge-memory` or `skip-memory`. `resolution_action: SyncResolutionAction | None` narrows recovery
control to `continue` or `cancel`. Both aliases are owned by the public worktree model and travel
unchanged through application/registration/CLI adapters. The transaction journals the admitted
memory choice; a later continue/cancel addresses the same contract generation and cannot silently
change it.

`lifecycle_id: str = ""` (slice 2c): the observable-lifecycle id the application entry point
resolves (the active lifecycle's id, or a fresh mint when none is active) and
threads through to `_build_start_contract`, which stamps it into the contract's
`lifecycle:` block — the durable resume anchor.

`gate_policy: GatePolicy = DEFAULT_GATE_POLICY` (260703-L4) is the parsed
server-side gate delegation policy threaded from MCP config into worktree
closeout. Existing CLI/tests that omit it keep the all-human default.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public sync choice and resolution-action vocabularies are owned once by the worktree model. | `MemorySyncChoice`; `SyncResolutionAction` | mcp/src/agents_remember/models/worktree.py:57-58 |
| Provider setup config is typed through the companion worktree models module. | `WorktreeProviderSetupConfig` | mcp/src/agents_remember/worktrees/modules/models.py:36-43 |
| Worktree CLI builds argparse namespaces that this DTO adapts via `from_namespace`. | `build_parser` | mcp/src/agents_remember/worktrees/modules/cli.py:136-194 |
| Gate delegation policy model (kernel-owned since L9). | "class GatePolicy:"; "DEFAULT_GATE_POLICY = GatePolicy()" | mcp/src/agents_remember/kernel/primitives/gate_policy.py:54-54; mcp/src/agents_remember/kernel/primitives/gate_policy.py:66-66 |

## Series-Contract Notes

`WorktreeArgs` carries `parent_task` and `leaf_id` through CLI, MCP, and source API entrypoints, giving all operations the same active-task and leaf-selection inputs.

## L23 Final Candidate Disposition

The internal worktree argument DTO carries accepted candidate, task contract, and operation-progress
facts between modules. Public callers still address the canonical task and never supply private
operation, process, lease, or approval identifiers.

## 260821-CLIVE-L1 Internal Transport

`WorktreeArgs` no longer carries raw code and memory closeout message strings. Closeout execution receives one optional `EffectiveCloseoutInput`, populated only after validation; the remaining `ledger_commit_message` belongs to integration, not closeout. This prevents worker, preview, recovery, and commit code from independently normalizing or defaulting closeout subjects.

## 260821-CLIVE-L2 Current Contract

The current source seams include `WorktreeArgs`, `report_operation_progress`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `WorktreeArgs`, `report_operation_progress` at this ownership boundary. | `WorktreeArgs`; `report_operation_progress` | mcp/src/agents_remember/worktrees/modules/args.py:31-105; mcp/src/agents_remember/worktrees/modules/args.py:108-111 |

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the new optional certification_profile field on WorktreeArgs carrying the repository-owned profile reference into closeout/integration.


- 2026-08-26T03:37+02:00 — Narrowed sync inputs to shared `MemorySyncChoice` and
  `SyncResolutionAction` aliases and documented contract-addressed continue/cancel. Verification
  remains post-Dagger/closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.
- 2026-08-17T12:35+02:00 — 260815-DAG-L5: added the optional integration `quality_certification` field to worktree arguments. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added the optional integration `quality_certification` field to worktree arguments. Verification remains closeout-owned.

- 2026-08-14T06:36+02:00 — L23 final candidate review: internal worktree arguments carry operation
  progress and accepted-candidate evidence while public tool inputs remain task-addressed.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 3 worktree-argument reference claims with exact model, CLI, and gate-policy anchors; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.

- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.

- 2026-07-04T12:32+02:00 — 260703-L4: `WorktreeArgs` now carries
  `gate_policy`, defaulting to all-human, so closeout preview/apply consumes the
  trusted MCP gate delegation policy. Verification metadata pinned until closeout
  stamps the L4 commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `WorktreeArgs` now includes `parent_task` and `leaf_id` so all worktree operations can resolve nested active task roots and specific leaf enclosures without filesystem paths. Verification metadata pinned until closeout stamps the code commit.

- 2026-06-13T18:45+02:00 — Slice 2c: added `lifecycle_id: str = ""` (the observable-lifecycle enclosure anchor the controller resolves and `_build_start_contract` stamps into the contract). Verification metadata pinned until closeout stamps the 2c code commit.

- 2026-06-10T09:56+02:00 — Added `memory_sync_choice: str | None = None` (GitHub #54 sub-task D worktree_sync recovery selector).

- 2026-06-10T09:30+02:00 — Added `stale_base_choice: str | None = None` (GitHub #54 stale-base preflight recovery selector).

- 2026-06-10T07:30+02:00 — Added `retry_provider_setup: bool = False` (GitHub #53): on an existing contract, worktree start relaunches background provider setup instead of attaching; refused while a live setup heartbeat exists.

- 2026-06-01T20:45+02:00 — `WorktreeArgs` gained `force` and `teardown_providers` for the abandon/cleanup teardown path.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.

## Governing Overview

[governing overview](overview.md)
## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.