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

## Current source account

The projection guard retains two completion-truth clauses: (core/acceptance.md, "Terminal truth is mechanical; acceptance is the owner's.") and (roles/worker.md, "A finished turn is not AR acceptance."). The two formerly listed clauses (manager deliverable inspection; worker parent report notice) stay out under the retired-wording register (test_sync_scripts.py:114-118). A third projected clause now comes from `reference/shared-writing-profile.md`: “A clearer rewrite is never proof of preserved meaning.” It is a reach check for guidance, not another completion-truth owner or a semantic validator. Canonical and all nine generated targets must retain each marker; removing one from a packaged copy is detected. Copy/swap recovery and exact inventory guards remain.

## Code Commentary

New declaration/profile cases project a synthetic skill target into the generated-skills input and recompute the digest without changing other modeled profile content. The byte projector leaves its input profile file unchanged. A temporary two-target normal-sync matrix rejects missing, invalid-JSON and digest-mismatched profiles before any target mutation; the valid arm asserts projected profile bytes and canonical copy digests. The inventory and boundary loops call `skill_targets()` rather than a fixed `TARGETS` tuple. This source inspection ran no sync/check command, read no generated/private mirror and supplies no new projection or test grade.

### Logic

Four readings, each defended by a different case class:

- **Every declared copy equals `skills/` byte for byte**, in this checkout, with no pytest-only
  invocation required — `CanonicalProjectionConvergenceTests` reads the real nine targets and names the
  repair command that fixes each drifted path.
- **The drift reader itself can still fail** — `ReplaceTreeSequenceTests` hand-edits, deletes and adds
  files in a throwaway tree and requires all three failure kinds to be reported. The copy-then-swap
  sequence is characterized at the two places it can fail, including the rename interruption
  (`RenameInterruption`, 246).
- **The declared inventory is the certified one** — `DeclaredProjectionInventoryTests` requires the
  script's declaration-backed `skill_targets()` to equal the paths `mcp/certification-profile-v1.json` declares as the
  `generated-skills` generated input, so a target silently dropped from the script fails.
- **The corrected boundary clauses reach every copy** — `BoundaryPropagationTests` (459) re-asserts the
  shipped completion-truth clauses against canonical **plus** the nine copies through
  `boundary_locations()` / `boundary_surface_texts()` / `missing_clause_locations()`, and
  `test_a_clause_missing_from_one_...` deletes the Worker acceptance clause from one copy to prove that reach case bites.

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

## Current scoped contract

The new shared-profile marker is included in `PROJECTED_BOUNDARY_CLAUSES`, so the positive canonical/generated-copy reach loop checks that document too. The seeded missing-copy case explicitly selects the Worker acceptance clause; it is not a separately seeded shared-profile negative control. The two completion-truth markers and retirement exclusions remain. Executed reach checks would establish declared propagation, never equivalence of any rewritten invariant; this curation is source inspection only.

## Evidence

- Declaration-backed targets, pure profile projection and the normal-sync prevalidation matrix preserve unrelated profile fields and refuse bad profiles before target mutation. [6]


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


- The shared-profile marker participates in the positive canonical/copy loop; the seeded missing-copy case selects the Worker acceptance clause, not the profile. The two completion-truth markers and retired omissions remain. [7]
