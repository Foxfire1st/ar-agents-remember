# mcp/src/agents_remember/memory/knowledge/candidate_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:05:00+02:00 |
| lastVerifiedCommitHash | `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890` |
| lastVerifiedCommitDate | 2026-09-18T01:58:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

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
| The thirteen directly writable tables and the refusal of a table outside them. | `WRITABLE_TABLES`; `stored_record_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:39-53; mcp/src/agents_remember/memory/knowledge/candidate_records.py:59-65 |
| The per-table readers, each delegating to the owning concept's own read. | "_RECORD_READERS: dict[str, RecordReader] = {"; `_anchor_digest` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:106-120; mcp/src/agents_remember/memory/knowledge/candidate_records.py:88-90 |
| The one-identity-per-kind map, with the two-identity claim command handled separately. | "_WRITTEN_IDENTITY: dict[str, Callable[[Any], tuple[str, str]]] = {"; "def written_identities(command: ChangeCommand) -> IdentityPairs:" | mcp/src/agents_remember/memory/knowledge/candidate_records.py:125-151; mcp/src/agents_remember/memory/knowledge/candidate_records.py:166-187 |
| The commands that address an existing row and therefore create nothing. | "_ADDRESSES_EXISTING: tuple[str, ...] = ("; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:155-163; mcp/src/agents_remember/memory/knowledge/candidate_records.py:190-195 |
| The batch's declared identity set and the existence question that admits it. | `pending_identities`; `present` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:198-204; mcp/src/agents_remember/memory/knowledge/candidate_records.py:207-214 |
| The preconditions that consume these answers. | `require_expected_records`; `require_insertions_absent`; `require_command_targets` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:129-240 |
| The vocabulary the writable table set mirrors. | "MutableRecordTable = Literal[" | mcp/src/agents_remember/models/knowledge/candidate.py:122-136 |
| The anchor row digest the anchor reader derives rather than stores. | `anchor_row_digest` | mcp/src/agents_remember/memory/knowledge/records.py:366-381 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T04:55+02:00 — 260915-KS-L11 owning seat (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this claim against the source and re-cited it by hand, replacing a generated projection.** The claim said *seven* directly writable tables; `WRITABLE_TABLES` now declares **thirteen** (`candidate_records.py:39-53`, counted from the declaration itself, and equal to `MutableRecordTable`'s thirteen members in `models/knowledge/candidate.py`). The wording and the range were both rewritten by an agent that read the declaration, so the citation is no longer a mechanical anchor-range projection: the range is the declaration the claim's own words describe.
- 2026-09-18T01:18+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this card against the source for the round-2 citation work and recorded a contradiction instead of softening the row.** The row above reading "The thirteen directly writable tables and the refusal of a table outside them" is **no longer true**: `WRITABLE_TABLES` (`mcp/src/agents_remember/memory/knowledge/candidate_records.py:39-53`) now holds **thirteen** names — the seven it held at `76c7697c` plus `knowledge_record`, `record_revision`, `facet_attachment`, `facet_decision_supersession`, `explanation` and `explanation_revision`, which this leaf's facet write path added. The row's citation was re-pointed to that tuple and its anchor left naming the tuple; its *count* was not rewritten, because a claim's meaning belongs to the owning seat rather than to the citation curator. The one-word correction owed is `seven` → `thirteen`. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp. No content impact: this entry records a review, not a content change.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `_ADDRESSES_EXISTING`; `inserted_identities` repointed to mcp/src/agents_remember/memory/knowledge/candidate_records.py:155-163; mcp/src/agents_remember/memory/knowledge/candidate_records.py:190-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `pending_identities`; `present` repointed to mcp/src/agents_remember/memory/knowledge/candidate_records.py:198-204; mcp/src/agents_remember/memory/knowledge/candidate_records.py:207-214. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `MutableRecordTable` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:122-136. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new batch identity vocabulary. It records the one-identity-scheme rule (a digest here is exactly what a read exposes), the read-only boundary that lets the preconditions and the apply step share it, the addressing-versus-creating distinction that lets one row be edited and removed in one batch, and the whole-sequence pending set that makes a forward reference legal. Verification metadata remains empty until closeout stamps the code commit.
