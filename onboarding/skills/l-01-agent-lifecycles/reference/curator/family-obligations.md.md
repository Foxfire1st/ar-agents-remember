# skills/l-01-agent-lifecycles/reference/curator/family-obligations.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for deciding family coverage and updating a family: the joint guarantee, membership judgment, authored history and readback.

## Code Commentary

For each scoped obligation the Curator decides whether evidence and project intent justify a joint obligation; where they do, a `family` record with its own guarantee, members, routes and admission is authored in the same list's `records` section. An obligation may belong to several families, and grouping merely by directory, route, label or shared anchor is never a family. A member or membership change requires a fresh examination of the recorded guarantee; the stored family changes only when justified, and its worklist item is answered with a history row saying what was examined. Implementation alone never rewrites member intent or a record's meaning. A restated guarantee is a `changed` history row with the Curator's authored `effect`, and the writer fills the family's revision. After authoring, `knowledge_read` with `view="family"` over the leaf's memory worktree and the Curator's own file reads confirm the result, and authored, updated, examined and unchanged families go into the handover. Unattributed code locations named by the task's prepared context are attributed to a family or explained.

## Evidence

- Families are authored from evidence and intent, never from directory, route, label or anchor grouping. [1]
- Membership changes trigger re-examination and a history row; restated guarantees are `changed` rows with an authored effect. [2]
- Families are read back with `knowledge_read` and every unattributed prepared location is attributed or explained. [3]
