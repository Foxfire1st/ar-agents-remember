# mcp/src/agents_remember/application/knowledge_gate/deferrals.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Evaluates dependent-record deferral rules during leaf closeout judgment, returning refusing findings for due deferrals or post-sync unedited confirmations and report-only warnings for orphaned deferrals or pre-base watched-file changes.

## Code Commentary

### Logic

- `deferral_gate_findings(trees, owner, *, context=None)` returns `(refusing, reports)` for the leaf candidate memory `K_C` and code diff `B..C`.
- Exports five finding codes: refusing `CONFIRMED_DEFERRED_WITHOUT_EDIT` (`confirmed-deferred-document-without-edit`), `DEFERRAL_DUE_TASK` (`knowledge-deferral-due-task`), and `DEFERRAL_DUE_FILE` (`knowledge-deferral-due-file`); report-only `DEFERRAL_ORPHANED` (`knowledge-deferral-orphaned`) and `DEFERRAL_DUE_FILE_WARNING` (`knowledge-deferral-due-file-warning`).
- Refuses closeout when `owner` confirmed a deferred dependent without changing `record.document` in `B..C`, when an open deferral names `condition.task == owner`, or when `condition.file` changed relative to `fileBlob` and `watched` is in the leaf's own `B..C` diff (`changed_files`).
- Skips deferrals created by the current leaf (`deferral.createdByLeaf == owner`) so a deferral is never due in its creating leaf.
- Emits report-only warnings (never blocking) when `condition.task` is terminal in `load_task_facts` (`orphaned`) or when a watched file changed before `B` (`watched not in changed_files`).
- Fails closed with `RUN_INCOMPLETE` when `K_C`, `C`, or the `B..C` diff cannot be read.

## Relationships

- Called by `application/knowledge_gate/gate.py` (`judge`); intentionally kept outside `memory_quality/knowledge_validator/` so `worktree_sync` is never blocked by a due deferral.
- Reads coordination task status through `tasks/task_facts.py` (`load_task_facts`).

## Evidence

- `deferral_gate_findings` evaluates post-sync unedited confirmations, due-by-task and due-by-leaf-diff blocks, creating-leaf exclusions, and non-blocking orphan/pre-base warnings. [1]
