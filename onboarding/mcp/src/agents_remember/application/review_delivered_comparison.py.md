# mcp/src/agents_remember/application/review_delivered_comparison.py

## Governing Overview

[Owning route overview](../../../../overview.md)

## Purpose

Establish the pair a landed leaf delivered, open it as a comparison, and state whether the comparison on screen is that pair.

A leaf's enclosure records a delivery: the commit its successful landing produced and the memory content commit its closeout published. Those are delivery records, not review records, so the last numbered comparison a leaf holds may predate curation and honestly compare a base with itself. This module answers which pair the leaf actually delivered.

## Code Commentary

### The delivered pair

`delivered_pair` reads the enclosure's own cells: the recorded code base, the successful landing's commit, the recorded memory base and the closeout's memory content commit. `_landed_code` prefers the integration landing record and falls back to the closeout's code cell only for a leaf that was closed out and not landed, so a replayed landing is never silently replaced. `_delivered_memory` reads the closeout's memory cell and nothing else.

`_resolved_side` validates one cell: a full commit id that the repository its record names holds as a commit, whose tree is then derived. `_object_kind` asks the repository for the object's kind, so a tree or blob id cannot pass as a commit. Every failure is a refusal naming the side and the record cell, with the one restore action; nothing is substituted.

`_records_a_delivery` decides whether the enclosure claims a delivery at all from the closeout or integration status. A leaf that records none answers `None`, which keeps the caller's recorded default. A leaf whose delivered memory holds no layout marker is established for its source identities only; `_conversion_of` converts an unconverted recorded base through the shipped owner and refuses by name when it cannot, so a raw tree is never indexed as an empty before side.

### Opening and recording it

`delivered_comparison` returns the leaf's record whose four trees are exactly this pair, whatever its number, or records the pair through the comparison owner's `_record`; `record=False` answers only what the leaf already holds and writes nothing for a reader. `_exact_record` reuses the oldest exact record, so a delivered pair recorded before the last review record keeps that record and its number. `_opened` reopens the record's trees from its ids.

`delivered_default` is the resolution a landed leaf's review opens: it returns `tree_resolution` for the recorded pair, or the source-only legacy review (`_unconverted_delivery`) when the delivered memory holds no converted knowledge, in which case no comparison record is created.

### The notice

`delivered_notice` answers whether the shown record is the delivered pair: `delivered` when the four trees are exactly that pair, `differs` otherwise, and `unavailable` with the refusal's detail when the enclosure claims a delivery this read cannot establish. `_statement` is the one concise line: it names the shown number and the delivered code and memory trees and says nothing about whether an earlier record's own count or statement was right. Nothing here records, reviews or accepts anything.

`recorded_latest` answers the leaf's highest recorded comparison number, which the comparison menu lists; it is a different fact from the comparison the review resolved.

## Invariants And Boundaries

Reading the module establishes no review, curation or semantic acceptance of the delivered pair. It reads no `HEAD`, today's source-line tip or last review record as a delivered endpoint. A side Git cannot establish stays a named refusal, never a substitute, and a reader's notice read publishes no record.

## Evidence

- The delivered pair is the four enclosure cells, each resolved to its exact commit and tree. [1]
- The code candidate is the successful landing's commit; the closeout's code cell answers only where no landing happened. [2]
- The memory candidate is the closeout's memory content cell, and only it. [3]
- A commit cell must be a full commit id the repository holds as a commit before its tree is derived. [4]
- The repository's object kind decides commit versus tree or blob. [5]
- An unconverted recorded base is converted through the shipped owner or refused by name. [6]
- An exact record is reused at its own number; a pair no record holds is recorded by the numbering owner. [7]
- The default resolution is the delivered pair, or the source-only legacy review for unconverted memory. [8]
- The notice answers delivered, differs or unavailable and names the delivered identities. [9]
- The one line names the shown number and the delivered trees, and no verdict about a historical count. [10]
- The highest recorded number is a separate fact from the resolved comparison. [11]
