# mcp/src/agents_remember/application/memory_quality/answer.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Projects full memory-quality run outcomes into caller-sized status answers without changing execution, finding classification or checklist authority.

## Code Commentary

Sync and completed-poll answers carry outcome, counts by finding kind, ordered blocking work orders and locations. Blocking rows are selected from repair findings, missing cards and stale indexes in repair-loop order; reasons are shortened only in the answer, not in the retained whole result. Start/poll outcomes preserve running/refused/completed state and scope-bound follow-up arguments. A failed coherence takeover keeps its code and next action, including task_doc for a missing task parent. A missing report is disclosed rather than treated as absence of findings.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- Completed results retain status, blocking totals and report locations. [1]
- The bounded blocking list preserves repair-loop order and whole-population count. [2]
- A taken-over failure retains its own code and recovery action. [3]
- Poll projection distinguishes live, absent and completed runs. [4]
