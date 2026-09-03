# mcp/src/agents_remember/worktrees/modules/context.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/context.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Resolves coordination context for worktree lifecycle operations.

## Code Commentary

`resolve_context()` adapts the typed `WorktreeArgs` dataclass (from
`agents_remember.worktrees.modules.args`) to the kernel resolver.
`contract_context()` reconstructs context from a persisted worktree contract
and, for external-memory tasks, reparses settings from the memory worktree when
that task branch changed memory settings.

Since 260731-EFA-L2 both calls use the resolver's two parameter objects (from
`kernel.coordination_context_resolver`). `resolve_context` passes
`hints=CoordinationHints(topology=…, coordination_root=…)` plus an
`EnclosureSelector(contract_path, task_name, parent_task, leaf_id, worktree_name)` built from the
same `getattr(args, …, None)` reads as before; `contract_context` passes
`selector=EnclosureSelector(contract_path=contract.contract_path)`. This module is the
`WorktreeArgs`-to-resolver adapter, so it is where a new worktree-side resolution input gets
mapped onto a resolver bundle.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The kernel resolver facade and the coordination-context builder own topology, storage, path rules, and cross-repo resolution. | "def build_coordination_context(" | mcp/src/agents_remember/kernel/coordination_context/resolver.py:272-312 |
| Closeout planning uses this module before the sole external-phase owner refreshes onboarding metadata. | "def _memory_refresh_preview("; "def _closeout_contract_context("; "def external_closeout_commits(" | mcp/src/agents_remember/worktrees/modules/closeout.py:226-226; mcp/src/agents_remember/worktrees/modules/closeout.py:965-965; mcp/src/agents_remember/worktrees/modules/closeout_external.py:61-61 |

## Series-Contract Notes

The context wrapper forwards `parent_task` and `leaf_id` from `WorktreeArgs` to the resolver before operation modules build or load contracts.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 2 table citations and normalized 2 source paths; no unresolved Tier-3 claims.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update for the kernel resolver's new
  signature — `resolve_context` builds a `CoordinationHints` + `EnclosureSelector`, and
  `contract_context` an `EnclosureSelector(contract_path=…)`. Same resolved contexts. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree context resolution now forwards `parent_task` and `leaf_id` from `WorktreeArgs` into the coordination resolver. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — `resolve_context()` now takes a typed `WorktreeArgs` (from `agents_remember.worktrees.modules.args`) instead of `argparse.Namespace`, dropping the `import argparse`; corrected Code Commentary "command namespaces" prose to name the dataclass (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
