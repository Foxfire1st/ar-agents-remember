# mcp/src/agents_remember/models/knowledge/candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `7dcec036094768c5f50e571fb45e59a27ae78efc`|
| lastVerifiedCommitDate |  2026-09-19T18:19:12+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

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

**Two appended members of the closed union, and no promotion member.** `AddEvidenceClaim` and `AddVerificationObservation` join `ProposedCommand` beside the facet commands, and `MutableRecordTable` gains the five tables generation 5 appends. Nothing in the union promotes between record kinds: the two commands author proposals, and the write path refuses accepted-origin data with the shipped `promotion_not_supported` rather than gaining a member for it. `context_digest` is the module-level digest the validator calls and the operation re-derives; it is untouched by this leaf and lives at `:280`.

**Three more appended members and six more tables, added by `260915-KS-L21` for the truth-coverage census.** `CensusInventoryRowCommand`, `CensusClaimCommand` and `CensusDispositionCommand` join `ProposedCommand` at the tail of the union (`mcp/src/agents_remember/models/knowledge/candidate.py:640-642`), which is what makes the census's three record kinds writable through the one candidate batch operation rather than through a second write path — and `candidate_records.apply_census_command` dispatches them from the same family table the other groups use. `MutableRecordTable` gains the six tables those commands write (`:186-191`): the inventory row, the assessable claim, the migration disposition and the three relations they resolve through (`census_claim_evidence`, `census_claim_realization`, `census_disposition_link`), each addressed by its own primary key so an expectation, a duplicate check and a receipt can name one row. The comment above them records the reason they are here in the register the composition and supporting-record groups already established (`:181-185`). The three command models are imported **late**, in the same block that already imports the other command modules late (`:213-216`), because the union's own annotation reaches back into this module; the block's existing comment records that nothing else is imported late. **No census table carries a content address, a logical digest or a fingerprint column**, and a case in the census module asserts that from the declared columns rather than by convention.

### Conventions

- Literal vocabularies (`KnowledgeLane`, `MutableRecordTable`) are declared here and imported by the decider,
  never declared by the decider and re-exported downward.
- Every model inherits `KnowledgeModel`: frozen, `extra="forbid"`, with the shared identifier and digest
  patterns from `models/knowledge/base.py`. A payload naming an unknown field fails at construction.
- Command payloads are **provenance-free**: no command carries an `Authorship`. The admitted envelope is
  attached by the store, so a draft that arrived carrying its own actor, authorization or instant is re-stamped.
- `MutableRecordTable` names the twenty-five tables a command can write — the shipped thirteen plus the six facet, the six composition and the six census tables it has gained since. The `repository` row and the two
  predecessor-edge tables are written only as part of the aggregate that owns them, so an expectation about
  them would name a state no command could produce.

### Invariants And Boundaries

- **The union is the reach.** A command kind outside `ProposedCommand` cannot be expressed, and no field
  anywhere in this module can carry an approval, an acceptance or a SQL statement — the census's three
  commands joined it on exactly those terms, and the only thing they widen is which of this module's own
  declared tables a batch may write.
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
| The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. | `KnowledgeLane`; `CANDIDATE_LANES` | mcp/src/agents_remember/models/knowledge/candidate.py:107-107; mcp/src/agents_remember/models/knowledge/candidate.py:109-111; mcp/src/agents_remember/models/knowledge/candidate.py:117-119 |
| The portable content identity and the two exact candidate inputs. | `SnapshotIdentity`; `ExactCandidateInput` | mcp/src/agents_remember/models/knowledge/candidate.py:195-207; mcp/src/agents_remember/models/knowledge/candidate.py:210-218; mcp/src/agents_remember/models/knowledge/candidate.py:224-233 |
| The resolved context and its two consistency validators. | `KnowledgeContext` | mcp/src/agents_remember/models/knowledge/candidate.py:236-277 |
|  The module-level digest the validator calls and the operation re-derives. | "def context_digest(" | mcp/src/agents_remember/models/knowledge/candidate.py:280-280  |
| The receipt entry, including the two-state rule and the no-entry case. | `RecordIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:293-314 |
| The expectation model and its present-with-digest / absent-without-digest rule. | `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:317-339 |
| **The twenty-five-member discriminated union, with no promotion, approval or SQL member — the twenty-two it held before this leaf's three census command kinds joined it at the tail.** | `ProposedCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:611-643 |
| **The six census tables `MutableRecordTable` gained, and the three census command models imported late in the same block that already imported the other command modules late.** | `MutableRecordTable`; `CensusInventoryRowCommand`; `CensusClaimCommand`; `CensusDispositionCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:140-191; mcp/src/agents_remember/models/knowledge/candidate.py:181-185; mcp/src/agents_remember/models/knowledge/candidate.py:186-191; mcp/src/agents_remember/models/knowledge/candidate.py:213-216 |
| The portable content identity and the two exact candidate inputs. | `SnapshotIdentity`; `ExactCandidateInput` | mcp/src/agents_remember/models/knowledge/candidate.py:195-207; mcp/src/agents_remember/models/knowledge/candidate.py:210-218; mcp/src/agents_remember/models/knowledge/candidate.py:224-233 |
| The alias a batch's commands travel under, and the construct that makes the union's membership checkable in one place. | `ChangeCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:646-651 |
| The resolution shape that deliberately omits the dataset identity. | `CandidateResolution` | mcp/src/agents_remember/models/knowledge/candidate.py:656-673 |
| The batch and the receipt consistency validator the operation's results must satisfy. | `ChangeBatch`; `MutationResult` | mcp/src/agents_remember/models/knowledge/candidate.py:676-702; mcp/src/agents_remember/models/knowledge/candidate.py:704-747 |
| The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. | `KnowledgeLane`; `CANDIDATE_LANES` | mcp/src/agents_remember/models/knowledge/candidate.py:117-117; mcp/src/agents_remember/models/knowledge/candidate.py:119-119 |
| The portable content identity and the two exact candidate inputs. | `SnapshotIdentity`; `ExactCandidateInput` | mcp/src/agents_remember/models/knowledge/candidate.py:195-207; mcp/src/agents_remember/models/knowledge/candidate.py:224-233 |
| The resolved context and its two consistency validators. | `KnowledgeContext` | mcp/src/agents_remember/models/knowledge/candidate.py:236-277 |
|  The module-level digest the validator calls and the operation re-derives. | "def context_digest(" | mcp/src/agents_remember/models/knowledge/candidate.py:280-280  |
| The receipt entry, including the two-state rule and the no-entry case. | `RecordIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:293-314 |
| The expectation model and its present-with-digest / absent-without-digest rule. | `ExpectedRecord` | mcp/src/agents_remember/models/knowledge/candidate.py:317-339 |
| The twenty-five-member discriminated union with no promotion, approval or SQL member — the twenty-two it held at `KS-R17@v1`, plus this leaf's three census command kinds. | `ProposedCommand`; `ChangeCommand` | mcp/src/agents_remember/models/knowledge/candidate.py:611-643; mcp/src/agents_remember/models/knowledge/candidate.py:640-642; mcp/src/agents_remember/models/knowledge/candidate.py:646-651 |
| The resolution shape that deliberately omits the dataset identity. | `CandidateResolution` | mcp/src/agents_remember/models/knowledge/candidate.py:656-673 |
| The batch and the receipt consistency validator the operation's results must satisfy. | `ChangeBatch`; `MutationResult` | mcp/src/agents_remember/models/knowledge/candidate.py:676-702; mcp/src/agents_remember/models/knowledge/candidate.py:704-747 |
| The operation that consumes this vocabulary and the context it re-derives inside its transaction. | `change_candidate`; `_require_bound_context` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:148-183 |
| The composition seam that resolves a context from a live candidate and seals it. | `resolve_candidate_context`; `build_candidate_context`; `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:252-273; mcp/src/agents_remember/application/knowledge.py:275-301; mcp/src/agents_remember/application/knowledge.py:303-318 |
| The frozen base and the shared identifier/digest patterns every model here inherits. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The operation that consumes this vocabulary and the pre-lock lane check it applies first. | `change_candidate`; `require_writable_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:83-102 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): re-read this card's two vocabulary claims against the current source and recorded the census group substantively. The truth-coverage census appends **three command kinds** to `ProposedCommand` (`CensusInventoryRowCommand`, `CensusClaimCommand`, `CensusDispositionCommand` at `mcp/src/agents_remember/models/knowledge/candidate.py:640-642`, taking the union to **twenty-five** members) and **six tables** to `MutableRecordTable` (`:186-191` — the inventory row, the assessable claim, the migration disposition and the three relations they resolve through), with the three command models imported late in the block that already imported the other command modules late (`:213-216`). The card's counts were therefore corrected rather than carried: the `MutableRecordTable` sentence said thirteen tables, the invariants said a thirteenth command kind could not be expressed, and the union rows said twenty-two members. Every citation this card carries was checked against the source as it now stands — this leaf's additions moved the module's later constructs — and the stale ranges were re-cited to the constructs that actually hold their anchors (`context_digest` at `:280`, `RecordIdentity` at `:293-314`, `ExpectedRecord` at `:317-339`, the union at `:611-643`, `ChangeCommand` at `:646-651`, `CandidateResolution` at `:656-673`, `ChangeBatch`/`MutationResult` at `:676-702` and `:704-747`, and `SnapshotIdentity`/`ExactCandidateInput` at `:195-207` and `:224-233`). No claim was deleted and no superseded value was removed. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "def context_digest(" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `RecordIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:278-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `ExpectedRecord` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:302-324. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `CandidateResolution` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:638-655. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `SnapshotIdentity`; `ExactCandidateInput` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:185-194; mcp/src/agents_remember/models/knowledge/candidate.py:209-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `KnowledgeContext` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:221-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "def context_digest(" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `RecordIdentity` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:278-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `ExpectedRecord` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:302-324. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `CandidateResolution` repointed to mcp/src/agents_remember/models/knowledge/candidate.py:638-655. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "def context_digest(" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:249-249. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "def context_digest(" repointed to mcp/src/agents_remember/models/knowledge/candidate.py:249-249. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the two union claims this leaf widened and corrected the counts.** `ProposedCommand` now holds **twenty-two** variants — the eighteen it held at the previous leaf plus this leaf's four composition command kinds — and `ChangeCommand` is the alias it travels under; the card's eighteen-member wording was therefore false and is corrected, with the union row split into one row per anchor so each resolves in its own declaration. `MutableRecordTable` gained the six composition tables. The generated bullet that had rewritten the alias row's range mechanically was removed and replaced by this entry. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand** — `KnowledgeLane`, `CANDIDATE_LANES`, `def context_digest(`, `RecordIdentity`, `ExpectedRecord`, `CandidateResolution`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; their claims' ranges were **re-verified by hand against the current source in this pass** and repaired where this leaf's addition moved them, so a mechanically projected range is no longer the only evidence any of these claims carries. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the two appended union members, the five new mutable tables, and that no promotion member was added. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T02:55:00+00:00 — 260915-KS-L11 owning seat (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this claim against the source and re-cited it by hand, replacing a generated projection.** The claim said *twelve* members; the union now admits **eighteen** — the twelve shipped command models plus the six facet commands this leaf adds — at `models/knowledge/candidate.py:372-392`. The card's three other statements of the old count (the summary, the closed-union invariant and the `MutableRecordTable` sentence) were reconciled in the same read, so every count in this card now matches the declaration.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): **re-read this card against the source for the round-2 citation work and recorded a contradiction instead of softening the row.** The row above reading "The eighteen-member discriminated union with no promotion, approval or SQL member" is **no longer true**: `ProposedCommand` (`mcp/src/agents_remember/models/knowledge/candidate.py:372-392`) now admits **eighteen** members — the shipped twelve plus `AddFacet`, `AttachFacet`, `RemoveFacetAttachment`, `AuthorExplanation`, `AddExplanationRevision` and `DesignateExplanation`, which this leaf's authored-judgment vocabulary added; `ChangeCommand` still aliases it at `:394`. The row's citation and range follow the union as it now stands, and its *member count* was not rewritten, because a claim's meaning belongs to the owning seat rather than to the citation curator. The one-word correction owed is `eighteen-member` → `eighteen-member`. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp. No content impact: this entry records a review, not a content change.

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-change vocabulary. It records the closed twelve-command union with no promotion/approval/SQL member, the resolved-versus-authored and expected-versus-assumed splits, the deliberately absent dataset-identity field on `CandidateResolution`, the two-state receipt and its consistency validator, and the `baseline`/`task-candidate` lane distinction that exists so both can be refused by name. Verification metadata remains empty until closeout stamps the code commit.
