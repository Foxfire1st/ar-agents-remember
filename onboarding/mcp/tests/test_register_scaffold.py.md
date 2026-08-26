# mcp/tests/test_register_scaffold.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_register_scaffold.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the 260815-DAG-L13-R6 register contract: sprint creation scaffolds the empty canonical
Judgment and Priority Register sections (so set-grade never dead-ends on a missing register), and
every write through a register heading keeps the canonical table shape. Read paths stay tolerant —
malformed registers are facts, never crashes.

## Code Commentary

### Logic

`RegisterScaffoldTests` proves sprint creation gains both empty canonical registers while a plain
master scaffolds nothing, a supplied valid register is preserved, `create`/`replace`/`set_section`
with a malformed register-heading section are refused at write time, and a sprint cannot drop its
authored `executionGraph` through `replace`.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- Writes are strict and reads stay tolerant — both directions are forced.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Register scaffolding and write-time shape validation forcing. | `RegisterScaffoldTests` | mcp/tests/test_register_scaffold.py:42-233 |
| The scaffold and write-time gate under test. | `register_scaffold_sections`; `require_register_sections_valid` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:559-586; mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:597-611 |
| The task-doc create/write integration under test. | "def scaffold_register_sections(data: dict[str, Any]) -> None:"; "def _enforce_register_section_shapes(doc: TaskDocument) -> None:" | mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:17-37; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:587-592 |

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: created as the register scaffold/write-time validation
  forcing suite. Verification remains closeout-owned.