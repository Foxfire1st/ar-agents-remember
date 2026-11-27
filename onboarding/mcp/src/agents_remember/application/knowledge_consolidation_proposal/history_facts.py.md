# mcp/src/agents_remember/application/knowledge_consolidation_proposal/history_facts.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Extracts the two consolidation-proposal facts stored only in raw `knowledge/history/*.json` files (not in the SQLite index): which rules a finished master's leaves wrote (`master_writes`) and when each family was last consolidated (`last_consolidations`).

## Code Commentary

`master_writes` validates `master_id` against `MASTER_ID_PATTERN` (`^[0-9]{6}-[A-Za-z0-9]+$`, raising `ProposalRefusal("bad_master", ...)`), reads `knowledge/history/<master_id>-*.json` files whose `history.leaf` starts with `<master_id>-`, tallies `closed_files` and `open_files`, and refuses with `selector_absent` when zero leaf files match. It unions rules written by closed files with live rules whose `origin.leaf` starts with `<master_id>-`. `_rules_written` counts invariant IDs in `history.written` plus `InvariantRow` subjects with dispositions in `CARD_OR_TEXT_DISPOSITIONS` (`changed`, `deleted`, `moved`, `extended`), excluding read-only dispositions (`no_impact`, `stands`, `unresolved`). `last_consolidations` pre-filters history file bytes for `_CONSOLIDATOR_MARK` (`"consolidator"`) before JSON/model parsing, then inspects only closed files with `review.handed_over_by.role == CONSOLIDATOR_ROLE`. For every family in `_families_reached` (`written` family IDs or `FamilyRow` dispositions other than `unresolved`), it records the latest `review.reviewer.at` timestamp (normalized via `_instant`, treating naive timestamps as UTC and unparseable values as `datetime.min` UTC). `_files` parses each matching file through `parse_document_text` and `history_document`, turning any `OSError` or `ValueError` into `ProposalRefusal("unavailable", ...)`.

## Relationships

Called by `view._proposal` (`master_writes` for `masterId`, `last_consolidations` for `oldest`). Uses `models.knowledge_files.documents`, `models.knowledge_files.history`, `models.knowledge_files.ids`, `models.knowledge_files.record_state`, and raises `.refusal.ProposalRefusal`.

## Evidence

- `master_writes` enforces `MASTER_ID_PATTERN` (`bad_master`), counts open and closed leaf history files (`selector_absent` when none exist), and combines closed-file writes with `rule_origins` matching the master prefix. [1]
- `last_consolidations` scans only files containing `"consolidator"`, requires closed files whose review was handed over by a consolidator, and records each reached family's latest reviewer timestamp. [2]
- `_rules_written` counts invariant records in `written` and `InvariantRow` rows in `CARD_OR_TEXT_DISPOSITIONS`, ignoring read-only dispositions. [3]
- `_files` parses matching JSON history files through `history_document` and converts `OSError`/`ValueError` into `ProposalRefusal("unavailable", ...)`. [4]
