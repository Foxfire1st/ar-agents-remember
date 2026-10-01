# mcp/src/agents_remember/application/knowledge_merge.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The third composition seam of the knowledge substrate**: the guarded common-base merge, beside the single candidate write in `application/knowledge.py` and the candidate-lifecycle/publication seam in `application/knowledge_snapshot.py`. It exists for the same reason as the snapshot seam — a merge is a different composed operation from a single candidate write, and keeping it apart leaves each entry point readable as one intent.

Nothing here decides authority and nothing here holds durable state. It resolves a base claim, merges, and returns the typed result unchanged. Storage ranks below application, so a lower owner — the worktree or lifecycle package that would call a merge — receives `agents_remember.models.knowledge` values and never an import of this module or of the store.

**The adapter was *callable rather than wired*; CYCLE-02 wired it, and the non-claims it made about Git still hold.** No Git merge driver is installed, no attribute is configured and no commit is created anywhere on this path — that has not changed and is not what wiring meant. What changed is who calls it: the sync transaction now reaches this module through `merge_conflicted_stages`, the dataset half of a conflicted knowledge database's settlement, so the seam is no longer reachable only by a caller that already knew to compose `resolve_knowledge_merge_base` with `merge_resolved_knowledge_datasets` by hand. The Git half of that settlement lives in `worktrees/knowledge_conflict.py` and cannot live here, because a module under `worktrees/` may not import the memory domain; this half reads the three materialised stages' identities, proves the base and publishes the union, and returns a typed settlement rather than a compatibility verdict.

**CYCLE-02's remainder changed what the settlement *is*, and it is the reason this card reads differently.** `merge_conflicted_stages` used to answer a bare boolean: the adapter's own refusal and the engine's row-level `MergeConflict` were reduced to `False`, so the public sync could report only `sync-resolution-required` with `files: ["knowledge.sqlite"]` while the explanation sat one layer below the agent. It now returns `KnowledgeStageSettlement(settled, conflict, refusal, detail)`, carrying the engine's typed values **verbatim** — including the fact that nothing here re-renders them, because a caller that re-rendered the diagnosis would be reimplementing the thing this exists to preserve. Both failure shapes are reported: a stage that never reached the adapter carries the seam's own `detail` (`_stage_inputs`), and a stage the adapter answered carries the refusal or the conflict and leaves `detail` empty.

## Code Commentary

### Logic

Two entry points, each a rename of one storage operation onto the models vocabulary, each returning the storage layer's typed value unchanged:

- `resolve_knowledge_merge_base(request)` delegates to `memory.knowledge.merge_base.resolve_merge_base` and returns a resolution for shorthand — or `None` — so a caller composing a tool response is not handed a second resolution shape.
- `merge_resolved_knowledge_datasets(request)` delegates to `memory.knowledge.merge.merge_knowledge_datasets` and returns the whole `MergeOutcome`: the coverage of both deltas and the publication state when a destination was named. A resolution is returned as the proven value; a failure is returned as the typed refusal, so a caller branches on one code instead of catching an exception.

A third entry point is the driving half CYCLE-02 added, and it is the reason the lower layer can call this module without importing it:

- `merge_conflicted_stages(destination, stages, repository_root, commits, reconciliations=())` takes three materialised index stages and returns a `KnowledgeStageSettlement`. It reads each stage's identity with `dataset_identity`, opens the left stage read-only to decode the one `repository` row the base claim is about, composes the two entry points above, and answers `settled=True` only for `structurally_merged` **and** `published`. `KnowledgeStageSettlement` is the whole contract now: `settled` is the only success there is, `conflict` is the engine's row-level attribution (table, operation and the exact refused key), `refusal` is the typed explanation with the action it advertises, and `detail` is this seam's own reason for the cases that never reached the adapter — a stage that is not a dataset, an unreadable namespace row — and it is empty whenever the adapter itself answered. `_stage_inputs` is the extraction of those four never-reached-the-adapter reasons, split out so the identity read stays readable as one intent and so each `False` the old boolean collapsed now names which fact was missing.
- `reconciliations` is the sequence of authored decisions the caller has already accepted, and the **only** way an authored resolution enters the merge. It is a **sequence rather than one decision** because a retained merge is answered one conflict at a time and the answer to the second has to carry the first: with only the newest decision carried, a two-conflict merge alternates between the same two rows forever, re-offering a decision that has already been made and already had its effect. This layer still decides nothing about them — the tuple is passed through unchanged, and the adapter still refuses every row no decision named. `ConflictCommits` groups the three commits one conflicted merge spans, because the adapter requires all three together: a base claim naming two of them would not be a claim at all.

`KnowledgeMergeSeamDefect` is the one internal state the layer below makes unreachable — a refusal and a value both absent — and it is a defect rather than a caller-facing refusal for exactly that reason.

### Conventions

- Every function is a pure delegation with a docstring that states the boundary it does not cross; the module keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without an application-level wrapper type — the same shape the two sibling seams use. `KnowledgeStageSettlement` is the one exception and it is a *union of the storage layer's own values plus this seam's reason*, not a re-rendering: the conflict and the refusal it carries are objects the engine produced.
- The one exception to "pure delegation" is `merge_conflicted_stages`, and it is a structural one rather than a stylistic one: it exists here because the module that owns the Git side of the conflict may not import the memory domain, so this is the lowest layer that can read a dataset's identity at all. It still decides nothing about the merge — and it decides nothing about the authored decision either, which travels through it untouched.
- The module docstring states the non-claim (no driver, no attribute, no commit) rather than leaving it to be inferred.
- A reason this layer owns is named as `detail` and kept disjoint from the engine's own values, so a reader can always tell "the adapter refused this" from "this never became a dataset".

### Invariants And Boundaries

- **No authority is conferred here.** The request models carry the identities a caller admitted; approval, acceptance and task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner receives `models.knowledge` values.
- **The result carries no compatibility verdict.** A `structurally_merged` outcome is a statement about the candidate's structure and nothing about whether the merged knowledge is correct. `settled=True` is that same structural fact plus the publication, and adds no verdict of its own.
- **The seam is wired into exactly one caller, and the Git non-claims survive the wiring.** `worktrees/knowledge_conflict.py` imports `merge_conflicted_stages` and `ConflictCommits`; it is the one non-test importer in `mcp/src`, so the two delegating entry points above are now reachable from production code as well. No Git merge driver, no `.gitattributes` attribute and no commit were added by that change: the transaction still lets Git declare the conflict and then republishes the union itself.
- **A stage the adapter will not decide stays the agent's, and it now says why.** `settled=False` rather than raising or guessing, with the engine's own conflict or refusal carried out with it, so a schema disagreement narrows the agent's work instead of hiding it.
- **The diagnosis is carried, never re-rendered.** Every value in `KnowledgeStageSettlement` is the engine's or this seam's; nothing here reformats, summarises or re-keys the refused row, because a re-rendered diagnosis is a second implementation of it.

### Todos

None recorded for this slice. The wiring that `merge_conflicted_stages` completes was a carried limitation of the earlier increment rather than a defect: the requirement had said this module supplies evidence and a callable boundary, not production configuration, and the separately reviewed change that turned it into a driver is the one recorded above.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The base-resolution entry point and its refusal-or-resolution contract. [1]
- The merge entry point, including the carried statement that the result holds no compatibility verdict. [2]
- **The driving entry point: three materialised stages in, one typed settlement out, with the caller's one authored decision passed through untouched.** [3]
- **The settlement that replaced the boolean: the only success, the engine's conflict, the typed refusal, and this seam's own reason for a stage the adapter never saw.** [4]
- **The four reasons a path never reached the adapter, each named instead of collapsed into one `False`.** [5]
- **The three commits one conflicted merge spans, grouped because the adapter's base claim needs them together.** [6]
- The defect the layer below makes unreachable. [7]
- The two storage operations this seam delegates to. [8]
- The request and outcome vocabulary this seam takes and returns unchanged. [9]
- **The authored decision this seam carries without deciding anything about it.** [10]
- The two sibling seams this module sits beside. [11]
- The layer ranks that make a lower owner consume models rather than this module. [12]
- **The one non-test importer this module has, and the Git half of the settlement that cannot live here — including the single-path reconcile entry point that carries the authored decision back in.** [13]
- The unit node that drives the conforming merge end to end through the public operations. [14]
- **The integration node that drives the structured diagnosis and the authored reconcile through the real transaction.** [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
