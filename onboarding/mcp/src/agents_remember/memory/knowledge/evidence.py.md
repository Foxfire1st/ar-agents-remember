# mcp/src/agents_remember/memory/knowledge/evidence.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The supporting records' write path: resolve every link, check the artifact digest against the bytes when
a root is available, gate on the generation, and write one sealed aggregate inside the batch's existing
transaction.

## Code Commentary

### Logic

Both records are written through the one operation that writes the knowledge graph. In a batch they arrive
as the two authored commands this leaf appends to the closed union; as a standalone call they arrive
through `add_evidence_claim` and `add_verification_observation`, which are the same driver shape the facet
writes use — one candidate lock, one `BEGIN IMMEDIATE` transaction, one in-transaction step that raises a
typed refusal for the batch path to roll back. `apply_evidence_command` is the batch dispatch.

**Five rules shape the module, and each is a clause of the leaf's requirement.**

1. *Code resolves the links; code does not judge what the evidence demonstrates.* `require_claim_links`
   resolves the subject, the evidence anchor and every claimed-coverage endpoint against rows that exist in
   this namespace, and a link that does not resolve is a typed `invalid_reference` refusal **before** any
   row is written. `require_evidence_subject` and `require_facet_revision_subject` are the per-kind halves.
   No function here returns anything but rows, digests and refusals.
2. *The author envelope comes from the admission, never from the caller.* `_write_envelope` writes the
   provenance the admitted boundary built; neither command nor payload carries a field that could become
   it.
3. *Persisting a record endorses nothing.* Both records store `proposed` origin data, and
   `require_proposed_origin` refuses accepted origin data with the shipped `promotion_not_supported` before
   any row exists.
4. *The artifact digest is compared against bytes when the caller supplies the bytes' root.* The rule does
   not choose between verifying and asserting; it decides that the record **states which happened**.
   `checked_artifact_reference` therefore records `digest_checked_against_bytes` truthfully — true only
   after it read the artifact and found the recorded sha256 and size, false when no root was available to
   read — and it **refuses** a digest that disagrees with the bytes at the recorded path rather than writing
   a record whose stated digest it observed to be false. `digest_checked_against_bytes` is measured, never
   asserted.
5. *The generation gate is a refusal, not a migration.* `require_evidence_generation` refuses a dataset
   whose recorded generation predates this leaf's tables, naming the observed and required versions as
   facts, and nothing is migrated, widened, repaired or extended in place.

**The observation's insert statement is derived from the codec's declared column order.**
`_OBSERVATION_INSERT_COLUMNS` is the generation's own order after the two key columns, and
`_OBSERVATION_INSERT` is built from it, so the statement and the row it is given cannot describe different
orders. The same shape exists in the shipped codecs and is a trap for the next leaf: a statement and a codec
that restate the same order can disagree, and the disagreement presents as a misleading `NOT NULL
constraint failed` rather than as an ordering error.

### Conventions

A refusal raised inside the transaction is carried out as `KnowledgeRefused` so the batch can roll back and
return it; `_applied`, `_refused` and `_written` build the typed result states. Every refusal is a typed
`KnowledgeRefusal` with a shipped code that names the fact — `invalid_reference` for an unresolved link and
for a digest the bytes contradict, `unsupported_schema` for the generation gate, `promotion_not_supported`
for accepted origin data, and the shipped `invalid_payload` for a payload-shape failure — so no refusal
vocabulary was widened by this leaf.

### Invariants And Boundaries

- **Nothing here copies artifact bytes into the database.** The reference is an identity of an artifact that
  lives somewhere else; there is no second content store.
- **A stored digest is either verified or never claimed verified.** There is no path that re-pins a stored
  digest to whatever bytes are present now, and no path that writes a digest it observed to be false.
- **A missing artifact at write time is recorded, not refused.** The record is written with the resolution
  state that says so; a missing artifact never erases the record that referenced it.
- **Link resolution is complete before the first write.** The subject, the anchor and every coverage
  endpoint are checked up front, so a partially written claim is not a state this code can reach.
- **The generation gate reads the number off the record.** `REQUIRED_EVIDENCE_GENERATION` is the generation
  constant, and a renumber changes that binding rather than the gate's logic.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The generation this write path requires, read from the registry rather than spelled as a literal. [1]
- The two standalone write entry points and the batch dispatch. [2]
- The two in-transaction application steps that raise a typed refusal for the batch to roll back. [3]
- The link resolution that refuses an unresolved subject, anchor or coverage endpoint before any row exists. [4]
- The generation gate: a refusal naming both versions, never a migration. [5]
- The origin rule that makes a supporting record a proposal and refuses accepted data. [6]
- The write-time digest decision: measured against the bytes when a root is available, refused when the bytes contradict it. [7]
- The observation insert whose statement is derived from the codec's declared column order. [8]
- The case that asserts the digest is checked against real bytes and recorded as checked. [9]
- The case that asserts a digest the bytes contradict is refused with exact facts. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
