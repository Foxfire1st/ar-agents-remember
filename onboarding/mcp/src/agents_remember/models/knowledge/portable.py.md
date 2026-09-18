# mcp/src/agents_remember/models/knowledge/portable.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/portable.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The portable export/import vocabulary, and the boundary it draws around external input.**

Three splits carry this module's contract, and each exists because collapsing it would make a statement the
code cannot support:

- **A request versus an admitted identity.** `ExportRequest` carries the exact logical identity the caller
  admitted for the database it names. Storage re-reads it before encoding, so an export cannot silently
  describe a dataset that moved between the caller's check and the read.
- **A validated artifact versus a published dataset.** `PortableValidation` reports what was **checked**;
  `ImportResult` reports what now **exists**. Neither can carry a semantic judgement about whether the
  knowledge is correct, and neither can grant acceptance.
- **A staging fact versus a destination fact.** An import can validate perfectly and still not publish, so
  the result reports a verified logical identity separately from the state of the destination it did or did
  not reach.

## Code Commentary

### Logic

`ExportFormat` / `EXPORT_FORMAT` declare the one format member this package writes and reads
(`ar-knowledge-export/v1`). It is declared **here** rather than in the encoder so a caller can name the
format without importing the storage module that implements it — the same direction rule the rest of
`models.knowledge` follows.

`ExportRequest(database_path, expected_identity)` — `expected_identity` is **required**: an export is
addressed at *a dataset*, not at whatever a path currently holds, and the identity is what makes the two
the same object.

`ImportRequest(artifact, destination_path, expected_destination=None, expected_repository_id=None)` —
`expected_destination` is a closed choice in effect: the exact identity the caller observed, or `None` for
"the destination is expected to be absent". **There is no third mode.** `expected_repository_id` is
optional and only narrows; it rests on the same fact the repository table already declares (a dataset is
bound to exactly one namespace), so it admits nothing — it refuses an artifact that is internally valid but
belongs elsewhere.

`PortableValidation(state, ...)` — `row_counts` covers every canonical table including the empty ones,
because "present and empty" is the fact that separates a complete export from one that dropped a
collection. Its validator enforces the two-state contract: a `refused` validation must carry its refusal
and **reports no logical identity** (a refused artifact established none), while a `validated` one carries
no refusal and must name the namespace it is bound to and the digest its records produce.

`ExportResult` — the artifact is carried as **text**, not written, because the encoder has no filesystem
side effect at all; `row_counts` and the result's `notes` (`PORTABLE_NOTES`) travel with it. A `refused`
export carries its refusal and reports no artifact and no identity; an export that was produced carries no
refusal and must report the artifact, its format and the identity it seals.

`ImportResult(state, verified_identity, destination_identity, publication, ...)` — `state` is `installed`,
`no_change` (the destination already held the artifact's exact logical dataset, so no bytes were rewritten)
or `refused`. `verified_identity` is carried **independently of the state**, because a validated artifact
that failed to publish has an identity worth naming, and `publication` is `None` in that case rather than a
state. The validator enforces the rest: a refused import reports no destination identity and no publication
state, and an import that was not refused must name both identities **and** they must agree on the logical
digest.

### Conventions

- Models extend `KnowledgeModel` and use the shared `SHA256_PATTERN` and `PATH_MAX_LENGTH` from
  `models/knowledge/base.py`, so a malformed digest or an over-long destination ref is refused at
  construction rather than at use.
- Every consistency rule is an `@model_validator(mode="after")` — the same shape the rest of the knowledge
  vocabulary uses, so an internally inconsistent outcome is caught at the returning call site.
- The three-argument/three-state shapes are named for the caller's decision, not for the storage step that
  produced them.

### Invariants And Boundaries

- **Nothing here can carry a verdict or grant authority.** A row whose `state_at_origin` says `accepted`
  crosses as that stored value; no field in this module can promote it, and none can record whether the
  imported knowledge is *correct*.
- **A refused artifact has no identity to report.** That is why `PortableValidation` refuses a
  `logical_digest` on a refused validation rather than leaving the field open.
- **A destination that was reached must hold exactly what was verified.** `ImportResult` refuses to
  construct when `verified_identity.logical_digest != destination_identity.logical_digest`.
- **Boundary.** This module owns the wire vocabulary and its consistency rules. It holds no SQL, no file
  access, no Git resolution and no authorization decision; the reader/encoder live in
  `memory/knowledge/export_portable.py` and the operation in `memory/knowledge/export_import.py`.
- **Not re-exported from the package root.** `models/knowledge/__init__.py` does not import this module, so
  a consumer reaches it as `agents_remember.models.knowledge.portable`; the merge vocabulary follows the
  same convention, and the handoff names the full path for the next leaves.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three splits that carry this module's contract, in the form a consumer reads them. | "A request versus an admitted identity"; "A validated artifact versus a published dataset"; "A staging fact versus a destination fact" | mcp/src/agents_remember/models/knowledge/portable.py:1-17 |
| The one portable format member, declared here so a caller can name it without importing storage. | `ExportFormat`; `EXPORT_FORMAT` | mcp/src/agents_remember/models/knowledge/portable.py:32-33 |
| **The export request whose admitted identity is required rather than optional.** | `ExportRequest` | mcp/src/agents_remember/models/knowledge/portable.py:36-44 |
| **The import request: the closed two-mode destination admission, with no third mode, and the namespace narrowing that admits nothing.** | `ImportRequest` | mcp/src/agents_remember/models/knowledge/portable.py:47-63 |
| **The validation report: all tables counted including the empty ones, and no identity for a refused artifact.** | `PortableValidation` | mcp/src/agents_remember/models/knowledge/portable.py:66-98 |
| **The export result: the artifact carried as text because the encoder has no filesystem side effect.** | `ExportResult` | mcp/src/agents_remember/models/knowledge/portable.py:101-133 |
| **The import result: the verified identity carried independently of the state, and the two must agree.** | `ImportResult` | mcp/src/agents_remember/models/knowledge/portable.py:136-176 |
| The shared pattern and length constants every field is validated against, and the model base. | `KnowledgeModel`; `SHA256_PATTERN`; `PATH_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:34-37; mcp/src/agents_remember/models/knowledge/base.py:19-19; mcp/src/agents_remember/models/knowledge/base.py:27-27 |
| The identity shape both requests and both results carry. | `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:185-194 |
| The refusal shape a refused validation or result carries. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:225-235 |
| The operation that consumes this vocabulary. | `export_knowledge_dataset`; `import_knowledge_dataset` | mcp/src/agents_remember/memory/knowledge/export_import.py:133-192; mcp/src/agents_remember/memory/knowledge/export_import.py:195-244 |
| The reader, validator and encoder this vocabulary describes. | `parse_export`; `validate_export`; `encode_export` | mcp/src/agents_remember/memory/knowledge/export_portable.py:490-543; mcp/src/agents_remember/memory/knowledge/export_portable.py:667-712; mcp/src/agents_remember/memory/knowledge/export_portable.py:276-301 |
| The nodes that hold the round trip, the preservation rule and the destination behaviour to this vocabulary. | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset"; "test_accepted_origin_state_crosses_as_data_and_is_not_promoted"; "test_a_destination_is_replaced_only_for_the_admitted_identity" | mcp/tests/test_knowledge_portable_roundtrip.py:357-427; mcp/tests/test_knowledge_portable_roundtrip.py:473-486; mcp/tests/test_knowledge_portable_roundtrip.py:1023-1080 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T08:36:42+00:00: Generated citation repair: `SnapshotIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:185-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:225-235. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: `SnapshotIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:169-178. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:06:32+00:00: Generated citation repair: `SnapshotIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:158-167. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:06:32+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:207-217. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T05:29:42+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:190-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T02:37:44+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:175-185. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T22:33:10+00:00: Generated citation repair: `SnapshotIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:139-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T22:33:10+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:163-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T06:49:47+00:00: Generated citation repair: `KnowledgeRefusal` repointed to mcp/src/agents_remember/models/knowledge/result.py:148-158. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T15:45:00+00:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): created this one-to-one card for the portable wire vocabulary. It records the three splits the module's own docstring makes load-bearing — a request versus an admitted identity, a validated artifact versus a published dataset, and a staging fact versus a destination fact — the closed two-mode destination admission in `ImportRequest` (with the namespace narrowing that admits nothing), the all-tables `row_counts` that separates a complete export from one that dropped a collection, the carrier-not-writer export result that mirrors the encoder's missing filesystem side effect, and the import result whose `verified_identity` is carried independently of the state and whose two identities must agree on the logical digest. It states the module's own absences as boundaries — no verdict field, no authority, no identity for a refused artifact — and records that the module is deliberately **not** re-exported from `models/knowledge/__init__.py`, so a consumer names `agents_remember.models.knowledge.portable` as the handoff does. Verification metadata remains empty until closeout stamps the code commit.
