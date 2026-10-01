# mcp/tests/test_knowledge_reader.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R29's backend proof: the path-based knowledge reader's explorer, path view, subtree pages, truth views,
timeline, census, selections, failures, route and read-only behaviour.** 21 cases, self-contained (the module
imports no test support module, so the evidence-lifecycle catalog needed no re-pin). It is registered in the
`unit-regression` lane of `test-evidence-lanes.toml`.

## Code Commentary

### Logic

- **The fixture world** (`world`) is a coordination root with one repository `demo`: a code repository (the
  review file with `loadReview`, three sibling files, a test file and a binary blob with a NUL) and its
  converted memory repository at `memory-repos/ar-demo`, with three commits:
  - an **unconverted** commit (`memory.md` only);
  - **commit 1** (`Code-Commit` of the code commit): MIK-R23's review-example tree, a family realized across
    four files, a test proof, a decision and an incident linking to an invariant, a route sidecar, two leaves'
    history rows, a retired invariant, a sibling-prefix file (`dashboard/src/database.ts`), onboarding prose with
    numbered references, and a census;
  - **commit 2**: the invariant's statement revised, one realization re-anchored in place and one moved to
    another file, a third leaf's history row, an assumption facet, and a decision superseding the first.
- **The cases, by rule:**
  - rule 2: the file view (references, entries with states, the family via its route and its other
    locations, linked records), the bounded directory view (own level, children with counts, subtree size,
    the route link; F2), the test file (proofs with facets), and the without-proof list by path;
  - F2, F16, F17, R3-1 and R3-2: the subtree walk (complete, ordered, every whole answer within the bound, the
    sibling prefix never counted), a walk resumed after a code commit (page 2 at page 1's tree in both
    `page.codeTreeId` and `selection.codeTree`, the "moved since" note, a fresh walk at the new HEAD, and a token
    naming an absent tree refused), and another walk's token refused (another path, another memory tree,
    garbage);
  - rule 1: the explorer (code and onboarding children, `inCode: false` for a moved realization's new file, a
    retired invariant's entry not counted);
  - rules 3 and 4: the invariant view with a three-source timeline, moves against re-anchors while reading only
    the sidecars naming them (F1, F5), the bounded timeline cache (built once per tree; a failed source is not
    remembered, F7 and F17), the family, the decision (derived supersession), the incident and facet with
    typed links both ways (and unreadable links named, F11), and the census;
  - selections: hexadecimal names only, a branch name refused, a commit list that cannot be read named (F6,
    F11, N1 `paired-code-commit`); the published tree reads uncommitted state, writes nothing and offers a pin
    only when clean (N2, N1 `checkout-head`, the tree key in the cache key); a live leaf and its code note;
    a partial index and a missing code tree named where they apply;
  - the route: every view served over HTTP, 503 unwired, nothing written in either repository; bad requests
    400 (malformed locators F3, `../etc`, an unknown view, NUL and control characters on every path view F15),
    a directory as code `absent` (F18), a binary blob `binary`, and a blob above the bound `too-large` without
    its bytes being read (F14, F17).
- **Read-only proof.** `_snapshot` records refs, `--no-optional-locks` status, `count-objects` and the index
  file of both repositories; the route case and the published case compare it before and after.

### Conventions

- Subtree cases cut at 800 tokens, where one row fits beside the reader's envelope.
- Cases were split into assertion helpers so no test function is at radon C or worse (review F8).

### Invariants And Boundaries

- The file is 1,182 lines, under the 1,200-line cap (the architect noted its size at R3). A later case should go
  to a new module.

### Todos

- **Size:** the next reader case belongs in a new test module, not here (ruling 2026-09-30T11:24:12 note).

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of the fixture's two converted commits. [1]
- The converted tree, the second commit's changes and the world with an unconverted commit. [2]
- The read-only snapshot of both repositories. [3]
- The file and bounded directory views. [4]
- The subtree walk, the walk's code tree (F16, R3-1, R3-2), and another walk refused. [5]
- The whole answer, envelope included, within the bound (F17). [6]
- The test file, the explorer and the without-proof list. [7]
- The invariant view, moves and re-anchors, and the timeline cache. [8]
- The family, decision, incident and facet, and census views. [9]
- The selections: commits, published, a leaf, and a partial index with no code tree. [10]
- The route, and bad requests and bounded code notices. [11]
- The lane row. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
