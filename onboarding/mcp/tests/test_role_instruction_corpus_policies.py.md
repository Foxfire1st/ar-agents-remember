# mcp/tests/test_role_instruction_corpus_policies.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Operational policy and contract proofs for the consolidated lifecycle instruction corpus, split out from `test_role_instruction_corpus.py`.

## Code Commentary

Covers seven policy areas: single-home `templates/curator-handoff-list.md` and `templates/curator-handoff-ingestion.md` contracts plus role/manifest wiring across canonical and `GENERATED_SKILL_COPIES`; JSON-primary master requirement before leaf dependencies both in doctrine and natively via `task_doc_tool`; Architect-only packet-alignment sweep, all-role originating-leaf ownership, advisory-review isolation (`reference/review/advisory-reviews.md`), and Architect-only formal permissions; closeout knowledge-gate refusal routes, Manager dependency checks, and `reference/curator/worklist.md` plus `reference/knowledge/commands.md` coverage; per-command public documentation ownership; exclusion of retired `lenses.md` and `reframe-research` from `skills/` and root `AGENTS.md`; and role-specific `system/task-publication.md` moments for Manager and Architect in both canonical and packaged copies.

## Relationships

Split from `mcp/tests/test_role_instruction_corpus.py` (imports `LIFECYCLE_ROOT`, `REPOSITORY_ROOT`, `ROLE_ORDER`, `SKILLS_ROOT`, `_manifest`, `unresolved_references`). Exercises `task_doc_tool`, `PUBLIC_TOOLS`, `task_document_instruction_contracts`, `GENERATED_SKILL_COPIES`, and `instruction_consistency` helpers.

## Evidence

- Curator hand-off list and ingestion contracts are verified across canonical and generated skill copies alongside role manifest declarations. [1]
- JSON-primary master dependency rules are checked in both instruction contracts and native `task_doc_tool` execution. [2]
- Packet-alignment, advisory-review, formal-permission, closeout knowledge-gate, worklist, public-command, retired-lens, and task-publication policies are pinned with mutation teeth. [3]
