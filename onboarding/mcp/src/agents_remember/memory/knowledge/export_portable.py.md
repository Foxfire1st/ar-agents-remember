# mcp/src/agents_remember/memory/knowledge/export_portable.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/export_portable.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The portable artifact format `ar-knowledge-export/v1`, its one encoder, and the reader that refuses every
document which is not that encoder's own rendering.**

The envelope exists because a dataset identity is not a file. Two databases hold the same knowledge when
their canonical logical bodies are equal, whatever SQLite's page layout, journal state, mtime or path
happens to be — so the artifact carries exactly the body `logical.logical_digest` seals, plus the header
naming the format, the schema generation, the namespace and the digest. This module does **not** define a
second logical encoding: `logical.py` owns the body and the digest, and this module transports it.

## Code Commentary

### Logic

**The one guarantee, stated in the only form a consumer may rely on.** It is the module's own contract,
carried at `export_portable.py:54-59` and restated in the guarantee table below because L7, L8 and L9 are
written against it:

> **Every accepted artifact is the canonical rendering of the logical content it carries.** Two artifacts
> that both validate and declare the same `logicalDigest` are therefore the same bytes, and a dataset
> restored from an accepted artifact re-encodes to that artifact byte for byte.

**Acceptance is two checks, and both are needed for that sentence.**

1. **The whole-document gate** (`_non_canonical_refusal`, reached from `parse_export` after the shape and
   manifest checks): the text must be the **exact** rendering of the document it holds, at every level the
   format declares an order or a spelling for. The reader re-renders what it parsed through
   `_render_declared_document` and refuses unless `text == rendering`. Exhaustive by construction: a JSON
   escape spelling the same character, insignificant whitespace, a reordered envelope header and a
   reordered table mapping are each a different *document* of one dataset, and all are refused with
   `invalid_export` (`record_id == "<canonical document>"`) and a bounded statement of where the text
   diverges. **Nothing is repaired**: an artifact is refused rather than silently normalised, because
   normalising would accept a document nobody can reproduce from the bytes handed over.
2. **The header check** (`_validate_header`): every header *declaration* must be the one this build
   implements **and of the type this build writes**. `format`, `schema` and `schemaFingerprint` are
   compared by equality against this build's strings; `logicalDigest` and `repositoryId` are guarded by
   `isinstance`; `tables` must be a JSON object; and **`userVersion` is compared strictly by type**
   (`type(declared_version) is not int`), so `1.0` and `true` — which Python's `==` calls equal to `1` —
   are refused **by name** as unsupported generations rather than silently compared equal.

**The two checks cover different things, and a consumer comparing a hash must know which.**

| Inside `logicalDigest` | Outside it, pinned by the document form |
| --- | --- |
| the schema fingerprint and every canonical record — all ten tables' rows, in the digest encoding's sorted-key order | the envelope's field order; the declared manifest order of the tables; each row's declared column order; the canonical spelling of every value (compact separators, no insignificant whitespace, literal Unicode rather than escapes, sorted nested keys); **and the JSON type of every header value** |

The digest **excludes itself** by design: it cannot seal the field that carries it. The header's *types*
are not in the digest either — the reader is what pins them. Two artifacts can therefore share a digest
while differing on the last axes, and the reader refuses every such artifact, which is exactly why a byte
or content-hash comparison across **accepted** artifacts is sound. `logical_digest` remains the primary
contract and is what to compare when in doubt; `artifact_digest(text)` is the sha256 of the artifact's
exact UTF-8 bytes and is a function of the dataset.

**Two JSON encodings, deliberately, and confusing them breaks the format.**

- `CANONICAL_JSON_KWARGS` (sorted keys, imported from `kernel.canonical_json`) is what **seals the
  digest**; it must be insensitive to how a value was spelled.
- `DOCUMENT_JSON_KWARGS` is `CANONICAL_JSON_KWARGS` with `sort_keys=False`, and it is what **renders the
  artifact**: the declared column order is part of the format and the sorted form would erase it. Sorting
  is stated as the *only* departure, so separators, literal Unicode and the no-NaN policy stay the
  kernel's and the two encodings cannot drift apart silently.

**The reading order is the contract** (`parse_export`'s docstring lists it): (1) duplicate JSON keys and
unparsable text — `_Document` is a `dict` subclass that keeps its own pair list and raises on a repeated
key, because JSON's last-one-wins read would silently pick a value; (2) unknown or missing envelope fields
(`_shape_refusal`, a set comparison, not a tolerant read); (3) the table manifest (`_manifest_refusal`,
run **before** the gate so an undeclared table is refused for being undeclared rather than for the
spelling difference it causes); (4) the whole-document gate; (5) the header check.

**What `validate_export` adds on top of a parsed document:** declared column order per row
(`_validate_table_rows` compares `row.ordered_items()` against `schema.CANONICAL_COLUMNS`), declared
column types (`_typed_row` — a typed JSON column accepts a string/list/dict, a TEXT column only a string),
primary-key uniqueness, the repository binding (exactly one `repository` row, and it must name the
namespace the header declares), and the recomputed digest against the declared one. `ValidatedExport`
carries **both** the report and the decoded rows, because a caller that validated one reading and loaded
another would import rows nobody checked.

**Two callables a consumer must not misuse.**

- `canonical_document(text) -> str | None` is the canonical rendering of an artifact's text, or `None`
  when the text is not a renderable artifact of this format at all (not a JSON object, or carrying a
  number the canonical encoding has no spelling for: `NaN`, an infinity, a JSON number that overflows to
  one). `text == canonical_document(text)` is the property every accepted artifact satisfies, and the
  equality is **necessary and not sufficient** for acceptance: the three build-constant declarations are
  compared by value *after* the gate, so a document declaring another schema renders equal to itself and
  is still refused. **It is not an acceptance oracle** — that is `validate_knowledge_artifact`.
- `encode_export(envelope) -> str` is the one encoder and the re-encoding path for a consumer holding an
  envelope. It renders header scalars from **the value this build validates** (`_validated_header`), so an
  envelope declaring this generation as `1.0` or `true` is written as the integer this build writes and
  the published encoder cannot emit an artifact its own reader refuses. A declaration that is *not* this
  generation (`2`, `"1"`) is written exactly as given, so it is still refused by name.

### Conventions

- Every refusal on this boundary is a returned `KnowledgeRefusal`, never a raised exception — including
  for a value the canonical encoding cannot spell, which would otherwise escape as a raw `ValueError` with
  no code for a caller to branch on.
- Row-level refusals use `_row_refusal` (a plain `KnowledgeRefusal`); document-level checks wrap theirs in
  `ValidatedExport` through `_invalid`. Keeping the two factories apart is what makes a row failure unable
  to be mistaken for a validated document.
- `EXPORT_FORMAT` and `ENVELOPE_KEYS` are module constants; the declared key order of `ENVELOPE_KEYS` is
  the order the document renders in.
- `_short` bounds every value a refusal echoes; `_canonical_difference` reports where the text diverges
  rather than printing two documents.

### Invariants And Boundaries

- **The canonical form is the only accepted form, and the rule is part of what the format means.** A
  foreign producer must write the canonical form — including the header's types. A later leaf that needs
  to accept other spellings needs a **new format member with its own reader**, never a tolerant read of
  `ar-knowledge-export/v1`. An unrecognised `format` is refused rather than interpreted through the
  closest reader available.
- **All ten canonical collections are always present, in declared manifest order, including empty ones.**
  "Examined and had nothing to carry" and "never mentioned" are different facts, and only the first is a
  complete export.
- **The stored spelling of a JSON value is not knowledge.** A typed JSON column crosses as a decoded JSON
  value with its nested keys sorted (`_ordered_rows` / `_canonical_json_value`); every other column
  crosses as exact stored text and keeps its Unicode and line endings.
- **The digest excludes itself, and nothing else is excluded by accident.** SQLite page order, header
  counters, mtimes, filesystem paths, Git commits, ledger rows and rendered views are all outside the
  artifact.
- **`_out_of_canonical_order` is defence in depth and unreachable from the public reader.** The
  whole-document gate refuses an out-of-order nested key one step earlier, so no artifact reaches
  `_typed_row` with one. It is kept because it states the rule where the value is typed, and the evidence
  records the ordering rather than assuming it; no case claims it as the reason an artifact was refused.
- **No filesystem side effect.** This module reads and renders text; it never opens, writes or deletes a
  database. A caller that wants the artifact on disk writes `ExportResult.artifact` through the
  repository's own atomic write.
- **Boundary.** This module owns the format, the encoder and the reader. It does not decide whether an
  artifact may be installed *here* (the destination admission is `export_import.py`'s), does not take a
  lock, and does not grant authority: a row whose `state_at_origin` says `accepted` crosses as that stored
  value and is nothing more.

### Todos

None recorded for this slice. Two carried facts belong to a consumer rather than to a defect here: the
`_out_of_canonical_order` branch above, and the header's namespace-binding check at
`export_portable.py:911` (`bound != document.repository_id`), which is reachable and verdict-changing but
has no killing node in this leaf's population — reported by the scoped final verification as an
observation for **L9**, not as a claim of this leaf.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The acceptance rule, the guarantee and the digest-coverage statement, in the form a consumer may rely on.** | "Every accepted artifact is the canonical rendering of the logical content it carries"; "Inside `logicalDigest`" | mcp/src/agents_remember/memory/knowledge/export_portable.py:39-75 |
| The declared format member and the envelope key order the document renders in. | `EXPORT_FORMAT`; `ENVELOPE_KEYS` | mcp/src/agents_remember/memory/knowledge/export_portable.py:116-116; mcp/src/agents_remember/memory/knowledge/export_portable.py:120-128 |
| The boundary an export carries for its reader, returned on the result rather than embedded in the artifact. | `PORTABLE_NOTES` | mcp/src/agents_remember/memory/knowledge/export_portable.py:133-140 |
| The document encoding: the kernel's canonical kwargs with key sorting deliberately omitted, so the declared column order survives. | `DOCUMENT_JSON_KWARGS` | mcp/src/agents_remember/memory/knowledge/export_portable.py:147-150 |
| The envelope builder: declared column order, canonical nested keys and declared manifest order. | `export_envelope`; `_ordered_rows`; `_canonical_json_value` | mcp/src/agents_remember/memory/knowledge/export_portable.py:199-239; mcp/src/agents_remember/memory/knowledge/export_portable.py:242-264; mcp/src/agents_remember/memory/knowledge/export_portable.py:267-274 |
| The one encoder, and the header rule that stops it emitting a form its own reader refuses. | `encode_export`; `_validated_header`; `_render_document` | mcp/src/agents_remember/memory/knowledge/export_portable.py:277-302; mcp/src/agents_remember/memory/knowledge/export_portable.py:305-331; mcp/src/agents_remember/memory/knowledge/export_portable.py:346-349 |
| `canonical_document`, the renderer that answers "is this the canonical form?", with the necessary-but-not-sufficient caveat. | `canonical_document` | mcp/src/agents_remember/memory/knowledge/export_portable.py:367-399 |
| The gate's rendering, which keeps each header scalar's declared JSON type so the header check is the site that refuses a respelled generation by name. | `_render_declared_document`; `_plain_envelope`; `_plain_tables`; `_canonical_rows` | mcp/src/agents_remember/memory/knowledge/export_portable.py:402-416; mcp/src/agents_remember/memory/knowledge/export_portable.py:352-364; mcp/src/agents_remember/memory/knowledge/export_portable.py:419-448; mcp/src/agents_remember/memory/knowledge/export_portable.py:451-472 |
| The reading order: duplicate keys and unparsable text, envelope shape, manifest, gate, header. | `parse_export`; `_Document` | mcp/src/agents_remember/memory/knowledge/export_portable.py:493-546; mcp/src/agents_remember/memory/knowledge/export_portable.py:1029-1062 |
| The shape refusal (unknown and missing envelope fields) and the manifest refusal that runs before the gate. | `_shape_refusal`; `_manifest_refusal` | mcp/src/agents_remember/memory/knowledge/export_portable.py:549-573; mcp/src/agents_remember/memory/knowledge/export_portable.py:576-610 |
| **The whole-document gate, its refusal-identity and the bounded statement of how the text differs.** | `_non_canonical_refusal`; `_canonical_difference` | mcp/src/agents_remember/memory/knowledge/export_portable.py:613-645; mcp/src/agents_remember/memory/knowledge/export_portable.py:648-667 |
| The dataset checks: declared column order, declared types, canonical nested order, primary-key uniqueness, namespace binding and the recomputed seal. | `validate_export`; `_validate_table_rows`; `_typed_row`; `_validate_dataset` | mcp/src/agents_remember/memory/knowledge/export_portable.py:670-715; mcp/src/agents_remember/memory/knowledge/export_portable.py:842-885; mcp/src/agents_remember/memory/knowledge/export_portable.py:888-928; mcp/src/agents_remember/memory/knowledge/export_portable.py:967-1026 |
| **The type-strict generation comparison that is the second half of the guarantee, and the entry's public symbol list.** | `_validate_header`; `__all__` | mcp/src/agents_remember/memory/knowledge/export_portable.py:758-815; mcp/src/agents_remember/memory/knowledge/export_portable.py:1144-1159 |
| The reachable, verdict-changing namespace guard with no killing node (an observation for L9). | `bound` | mcp/src/agents_remember/memory/knowledge/export_portable.py:984-1001 |
| The one canonical logical encoder this module transports rather than re-implements. | `logical_body_from_tables`; `logical_digest_of_tables` | mcp/src/agents_remember/memory/knowledge/logical.py:95-129; mcp/src/agents_remember/memory/knowledge/logical.py:132-135 |
| The kernel canonical encoding the digest kwargs come from, and its no-NaN policy. | `CANONICAL_JSON_KWARGS`; `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:20-32; mcp/src/agents_remember/kernel/canonical_json.py:34-38 |
| The table and column manifest the declared orders are read from. | `CANONICAL_TABLES`; `CANONICAL_COLUMNS`; `SCHEMA_USER_VERSION` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112; mcp/src/agents_remember/memory/knowledge/schema.py:27-27 |
| The typed JSON column set a value is canonicalised against. | `JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:154-162 |
| **The node that asserts the canonical form is the only form the reader accepts, including all seven header types.** | "test_the_canonical_form_of_the_whole_document_is_the_only_form_the_reader_accepts" | mcp/tests/test_knowledge_portable_boundaries.py:133-258 |
| The node that asserts an unreadable artifact is refused with a typed code. | "test_an_artifact_that_cannot_be_read_as_text_is_refused_with_a_typed_code" | mcp/tests/test_knowledge_portable_boundaries.py:686-736 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The artifact crosses **machines**, not
repositories: nothing here reads a second checkout, resolves a source object or consults Git.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): created this one-to-one card for the portable artifact format. It records the guarantee in the only form a consumer may rely on — **every accepted artifact is the canonical rendering of the logical content it carries**, so two artifacts that both validate and declare the same `logicalDigest` are the same bytes — and states that acceptance is **two** checks: the whole-document gate (the text must be the exact rendering of the document it holds, at every level the format declares an order or a spelling for) and the header check (every declaration must be the one this build implements **and of the type this build writes**, with `userVersion` compared type-strictly so `1.0` and `true` are refused by name as unsupported generations). It records what the digest covers and what the document form covers instead — the envelope's field order, the declared manifest order, each row's declared column order, every value's canonical spelling, and the JSON type of every header value — the two deliberately different JSON encodings, the reading order that makes each refusal the first applicable one, and the two misusable callables (`canonical_document` as necessary-but-not-sufficient, `encode_export` as the re-encoding path from the validated value). The `_out_of_canonical_order` branch is recorded as unreachable defence in depth, and the namespace-binding guard at `:911` is recorded as a reachable guard with no killing node, reported for L9. Verification metadata remains empty until closeout stamps the code commit.
