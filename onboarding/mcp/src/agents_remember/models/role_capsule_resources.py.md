# mcp/src/agents_remember/models/role_capsule_resources.py

## Governing Overview

[models overview](overview.md)

## Purpose

The **wire contracts** for the capsule operation and the skill resource surface. Both top-level
responses are strict: this server owns every field in them. The capsule response carries the compiled
content plus its provenance — each instruction block's source path and revision, each skill reference's
origin and revision, and the requested tool identities — so a consumer can pin exactly what it
received without re-deriving it. A refusal is the same envelope with `ok` false, a typed
`refusalStatus`, and whatever was still true about the seat it addressed.

The nested payloads are plain strict values, not envelopes: they are constructed once by the
application boundary and are never independently tokenized or finalized.

## Code Commentary

### Logic

Three bridge-name constants (`ROLE_CAPSULE_COMPILE_OPERATION`, `SKILL_CATALOG_LIST_OPERATION`,
`SKILL_CATALOG_READ_OPERATION`) and one trust constant
(`SERVER_SUPPLIED_CONTENT_TRUST = "server-supplied-data"`).

`RoleCapsuleResponse` is the largest contract. Its identity and provenance fields
(`role`, `seatAltitude`, `operationName`, `taskReference`, `taskDocumentDigest`, `repositoryId`,
`workBranch`, `semanticDigest`, `compositionOrder`, `instructionIdentities`, `instructions`,
`skillReferences`, `requestedTools`, `grantedTools`, `taskContext`, `sources`, `conflictKinds`) are all
optional or defaulted, because a refusal legitimately carries only the subset that was established
before it refused. `explanation` is required: every shape has one operator-facing line.

The nested payloads are one per fact family: an instruction block (with `compositionRoot`,
`sourcePath`, `revision`, `contentDigest`, `authorities` and `content`), a skill reference
(`skillIdentity`, `origin`, `uri`, `revision`), a requested tool (`toolId`, `authority`), the task
context (origin, projection revision, digest, Markdown), and a source record (`selected`,
`collapsedDuplicate`, `selectionReason`, `supersededBy`, `supersededKind`).

`SkillCatalogListResponse` carries `origin`, `sourceRoot`, `indexUri`, `skills[]` and `unreadable[]`.
`SkillCatalogEntryPayload` lists `files` as **relative paths**, not content. `SkillCatalogReadResponse`
carries the selected file's `revision` and its skill's `skillRevision` as two separate fields, plus
`contentTrust` defaulting to the server-supplied constant.

### Conventions

Strict response models extend `StrictResponseModel`/`ToolResponse`, so an undeclared field fails its
own model — the reply is never silently widened. Field names are camelCase on the wire while the
`operation` literal is pinned per model, so a payload that reports the wrong operation name fails
validation rather than misleading a consumer.

### Invariants And Boundaries

- **`ok` and `explanation` exist in every shape.** A refusal is not an error type crossing the wire;
  it is the same envelope with `ok` false and a typed status.
- **`grantedTools` is the admitted policy snapshot, `requestedTools` is what the capsule asked for.**
  The two are deliberately separate fields: the compiler narrows requests against the granted set and
  refuses a request outside it, and keeping both on the wire is what makes that narrowing auditable.
  `M2` of the leaf's mutation probe targets this boundary.
- **`contentTrust` is a constant with a default, not a settable input.** No code path derives a trust
  level from content.
- **`declaredAllowedTools` is observed frontmatter, never a permission.** It is present so a reader can
  refuse or gate a skill; no field exists through which it becomes an activation.
- **`revision` and `skillRevision` are distinct.** On a supporting file they differ, and collapsing
  them would make a supporting file's provenance claim something it cannot support.
- The `operation` literal on each response is the name `tool_registry.py` indexes by, so a response
  built with the wrong literal fails at the registry rather than reaching a caller mislabeled.

### Todos

None recorded.

## Evidence

### Docs References

The extension's security posture is the source of the trust field's fixed value and of the
recorded-not-applied tool declaration.

- A declared tool set is an observation, never a permission channel. [1]
- The per-read provenance block whose trust statement is a fixed string. [2]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

### Repo-Internal References

- The capsule envelope: required explanation, optional identity/provenance, and the refusal fields. [3]
- The nested capsule payloads, one per fact family. [4]
- The listing carries relative file names and no content; the read carries two distinct revisions. [5]
- The constant trust statement every served file declares. [6]
- The registry rows that make these three names returnable. [7]
- The builder that fills these contracts from owner-produced values only. [8]
- The requested-versus-granted boundary the compiler narrows against: the policy type is declared in the `models` leaf, and the operation snapshots the published roster into it. [9]
- The case that executes the no-grant guarantee on a served skill's declared tools. [10]

### Cross-Repo References

No meaningful cross-repository reference applies.
