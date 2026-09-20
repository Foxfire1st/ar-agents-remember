# mcp/tests/test_record_integrity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_record_integrity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:58+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l3-ar` uncommitted source (this file was L2's addition and is now **1140 lines, 37 cases**, sha256 `86c785b4eea752a55fe41885c850466e584eb39379b7658b9916e74fd8c6cc47`, 55,356 bytes); base `a12c511f6e76bd1188719cad0a9104d78d46920c` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pin the four comparisons of
`mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py` against the
historical artifacts they were written for, in **both** directions: the shipped function must FAIL on
the artifact as it stood when the drift was live, and PASS on the artifact that replaced it. A check
asserted only in the refusal direction cannot be shown to be non-vacuous, which is the fault the
sibling `instrument_discipline.py` exists to catch.

Three artifacts are read from the record rather than reconstructed, and each is named in its case:
`260712_task-reader-body-priority-rc5` (seven leaves, every contract `completed/completed`, every
document still `planning`/`inProgress`, and a master whose rows read `Completed` over them);
`260918_tool-surface-and-process-integrity` (this master, whose contracts and documents agree); and
the memory repository's own revision `e116e5ee`, which carries `T45`'s two route documents as they
stood while they stated `instrument_discipline.py` at 361 lines and `test_instrument_discipline.py`
at 350 lines / 16 cases.

The control worlds are built by **copying** those task roots into a temporary directory, so the real
coordination tree is only ever read. When the tree is not reachable the cases that need it **skip
with the reason named** rather than passing on a fixture that no longer resembles the artifact.

## Code Commentary

### Logic

**Thirty-seven cases, measured on this candidate rather than carried.** The file defines **37
`def test_` methods** in five classes and no module-level case, with **0** parametrisations, and
`pytest --collect-only -q` reports **`37 tests collected`** — so the collected count and the defined
count are the same 37. The file was 599 lines / 27 cases when the worker delivered it, 911 lines /
35 cases after the first repair round, and 1000 lines / 37 cases when L2 curated it; **L3's repair
round rewrote the four live-state sites and left the case population alone, so this card is written
against the current 1140 lines / 37 cases.**

- `LeafDocumentAgainstContractTests` (257-357), **5 cases** — the historical master's seven
  disagreements are reported with both populations stated; this master's two contracts and two
  documents agree at zero; the tolerant `L<n>` key is shown to find what the strict spelling
  under-reports; a contract with no leaf document is **counted rather than failed**; and a document
  reading `Completed` before its closeout has started is a finding, not a count.
- `MasterRowAgainstLeafDocumentTests` (360-560), **7 cases** — the historical master's rows read
  `Completed` over unlanded documents; this master's rows agree with their documents **at the
  declared leaf count** rather than at the live one; the boundary `D42` crossed is pinned from
  **both** sides by `test_a_row_is_never_completed_on_step_state_alone` (every step marked, document
  not landed → the row is `inProgress`) and
  `test_a_completed_document_with_an_open_step_is_not_completed` (the document reads `Completed`
  while one of its own steps is open → still `inProgress`); an abandoned leaf stays abandoned; and
  the two reported halves —
  `test_a_row_completed_without_its_document_is_reported` (464) and
  `test_a_row_completed_over_a_document_with_an_open_step_is_reported` (509) — reach the finding
  through the step-completeness conjunct rather than through the status, which is the half the
  sibling case cannot reach.
- `RegisterOwnerArrowTests` (563-665), **5 cases** — this master's register is reported with its
  arrow count stated **against the declared leaf set**, so the count the next leaf moves cannot red
  the case; a register whose arrows all resolve is clean; an arrow to an undeclared leaf is reported
  with **both** sets; only the State cell is graded, pinned as the reason the Owner cell is not; and
  a master with no leaf set **refuses** rather than reporting a zero.
- `DeclaredFigureCurrencyTests` (668-1012), **12 cases** — the two shapes are measured from the source
  rather than declared by the test; the historical route documents are read **by Git object** at
  `e116e5ee`; a correct pair of figures is not a disagreement; a stale prose figure is reported
  against the current source; a correction sentence is graded at the value it corrected *to*; a
  figure in frontmatter is not a body claim; an unknown shape and an unresolvable base commit and a
  source outside any Git tree each **refuse** rather than zero; the corrected prose passes; a bare
  line count belonging to another file is not this source's figure (the case that pins the first
  run's fault, where a pattern of `\d+ lines` alone matched twelve counts, eleven of them other
  files' sizes); and a claim scoped to one document does not grade another.
- `RecordIntegrityReportTests` (1015-1140), **8 cases** — every comparison states its two populations;
  *"said what it compared"* reads as the comparison rather than as a status; the CLI names its input
  when none is supplied and refuses a root carrying no `tasks/` tree; the CLI runs from a task root
  **and writes nothing**; a clean world exits zero; the prose-figure check runs from the task root and
  writes nothing; and a figure claim that cannot be read **refuses rather than being skipped**.

`_coordination_root` (80-92) is the reason the record-reading cases behave as they do: with
`AR_COORDINATION_ROOT` unset the default resolution is `REPO_ROOT.parents[1] / "ar-coordination"`,
which inside a worktree is a path that does not exist, so those cases **skip**. Fourteen cases read
the record, and a seat that runs the suite without the variable gets a green that says nothing about
the record.

### Conventions

The three world-builders are shared and each says why it is a copy: `_task_root` (95-99) skips when
the artifact is absent, `_control_world` (102-109) copies whole task roots into a disposable
coordination tree, and `_memory_repository` (112-117) skips when the memory repository is absent.
`_frozen_document` (120-141) writes out the bytes a **named revision** committed, because the working
tree moves under a test and then the test lies about what it measured; it indexes the two route cards
so two documents sharing a basename really are scanned as two. `_frozen_register_snapshot` (144-254)
replaces the copied master's register with a snapshot that carries `R11`'s `→ L20` arrows **by
construction** — pinning the live register would make the case assert the world's defect count, so
repairing the world would turn the suite red precisely when the check it protects is right.

**`DECLARED_LEAVES` / `DECLARED_LEAF_COUNT` (56-60) and `_frozen_leaf_snapshot` (218, with
`_write_declared_document` 165, `_prune_to_declared_leaves` 179 and `_reduce_to_declared_rows` 205)
are L3's repair of `T51` by class.** The register snapshot above froze one construct; the *other*
reads of the live, growing master were not frozen, so four cases were green only while this master
had the leaf population they were written for: the subject count, the unmatched-row verdict, the
register's `authority` count and the CLI's clean-world exit. The snapshot prunes the copied master to
the two leaves L1 and L2 landed, writes their document statuses, and reduces the master's rows to
them, so every count and verdict in the four cases is the case's own. **It is a repair of a fixture,
not of a check**: the checks' real claims held while the counts failed — `result.ok` was true and only
the hard-coded population was wrong.

The two prose labels are spelled so neither can match the tail of the other's name: `INSTRUMENT_LABEL`
(76) carries a lookbehind because a bare `instrument_discipline\.py` matches inside
`test_instrument_discipline.py`, which would credit the suite's own figure to the module the suite
tests. Assertions state subject and authority counts alongside the finding, so a case cannot pass by
being zero for the wrong reason.

### Invariants And Boundaries

- **Both directions, every comparison.** A refusal-only case shows a function rejects something; only
  a paired acceptance case shows it would have passed a good artifact.
- **A finding case asserts the finding's own sides**, not merely that something was reported —
  `declared`, `measured` and `rule` are matched, so a case cannot pass by being refused, or reported,
  for the wrong cause.
- **The evidence is read from the record or the case says it skipped.** The historical task roots are
  **copied**, not reconstructed; the `T45` documents are read by Git object at a named revision; and a
  missing artifact is a named skip.
- **The suite never writes into the tree it measures.** Every writer takes `tmp_path`, and both CLI
  cases assert that a run from a task root leaves the tree unchanged. That rule is in the file because
  its first draft violated it: six fixture documents written through **relative** paths landed in the
  repository root, and the regression case asserting *"the check wrote to the tree it measured"*
  passed the whole time, because it compared a temporary tree that was never the victim.
- **A case does not pin live mutable state.** `test_record_integrity.py`'s own history is the proof,
  in two rounds. The first version asserted `result.disagreements == 5` against a copy of the **live**
  register, so repairing the register's six `→ L20` arrows made it `1 failed, 26 passed` with the
  environment variable set — and in the default lane the case **skipped**, so the failure was
  invisible; L2's `_frozen_register_snapshot` replaced it. **The second round is `T51`, and it is the
  same lesson applied to the class rather than to the instance:** L2's repair froze the register and
  left the other reads of the live master, so L3's own enclosure moved the subject count, the
  unmatched-row verdict, the register's `authority` count and the CLI's clean-world exit. All four now
  read `_frozen_leaf_snapshot`'s declared world. A fixture that asserts a live population is green
  exactly while the world happens to match it.

### Todos

None. This card was written by reading the current 1140-line source and by measuring the case
population on this candidate; no case in this file is known to be vacuous, and no case was added or
removed by the curator. **One consequence of `T51` stays open for the leaf that next touches this
file:** a case that reads the live master must take its population from `_frozen_leaf_snapshot`, and
the fixture's `DECLARED_LEAVES` is a second place the master's leaf list is written, so a leaf that
lands a contract must expect to update it. That is a deliberate, visible cost of freezing the world
rather than a defect.

## Docs References

No external Domain Documentation source is configured for this repository: `system/sources.md`
carries no entries, so no `Domain Documentation` category is available to cite. These are
repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured in this memory root. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above.
The historical evidence lives under task roots in the coordination tree and in the memory
repository's revision `e116e5ee`, and is cited by the source that reads it rather than linked as
durable memory. Every range was derived against the current 1140-line source.

| Finding | Anchor | Source |
| --- | --- | --- |
| The historical case for the leaf/contract comparison and for D42's class. | `HISTORICAL_MASTER` | mcp/tests/test_record_integrity.py:49-49 |
| This master, whose contracts and documents agree, read through a frozen register snapshot. | `CURRENT_MASTER` | mcp/tests/test_record_integrity.py:51-51 |
| The two leaves the frozen snapshot declares, and their count. | `DECLARED_LEAVES`; `DECLARED_LEAF_COUNT` | mcp/tests/test_record_integrity.py:56-60 |
| The revision that committed T45's stale figures, and the two route documents it carried. | `T45_FREEZE`; `T45_ROUTE_DOCUMENT`; `T45_SUITE_DOCUMENT` | mcp/tests/test_record_integrity.py:63-67 |
| The two labels spelled so neither can match the tail of the other's name. | `INSTRUMENT_LABEL`; `SUITE_LABEL` | mcp/tests/test_record_integrity.py:76-77 |
| The coordination root the session was told about, or a named skip rather than a silent pass. | `_coordination_root` | mcp/tests/test_record_integrity.py:80-92 |
| Task roots are copied into a disposable coordination tree, so the real tree is only read. | `_control_world`; `_task_root` | mcp/tests/test_record_integrity.py:95-109 |
| The bytes a named revision committed, written out so the case reads history rather than the tree. | `_frozen_document` | mcp/tests/test_record_integrity.py:120-141 |
| The register snapshot that carries R11's arrows by construction, so the case cannot assert the world's defect count. | `_frozen_register_snapshot` | mcp/tests/test_record_integrity.py:144-254 |
| The frozen leaf world every live-state case now reads: declared documents, pruned leaves, reduced rows. | `_frozen_leaf_snapshot`; `_write_declared_document`; `_prune_to_declared_leaves`; `_reduce_to_declared_rows` | mcp/tests/test_record_integrity.py:165-254 |
| The historical master fails as required and this master passes, with both populations stated. | `LeafDocumentAgainstContractTests` | mcp/tests/test_record_integrity.py:257-357 |
| The rule D42 crossed, pinned from both sides of the step-completeness conjunct. | `MasterRowAgainstLeafDocumentTests` | mcp/tests/test_record_integrity.py:360-560 |
| Only the State cell is graded, and a master with no leaf set refuses. | `RegisterOwnerArrowTests` | mcp/tests/test_record_integrity.py:563-665 |
| A prose figure is compared with its source at the revision the prose describes. | `DeclaredFigureCurrencyTests` | mcp/tests/test_record_integrity.py:668-1012 |
| Every comparison states its two populations, and the CLI writes nothing. | `RecordIntegrityReportTests` | mcp/tests/test_record_integrity.py:1015-1140 |
| The module whose four comparisons these cases pin. | `check_leaf_document_against_contract`; `check_master_rows_against_leaf_documents`; `check_register_row_ownership`; `check_declared_figure_currency` | mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py:441-955 |
| The lane this module is registered in, so the fail-closed manifest admits it. | "mcp/tests/test_record_integrity.py" | mcp/tests/test-evidence-lanes.toml:305-305 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository
allowance is empty and no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_record_integrity.py" repointed to mcp/tests/test-evidence-lanes.toml:305-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_record_integrity.py" repointed to mcp/tests/test-evidence-lanes.toml:248-248. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T14:58+02:00 — 260918-TSIP-L3 curator (uncommitted change set on `ar/260918-tsip-l3-ar`,
  base `a12c511f`): this file is one of the leaf's five changed paths — **L2's landed test module,
  changed deliberately** — so the card gained a **body** update rather than a restamp. The repair
  round rewrote the four live-state sites by class (`T51`) and added `DECLARED_LEAVES` /
  `DECLARED_LEAF_COUNT` and the four helpers behind `_frozen_leaf_snapshot`; the case population is
  unchanged at **37 cases** and the file is **1000 → 1140 lines**. Recorded: the new fixture and what
  it freezes, why the repair is of a fixture rather than of a check (`result.ok` held while the
  hard-coded population failed), that the four cases' counts are now the case's own, and the one
  standing cost — `DECLARED_LEAVES` is a second place the master's leaf list is written, so the leaf
  that lands a contract must expect to update it. **All thirteen retained citation rows were
  re-derived against the new bytes**: eight moved with their prefix intact and six were re-scoped
  because an insertion now lies inside their extent (the shape the shipped citation fixer declined on
  L1), each new boundary verified to hold exactly the line its old boundary held; one row was added
  for `DECLARED_LEAVES`. The card's prose ranges were re-derived in the same pass — the six other
  numbers in `Logic`/`Conventions` moved with the classes they name, and stale in-prose figures are
  invisible to `range_resolution` and `claim_reopen` alike (`T45`), which is why they were grepped
  rather than assumed. `lastUpdated` advances with this body edit; `lastVerifiedCommitHash` /
  `lastVerifiedCommitDate` are deliberately unchanged because the candidate is uncommitted and the
  governed closeout owns the real code commit.
- 2026-09-18T13:39+02:00 — 260918-TSIP-L2 curator (uncommitted change set on `ar/260918-tsip-l2-ar`,
  base `d9becade`): created this card for the new test module the leaf added, so the source file has
  its 1-to-1 onboarding pair before closeout. The case count was **re-measured on this candidate**
  rather than carried from any report: `grep -c '^    def test_'` = **37** class methods, `grep -c
  '^def test_'` = **0** module-level cases, `pytest --collect-only -q` → **`37 tests collected`**, so
  collected and defined agree. The card states the file's own two revisions rather than hiding them:
  599 lines / 27 cases as delivered, 911 / 35 after the first repair round, **1000 / 37** here. Two
  behaviours are recorded because they are the ones a reader of this suite most needs: fourteen cases
  read the record and **skip** without `AR_COORDINATION_ROOT`, and the `T45` documents are read by Git
  object at `e116e5ee` rather than from a working tree that moves. `lastUpdated` tracks this body
  edit; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are left at the leaf's frozen code base
  because the source is an uncommitted candidate and the governed closeout owns the real code commit.
  This seat writes no source and ran no product test beyond read-only collection.
