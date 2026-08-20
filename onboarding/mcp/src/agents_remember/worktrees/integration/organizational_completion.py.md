# mcp/src/agents_remember/worktrees/integration/organizational_completion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Computes and publishes the exact completion proof for a branchless organizational master's final-leaf landing.

## Code Commentary

### Logic

`organizational_completion_plan` resolves the canonical sprint→master→leaf topology, requires `executionNature="organizational"`, and refuses any other queue candidate from the same master. It loads a confined landing contract for every sibling and requires each sibling's exact landed code/memory/ledger pair to be reachable from the current sprint super. The completion fingerprint binds the master semantic digest, landed sibling facts, and the exact code/memory/ledger commits. `publish_organizational_master_completion` writes the master `status=Completed` decision marker only after the certified ref movement and the fingerprint match.

### Invariants And Boundaries

- Task parentage (logical master) and Git parentage (sprint super) stay deliberately separate.
- A sibling contract reached through any symlink or path escape is refused.
- Ledger rows stay one-to-one with the landed code+memory pair; retries cannot publish a stale mapping.
- An already-Completed master that lacks its exact certified marker raises.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact final-leaf plan requires sibling code/memory/ledger proof and sprint integrationBranch. | `organizational_completion_plan` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:87-144 |
| Scope validation pins executionNature, owning master, and canonical child. | `_completion_scope` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:147-183 |
| Sibling code ancestry is re-proved against the sprint super. | `_require_landed_sibling` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:307-343 |
| Sibling memory ancestry and unique ledger mapping are enforced. | `_require_landed_sibling_memory`, `_sibling_memory_mappings` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:376-385; mcp/src/agents_remember/worktrees/integration/organizational_completion.py:413-443 |
| Master completion is published only with the exact certified fingerprint. | `publish_organizational_master_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:229-264 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational direct-super completion proof.