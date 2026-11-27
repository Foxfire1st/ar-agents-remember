# mcp/src/agents_remember/application/knowledge_queries.py

## Governing Overview

[application](overview.md)

## Purpose

Internal application query-view dispatcher bridging `knowledge_read` requests for `QUERY_VIEWS = frozenset({"impact", "search", "records"})` to their application query owners, handling automatic code-source pairing, dataset selection lifecycle, error refusal mapping, and standard MCP `state: "view"` / `"refused"` envelopes.

## Code Commentary

- `run_query_view` refuses (`snapshot_unavailable`) when `selected.memory_tree` is `None` or `selection_for_dataset` raises `READ_FAILURES`; converts `NoCodeTreeError` from `observe_code_source` into an unpaired read (`source = None`) rather than failing, and always closes `selection` and `source` in `finally` and on open error.
- `_dispatch` maps `request` fields to `ImpactQuery` (with `folder = request.folder or request.source_path`), `SearchQuery`, or `records_view`.
- Application-level refusals (`"refusalCode"` in payload) map to `_refused` (`ok: True`, `state: "refused"`, `refusalCode`, `refusalDetail`), while `READ_FAILURES` during query execution return `refusalCode="unavailable"`.
- Lifts `payload.pop("continuation", None)` to top-level `answer["continuation"]` and ANDs `payload["enumerationComplete"]` with `tree.index_state == "complete"` so partial indexes never advertise complete enumeration.

## Relationships

- Called by `mcp/src/agents_remember/mcp/tools/knowledge.py` (`QUERY_VIEWS`, `QueryViewContext`, `run_query_view`); tested in `mcp/tests/test_kno_r07_knowledge_queries.py`.
- Depends on `application/knowledge_code_pairing.py`, `application/knowledge_impact.py`, `application/knowledge_search.py`, `application/knowledge_reader/records_batch.py`, `application/knowledge_reader/selection.py`, `application/published_intent.py::SelectedKnowledgeDataset`, and `kernel/primitives/runtime_config.py::RepositoryScope`.

## Evidence

- Declares `QUERY_VIEWS` (`impact`, `search`, `records`) and `QueryViewContext`. [1]
- `run_query_view` pairs code source, closes resources safely, maps refusals, lifts `continuation`, and gates `completeWithinDeclaredScope` on `tree.index_state == "complete"`. [2]
- `_dispatch` routes `impact`, `search`, and `records` requests to their application view functions. [3]
