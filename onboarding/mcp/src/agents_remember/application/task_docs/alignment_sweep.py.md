# mcp/src/agents_remember/application/task_docs/alignment_sweep.py

## Governing Overview

[governing overview](overview.md)

## Purpose

New advisory packet-write sibling projection; no gate or task mutation.

## Code Commentary

alignment_sweep runs for subTask creation or set_field/replace requirements edits. It finds the explicit or folder master and uses its declared nonterminal, nonretired sibling rows, excluding the current leaf. Up to twelve siblings return IDs and available requirement identities; more than twelve return openLeafCount and the master Markdown location. Empty or whitespace-only row.file is unavailable/no-file, a nameless path such as dot is unavailable/no-name, and FileNotFoundError on a named sibling is unavailable/missing; _unavailable logs the cause with warning. The advice neither changes sibling packets nor decides release. Other read failures are not converted here.

## Evidence

- New advisory packet-write sibling projection; no gate or task mutation. [1]
