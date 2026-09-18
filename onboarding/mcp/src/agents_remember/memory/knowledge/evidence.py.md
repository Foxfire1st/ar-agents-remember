# mcp/src/agents_remember/memory/knowledge/evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate |  2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generation this write path requires, read from the registry rather than spelled as a literal. | `REQUIRED_EVIDENCE_GENERATION` | mcp/src/agents_remember/memory/knowledge/evidence.py:88-88 |
| The two standalone write entry points and the batch dispatch. | `add_evidence_claim`; `add_verification_observation`; `apply_evidence_command` | mcp/src/agents_remember/memory/knowledge/evidence.py:134-145; mcp/src/agents_remember/memory/knowledge/evidence.py:148-160; mcp/src/agents_remember/memory/knowledge/evidence.py:163-176 |
| The two in-transaction application steps that raise a typed refusal for the batch to roll back. | `_apply_add_claim`; `_apply_add_observation` | mcp/src/agents_remember/memory/knowledge/evidence.py:183-262; mcp/src/agents_remember/memory/knowledge/evidence.py:265-314 |
| The link resolution that refuses an unresolved subject, anchor or coverage endpoint before any row exists. | `require_claim_links`; `require_evidence_subject`; `require_facet_revision_subject` | mcp/src/agents_remember/memory/knowledge/evidence.py:413-427; mcp/src/agents_remember/memory/knowledge/evidence.py:431-452; mcp/src/agents_remember/memory/knowledge/evidence.py:456-466 |
| The generation gate: a refusal naming both versions, never a migration. | `require_evidence_generation` | mcp/src/agents_remember/memory/knowledge/evidence.py:491-510 |
| The origin rule that makes a supporting record a proposal and refuses accepted data. | `require_proposed_origin` | mcp/src/agents_remember/memory/knowledge/evidence.py:515-525 |
| The write-time digest decision: measured against the bytes when a root is available, refused when the bytes contradict it. | `checked_artifact_reference` | mcp/src/agents_remember/memory/knowledge/evidence.py:532-582 |
| The observation insert whose statement is derived from the codec's declared column order. | `_OBSERVATION_INSERT_COLUMNS`; `_OBSERVATION_INSERT` | mcp/src/agents_remember/memory/knowledge/evidence.py:117-120; mcp/src/agents_remember/memory/knowledge/evidence.py:122-125 |
| The case that asserts the digest is checked against real bytes and recorded as checked. | "def test_the_write_time_digest_is_checked_against_the_bytes_and_recorded_as_checked(" | mcp/tests/test_knowledge_evidence_observations.py:329-380 |
| The case that asserts a digest the bytes contradict is refused with exact facts. | "def test_a_digest_that_does_not_describe_the_bytes_is_refused_with_exact_facts(" | mcp/tests/test_knowledge_evidence_observations.py:381-415 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the supporting records' write path. It records the five shaping rules, the measured rather than asserted digest flag, the derived observation insert order, and the generation gate that refuses instead of migrating. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
