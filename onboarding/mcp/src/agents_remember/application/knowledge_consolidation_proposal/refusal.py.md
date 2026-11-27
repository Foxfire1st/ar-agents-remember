# mcp/src/agents_remember/application/knowledge_consolidation_proposal/refusal.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Defines `ProposalRefusal`, the single structured exception raised when a `consolidation_proposal` read cannot be answered.

## Code Commentary

`ProposalRefusal(code: str, detail: str)` stores both attributes on the exception instance and passes `detail` as the `Exception` message so callers can map `code` to a typed refusal envelope while forwarding `detail` as the remediation sentence.

## Relationships

Raised by `.history_facts` (`bad_master`, `selector_absent`, `unavailable`) and `.view` (`snapshot_unavailable`, `bad_selector`, `selector_absent`, `report-unwritable`). Re-exported by package `__init__.py` and caught by `mcp/tools/knowledge_views/record_views.py`.

## Evidence

- `ProposalRefusal` subclasses `Exception`, initializes the message with `detail`, and stores `code` and `detail` attributes. [1]
- The module docstring establishes that consolidation proposal refusals carry a code and a remediation sentence. [2]
