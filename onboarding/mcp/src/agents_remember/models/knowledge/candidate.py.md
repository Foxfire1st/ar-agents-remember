# mcp/src/agents_remember/models/knowledge/candidate.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The served knowledge vocabulary as an explicit re-export list, which this module's names joined. [1]
- The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. [2]
- The portable content identity and the two exact candidate inputs. [3]
- The resolved context and its two consistency validators. [4]
- The module-level digest the validator calls and the operation re-derives. [5]
- The receipt entry, including the two-state rule and the no-entry case. [6]
- The expectation model and its present-with-digest / absent-without-digest rule. [7]
- **The twenty-five-member discriminated union, with no promotion, approval or SQL member — the twenty-two it held before this leaf's three census command kinds joined it at the tail.** [8]
- **The six census tables `MutableRecordTable` gained, and the three census command models imported late in the same block that already imported the other command modules late.** [9]
- The portable content identity and the two exact candidate inputs. [10]
- The alias a batch's commands travel under, and the construct that makes the union's membership checkable in one place. [11]
- The resolution shape that deliberately omits the dataset identity. [12]
- The batch and the receipt consistency validator the operation's results must satisfy. [13]
- The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. [14]
- The portable content identity and the two exact candidate inputs. [15]
- The resolved context and its two consistency validators. [16]
- The module-level digest the validator calls and the operation re-derives. [17]
- The receipt entry, including the two-state rule and the no-entry case. [18]
- The expectation model and its present-with-digest / absent-without-digest rule. [19]
- The twenty-five-member discriminated union with no promotion, approval or SQL member — the twenty-two it held at `KS-R17@v1`, plus this leaf's three census command kinds. [20]
- The resolution shape that deliberately omits the dataset identity. [21]
- The batch and the receipt consistency validator the operation's results must satisfy. [22]
- The operation that consumes this vocabulary and the context it re-derives inside its transaction. [23]
- The composition seam that resolves a context from a live candidate and seals it. [24]
- The frozen base and the shared identifier/digest patterns every model here inherits. [25]
- The operation that consumes this vocabulary and the pre-lock lane check it applies first. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
