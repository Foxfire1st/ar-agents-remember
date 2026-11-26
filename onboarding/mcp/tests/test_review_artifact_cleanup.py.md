# mcp/tests/test_review_artifact_cleanup.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R25 rule 5 cases: the archive hook deletes only the archived
task's own review artifacts, and a repeated attempt keeps its receipts.** The `task`
fixture is a coordination task root with its task document and one leaf enclosure contract, a plain code and a
plain memory repository and no converted-memory fixture. The hook inspects refs, manifests and file content, including SQLite datasets. The core cleanup and ownership cases assert what another task still holds. Cache-only cases assert the addressed task’s preview, deletion, remainder and receipt replay. The file is self-contained (no shared
support module).

## Code Commentary

### Logic

- The dry run lists the review refs and dataset copies and checks that the first snapshot still
  exists. The apply runs through the finalizer’s `_with_review_artifact_cleanup` with the cleanup
  port bound. The task's review ref under its directory name (both repositories), its own legacy
  retained-code pin, the knowledge dataset at `knowledge/after/snapshot.sqlite` and a renamed copy (`pub2.sqlite`, found by content) are
  deleted. A review ref under the `task.json` ID, the two colliding pins, another task’s review ref,
  and a non-knowledge SQLite file survive. The test reads the persisted receipt back and checks
  its `reviewRefs` and empty failure list.
- **Identity (rulings 23:15:34 F1, 00:08:39, 02:12:06, 02:32:42):** colliding task ids never select each other's
  pins (parametrized over `260906-IAS`/`260906-ias-memory-recovery-l01` and `260928-MIK`/`260928-mik-extra-l01`); a
  comparison record naming another task never widens the archive; a `task.json` naming another task touches none
  of its refs; a planted leaf contract never reaches another task's review refs (V10; the legacy `other-1-l1` pin
  follows the trust line).
- **Missing repository and refused release (F2, F3).** The cleanup report lists both failures. The
  refused generation retains its pin and snapshot. The finalizer also reports an injected hook
  exception after archival.
- **Provable ownership (ruling 01:00:07):** a planted foreign manifest releases nothing — four parametrized cases:
  a foreign leaf, a foreign pin, a foreign repository, and a snapshot path escaping its directory.
- **Physical confinement (ruling 01:37:42):** the content scan never follows a symlink out of the task; a
  symlinked `notes` root is neither scanned nor written (`reportPath` null); a symlinked generation directory
  releases nothing and writes no `deletions/` outside.

- **Receipts per attempt:** `test_a_repeated_attempt_keeps_receipts_never_leaves_the_name_empty_and_reports_absence`
  runs the hook three times: an initial cleanup, a no-op replay, and a later cleanup with new work. The first attempt writes receipt 1 with an empty `alreadyAbsent`. A second attempt with nothing
  new returns `receipt: "unchanged"`, writes no numbered copy, leaves the canonical bytes alone, and lists the ref the
  first attempt deleted as `alreadyAbsent`. A later attempt with real work keeps the first receipt as
  `review-artifact-cleanup.attempt-1.json`, writes attempt 2 under the canonical name, and the canonical name existed
  at the moment of the atomic replace.

- **Cache class through receipts:** the `arCaches` cases prove an interrupted cache deletion replays as attributed absence, a cache-only dry run shows its remainder and preview, review refs, dataset copies and caches share one receipt recovery, and the fixture cache remains when the initial receipt cannot be written.

### Conventions

- `_owners` patches `read_manifest` and the two reclamation owners where a case plants a manifest and observes
  whether an owner was called; the refs and files are real.

### Invariants And Boundaries

- The fixtures check task-scoped ref selection and filesystem confinement. Refs belong to the
  supplied disposable code and memory repositories. The ordinary dataset scan stays inside the
  task root, and the explainer case uses its own confined environment root.

### Todos

No additional work is asserted by this card.

The pinned planned-key set includes `frameRevisions`.

The planned receipt classes include `explainerArtifacts`. The interrupted archive fixture leaves the external workspace, old generation counter and old lock absent. The case documents workspace removal as retirement's step before the sweep; the retry asserts `interrupted=true` `alreadyAbsent` entries of that class for the migrated `seat-generation` counter path and the old lock path. It does not assert a workspace entry in that retry receipt.

## Retained Full-Card Audit Context

The following distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe that recorded epoch. They add no fresh execution, mutation result or acceptance. Historical numeric reference labels are custody text and do not select live sidecar anchors.

### Split ruling

Summary of the earlier card account:

> Split out of `test_review_git_trees.py` by ruling 2026-09-30T02:32:42.

### Self-contained change-scope account

Summary of the earlier card account:

> The earlier card recorded this file as self-contained (no shared support module), and therefore recorded its catalog as unchanged.

“Unchanged” describes that prior change, not an inference about every later catalog revision.

### Frame-revision addition and earlier fail/pass account

Summary of the earlier card account:

> The pinned planned-key set now includes `frameRevisions`, the archive class MIK-R103 rule 8 adds; the case fails on the previous set and passes on this one.

The previous-set failure and current-set pass are the earlier card’s attributed account. This audit performed no test or mutation run; the frozen source still includes frameRevisions in its asserted planned set.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` lives outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The plain task fixture with its leaf contract and two repositories. [1]


- The main archive case. [2]


- Colliding task ids. [3]
- A record, a task document, or a planted leaf contract never reaches another task's refs. [4]


- The cleanup reports a missing repository and a refused release. The refused pin and snapshot remain. The finalizer reports an injected hook exception. [5]


- A planted foreign manifest releases nothing. [6]
- Symlinks: the scan, the notes root, the generation directory. [7]

### Cross-Repo References

The cases use two disposable repositories and a temporary coordination root.

### Repo-Internal References (continued)

- A repeated attempt reports what is already absent, keeps the first receipt as attempt 1, and writes none when nothing is new. [9]

- The interrupted archive fixture removes the workspace, old generation counter and old lock. After retry the migrated seat-generation counter path and old lock path have interrupted alreadyAbsent explainerArtifacts entries. The test does not require a workspace receipt entry. [11]

- The receipt's planned-key set carries the frame-revision class. [10]

- The `unit-regression` lane selects `mcp/tests/test_review_artifact_cleanup.py`. [8]
