# mcp/src/agents_remember/application/review_artifact_cleanup.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The archive hook for review artifacts: nothing a review pinned or copied outlives its task (MIK-R25 rule 5,
D17).** When a task is archived, this deletes, in both the code and the memory repository:

- every `refs/ar/review/<task-directory>/…` ref — the pins of the task's tree comparisons;
- the task's legacy `refs/ar/retained-code/<leaf>/…` refs — the landed reviewer's code pins;

and, under the task's `notes/`, every legacy knowledge dataset copy: a comparison generation's retained snapshot,
or any other SQLite file with the knowledge schema, identified **by content, not by name** (MIK-R26 rule 6).
Git-tracked files are skipped; they leave with their branch. Every deletion and every failure is recorded in the
task's archive report, `notes/reports/review-artifact-cleanup.json`, which the finalizer also returns as
`taskArchive.reviewArtifacts` (ruling 22:22:37 Q3). It is bound into the worktree layer as the
`ReviewArtifactCleanupPort` (`worktrees/services.py`) by `application/worktree_services.py`, and called by
`worktrees/modules/finalize.py` after the archive move.

## Code Commentary

### Logic

- **`cleanup_review_artifacts(request)`** builds a `_Confinement` of the task root, takes the legacy identity from
  `_confirmed_task_id`, releases the generations (`_release_generations`), deletes the review refs under
  `refs/ar/review/{request.task_name}/` and the task's own retained-code refs in each of the request's two
  repositories (a held ref is skipped), scans `notes/` for leftover copies (`_delete_dataset_copies`), and writes the
  report unless it is a dry run. The report state is `would-delete`, `deleted` or `partial` (any failure).
- **The hook never raises (review F2, 23:15:34).** A missing repository is a `failures` entry; the Git helpers
  catch `OSError`; the finalizer turns any exception into `reviewArtifacts: {state: "failed", detail}`.
- **Generations go through their own deletion owners.** `_release_one` calls
  `release_comparison_code_object` for the pin and `discard_comparison_snapshots` for the snapshots
  (`review_comparison_reclamation`), which write the unavailable-history record first, so a later reopen of the
  archived generation says the history was deleted and why. **A refused release is held (review F3):**
  `_Report.hold` leaves that generation's ref (the direct pass then skips it) and its directory (the content scan
  then skips it) and lists both under `failures` as "held, not deleted: …".
- **Exact own-task selection (review F1).** `_own_leaf(task_id)` is the full match `<task-slug>(-l\d+[a-z]?)?`, so
  `260906-IAS` never selects `260906-ias-memory-recovery-l01` and `260928-MIK` never selects
  `260928-mik-extra-l01`. `_retained_code_refs` applies it to the leaf segment of every retained-code ref.
- **No record widens the archive (ruling 2026-09-30T00:08:39).** The fix round's sweep of task ids named in
  `review-comparisons` records is removed: nothing read from a comparison record or a manifest widens the
  namespace.
- **A generation is released only when it provably belongs to the task (ruling 01:00:07).**
  `_foreign_generation` holds a generation unless `slugify(manifest.leaf_id)` and the leaf segment of its pin both
  pass the F1 rule, its code repository resolves to the request's, the owner's own `generation_directory` is the
  directory the manifest was found in, and every snapshot path resolves inside it.
- **Physical confinement (ruling 01:37:42).** `_Confinement.problem(path)` passes a path only when no component
  between the unresolved task root and it is a symlink (`is_symlink`, an `lstat`) and the resolved path lies inside
  the resolved root. It gates the manifest before it is read (a held generation's named pin is held too,
  `_named_pin`), the `deletions/` directory and each snapshot (`_outside_generation`), the `notes` scan root
  (`_scan_root`), every scan candidate (`_is_leftover_copy`), `task.json` (`_task_document_id`), the leaf contracts
  `_confirmed_task_id` reads, and the report (`_write_report`: written only inside the task, else `reportPath: null`
  with a failure entry).
- **The trust line for the legacy targets (rulings 02:12:06 and 02:32:42 (b)).** `_confirmed_task_id` takes
  `task.json`'s `id` only when it equals the task directory name, or when a leaf enclosure contract physically
  inside the task, naming this task as parent, has a leaf id `<id>-L<n>`; otherwise the directory name is used and a
  `task.json` failure is reported. That id serves **only** the retained-code pins and the manifest own-leaf check;
  review refs use the directory name whatever any file says. The module docstring states the identity source of
  every target, the trust line, the confinement and the accepted check-then-use window.
- **Content identification.** `_is_knowledge_dataset` reads the SQLite header, opens read-only, and requires the
  tables `invariant` and `invariant_revision`; `_tracked` skips a file Git tracks.

### Conventions

- Every deletion target is derived from the archived task's own identity, and every filesystem effect lies
  physically inside the task (the general principle of ruling 01:00:07, with 01:37:42's confinement).
- The report schema is `ar-review-artifact-cleanup/v1`; entries carry the repository, the ref and its target, or
  the path, the digest and `via` (the owner, or `content`).

### Invariants And Boundaries

- **Candidate invariant (not ingested): archival deletes only targets derived from the archived task's own
  identity, confined to its physical folder.** Realized by the directory-name review namespace,
  `_own_leaf`/`_retained_code_refs`, `_foreign_generation`, `_Confinement` and the removed record sweep. Proved by
  the 14 cases of `test_review_artifact_cleanup.py`, notably
  `test_archiving_one_task_never_selects_a_colliding_tasks_pins`,
  `test_a_comparison_record_naming_another_task_never_widens_the_archive`,
  `test_a_planted_foreign_manifest_releases_nothing`, `test_a_symlinked_notes_root_is_neither_scanned_nor_written`,
  `test_a_symlinked_generation_directory_releases_nothing` and
  `test_a_planted_leaf_contract_never_reaches_another_tasks_review_refs`, and on real data by the worker's archive
  rounds 2–5 and the reviewer's R6 probes (every planted foreign, old-namespace and prefix-collider ref survived).
- **Accepted limits (ruling 02:32:42).** A task whose `task.json` and a leaf contract are **both** forged can still
  delete another task's *legacy* retained-code pins (reviewer R6 note 1, probe V10): forging two control documents is
  outside the threat model. The check-then-use (TOCTOU) window between `_Confinement` and the owners' own writes is
  accepted: it needs a concurrent writer inside the just-archived task, which could delete those files anyway.
- **Not gated on conversion (ruling 22:22:37 Q4).** Once this build is installed (MIK-R37 at the earliest), archival
  also deletes unconverted tasks' legacy copies and retained-code refs, releasing through the reclamation owners so a
  later reopen reads `unavailable-history`.

### Todos

- **L37 (rulings 22:22:37 Q4 and 23:15:34 F7):** the cutover notes state that archival deletes all legacy dataset
  copies, including curator scratch copies (65 in the ICR task: 44 through the owner, 21 by content).

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` (rule 5), MIK-R26 rule 6 and D17 of task `260928_maintained-invariant-knowledge`, with the rulings in
`25_reviewer-on-git-trees.json`; they live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement of every target's identity source, the trust line, the confinement and the accepted window. [1]
- The report file, the reason, and the two tables that make a file a knowledge dataset. [2]
- The report, and holding a generation's pin and snapshots with the reason. [3]
- The composition-bound port implementation. [4]
- The whole hook: review refs by directory name, own retained-code refs, generations, copies, the report. [5]
- The report is written only inside the task. [6]
- Physical confinement: no symlink on the way, and the resolved path inside the resolved root. [7]
- The legacy identity by the trust line, and `task.json` read only when it is the task's own. [8]
- Generations released through their owners, or held. [9]
- A manifest naming another leaf, pin, repository or directory is held. [10]
- The F1 exact own-task rule and the retained-code refs it selects. [11]
- The content scan: confined root, confined candidates, knowledge schema, untracked. [12]
- The finalizer carries the report after the archive move, and never raises. [13]
- The main archive case and the colliding-task case. [14]

### Cross-Repo References

The hook deletes refs only in the two repositories the archived task's series contract names; a manifest's
repository is only compared against them.

No cross-repo boundary is crossed by this file.
