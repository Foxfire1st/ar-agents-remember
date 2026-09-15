# mcp/src/agents_remember/models/knowledge/result.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/result.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The typed operation requests, the refusal vocabulary and the mutation results: every knowledge failure is a
returned value with a code, an offending record and a concrete next action, rather than an exception a caller has
to parse.

## Code Commentary

### Logic

`KnowledgeOperation` is the three-member literal union of mutating operations (`create_repository`,
`create_invariant`, `create_invariant_revision`). `KnowledgeRefusalCode` declares fourteen codes:
`invalid_payload`, `unauthorized_scope`, `unsupported_schema`, `destination_occupied`, `candidate_busy`,
`lock_capability_unavailable`, `missing_expected_row`, `duplicate_identity`, `immutable_revision`,
`invalid_reference`, `lineage_cycle`, `relationship_constraint`, `unknown_invariant`, `no_change`.

`KnowledgeRefusal` carries `code`, `operation`, `detail`, optional `table`/`record_id`/`expected`/`observed` and a
required `next_action`.

`RevisionDraft` is the caller-supplied aggregate **before sealing** and therefore has no `payload_digest` field; it
refuses a self-declared predecessor. `RevisionRequest` pairs a draft with its `repository_id`, and
`InvariantRequest` carries an invariant identity insert.

`CreateRevisionResult`, `CreateInvariantResult` and `RepositoryCreationResult` each enforce their own outcome
consistency in an after-validator: a `created` result carries a digest where applicable, `stored=True` and no
refusal; a `no_change` result stored nothing and carries no refusal; a `refused` result must carry its refusal and
must not claim it stored a row.

### Conventions

Codes are a declared vocabulary: a storage failure with no code here is a defect, not a new code invented at the
raise site. A caller branches on `code`, never on message text.

### Invariants And Boundaries

- The digest is absent from `RevisionDraft` by design — the store recomputes and stores it, so a caller cannot
  present a payload whose seal belongs to different content.
- The result models are the typed contract of the operation; they refuse an internally inconsistent outcome at
  construction, so an "everyone agrees" bug is caught at the returning call site and not by a caller's branch.
- `unsupported_schema` and `missing_expected_row` are declared vocabulary that this leaf's code does not raise
  (schema failures surface as `KnowledgeStorageError`); they are recorded here as available interface, not as
  proven behaviour of the current write path.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared refusal vocabulary, with each member naming a distinct observable failure. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:31-48 |
| The refusal value carrying code, operation, offending record and next action. | `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/result.py:51-61 |
| The digest-free caller draft that refuses a self-declared predecessor. | `RevisionDraft`; `_refuse_self_predecessor` | mcp/src/agents_remember/models/knowledge/result.py:64-87 |
| The three outcome models and their consistency validators. | `CreateRevisionResult`; `CreateInvariantResult`; `RepositoryCreationResult` | mcp/src/agents_remember/models/knowledge/result.py:106-174 |
| The factories that build every refusal in this package, one per code and case. | `refusal`; `lineage_cycle_refusal`; `map_sqlite_error` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-77; mcp/src/agents_remember/memory/knowledge/refusals.py:238-277; mcp/src/agents_remember/memory/knowledge/refusals.py:308-350 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed request/refusal/result vocabulary. It records that `RevisionDraft` has no digest field by design and that two declared codes are not raised by the current write path. Verification metadata remains empty until closeout stamps the code commit.
