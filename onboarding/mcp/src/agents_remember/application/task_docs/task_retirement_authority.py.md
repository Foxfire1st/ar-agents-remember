# mcp/src/agents_remember/application/task_docs/task_retirement_authority.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

Protects complete retained retirement rows against generic task-document edits.

## Code Commentary

`require_retirement_proofs_unchanged` compares complete retired `SubTaskRef` rows by number, including proof, name, scope, status and file. Generic operations cannot add, change or remove them; direct row targeting also refuses. The diagnostic tells the caller to leave the row unchanged.

`retire_master` creates a retirement record and an identical retained request may complete remaining steps. It is not a general editor of an existing proof. The task-document candidate validator applies the whole-row guard before publication.

## Evidence

- Generic candidate publication preserves complete retirement rows. [3]
- The refusal names the protected row and instructs the caller to leave it unchanged. [4]
