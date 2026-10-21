# mcp/src/agents_remember/cli/dashboard_review_reads.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Bind recorded intent, catalogue and tree-view answers to their exact question and retained input closure, while returning fresh failed reads without keeping them.

## Code Commentary

recorded_answer_sources accepts a valid leaf address and reads the leaf enclosure. Its dependencies are contract bytes, comparison/generation directory listings, worklist bytes or absent path, and existing code/memory object stores. It neither authorizes arbitrary paths nor substitutes a live HEAD.

Before reuse, _recorded_sides deduplicates all four repository/tree pairs across retained records. _trees_still_readable traverses their closures with missing-object reporting, then _object_bodies_readable consumes exact batch bodies, validating identity/length/newline framing and complete output. A stable object census cannot mask a removed or unreadable descendant.

Recorded intent uses the full serialized request key and may reuse that recorded question while the enclosure remains live. Ordinary intent requests produce fresh answers. Entry catalogues include optional comparison number in the key, but retain the closed-enclosure rule; tree keys include every query field and ordinary working-view queries produce fresh answers. Explicit recorded/numbered tree questions still pass the closed-enclosure check before reuse.

The common _answer path requires the proper leaf record, the applicable closed-enclosure condition, readable recorded closures and the same observed input set before delegating to the app-owned RecordedAnswerReuse. A failed condition calls the same producer fresh rather than serving an older inventory.

_keepable_tree_view rejects typed tree responses with any unavailable-history side, and card-memory failure when the after knowledge side is available. These describe transient read/index failures over readable recorded inputs and must be retried next time. Missing entry_memory or available memory can be kept; legacy-unavailable remains an immutable record fact. Non-ReviewTreesResult values are admitted by this predicate. Summary caching belongs to IntentSummaryCache.

## Invariants And Boundaries

Working-view answers are computed fresh. Recorded question keys and dependency validation govern reuse, not acceptance or file writes. A failed read cannot become permanent merely because its record inputs stayed unchanged; an unavailable legacy state is distinct from such a failure.

## Evidence

- Valid leaf addressing supplies exact contract/directory/worklist/store dependencies. [5]
- Recorded closures and object bodies are checked rather than inferred from counts. [6]
- Intent, numbered entries and tree questions keep their own recorded/closed rules. [7]
- The common path validates record/closure before reuse. [8]
- Transient index/card-memory failures are returned but not retained. [9]
- Every query selector participates in the tree key. [10]
