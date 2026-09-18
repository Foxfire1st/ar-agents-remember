# mcp/src/agents_remember/models/knowledge/candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:05:00+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

**The whole vocabulary of the one candidate-change write boundary.** A `ChangeBatch` names the resolved
context it was authored against, the exact record states it expects, and a **closed** sequence of eighteen
domain commands; the same module owns the receipt (`MutationResult`) that reports what the operation did.
Nothing here can express arbitrary SQL, request an approval or promote a proposal — the union is the
operation's entire reach, so those refusals are properties of the vocabulary rather than rules the
operation remembers to apply.

This module is the model-level half of `KS-R03`; the operation that consumes it is
`memory/knowledge/candidate.py`, and the vocabulary is served through `models/knowledge/__init__.py`.

## Code Commentary

### Logic

- **Resolved context versus proposed content.** `KnowledgeContext` carries the identity the admitted
  runtime *resolved* — namespace, lane, both exact candidate inputs, the logical knowledge snapshot and the
  opaque `snapshot_ref`/`candidate_ref`/`task_ref` — plus `context_digest`, which `context_digest()` computes
  over every field except itself. `_require_sealed_context` refuses a context whose digest does not seal it,
  and `_require_one_namespace` refuses one whose snapshot belongs to another repository.
- **Expected state versus assumed state.** `ExpectedRecord` is `present` with a digest or `absent` without
  one, enforced at construction. There is deliberately no third mode: "I did not say" is not an expectation,
  so a caller cannot leave a mutable record unnamed and have the batch proceed on the strength of its silence.
- **`CandidateResolution` deliberately has no dataset-identity field.** A caller describes *which* candidate
  it admitted and *which* exact tree inputs it resolved; the application reads the identity those inputs
  currently hold. That is what makes the batch's dataset precondition a checked value instead of a remembered one.
- **The closed command union.** `ProposedCommand` is a discriminated union of exactly eighteen frozen models —
  `AddInvariant`, `AddInvariantRevision`, `SetInvariantLabel`, `AddFamily`, `AddFamilyRevision`,
  `SetFamilyLabel`, `AddSourceAnchor`, `RemoveSourceAnchor`, `AddFamilyMember`, `RemoveFamilyMember`,
  `AddRealizationClaim`, `RemoveRealizationClaim` — discriminated on `kind`. There is no promotion member, no
  approval member, no arbitrary-SQL member and no free-form field. `ChangeCommand` is an alias.
  `AddInvariantRevision`/`AddFamilyRevision` carry a `RevisionDraft`/`FamilyRevisionDraft` with no
  `payload_digest`, so the store recomputes the seal rather than accepting it.
- **`ChangeBatch` orders both halves differently on purpose.** `expected_records` is checked as a set and
  refuses two expectations for one record (`_require_unique_expectations`); `commands` are applied in the
  order given. The *declarations* inside the commands are validated over the completed graph, not over that
  order — see `memory/knowledge/batch_preconditions.py`.
- **The receipt states facts only.** `RecordIdentity.state` is exactly `written | removed`: a written row
  carries the digest the store computed for it, a removed row carries the identity and the digest it *had*.
  A command whose requested effect was already stored contributes **no** entry, because no statement ran.
  `MutationResult._require_consistent_receipt` refuses a refusal that carries changed rows or unequal
  before/after identities, a non-refused result carrying a refusal, a `no_change` result with entries, a
  `changed` result with an empty entry list, and a `changed` result whose two identities are equal.
- **`SnapshotIdentity`** is `repository_id` + `schema_version` + `logical_digest`; it is the portable content
  identity the whole substrate compares on, and its digest is produced by `memory/knowledge/logical.py`.
- **The lane vocabulary is named so it can be refused by name.** `KnowledgeLane` includes the read-only
  `baseline` selection, which is a member precisely so a request can *name* it and be refused rather than fail
  to parse; `CANDIDATE_LANES` is the writable pair. `task-candidate` is a member of both, and the operation
  refuses it until a resolved, owner-validated task binding exists.

### Conventions

- Literal vocabularies (`KnowledgeLane`, `MutableRecordTable`) are declared here and imported by the decider,
  never declared by the decider and re-exported downward.
- Every model inherits `KnowledgeModel`: frozen, `extra="forbid"`, with the shared identifier and digest
  patterns from `models/knowledge/base.py`. A payload naming an unknown field fails at construction.
- Command payloads are **provenance-free**: no command carries an `Authorship`. The admitted envelope is
  attached by the store, so a draft that arrived carrying its own actor, authorization or instant is re-stamped.
- `MutableRecordTable` names the thirteen tables a command can write. The `repository` row and the two
  predecessor-edge tables are written only as part of the aggregate that owns them, so an expectation about
  them would name a state no command could produce.

### Invariants And Boundaries

- **The union is the reach.** A thirteenth command kind cannot be expressed, and no field anywhere in this
  module can carry an approval, an acceptance or a SQL statement.
- **A context is compared, never trusted.** The digest is computed by the module, and the operation
  re-derives it inside its own transaction; `model_copy(update=…)` is a public validator-bypassing path, which
  is exactly why the operation-level comparison exists.
- **Values, not rows.** Model immutability is a process-local property; refusing an update to a *stored* row is
  a storage rule enforced by the schema triggers and the operation's preconditions.
- **The carried references prove nothing about the world.** `snapshot_ref`, `candidate_ref` and `task_ref` are
  opaque strings recorded as resolved facts; nothing here re-verifies that a Git object or a task contract
  exists, and a consumer must not read them as that proof.
- **Boundary.** This module decides shapes and consistency; whether a stored record matches an expectation,
  whether an identity is already stored, and which refusal code a condition produces are the operation's
  checks and `refusals.py`'s wording.

### Todos

None recorded for this slice. The vocabulary is complete for the increment that consumes it; a later leaf that
implements task-bound admission replaces the `task-candidate` refusal without widening this union, and the
publication/merge requirements (`KS-R04`, `KS-R05`) reuse `SnapshotIdentity` rather than redefining it.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The served knowledge vocabulary as an explicit re-export list, which this module's names joined. | `__all__` | mcp/src/agents_remember/models/knowledge/__init__.py:98-170 |
| The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. | `KnowledgeLane`; `CANDIDATE_LANES` | mcp/src/agents_remember/models/knowledge/candidate.py:107-107; mcp/src/agents_remember/models/knowledge/candidate.py:109-109 |
| The portable content identity and the two exact candidate inputs. | `SnapshotIdentity`; `ExactCandidateInput` | mcp/src/agents_remember/models/knowledge/candidate.py:158-167; mcp/src/agents_remember/models/knowledge/candidate.py:170-179 |
| The resolved context and its two consistency validators. | `KnowledgeContext` | mcp/src/agents_remember/models/knowledge/candidate.py:182-223 |
|  The module-level digest the validator calls and the operation re-derives. | "def context_digest(" | mcp/src/agents_remember/models/knowledge/candidate.py:226-226  |
| The receipt entry, including the two-state rule and the no-entry case. | `RecordIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:220-241 |
| The expectation model and its present-with-digest / absent-without-digest rule. | `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:244-266 |
| **The twenty-two-member discriminated union, with no promotion, approval or SQL member — the eighteen it held at `KS-R14@v1` plus this leaf's four composition kinds.** | `ProposedCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:469-493 |
| The alias a batch's commands travel under, and the construct that makes the union's membership checkable in one place. | `ChangeCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:495-589 |
| The resolution shape that deliberately omits the dataset identity. | `CandidateResolution` | mcp/src/agents_remember/models/knowledge/candidate.py:498-515 |
| The batch and the receipt consistency validator the operation's results must satisfy. | `ChangeBatch`; `MutationResult` | mcp/src/agents_remember/models/knowledge/candidate.py:518-545; mcp/src/agents_remember/models/knowledge/candidate.py:546-546 |
| The operation that consumes this vocabulary and the context it re-derives inside its transaction. | `change_candidate`; `_require_bound_context` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:148-183 |
| The composition seam that resolves a context from a live candidate and seals it. | `resolve_candidate_context`; `build_candidate_context`; `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:252-273; mcp/src/agents_remember/application/knowledge.py:275-301; mcp/src/agents_remember/application/knowledge.py:303-315 |
| The frozen base and the shared identifier/digest patterns every model here inherits. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The operation that consumes this vocabulary and the pre-lock lane check it applies first. | `change_candidate`; `require_writable_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:83-102 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:00+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the two union claims this leaf widened and corrected the counts.** `ProposedCommand` now holds **twenty-two** variants — the eighteen it held at the previous leaf plus this leaf's four composition command kinds — and `ChangeCommand` is the alias it travels under; the card's eighteen-member wording was therefore false and is corrected, with the union row split into one row per anchor so each resolves in its own declaration. `MutableRecordTable` gained the six composition tables. The generated bullet that had rewritten the alias row's range mechanically was removed and replaced by this entry. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T04:55+02:00 — 260915-KS-L11 owning seat (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this claim against the source and re-cited it by hand, replacing a generated projection.** The claim said *twelve* members; the union now admits **eighteen** — the twelve shipped command models plus the six facet commands this leaf adds — at `models/knowledge/candidate.py:372-392`. The card's three other statements of the old count (the summary, the closed-union invariant and the `MutableRecordTable` sentence) were reconciled in the same read, so every count in this card now matches the declaration.
- 2026-09-18T01:18+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this card against the source for the round-2 citation work and recorded a contradiction instead of softening the row.** The row above reading "The eighteen-member discriminated union with no promotion, approval or SQL member" is **no longer true**: `ProposedCommand` (`mcp/src/agents_remember/models/knowledge/candidate.py:372-392`) now admits **eighteen** members — the shipped twelve plus `AddFacet`, `AttachFacet`, `RemoveFacetAttachment`, `AuthorExplanation`, `AddExplanationRevision` and `DesignateExplanation`, which this leaf's authored-judgment vocabulary added; `ChangeCommand` still aliases it at `:394`. The row's citation and range follow the union as it now stands, and its *member count* was not rewritten, because a claim's meaning belongs to the owning seat rather than to the citation curator. The one-word correction owed is `eighteen-member` → `eighteen-member`. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp. No content impact: this entry records a review, not a content change.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `KnowledgeLane`; `CANDIDATE_LANES` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:99-99; mcp/src/agents_remember/models/knowledge/candidate.py:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "def context_digest(" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `RecordIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:220-241. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `ExpectedRecord` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:244-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `CandidateResolution` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:397-414. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-change vocabulary. It records the closed twelve-command union with no promotion/approval/SQL member, the resolved-versus-authored and expected-versus-assumed splits, the deliberately absent dataset-identity field on `CandidateResolution`, the two-state receipt and its consistency validator, and the `baseline`/`task-candidate` lane distinction that exists so both can be refused by name. Verification metadata remains empty until closeout stamps the code commit.
