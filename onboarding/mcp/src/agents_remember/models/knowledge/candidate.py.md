# mcp/src/agents_remember/models/knowledge/candidate.py

## Governing Overview


[models route overview](../overview.md)

## Purpose


Defines portable snapshot and exact candidate-input identities, and a sealed resolved knowledge context.

## Code Commentary


`SnapshotIdentity` is repository_id, schema_version and logical_digest. `ExactCandidateInput` carries the exact tree plus any recorded commit/dirty facts; it does not make a tree an alias for HEAD. `KnowledgeContext` validates its digest and the namespace of the carried snapshot. `context_digest` derives the seal from the other fields. The canonical ChangeBatch, expected-record vocabulary, command union and mutation receipt were removed. A carried opaque reference is a resolved value, not proof that its Git object or task exists.

**`SnapshotIdentity`** is `repository_id` + `schema_version` + `logical_digest`; it is the portable content
  identity the whole substrate compares on, and its digest is produced by `memory/knowledge/logical.py`.

**Resolved context versus proposed content.** `KnowledgeContext` carries the identity the admitted
  runtime *resolved* — namespace, lane, both exact candidate inputs, the logical knowledge snapshot and the
  opaque `snapshot_ref`/`candidate_ref`/`task_ref` — plus `context_digest`, which `context_digest()` computes
  over every field except itself. `_require_sealed_context` refuses a context whose digest does not seal it,
  and `_require_one_namespace` refuses one whose snapshot belongs to another repository.

**The carried references prove nothing about the world.** `snapshot_ref`, `candidate_ref` and `task_ref` are
  opaque strings recorded as resolved facts; nothing here re-verifies that a Git object or a task contract
  exists, and a consumer must not read them as that proof.

Every model inherits `KnowledgeModel`: frozen, `extra="forbid"`, with the shared identifier and digest
  patterns from `models/knowledge/base.py`. A payload naming an unknown field fails at construction.

## Evidence


### Repo-Internal References

- `SnapshotIdentity` owns the current boundary described above. [26]
- `ExactCandidateInput` owns the current boundary described above. [27]
- `KnowledgeContext` owns the current boundary described above. [28]
- `context_digest` owns the current boundary described above. [29]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

- The lane vocabulary, including the read-only `baseline` member that exists so it can be refused by name. [30]
- The portable content identity and the two exact candidate inputs. [31]
- The resolved context and its two consistency validators. [32]
- The module-level digest the validator calls and the operation re-derives. [33]
- The frozen base and the shared identifier/digest patterns every model here inherits. [34]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
