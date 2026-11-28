# mcp/src/agents_remember/application/knowledge_integrity_answer.py

## Governing Overview

[application overview](overview.md)

## Purpose

This module projects a full `knowledge_integrity_check` result into its bounded inline tool answer. It keeps validation counts, bounded top violations, family route summary counts, and worklist summary metadata inline while the full route rows and worklist item rows stay in the validated payload and daily tool log.

## Code Commentary

`summarize_routes` iterates over route rows and returns a fixed-size summary object containing `familyCount`, `byStatus` (sorted status counts), `routeUnassigned`, `routeless`, and `differs` instead of returning per-family route rows inline.

`summarize_worklist` retains only `_WORKLIST_SUMMARY_KEYS` (`path`, `digest`, `itemCount`, `state`, `owner`, `itemsByKind`, `detail`) plus up to `TOOL_ANSWER_STATUS_ENTRY_MAX` entries from `incomplete` when present; it omits the per-item `items` list so callers read the full worklist from its file path or the daily tool log.

`_bounded_validation` caps `validation["violations"]` at `TOOL_ANSWER_STATUS_ENTRY_MAX` entries (both raw list and `{count, items, truncated}` mapping shapes) and sets `truncated: True` whenever the total exceeds the cap. `integrity_answer` strips `ENVELOPE_STRIPPED_FIELDS` and `None` values from the full payload and replaces `routes`, `worklist`, and `validation` with their bounded projections when present.

## Relationships

`mcp/src/agents_remember/mcp/tools/knowledge.py::_integrity_answer` delegates directly to `integrity_answer` when building the `answer=` argument for `_tool_payload`. The module imports only `ENVELOPE_STRIPPED_FIELDS` and `TOOL_ANSWER_STATUS_ENTRY_MAX` from `models/tools/tool_answer.py`; it performs no validation, disk reads, or Git calls itself. Full per-family route rows remain available in the daily tool log and via `agents-remember knowledge-routes`.

## Evidence

- `summarize_routes` aggregates family route rows into `familyCount`, `byStatus`, `routeUnassigned`, `routeless`, and `differs` counts without per-family inline rows. [1]
- `summarize_worklist` keeps only `_WORKLIST_SUMMARY_KEYS` and bounded `incomplete` entries inline, omitting `items` so per-item rows stay in the persisted file and tool log. [2]
- `_bounded_validation` caps violation lists at `TOOL_ANSWER_STATUS_ENTRY_MAX` entries and marks `truncated: True` when shortened, and `integrity_answer` assembles the stripped inline projection. [3]
