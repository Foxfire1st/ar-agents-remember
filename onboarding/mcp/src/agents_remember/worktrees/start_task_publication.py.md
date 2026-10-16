# mcp/src/agents_remember/worktrees/start_task_publication.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Publish start or reattachment task facts through the existing task-fact transaction.

## Code Commentary

Leaf registration first checks the selected enclosure binding and refuses terminal documents with unresolved work units by the existing typed error. The prepared stage change includes the registered document and its parent row. Start requests inProgress even if the binding was already exact; reattachment preserves stage. Dry run writes nothing.

Publication occurs only when document facts differ and revalidates inside the transaction; projection scopes use the exact document/path candidates. The final binding check remains explicit. Authority refusal is a named re-read/repair instruction, never an invented task_doc read tool. Series activation can run the same stage preflight before structural work.

## Evidence

- Start and attachment use one stage planner and task-fact publication owner. [1]
- Series bootstrap checks stage authority before mutation. [2]
