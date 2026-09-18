# mcp/src/agents_remember/memory/knowledge/batch_commands.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/batch_commands.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The apply loop, the observed failure position and the deferred-foreign-key check at the end of a completed pass. | `apply_commands` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:193-218 |
| The outcome object that carries what the loop observed. | `BatchApplication`; `observed_failure` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:164-190; mcp/src/agents_remember/memory/knowledge/batch_commands.py:185-190 |
| The ledger that produces the receipt and registers batch-created identities. | `BatchLedger`; "def written("; `removed` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:131-161 |
| **The dispatch table an apply step chooses between, keyed on the vocabulary's own kind sets — now seven family rows, the census group's `CENSUS_COMMAND_KINDS` row being this leaf's addition and the last.** | `_APPLY_FAMILIES` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:574-582 |
| The inserting command kinds the dispatch admits. | `_INSERTING_KINDS` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:406-416 |
| The labelling command kinds the dispatch admits, which is a different set from the inserting ones. | `_LABELING_KINDS` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:418-418 |
| The unreachable-kind defect: a command that reaches the dispatch and belongs to no family is refused rather than silently skipped. | `_refuse_unreachable` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:654-663 |
| The two receipt entries a claim that records its own anchor produces. | `_add_claim`; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:794-816; mcp/src/agents_remember/memory/knowledge/batch_commands.py:819-830 |
| The removal steps, each reporting the digest the row had when it was deleted. | `_remove_anchor`; `_remove_member`; `_remove_claim` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:872-887; mcp/src/agents_remember/memory/knowledge/batch_commands.py:890-896; mcp/src/agents_remember/memory/knowledge/batch_commands.py:899-907 |
| The outcome object that carries what the loop observed. | `BatchApplication`; `observed_failure` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:164-190; mcp/src/agents_remember/memory/knowledge/batch_commands.py:185-190 |
| The ledger that produces the receipt and registers batch-created identities. | `BatchLedger`; "def written("; `removed` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:131-161 |
| **The seven-family dispatch and the unreachable-kind defect.** | `_apply_command`; `_INSERTING_KINDS`; `_LABELING_KINDS`; `_refuse_unreachable` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:314-325; mcp/src/agents_remember/memory/knowledge/batch_commands.py:406-416; mcp/src/agents_remember/memory/knowledge/batch_commands.py:418-418; mcp/src/agents_remember/memory/knowledge/batch_commands.py:654-663 |
| The two receipt entries a claim that records its own anchor produces. | `_add_claim`; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:794-816; mcp/src/agents_remember/memory/knowledge/batch_commands.py:819-830 |
| The removal steps, each reporting the digest the row had when it was deleted. | `_remove_anchor`; `_remove_member`; `_remove_claim` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:872-887; mcp/src/agents_remember/memory/knowledge/batch_commands.py:890-896; mcp/src/agents_remember/memory/knowledge/batch_commands.py:899-907 |
| The no-op label edit that contributes no receipt entry. | `_apply_label`; `_set_invariant_label`; `_set_family_label` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:626-637; mcp/src/agents_remember/memory/knowledge/batch_commands.py:833-851; mcp/src/agents_remember/memory/knowledge/batch_commands.py:854-869 |
| The after-integrity re-proof the apply step runs last: foreign keys, every revision seal, both lineage graphs — and, since this leaf, the authored-effect seals and the change-set succession graph. | `require_after_integrity` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:913-934 |
| The seal half of the re-proof. | `_require_sealed_rows` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:937-948 |
| **The graph half of the re-proof, and the composition pass this leaf added to it.** | `_require_acyclic_graph` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:1132-1145 |
| **The census record group's dispatch family — the seventh row of the dispatch table, handed no `pending` set and delegating to the group's own in-transaction step.** | `_apply_family_census` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:328-349 |
| **The in-transaction step the census family delegates to: it re-checks the dataset's generation, resolves the governing route, then applies the inventory row, the claim or the disposition and their relations in command order.** | `apply_census_command` | mcp/src/agents_remember/memory/knowledge/census_records.py:401-419 |
| **The closed three-command vocabulary the census dispatch row and the isinstance guard are both built from.** | `CENSUS_COMMAND_KINDS` | mcp/src/agents_remember/models/knowledge/census.py:352-354 |
| The store's two batch-facing primitives, which the apply step calls instead of a nested operation. | `insert_invariant_identity`; `insert_revision_aggregate` | mcp/src/agents_remember/memory/knowledge/store.py:296-325 |
| The invariant identity and revision insert bodies the same call reaches. | `insert_invariant`; `insert_revision` | mcp/src/agents_remember/memory/knowledge/store.py:536-572; mcp/src/agents_remember/memory/knowledge/store.py:575-632 |
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
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): **re-read every citation this card carries against the staged working candidate and recorded the census record group's dispatch family.** The leaf appended `(frozenset(CENSUS_COMMAND_KINDS), _apply_family_census)` to `_APPLY_FAMILIES`, so the dispatch table now holds **seven** family rows rather than the six this card stated; the dispatch bullet and the two `_APPLY_FAMILIES` rows were re-worded to that count, and a new Logic bullet records what `_apply_family_census` does — it deletes its `pending` parameter exactly as the evidence and authored-effect steps do, and delegates to `census_records.apply_census_command`, so a census relation is resolved against the rows as they stand in the order the author wrote the commands and a disposition may link to a claim the same batch creates. The "three families rather than one twelve-way ladder" sentence was **replaced by the table it describes**, including the closure count: the union and the dispatch tables are closed over the same thirty-one command kinds, not twelve. Fifteen rows whose cited ranges this leaf's insertions (two import blocks, one 22-line apply step, one dispatch row) had moved were **re-cited by hand to each construct's own declaration extent** — `apply_commands`, `BatchApplication`/`observed_failure`, `BatchLedger`, `_INSERTING_KINDS`, `_LABELING_KINDS`, `_refuse_unreachable`, `_apply_command`, `_add_claim`/`_anchor_digest`, the three removal steps, the three label steps, `require_after_integrity`, `_require_sealed_rows` and `_require_acyclic_graph` — and three rows were added for the census family, the step it delegates to and the vocabulary that closes it. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `BatchLedger`; `removed`; "def written(" repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:124-154; mcp/src/agents_remember/memory/knowledge/batch_commands.py:142-145; mcp/src/agents_remember/memory/knowledge/batch_commands.py:136-136. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_APPLY_FAMILIES` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:543-550. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_LABELING_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:387-387. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `BatchApplication`; `observed_failure` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:157-183; mcp/src/agents_remember/memory/knowledge/batch_commands.py:178-183. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `require_after_integrity` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:881-902. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_require_sealed_rows` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:905-916. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_require_acyclic_graph` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:1100-1113. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `apply_commands` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:177-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_INSERTING_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:365-375. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_LABELING_KINDS` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:377-377. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_refuse_unreachable` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:600-609. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `BatchApplication`; `observed_failure` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:148-174; mcp/src/agents_remember/memory/knowledge/batch_commands.py:169-174. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `BatchLedger`; `removed`; "def written(" repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:115-145; mcp/src/agents_remember/memory/knowledge/batch_commands.py:133-136; mcp/src/agents_remember/memory/knowledge/batch_commands.py:127-127. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_apply_label`; `_set_invariant_label`; `_set_family_label` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:572-583; mcp/src/agents_remember/memory/knowledge/batch_commands.py:779-797; mcp/src/agents_remember/memory/knowledge/batch_commands.py:800-815. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_require_sealed_rows` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:883-894. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_require_acyclic_graph` repointed to mcp/src/agents_remember/memory/knowledge/batch_commands.py:1078-1091. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand while resolving the memory sync** — `_add_claim`, `_anchor_digest`, `_remove_anchor`, `_remove_member`, `_remove_claim`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the four claims this leaf's additions moved and re-cited each by hand.** The four composition apply steps joined the dispatch, and the shared endpoint check now names the offending identity in its refusal's `record_id` and the endpoint kind in its `table`; the after-integrity re-proof gained the whole-graph composition cycle pass beside its existing seal and lineage halves. Four rows whose anchors the leaf's insertions had moved — the outcome object, the claim-and-digest pair, the three removal steps, and the three parts of the re-proof — were each split so every anchor sits in a range that actually holds it. No claim was softened or deleted to clear a row. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand** — `_add_claim`, `_anchor_digest`, `_remove_anchor`, `_remove_member`, `_remove_claim`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; their claims' ranges were **re-verified by hand against the current source in this pass** and repaired where this leaf's addition moved them, so a mechanically projected range is no longer the only evidence any of these claims carries. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the fifth dispatch family and **the shipped defect this leaf's addition exposed** — the after-integrity pass decoded every `record_revision` as a facet revision, which was correct only by accident of who else wrote envelope rows, and is now scoped to `FACET_KINDS`. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the batch apply and integrity module. It records the three shaping rules (admitted provenance, a receipt derived from what was touched, an observed failure position), the three-family dispatch, the shared in-transaction primitives that keep the batch from drifting from the single-record operations, the receipt shapes a consumer must read exactly (two entries for a claim that records its anchor, the digest a removal carries, no entry for a no-op edit) and the after-integrity re-proof as defence in depth rather than the sole enforcement. Verification metadata remains empty until closeout stamps the code commit.
