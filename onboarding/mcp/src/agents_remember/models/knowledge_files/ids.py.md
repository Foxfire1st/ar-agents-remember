# mcp/src/agents_remember/models/knowledge_files/ids.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/ids.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Stable, branch-safe identity for every knowledge record and sidecar entry (MIK-R21 rule 2).** An
ID is `<KIND>-<body>` in Crockford base32. New IDs are **minted at random** (6 characters), which is
what makes them safe across parallel leaves that never coordinate; IDs of records and entries
exported from the legacy knowledge database are **derived** (8 characters) from legacy identity so
every line that converts the same claim computes the same ID (MIK-R24 rules 4 and 6). This module
also holds the one table of record kinds and their prefixes, and the two entry kinds.

## Code Commentary

### Logic

- `RECORD_PREFIXES` maps the ten record kinds (`invariant`→`INV`, `family`→`FAM`, `decision`→`DEC`,
  `incident`→`INC`, `assumption`→`ASM`, `limitation`→`LIM`, `failure_mode`→`FLM`, `scenario`→`SCN`,
  `diagnostic`→`DGN`, `term`→`TRM`); `ENTRY_PREFIXES` maps `realization`→`RLZ` and `proof`→`PRF`.
- `id_pattern(*prefixes)` builds the anchored regex: prefix, `-`, six Crockford characters, optionally
  two more. `RECORD_ID_PATTERN`, `REALIZATION_ID_PATTERN` and `PROOF_ID_PATTERN` are built from it and
  used by `shapes.py`, `sidecars.py` and `documents.py`.
- `mint_id(kind)` draws six characters with `secrets.choice`. An unknown kind raises `ValueError`.
- `crockford_base32(data, length)` encodes the leading `length*5` bits most-significant first;
  `derived_id(kind, material)` takes SHA-256 of the material and keeps 8 characters (40 bits).
- `derived_record_id(kind, legacy_id)` derives from the UTF-8 legacy ID; `derived_realization_id`
  derives from the compact, key-sorted JSON array `[invariant legacy ID, path, locator]`, where the
  locator is in the **new sidecar form** (`{"kind":"symbol","name":…}`, `line_range` with
  `start`/`end`, or `file`). The conversion must translate legacy `qualified_name`/`start_line`
  locators before deriving, or the IDs will not match.

### Conventions

- Crockford alphabet `0-9A-Z` without `I`, `L`, `O`, `U`; one alphabet constant is shared by the
  patterns and the encoder.
- A filename slug is display only (`<ID>-<slug>.json`); the ID never depends on it.

### Invariants And Boundaries

- **An ID is never derived from content, except the derived IDs of exported legacy records and
  entries.** Minted IDs are random; a sequential counter such as `INV-0143` is refused by the
  pattern because parallel leaves would mint it twice.
- The derivation bytes are part of the format: changing the JSON serialization of the realization
  material, or the bit order of the encoder, changes every exported ID. Golden values in
  `test_knowledge_file_formats.py` (`FAM-SEQNTS6C`, `RLZ-0QYX992Q`) pin both.
- Uniqueness of a minted ID is checked by the validator (MIK-R22), not here.

### Todos

MIK-R24 must adopt the realization-ID material exactly as pinned here, or change it together with the golden value.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The patterns built here are the only ID spellings the rest of the package accepts.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two kind tables, declared once. | `RECORD_PREFIXES`; `ENTRY_PREFIXES` | mcp/src/agents_remember/models/knowledge_files/ids.py:49-61 |
| The ID regex: six characters, optionally eight. | `id_pattern` | mcp/src/agents_remember/models/knowledge_files/ids.py:66-69 |
| Random minting. | `mint_id` | mcp/src/agents_remember/models/knowledge_files/ids.py:87-91 |
| SHA-256, first 40 bits, most significant first. | `crockford_base32`; `derived_id` | mcp/src/agents_remember/models/knowledge_files/ids.py:94-105; mcp/src/agents_remember/models/knowledge_files/ids.py:108-112 |
| The pinned realization material and its new-form locator rule. | `derived_realization_id` | mcp/src/agents_remember/models/knowledge_files/ids.py:123-146 |
| Golden values pin the derivation. | `test_derived_ids_are_eight_characters_and_deterministic` | mcp/tests/test_knowledge_file_formats.py:88-111 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
