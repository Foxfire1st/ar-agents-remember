# mcp/src/agents_remember/models/knowledge_files/history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Per-leaf history files: the curator's judgment rows, one file per owner (MIK-R07).**
`knowledge/history/<owner-id>.json` (`ar-history/v1`) belongs to exactly one owner — a `leaf`, a
migration `wave`, or a master-line `crossing` sync — and the owner ID names the file, so two leaves
never write the same file and their history merges without conflict. An invariant's *meaning*
history is the `git log` of its record file; its *judgment* history is the set of rows about it
across all history files. Nothing here is written into a record file, and no row is produced
automatically. The module also carries the freeze predicate for closed files and the writer-support
checks that compare a row with facts the caller reads from the base (K_B) and candidate (K_C) trees.

## Code Commentary

### Logic

- `HistoryRow` is the shared row shape: `id` (`ROW-…`, minted), `subject`, `disposition`, a
  nonblank `reason` and unique `items[]` (worklist item IDs, informational only). It cannot be
  validated directly; a concrete kind fixes `subject_pattern` and `dispositions`.
- `InvariantRow` (subject `INV-…`): `changed` | `moved` | `deleted` | `extended` | `no_impact`
  (D28), with `covers[]`, the invariant's K_C `revision` (≥1), `effect` (from the shipped nine
  `EffectLabel`s) and optional, non-empty `because[]` (decision IDs or requirement references).
  `_require_disposition_evidence` refuses a disposition its own covers or effect contradict:
  `changed` needs an effect; only `changed` and `deleted` may carry one, and `deleted` only
  `retire`; `deleted` without `retire` needs a removed entry. The `_COVER_REQUIREMENTS` table holds
  the rest: `moved` needs a re-anchored entry and no added or removed entry; `extended` needs an
  added entry; `no_impact` refuses added or removed entries.
- `CoveredEntry` is `{id: RLZ/PRF, before, after}`; each side is an anchor naming its `path`, or
  `"absent"`, never both absent. `added`, `removed` and `reanchored` derive from the two sides; any
  difference, including a blob-only one, counts as re-anchored.
- `FamilyRow` (subject `FAM-…`): `changed` | `rerouted` | `assigned` | `retired` | `no_impact`,
  with `examined[]` of `{id: INV, revision}` members, unique by ID.
- `HISTORY_ROW_KINDS` is the row-kind registry; `row_kind_for_subject` and `parse_row` dispatch a
  row to the one kind whose subject form it has, and refuse a subject no kind claims. Later packets
  (MIK-R06, R10, R11, R14, R30) add their kinds here.
- `HistoryFile` has `schema`, exactly one of `leaf`/`wave`/`crossing` (a crossing must match
  `<task>-crossing-<n>`), `closed` (strict bool) and `rows[]`, with row IDs and subjects each
  unique, so a file holds at most one row per subject (`row_about`). `closed_copy` and
  `empty_history(..., closed=True)` produce what the closeout writes.
- `is_closed_history` reads only `schema` and `closed` from raw bytes, so a closed file holding a
  row kind registered later is still recognized. `frozen_history_violation(bases, candidate)` is
  true when the file is closed on any base side (K_B or any merge parent) and the candidate bytes
  differ, including deletion and reformatting.
- Writer support: `reanchor_mismatches` (each `after` equals the entry's K_C anchor, `absent`
  means absent), `sidecar_entry_anchors` (fills the sidecar path into entry anchors for that
  comparison), `unknown_subjects`, `invariant_revision_violation` (the row's revision is the K_C
  revision; `changed` is exactly K_B + 1; `moved`, `extended` and `no_impact` keep the K_B revision;
  `deleted` is checked only against K_C; an invariant absent from K_B needs no row) and
  `stale_examined_members` (a member whose K_C revision differs is stale; one absent from K_C is
  not).

### Conventions

- Reuses L21's building blocks (`FileModel`, `Anchor`, `RequirementReference`, `require_unique`,
  `parse_json`, `id_pattern`) and the shipped `EffectLabel`, so the effect vocabulary is unchanged.
- Arrays `rows`, `covers` and `examined` are identified-entry arrays: the canonical formatter sorts
  them by `id`, so file order carries no recency.
- Several spellings were chosen by the L07 worker where the packet was silent: the `ROW-` prefix,
  the `crossing` owner pattern, and `items[]` accepting any exact token until MIK-R08 fixes item
  IDs.

### Invariants And Boundaries

- **A history file closed in K_B, or in any merge parent, is byte-identical in K_C.** Only the
  predicate lives here; the validator (MIK-R22 rule 7) enforces it and the closeout (MIK-R09, live
  from MIK-R37) sets `closed: true`.
- **A judgment is never stored in a record file.** Records forbid extra fields, so a `no_impact`
  judgment can only live in a history row.
- The models check shape and the helpers check facts the caller supplies; whether a row is current
  for a worklist item is the gate's rule (MIK-R09 rule 2), and the writer is MIK-R12's.
- Nothing in the installed runtime reads or writes history files before MIK-R37.

### Todos

D28 names seven dispositions; the family `retired` token follows MIK-R07 rule 5 and the architect's
ruling. Doc14 §4.7 still shows the older illustrative history shape; the architect owns that update.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R07@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The file model is registered in `documents.py`; the tests in `test_knowledge_history_files.py` pin
each rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two disposition vocabularies. | `INVARIANT_DISPOSITIONS`; `FAMILY_DISPOSITIONS` | mcp/src/agents_remember/models/knowledge_files/history.py:74-75 |
| The shared row shape and kind dispatch check. | `HistoryRow` | mcp/src/agents_remember/models/knowledge_files/history.py:94-119 |
| Covered entries: anchors with a path, or absent on one side. | `CoveredEntry` | mcp/src/agents_remember/models/knowledge_files/history.py:122-153 |
| What each disposition's covers must show. | `_COVER_REQUIREMENTS`; `_require_disposition_evidence` | mcp/src/agents_remember/models/knowledge_files/history.py:165-187; mcp/src/agents_remember/models/knowledge_files/history.py:190-206 |
| The invariant row. | `InvariantRow` | mcp/src/agents_remember/models/knowledge_files/history.py:209-225 |
| The family row and its examined members. | `ExaminedMember`; `FamilyRow` | mcp/src/agents_remember/models/knowledge_files/history.py:228-232; mcp/src/agents_remember/models/knowledge_files/history.py:235-247 |
| The row-kind registry and dispatch. | `HISTORY_ROW_KINDS`; `row_kind_for_subject` | mcp/src/agents_remember/models/knowledge_files/history.py:261-264; mcp/src/agents_remember/models/knowledge_files/history.py:267-273 |
| The file: one owner, one row per subject. | `HistoryFile` | mcp/src/agents_remember/models/knowledge_files/history.py:293-337 |
| The freeze predicate. | `is_closed_history`; `frozen_history_violation` | mcp/src/agents_remember/models/knowledge_files/history.py:351-370; mcp/src/agents_remember/models/knowledge_files/history.py:373-381 |
| Re-anchoring checked against K_C. | `reanchor_mismatches`; `sidecar_entry_anchors` | mcp/src/agents_remember/models/knowledge_files/history.py:389-401; mcp/src/agents_remember/models/knowledge_files/history.py:404-409 |
| The revision binding for invariant and family rows. | `invariant_revision_violation`; `stale_examined_members` | mcp/src/agents_remember/models/knowledge_files/history.py:422-442; mcp/src/agents_remember/models/knowledge_files/history.py:445-456 |
| The history schema is dispatched by `documents.py`. | `HISTORY_SCHEMA` | mcp/src/agents_remember/models/knowledge_files/documents.py:64-71 |
| Closed files stay byte-identical, even when reformatted. | `test_closed_in_base_implies_byte_identical_in_candidate` | mcp/tests/test_knowledge_history_files.py:320-348 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 adds the census import and the `CensusDocument` member to `models/knowledge_files/documents.py`, so its `SCHEMA_MODELS` table moved to `:64-71`; this card's history-schema row was re-pointed, its claim unchanged (the history schema is still registered there). No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta, after worker fix round 1): created this card for the new file MIK-R07 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
