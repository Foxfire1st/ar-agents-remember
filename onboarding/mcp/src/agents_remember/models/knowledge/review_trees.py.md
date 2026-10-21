# mcp/src/agents_remember/models/knowledge/review_trees.py

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Define the durable four-tree comparison record and the distinct leaf-wide, cards, lane and file tree-view response carriers.

## Code Commentary

The comparison schema remains ar-review-tree-comparison/v1. Each side names its repository and tree plus an optional commit or review pin under refs/ar/review; these declarations do not enforce commit/ref exclusivity or perform Git reads. A converted base records its memory commit, conversion version, anchoring code commit and produced tree, with no database copy.

same_trees compares task/leaf, four repository/tree pairs and converted base. It ignores number, timestamp and commit/ref spelling. Number zero represents closed-leaf committed endpoints that need no independent pin or comparison record.

Knowledge sides distinguish available, unavailable-history and legacy-unavailable, carrying complete/partial index state and problems. Reopened code sides distinguish available from unavailable-history. Standalone file/record/source/tree memory-diff carriers remain exported; their existence does not add a knowledge_diff field to ReviewTreesResult.

ReviewWorklistView carries source/bound metadata, item/history documents, gate-owned item verdicts, linked changes and incomplete items. Its code_changes attribute is excluded from serialization; the root result has a separate public code_changes field. Application owners project document keys and establish binding: the DTO does neither.

The root result carries currentness/worklist/code facts for the leaf-wide read, entries for the focused invariant cards, lane for a files-lane read or file_classification for one file. Optional payloads are carriers, not a claim that all reads populate every field. The earlier 637 KB leaf-wide excerpt measurement is historical motivation for focused entry reads, not a measurement of this candidate.

ReviewEntryMemoryState now accompanies a card read. It names the after memory tree and available/unavailable state; available carries the index own complete/partial state, while unavailable can name the failed read in reason. Entries may still be returned without values. The model supplies no state-combination validator authenticating these producer claims.

## Invariants And Boundaries

All shapes use the shared frozen bounded model conventions. They record trees, optional refs/commits, values and reasons, never a retained database. Typed refusal, optional fields, source/bound flags and item verdicts do not establish CODE or MEMORY approval. The standalone diff types and absence of an embedded knowledge_diff field predate A4-F5.

## Evidence

- Schema, review-pin namespace and side/conversion addresses remain distinct. [18]
- Comparison identity excludes number, timestamp and pin spelling. [19]
- Knowledge and code sides retain explicit availability and partial-index evidence. [20]
- The internal worklist code facts are excluded while the public response keeps its own payloads. [21]
- A card memory read names its after tree, completeness or unavailable reason. [22]
