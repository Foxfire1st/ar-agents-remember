# operations/recovery.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

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

### Completion truth on the recovery surface

The block now closes with **Completion truth** (`../core/acceptance.md`): terminal/finalizer truth
attests only that this turn ended, and the owner the recovery exits into opens and validates the
artifact itself. That is the clause this surface needs most, because a recovery exit *looks* like a
completed handoff while leaving an artifact the successor has never read — the clause puts validation
on the seat that continues the work instead of letting a turn-ended signal stand in for acceptance.
The boundary's one home is `core/acceptance.md`; this block states the recovery side of it.

### Conventions

A genuinely semantic conflict follows the ordinary escalation path rather than being silently converted into abandonment.

### Invariants And Boundaries

- An operation block holds procedure only; a rule that applies across roles belongs in `core/`.
- A role file names the operation it selects; it does not restate the procedure.
- The operation vocabulary is closed at eight names, so an unknown operation is an explicit error rather than a silent fallback.
- Authority gates and failure handling stay inside this block, not in the role that triggers it.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1; skills/l-01-agent-lifecycles/composition-manifest.json:45-45; skills/l-01-agent-lifecycles/composition-manifest.json:47-47; skills/l-01-agent-lifecycles/composition-manifest.json:63-63; skills/l-01-agent-lifecycles/composition-manifest.json:73-73; skills/l-01-agent-lifecycles/composition-manifest.json:80-80; skills/l-01-agent-lifecycles/composition-manifest.json:90-90; skills/l-01-agent-lifecycles/composition-manifest.json:98-98; skills/l-01-agent-lifecycles/composition-manifest.json:107-107; skills/l-01-agent-lifecycles/composition-manifest.json:115-115; skills/l-01-agent-lifecycles/composition-manifest.json:128-128; skills/l-01-agent-lifecycles/composition-manifest.json:185-185; skills/l-01-agent-lifecycles/composition-manifest.json:223-223; skills/l-01-agent-lifecycles/composition-manifest.json:261-261; skills/l-01-agent-lifecycles/composition-manifest.json:289-289; skills/l-01-agent-lifecycles/composition-manifest.json:324-324; skills/l-01-agent-lifecycles/composition-manifest.json:366-366; skills/l-01-agent-lifecycles/composition-manifest.json:397-397; skills/l-01-agent-lifecycles/composition-manifest.json:429-429; skills/l-01-agent-lifecycles/composition-manifest.json:463-463; skills/l-01-agent-lifecycles/composition-manifest.json:489-489; skills/l-01-agent-lifecycles/composition-manifest.json:512-512; skills/l-01-agent-lifecycles/composition-manifest.json:539-539; skills/l-01-agent-lifecycles/composition-manifest.json:48-48; skills/l-01-agent-lifecycles/composition-manifest.json:64-64; skills/l-01-agent-lifecycles/composition-manifest.json:74-74; skills/l-01-agent-lifecycles/composition-manifest.json:81-81; skills/l-01-agent-lifecycles/composition-manifest.json:91-91; skills/l-01-agent-lifecycles/composition-manifest.json:99-99; skills/l-01-agent-lifecycles/composition-manifest.json:108-108; skills/l-01-agent-lifecycles/composition-manifest.json:116-116; skills/l-01-agent-lifecycles/composition-manifest.json:129-129; skills/l-01-agent-lifecycles/composition-manifest.json:138-138; skills/l-01-agent-lifecycles/composition-manifest.json:142-142; skills/l-01-agent-lifecycles/composition-manifest.json:146-146; skills/l-01-agent-lifecycles/composition-manifest.json:150-150; skills/l-01-agent-lifecycles/composition-manifest.json:154-154; skills/l-01-agent-lifecycles/composition-manifest.json:158-158; skills/l-01-agent-lifecycles/composition-manifest.json:49-49; skills/l-01-agent-lifecycles/composition-manifest.json:65-65; skills/l-01-agent-lifecycles/composition-manifest.json:75-75; skills/l-01-agent-lifecycles/composition-manifest.json:82-82; skills/l-01-agent-lifecycles/composition-manifest.json:92-92; skills/l-01-agent-lifecycles/composition-manifest.json:100-100; skills/l-01-agent-lifecycles/composition-manifest.json:109-109; skills/l-01-agent-lifecycles/composition-manifest.json:117-117; skills/l-01-agent-lifecycles/composition-manifest.json:130-130 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225; mcp/tests/test_role_instruction_corpus.py:66-66; mcp/tests/test_role_instruction_corpus.py:177-177; mcp/tests/test_role_instruction_corpus.py:180-180; mcp/tests/test_role_instruction_corpus.py:253-253 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/recovery.md:1-1 |
| The completion-truth clause this block now carries, and the boundary's one home. | `**Completion truth**` | skills/l-01-agent-lifecycles/operations/recovery.md:73-74; skills/l-01-agent-lifecycles/core/acceptance.md |

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
