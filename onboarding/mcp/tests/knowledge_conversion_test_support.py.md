# mcp/tests/knowledge_conversion_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_conversion_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**Fixture repositories for the MIK-R24 conversion tests.** It builds a code repository and an unconverted
memory tree whose cards exercise every citation-row case, plus a legacy knowledge database. The database
holds only the tables and columns the export reads, in the real schema's spelling, so the export runs the
same queries it runs on a real `knowledge.sqlite`.

## Code Commentary

### Logic

- `code_repository(root)` builds a two-commit code repository (`CodeFixture`: root, `first`, `head`,
  the app and deleted blobs). `src/pkg/app.py` holds `alpha`, `beta` and `Holder.method` (`APP_SOURCE`);
  `src/pkg/deleted.py` exists only in the first commit; there is also a test file and a guide.
- `app_card(commit)` is the card with each table kind:
  - several anchors and sources in one row, with covered ranges;
  - placeholder rows;
  - a quoted anchor, a removed path and a range past the end;
  - a URL, a whole-file source and a test source;
  - marker-shaped prose (`signals[0]`) and an Update History;
  - a stray row appended below a table (`STRAY_ROW`).

  `other_card` has no evidence. `route_card` is a route overview with no verified commit, so it is a
  fallback card.
- `legacy_database(path, code, *, colliding=False)` writes a legacy database:
  - a two-revision invariant, a second invariant and a family;
  - hand-off lines in `conditions`;
  - actor refs of both shapes (`LEAF_ACTOR`, `DOC_ACTOR`);
  - claims, one of them on the deleted file, and one with the hand-off role `incidental`.

  `colliding=True` adds a claim whose derived entry ID collides.
- `memory_repository(root, code, *, database=True)` commits the memory tree (and the database) and returns
  its head.
- `git`, `init_repository` and `commit_files` are the shared Git helpers.

### Conventions

- Registered in `mcp/tests/evidence-lifecycle.toml` as a `shared-support` artifact (`introduced_by` `260928-MIK-L24`), with its exact consumers.

### Invariants And Boundaries

- The legacy schema is spelled as the real one, so a fixture pass means the real queries run.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The fixture builders.

| Finding | Anchor | Source |
| --- | --- | --- |
| The code repository. | `code_repository`; `CodeFixture`; `APP_SOURCE` | mcp/tests/knowledge_conversion_test_support.py:84-104; mcp/tests/knowledge_conversion_test_support.py:75-81; mcp/tests/knowledge_conversion_test_support.py:25-40 |
| The card with every row case, and the stray row. | `app_card`; `STRAY_ROW` | mcp/tests/knowledge_conversion_test_support.py:118-141; mcp/tests/knowledge_conversion_test_support.py:41-41 |
| The route overview and the evidence-free card. | `route_card`; `other_card` | mcp/tests/knowledge_conversion_test_support.py:152-157; mcp/tests/knowledge_conversion_test_support.py:144-149 |
| The legacy database in the real column spelling. | `legacy_database` | mcp/tests/knowledge_conversion_test_support.py:192-297 |
| The committed memory repository. | `memory_repository` | mcp/tests/knowledge_conversion_test_support.py:300-314 |
| Its catalog row. | "mcp/tests/knowledge_conversion_test_support.py" | mcp/tests/evidence-lifecycle.toml:1855-1874 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
