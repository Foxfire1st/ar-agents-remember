# mcp/tests/test_lifecycle_finalize.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Lifecycle finalization of a leaf and immediate parent row: a leaf that names its master, and (since MIK-R38) a
leaf that names none and is listed by its folder's `task.json` master.

## Code Commentary

### Logic

Finalization marks the leaf Completed and its parent subtask row Completed, records the finalization decision and leaves the master inProgress. Failure while publishing the second document rolls back the leaf, parent and their rendered files to exact previous bytes.

**Fixtures (260928-MIK-L38).** The contract and document builders moved to the base class `_FinalizeFixtures`: a
landed, cleaned leaf contract (`_contract`, whose `fixture_name` keeps subtests apart), `_docs` (a folder master plus
the leaf; `leaf_master`, `rows` and `master_status` vary the pair), `_leaf_doc`, `_folder_doc` (the folder's
`task.json` as a master, or a non-master document in its place) and `_set_leaf_steps`. `_row` builds a master row and
`_sources` captures each document's JSON and rendered Markdown bytes, so every refusal can assert that nothing was
written.

**`LifecycleFinalizeTests`** keeps its two named-master cases unchanged and gains the parent-side placement case
(ruling 2026-09-30T13:35:32): a leaf naming a hand-made master `other.json` is refused with "`<other.json>` would be
rewritten to `<task.json>`", and the leaf, `other.json` and the series master are byte-identical afterwards.

**`FolderMasterFinalizeTests`** (MIK-R38; every leaf has `master: null`):
- the listing folder master's row completes, a second open row stays `inProgress`, and a `Completed` master is
  demoted to `inProgress` (behaviours 1 and 2);
- a dry run reports `would-update` with the resolved `task.json` and row `14`, accepts the caller's matching
  assertions, and writes nothing (behaviour 5);
- no `task.json`, a master without the leaf's row, and a `light` leaf that is itself the `task.json` each finalize
  standalone with the parent `skipped` and the master untouched (behaviour 3, three subtests);
- a non-master, an unreadable `task.json`, a duplicate row, a row pointing elsewhere, an asserted other master and an
  asserted master without the row are each refused as `task-document-resolution-blocked` with the named-master text
  (or the named cause) and no bytes changed (behaviour 4 and review R1 notes 2 and 4, six subtests);
- a hand-made `light` leaf `14_finalize.json`, which the store would write as `task.json`, is refused before any
  write (review R1 finding 1).

The worker and both review rounds removed each guard in turn; every removal failed at least one of these cases, and
the base build fails the folder-master cases while passing the standalone ones.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Child completion does not automatically complete the master. Document publication is atomic across the affected pair and is not a replacement for lifecycle acceptance.

The module sits in the integration lane with the existing finalize cases (ruling 2026-09-30T12:33:07 Q1), because
finalize publishes through the task transaction. Every refusal case compares the documents' bytes before and after,
so a refusal that wrote anything fails.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Finalized updates leaf and immediate parent row. [1]
- Second document publish failure rolls back leaf and parent. [2]
- The shared fixtures: the landed contract, the folder master and leaf pair, and the byte capture. [3]
- A named master the store would write elsewhere is refused before any write. [4]
- The folder master's row completes under the demotion rule. [5]
- A dry run reports the folder master's row and accepts its assertion. [6]
- Without a listing folder master the leaf finalizes standalone. [7]
- A folder master is refused exactly as a named master, before any write. [8]
- A leaf the store would write elsewhere is refused before any write. [9]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
