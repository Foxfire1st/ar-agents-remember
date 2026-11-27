# mcp/src/agents_remember/application/knowledge_consolidation_proposal/proposal.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Pure selection and ordering engine that computes a `Proposal` (proposed `ProposedFamily` rows plus loose `rules_in_no_family`) from an in-memory `ProposalStore` across the four proposal ways: `master`, `family`, `folder`, and `oldest`.

## Code Commentary

`for_master` intersects `written_rules` with live `store.rules`, counts touched members per live family, orders families by `(-touched_members, family_id)`, and puts live written rules belonging to no live family into `rules_in_no_family`. `for_family` returns the single named live family with empty `rules_in_no_family`. `for_folder` selects every live family with at least one member realized in a folder equal to or nested beneath `folder` (`""` and `"."` match all folders; `_under` enforces path-boundary matching via `<folder>/`) sorted by family ID. `oldest_first` partitions live families into never-consolidated (ordered by `_first_written_key`: committed families first by `first_written.timestamp()`, then working-tree-only families by `stamped_at` and ID) followed by previously consolidated families ordered by `(last_consolidated, family_id)`. `_proposed` populates each `ProposedFamily` with its live member count and `store.attached_rules(family)` (unaffiliated live rules realized in the same exact files as the family's members); `attached_total` returns the distinct count across an iterable of proposed families.

## Relationships

Consumes `.store.ProposalStore` and is invoked exclusively by `.view` (`for_master`, `for_family`, `for_folder`, `oldest_first`, `attached_total`, `PassTimes`, `Proposal`, `ProposedFamily`). Performs no I/O or validation.

## Evidence

- `for_master` ranks live families by descending count of master-written member rules then family ID, and lists live written rules outside all families in `rules_in_no_family`. [1]
- `for_folder` selects live families having any member realized at or under the normalized folder path (with `""`/`.` matching all folders), sorted by family ID. [2]
- `oldest_first` places never-consolidated families first (ordered by `_first_written_key`) followed by consolidated families ordered oldest `last_consolidated` first. [3]
- `_proposed` constructs each `ProposedFamily` from `ProposalStore`, attaching sorted loose rules realized in its members' files. [4]
