# dashboard/src/panels/knowledge-reader/knowledgeReader.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Real served bodies of `/api/knowledge/reader` for the dashboard's reader tests (`KnowledgeReader.test.tsx`):
17 answers read by this leaf's code over a converted scratch copy of the real repositories.** About 314 KB,
prettier-formatted. The `_provenance` key records where the bodies came from and how they were trimmed.

- **Scratch:** the memory `f94bc410` converted by `knowledge-convert` (`9f1c5de6`), with SCRATCH-AUTHORED
  curation (`5cf57da6`: family routes, decisions, incident, history rows; `879ff5df`: a revision, a proof and a
  re-anchor) and the census `1e3c8b1e`; the code `48f680d5`. Every scratch-authored record's text says
  SCRATCH, because converted memory holds no routes, decisions, incidents, proofs, history rows or censuses yet.
- **Source:** `notes/reports/260928-MIK-L29-evidence/served/*.json`, produced by `run_reader.py` over
  `/tmp/mik-l29-real`, and re-captured after review fix round R1 (the bounded directory view, subtree pages, the
  `re-anchored` label, `pinnedCommit` and `codeSource`) by `capture_ui_fixture.py`.
- **Trims:** the worktrees directory's and the root's prose to 4,000 characters, the root's references to the
  first 8, and the code body to 240 lines.

## Code Commentary

### Logic

- **The bodies:** `census`, `code-integrate`, `path-integrate-file`, `path-root` (the root summary),
  `path-test-file`, `path-worktrees-dir` (the packet's conforming example), `record-decision`,
  `record-decision-superseded`, `record-family`, `record-incident`, `record-invariant`, `records`, `selections`,
  `subtree-worktrees` (one complete page of 9 rows under policy `knowledge-reader-subtree`), `tree-root`,
  `tree-worktrees` and `without-proof-worktrees`.
- **What they show:** every selection is `published` at memory `1e3c8b1e…`, measured at the checkout's `HEAD`
  (`codeSource: checkout-head`) with `pinnedCommit` set because the tree was clean; `DEC-R29AAA` is stored
  `active` and derived `superseded`; the selector lists the recent commits with `commitsState: listed`, the
  unconverted ones marked.

### Conventions

- The fixture embeds absolute `/tmp/mik-l29-real` paths and the SCRATCH-authored texts; the reviewer judged it
  acceptable (review R1 note N3), in line with `familyPaging.captured.json` and `gitTrees.invariant.captured.json`.

### Invariants And Boundaries

- The fixture's key sets equal the backend's output (the reviewer diffed all captured views). A backend field
  change needs a re-capture, not a hand edit.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The provenance: the re-capture, the scratch commits, the source and the trims. [1]
- The root summary's body. [2]
- The superseded decision: stored active, derived superseded. [3]
- The invariant's body with its timeline. [4]
- The commit list named as listed. [5]
- One subtree page under the reader's policy. [6]
- The test that reads it. [7]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
