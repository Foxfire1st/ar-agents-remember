# mcp/src/agents_remember/application/knowledge_consolidation_proposal/store.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Loads the live family, rule, and realization-location graph for one memory tree in a constant number of `KnowledgeIndex` queries so proposal computation is purely in-memory.

## Code Commentary

`load_store` reads `index.records_of_kind("invariant")`, `index.records_of_kind("family")`, and `index.entries_under(".").value.realizations` once each. Retired records (`status == RETIRED_STATUS`) are excluded: retired rules never enter `store.rules` or a `FamilyFacts.members` tuple, and a rule whose only family is retired becomes a loose rule (`loose_rules()`). `folder_of` computes the parent POSIX directory of a normalized realization path (`.` for root-level files) for folder seeding, while `_place_realizations` indexes `loose_by_file` by exact normalized realization file path (`entry.path`) so `ProposalStore.attached_rules(family)` attaches only unaffiliated live rules sharing an exact source file with a family member. `_origin_leaf` captures each live rule's `origin.leaf` string for master-write attribution, and `_family` extracts `title`, live `members`, and `writer.at` (`stamped_at`).

## Relationships

Called by `.view._store_of` and consumed by `.proposal` and `.view._proposal`. Reads `RETIRED_STATUS` from `memory.knowledge_index.projection` and queries `memory.knowledge_index.query.KnowledgeIndex`.

## Evidence

- `ProposalStore` maintains live family/rule/file/folder maps and derives `loose_rules`, `member_files`, `member_folders`, and sorted `attached_rules` in memory. [1]
- `load_store` filters out `RETIRED_STATUS` invariants and families, builds `rule_origins` and `rule_families`, and populates realizations in one pass. [2]
- `_place_realizations` scans `index.entries_under(".").value.realizations` once to map live rules to normalized files and parent folders and index loose rules by exact file path. [3]
