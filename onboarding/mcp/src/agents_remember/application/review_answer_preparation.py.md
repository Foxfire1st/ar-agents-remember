# mcp/src/agents_remember/application/review_answer_preparation.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Name the exact inputs a recorded comparison's answers are a function of, and serve those answers again unchanged while every input holds — for a closed leaf's record, and for a live leaf's whole reviews on the witness of the comparison they name.

## Code Commentary

One place decides, per read, whether an answer is a function of a record or of a working view, so the three routes — the whole intent request, an entry catalogue, a tree view — cannot disagree about which reads are reusable. The keys are the exact questions: the whole intent request, the task context of a catalogue, and every field that selects a tree view.

`recorded_answer_sources` accepts a valid leaf address and reads the leaf's record. Its dependencies are contract bytes, comparison and generation directory listings, worklist bytes or absent path, and existing code and memory object stores. It neither authorizes arbitrary paths nor substitutes a live `HEAD`.

Before reuse, `_recorded_sides` deduplicates all four repository/tree pairs across retained records. `_trees_still_readable` traverses their closures — through `_closure_still_readable`, `_prove_closure`, `_rewitnessed_closure` and the closure-proof store — with missing-object reporting, then `_object_bodies_readable` consumes exact batch bodies, checking identity, length and the newline framing of the whole batch. A stable object census cannot mask a removed or unreadable descendant.

A live leaf's whole reviews and its subject catalogue are kept too, on `LiveWitness`: the comparison's number and four trees, the inputs its witness observed, and a `current` predicate that proves the working views still capture to those trees. The witness is never loaded from disk; `_live` keeps a live answer only when it names the same comparison and the witness still holds once the answer was made, re-observing every read it made before any reuse, and with no witness proven the answer is computed fresh. A page of a collection, or a refresh against a binding, is computed each time.

`_AnswerPolicy` states one answer kind's rules instead of scattering them: whether it must be closed, whether it observes the capture worktrees' existence, which answers are keepable at all, whether it persists, how it is prepared and decorated, and whether it is an invariant's detail. Detail answers — an invariant's cards or its review — are kept in a separate store, because a leaf has as many as it has changed invariants and one store would push the page's opening answers out of it.

`_answer` requires the recorded contract, the applicable closed-enclosure condition, readable recorded closures and the same observed input set before delegating to the app-owned reuse store; a tree the answer was computed from having gone means the kept answer must never stand in for the fresh read that reports the loss. Persisted envelopes never supply paths to open or predicates to probe.

`_shared` runs one computation per exact question in flight; a second asker waits, takes a copy and replays the reads it consumed, so its own recorder names the same inputs. The computation belongs to the flight rather than to its first asker, and a read whose askers have left keeps nothing.

`stale` keeps the explainer's staleness of one recorded comparison on every read it made — the leaf's documents, the binding, the grades, the revisions' manifests and the admitted sources, listings included — each re-observed identical before any reuse.

`_keepable_tree_view` rejects typed tree responses with any unavailable-history side, and card-memory failure when the after knowledge side is available: those describe transient read or index failures over readable recorded inputs and must be retried next time. A missing entry memory, or one that is available, can be kept; a legacy-unavailable memory remains an immutable record fact. Non-`ReviewTreesResult` values are admitted by this predicate, and summary caching belongs to `IntentSummaryCache`.

## Invariants And Boundaries

Working-view answers are computed fresh. Recorded question keys and dependency validation govern reuse, not acceptance or file writes. A failed read cannot become permanent merely because its record inputs stayed unchanged; an unavailable legacy state is a distinct fact from such a failure. A live answer is kept only on a proven witness, and the witness is proof of the working views, never a stored claim about them.

## Evidence

- Valid leaf addressing supplies exact contract, directory, worklist and store dependencies. [5]
- Recorded closures and object bodies are checked rather than inferred from counts. [6]
- Intent, numbered entries and tree questions keep their own recorded and closed rules. [7]
- The common path validates the record and the closure before any reuse. [8]
- Transient index and card-memory failures are returned but not retained. [9]
- Every query selector participates in the tree key. [10]
