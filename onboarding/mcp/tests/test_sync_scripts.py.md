# mcp/tests/test_sync_scripts.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Convergence guard for the skill projection: `skills/` is the only source, and every declared packaged
copy is its byte image. The subject is a *role-dependent lifecycle truth* — an agent reads whichever
skill tree its harness installed (root `skills/`, the MCP package data `runtime_install` copies into a
coordination root, or one of the eight harness starter packages), so correcting one copy and leaving
eight stale means two agents in the same task hold different authority boundaries and neither can tell.
`scripts/sync-skills.py` is the mechanism that makes that impossible, and this module is the
executable statement that it happened.

## Code Commentary

### Logic

Four readings, each defended by a different case class:

- **Every declared copy equals `skills/` byte for byte**, in this checkout, with no pytest-only
  invocation required — `CanonicalProjectionConvergenceTests` reads the real nine targets and names the
  repair command that fixes each drifted path.
- **The drift reader itself can still fail** — `ReplaceTreeSequenceTests` hand-edits, deletes and adds
  files in a throwaway tree and requires all three failure kinds to be reported. The copy-then-swap
  sequence is characterized at the two places it can fail, including the rename interruption
  (`RenameInterruption`, 245).
- **The declared inventory is the certified one** — `DeclaredProjectionInventoryTests` requires the
  script's `TARGETS` to equal the paths `mcp/certification-profile-v1.json` declares as the
  `generated-skills` generated input, so a target silently dropped from the script fails.
- **The corrected boundary clauses reach every copy** — `BoundaryPropagationTests` (458) re-asserts the
  shipped completion-truth clauses against canonical **plus** the nine copies through
  `boundary_locations()` / `boundary_surface_texts()` / `missing_clause_locations()`, and
  `test_a_clause_missing_from_one_...` deletes one clause from one copy to prove the reach case bites.

`BoundaryClause` (101) is deliberately a **reach** table, not a second vocabulary: *which* clauses each
surface owes is the doctrine guard's subject (`mcp/tests/test_lifecycle_turn_truth_doctrine.py`), and
this table quotes that module's shipped wording rather than paraphrasing it, so the two guards cannot
drift into two spellings of one boundary.

### Conventions

- The canonical tree is read from the checkout (`CANONICAL_SKILLS_PATH`), and each target is compared
  byte for byte — no hashing shortcut that would let a whitespace-only drift pass.
- Failure messages name the repair command (`REPAIR_COMMAND`), because the reader's next move is to run
  it rather than to hand-edit a copy.
- Temporary trees are throwaway; the staging/retired suffixes (`.ar-sync-new`, `.ar-sync-old`) are the
  script's own and are asserted rather than assumed.

### Invariants And Boundaries

- **A generated copy is never hand-edited.** Canonical plus `scripts/sync-skills.py` is the only route;
  a hand-fixed copy is drift that will be re-broken by the next sync, and the convergence case exists to
  make that impossible rather than to be worked around.
- **The projection table quotes the doctrine guard's own shipped wording.** A row whose surface or
  marker stops matching the canonical tree and its nine copies still fails; re-pointing the table is a
  data change and never a loosening of the reach.
- **Clause reach is not clause meaning.** This module proves a clause arrived; it does not decide what
  the clause should say. Loosening a row here to make a copy pass would defeat the guard's purpose.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; both sides of the comparison are
repository-owned files.

No configured `Domain Documentation` source applies; the subject is the repository's own projection script and its declared targets.

### Repo-Internal References

- The projection mechanism whose behavior this module pins. [1]
- None [2]
- The boundary clauses this module re-asserts across canonical plus the nine copies, quoted from the doctrine guard. [3]
- The doctrine guard that owns which clauses each surface owes, whose wording this table quotes. [4]
- The doctrine surface the whole-boundary clause now ships at, and the copy family that must carry it. [5]

### Cross-Repo References

No external repository boundary is exercised; the nine targets are this repository's own skill trees.

No meaningful cross-repo references found.
