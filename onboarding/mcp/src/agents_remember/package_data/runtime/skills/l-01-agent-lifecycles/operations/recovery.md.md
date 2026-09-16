# operations/recovery.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/recovery.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba` |
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview      | `../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

Resuming, re-synchronizing, repairing, or retiring a run whose state moved out from under it. Recovery is an explicit, bounded state transition — never a quiet fallback.

Every operation block shares one five-part shape — who carries it, required inputs, normal workflow, authority gates, failure handling, and handoff/exit — which is what makes a long procedure separately loadable instead of padding every role file.

## Code Commentary

### Logic

`## The recovery moves, and when each applies` is a trigger → exact-move table and is the block's core
value: `source-lineage-stale` / `source-lineage-unavailable` on dispatch creates no child and is recovered
by the refusal's ordered contract-addressed `worktree_sync` before re-dispatching the same document and
role; a source parent that advanced before a handoff is reconciled before the curator or closeout
consumes it; a later source move after a door declaration uses `closeout_door` provenance update rather
than mutating an old queue row; an interrupted closeout/integration/direct-landing resumes the exact
generation through the advertised `worktree_operation_control` action, because the transient landing lock
and the closeout queue are **never** recovery evidence; a non-admitting projection is rebuilt from its
own task- or sprint-addressed action; and a wrong deliverable during baseline execution is repaired by
`task_reopen` under the leaf's own id.

### Conventions

A genuinely semantic conflict follows the ordinary escalation path rather than being silently converted into abandonment.

### Invariants And Boundaries

- An operation block holds procedure only; a rule that applies across roles belongs in `core/`.
- A role file names the operation it selects; it does not restate the procedure.
- The operation vocabulary is closed at eight names, so an unknown operation is an explicit error rather than a silent fallback.
- Authority gates and failure handling stay inside this block, not in the role that triggers it.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/recovery.md:1-1 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/operations/recovery.md` — a file added by the role-instruction corpus consolidation. The canonical source is an operation-scoped procedure block extracted from interleaved role prose (recovery).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
