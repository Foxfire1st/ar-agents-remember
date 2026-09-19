# mcp/src/agents_remember/memory/knowledge/candidate_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The writable-table union the refusal reads — the shipped seven, the two envelope tables, and each record group's own set subtracted to its non-envelope remainder, which is where this leaf's authored-effect group contributes nothing and the census group contributes its six. | `WRITABLE_TABLES`; `EFFECT_ONLY_WRITABLE_TABLES` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:114-122; mcp/src/agents_remember/memory/knowledge/candidate_records.py:94-96 |
| The per-table readers, each delegating to the owning concept's own read. | "_RECORD_READERS: dict[str, RecordReader] = {"; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:280-315; mcp/src/agents_remember/memory/knowledge/candidate_records.py:157-161 |
| The one-identity-per-kind map, with the multi-row commands handled separately. | "_WRITTEN_IDENTITY: dict[str, Callable[[Any], tuple[str, str]]] = {"; "def written_identities(command: ChangeCommand) -> IdentityPairs:" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:320-379; mcp/src/agents_remember/memory/knowledge/candidate_records.py:399-408 |
| The commands that address an existing row and therefore create nothing. | "_ADDRESSES_EXISTING: tuple[str, ...] = ("; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:383-396; mcp/src/agents_remember/memory/knowledge/candidate_records.py:495-500 |
| The batch's declared identity set. | `pending_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:503-509 |
| **The existence question that admits the declared set: a record counts as present if it is already stored or will be by the time this batch is applied.** | `present` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:512-519 |
| The writable-table union the refusal reads, and the digest reader it uses for a stored row. | `WRITABLE_TABLES`; `stored_record_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:114-122; mcp/src/agents_remember/memory/knowledge/candidate_records.py:128-134 |
| The per-table readers, each delegating to the owning concept's own read. | "_RECORD_READERS: dict[str, RecordReader] = {"; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:280-315; mcp/src/agents_remember/memory/knowledge/candidate_records.py:157-161 |
| The one-identity-per-kind map, with the multi-row commands handled separately. | "_WRITTEN_IDENTITY: dict[str, Callable[[Any], tuple[str, str]]] = {"; "def written_identities(command: ChangeCommand) -> IdentityPairs:" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:320-379; mcp/src/agents_remember/memory/knowledge/candidate_records.py:399-408 |
| The commands that address an existing row and therefore create nothing. | "_ADDRESSES_EXISTING: tuple[str, ...] = ("; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:383-396; mcp/src/agents_remember/memory/knowledge/candidate_records.py:495-500 |
| The batch's declared identity set and the existence question that admits it. | `pending_identities`; `present` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:503-509; mcp/src/agents_remember/memory/knowledge/candidate_records.py:512-519 |
| The preconditions that consume these answers. | `require_expected_records`; `require_insertions_absent`; `require_command_targets` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:185-206; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:368-384; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:387-399 |
| The vocabulary the writable table set mirrors. | "MutableRecordTable = Literal[" | mcp/src/agents_remember/models/knowledge/candidate.py:140-140 |
| The anchor row digest the anchor reader derives rather than stores. | `anchor_row_digest` | mcp/src/agents_remember/memory/knowledge/records.py:366-381 |
| **The census group's own table set, subtracted to its non-envelope remainder and appended to the union: its three record tables and three relation tables, declared beside its commands rather than restated here.** | `CENSUS_ONLY_WRITABLE_TABLES` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:110-112 |
| **The three census record tables' readers — every census expectation is answered by the census module's own read, and the group's three relation tables are deliberately absent because no command addresses one.** | `census_records.inventory_row_digest`; `census_records.claim_digest`; `census_records.disposition_digest`; "census_inventory_row"; "census_claim"; "census_disposition" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:308-314 |
| **The three census commands' identities: each names one record table and one `record_id`, so a duplicate check and a receipt address the row the command creates.** | `"add_census_inventory_row": lambda command: ("census_inventory_row", command.record_id)`; `"add_census_claim": lambda command: ("census_claim", command.record_id)`; `"add_census_disposition": lambda command: ("census_disposition", command.record_id)`; "add_census_inventory_row"; "add_census_claim"; "add_census_disposition" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:363-371 |
| **The census reads the three reader rows delegate to.** | `inventory_row_digest`; `claim_digest`; `disposition_digest` | mcp/src/agents_remember/memory/knowledge/census_records.py:893-901; mcp/src/agents_remember/memory/knowledge/census_records.py:904-911; mcp/src/agents_remember/memory/knowledge/census_records.py:914-923 |
| **The census vocabulary's own declared table set, which the union's census constant is derived from rather than restated.** | `CENSUS_WRITABLE_TABLES` | mcp/src/agents_remember/models/knowledge/census.py:364-373 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): **re-read every citation this card carries against the staged working candidate and recorded the census record group's share of the batch vocabulary.** The leaf added `CENSUS_ONLY_WRITABLE_TABLES` — the census vocabulary's eight-name `CENSUS_WRITABLE_TABLES` minus the two envelope tables — and appended it to `WRITABLE_TABLES`, so the union is now **thirty** tables, equal to `MutableRecordTable`'s thirty members; the union paragraph and the writable-table convention were both re-worded to that count and now name every group's own constant, including the census's. Three reader rows (`census_inventory_row`, `census_claim`, `census_disposition`) and three identity rows (`add_census_inventory_row`, `add_census_claim`, `add_census_disposition`) joined the two dispatch dicts, and the card now states why the group's three *relation* tables are absent from both: they are written only as part of the aggregate that owns them, so no command addresses one — the disposition the authored-effect succession edge already takes — and they stay in the union because the batch does write them. Two stale Logic claims were corrected rather than softened: `written_identities` is no longer "one per command kind for eleven kinds" (twenty-five kinds sit in `_WRITTEN_IDENTITY` and the multi-row commands are answered by two earlier dispatch shapes), and `_ADDRESSES_EXISTING` holds **eight** kinds, not five, with the Todos closure count moved from eighteen to **thirty-one** command kinds. Eleven rows whose cited ranges this leaf's insertions had moved were **re-cited by hand to each construct's declaration extent** — the union and `EFFECT_ONLY_WRITABLE_TABLES`, both reader rows, both identity rows, `_ADDRESSES_EXISTING`/`inserted_identities`, `pending_identities`, `present`, `stored_record_digest`, the two preconditions rows into `batch_preconditions.py` and the three identity readers — and five rows were added for the census union constant, the census readers, the census identities, the census digest functions and the vocabulary the union is derived from. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
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
