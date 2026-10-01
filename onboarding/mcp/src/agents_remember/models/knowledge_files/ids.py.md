# mcp/src/agents_remember/models/knowledge_files/ids.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Stable, branch-safe identity for every knowledge record and sidecar entry (MIK-R21 rule 2).** An
ID is `<KIND>-<body>` in Crockford base32. New IDs are **minted at random** (6 characters), which is
what makes them safe across parallel leaves that never coordinate; IDs of records and entries
exported from the legacy knowledge database are **derived** (8 characters) from legacy identity so
every line that converts the same claim computes the same ID (MIK-R24 rules 4 and 6). This module
also holds the one table of record kinds and their prefixes, the two entry kinds, and (since
MIK-R07) the history row kind.

## Code Commentary

### Logic

- `RECORD_PREFIXES` maps the ten record kinds (`invariant`→`INV`, `family`→`FAM`, `decision`→`DEC`,
  `incident`→`INC`, `assumption`→`ASM`, `limitation`→`LIM`, `failure_mode`→`FLM`, `scenario`→`SCN`,
  `diagnostic`→`DGN`, `term`→`TRM`); `ENTRY_PREFIXES` maps `realization`→`RLZ` and `proof`→`PRF`;
  `ROW_PREFIXES` maps the one row kind `history_row`→`ROW` (MIK-R07 rule 1; the `ROW-` spelling was
  chosen by the L07 worker, the packet names no prefix).
- `id_pattern(*prefixes)` builds the anchored regex: prefix, `-`, six Crockford characters, optionally
  two more. `RECORD_ID_PATTERN`, `REALIZATION_ID_PATTERN`, `PROOF_ID_PATTERN`, `ENTRY_ID_PATTERN`
  (either entry prefix) and `ROW_ID_PATTERN` are built from it and used by `shapes.py`,
  `sidecars.py`, `documents.py` and `history.py`.
- `mint_id(kind)` accepts a record, entry or row kind and draws six characters with
  `secrets.choice`. An unknown kind raises `ValueError`. Row IDs are minted, never derived:
  `derived_id` still takes only record and entry kinds.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The patterns built here are the only ID spellings the rest of the package accepts.

- The kind tables, declared once. [1]
- The entry and row ID patterns history rows use. [2]
- The ID regex: six characters, optionally eight. [3]
- Random minting, for record, entry and row kinds. [4]
- SHA-256, first 40 bits, most significant first. [5]
- The pinned realization material and its new-form locator rule. [6]
- Golden values pin the derivation. [7]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
