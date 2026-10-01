# mcp/tests/test_record_integrity.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository: `system/sources.md`
carries no entries, so no `Domain Documentation` category is available to cite. These are
repository-owned fixture and assertion contracts; no external library behavior is inferred.

External domain documentation is not configured in this memory root.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above.
The historical evidence lives under task roots in the coordination tree and in the memory
repository's revision `e116e5ee`, and is cited by the source that reads it rather than linked as
durable memory. Every range was derived against the current 1140-line source.

- The historical case for the leaf/contract comparison and for D42's class. [1]
- This master, whose contracts and documents agree, read through a frozen register snapshot. [2]
- The two leaves the frozen snapshot declares, and their count. [3]
- The revision that committed T45's stale figures, and the two route documents it carried. [4]
- The two labels spelled so neither can match the tail of the other's name. [5]
- The coordination root the session was told about, or a named skip rather than a silent pass. [6]
- Task roots are copied into a disposable coordination tree, so the real tree is only read. [7]
- The bytes a named revision committed, written out so the case reads history rather than the tree. [8]
- The register snapshot that carries R11's arrows by construction, so the case cannot assert the world's defect count. [9]
- The frozen leaf world every live-state case now reads: declared documents, pruned leaves, reduced rows. [10]
- The historical master fails as required and this master passes, with both populations stated. [11]
- The rule D42 crossed, pinned from both sides of the step-completeness conjunct. [12]
- Only the State cell is graded, and a master with no leaf set refuses. [13]
- A prose figure is compared with its source at the revision the prose describes. [14]
- Every comparison states its two populations, and the CLI writes nothing. [15]
- The module whose four comparisons these cases pin. [16]
- The lane this module is registered in, so the fail-closed manifest admits it. [17]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository
allowance is empty and no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
