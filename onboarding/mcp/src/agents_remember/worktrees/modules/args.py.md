# mcp/src/agents_remember/worktrees/modules/args.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/args.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-20T06:22+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l40-ar`, uncommitted; base `f79f4db745ad00b908d6ce4871d0b4ab2320207c` |
| lastVerifiedCommitHash | `74c6c693b8c5a5863ce15f016793192931f4adc1` |
| lastVerifiedCommitDate | 2026-09-20T06:22:08+02:00|
| governingOverview | `overview.md` |

## Purpose

Defines the typed cross-layer DTO that carries worktree operation inputs from
the MCP application entry points and the worktree CLI into the worktree domain functions.
`WorktreeArgs` replaces the loosely typed `argparse.Namespace` that previously
flowed across those layers (F17), giving every layer a single explicit field set
to read and write.

## Code Commentary

### Logic

The internal transport carries one normalized code/memory closeout input and the actual landed code/memory-content commits. Integration has no separate ledger commit message, and PR landing has no ledger commit argument. Consumer-cache data never enters the Git output tuple.

`WorktreeArgs` now carries an optional `quality_certification` field for the organizational full-gate proof, and (CCR-R22@v1, L22, commit `685f83c44055`) the optional `certification_profile: Path | None` field: the configured repository-relative certification profile reference forwarded by the application entry points and lifecycle worker into closeout/integration, which the quality gate resolves and admits before any code commit.

L23 adds worker-injected operation fingerprint, candidate-tree, and progress callback fields to `WorktreeArgs`; CLI namespaces cannot populate these plane-owned controls.

**L40 adds the one decided input this DTO carries, and it is deliberately a typed model rather than a loose mapping.** `knowledge_resolution: AuthoredReconciliation | None` is the authored decision one `resolution_action='reconcile'` call carries: exactly one conflict the knowledge merge refused, and which side's authored value is the reconciled one. It is typed through `models.knowledge.merge` for the same reason `resolution_action` is typed through `models.worktree` — the vocabulary is owned once and this transport only carries it — and it is optional because every operation that is not an authored reconciliation has no decision to carry. `sync_input_refusal` in the sync driver is what pairs it with its action in both directions (`reconcile` without a decision, and a decision with any other action, are refused by name), so this field cannot be read as a default or as a preference.

`WorktreeArgs` is a `@dataclass(frozen=True)`. Every field carries a default, so
any operation can construct just the subset it needs without supplying the rest;
fields are grouped by concern (coordination/repository resolution, start inputs,
provider setup, lifecycle flags, and normalized closeout input and integration facts). The
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

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

The ledger is a computed consumer cache; it cannot supply an additional Git output or lifecycle prerequisite.

### Todos

None recorded for the ledger-retirement boundary.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `WorktreeArgs` carries normalized closeout input, actual landed code/memory facts, and the one authored knowledge decision a reconcile call may carry. | `WorktreeArgs`; `knowledge_resolution` | mcp/src/agents_remember/worktrees/modules/args.py:35-118; mcp/src/agents_remember/worktrees/modules/args.py:60-62 |
| `report_operation_progress` publishes progress through the exact worker-owned callback. | `report_operation_progress` | mcp/src/agents_remember/worktrees/modules/args.py:118-121 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Public sync choice and resolution-action vocabularies are owned once by the worktree model. (`MemorySyncChoice`; `SyncResolutionAction`) | `MemorySyncChoice`; `SyncResolutionAction` | mcp/src/agents_remember/models/worktree.py:96-96; mcp/src/agents_remember/models/worktree.py:95-95 |
| **The authored-decision vocabulary this transport carries for a reconcile call, owned by the merge model rather than restated here.** (`AuthoredReconciliation`) | `AuthoredReconciliation` | mcp/src/agents_remember/models/knowledge/merge.py:175-211 |
| Provider setup config is typed through the companion worktree models module. (`WorktreeProviderSetupConfig`) | `WorktreeProviderSetupConfig` | mcp/src/agents_remember/worktrees/modules/models.py:35-43 |
| Worktree CLI builds argparse namespaces that this DTO adapts via `from_namespace`. (`build_parser`) | `build_parser` | mcp/src/agents_remember/worktrees/modules/cli.py:132-195 |
| Gate delegation policy model (kernel-owned since L9). (`GatePolicy`; `DEFAULT_GATE_POLICY = GatePolicy()`) | `GatePolicy` | mcp/src/agents_remember/kernel/primitives/gate_policy.py:53-63 |

## Series-Contract Notes

`WorktreeArgs` carries `parent_task` and `leaf_id` through CLI, MCP, and source API entrypoints, giving all operations the same active-task and leaf-selection inputs.

## L23 Final Candidate Disposition

The internal worktree argument DTO carries accepted candidate, task contract, and operation-progress
facts between modules. Public callers still address the canonical task and never supply private
operation, process, lease, or approval identifiers.

## 260821-CLIVE-L1 Internal Transport

`WorktreeArgs` no longer carries raw code and memory closeout message strings. Closeout execution receives one optional `EffectiveCloseoutInput`, populated only after validation; integration and PR landing carry only their actual code/memory output facts. This prevents worker, preview, recovery, and commit code from independently normalizing or defaulting closeout subjects.

## 260821-CLIVE-L2 Current Contract

The current source seams include `WorktreeArgs`, `report_operation_progress`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Inputs shared by the worktree application layer, CLI, and domain functions. (`WorktreeArgs`) | `WorktreeArgs` | mcp/src/agents_remember/worktrees/modules/args.py:35-118 |
| Advance the plane-owned operation when this call runs under its detached worker. (`report_operation_progress`) | `report_operation_progress` | mcp/src/agents_remember/worktrees/modules/args.py:118-121 |

## Current Landed Composition

The internal `integration_certification_owner` field carries the typed journal-owned integration certification continuation. It defaults to absent and is not a public authorization token; the integration owner validates its own authority.

## Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Governing Overview

[Governing route overview](overview.md)

## Update History
- 2026-09-20T07:35+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `b7bfebb550f036a7e51de1f390be1123cd2d2172`): **reopened claim re-read against the construct its range now covers, and the stale generated-projection record retired after that read.** The claim — *"Public sync choice and resolution-action vocabularies are owned once by the worktree model."* — names `MemorySyncChoice` and `SyncResolutionAction`. Each anchor was resolved at its own current declaration in the code worktree and the cited range holds it, so the pointer is current and the wording still holds unchanged: no re-cite and no re-wording was needed. The generated citation-repair bullet that recorded the mechanical projection of this claim's range was **removed** because that projection resolves an exact NAME rather than the claim's subject, so keeping it would leave an unverifiable range asserting currency it cannot support; with it retired the range stands as the curator-read citation it now is. The rest of the card's history is untouched, no other bullet or row was deleted, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T06:22+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the internal transport gained the one decided input this leaf adds.** `WorktreeArgs.knowledge_resolution: AuthoredReconciliation | None` is recorded with what it is (the authored decision for exactly one refused conflict and the side whose value is the reconciled one), why it is typed through `models.knowledge.merge` rather than restated here (the vocabulary is owned once, exactly as `resolution_action` is owned by `models.worktree`), and the fact that the pairing with its action is enforced in the sync driver's `sync_input_refusal` rather than by a default here. Every cited range in this card was re-derived against the delivered tree. Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate named beside it; closeout owns the committed stamp.

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=5e45e8425b3e6205a35a8a343e9c0178d1b2ec87f24472d586fb5cd181ccc24e. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "class WorktreeArgs" repointed to mcp/src/agents_remember/worktrees/modules/args.py:33-33. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
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
