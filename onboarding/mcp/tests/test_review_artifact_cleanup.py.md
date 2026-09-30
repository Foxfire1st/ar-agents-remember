# mcp/tests/test_review_artifact_cleanup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_artifact_cleanup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R25 rule 5 cases (14 collected, with the parametrized ones): the archive hook deletes only the archived
task's own review artifacts.** Split out of `test_review_git_trees.py` by ruling 2026-09-30T02:32:42. The `task`
fixture is a coordination task root with its task document and one leaf enclosure contract, a plain code and a
plain memory repository, and nothing converted: the hook reads refs, manifests and files, never knowledge. Every
case asserts what is deleted and, as much, what another task still holds. The file is self-contained (no shared
support module), so the catalog is unchanged; it runs in the `unit-regression` lane
(`test-evidence-lanes.toml:123`).

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

### Conventions

- `_owners` patches `read_manifest` and the two reclamation owners where a case plants a manifest and observes
  whether an owner was called; the refs and files are real.

### Invariants And Boundaries

- These cases prove the candidate invariant recorded on `application/review_artifact_cleanup.py`: archival
  deletes only targets derived from the archived task's own identity, confined to its physical folder.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` lives outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The plain task fixture with its leaf contract and two repositories. | `Task`; `task` | mcp/tests/test_review_artifact_cleanup.py:78-168 |
| The main archive case. | `test_archiving_deletes_the_tasks_review_refs_legacy_pins_and_dataset_copies` | mcp/tests/test_review_artifact_cleanup.py:228-278 |
| Colliding task ids. | `test_archiving_one_task_never_selects_a_colliding_tasks_pins` | mcp/tests/test_review_artifact_cleanup.py:281-299 |
| A record, a task document, or a planted leaf contract never reaches another task's refs. | `test_a_comparison_record_naming_another_task_never_widens_the_archive`; `test_a_task_document_naming_another_task_touches_none_of_its_refs`; `test_a_planted_leaf_contract_never_reaches_another_tasks_review_refs` | mcp/tests/test_review_artifact_cleanup.py:305-348 |
| Never raises; a refused generation is held. | `test_the_archive_hook_never_raises_and_holds_a_generation_its_owner_refused` | mcp/tests/test_review_artifact_cleanup.py:354-395 |
| A planted foreign manifest releases nothing. | `test_a_planted_foreign_manifest_releases_nothing` | mcp/tests/test_review_artifact_cleanup.py:398-430 |
| Symlinks: the scan, the notes root, the generation directory. | `test_the_content_scan_never_follows_a_symlink_out_of_the_task`; `test_a_symlinked_notes_root_is_neither_scanned_nor_written`; `test_a_symlinked_generation_directory_releases_nothing` | mcp/tests/test_review_artifact_cleanup.py:436-478 |
| The lane row. | "mcp/tests/test_review_artifact_cleanup.py" | mcp/tests/test-evidence-lanes.toml:123-123 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new test file, recording rulings 23:15:34 (F1, F2, F3), 00:08:39, 01:00:07, 01:37:42, 02:12:06 and 02:32:42 (the test split). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
