# mcp/src/agents_remember/application/knowledge_consolidation_proposal/__init__.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Package entry point for the `consolidation_proposal` reader view of `knowledge_read`. It documents the five-stage submodule pipeline (`.store`, `.history_facts`, `.first_written`, `.proposal`, `.view`) and re-exports the view's public boundary without implementing logic of its own.

## Code Commentary

Re-exports `PROPOSAL_VIEW`, `ProposalRefusal`, `ProposalRequest`, and `proposal_view` via `__all__`. No side effects or registry mutations occur on import.

## Relationships

Imported by `mcp/tools/knowledge.py` (`PROPOSAL_VIEW`) and `mcp/tools/knowledge_views/record_views.py` (`PROPOSAL_VIEW`, `ProposalRefusal`, `ProposalRequest`, `proposal_view`). Delegates all refusal and view behavior to `.refusal` and `.view`.

## Evidence

- The package docstring maps `.store`, `.history_facts`, `.first_written`, `.proposal`, and `.view` as the `consolidation_proposal` reader pipeline. [1]
- `__all__` exposes only `PROPOSAL_VIEW`, `ProposalRefusal`, `ProposalRequest`, and `proposal_view` from `.refusal` and `.view`. [2]
