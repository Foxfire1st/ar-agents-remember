# mcp/src/agents_remember/models/role_capsule_resources.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/role_capsule_resources.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `overview.md` |

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

## Docs References

The extension's security posture is the source of the trust field's fixed value and of the
recorded-not-applied tool declaration.

| Finding | Anchor | Source |
| --- | --- | --- |
| A declared tool set is an observation, never a permission channel. | `declared_allowed_tools` | mcp/src/agents_remember/models/skill_resources.py:270-285 |
| The per-read provenance block whose trust statement is a fixed string. | `skill_meta` | mcp/src/agents_remember/models/skill_resources.py:253-267 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The capsule envelope: required explanation, optional identity/provenance, and the refusal fields. | `RoleCapsuleResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:86-115 |
| The nested capsule payloads, one per fact family. | `CapsuleInstructionBlockPayload`; `CapsuleSkillReferencePayload`; `CapsuleRequestedToolPayload`; `CapsuleTaskContextPayload`; `CapsuleSourceRecordPayload` | mcp/src/agents_remember/models/role_capsule_resources.py:35-44; mcp/src/agents_remember/models/role_capsule_resources.py:47-53; mcp/src/agents_remember/models/role_capsule_resources.py:56-60; mcp/src/agents_remember/models/role_capsule_resources.py:63-69; mcp/src/agents_remember/models/role_capsule_resources.py:72-83 |
| The listing carries relative file names and no content; the read carries two distinct revisions. | `SkillCatalogEntryPayload`; `SkillCatalogListResponse`; `SkillCatalogReadResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:118-127; mcp/src/agents_remember/models/role_capsule_resources.py:137-150; mcp/src/agents_remember/models/role_capsule_resources.py:153-167 |
| The constant trust statement every served file declares. | `SERVER_SUPPLIED_CONTENT_TRUST` | mcp/src/agents_remember/models/role_capsule_resources.py:32-32 |
| The registry rows that make these three names returnable. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:155-239 |
| The builder that fills these contracts from owner-produced values only. | `role_capsule_response`; `_fill_manifest` | mcp/src/agents_remember/application/skill_resources/responses.py:34-55; mcp/src/agents_remember/application/skill_resources/responses.py:58-119 |
| The requested-versus-granted boundary the compiler narrows against: the policy type is declared in the `models` leaf, and the operation snapshots the published roster into it. | `CapsuleToolPolicy`; `admitted_tool_policy` | mcp/src/agents_remember/models/role_capsules/types.py:182-182; mcp/src/agents_remember/application/skill_resources/capsule.py:394-409 |
| The case that executes the no-grant guarantee on a served skill's declared tools. | `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names` | mcp/tests/test_capsule_serving.py:811-845 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-16T10:41:01+00:00: Generated citation repair: `skill_meta` repointed to mcp/src/agents_remember/models/skill_resources.py:253-267. No content impact: mechanical anchor-range projection bound to citation source snapshot d000fd9192b3f076fd4f39e5e775a368dd70d71b172c679cb9d28176bdc33096; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T10:41:01+00:00: Generated citation repair: `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names` repointed to mcp/tests/test_capsule_serving.py:811-845. No content impact: mechanical anchor-range projection bound to citation source snapshot d000fd9192b3f076fd4f39e5e775a368dd70d71b172c679cb9d28176bdc33096; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: citation work on this document,
  scoped to it alone (`citation_fix --document mcp/src/agents_remember/models/role_capsule_resources.py.md`).
  Two generated repairs landed: `skill_meta` repointed to `models/skill_resources.py:253-267` and
  `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names` to
  `mcp/tests/test_capsule_serving.py:811-845` (the repairs moved it). The tool then **declined two rows
  as `anchor_ambiguous` rather than guessing**, and I resolved both by reading the candidates:
  `declared_allowed_tools` repointed from `219-234` to the **function** at `270-285` (the other candidate
  is the unrelated `SkillResourceEntry` field at `:96`), and the policy row's `CapsuleToolPolicy` anchor
  corrected to its actual declaration in `models/role_capsules/types.py:182` — it was never declared in
  `capsule.py`, where the row had cited it. Verification metadata remains closeout-owned; no acceptance
  claim is made.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the capsule and skill wire
  contracts. Recorded the shared refusal/success envelope, the deliberate
  requestedTools-versus-grantedTools split that makes the compiler's narrowing auditable, the constant
  trust field, the observed-never-applied declared tool list, and the two distinct revision fields on a
  served file. Verification metadata remains closeout-owned; no acceptance claim is made.
