# mcp/tests/knowledge_conversion_test_support.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The fixture builders.

- The code repository. [1]
- The card with every row case, and the stray row. [2]
- The route overview and the evidence-free card. [3]
- The legacy database in the real column spelling. [4]
- The committed memory repository. [5]
- Its catalog row. [6]

### Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

No cross-repo boundary is crossed by this file.
