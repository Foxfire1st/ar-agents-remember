# mcp/src/agents_remember/mcp/tools/knowledge_views/record_views.py

## Governing Overview

[MCP Tool Payload Adapters](../overview.md)

## Purpose

Implements the single-record, mark-listing, writer-table, and consolidation-proposal `knowledge_read` view adapters over an already selected and verified `SelectedKnowledgeDataset`.

## Code Commentary

`SINGLE_RECORD_VIEWS` enumerates `("record", "weakness", "dependent", "writers", PROPOSAL_VIEW)`, dispatched by `_one_view`. `_record_view` requires `record_id`, opens a dataset selection against any resolvable code tree (falling back to unverifiable links if `_observe_source` raises `_NoCodeTreeError`), calls `application.knowledge_reader.truth.record_view`, strips inline record document/prose text so only `{path, state}` is named, attaches `record_answer_standing`, and caps `outgoing`, `incoming`, and `timeline.events` at `TOOL_ANSWER_LIST_MAX` with total counts via `_bound_record_lists`. `_marks_view` serves `weakness` and `dependent` listings with `rows:<n>` continuation cursors (refusing malformed tokens with `bad_continuation` rather than restarting), capping page size to `TOOL_ANSWER_LIST_MAX` and emitting `readOn` when rows remain. `_writers_view` and `_proposal_view` are thin adapters delegating to `application.knowledge_writers_view.writers_view` and `application.knowledge_consolidation_proposal.proposal_view`, converting `WriterTableRefusal` and `ProposalRefusal` into `_refused_read`.

## Relationships

`mcp/src/agents_remember/mcp/tools/knowledge.py` imports `_proposal_view` and `_writers_view` directly from this module for its `writers` and `consolidation_proposal` dispatch, while `knowledge.py` keeps its own `view_context`-aware `_record_view`, `_marks_view`, and `_one_view`. `mcp/tests/test_mik_r118_r124_marks.py` imports `record_views` directly. Delegates domain logic to `application.knowledge_consolidation_proposal`, `application.knowledge_writers_view`, `application.knowledge_reader.{marks,selection,truth}`, and `application.record_standing_answers`, and uses `read_request.py` for request/refusal/code-source primitives.

## Evidence

- `_record_view` validates `record_id` and tree presence, reads one record via `record_view`, strips inline `document`/`prose` text to location metadata, attaches standing, and bounds link/timeline lists. [1]
- `_one_view` routes `writers`, `consolidation_proposal` (`PROPOSAL_VIEW`), `record`, and mark-listing views to their respective adapters. [2]
- `_marks_view` pages `weakness` and `dependent` rows using strict `rows:<n>` continuation tokens capped by `TOOL_ANSWER_LIST_MAX` and emits `readOn` when rows remain. [3]
- `_proposal_view` forwards `master_id`, `record_id`, `source_path`, and `limit` to `application.knowledge_consolidation_proposal.proposal_view` and translates `ProposalRefusal` into `_refused_read`. [4]
