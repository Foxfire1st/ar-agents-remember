# mcp/src/agents_remember/memory/knowledge/export_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/export_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T17:45+02:00 |
| lastVerifiedCommitHash | `4eb2b1992f6183fba06e9f31aa664d9a93094c26`|
| lastVerifiedCommitDate | 2026-09-16T18:28:38+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The refusal vocabulary of the portable export/import boundary**: one factory per observable failure
point, in one module so the codes, the offending record and the advertised next action stay together
instead of being spelled out at each call site.

The artifact is an **external input** — it arrives as text, it was written by something that may not be
this code, and nothing about it is trusted because it parses. The factories separate the three questions
that creates: is this a well-formed artifact of a supported generation, is what it carries a complete
logical dataset, and may it be installed *here*.

The shared `refusal` factory and the exception types stay in `refusals.py`; this module only names the
failures a portable artifact can produce.

## Code Commentary

### Logic

Five factories, and the code each one produces is the caller's branch:

- `invalid_export_refusal` — `invalid_export`. **One code covers the malformed document and the incomplete
  dataset on purpose**: the caller's decision is the same for both (the artifact cannot be imported) and
  `detail` names which of the two it is. Splitting it would invite a caller to treat "parsed" as
  "trustworthy", which is the confusion this boundary exists to prevent. Its next action states that
  nothing was published, the destination still holds exactly what it held before, and no missing
  information was invented to complete the dataset.
- `non_canonical_export_refusal` — `invalid_export` with `record_id == "<canonical document>"`. It has its
  own factory because the **fact** is different and is the one this format's guarantee rests on: the
  document parses and the dataset it declares is the dataset inside it, but it is spelled some other way
  than the one form the format accepts. Nothing is repaired here — an artifact is refused, never quietly
  normalised — and the next action tells the caller to re-encode with this package's encoder.
- `unsupported_schema_refusal` — `unsupported_schema`. A version string is not evidence that the tables
  match it, so the refusal names the declared generation and the supported one. A future generation needs a
  reader that implements it rather than a tolerant read of this one: the operation never migrates and never
  drops a collection it does not understand.
- `destination_occupied_refusal` — `destination_occupied`, and `destination_absent_refusal` —
  `destination_stale`. The two mirrors of one rule: an import never patches a live destination in place.
  When the request admits no expectation there is nothing to compare against, so an occupied destination
  is refused and the caller must state the identity it believes is there; and when the caller *did* name an
  identity it expected to replace, an absent destination is a refusal rather than a fresh install, because
  creating one would answer a different question than the one asked.
- `import_validation_failed_refusal` — `relationship_constraint`. This is the refusal of the **staged**
  database: the artifact's rows loaded, and the integrity checks a normal store open performs — foreign
  keys, typed JSON columns, recomputed sealed payload digests — did not hold. It is a different fact from a
  malformed artifact, so a caller can tell "your document is wrong" from "your records are not this
  schema's knowledge".

### Conventions

- Every factory takes the operation name as its first argument, so the refusal names the operation the
  caller actually addressed (`export_knowledge_dataset` or `import_knowledge_dataset`).
- `RefusalFacts` carries the offending `table`, `record_id`, `expected` and `observed` where they exist;
  a factory with no fact to report passes none rather than inventing a placeholder.
- Each factory carries its own `next_action` sentence, because the remedy differs: re-encode the artifact,
  import with the build that implements its generation, re-issue the request naming the destination's
  identity, or regenerate from a dataset this store produced.

### Invariants And Boundaries

- **Every one of these refusals leaves the destination exactly as it was.** Staging happens in a private
  file and the install is the same atomic replace every other publication uses, so an artifact that is
  refused publishes nothing and a partially imported dataset is not an observable state.
- **A refusal is a value, never an exception, on this boundary.** These factories are what a caller
  receives instead of an `OSError`, an `apsw.Error` or a `ValueError`, including for a value the canonical
  encoding cannot spell.
- **A refusal's identity is contract.** Which code, which `record_id` and which `table` a caller gets is
  asserted by the leaf's nodes, not incidental.
- **Boundary.** This module names failures; it does not decide them. The reader and the validator decide
  (`export_portable.py`), the operation sequences them (`export_import.py`), and the shared `refusal`
  factory owns the value shape.

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
| **The malformed-or-incomplete refusal, and why one code covers both facts.** | `invalid_export_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:26-50 |
| **The canonical-form refusal: the same code, its own factory and its own record identity, because the fact is the one the guarantee rests on.** | `non_canonical_export_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:53-75 |
| The unsupported-generation refusal and its no-migration next action. | `unsupported_schema_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:78-102 |
| The two mirrors of "an import never patches a live destination in place". | `destination_occupied_refusal`; `destination_absent_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:105-126; mcp/src/agents_remember/memory/knowledge/export_refusals.py:129-148 |
| The staged-database refusal, which is a different fact from a malformed artifact. | `import_validation_failed_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:151-172 |
| The shared value shape and facts every factory builds on. | `refusal`; `RefusalFacts` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-77; mcp/src/agents_remember/memory/knowledge/refusals.py:36-54 |
| The declared vocabulary these factories produce, including the one code only a portable artifact can reach. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:72-120 |
| The nodes that assert each of these refusals by code rather than by message. | "test_an_incomplete_or_inconsistent_artifact_is_refused"; "test_a_document_that_is_not_a_well_formed_artifact_is_refused"; "test_an_artifact_this_build_or_this_namespace_cannot_accept_is_refused" | mcp/tests/test_knowledge_portable_roundtrip.py:602-659; mcp/tests/test_knowledge_portable_roundtrip.py:717-802; mcp/tests/test_knowledge_portable_roundtrip.py:804-876 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): created this one-to-one card for the portable boundary's refusal vocabulary. It records the five factories and the fact each one names, the deliberate single `invalid_export` code for both the malformed document and the incomplete dataset (with the reason: splitting it would invite a caller to read "parsed" as "trustworthy"), the canonical-form refusal's own factory and `"<canonical document>"` record identity, the closed two-mode destination rule behind `destination_occupied`/`destination_stale`, and the staged-database refusal that keeps "your document is wrong" distinct from "your records are not this schema's knowledge". It states the boundary rule once — **every one of these refusals leaves the destination exactly as it was** — and that a refusal here is a value rather than an exception. Verification metadata remains empty until closeout stamps the code commit.
