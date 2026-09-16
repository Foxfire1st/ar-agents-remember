# mcp/src/agents_remember/memory/knowledge/batch_commands.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/batch_commands.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

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
- Dispatch is three families rather than one twelve-way ladder: `_INSERTING_KINDS` → `_apply_insert` (identity
  rows, sealed aggregates, anchor, membership, claim), `_LABELING_KINDS` → `_apply_label`, everything else →
  `_apply_removal`. `_refuse_unreachable` is the `KnowledgeStorageError` for a kind that reached apply without a
  handler; it is unreachable by construction because the union and the dispatch tables are closed over the same
  twelve kinds, so it is a defect rather than a caller-provokable refusal.
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

### Conventions

- The three dispatch sets and the per-family dispatch chains are module constants/dispatchers, so adding a
  command kind is one entry in the union, one in the dispatch, and one apply step.
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The apply loop, the observed failure position and the deferred-foreign-key check at the end of a completed pass. | `apply_commands` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:147-172 |
| The outcome object that carries what the loop observed. | `BatchApplication`; `observed_failure` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:118-144 |
| The ledger that produces the receipt and registers batch-created identities. | `BatchLedger`; `written`; `removed` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:85-115 |
| The three-family dispatch and the unreachable-kind defect. | `_apply_command`; `_INSERTING_KINDS`; `_LABELING_KINDS`; `_refuse_unreachable` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:192-223; mcp/src/agents_remember/memory/knowledge/batch_commands.py:295-304 |
| The two receipt entries a claim that records its own anchor produces. | `_add_claim`; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:435-471 |
| The removal steps, each reporting the digest the row had when it was deleted. | `_remove_anchor`; `_remove_member`; `_remove_claim` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:513-548 |
| The no-op label edit that contributes no receipt entry. | `_apply_label`; `_set_invariant_label`; `_set_family_label` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:267-278; mcp/src/agents_remember/memory/knowledge/batch_commands.py:474-510 |
| The after-integrity re-proof: foreign keys, every revision seal, both lineage graphs. | `require_after_integrity`; `_require_sealed_rows`; `_require_acyclic_graph` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:554-570; mcp/src/agents_remember/memory/knowledge/batch_commands.py:573-584; mcp/src/agents_remember/memory/knowledge/batch_commands.py:604-617 |
| The store's two batch-facing primitives, which the apply step calls instead of a nested operation. | `insert_invariant_identity`; `insert_revision_aggregate` | mcp/src/agents_remember/memory/knowledge/store.py:272-301 |
| The invariant identity and revision insert bodies the same call reaches. | `insert_invariant`; `insert_revision` | mcp/src/agents_remember/memory/knowledge/store.py:512-549; mcp/src/agents_remember/memory/knowledge/store.py:551-608 |
| The family half's in-transaction inserts, which the batch composes rather than re-implementing. | `insert_family`; `insert_family_revision` | mcp/src/agents_remember/memory/knowledge/families.py:110-131; mcp/src/agents_remember/memory/knowledge/families.py:173-208 |
| The anchor insert and delete the batch shares with the anchor operation. | `insert_anchor_row`; `delete_anchor` | mcp/src/agents_remember/memory/knowledge/anchors.py:99-119; mcp/src/agents_remember/memory/knowledge/anchors.py:184-207 |
| The membership draft-sealing insert, which is where the batch's member row digest is computed. | `insert_family_member_draft` | mcp/src/agents_remember/memory/knowledge/memberships.py:61-86 |
| The realization claim insert whose `None` answer means the identical claim was already stored. | `insert_realization_claim` | mcp/src/agents_remember/memory/knowledge/realizations.py:93-141 |
| The label edit whose `False` answer means no statement ran, which is why the apply step returns no receipt entry. | `apply_invariant_label` | mcp/src/agents_remember/memory/knowledge/labels.py:62-99 |
| The caller that turns an observed failure into the batch's typed refusal. | `_apply_within_transaction`; `_mapped_failure` | mcp/src/agents_remember/memory/knowledge/candidate.py:128-145; mcp/src/agents_remember/memory/knowledge/candidate.py:251-267 |
| The nodes that prove a late failure rolls the whole batch back, and that a removal-only batch returns a typed result. | "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch"; "test_a_removal_only_batch_of_each_kind_returns_a_typed_result" | mcp/tests/test_candidate_batch_transaction.py:62-110; mcp/tests/test_candidate_batch_transaction.py:933-962 |
| The node that proves the database's own refusal names the command that actually failed. | "test_a_database_refusal_mid_batch_names_the_command_that_actually_failed" | mcp/tests/test_candidate_batch_transaction.py:993-1061 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The apply step writes rows in one SQLite file; it
writes no Git object, no ledger row and no second repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the batch apply and integrity module. It records the three shaping rules (admitted provenance, a receipt derived from what was touched, an observed failure position), the three-family dispatch, the shared in-transaction primitives that keep the batch from drifting from the single-record operations, the receipt shapes a consumer must read exactly (two entries for a claim that records its anchor, the digest a removal carries, no entry for a no-op edit) and the after-integrity re-proof as defence in depth rather than the sole enforcement. Verification metadata remains empty until closeout stamps the code commit.
