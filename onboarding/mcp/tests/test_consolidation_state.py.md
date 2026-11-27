# mcp/tests/test_consolidation_state.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Verifies the post-closeout record states a consolidation pass produces in `KnowledgeIndex.standing`, the unpassed-closeout review note sentences, and the five consolidation columns in the `writers` view.

## Code Commentary

Constructs converted memory trees with reviewed base histories and a consolidation leaf history (`consolidationSubjects` + `consolidator` writer/review facts) and checks three invariants: (1) after a closeout with a recorded review pass, revisions the Consolidator wrote, listed revisions left `stands`, listed rules with card-only `extended` or non-retiring `deleted` rows, and a `stands` family read `"consolidated"`, while an `unresolved` rule and an unlisted family reached via a corrected member keep `"reviewed"`; (2) without a review pass, the Consolidator's written revision reads `"proposed"`, read-only revisions stay `"reviewed"`, and both `closed_history_review_note` and `closeout_external._review_note` emit `NO_PASS_SENTENCE` followed by `NOTHING_CONSOLIDATED_SENTENCE` (whereas an ordinary unpassed task emits only `NO_PASS_SENTENCE` and a passed file emits `""`); and (3) the `writers` view counts `consolidationKept`, `consolidationCorrected`, `consolidationMerged`, `consolidationRetired`, and `consolidationUnresolved` per original writer of each revision read and lists the underlying `INV-...@1` revisions in the report.

## Relationships

Exercises `KnowledgeIndex.standing`, `worktrees.review_note.closed_history_review_note`, `worktrees.modules.closeout_external._review_note`, `worktrees.review_fact_source`, and `application.knowledge_writers_view` through `knowledge_review_fact_test_support`, `test_knowledge_record_state`, and `test_knowledge_writer_table` helpers. Complements `test_consolidation_pass.py` (in-pass worklist/gate/writer behavior).

## Evidence

- Verifies a passed consolidation closeout marks written, `stands`, card-only (`extended`/non-retiring `deleted`), and `stands`-family revisions `"consolidated"`, while keeping `unresolved` and unlisted families `"reviewed"`. [1]
- Verifies an unpassed consolidation closeout leaves written revisions `"proposed"`, read revisions `"reviewed"`, and emits both `NO_PASS_SENTENCE` and `NOTHING_CONSOLIDATED_SENTENCE` on closeout notes. [2]
- Verifies the `writers` view tallies all five consolidation outcome columns (`consolidationKept`..`consolidationUnresolved`) per writer of the read revision and records backing revision IDs in the report. [3]
