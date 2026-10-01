# mcp/src/agents_remember/application/review_sync_rebinding.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The rebinding record: one comparison generation measured against the exact source/knowledge pair a
managed sync resolved (ICR-R22@v1).** A comparison generation records what a review *read*; a managed
sync then moves both of the things that generation bound — the candidate source tree captured from the
leaf's worktree, and the knowledge dataset at the repository's declared publication location. A reader
holding only "a generation was frozen" cannot tell whether that generation still describes the pair the
leaf now holds, which is the packet's conforming example, and its non-conforming example is exactly the
state where the old review keeps reading as untouched. This module owns the missing step, and exactly
four things:

| Owned thing | Operation | What it answers |
| --- | --- | --- |
| **The measurement** | `record_review_sync_rebinding` (`:271-313`) | the generation's reviewed identities beside the pair the sync resolved, and the match each channel earned |
| **The reason nothing was measured** | `rebinding_result_block` (`:316-373`) | which state the sync was actually in, in this block's own vocabulary, instead of a blanket claim about completions |
| **The read-back** | `read_review_sync_rebinding` (`:376-438`) | what is recorded for one generation, as `recorded` / `not-recorded` / `unreadable` |
| **The generation check** | `rebinding_names_the_generation` (`:441-476`) | whether the record at that location describes *this* generation or some other one |

**It measures owners' values; it re-implements none of them.** The generation being judged is selected
from the generation store's own order (`select_review_generation`, cited below), its reviewed identities
are read from its own sealed manifest, the resolved source side is the shipped capture owner
(`capture_future_code_candidate`, cited below) re-derived after the sync, and the resolved knowledge side
is the ordinary read route's own answer at the declared publication location
(`resolve_published_intent` reached through `declared_publication_location`, both cited below). The
record's own verdict comes from one function in the model module
(`review_sync_verdict`, cited below) rather than from a second copy of the rule.

**Nothing here can refuse a sync.** The transaction has finished its Git work and written its contract by
the time this runs, and it is called with the result that fact produced. A capture that fails, a leaf with
no published generation, an unreadable manifest and a location holding nothing are all *states* this
reports rather than exceptions it raises; a rebinding that could fail a completed sync would be a
mandatory review gate on the sync wearing a receipt's name.

**Movement is recorded, never papered over, and never substituted.** The record supersedes nothing by
itself: the remedy it names is a successor generation frozen with the judged generation as its `parent`
(`freeze_review_comparison`, cited below), so the supersession is a lineage a reader resolves rather than
a claim this record makes. Reclamation is `discard_review_sync_rebindings` (`:505-528`) — a derived
measurement, so a discarded record reads back as `not-recorded` naming the location it looked in, while
the generation's own manifest and retained bytes are untouched here.

## Code Commentary

### Logic

**What counts as a completed sync is three checked facts, not an inference from payload keys.**
`resolved_pair_completed` (`:196-220`) requires the operation to be `worktree_sync`, `ok` to be true, and
the state to be one of the three in `_CARRYING_SYNC_STATES` (`:155-161`) — `synced`,
`sync-pass-completed-memory-skipped`, `sync-pass-completed-source-moved-again`. `already-current` is
deliberately **not** a carrying state: that result reports that the recorded pair and the participating
work branches already contained the official line, so nothing was carried and there is no resolved pair to
measure a review against. The success conjunct is carried even though every producer of those three states
returns zero today, because a carrying state beside `ok: false` is a result this tool must not measure.

**Every state that carried nothing is described by its own entry.** `_CARRIED_NOTHING` (`:167-193`) is a
table rather than a ladder, one row per state, each pairing a block state with the store fact it observed:
`would-sync` → `preview`, `already-current` → `no-movement`, `sync-resolution-required` → `not-resolved`,
`sync-cancelled` → `cancelled`, `memory-sync-choice-required` → `choice-required`. A state outside the
table answers `not-measured` naming the state it was actually given. This is the shape that replaced a
single false sentence ("this result is not a completed sync"), which was false for several of these.

**A source side that could not be captured produces no record at all.** `record_review_sync_rebinding`
(`:271-313`) returns `None` in exactly two cases — the payload is not a completed sync, or the leaf
published no comparison generation — and raises the private `_ResolvedSourceUnmeasurable` (`:141-146`)
when `_resolved_capture` (`:681-700`) reports that the leaf's own capture owner refused. No candidate tree
is invented for it: the resolved source half does not exist to be bound, and an identity nobody observed
is the invented input this vocabulary refuses to carry.

**The record is assembled from owner values and its verdict from one rule.** `_assemble` (`:641-678`)
copies the generation's own manifest values (id, index, binding digest, manifest digest, reviewed baseline
and candidate trees, the reviewed knowledge state and its digest), reads the resolved knowledge side
through the ordinary route, computes the two channel matches with the vocabulary's own functions and asks
`review_sync_verdict` for the state — so a writer and the record's validator cannot disagree about the
rule. `_resolved_knowledge` (`:703-727`) converts the read route's own answer into
`SyncKnowledgeObservation`: `published` with the dataset identity exactly when a dataset was read, and the
route's own `not-recorded` / `unusable` state and sentence otherwise.

**The read-back distinguishes three facts that used to be one.** `read_review_sync_rebinding` (`:376-438`)
answers `recorded` with the record, its canonical `sha256:<hex>` reference (`_digest`, `:730-733`) and its
own statement; `not-recorded` with the location it looked in, saying plainly that a record reclamation
discarded and one that was never written read the same there; and `unreadable` with the reader's own
reason. A present-but-broken artifact is never reported as an absent measurement.

**The generation check is the half the record's own validator cannot supply.**
`rebinding_names_the_generation` (`:441-476`) compares the record against the *store*: the generation id,
index, binding digest, the reviewed baseline and candidate trees, and the reviewed knowledge state and
digest must all be the ones the leaf's published manifest holds. A record whose fields and verdict were
forged together is still internally consistent — comparing two fabricated identities is still a
comparison — so this check is what makes `read_review_sync_rebinding` evidence of a measurement rather
than proof that the measurement describes this generation.

**Why nothing was bound is its own vocabulary, and it does not borrow the selection owner's words.**
`_nothing_to_bind_block` (`:534-595`) separates three families: the transaction carried no pair (the state
table), the result is not a `worktree_sync` at all (`not-applicable`), or the pair is carried and this leaf
has no generation to measure against it. `_no_generation_block` (`:597-639`) gives that last family one
entry per selection state — `no-generation`, `generation-selection-ambiguous`, `generation-unreadable` —
while the selection owner's own state and sentence travel beside them under `selection_state` and
`selection_detail`. The reason is stated in the code: `unreadable` from `select_review_generation` means
the *generation manifests* could not be read, while `unreadable` from `read_review_sync_rebinding` means
the *rebinding artifact* could not be read, and one key must not carry two meanings on two surfaces.

**The consuming route is the reopen owner, and the leaf-wide pair is the acceptance route.**
`read_review_sync_rebindings` (`:479-502`) reads every rebinding recorded for a leaf's generations in the
store's own generation order, and `discard_review_sync_rebindings` (`:505-528`) removes exactly the
prefix-matching derived artifacts. Both are documented in the code as having **no mounted tool caller**:
the per-generation read is reached in production from `reopen_comparison_generation` (cited below), while
the leaf-wide reader and the reclamation owner are what an acceptance reader or a curator draining a
leaf's history holds. Recording that is the honest alternative to implying a caller that does not exist.

### Conventions

`__all__` (`:96-112`) publishes the two dataclasses, the read type, the exported constant pair, the four
operations and the two readers. `ReviewSyncRebindingPublication` (`:232-238`) is the durable artifact
beside the record and the read-back that proves it; `ReviewSyncRebindingRead` (`:241-262`) carries the
three read states plus the destination, the sha256 and the detail, and offers `covers_resolved_pair` so a
consumer branches on one predicate instead of re-deriving the rule. `ReviewSyncRebinding` itself is the
pydantic `KnowledgeModel` re-exported from the models module — one type, one import site. The private
helpers are `_`-prefixed and each carries one job: `_ResolvedCapture` (`:223-229`),
`_ResolvedSourceUnmeasurable` (`:141-146`). The one durable file name is derived once, by
`rebinding_file_name` (`:265-269`), as `review-sync-rebinding-<leaf>-<generation-id>.json` under the
shipped durable reports root.

### Invariants And Boundaries

- **No refusal reaches the sync.** `rebinding_result_block` (`:316-373`) catches the unmeasurable-capture
  control-flow exception and the storage/os/runtime/value errors, and writes a state onto the payload in
  each case. Nothing in this module can block the Git transaction it describes.
- **No invented identity.** A capture the worktree refused publishes no record; an identity is carried
  exactly when a dataset was read; a resolved identity travels only on the channel that moved.
- **One file per (leaf, generation), not per sync.** A later sync over the same generation replaces that
  answer instead of accumulating a second one beside it, because the question is "does the review still
  describe what the leaf holds".
- **The supersession is the freeze owner's act.** The record names
  `freeze_review_comparison` (cited below) as its remedy and performs nothing itself; it rewrites no
  manifest and relabels no earlier result as covering the moved inputs.
- **Boundary: the leaf-wide reader and the reclamation owner have no shipped caller, and that is recorded
  in the code rather than hidden.** Both docstrings state it and name what will hold them (the acceptance
  reader, or a curator draining a leaf's history). This is routed debt, not an oversight.
- **Boundary: paths are recorded as produced.** `task_root` and `contract_path` travel as the contract
  gave them, so a relocated coordination root leaves a record whose paths no longer resolve where they
  did; the identities remain readable.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstrings and functions and in the cases that
drive the real tool. The three details a reader should carry: **the record's verdict is derived from one
rule shared with its own validator**; **a sync that cannot be measured is still returned unchanged**, with
the reason on the payload; and **the record is checked against the store before it is read as a
measurement of a generation**, because a forged record is internally consistent.

- **The module's own statement of the gap it closes, the owners it reuses, and why it can never refuse a sync.** [1]
- The published surface: the record re-export, the two dataclasses, the readers and the block. [2]
- The one durable file-name prefix, one file per leaf and judged generation. [3]
- **The one action that produces a comparison current with the resolved pair, stated once.** [4]
- **The three states in which the transaction carried the official line, and why `already-current` is not one.** [5]
- **The five states that carried nothing, each with the store fact it observed.** [6]
- **The three checked facts, including the success conjunct carried for a producer that does not exist yet.** [7]
- The resolved source side as a state, with the named reason it could not be measured. [8]
- One published rebinding: the durable artifact, the record, and the read-back that proves it. [9]
- **The read-back's three states, with the predicate a consumer branches on.** [10]
- The one durable destination a generation's rebinding is published to. [11]
- **Measuring one finished sync and publishing it, and the two cases that publish nothing at all.** [12]
- **The never-raising entry point the sync tool calls, and the states it writes instead of raising.** [13]
- **Reading one generation back: `recorded`, `not-recorded` naming the location, `unreadable` with the reason.** [14]
- **The check against the store that a forged-but-consistent record cannot pass.** [15]
- **The leaf-wide reader, and the code's own statement that no mounted tool calls it yet.** [16]
- **The named reclamation owner: a derived measurement whose removal costs no retained input.** [17]
- **The carried-nothing vocabulary, one entry per observed state.** [18]
- **The generation vocabulary in this block's own words, with the selection owner's answer carried beside it.** [19]
- Assembly that selects nothing and re-derives no reviewed value, asking the vocabulary for the one verdict rule. [20]
- The shipped capture owner's refusal converted into a state rather than an exception. [21]
- **The resolved knowledge side read through the route a later planner selects knowledge with.** [22]
- The canonical `sha256:<hex>` reference of one published artifact's bytes. [23]
- **The one verdict rule the writer and the record's validator share.** [24]
- The sealed record itself: the reviewed pair, the resolved pair, both channel matches and the state. [25]
- The generation store's own order and the manifest this module reads and never rewrites. [26]
- The selection rule this record names, owned by the final-output receipt module. [27]
- The freeze route that publishes the successor this record's remedy names. [28]
- The durable-evidence pair every rebinding is published and read back through. [29]
- **The shipped capture owner whose add-all tree is the resolved source side.** [30]
- The publication route whose declared location the resolved knowledge side is read at. [31]
- **The production call site: the sync tool's result, after its Git work and contract write.** [32]
- **The reopen owner's fifth channel, which makes the per-generation reader a production consumer.** [33]
- **The live read that renders the measurement, and the movement that outranks a carried identity.** [34]
- **The cases that drive the real production sync tool: the movement measurement, the clean union with parked WIP returned, the forged verdict, every carried-nothing state, the locator clause, and the reader after its own reclamation.** [35]
- The live code/memory worktree pair the managed-sync cases are built on. [36]
- **The read-side cases: the live read's rendering, the uncompared knowledge channel, the unusable record, the carrying-state-as-failure, and the validator refusals.** [37]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a task root, the leaf's own worktree and
a publication location that all lie inside the contract's own repository boundary; the relocation boundary
that follows from a recorded absolute path is stated above.

No meaningful cross-repo references found.
