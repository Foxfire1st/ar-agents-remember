# mcp/tests/test_sync_scripts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_scripts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository; both sides of the comparison are
repository-owned files.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source applies; the subject is the repository's own projection script and its declared targets. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection mechanism whose behavior this module pins. | `TARGETS` | scripts/sync-skills.py:43-56 |
| The certified generated-input declaration the target list must equal. | `generated-skills` | mcp/certification-profile-v1.json |
| The boundary clauses this module re-asserts across canonical plus the nine copies, quoted from the doctrine guard. | `PROJECTED_BOUNDARY_CLAUSES`; `BoundaryClause`; `boundary_locations`; `boundary_surface_texts`; `missing_clause_locations` | mcp/tests/test_sync_scripts.py:101-129; mcp/tests/test_sync_scripts.py:184-214 |
| The doctrine guard that owns which clauses each surface owes, whose wording this table quotes. | `OWED_STATEMENTS`; `COMPLETION_TRUTH_ROSTER` | mcp/tests/test_lifecycle_turn_truth_doctrine.py:112-127; mcp/tests/test_lifecycle_turn_truth_doctrine.py:478-529 |
| The doctrine surface the whole-boundary clause now ships at, and the copy family that must carry it. | "templates/turn-report.md" | skills/l-01-agent-lifecycles/roles/worker.md:158-158 |

## Cross-Repo References

No external repository boundary is exercised; the nine targets are this repository's own skill trees.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `OWED_STATEMENTS`; `COMPLETION_TRUTH_ROSTER` repointed to mcp/tests/test_lifecycle_turn_truth_doctrine.py:478-529; mcp/tests/test_lifecycle_turn_truth_doctrine.py:112-127. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: created this card. The module is **260831-LOCR's
  landed projection guard**, two of whose five `PROJECTED_BOUNDARY_CLAUSES` rows this leaf re-pointed at
  the consolidated corpus as a declared cross-task change: the `SKILL.md` row follows the boundary's one
  home to `core/acceptance.md`, and the manager row is quoted at the words the file carries today. The
  reach machinery, `boundary_locations()` over canonical plus the nine targets, and the
  delete-one-clause mutant case were **not** touched, and `scripts/sync-skills.py --check` exits 0, so
  the clauses are asserted against the copies as they now ship. This card also records the readings the
  module defends and the boundary that a generated copy is never hand-edited. Verification metadata is
  pinned to this leaf's synced base `8997e184` because the candidate is deliberately uncommitted — the
  governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
