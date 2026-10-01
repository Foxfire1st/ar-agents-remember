# mcp/src/agents_remember/application/review_final_output_receipt.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The final-output receipt: one comparison generation bound to the output normal closeout and integration
actually delivered (ICR-R21@v1).** A generation records what a review *read*; the two are not the same
fact, and a reader holding only "a comparison was made" cannot tell whether the historical review opens
the pair the task landed. This module owns the record that closes that gap, and exactly three things:

| Owned thing | Operation | What it answers |
| --- | --- | --- |
| **The selection** | `select_review_generation` (`:182-213`) | which generation a leaf's final output is recorded against — the leaf's highest recorded `generation_index`, read from the generation store's own ordered refs |
| **The receipt** | `record_final_output_receipt` (`:258-299`) | the delivered code commit/tree, memory-content commit/tree and published knowledge identity, beside the two match verdicts and the one state |
| **The read-back** | `read_final_output_receipt` / `read_final_output_receipts` (`:429-485`) | one phase's record, plus the generations that came after it |

**Recording is not a gate, and nothing here can refuse a transaction.** The transaction owners call
`final_output_result_block` (`:726-768`) with the commits they already created; it measures, publishes one
small durable artifact and reads it back. A closeout or an integration that cannot record a receipt — no
generation, an unreadable store, a destination that refuses the write — still completes and carries the
concrete reason instead. That is deliberate: the packet adds no mandatory review gate to closeout, and a
recorder that could block the Git transaction it describes would be that gate wearing a receipt's name.

**Movement is recorded, never papered over.** A selected input that moves produces `state: moved` and a
statement naming the exact mismatch plus the remedy (publish a successor generation naming this one as its
predecessor). Freezing that successor is
`agents_remember.application.review_comparison_freeze.freeze_review_comparison`, whose options already
accept the predecessor ref, so the supersession is a value a reader **resolves** rather than a claim this
module makes — and the earlier receipt's bytes are never rewritten.

## Code Commentary

### Logic

**The selection reads the store's own order and nothing else.** `select_review_generation` (`:182-213`)
asks `read_generation_refs` — the readable generations, ordered by recorded index — and reports four
states: `selected`, `no-generation` (a task that was never reviewed is **not** a task whose review was
lost), `unreadable` (directories exist and none holds a readable manifest), and `ambiguous`.
`_selected` (`:216-246`) takes the last ref and refuses a tie: two bindings claiming one index with
different digests is `ambiguous` and records nothing, rather than binding whichever directory sorts last.
No live branch tip, no current HEAD and no clock participates.

**What a phase delivered is read out of the repositories that hold it.** `_delivered_output` (`:360-375`)
resolves each commit's tree with `_commit_tree` (`:420-423`, `git rev-parse <commit>^{tree}`), and treats
an absent memory commit as no memory output rather than as an empty one — the record's
`memory_output_state` carries that distinction.

**The published identity is read through the route a later task's planner uses.**
`_published_knowledge` (`:312-336`) resolves `declared_publication_location(contract)` and calls
`resolve_published_intent`; three states come back and are preserved, not flattened: `published` with its
`SnapshotIdentity`, `not-recorded` from the owner's own `state`, and `unusable` for anything else the
route refuses — carrying the owner's sentence verbatim.

**Assembly selects nothing and re-derives no identity.** `_assemble_receipt` (`:378-417`) copies the
generation's own values off the sealed manifest (including `binding_digest`, and `manifest_digest` from
the ref), computes the two match verdicts with the vocabulary's own functions
(`code_match_state`, `knowledge_match_state`) and asks `final_output_verdict` (`:416`) for the state,
instead of holding a second copy of the rule.

**Publication and read-back are the durable-evidence pair.**
`record_final_output_receipt` (`:258-299`) publishes through `publish_durable_evidence` under
`receipt_file_name` (`:252-255`) — `final-output-<leaf>-<generation-id>-<phase>.json` in the shipped
durable reports root — and returns the record beside `read_back_evidence`'s result. A phase measured
twice converges on one file and reports `replaced_existing`, because the record says what that phase
delivered **when it was read**.

**The read-back distinguishes absence from unreadability and names supersessions.**
`read_final_output_receipts` (`:451-485`) scans the store's refs once (`_superseding_in`, `:542-550`) and
then reads each phase's destination through `_read_destination` (`:498-539`): a missing file is
`not-recorded` naming the location it looked in, a file that cannot be validated is `unreadable` with the
error, and a valid one is `recorded` with its sha256 and its successors. `superseded_by` is **measured at
read time**, never written into the receipt — a receipt rewritten to point at its successor would be a
record edited after the fact.

**The consuming route is the reopen owner, and the wiring is in the module's own docstring.**
`read_final_output_receipt` (`:429-448`) names
`reopen_comparison_generation` as its consumer: the reopen reports what each phase recorded as part of
reopening one generation, which is how a reader of the recorded comparison sees the delivered output
beside the inputs it was compared against. The closed-leaf review route
(`application/review_committed_leaf.py`) reaches that reopen, so this reader is not a dead API.

**The transaction owners' projections.** `attach_prepared_selection` (`:667-681`) adds
`final_comparison_selection` to a closeout *preview* — read-only, refusing nothing, so a leaf that never
froze a comparison previews exactly as it did. `final_output_selection_block` (`:588-650`) makes exactly
one comparison, `prepared_is_reviewed_candidate`, and it is `None` when either side is unknown rather
than `True`: a prepared candidate that was never measured and a leaf with no selected generation are
**not** a prepared candidate that agrees with the review. `attach_closeout_receipt` (`:684-701`) and
`attach_integration_receipt` (`:704-723`) fire only on `ok` plus a real commit — a blocked, refused or
dry-run transaction carries nothing to record, and nothing is recorded. `final_output_result_block`
(`:726-768`) is the never-raising entry point: `recorded` with the identities and the read-back that
proves the bytes, `not-recorded` with the concrete reason, `not-applicable` for a series contract, which
owns no leaf comparison generation at all. `_recording_block` (`:771-804`) is the wire projection,
including the derived `statement`.

### Conventions

`__all__` (`:105-128`) publishes the selection/record/read dataclasses, the two operations per direction,
the two projection blocks and the three attachments. The three result types are **frozen dataclasses**
(a reading, not a stored wire shape) while the record itself is the pydantic `KnowledgeModel` re-exported
from the models module — one type, one import site. Private helpers are `_`-prefixed and each carries one
job: `_PublishedKnowledge` (`:302-309`), `_ReceiptInputs` (`:339-347`), `_DeliveredOutput` (`:350-357`),
`_ReadDestination` (`:488-495`). The routes are imported from their owners (`declared_publication_location`,
`resolve_published_intent`, `read_generation_refs`, `read_manifest`, `publish_durable_evidence`,
`route_review`) and none is re-implemented.

### Invariants And Boundaries

- **Nothing here can refuse a transaction.** The recording runs *after* the Git transaction and its
  contract write, inside the result builder; every failure becomes a state in the payload. The one
  raising function is `record_final_output_receipt`, and the transaction owners deliberately call the
  never-raising wrapper instead.
- **A phase that recorded nothing is still reported.** `read_final_output_receipts` returns one entry per
  phase, so "nothing was recorded" and "no phase was asked about" never read the same.
- **No silent fallback.** Selection reads the generation store; delivered identities are read from the
  commits the transaction *created*; the published identity is read through the publication route. A
  missing generation is a reported state, never a substituted HEAD or today's dataset.
- **Carried, never recomputed.** The record stores the owners' values and re-derives no identity; in
  particular `binding_digest`/`manifest_digest` are the generation's own.
- **One file per (leaf, generation, phase)**, so a leaf accumulates at most two files per generation it
  publishes and a repeated measurement converges on its own location.
- **Boundary: the reclamation owner has no shipped caller, and that is documented in the code rather than
  hidden.** `discard_final_output_receipts` (`:553-582`) states it plainly, names its consumers, and
  points at the same shape the generation owner landed
  (`application/review_comparison_reclamation.py` is likewise a named owner no automatic caller invokes).
  The reason is in the sentence: the receipt is *retained evidence* — ICR-R21@v1 exists so a later reader
  can open the comparison the task landed — and deleting it during ordinary closeout/cleanup would destroy
  the artifact the requirement asks to survive. **This is routed debt: L21 → R25**, with the R11
  retention/release route secondary; reclamation is *not* automatic at this candidate.
- **Boundary: the receipt's `moved` state does not block the transaction.** Closing that gap is the
  packet's "new generation or explicit supersession" remedy, recorded in the statement; adding a gate was
  forbidden by the packet's preservation boundaries.
- **Boundary: an absolute `task_root`/`contract_path`/`published_knowledge_path` is recorded as produced.**
  A relocated coordination root therefore leaves a receipt whose paths no longer resolve where they did;
  the record's identities remain readable, and relocation-stable resolution is ICR-R12/R13's boundary.
- **Boundary: direct in-process callers of `git_worktree_manager.closeout_result` see no receipt.** The
  receipt is attached at the MCP tool result (`application/worktree_tools.py`), which is the production
  result surface; `layers.toml` ranks `application` above `worktrees`, so putting the block in
  `worktrees/modules/closeout.py` would add a layering violation, and the only other production caller
  (`worktrees/modules/cli.py`) is unreachable from any shipped console script.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstrings and functions and in the cases that
drive the real tools. The three details a reader should carry: **the record is a measurement, not
history** (a phase measured twice replaces its own file, while the generation's manifest and retained
bytes are never rewritten); **the selection rule is the store's own order** and an ambiguous tie records
nothing; and **`prepared_is_reviewed_candidate` is `None` when either side is unknown**, because an
unmeasured candidate is not an agreeing one.

- **The module's own statement of the gap it closes, the three things it owns, and why recording is not a gate.** [1]
- The published surface: the record re-export, both read directions, the projections and the three attachments. [2]
- The one durable file-name prefix, one file per leaf, generation and phase. [3]
- **The four selection states, and why "never reviewed" is not "review lost".** [4]
- One published receipt: the durable artifact, the record, and the read-back that proves it. [5]
- **The read-back's three states beside the successors — supersession measured at read time, never written into the record.** [6]
- **The selection rule: the store's own order, with `unreadable` and `no-generation` as separate answers.** [7]
- **The refusal that keeps a tie from being resolved by directory order.** [8]
- The one durable destination a phase publishes to. [9]
- **Measuring one phase and publishing it: the owners' values, the read-back, and `replaced_existing` rather than a hidden rewrite.** [10]
- **The published-knowledge channel read through the route a later planner uses, with the owner's own three states and sentence.** [11]
- The inputs one receipt is assembled from, and the delivered identities read out of the repositories that hold them. [12]
- **Assembly that selects nothing and re-derives no identity, asking the vocabulary for the one verdict rule.** [13]
- The tree of a commit, read from the repository that holds it. [14]
- **The reader, and the docstring that names the reopen owner as its consuming route.** [15]
- **Reading every phase in order, with the supersession set measured once.** [16]
- **A missing file is `not-recorded` naming the location, a broken file is `unreadable` with the error — never conflated.** [17]
- Every readable generation that came after the one a receipt names. [18]
- **The named reclamation owner, and the code's own plain statement that no shipped route calls it and why (routed to ICR-R25@v1, secondary R11).** [19]
- **The prepared-work projection: the one comparison it makes, and `None` rather than `True` when either side is unknown.** [20]
- A manifest that cannot be read back is reported in the block itself rather than raised. [21]
- **The three attachments and the `ok`-plus-a-real-commit gate that keeps a failed transaction from carrying a receipt.** [22]
- **The never-raising entry point and its three states, including `not-applicable` for a series contract.** [23]
- The wire projection of a published receipt, including the derived sentence. [24]
- **The three production call sites: closeout preview, closeout apply and integration.** [25]
- **The reopen owner's fourth channel, which is what makes the reader a production consumer.** [26]
- The generation store's own order and the manifest this module reads and never rewrites. [27]
- The freeze route that publishes the successor a `moved` receipt's remedy names. [28]
- The publication route whose declared location the published channel is read at, and the read route that resolves it. [29]
- The durable-evidence pair every receipt is published and read back through. [30]
- **The cases that drive the real tools: the conforming pair, the non-conforming dataset, the moved candidate with a successor, the leaf with no generation that still closes, and the forged verdict.** [31]
- **The case that measures reclamation and leaf scoping through the named owner.** [32]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a task root and a repository path the
worktree contract names, and it resolves the declared publication location inside the same repository
boundary; the relocation boundary that follows from a recorded absolute path is stated above and is the
same one ICR-R12/R13 own for the generation record.

No meaningful cross-repo references found.
