# mcp/src/agents_remember/memory/knowledge/candidate_records.py

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
- `written_identities(command)` answers "which identities does this command address" by trying three shapes in
  turn: `_supporting_record_identities` for the two supporting-record commands, whose identities depend on the
  subject's kind and on the number of claimed coverage endpoints; `_authored_record_identities` for the
  multi-row authored commands (`add_realization_claim`'s optional new anchor, `add_facet`'s optional superseded
  revision, `author_explanation`, the four authored-effect commands and
  `author_family_explanation_context`); and `_WRITTEN_IDENTITY` for the **twenty-five** one-identity commands,
  which is the table that stays a table of one-identity commands. The three census commands are in that last
  shape: `add_census_inventory_row`, `add_census_claim` and `add_census_disposition` each name one record table
  and one `record_id`.
- `inserted_identities(command)` is the narrower question "which identities does this command **create**": the
  eight kinds in `_ADDRESSES_EXISTING` (`set_invariant_label`, `set_family_label`, `remove_source_anchor`,
  `remove_family_member`, `remove_realization_claim`, `remove_facet_attachment`, `designate_explanation` and
  `set_family_revision_route`) address a row that must already exist and create nothing, so they return `()`.
  That distinction is what lets a batch state a label edit and a removal for the same row without tripping the
  duplicate-identity rule.
- **The census group's three relation tables are deliberately unreachable by identity.** `census_claim_evidence`,
  `census_claim_realization` and `census_disposition_link` are each written only as part of the aggregate that
  owns them, so no command addresses one and no expectation could name a state a command could produce — the
  same disposition the authored-effect group's succession edge takes. They are therefore absent from both
  `_RECORD_READERS` and `_WRITTEN_IDENTITY` while still appearing in `CENSUS_ONLY_WRITABLE_TABLES`, because the
  batch does write them; what is absent is a way to *address* one.
- `pending_identities(commands)` is the batch's own declared set, and `present(store, pending, table,
  record_id)` is the one existence question that admits it — which is how a command may cite a record another
  command in the same batch creates, in either direction. The set is built over the **whole** command
  sequence, not a running prefix, because validation is over the completed graph rather than the request order.

**The writable-table union is now spelled per record group, and the envelope digests are kind-agnostic.** `SHIPPED_WRITABLE_TABLES` holds the seven shipped names, `ENVELOPE_WRITABLE_TABLES` holds the two envelope tables every record group writes, and `FACET_WRITABLE_TABLES`, `EVIDENCE_WRITABLE_TABLES`, `COMPOSITION_WRITABLE_TABLES`, `EFFECT_WRITABLE_TABLES` and `CENSUS_WRITABLE_TABLES` are imported from the vocabularies that own those commands; `WRITABLE_TABLES` is their union — **thirty** tables, equal to `MutableRecordTable`'s thirty members — so a group that writes the envelope is not thereby claiming the table for itself and a command cannot write a table the list does not name. Each group contributes its own named constant rather than an edit inside another leaf's list: the authored-effect group's remainder is empty (it writes the envelope and nothing of its own) and the census group's is `CENSUS_ONLY_WRITABLE_TABLES`, its three record tables and three relation tables minus the same two envelope names. `_envelope_record_digest` is the kind-agnostic reader the batch's before/after comparison needs: `knowledge_record` is the one table more than one record group writes, so its digest is computed from the row's own stored fields regardless of which group wrote it, and the identity readers expose an evidence claim's, an observation's and each census record's identities to the dispatch. Each group's declared table set is the set its own commands write — the census's six are declared beside its three commands and its three relations — which is what the union case asserts.

### Conventions

- The readers are module-level private functions gathered into one dispatch dict, so a new writable table is
  added by naming its reader rather than by extending a chain of conditionals. The census group's three record
  tables name `census_records.inventory_row_digest`, `census_records.claim_digest` and
  `census_records.disposition_digest`, so a census expectation is answered by the census module's own read.
- `WRITABLE_TABLES` is the declared set the vocabulary agrees with `MutableRecordTable` on: the **thirty** tables
  a command can write directly, each group contributing its own named constant to the union. The `repository`
  row and the two predecessor-edge tables are written only as part of the aggregate that owns them.
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

None recorded for this slice. The dispatch dicts are closed over the **thirty-one** command kinds; a
thirty-second kind is a vocabulary decision in `models/knowledge/candidate.py`, and these tables would be
extended with it in the same change. A record group that adds kinds the batch writes but no command addresses —
the census group's three relation tables are the current case — adds them to its own declared table set and to
neither dispatch table, which is the same shape the authored-effect succession edge has.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The writable-table union the refusal reads — the shipped seven, the two envelope tables, and each record group's own set subtracted to its non-envelope remainder, which is where this leaf's authored-effect group contributes nothing and the census group contributes its six. [1]
- The per-table readers, each delegating to the owning concept's own read. [2]
- The one-identity-per-kind map, with the multi-row commands handled separately. [3]
- The commands that address an existing row and therefore create nothing. [4]
- The batch's declared identity set. [5]
- **The existence question that admits the declared set: a record counts as present if it is already stored or will be by the time this batch is applied.** [6]
- The writable-table union the refusal reads, and the digest reader it uses for a stored row. [7]
- The per-table readers, each delegating to the owning concept's own read. [8]
- The one-identity-per-kind map, with the multi-row commands handled separately. [9]
- The commands that address an existing row and therefore create nothing. [10]
- The batch's declared identity set and the existence question that admits it. [11]
- The preconditions that consume these answers. [12]
- The vocabulary the writable table set mirrors. [13]
- The anchor row digest the anchor reader derives rather than stores. [14]
- **The census group's own table set, subtracted to its non-envelope remainder and appended to the union: its three record tables and three relation tables, declared beside its commands rather than restated here.** [15]
- **The three census record tables' readers — every census expectation is answered by the census module's own read, and the group's three relation tables are deliberately absent because no command addresses one.** [16]
- **The three census commands' identities: each names one record table and one `record_id`, so a duplicate check and a receipt address the row the command creates.** [17]
- **The census reads the three reader rows delegate to.** [18]
- **The census vocabulary's own declared table set, which the union's census constant is derived from rather than restated.** [19]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
