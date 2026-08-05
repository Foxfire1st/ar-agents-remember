# 260731-EFA-L6 Curator Mutation Report

| Field | Value |
| --- | --- |
| Session | `019fc28b-4d2e-73e2-ad47-4b4f23ab72b9` |
| Master / leaf | `260731-EFA` / `260731-EFA-L6` |
| Lifecycle | `01KYZ1BS8VTQ6H1PMG2V37HN5R` |
| Role | curator; sender `90d8a7eb20a0412c992830160bcf78f6` |
| Code base | `a714114ef94eedb8042fb4caa38d9469f4767dd6` |
| Memory base | `15953ff882e296e32096b60e3478fc1731f47938` |

## Release evidence

The leaf task record was refreshed through `task_doc.get` for slug
`06_fitness-functions`. The JSON-primary ledger reads 28 of 30 steps done, S18
`inProgress`, and S29 `pending`. The S23/S24 and S27 delta verdicts were read;
both are PASS. `worktree_status` reports current frozen code/memory bases,
pending review, no commit approval, and closeout/integration not started.

## Tier-1 mutation

The checkout-local command was run with `PYTHONPATH=mcp/src` and the exact
contract path. The initial frozen live check was 1,168 documents and 11,916
findings across 1,118 affected documents. The release shorthand named 204
exact fixes; the frozen checkout's exact `--fix --dry-run` payload contained
208 unique repairs across 71 documents. All 208 were applied because they were
unique anchor/range repairs in the current frozen source tree; this 204 -> 208
reconciliation is retained in the manifest.

The safe old-form migration was 92 items across 43 documents. The exact scoped
operations were one `--migrate --document <onboarding-root-relative-path>` or
one `--fix --document <onboarding-root-relative-path>` per document. Per-group
hash checks proved that each group changed only its assigned onboarding files;
no overview or route index was refreshed.

The complete exact document lists are also machine-retained at the manifest's
`sourceCheck.tier1.migrationDocuments` and
`sourceCheck.tier1.exactFixDocuments` fields. For auditability, they are:

### 92 safe old-form migrations / 43 documents

```text
dashboard/src/data/capabilityCatalog.ts.md
dashboard/src/data/catalogPoll.ts.md
dashboard/src/data/commands.ts.md
dashboard/src/data/conversation-library/store.test.ts.md
dashboard/src/data/conversation/agents.ts.md
dashboard/src/data/conversation/thinkingPreference.ts.md
dashboard/src/data/keymap/focus.ts.md
dashboard/src/data/keymap/zones.ts.md
dashboard/src/data/launchEvidence.ts.md
dashboard/src/data/launchFlow.ts.md
dashboard/src/data/ptyHarvest.ts.md
dashboard/src/data/seatEvents.ts.md
dashboard/src/data/sessionLayout.ts.md
dashboard/src/data/sessionLifecycle.ts.md
dashboard/src/data/sessions.ts.md
dashboard/src/grammar/EvidenceBadge.tsx.md
dashboard/src/panels/FlowTab.tsx.md
dashboard/src/panels/session-cockpit/conversation/primitives.test.tsx.md
dashboard/src/test/fixtureOverrides.test.ts.md
dashboard/src/test/fixtures/overrides.ts.md
dashboard/src/test/servedProjection.ts.md
dashboard/src/test/wireFixtureGuard.ts.md
mcp/src/agents_remember/kernel/git_facts.py.md
mcp/src/agents_remember/kernel/memory_init.py.md
mcp/src/agents_remember/kernel/memory_ledger.py.md
mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py.md
mcp/src/agents_remember/models/tokens.py.md
mcp/src/agents_remember/observer/lifecycle_state.py.md
mcp/src/agents_remember/observer/reducer.py.md
mcp/src/agents_remember/observer/snapshots.py.md
mcp/src/agents_remember/serving/app.py.md
mcp/src/agents_remember/serving/changeset.py.md
mcp/src/agents_remember/worktrees/modules/landing.py.md
mcp/src/agents_remember/worktrees/modules/start_contract.py.md
mcp/src/agents_remember/worktrees/worktree_contract.py.md
mcp/tests/_store_durability.py.md
mcp/tests/test_git_command.py.md
mcp/tests/test_provider_store_durability.py.md
mcp/tests/test_serving.py.md
mcp/tests/test_serving_response_conformance.py.md
mcp/tests/test_sync_scripts.py.md
mcp/tests/test_tool_response_conformance.py.md
mcp/tests/test_wire_vocabulary_exhaustiveness.py.md
```

### 208 exact fixes / 71 documents

```text
.git-blame-ignore-revs.md
dashboard/src/cockpit/Cockpit.tsx.md
dashboard/src/data/interactionAnswer.test.ts.md
dashboard/src/data/store.test.ts.md
dashboard/src/data/store.ts.md
dashboard/src/data/taskHierarchy.test.ts.md
dashboard/src/data/taskHierarchy.ts.md
dashboard/src/dev/fixtures.ts.md
dashboard/src/fixtures/snapshot.json.md
dashboard/src/overview.md
dashboard/src/panels/LifecycleList.test.tsx.md
dashboard/src/panels/engine-room/EnclosureStackList.tsx.md
dashboard/src/panels/engine-room/buildEngineRoomModel.ts.md
dashboard/src/test/contract.test.ts.md
dashboard/src/test/fixtures/wire.ts.md
dashboard/src/test/wireFixtureGuard.test.ts.md
dashboard/src/test/wireFixtureGuard.ts.md
dashboard/src/types/projection.ts.md
dashboard/src/types/terminalOpen.ts.md
mcp/src/agents_remember/code_quality/diff_coverage.py.md
mcp/src/agents_remember/controlplane/attention_dismissals.py.md
mcp/src/agents_remember/controlplane/durable_store.py.md
mcp/src/agents_remember/controlplane/expectation_rows.py.md
mcp/src/agents_remember/controlplane/operator_inbox_store.py.md
mcp/src/agents_remember/controlplane/orchestration_nudges.py.md
mcp/src/agents_remember/controlplane/supervisor_signals.py.md
mcp/src/agents_remember/kernel/agentic_settings.py.md
mcp/src/agents_remember/mcp/registration/orchestration.py.md
mcp/src/agents_remember/mcp/registration/overview.md
mcp/src/agents_remember/mcp/registration/tasks.py.md
mcp/src/agents_remember/mcp/tools/base.py.md
mcp/src/agents_remember/mcp/tools/gates.py.md
mcp/src/agents_remember/mcp/tools/next_step.py.md
mcp/src/agents_remember/mcp/tools/terminal.py.md
mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py.md
mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/report.py.md
mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py.md
mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py.md
mcp/src/agents_remember/models/tokens.py.md
mcp/src/agents_remember/models/tool_registry.py.md
mcp/src/agents_remember/observer/lifecycle_state.py.md
mcp/src/agents_remember/observer/projection.py.md
mcp/src/agents_remember/observer/series_tokens.py.md
mcp/src/agents_remember/observer/snapshots.py.md
mcp/src/agents_remember/serving/change_watcher.py.md
mcp/src/agents_remember/serving/notes.py.md
mcp/src/agents_remember/serving/retire.py.md
mcp/src/agents_remember/serving/retire_policy.py.md
mcp/src/agents_remember/serving/scope.py.md
mcp/src/agents_remember/serving/seat_events.py.md
mcp/src/agents_remember/worktrees/modules/code_quality_gate.py.md
mcp/src/agents_remember/worktrees/modules/guidance.py.md
mcp/src/agents_remember/worktrees/worktree_contract.py.md
mcp/tests/_store_durability.py.md
mcp/tests/conftest.py.md
mcp/tests/overview.md
mcp/tests/test_change_watcher.py.md
mcp/tests/test_cold_start.py.md
mcp/tests/test_controlplane_gates.py.md
mcp/tests/test_controlplane_store_durability.py.md
mcp/tests/test_durable_store_contract.py.md
mcp/tests/test_gate_replay_window.py.md
mcp/tests/test_interaction_retention.py.md
mcp/tests/test_observer_projection.py.md
mcp/tests/test_provider_containment.py.md
mcp/tests/test_provider_store_durability.py.md
mcp/tests/test_serving.py.md
mcp/tests/test_sync_scripts.py.md
mcp/tests/test_wire_vocabulary_exhaustiveness.py.md
mcp/tests/test_worktree_closeout_quality_gate.py.md
mcp/tests/test_worktree_contract_lifecycle.py.md
```

The post-Tier-1 live check retained in the manifest is 11,453 findings across
1,116 affected documents. Its code counts are:

| Code | Count |
| --- | ---: |
| `citation_anchor_absent_from_range` | 36 |
| `citation_anchor_missing` | 4,806 |
| `citation_prose_not_in_cit_form` | 1,525 |
| `citation_range_out_of_bounds` | 2 |
| `citation_source_malformed` | 5,083 |
| `citation_source_vanished` | 1 |

## Dispatch manifest

Manifest: `/tmp/claude-1000/-home-mohamedreadone-Projects/6991d9c6-7c73-4762-9708-52d8b5904682/scratchpad/L6-CURATOR-BATCHES.json` (11,600,980 bytes).

It retains the complete post-Tier-1 JSON/work order, every document's finding
records/codes, 60 non-overlapping batches, and five waves of 12 batches. The
cardinality proof is: 1,116 affected documents; 1,116 batch occurrences;
1,116 unique documents; zero duplicates; zero omissions; zero extras; 60
batches; 12 batches in each wave; 11,453 findings. Cards with 50 or more
findings are singleton batches; the rest use finding-weight LPT packing, and
wave assignment balances finding weight rather than document count.

## W1-B01 lead pass

Assigned document:

```text
mcp/src/agents_remember/observer/series_tokens.py.md
```

The single Tier-2 finding was `citation_prose_not_in_cit_form` in the existing
Update History. I re-read the claim and `mcp/src/agents_remember/observer/series_tokens.py`,
then supplied the exact anchors `SeriesNode` and `seriesTokenTotal` plus the
source path. The scoped command rewrote the temporary `:1-1` range to the
verified `mcp/src/agents_remember/observer/projection.py:671-697` range.

One newest offset-bearing Update History entry was added at
`2026-08-02T16:20:23+02:00`. The scoped result was `claimsRepaired=1`,
`declinedCount=0`, `findingsRemaining=0`; the scoped recheck returned zero
findings. W1-B01 has no unresolved item and no Tier-3/claim dispute. Remaining
findings belong to the other manifest batches and were not claimed by this
seat.

The final full check after W1-B01 is 11,452 findings across 1,115 affected
documents: 36 anchor-absent, 4,806 anchor-missing, 1,524 old-form prose,
2 out-of-bounds, 5,083 malformed-source, and 1 vanished-source finding.

## Preservation and checks

- No code, task JSON/Markdown, contract, settings, branch, index, stash,
  commit, lifecycle, closeout, integration, push, overview, or route-index
  state was changed.
- Tier-1 scoped batches and W1-B01 changed only their assigned onboarding
  documents; the final report and scratch manifest are the only additional
  artifacts written.
- `git diff --check` passed in the memory worktree.
- Providers and CGC remained off. All citation commands used the checkout
  virtualenv and `PYTHONPATH=mcp/src`.

