# mcp/src/agents_remember/models/knowledge/merge.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The common-base merge vocabulary: explicit inputs, coverage facts and one structural outcome.** A merge is a *structural* operation over three datasets that already exist — an explicit common base, two sides derived from it, and a private candidate produced from the first side.

**Nothing in this module can carry a judgement about whether the merged knowledge is *correct*.** There is no compatibility, acceptance, approval or "harmless" field, and the one non-refusal state is named `MERGE_STATES = ("structurally_merged",)` because that is the entire claim it makes. This is the shape requirement `KS-R05@v1` names for the result, and it is enforced at construction rather than by convention: the model validators make the mixed states unrepresentable.

**Authored decisions enter here, and each is a decision about one row rather than a policy.** `AuthoredReconciliation` is the vocabulary for the caller's own explicit reconciliation of exactly one conflict the engine refused: `table` and `record_id` name that row as the refusal rendered it, `decision` is one of `keep-left` / `keep-right`, and `MergeRequest.reconciliations` carries the ones the caller has accepted into the merge. `expressible_decisions(conflict)` is the single place that answers which decisions a conflict admits, so the refusal, the public sync response and the merge's own conflict callback cannot answer it differently. This is the half of CYCLE-02's remainder that had to live in the vocabulary: the engine already produced the exact diagnosis, and the agent needed a way to answer the row that diagnosis names. The field is a **tuple** even though each member is one row, because a retained merge is answered one conflict at a time and the answer to the second has to carry the first: with a single decision per attempt a two-conflict merge alternates between the same two rows forever, re-offering a decision that has already been made and already had its effect.

**Whether a row-less decision is offered at all is a measured fact this vocabulary carries, not something the conflict code can say.** A referential conflict arrives under one code in two orientations — the arriving side added a broken reference, or it removed a row the retained side still cites — and `keep-left` is a retraction of rows the arriving delta *inserted*, so it is available in the first and provably unavailable in the second. `RetractionPrecondition` is that one bit (`arriving_insertion` / `no_arriving_insertion`) and `MergeConflict.precondition` records the answer the application measured, defaulting to `arriving_insertion` because the question is only ever asked of the one row-less code. `expressible_decisions` therefore reads the field rather than inferring the offer from the code, and the type is part of the published vocabulary (`__all__`), because a consumer that reads a conflict record has to see the same fact the offer was built from.

## Code Commentary

### Logic

Three splits are load-bearing, and each is a place where a weaker model would have permitted a guess:

- **An explicit input versus a resolved one.** `MergeInput` names a dataset *and* the exact logical identity the caller admitted for it (`role`, `database`, `identity`, `reference`). A caller cannot hand over a path and let the operation decide which dataset it meant: the identity is re-read and compared before any byte is copied. `reference` is the caller's own durable anchor (a Git tree, a commit pair, a snapshot reference) and is carried as a fact, never resolved here — this layer does not read Git objects to decide what a dataset is.
- **A base claim versus a base fact.** The claim is a closed union of `SuppliedGitBase` (the caller resolved the base itself and names the exact commit and tree) and `ResolvedGitBase` (the caller claims one commit is the *unique* common base and asks for the evidence). There is no third member — "the operation may pick one" is not expressible, which is what keeps an arbitrary `git merge-base` result out of reach. `MergeBaseResolution` records which of the two applied: `git_base_commit` is the exact admitted commit or `None`, and `uniqueness_checked` distinguishes "the history had one common base" from "the caller said which commit it was" without re-deriving it from the claim.
- **A measurement versus a verdict.** `MergeCoverage` reports which tables the changeset touched, which tables the replay proved covered, and how many operations of each kind were materialised. `MergeOutcome` reports the identities it observed. Neither can express an opinion about the data.

`MergeRequest` restates the datasets' paths beside the resolution's identities rather than carrying them inside it, because they are local operation facts: a dataset *identity* is what the resolution proves, and the file it is read from is an input this request names. It is a dataclass rather than a third model member so the paths cannot be serialized into anything durable. `destination` is optional on purpose: a caller may run the merge and inspect the structural outcome without publishing anything.

`TableCoverage` separates two facts that a return code conflates: `table_changed` is read from the two datasets (whether the side's rows differ from the base's for this table) while `operations` counts the materialised changeset operations. A table that changed but contributed no operation is the silent omission the coverage exists to catch, and `replayed` records whether applying the changeset to a fresh copy of the base reproduced the side's whole logical dataset. `MergeCoverage` covers **every** canonical table, including unchanged ones, because "this table was examined and had nothing to carry" is a different fact from "this table was never attached".

`MergeConflict` carries exactly the facts SQLite supplied, in two shapes that are not interchangeable:

- a **row-level** conflict, where SQLite hands the callback the operation in hand: `attribution` is `engine_attributed` and `table`, `operation` and `record_id` are all present. `record_id` is the exact key of the row the engine refused, copied out of the change the callback received and therefore read from the operation's **old** values — a changeset supplies only the columns an operation changes, and an `UPDATE` leaves its key columns unchanged, so a key read from the new side would be the not-supplied marker rather than a row.
- a **foreign-key** conflict, where SQLite hands the callback **no change at all** and reports only that the application could not be completed: `attribution` is `engine_reported_without_row`, the row fields are absent, and `detail` says so. This is also the only shape whose `precondition` is consulted: `RetractionPrecondition` says whether the retraction the row-less `keep-left` performs is available, and it is a fact about the application rather than about the conflict code, so the caller that ran the delta supplies it and the default `arriving_insertion` stands for every conflict where the question does not arise.

Nothing is fabricated to fill either gap. A row-level conflict whose change carried no readable key columns reports no `record_id` and must say so in `detail` rather than substitute a row identity, and **no violation count is reported for the foreign-key shape**: the pinned binding raises `ConstraintError` with no count in its arguments, so a number there would be the operation's own inference rather than the engine's report.

**The authored vocabulary is keyed to those two shapes rather than to a caller's preference.** `AuthoredDecision` names the two sides the refusal itself prints — `expected` is the left side's stored value, `observed` is the right side's supplied value — so `keep-left` retracts the arriving change and `keep-right` applies it over the stored value, and an agent that read the refusal already knows what each means. `expressible_decisions` answers in three parts: a conflict that named no row admits nothing at all (a schema disagreement above all, whose own next action says the difference is reported rather than reconciled); the row-less referential conflict admits `keep-left` **only when the measured precondition says an arriving insertion can be retracted**, and admits nothing when it says otherwise; and a conflict that named a row admits `keep-left`, plus `keep-right` where `_OVERWRITE_CONFLICT_CODES` has proven the overwrite direction. The order of those two answers is load-bearing rather than stylistic: a row-less conflict has no table and no record id, so asking the row-level question first would answer "no row, admit nothing" for the one code a row-less decision exists for. **`AuthoredReconciliation` has exactly two structural shapes** and no mode flag: `table` and `record_id` together name the exact row, or both are absent and the decision can only answer a conflict the engine reported without a row — in which case only `keep-left` validates, because an overwrite needs a row to overwrite. Half a row identity is refused by name, so a decision always applies to the conflict the caller read and never to a neighbouring one.

### Conventions

- `MergeBaseRequest._require_one_input_per_role` and `MergeRequest._require_every_role` refuse a request whose roles are not exactly one of each, which is why `MergeBaseRequest.input_for(role)` has an answer for every member of the union and needs no failure branch.
- `MergeCoverage._require_every_canonical_table` refuses a coverage record that omits a table, so "not attached" cannot be silently reported as "nothing to carry".
- `MergeConflict._require_consistent_conflict_facts` and `MergeOutcome._require_consistent_merge_outcome` refuse the mixed states at construction, so an inconsistent outcome is caught at the returning call site rather than by a caller's branch.
- `MergeCoverage.changed_tables()` and `table_operations()` are derived readers rather than a second stored field, so a coverage record cannot disagree with itself.
- `AuthoredReconciliation._require_one_decidable_shape` refuses half a row identity and refuses an overwrite on a row-less decision, so the two shapes are structural rather than a flag a caller could set inconsistently.

### Invariants And Boundaries

- **No field can carry a verdict.** The forbidden tokens are absent from `model_dump(mode="json")`, and the validators refuse `structurally_merged` without an identity and coverage, and refuse a conflict on a merged outcome.
- **A refusal still carries what was proven.** `MergeOutcome`'s refused state keeps the coverage measured *before* application, so a caller can see that the inputs were read completely even though nothing was published.
- **`MergeRequest` is not durable.** Its paths are a dataclass field precisely so they cannot be serialized into a stored value.
- **An authored decision is one row, never a policy.** `reconciliations` is optional and is a **tuple**: every entry still names exactly one row, there is no field meaning "prefer my side", a decision that names no row cannot overwrite anything, and every conflict none of them names is still refused exactly as it was. It is plural for a measured reason rather than for generality — a retained merge is answered one conflict at a time, and the attempt that answers the second has to carry the first, because with only the newest decision carried a two-conflict merge alternates between the same two rows forever. Which decisions are expressible at all is answered in one place (`expressible_decisions`) rather than by each caller, and for the one code where the answer is not a property of the code, that place reads a measured field (`MergeConflict.precondition`) instead of guessing from the diagnosis.
- **A row-less decision is never offered on an unmeasured promise.** `RetractionPrecondition` is supplied by the application that ran the delta and carried on the conflict record; nothing in this module re-derives it, and `expressible_decisions` cannot offer a retraction the producing merge has not observed to settle.
- **Boundary.** This module declares vocabulary. It performs no I/O, resolves no Git claim, applies no changeset and publishes nothing. `expressible_decisions` is a pure function over an already-produced `MergeConflict`; it reads no database.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one non-refusal state name, which is the entire claim the operation makes. [1]
- The closed two-member base claim. [2]
- The explicit input that carries the identity a caller admitted and a reference that is never resolved here. [3]
- **The two authored decisions one refused conflict admits, the conflict-code sets that decide which of them is offered, and the measured precondition that decides the one offer the code cannot.** [4]
- **The one authored-decision shape: the exact refused row with its side, or the row-less retraction that is the only decision a conflict without a row admits — and only where the measured precondition says it can apply.** [5]
- The base-resolution request and its exactly-one-input-per-role rule. [6]
- The resolution that records which of the two base claims applied. [7]
- The complete merge request, including the optional destination, the one authored decision it may carry, and why the paths are a dataclass. [8]
- The two coverage records that separate "changed" from "carried an operation" and cover every canonical table. [9]
- The conflict record's two shapes, the old-side key rule, the deliberately absent foreign-key row and count, and the precondition field the row-less offer reads. [10]
- The outcome that carries identities, coverage and publication state and no verdict. [11]
- The two operation names and twelve refusal codes this vocabulary is keyed by. [12]
- The node that confirms the published result carries no forbidden field and reports the coverage record. [13]
- The boundary node that holds the conflict record to the engine's own row identity. [14]
- **The node that drives the authored decision through the real merge and holds the unnamed-conflict refusal.** [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
