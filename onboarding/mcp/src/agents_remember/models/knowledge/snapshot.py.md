# mcp/src/agents_remember/models/knowledge/snapshot.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/snapshot.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The snapshot vocabulary**: one admitted candidate's local identity, the immutable receipt that binds it to
its admission, one closed snapshot stage, one publication request/result pair, the publication-state value a read
gates on, and the closed disposal union. It declares the local candidate layout (`knowledge-candidate.sqlite`
beside `candidate-receipt.json`) so the operation that opens the candidate for writes and the operation that
publishes it cannot disagree about which file is the working database.

Two splits carry the whole contract:

1. **Working identity versus published identity.** The database's *logical* identity is read from the database,
   never asserted — `CandidateReceipt` deliberately carries **no dataset digest** — so a caller cannot hand-write
   the identity its publication will later be compared against. What a publication installs is a *closed*
   representation of that identity at one frozen point, and the two are compared **by digest, not by bytes**: a
   `VACUUM`ed copy or a different SQLite page layout is the same knowledge.
2. **A receipt versus a verdict.** `CandidateResult`, `SnapshotPublicationResult`, `PublicationState` and
   `CandidateDisposalResult` report what was done and what exists. No field in this module can carry a semantic
   judgement, an acceptance or an approval.

Paths appear only as local operation facts. A destination path is a deliberate local configuration input, and no
portable knowledge record is built from one; the receipt stores no absolute path and no filesystem timestamp, so a
candidate stays identifiable after its directory moves.

## Code Commentary

### Logic

- `CANDIDATE_DATABASE_NAME` / `CANDIDATE_RECEIPT_NAME` and the two path builders (`candidate_database_path`,
  `candidate_receipt_path`) are the one declaration of the local layout. Both names are fixed here because two
  different operations derive a path from the same directory, and one of them writes while the other reads.
- `AdmittedCandidateDestination` is the typed handle the admitted-authority path builds: directory, namespace and
  the resolved `CandidateResolution`. Its two properties derive the database and receipt paths, so a caller that
  wrote into one database cannot publish another. It confers **no** authority by itself — it exists so a
  deserialized request cannot become admitted input.
- `CandidateBaseline` requires **both** the file and the exact logical identity the caller admitted for it, so a
  clone cannot silently start from whatever now sits at that path: the identity is re-read and compared before a
  byte is copied.
- `CandidateReceipt` carries only what survives being moved, copied or reopened — version, namespace, lane, the
  exact code and memory inputs, the schema generation and fingerprint, the snapshot/candidate/task references —
  and `receipt_digest` seals every other field. Its `_require_sealed_receipt` validator recomputes the seal on
  **every** construction, including on read, so a receipt edited in place is detectable without trusting the file
  that holds it.
- `build_candidate_receipt` is the one constructor: it derives every field from the admitted resolution and the
  schema the database actually carries (`model_construct` with a placeholder digest, then `model_copy` with the
  computed seal, then `model_validate` so the seal is checked by the same rule every reader applies).
- `CandidateResult` (`created` | `resumed` | `refused`) reports the identity the candidate holds **now** and the
  receipt that binds it; a refusal carries neither, and an admitted candidate cannot also carry a refusal. Its
  validator additionally requires the identity and the receipt to name one repository namespace.
- `PreparedKnowledgeSnapshot` is one closed stage, and carrying both `identity` and `file_digest` is deliberate:
  publication compares the logical identity to decide whether the destination already holds this knowledge, and
  the physical digest to detect a stage replaced between freezing it and installing it.
- `SnapshotDestinationRequest.expected_destination` is either the exact observed identity or `None` for "expected
  to be absent". There is no third mode: an unstated destination is not an expectation, so a publication cannot
  overwrite a file the caller never admitted.
- `SnapshotPublicationResult` reports `published` | `no_change` | `refused`, with both the destination identity it
  reached and the `previous_identity` that was there (`None` when absent). A refusal reports no identity at all:
  nothing was established about a destination state the operation did not produce.
- `PublicationState` (`current` | `candidate_snapshot_unpublished` | `refused`) reports the two identities it
  measured and **never guesses which side moved** — a newer runtime candidate needs a publication, a stale
  published file needs republishing or a refusal, and that decision is the caller's.
- `CandidateDisposition` is a closed discriminated union of exactly two members: `DiscardCandidate` (an explicit
  authorized discard naming the candidate identity) and `PublishedCandidate` (grounded in an exact published
  snapshot). `authorization_ref` is **carried rather than examined** — this layer decides *permissibility* (is the
  named identity the one the candidate holds now, so that discarding abandons no retained work?) while the caller
  owns the authority chain that made the discard authorized. A reference examined here would be this layer
  pretending to know an approval chain it does not own.
- There is no third disposal member on purpose: "it looked published" and "the candidate looked disposable" are
  not expressible.

### Conventions

- Every result is a **closed** model with an `after`-validator that refuses an inconsistent combination: a
  refusal must carry its refusal, a non-refusal must not, and a non-refused result must name what it established.
  A caller therefore branches on `state` and trusts the rest of the shape.
- Literal states and version strings live here rather than in the decider, per the route's "vocabulary is defined
  where it decides" rule.
- `CandidateReceiptVersion` is a `Literal` with one member plus a constant, so a v2 receipt is a new member rather
  than a free string.

### Invariants And Boundaries

- **The receipt never carries a dataset digest.** If it did, a caller could assert the identity its publication
  would be compared against; the identity is read from the database or it does not exist.
- **The receipt is derived, never accepted.** `build_candidate_receipt` takes a resolution and the observed schema;
  no code path accepts a caller-built receipt as an authoritative binding.
- **A receipt that does not seal itself is not a receipt.** `_require_sealed_receipt` runs on read, so a
  hand-edited file fails validation instead of being partially trusted.
- **No portable knowledge record is built from a path.** Paths are local operation facts; the receipt stores none.
- **No field carries a verdict.** Acceptance, approval and task status are deliberately not representable here.
- **`no_change` is a publication outcome, not a refusal code.** The result state and the reserved refusal code are
  different vocabularies; a consumer branches on `SnapshotPublicationResult.state`.
- **Boundary.** This module declares shapes and derives paths; it opens no database, copies no byte and writes no
  file. The behaviour is `memory/knowledge/{candidate_workspace,closed_snapshot,publication,materialization}.py`.

### Todos

None recorded for this slice. The disposal union is closed at two members; a third ground for disposal (an
accepted import, a merge result) would be a new member with its own evidence that no unique authored data remains,
not a relaxation of `DiscardedCandidate`/`PublishedCandidate`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one declaration of the local candidate layout and its two derived paths. | `CANDIDATE_DATABASE_NAME`; `CANDIDATE_RECEIPT_NAME`; `candidate_database_path`; `candidate_receipt_path` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-54; mcp/src/agents_remember/models/knowledge/snapshot.py:53-53; mcp/src/agents_remember/models/knowledge/snapshot.py:58-62; mcp/src/agents_remember/models/knowledge/snapshot.py:64-67 |
| The typed admitted handle that confers no authority by itself. | `AdmittedCandidateDestination` | mcp/src/agents_remember/models/knowledge/snapshot.py:70-93 |
| The baseline that requires both a file and the identity admitted for it. | `CandidateBaseline` | mcp/src/agents_remember/models/knowledge/snapshot.py:96-106 |
| The sealed receipt, its no-dataset-digest rule and the read-time seal validator. | `CandidateReceipt` | mcp/src/agents_remember/models/knowledge/snapshot.py:109-141 |
| The digest and the one derived constructor that seals a receipt. | `receipt_digest`; `build_candidate_receipt` | mcp/src/agents_remember/models/knowledge/snapshot.py:144-148; mcp/src/agents_remember/models/knowledge/snapshot.py:151-185 |
| The factual candidate outcome with its refusal/identity consistency rules. | `CandidateResult` | mcp/src/agents_remember/models/knowledge/snapshot.py:188-221 |
| The closed stage carrying both the logical identity and the physical digest. | `PreparedKnowledgeSnapshot` | mcp/src/agents_remember/models/knowledge/snapshot.py:224-236 |
| The destination request whose absent-expectation mode is the only way to overwrite. | `SnapshotDestinationRequest`; `PublishSnapshotRequest` | mcp/src/agents_remember/models/knowledge/snapshot.py:239-249; mcp/src/agents_remember/models/knowledge/snapshot.py:252-256 |
| The factual publication outcome with the previous identity it replaced. | `SnapshotPublicationResult` | mcp/src/agents_remember/models/knowledge/snapshot.py:259-293 |
| The publication-state measurement that never guesses which side moved. | `PublicationState` | mcp/src/agents_remember/models/knowledge/snapshot.py:296-321 |
| The closed disposal union, its carried-not-examined authorization reference and its verdict. | `DiscardCandidate`; `PublishedCandidate`; `CandidateDisposition`; `CandidateDisposalResult` | mcp/src/agents_remember/models/knowledge/snapshot.py:324-337; mcp/src/agents_remember/models/knowledge/snapshot.py:340-345; mcp/src/agents_remember/models/knowledge/snapshot.py:351-354; mcp/src/agents_remember/models/knowledge/snapshot.py:357-375 |
| The resolution shape every receipt field is derived from. | `CandidateResolution`; `ExactCandidateInput`; `KnowledgeLane`; `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:361-378; mcp/src/agents_remember/models/knowledge/candidate.py:125-135; mcp/src/agents_remember/models/knowledge/candidate.py:85-85; mcp/src/agents_remember/models/knowledge/candidate.py:113-123 |
| The canonical encoder the receipt seal is computed through. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-38 |
| The candidate lifecycle in which these shapes are produced. | `create_candidate`; `clone_candidate`; `open_candidate`; `authorize_candidate_disposal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:85-98; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:100-126; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:129-138; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:141-173 |
| The publication that installs a prepared stage. | `publish_candidate_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/publication.py:66-111; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |
| The node that proves a WAL-resident batch is published whole while a main-file copy is not. | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new snapshot vocabulary. It records the two splits the whole contract rests on (working identity read from the database versus published identity installed as a closed representation, compared by digest not bytes; and a receipt versus a verdict, with no field able to carry a judgement), the sealed receipt's deliberate absence of a dataset digest, the two-member closed disposal union with `authorization_ref` carried rather than examined, and the closed result validators that make `state` the only branch a caller needs. Verification metadata remains empty until closeout stamps the code commit.
