# mcp/tests/test_knowledge_worklist.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R08@v2 worklist cases over real Git repositories (21 cases).** Every case builds two real
repositories under `tmp_path`: **code** (a small package `pkg/review.py` with four functions, `pkg/other.py`,
a test module, a ten-line text file and a binary file) and a **converted memory** whose base commit records
realization and proof entries anchored at the code base, two families and their invariants. A case commits a
code candidate C and, where it matters, a memory candidate K_C, then computes the worklist over the four named
sides (`worklist_for_sides`) exactly as the leaf route does.

## Code Commentary

### Logic

- **Fixture.** `ENTRIES` maps eight entries to invariants `INV-AAAAAA` to `INV-FFFFFF` (symbol, line-range
  and file locators, one `proves` entry on `test_refuses_unlisted`); `FAMILIES` groups them. `World` commits
  code and memory, builds anchors and sidecars, and runs `worklist`. `items`, `classes` and `entry_facts`
  index a result. Since MIK-R10, `knowledge_items` (every item but the `UNEXPLAINED_KINDS`) is what the
  "raises nothing" assertions check: an unlinked hunk now raises MIK-R10's `unexplained_hunk`, which is not an
  item about recorded knowledge.
- **Covered obligations:**
  - hunk parsing and line-range mapping arithmetic (definition 2 and 3);
  - the conforming example: a body edit of `_not_listed` raises exactly one `touched_invariant` and its
    `reached_family`, the other entries in the file are `carried`, and siblings are classified; the
    non-conforming "four invariants" case is excluded by the exact item set;
  - the boundary: a comment between functions raises no knowledge item (it is linked to no entry, so it
    raises exactly one `unexplained_hunk`, MIK-R10), a comment inside raises;
  - class precedence: `stale_at_base` first, reaching its families without widening; `moved_or_absent` for
    deletion, rename (with a `mechanical` unique match), ambiguity (no match) and a deleted range;
  - line ranges that map, carry and touch; proof entries in change detection (a changed test body is
    `touched`, a deleted test `moved_or_absent`, on `INV-AAAAAA`);
  - gate linkage: binary changes against a file anchor, text hunks linked by either side's ranges, and a mode
    change with a text change (review R1 F5);
  - maintenance scope; added, retired and re-anchored entries (and new records raising nothing); a
    mechanical carry in K_C is not a change; a re-anchor of a stale entry raises the stale item; a record
    change with both revisions;
  - the registry's four declarations and refused duplicate; item-ID stability and determinism;
  - `incomplete` for an unknown B and an unparseable K_C; no worklist when both memory sides are
    unconverted; the definition-4 ruling (review R1 F3); a partial inventory with a real non-UTF-8 file name
    is `incomplete` (F4).

### Conventions

- Assertions check exact sets and exact classes, not "non-empty".
- The module is registered in the `unit-regression` lane of `test-evidence-lanes.toml`.

### Invariants And Boundaries

- The fixture's `_not_listed`, `test_refuses_unlisted` and `test_accepts_listed` are **fixture source text**
  inside string constants, not test cases of this module.
- Every case runs on real Git trees and real converted memory; nothing is mocked.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The two real repositories each case builds. [1]
- The fixture's entries and locators. [2]
- The fixture world and its worklist run. [3]
- The knowledge items, without MIK-R10's unexplained kinds. [4]
- Hunk parsing and mapping. [5]
- The conforming body-edit example. [6]
- The comment boundary: no knowledge item between functions, and exactly one unexplained hunk (MIK-R10). [7]
- Proofs in change detection. [8]
- Knowledge-side changes. [9]
- The registry. [10]
- `incomplete` inputs. [11]
- Both memory sides unconverted: no worklist. [12]
- The definition-4 ruling. [13]
- A partial inventory. [14]
- The lane registration. [15]

### Cross-Repo References

No meaningful cross-repo references found: every repository is built under `tmp_path`.

No cross-repo boundary is crossed by this file.
