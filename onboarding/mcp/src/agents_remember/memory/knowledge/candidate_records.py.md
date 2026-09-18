# mcp/src/agents_remember/memory/knowledge/candidate_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:05:00+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The row-identity vocabulary one candidate batch reads and reports.** Two questions run through the whole batch
operation — "what is stored under this identity?" and "which identities does this command address?" — and they
are answered here once, so the precondition module reads as rules over typed values rather than as a mix of
checks and SQL-shaped lookups.

Every digest this module returns is the value the read operations already expose: `row_digest` for an authored
row and `payload_digest` for a sealed revision aggregate. A caller therefore carries an expectation straight from
a read instead of deriving a second identity scheme that could disagree with the one it read.

## Code Commentary

### Logic

- `stored_record_digest(store, table, record_id)` is the single stored-state question, dispatched through
  `_RECORD_READERS` to the owning concept's own read (`store.get_invariant`,
  `families.get_family`/`get_family_revision`, `anchors.get_anchor`, `memberships.get_family_member`,
  `realizations.get_realization_claim`, `store.get_revision`) and returned as that read's digest. An anchor is
  the one case where the digest is derived rather than stored (`records.anchor_row_digest`), because the anchor
  row's digest is computed over its payload. A table outside `WRITABLE_TABLES` is a `ValueError`: it is a caller
  mistake, not a record the operation can address.
- `written_identities(command)` answers "which identities does this command address", one per command kind for
  eleven kinds through `_WRITTEN_IDENTITY`; the twelfth — `add_realization_claim` — addresses **two** when its
  anchor endpoint records a new anchor, and is handled in the function itself.
- `inserted_identities(command)` is the narrower question "which identities does this command **create**": the
  five kinds in `_ADDRESSES_EXISTING` (`set_invariant_label`, `set_family_label`, `remove_source_anchor`,
  `remove_family_member`, `remove_realization_claim`) address a row that must already exist and create nothing,
  so they return `()`. That distinction is what lets a batch state a label edit and a removal for the same row
  without tripping the duplicate-identity rule.
- `pending_identities(commands)` is the batch's own declared set, and `present(store, pending, table,
  record_id)` is the one existence question that admits it — which is how a command may cite a record another
  command in the same batch creates, in either direction. The set is built over the **whole** command
  sequence, not a running prefix, because validation is over the completed graph rather than the request order.

**The writable-table union is now spelled per record group, and the envelope digests are kind-agnostic.** `SHIPPED_WRITABLE_TABLES` holds the seven shipped names, `ENVELOPE_WRITABLE_TABLES` holds the two envelope tables every record group writes, and `FACET_WRITABLE_TABLES` and `EVIDENCE_WRITABLE_TABLES` are imported from the vocabularies that own those commands; `WRITABLE_TABLES` is their union, so a group that writes the envelope is not thereby claiming the table for itself and a command cannot write a table the list does not name. `_envelope_record_digest` is the kind-agnostic reader the batch's before/after comparison needs: `knowledge_record` is the one table four record groups write, so its digest is computed from the row's own stored fields regardless of which group wrote it, and the two new identity readers expose an evidence claim's and an observation's identities to the dispatch. Every evidence command's written identities are exactly the tables it writes, which is what the union case asserts.

### Conventions

- The readers are module-level private functions gathered into one dispatch dict, so a new writable table is
  added by naming its reader rather than by extending a chain of conditionals.
- `WRITABLE_TABLES` is the declared set the vocabulary agrees with `MutableRecordTable` on: the thirteen tables a
  command can write directly. The `repository` row and the two predecessor-edge tables are written only as part
  of the aggregate that owns them.
- Type aliases (`IdentityPairs`, `RecordReader`) keep the signatures readable; the module writes nothing and
  takes no lock.

### Invariants And Boundaries

- **One identity scheme.** A digest here is the value a read exposes; nothing re-derives a competing digest, so
  an expectation carried from a read cannot disagree with the check that consumes it.
- **Read-only.** This module performs no DML at all. It is safe to call from inside the batch's transaction and
  from the preconditions, which is why it can be the shared vocabulary of both.
- **`written_identities` is about addressing, not about writing.** A removal addresses a record it removes; the
  name is about which record the command is *about*, and `inserted_identities` is the narrower predicate.
- **Boundary.** This module owns identity addressing and stored-state reads. Whether a mismatch is a refusal,
  and which refusal code it produces, belongs to `batch_preconditions.py` and `refusals.py`.

### Todos

None recorded for this slice. The dispatch dicts are closed over the eighteen command kinds; a nineteenth kind is
a vocabulary decision in `models/knowledge/candidate.py`, and these tables would be extended with it in the same
change.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The writable-table union the refusal reads — the shipped seven, the two envelope tables, and each record group's own set subtracted to its non-envelope remainder, which is where this leaf's authored-effect group contributes nothing. | `WRITABLE_TABLES`; `EFFECT_ONLY_WRITABLE_TABLES` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:104-111; mcp/src/agents_remember/memory/knowledge/candidate_records.py:92-94 |
| The per-table readers, each delegating to the owning concept's own read. | "_RECORD_READERS: dict[str, RecordReader] = {"; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:103-130; mcp/src/agents_remember/memory/knowledge/candidate_records.py:206-206; mcp/src/agents_remember/memory/knowledge/candidate_records.py:253-258; mcp/src/agents_remember/memory/knowledge/candidate_records.py:146-148; mcp/src/agents_remember/memory/knowledge/candidate_records.py:262-269 |
| The one-identity-per-kind map, with the two-identity claim command handled separately. | "_WRITTEN_IDENTITY: dict[str, Callable[[Any], tuple[str, str]]] = {"; "def written_identities(command: ChangeCommand) -> IdentityPairs:" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:231-231; mcp/src/agents_remember/memory/knowledge/candidate_records.py:286-356; mcp/src/agents_remember/memory/knowledge/candidate_records.py:286-286; mcp/src/agents_remember/memory/knowledge/candidate_records.py:365-372 |
| The commands that address an existing row and therefore create nothing. | "_ADDRESSES_EXISTING: tuple[str, ...] = ("; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:278-278; mcp/src/agents_remember/memory/knowledge/candidate_records.py:324-425; mcp/src/agents_remember/memory/knowledge/candidate_records.py:468-473 |
| The batch's declared identity set. | `pending_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:476-482 |
| **The existence question that admits the declared set: a record counts as present if it is already stored or will be by the time this batch is applied.** | `present` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:485-492 |
| The writable-table union the refusal reads, and the digest reader it uses for a stored row. | `WRITABLE_TABLES`; `stored_record_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:104-111; mcp/src/agents_remember/memory/knowledge/candidate_records.py:117-123 |
| The per-table readers, each delegating to the owning concept's own read. | "_RECORD_READERS: dict[str, RecordReader] = {"; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:106-151; mcp/src/agents_remember/memory/knowledge/candidate_records.py:88-90; mcp/src/agents_remember/memory/knowledge/candidate_records.py:253-258; mcp/src/agents_remember/memory/knowledge/candidate_records.py:262-269 |
| The one-identity-per-kind map, with the two-identity claim command handled separately. | "_WRITTEN_IDENTITY: dict[str, Callable[[Any], tuple[str, str]]] = {"; "def written_identities(command: ChangeCommand) -> IdentityPairs:" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:125-151; mcp/src/agents_remember/memory/knowledge/candidate_records.py:166-356; mcp/src/agents_remember/memory/knowledge/candidate_records.py:286-286; mcp/src/agents_remember/memory/knowledge/candidate_records.py:365-372 |
| The commands that address an existing row and therefore create nothing. | "_ADDRESSES_EXISTING: tuple[str, ...] = ("; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:155-163; mcp/src/agents_remember/memory/knowledge/candidate_records.py:190-425; mcp/src/agents_remember/memory/knowledge/candidate_records.py:468-473 |
| The batch's declared identity set and the existence question that admits it. | `pending_identities`; `present` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:198-204; mcp/src/agents_remember/memory/knowledge/candidate_records.py:207-442; mcp/src/agents_remember/memory/knowledge/candidate_records.py:476-486 |
| The preconditions that consume these answers. | `require_expected_records`; `require_insertions_absent`; `require_command_targets` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:129-240 |
| The vocabulary the writable table set mirrors. | "MutableRecordTable = Literal[" | mcp/src/agents_remember/models/knowledge/candidate.py:140-140 |
| The anchor row digest the anchor reader derives rather than stores. | `anchor_row_digest` | mcp/src/agents_remember/memory/knowledge/records.py:366-381 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T08:36:42+00:00: Generated citation repair: `pending_identities` repointed to mcp/src/agents_remember/memory/knowledge/candidate_records.py:476-482. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `present` repointed to mcp/src/agents_remember/memory/knowledge/candidate_records.py:485-492. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "MutableRecordTable = Literal[" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:140-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand while resolving the memory sync** — `_ADDRESSES_EXISTING`, `inserted_identities`, `MutableRecordTable`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read this card's claims against the source and re-cited the rows the leaf's additions moved.** The writable-table tuple is now `WRITABLE_TABLES` — the base seven plus this leaf's six composition tables — with six new digest readers, and the identity set the batch declares is `inserted_identities`, `pending_identities` and `present` (the last of which ends one line earlier than a projected range claimed). The `pending_identities`/`present` row was split so each anchor has its own extent, and the generated repair bullet that had kept `claim_reopen` enforced on it was removed and replaced by this entry. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `_ADDRESSES_EXISTING`, `inserted_identities`, `pending_identities`, `present`, `MutableRecordTable`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the writable-table union spelled per record group and the kind-agnostic envelope digest reader that `knowledge_record`'s four writers require. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T02:55:00+00:00 — 260915-KS-L11 owning seat (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this claim against the source and re-cited it by hand, replacing a generated projection.** The claim said *seven* directly writable tables; `WRITABLE_TABLES` now declares **thirteen** (`candidate_records.py:39-53`, counted from the declaration itself, and equal to `MutableRecordTable`'s thirteen members in `models/knowledge/candidate.py`). The wording and the range were both rewritten by an agent that read the declaration, so the citation is no longer a mechanical anchor-range projection: the range is the declaration the claim's own words describe.

- 2026-09-18T02:55:00+00:00 — 260915-KS-L11 owning seat (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this claim against the source and re-cited it by hand, replacing a generated projection.** The claim said *seven* directly writable tables; `WRITABLE_TABLES` now declares **thirteen** (`candidate_records.py:39-53`, counted from the declaration itself, and equal to `MutableRecordTable`'s thirteen members in `models/knowledge/candidate.py`). The wording and the range were both rewritten by an agent that read the declaration, so the citation is no longer a mechanical anchor-range projection: the range is the declaration the claim's own words describe.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this card against the source for the round-2 citation work and recorded a contradiction instead of softening the row.** The row above reading "The thirteen directly writable tables and the refusal of a table outside them" is **no longer true**: `WRITABLE_TABLES` (`mcp/src/agents_remember/memory/knowledge/candidate_records.py:39-53`) now holds **thirteen** names — the seven it held at `76c7697c` plus `knowledge_record`, `record_revision`, `facet_attachment`, `facet_decision_supersession`, `explanation` and `explanation_revision`, which this leaf's facet write path added. The row's citation was re-pointed to that tuple and its anchor left naming the tuple; its *count* was not rewritten, because a claim's meaning belongs to the owning seat rather than to the citation curator. The one-word correction owed is `seven` → `thirteen`. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp. No content impact: this entry records a review, not a content change.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this card against the source for the round-2 citation work and recorded a contradiction instead of softening the row.** The row above reading "The thirteen directly writable tables and the refusal of a table outside them" is **no longer true**: `WRITABLE_TABLES` (`mcp/src/agents_remember/memory/knowledge/candidate_records.py:39-53`) now holds **thirteen** names — the seven it held at `76c7697c` plus `knowledge_record`, `record_revision`, `facet_attachment`, `facet_decision_supersession`, `explanation` and `explanation_revision`, which this leaf's facet write path added. The row's citation was re-pointed to that tuple and its anchor left naming the tuple; its *count* was not rewritten, because a claim's meaning belongs to the owning seat rather than to the citation curator. The one-word correction owed is `seven` → `thirteen`. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp. No content impact: this entry records a review, not a content change.

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new batch identity vocabulary. It records the one-identity-scheme rule (a digest here is exactly what a read exposes), the read-only boundary that lets the preconditions and the apply step share it, the addressing-versus-creating distinction that lets one row be edited and removed in one batch, and the whole-sequence pending set that makes a forward reference legal. Verification metadata remains empty until closeout stamps the code commit.
