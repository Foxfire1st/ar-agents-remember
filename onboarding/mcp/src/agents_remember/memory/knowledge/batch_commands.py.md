# mcp/src/agents_remember/memory/knowledge/batch_commands.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Applying a validated candidate batch, and re-proving what it left behind.** This is the only module in the
batch operation that writes. It runs strictly after every precondition has passed, inside the same transaction
and under the same candidate lock, so a failure raised from here rolls the whole batch back — including the rows
earlier commands in the same batch already inserted.

Three rules shape the apply step, and each one is a disclosure a consumer depends on:

- **Provenance comes from the admission, never from the payload.** Each draft is sealed with the admitted
  `Authorship`, so the fields a caller could author never become the record's provenance.
- **The receipt is derived from what was touched.** Each entry reports the row's own digest as the store
  computes it, and whether the batch wrote it or deleted it. A command that ran no statement contributes **no**
  entry rather than a claimed write.
- **The failure position is observed, not inferred.** When the database refuses mid-batch, the index the loop
  was running travels with the outcome, so the mapped refusal names the command that actually failed instead of
  the last one the caller happened to declare.

## Code Commentary

### Logic

- `apply_commands` walks the commands in declared order with the batch's whole pending identity set in hand.
  Each command's own `KnowledgeRefused` is restated through `batch_refusal` as a refusal of the batch that
  carried it (`_apply_one`), naming the position and kind. An `apsw.Error` leaves the loop immediately as a
  `BatchApplication` carrying `failed_index`, `failed_command` and the error; a completed pass ends with
  `store.require_referential_integrity()`.
- `BatchLedger` is the only mutable state the apply step keeps: `written(...)` adds a `written` receipt entry
  **and** registers the identity as batch-created; `removed(...)` adds a `removed` entry carrying the digest the
  row *had*. Entries are appended in command order, which is exactly the order `MutationResult.changed` promises.
- `BatchApplication` is the frozen outcome: `completed`, and `observed_failure()` returning
  `(error, index, kind)` or `None`. It exists so the caller — not this module — turns a database failure into
  the batch's typed refusal, keeping the SQLite-error mapping in one place.
- Dispatch is one table rather than a ladder: `_APPLY_FAMILIES` holds **seven** family rows — `_INSERTING_KINDS` →
  `_apply_insert` (identity rows, sealed aggregates, anchor, membership, claim), `_LABELING_KINDS` →
  `_apply_label`, the composition kinds, `FACET_COMMAND_KINDS`, `EVIDENCE_COMMAND_KINDS`, `EFFECT_COMMAND_KINDS`
  and `CENSUS_COMMAND_KINDS` — each delegating to its record group's own in-transaction step, with
  `_apply_removal` as the fallback for the removal kinds. `_refuse_unreachable` is the `KnowledgeStorageError`
  for a kind that reached apply without a handler; it is unreachable by construction because the union and the
  dispatch tables are closed over the same thirty-one command kinds, so it is a defect rather than a
  caller-provocable refusal.
- **The census family is the newest of the seven, and it is a delegation like the two before it.**
  `_apply_family_census` takes no `pending` set — it deletes the parameter, exactly as `_apply_family_evidence`
  and `_apply_family_effect` do — and hands its command to `census_records.apply_census_command`, the census
  record group's own in-transaction step. Every relation a census command declares (a claim's evidence, its
  realization attribution, a disposition's links) is therefore resolved against the rows as they stand, in the
  order the author wrote the commands: a disposition that links to a claim the same batch creates resolves once
  that claim's command has run. A kind outside the three census commands is a `KnowledgeStorageError` marked
  unreachable, because `CENSUS_COMMAND_KINDS` and the isinstance tuple are closed over the same three kinds.
- **Every write goes through a shared in-transaction primitive, never through a nested operation.** The apply
  steps call `store.insert_invariant_identity`, `store.insert_revision_aggregate`, `families.insert_family`/
  `insert_family_revision`, `anchors.insert_anchor_row`, `memberships.insert_family_member_draft`,
  `realizations.insert_realization_claim`, `labels.apply_*_label` and the three `delete_*` helpers — the same
  helpers the single-record operations now use, so the batch cannot drift from the operation it composes. None
  of them opens a transaction or takes a lock: the batch already owns both.
- **Receipt shapes worth reading twice.** An identity insert reports the row digest the store now holds; a
  sealed revision reports its `payload_digest`; a claim that also records a new anchor reports **two** written
  entries (the claim, then its anchor); a removal reports the digest the row had (the anchor's is read before
  the delete, the membership's and the claim's are the expectation the delete verified); a label edit that
  changed nothing returns `()` because no statement ran.
- `require_after_integrity` is the re-proof pass and is deliberately **not** a re-run of the preconditions: it
  checks the rows as they now stand — `store.require_referential_integrity()` for the deferred foreign keys,
  `_require_sealed_rows` for every stored revision's seal (decoding re-derives it), and `_require_acyclic_graph`
  over both lineage graphs as a whole-graph question rather than a per-candidate one.

**A fifth dispatch family, and a shipped defect this leaf's addition exposed.** `_apply_evidence` is the fifth family beside insertion, label edit, removal and the authored facet commands: it delegates to the supporting-record module's own in-transaction step, which resolves every link the command declares — subject, evidence anchor and every claimed-coverage endpoint — against the stored rows and refuses before it writes anything. That is why the batch's completed-graph pass asks only that the *command* be declared while the step asks whether the referenced rows exist. **The after-integrity pass was decoding every `record_revision` as a facet revision.** `_facet_revisions` drove the *facet* revision decoder over the whole shared `knowledge_record` table, which was correct only by accident of who else wrote envelope rows at the time: at that point only facets wrote `record_revision` through a batch. `knowledge_record` is shared — the facet, supporting-record, authored-effect and census groups all write envelope rows through a batch — so the pass is scoped to `FACET_KINDS` — the question 'which revisions does this pass own' is a question about the kind the envelope carries, not about the table.

### Conventions

- The dispatch sets and the per-family dispatch chains are module constants/dispatchers, so adding a command
  kind is one entry in the union, one in the dispatch, and one apply step. A record group whose commands all
  resolve through its own module — the census's three do — joins through one further shape: the vocabulary
  declares `CENSUS_COMMAND_KINDS` beside its commands and payload models, the dispatch table gains one row, and
  the step is a delegation (`census_records.apply_census_command`) rather than a body written here.
- A `# pragma: no cover - …` comment marks the branches that are unreachable because two closed sets agree;
  each explains which invariant makes it unreachable.
- A refusal built with a hardcoded `"0:<kind>"` position (`_anchor_digest`, `_remove_anchor`) is a damaged-store
  path, not a caller-provable one — the precondition already refused the reachable case.
- `_sealed_revision` and `_sealed_family_revision` re-stamp the draft's provenance with the admitted envelope
  before sealing, which is the mechanism behind the provenance rule above.

### Invariants And Boundaries

- **The only writer.** No other module in the batch operation performs DML. `batch_preconditions.py` reads and
  refuses; this module writes and can only be reached after those checks passed.
- **One transaction, no nesting.** Every helper called here assumes the caller holds the lock and the
  transaction; nesting a second `BEGIN IMMEDIATE` would be a SQLite error and re-taking the lock would break the
  one-lock rule.
- **The receipt reports the rows the store now holds.** A digest in a receipt is one the store computed (or, for
  a removal, the one the row had); nothing here is a caller-supplied value.
- **The integrity pass is defence in depth, not the sole enforcement.** The preconditions make a violation
  unreachable and the schema's foreign keys are `DEFERRABLE INITIALLY DEFERRED`, so SQLite itself refuses at
  `COMMIT`; this pass is what turns that into a refusal by the state the batch produced. Do not read its
  survival under mutation as a defect.
- **Boundary.** This module decides which statements run and what the receipt says. It does not decide what must
  hold (preconditions), the lane or the transaction boundary (`candidate.py`), or the wording of a refusal
  (`refusals.py`).

### Todos

None recorded for this slice. The disclosed cost is unchanged: the batch computes the logical body three times
(context re-derivation, before, after), which a later leaf may cache only after demonstrating equivalent
conformance.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The apply loop, the observed failure position and the deferred-foreign-key check at the end of a completed pass. [1]
- The outcome object that carries what the loop observed. [2]
- The ledger that produces the receipt and registers batch-created identities. [3]
- **The dispatch table an apply step chooses between, keyed on the vocabulary's own kind sets — now seven family rows, the census group's `CENSUS_COMMAND_KINDS` row being this leaf's addition and the last.** [4]
- The inserting command kinds the dispatch admits. [5]
- The labelling command kinds the dispatch admits, which is a different set from the inserting ones. [6]
- The unreachable-kind defect: a command that reaches the dispatch and belongs to no family is refused rather than silently skipped. [7]
- The two receipt entries a claim that records its own anchor produces. [8]
- The removal steps, each reporting the digest the row had when it was deleted. [9]
- The outcome object that carries what the loop observed. [10]
- The ledger that produces the receipt and registers batch-created identities. [11]
- **The seven-family dispatch and the unreachable-kind defect.** [12]
- The two receipt entries a claim that records its own anchor produces. [13]
- The removal steps, each reporting the digest the row had when it was deleted. [14]
- The no-op label edit that contributes no receipt entry. [15]
- The after-integrity re-proof the apply step runs last: foreign keys, every revision seal, both lineage graphs — and, since this leaf, the authored-effect seals and the change-set succession graph. [16]
- The seal half of the re-proof. [17]
- **The graph half of the re-proof, and the composition pass this leaf added to it.** [18]
- **The census record group's dispatch family — the seventh row of the dispatch table, handed no `pending` set and delegating to the group's own in-transaction step.** [19]
- **The in-transaction step the census family delegates to: it re-checks the dataset's generation, resolves the governing route, then applies the inventory row, the claim or the disposition and their relations in command order.** [20]
- **The closed three-command vocabulary the census dispatch row and the isinstance guard are both built from.** [21]
- The store's two batch-facing primitives, which the apply step calls instead of a nested operation. [22]
- The invariant identity and revision insert bodies the same call reaches. [23]
- The family half's in-transaction inserts, which the batch composes rather than re-implementing. [24]
- The anchor insert and delete the batch shares with the anchor operation. [25]
- The membership draft-sealing insert, which is where the batch's member row digest is computed. [26]
- The realization claim insert whose `None` answer means the identical claim was already stored. [27]
- The label edit whose `False` answer means no statement ran, which is why the apply step returns no receipt entry. [28]
- The caller that turns an observed failure into the batch's typed refusal. [29]
- The nodes that prove a late failure rolls the whole batch back, and that a removal-only batch returns a typed result. [30]
- The node that proves the database's own refusal names the command that actually failed. [31]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The apply step writes rows in one SQLite file; it
writes no Git object, no ledger row and no second repository.

No meaningful cross-repo references found.
