# dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The knowledge reader's explorer (MIK-R29 rule 1): the repository's directories and files at the selected
memory tree, one level per read, each child with its knowledge entry count.** A path known only to the
onboarding mirror (a card whose code is gone) is listed and marked "(onboarding only)"; a code tree that cannot
be listed is named, and the onboarding mirror is still shown.

## Code Commentary

### Logic

- **Lazy levels.** `useTreeLevels` asks one `tree` read per opened directory (the root `''` and the ancestors of
  the current path are open from the start) and keeps each level's answer, loading state or failure.
- **Stale answers dropped (ruling 2026-09-30T09:42:58, F13).** Each read remembers the (repository, memory
  tree) it was asked for; an answer that lands after either changed is another tree's listing and is dropped,
  and the levels are reset on a switch.
- **Rows.** `TreeNode` shows the toggle for a directory, the name (the current path highlighted), the entry
  count, and "(onboarding only)" when `inCode` is false. It only descends into a child that lies below its
  directory, so a listing that says otherwise is never followed.
- **Failures named.** `TreeLevel` shows a failed level's detail (`tree-unavailable`) and, above a listed level,
  the code side's state when it is not `listed` (`tree-code-unavailable`), for example a commit with no
  `Code-Commit` trailer.
- **Navigation.** Clicking a name calls `onOpen`, which the panel turns into a path address (a URL change); the
  repository row opens the root summary.

### Conventions

- Panda CSS owns the looks; the tree is a `nav` labelled "Repository paths".

### Invariants And Boundaries

- An unlisted code tree is named, never shown as an empty directory.
- Proved by the dashboard's navigation case (explorer counts, clicks change the hash) and the stale-answer case
  (the pinned commit's listings held, the selector switched back, then released: nothing lands); removing the
  guard fails it.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component's own statement of the explorer. | "The reader's explorer (MIK-R29 rule 1)" | dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx:1-4 |
| One read per opened level; an answer after a switch is dropped (F13). | `useTreeLevels` | dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx:46-71 |
| A row: toggle, name, count, "(onboarding only)"; descends only below its directory. | `TreeNode` | dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx:105-132 |
| A level, with a failed read and an unlisted code tree named. | `TreeLevel` | dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx:134-156 |
| The explorer, with the current path's ancestors open. | `KnowledgeTree` | dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx:158-202 |
| The stale-answer case. | "names side reads that failed, pins a clean published view, and drops stale explorer answers" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:455-455 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new explorer MIK-R29 adds, recording ruling 09:42:58 F13 (stale answers after a commit switch are ignored). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
