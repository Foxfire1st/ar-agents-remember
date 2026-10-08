# mcp/tests/test_review_artifact_cleanup.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R25 rule 5 cases: the archive hook deletes only the archived
task's own review artifacts, and a repeated attempt keeps its receipts.** Split out of `test_review_git_trees.py` by ruling 2026-09-30T02:32:42. The `task`
fixture is a coordination task root with its task document and one leaf enclosure contract, a plain code and a
plain memory repository, and nothing converted: the hook reads refs, manifests and files, never knowledge. Every
case asserts what is deleted and, as much, what another task still holds. The file is self-contained (no shared
support module), so the catalog is unchanged; it runs in the `unit-regression` lane
(`test-evidence-lanes.toml`).

## Code Commentary

### Logic

- **The main case, through the finalizer's `_with_review_artifact_cleanup` with the port bound:** a dry run lists
  and deletes nothing; then the task's review ref under its directory name (both repositories), its own legacy
  retained-code pin, a generation snapshot and a renamed knowledge copy (`pub2.sqlite`, found by content) are
  deleted and recorded in `notes/reports/review-artifact-cleanup.json`; a review ref under the `task.json` id
  namespace, the colliding `260101-trvx-l1` and `260101-trv-extra-l01` pins, another task's review ref and a
  non-knowledge SQLite file survive.
- **Identity (rulings 23:15:34 F1, 00:08:39, 02:12:06, 02:32:42):** colliding task ids never select each other's
  pins (parametrized over `260906-IAS`/`260906-ias-memory-recovery-l01` and `260928-MIK`/`260928-mik-extra-l01`); a
  comparison record naming another task never widens the archive; a `task.json` naming another task touches none
  of its refs; a planted leaf contract never reaches another task's review refs (V10; the legacy `other-1-l1` pin
  follows the trust line).
- **Never raises, and holds (F2, F3):** a missing repository and an owner that refuses a release are failures;
  the refused generation's pin and snapshot survive and are reported.
- **Provable ownership (ruling 01:00:07):** a planted foreign manifest releases nothing — four parametrized cases:
  a foreign leaf, a foreign pin, a foreign repository, and a snapshot path escaping its directory.
- **Physical confinement (ruling 01:37:42):** the content scan never follows a symlink out of the task; a
  symlinked `notes` root is neither scanned nor written (`reportPath` null); a symlinked generation directory
  releases nothing and writes no `deletions/` outside.

- **Receipts per attempt:** `test_a_repeated_attempt_keeps_receipts_never_leaves_the_name_empty_and_reports_absence`
  runs the hook twice. The first attempt writes receipt 1 with an empty `alreadyAbsent`. A second attempt with nothing
  new returns `receipt: "unchanged"`, writes no numbered copy, leaves the canonical bytes alone, and lists the ref the
  first attempt deleted as `alreadyAbsent`. A later attempt with real work keeps the first receipt as
  `review-artifact-cleanup.attempt-1.json`, writes attempt 2 under the canonical name, and the canonical name existed
  at the moment of the atomic replace.

### Conventions

- `_owners` patches `read_manifest` and the two reclamation owners where a case plants a manifest and observes
  whether an owner was called; the refs and files are real.

### Invariants And Boundaries

- These cases prove the candidate invariant recorded on `application/review_artifact_cleanup.py`: archival
  deletes only targets derived from the archived task's own identity, confined to its physical folder.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` lives outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The plain task fixture with its leaf contract and two repositories. [1]
- The main archive case. [2]
- Colliding task ids. [3]
- A record, a task document, or a planted leaf contract never reaches another task's refs. [4]
- Never raises; a refused generation is held. [5]
- A planted foreign manifest releases nothing. [6]
- Symlinks: the scan, the notes root, the generation directory. [7]
- The lane row. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

- A repeated attempt reports what is already absent, keeps the first receipt as attempt 1, and writes none when nothing is new. [9]
