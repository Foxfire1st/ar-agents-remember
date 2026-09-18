# mcp/src/agents_remember/memory/knowledge/effect_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/effect_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T10:25+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Row codecs for the authored-effect record group. The group stores **nothing of its own beyond one
succession edge**: an effect claim, a preservation claim, an unresolved question and a change set *are*
envelope records, so every conversion in both directions already has an owner — and it is not this
module. What this module owns is the statements that name this group's four kinds and its one edge
table.

## Code Commentary

### Logic

**Three conversions, and who owns each.** The generic column tuple
`(repository_id, revision_id, record_id, record_schema, payload, predecessor_revision_id,
content_digest, provenance)` is **reused** from `facet_records`, which is the envelope's row codec for
the authored record groups; a second implementation of that tuple, or of the digest the seal is
verified against, would be a second place the same identity could be computed two ways. The payload is
decoded through **the frozen shape the envelope registry resolves for its kind** — `PAYLOAD_MODELS.get((kind,
record_schema))` — not through a shape restated here, so a stored payload is read back as the model the
write path validated it against and a record of one kind can never be decoded as another. The stored
`content_digest` is **recomputed on the way out**: a payload rewritten behind its identity would
otherwise be served as the revision that identity names, and the whole point of a sealed revision is
that it cannot be.

**`EFFECT_RECORD_KINDS` is derived, not restated.**
`(*MEMBER_KINDS, SEMANTIC_CHANGE_SET_KIND)` reads the three member kinds from the vocabulary and the
change-set kind from the module that owns its payload, so a kind cannot join the registry without also
joining the group's own readers and its after-batch seal pass. `EffectPayload` is the corresponding
union alias, so a fifth kind added to the vocabulary is a **type error here** rather than a silent
omission.

**`EFFECT_REVISIONS_OF_KIND` is the join that lets the group answer "every stored effect claim"
without reading another group's rows.** The kind lives on `knowledge_record` and the payload lives on
`record_revision`, so the reader joins through the envelope on `(repository_id, record_id)` and filters
on `envelope.kind`. The reader lives here, beside the decoder, because two callers need the same rows
for different reasons — the write path's duplicate scan and the after-batch seal pass — and a
per-caller query would let the two disagree about which rows belong to a kind.

**Two failure modes are damaged-store reports rather than refusals.** A revision whose `record_schema`
is not the shape its kind declares was written outside this record group, and is reported as such
rather than decoded anyway; a stored payload that no longer validates against its declared shape is
likewise a store damaged outside the operation, reported as one rather than raised as a bare
`ValidationError`.

### Conventions

The decoder takes the `kind` as a **caller-supplied argument**, because a `record_revision` row does
not carry one — the kind lives on the envelope. Each stored row is decoded into a frozen dataclass
(`StoredEffectRecord`, `StoredEffectRevision`) rather than handed back as a positional tuple, so a
reader works with named fields. `StoredEffectRevision.payload` is the **validated frozen model**, not
the mapping it was decoded from, so a stored row carrying a field the vocabulary does not declare could
not have been decoded into one at all.

`EffectRecordDraft` exists so one envelope is a value rather than seven positional arguments.
`effect_record_row_digest` hashes the same fields in the shipped shape the facet codec uses for the
same table, so the two record groups report one table's row digest the same way and a caller can carry
a receipt entry straight into an expectation.

### Invariants And Boundaries

- **A record group never reads another kind's rows.** The statements here name this group's four kinds
  and its one edge table, and nothing else.
- **The seal is verified on every read, and a mismatch is fatal.** A revision that does not match its
  stored `content_digest` is reported as damaged with the stored and recomputed digests as facts and an
  instruction to recover from an intact snapshot; nothing here repairs, re-pins or rewrites a row.
- **`kind` and `record_schema` are the caller's declaration, never the payload's.** A caller therefore
  cannot store a pair the envelope's registry would refuse.
- **`authority_home` is the bound namespace's own**, not a field a caller authors, and the lifecycle
  column is written from the command's `state_at_origin`, which the batch refuses to store as anything
  but `proposed`.
- **One edge insert, one edges read, one predecessors read.** `CHANGE_SET_PREDECESSOR_INSERT`,
  `CHANGE_SET_PREDECESSOR_EDGES` (ordered, for the acyclic walk) and `CHANGE_SET_PREDECESSORS_OF` are
  the group's whole ownership of the generation-8 table.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The group's four kinds, derived from the vocabulary and the change-set kind so a kind cannot join the registry without joining the readers. | `EFFECT_RECORD_KINDS` | mcp/src/agents_remember/memory/knowledge/effect_records.py:61-61 |
| The union of the four frozen payload shapes, which makes a fifth kind a type error rather than a silent omission. | `EffectPayload` | mcp/src/agents_remember/memory/knowledge/effect_records.py:66-71 |
| The three owned statements: the envelope insert, the sealed revision insert, and the one succession-edge insert. | `EFFECT_RECORD_INSERT`; `EFFECT_REVISION_INSERT`; `CHANGE_SET_PREDECESSOR_INSERT` | mcp/src/agents_remember/memory/knowledge/effect_records.py:73-76; mcp/src/agents_remember/memory/knowledge/effect_records.py:78-81; mcp/src/agents_remember/memory/knowledge/effect_records.py:83-86 |
| The group's three scoped readers: one record by identity, every record of a kind, and every revision of one record. | `EFFECT_RECORD_BY_ID`; `EFFECT_RECORDS_OF_KIND`; `EFFECT_REVISIONS_OF_RECORD` | mcp/src/agents_remember/memory/knowledge/effect_records.py:88-91; mcp/src/agents_remember/memory/knowledge/effect_records.py:93-96; mcp/src/agents_remember/memory/knowledge/effect_records.py:98-101 |
| The join through the envelope that answers "every stored revision of one kind" without reading another group's rows. | `EFFECT_REVISIONS_OF_KIND` | mcp/src/agents_remember/memory/knowledge/effect_records.py:106-113 |
| The ordered edges read the shared acyclic walk runs over, and the per-successor predecessors read the views use. | `CHANGE_SET_PREDECESSOR_EDGES`; `CHANGE_SET_PREDECESSORS_OF` | mcp/src/agents_remember/memory/knowledge/effect_records.py:115-118; mcp/src/agents_remember/memory/knowledge/effect_records.py:120-123 |
| The value one envelope is carried in, so a write is not seven positional arguments. | `EffectRecordDraft` | mcp/src/agents_remember/memory/knowledge/effect_records.py:127-135 |
| The decoded revision type whose payload is the validated frozen model rather than the mapping it came from. | `StoredEffectRevision` | mcp/src/agents_remember/memory/knowledge/effect_records.py:152-167 |
| The decoder that verifies the seal and the declared kind, and the damaged-store report a mismatch produces. | `decode_effect_revision_row` | mcp/src/agents_remember/memory/knowledge/effect_records.py:263-310 |
| The reader shared by the duplicate scan and the after-batch seal pass, whose one query keeps the two from disagreeing about a kind's rows. | `stored_revisions_of_kind` | mcp/src/agents_remember/memory/knowledge/effect_records.py:333-346 |
| The envelope registry the payloads are decoded through rather than restated from. | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:118-157 |
| The generic revision column tuple and digest this module reuses instead of re-implementing. | `record_revision_row`; `record_revision_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:193-206; mcp/src/agents_remember/memory/knowledge/facet_records.py:209-224 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A row codec converts one namespace's own
stored columns, and the identities it carries are store-local.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:25+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the authored-effect record group's row codecs. It records the three owned conversions and who owns each, the derived kind tuple, the join that scopes a kind without reading another group's rows, the seal recomputed on the way out, and the damaged-store reporting that replaces silent decoding. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
