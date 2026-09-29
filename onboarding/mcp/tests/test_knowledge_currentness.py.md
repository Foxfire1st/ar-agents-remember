# mcp/tests/test_knowledge_currentness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_currentness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T19:59:41+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083`|
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R03 cases: stale invariants flagged at read time, over real Git code and a converted memory
tree.** Thirteen cases cover each entry state, the rule-2 precedence, `unrealized`, stale proofs, the
per-side computation, the observation cache key, Git failures, and the two read surfaces
(`knowledge_read` and the published-intent block). The module is in the `unit-regression` lane.

## Code Commentary

### Logic

- **The world.** Each case builds a real code repository (`pkg/review.py`, whose four functions
  `_not_listed`, `other`, `third` and `fourth` each realize their own invariant; `tests/test_review.py`,
  whose test proves one of them; a text file with a line-range anchor; a Markdown file with a symbol
  anchor) and a converted memory tree anchored at the code's first commit (`World`, `world`,
  `_memory_files`). A case then commits code changes the way raw Git would, outside any managed flow.
- **Entry states.** The packet's conforming example (`_body_edit` changes only `_not_listed`: exactly that
  invariant is stale and names its entry; the other three stay current); stale for an absent path, an
  ambiguous symbol and an unmappable range; `unverifiable` with a named reason for no tree, an unreadable
  tree and an unsupported locator.
- **The ruling-N1 order is pinned by `INV-HHHHHH`** (a symbol in Markdown): an unchanged blob is `current`,
  a changed blob is `unverifiable` ("no shipped grammar reads it"), a deleted file is `stale`.
- **Failures (ruling N2).** A patched `TimeoutExpired` gives an `unverifiable` entry, and the next read
  observes again (never cached). A patched `IndexMismatchError` in `knowledge_read` still returns
  `state: view` with its payload and a degraded block.
- **Surfaces.** `knowledge_read` with `codeTreeId` flags the stale invariant and keeps its statement;
  without a named tree, or with only `repositoryRoot`, it is `unverifiable` with compact entries even though
  `HEAD` holds the edit. The published-intent block names its resolved tree and the `treeScope` text; an
  uncommitted edit leaves every state unchanged; with no resolved tree it is `unverifiable`.

### Conventions

- The state-function cases pass a private cache (the `World` helper defaults to a fresh
  `BoundedMemo(1024)`), so they do not share cached answers. The surface cases go through the
  process-wide `OBSERVATIONS`.

### Invariants And Boundaries

- Every Git write is to the case's own temporary repository.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: real Git code, a converted memory tree, raw-Git edits. | "outside any managed flow" | mcp/tests/test_knowledge_currentness.py:1-9 |
| The fixture world, with a fresh private cache by default. | `World`; `world` | mcp/tests/test_knowledge_currentness.py:214-256; mcp/tests/test_knowledge_currentness.py:259-261 |
| The packet's conforming example. | `test_a_raw_git_body_edit_flags_only_its_invariant_and_names_the_entry` | mcp/tests/test_knowledge_currentness.py:273-306 |
| Stale reasons. | `test_stale_covers_an_absent_path_an_ambiguous_symbol_and_an_unmappable_range` | mcp/tests/test_knowledge_currentness.py:309-337 |
| Unverifiable reasons and the N1 order. | `test_unverifiable_names_why_for_no_tree_an_unreadable_tree_and_an_unsupported_locator` | mcp/tests/test_knowledge_currentness.py:340-365 |
| Git failures and no caching of them. | `test_a_failed_or_timed_out_git_call_is_unverifiable_with_its_reason` | mcp/tests/test_knowledge_currentness.py:368-378 |
| A missing recorded line-range blob. | `test_a_line_range_recorded_against_a_blob_the_store_lacks_is_unverifiable` | mcp/tests/test_knowledge_currentness.py:381-402 |
| Precedence and `unrealized`. | `test_precedence_stale_before_unverifiable_before_unrealized` | mcp/tests/test_knowledge_currentness.py:405-418 |
| Stale proofs. | `test_a_proof_whose_test_changed_or_disappeared_is_flagged_stale` | mcp/tests/test_knowledge_currentness.py:421-439 |
| Per side. | `test_one_function_computes_each_side_of_a_comparison` | mcp/tests/test_knowledge_currentness.py:442-461 |
| The cache key. | `test_observations_are_keyed_by_blob_locator_and_extractor_version_and_reused` | mcp/tests/test_knowledge_currentness.py:469-502 |
| `knowledge_read` with a named tree. | `test_knowledge_read_flags_a_stale_invariant_and_keeps_it_visible` | mcp/tests/test_knowledge_currentness.py:523-558 |
| `knowledge_read` without one. | `test_knowledge_read_without_a_named_tree_is_unverifiable_and_never_reads_head` | mcp/tests/test_knowledge_currentness.py:561-580 |
| The published-intent block. | `test_the_published_intent_block_flags_returned_invariants_at_its_resolved_tree` | mcp/tests/test_knowledge_currentness.py:583-630 |
| A failing step never refuses. | `test_a_failing_currentness_step_degrades_to_a_reason_and_never_refuses_the_read` | mcp/tests/test_knowledge_currentness.py:633-656 |
| The lane row. | "mcp/tests/test_knowledge_currentness.py" | mcp/tests/test-evidence-lanes.toml:112-112 |

## Cross-Repo References

No meaningful cross-repo references found: every case works in its own temporary repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): created this card for the new case module MIK-R03 adds (13 cases). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
