# mcp/tests/test_memory_citation_agreement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_agreement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T05:10+02:00 |
| lastVerifiedCommitHash | `4346e6979a9bb628bd07bd83957917e1b157f32b`|
| lastVerifiedCommitDate | 2026-09-20T15:23:19+02:00|
| reviewedWorkingCandidate | `260918-TSIP-L12` uncommitted source, **1124 lines / 35 cases**, sha256 `34db6ea729d58833…`, on base `15e100846a7ec984714580470d7f6985a425fcc4` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

**The stamp names the base, not the bytes, and the distinction is deliberate.** This file is new
in `260918-TSIP-L7` and **no commit yet carries its content**, so `lastVerifiedCommitHash` names
the commit the working candidate was cut from rather than one that contains this source; it does
not claim the uncommitted content was verified at that commit. The `reviewedWorkingCandidate` row
names the exact candidate and its digest, and the governed closeout owns the real stamp. Every
claim below was re-read against the module's current bytes in `260918-TSIP-L12`.

## Purpose

The two agreement classes the memory layer's own checks cannot see, kept green by cases rather than
by a report. **`T52`** is a construct that moved *inside* its cited range: `range_resolution` asks
whether an anchor **occurs** in a cited range, and a construct's name occurs at every call site, so a
range the definition has left stays green for as long as anything inside it still spells the name.
**`T45`/`T56`** is a case budget written in prose: no checker reads a prose numeral against the file
that declares it, so a route overview can advertise a budget the repository stopped declaring and
every check stays green.

This module is the durable form of the `260918-TSIP-L7` agreement leaf, extended by
`260918-TSIP-L12` when the master-end review falsified its own acceptance pins. It pins four
populations and one census: the product change the leaf lands (a report-only
`citation_anchor_definition_outside_range` finding, plus GFM's `\|` escape resolved where cell text
becomes anchor text), the live populations of both classes as **exact equalities** — including the
**enforced** population, which is **97 and inherited from the merged `260915_knowledge-substrate`
line**, not this master's — the classification of every stale budget figure the sweep found, the
superseded-pair worklist **derived from the tree** rather than remembered, and the census of
qualified `## Update History…` headings. A pin asserted in both directions is the point: a repair
that is not carried into the pin fails the suite, and a new stale site fails it until it is
classified.

## Code Commentary

### Logic

Seven classes, 35 cases, `unittest.TestCase` throughout, no `pytest` marks.

- **`T52`, the mechanism** (`DefinitionOutsideCitedRangeTests`, `:367-483`). The world is the measured
  shape reduced to its smallest form: a construct defined at `mcp/sample.py:20-21`, a **call** to it
  inside `:5-12`, and a claim citing `:5-12` for the construct's name. The membership test is
  satisfied by the call, so the claim reads current while pointing at the wrong lines
  (`test_the_moved_range_is_reported_and_stays_a_report`, `:394-407`). Three negatives bound it: a
  corrected range clears it (`:409-418`), an ambiguous anchor is not reported (`:420-431`), and a
  non-`SYMBOL` anchor has no definition to be outside of (`:433-474`) — the last pinning the **fact**
  the redundancy rests on rather than the redundant guard.
- **`T57`, the escape** (`EscapedPipeAnchorTests`, `:486-579`). A literal pipe in a GFM table cell must
  be written `\|`, so `` `useEffect(cb, [a \| b])` `` reached the anchor grammar carrying a character
  the source does not have and was silently counted as an *unchecked span* — reading as checked and
  not being checked. Seven cases cover the code-span anchor, the same escape in the **Source** cell, a
  **quote** anchor, and the documented bound: `unescaped` is one literal `\|` → `|` replacement, so
  with two backslashes the second is the one consumed and the source's `a | b` stays unmatched, which
  is GFM's own reading.
- **`T58`, the population the fixer can only count** (`WrappedCitationPopulationTests`, `:582-695`). A
  wrapped `cit:` is parsed by the checker (it joins the paragraph) and counted by the fixer in
  `claimsNotOnOneLine`, and the fixer can rewrite none of them. The detector is proven by planting the
  shape in a temporary document (`:617-625`) so the zero it reports over the repository is a measured
  zero rather than an instrument that never fires.
- **The budget screen** (`BudgetAgreementTests`, `:698-936`). The declared pair is read from
  `pyproject.toml` at run time, never restated; the repaired sentence must state that pair; the
  declarations on `conftest.py` must register both names and state no value; the two stale-figure
  classes are counted separately; and the superseded-pair worklist is pinned as **the count
  `superseded_pair_sites` returns**, not as a literal.
- **`T112`/`F2`, the derivation itself** (`SupersededPairDerivationTests`, `:939-993`). Five hermetic
  arms prove the worklist rule fires: a live site outside history is counted (`:958-961`); the same
  line inside `## Update History` is not (`:963-969`); a qualified `## Update History…` heading cannot
  hide a live line (`:971-983`); the comma-grouped spelling of the superseded unit ceiling is
  counted, where a plain grep for the digits alone under-counts (`:985-988`); and the declared pair
  is not itself a site (`:990-993`).
- **`T125`/`F8`, the heading census** (`QualifiedHistoryHeadingTests`, `:996-1055`). The corpus writes
  `## Update History` and the checker accepts only that spelling, so a qualified title renders as a
  section boundary while every entry beneath it is invisible to the order check — and the corpus
  carried two with no diagnostic at all. Four arms: the detector fires on the backtick-mangled title
  (`:1029-1031`) and on a dated title (`:1033-1036`), an exact heading — and a deeper `###` one — is
  not reported (`:1038-1041`), and a live arm asserts the named tree carries exactly the pinned list.
- **The module's own boundary** (`RepoStateTests`, `:1058-1124`). The module under test is the working
  tree's, no memory tree is reached for by default, and no `subprocess` is used.

### Conventions

Every root is derived from `__file__` — `MCP_SRC`, `MCP_TESTS`, `REPOSITORY_ROOT` (`:43-58`) — and
**never from the working directory**, which is the rule register row `T102`(d) states: a
repository-root-relative path literal makes a suite's result a fact about the directory it ran in.
The live-population cases are **hermetic by construction**: with no `AR_ONBOARDING_ROOT` they **skip**
rather than reach for a checkout that may not exist on the machine running them
(`live_onboarding_root`, `:273-284`), and the mechanism cases build their worlds under
`tempfile.TemporaryDirectory`.

The lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:120-120`), so the module is in
the **default selection** and the unit population a full run collects — it is not an integration-only
or manually-invoked lane. **Five** live cases additionally require `AR_ONBOARDING_ROOT` to name a
memory tree (`:661`, `:777`, `:883`, `:904`, `:1045`); without it they skip, and the mechanism cases
still enforce the behaviour they count. **A green lane run is therefore never evidence that the pins
hold** — that sentence is in the module's own header, and it is the answer to `T122`'s trap.

### Invariants And Boundaries

- **The tree is a pair, and both halves are named.** Every live number is measured against the pair
  `260918-TSIP-L12` **lands**: memory `ec1cebe5` — the `260918_tool-surface-and-process-integrity`
  memory tip after its **third sync**, which merged the concurrent `260915_knowledge-substrate` line
  — plus this leaf's memory change set, paired with code `15e10084` plus this leaf's code change set.
  The **official** memory checkout is a different tree on a different commit and is refused by the
  product at `mcp/src/agents_remember/application/memory_tools.py:105-105` (called at `:140`). Naming
  one half of the pair without the other is the defect class (`T65`) this module exists to stop.
- **The pins' address is a commit pair, not a branch, and it took two corrections to get there**
  (`F3`). The header this module used to carry named a leaf worktree (`fd1a024e`) that a leaf finalize
  reclaims; the repair named the MASTER work branch `ar/260918_tool-surface-and-process-integrity`,
  which the master's own cleanup reclaims in turn (the register's `T89`). The branch that is now
  named is only *where the commit may be found*: it is written by another line besides this master
  and it moved three times while this leaf lived, changing the tree under the pins each time. **A red
  pin on a moved or merged tree is not a regression until it is re-derived on that tree** (`T122`,
  law 7 — a pin is a claim about a moment).
- **The pins are exact and pair-specific, and that is falsifiable.** `T52_DEFINITION_OUTSIDE_RANGE`
  **130** is a REPORT, never a gate: every row rides `reportOnlyFindings`, so it is counted, rendered
  and reviewed without entering `findingCount`. `T52_ENFORCED_POPULATION` **97** is the opposite
  kind of number and the module says so in words: it is **inherited debt**, 96
  `citation_anchor_absent_from_range` plus 1 `citation_range_out_of_bounds`, the sibling line's
  citation debt merged into this tree on 2026-09-20, and the same 97 register row `T141` measured
  independently (392 failing / 337 repairable / 55 declined tree-wide, 97 enforced remaining). A pin
  that asserts a debt must say so, and this one does: **a change in either direction is a finding** —
  DOWN means somebody cleared rows (name them), UP means somebody added them (find the landing and
  re-read the construct rather than the number). `T58`'s **3** constructs in **2** documents were
  re-measured on the merged tree and hold across the sync.
- **The superseded-pair constant is DERIVED, and that is `F2`'s repair.** `NON_HISTORY_SUPERSEDED_SITES`
  (`:758`, value **55**) is pinned against the count `superseded_pair_sites` (`:228-248`) returns, and
  that function is red when the defect grows and when the derivation stops seeing. The constant it
  replaces — `SUPERSEDED_DECLARED_SITES = 20` — was compared with its own literal, so **no change to
  any tree could move it**: a hard-coded fact wearing the clothes of a measurement, in the module
  written to enforce agreement (law 4). Its named producer read **64** outside `## Update History` on
  the very tree the module pinned, and `F1` of the master-end review is the class it was blind to.
  The worklist reads 64 at base, 47 once this leaf repaired the seventeen lines that stated the
  superseded pair as current, and **55** on the merged tree; the +8 is the sibling line's own budget
  prose. It is a **worklist, not a verdict**: each line is a dated or as-of reading reviewed row by
  row, and none is asserted to be wrong by being counted.
- **The qualified-heading census is a NAMED population, not a zero.**
  `QualifiedHistoryHeadingTests.QUALIFIED_HEADINGS` (`:1017`) pins one entry —
  `mcp/tests/overview.md:4833`, the sibling `260915_knowledge-substrate` line's dated heading, which
  arrived with the merge. It is pinned rather than repaired deliberately, and the reading behind that
  is recorded on the document: the heading is the corpus's **deliberate dated form**, structurally
  intact and the last of its kind in the tree, so `T125`'s ruling — *normalise only when the heading
  is accidental* — does not apply to it. The census case therefore reds when the population moves in
  **either** direction.
- **The tree is a worklist with two bounds, both measured.** `history_section_flags` (`:190-225`) uses
  the exact-title rule `update_history_sections` accepts, where the producer uses a prefix match; and
  it ends a section only at a level-2 heading where the product ends it at level ≤ 2. Measured on
  planted documents (`notes/reports/tsip-instruments/l12-sv3-bound.py`): against the **product** the
  worklist can *under*-count (a level-1 heading inside a history section), and against the **producer**
  it can *over*-count (a qualified heading) — the second direction is deliberate, because it is the
  one a mangled heading cannot blind. Neither bound is reached on the pinned pair.
- **The `T58` comment's second site is off by three lines.** The header names
  `models/worktree.py.md` line 99; the wrapped construct begins at **`:102`** (line 99 is the previous
  claim's anchor, line 100 its one-line citation). `service.py.md` `:30` and `:43` are exact. Nothing
  asserts the comment, so nothing fails — recorded so a reader following it lands on the construct.
- **The two zero-populations are `T58`'s and the repository's, and they are different files.**
  `test_the_repository_carries_none` (`:631-643`) walks the **code** repository's markdown and asserts
  `0`; the three wrapped constructs live in the **memory** tree and are counted by
  `test_the_live_memory_tree_matches_the_pins` (`:645-695`), which enumerates documents with the same
  detector rather than reading the fixer's own counter — a case that reads its subject's counter cannot
  falsify it.
- **The AST guard's name is wider than its set.** `test_this_module_shells_out_to_nothing`
  (`:1087-1120`) flags the attributes `run`/`system`/`popen`/`check_output`/`Popen`, the bare names
  `system`/`popen` and any `subprocess` import; `os.posix_spawn`, `os.exec*` and `os.spawn*` are
  outside it, which the successor verification demonstrated by mutation. No such call exists; the
  honest statement of the property is the narrower one, and this bound is register row `T114`.
- **Scope boundary.** The module proves the *mechanism* on trees it builds and *pins* the live
  populations; it does not repair them. The `T52` rows, the 97 enforced rows and the stale budget
  figures are worklists for the route curators, and the module's job is to make them move when they
  move.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only. The
comment-level findings above (`T58`'s second site, `T114`'s guard bound, `SV-3`'s two derivation
bounds) belong to whatever change next touches the module. `T138` — the tool reference's 20-row table
divergence — is registered and not this module's.

## Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and they
make no acceptance claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory tree the product refuses, cited at the definition rather than at the module header's old wrong line (`R2-3`, repaired). | `_refuse_official_memory` | mcp/src/agents_remember/application/memory_tools.py:105-105 |
| The world: a code tree and the memory tree that documents it, both under one temporary root, with the citation cache slot its census was built in removed. | `World` | mcp/tests/test_memory_citation_agreement.py:287-356 |
| The live tree, named by the run and skipped when no run names one. | `live_onboarding_root` | mcp/tests/test_memory_citation_agreement.py:273-284 |
| The `T52` REPORT-ONLY population pin, re-derived on the pair this leaf lands: **130** rows over 95 documents. It is a report and not a gate, and the rows that moved it are named at the constant. | `T52_DEFINITION_OUTSIDE_RANGE` | mcp/tests/test_memory_citation_agreement.py:159-159 |
| The ENFORCED population on the same tree: **97**, which is the merged sibling line's inherited debt rather than this master's, so the check reports `ok: false` and the module says so. A change in either direction is a finding. | `T52_ENFORCED_POPULATION` | mcp/tests/test_memory_citation_agreement.py:160-160 |
| The `T58` pins, derived by enumeration rather than from the fixer's counter, re-measured on the merged tree. | `T58_WRAPPED_CITATIONS`; `T58_WRAPPED_DOCUMENTS` | mcp/tests/test_memory_citation_agreement.py:161-162 |
| The `T52` shape: green membership, definition outside the range, one report-only finding. | `DefinitionOutsideCitedRangeTests` | mcp/tests/test_memory_citation_agreement.py:367-483 |
| The negative that makes the check a check: a corrected range clears it. | `test_a_corrected_range_clears_it` | mcp/tests/test_memory_citation_agreement.py:409-418 |
| The escape resolved where cell text becomes anchor text, which is where the `T57` blind spot was. | `unescaped` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:40-53 |
| Both cells and the quote path: the escaped spelling must yield the anchor the plain spelling yields. | `EscapedPipeAnchorTests` | mcp/tests/test_memory_citation_agreement.py:486-579 |
| The wrapped-`cit:` detector, proven by a planted shape so the corpus zero is measured. | `wrapped_constructs` | mcp/tests/test_memory_citation_agreement.py:602-614 |
| The code repository's own markdown, enumerated: zero wrapped constructs is the pin. | `test_the_repository_carries_none` | mcp/tests/test_memory_citation_agreement.py:631-643 |
| The live case: `T52` 130, enforced 97, `T58` 3 constructs in 2 documents, on the pair. | `test_the_live_memory_tree_matches_the_pins` | mcp/tests/test_memory_citation_agreement.py:645-695 |
| Every stale site the sweep found, with the pair it states and the ceiling it was written against. | `NON_HISTORY_SITES` | mcp/tests/test_memory_citation_agreement.py:725-735 |
| The subset a repair moves, counted separately from the worklist the next curation inherits. | `LIVE_SITE_COUNT` | mcp/tests/test_memory_citation_agreement.py:736-738 |
| The superseded-pair worklist: **DERIVED from the tree**, never remembered. The rule is `superseded_pair_sites`, the producer it carries is `notes/reports/tsip-instruments/l7-curator-stale-pair-enum.py`, and a change in either direction is a finding (`T112`, `F2`). | `NON_HISTORY_SUPERSEDED_SITES` | mcp/tests/test_memory_citation_agreement.py:758-758 |
| The derived rule itself, so the pin can fail when the derivation stops seeing. | `superseded_pair_sites` | mcp/tests/test_memory_citation_agreement.py:228-248 |
| The five hermetic arms that prove the derivation fires: counted outside history, dated inside it, not hidden by a qualified heading, the comma-grouped spelling, and the declared pair excluded. | `SupersededPairDerivationTests` | mcp/tests/test_memory_citation_agreement.py:939-993 |
| The live arm: the worklist count on the named tree equals the derived count. | `test_the_superseded_pair_population_is_derived_from_the_tree` | mcp/tests/test_memory_citation_agreement.py:899-925 |
| The qualified-heading census: a NAMED population pinned at one entry, the merged sibling line's deliberate dated heading. | `QualifiedHistoryHeadingTests` | mcp/tests/test_memory_citation_agreement.py:996-1055 |
| The census constant: the pinned tuple the live arm compares against, and what each entry means. | `QUALIFIED_HEADINGS` | mcp/tests/test_memory_citation_agreement.py:1017-1017 |
| The live arm that reds when the pinned population moves in either direction. | `test_the_named_tree_carries_exactly_the_pinned_ones` | mcp/tests/test_memory_citation_agreement.py:1083-1095 |
| The two section-boundary bounds of the worklist rule, each with its direction, measured on planted documents. | `history_section_flags` | mcp/tests/test_memory_citation_agreement.py:190-225 |
| The budget screen: the declared pair read from `pyproject.toml`, never restated here. | `BudgetAgreementTests` | mcp/tests/test_memory_citation_agreement.py:698-936 |
| The repaired sentence held by a case now that its stale entry is gone, so a repair is not a gap. | `test_the_repaired_site_states_the_declared_pair` | mcp/tests/test_memory_citation_agreement.py:770-801 |
| Both figures asserted separately at every pinned site, so a site that has moved on is red. | `test_the_live_sites_still_state_the_figures_they_are_pinned_to` | mcp/tests/test_memory_citation_agreement.py:927-959 |
| The two figure classes counted separately: a live claim is not a dated record, and the worklist is larger than the set a repair moves. | `test_the_two_figure_classes_are_counted_separately` | mcp/tests/test_memory_citation_agreement.py:961-970 |
| The module's own mutation boundary, read from its own AST (`T114`'s bound). | `test_this_module_shells_out_to_nothing` | mcp/tests/test_memory_citation_agreement.py:1127-1160 |
| The lane row that keeps this module in the default selection. | "mcp/tests/test_memory_citation_agreement.py" | mcp/tests/test-evidence-lanes.toml:120-120 |
| The product counter this module's live case reads, and the code string it emits. | `definition_outside_range_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:466-513 |
| The entry point `memory_quality_check` dispatches through, so the case drives the product and not a copy. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:650-685 |
| The payload key the live pin reads. | "definitionsOutsideCitedRanges" | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:718-718 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## 260918-TSIP-L7 The Agreement Leaf's Own Acceptance Module

This card is created by the leaf's **curator**, not by the worker who wrote the module: a worker
editing the memory tree is the role boundary this master registered as `T105`, and the worker was
sanctioned only for the one budget sentence in `onboarding/mcp/overview.md` it disclosed. The module
is **new in that leaf** — 793 lines, 26 cases, sha256 `125d9cc414154e1c…` — and before this card it
had **no file-level onboarding and no mention anywhere in the memory tree**, while every other test
module in the route carries a card.

Two register questions this card answers rather than assumes.

**Does a lane someone actually runs reach it?** Yes, and by two independent routes. The lane row is
`mcp/tests/test-evidence-lanes.toml:120-120` in **`unit-regression`**, which is the lane the default
selection collects: the leaf's targeted run of eight modules is **85 passed / 3 skipped / 31 subtests**
and the module's own live run on the leaf pair is **26 passed** (155 s) with `AR_ONBOARDING_ROOT`
naming the leaf memory worktree. The registry loader (`mcp/tests/test_evidence_lanes.py`, **3 passed**)
is what makes the row load-bearing: the module was run before its row existed and the loader refused
it — *"test files without an explicit lane"* — so a module cannot enter the tree unreached. Removing
the row is also the one evasion the successor verification's mutation battery **caught**.

**Does it need a row in `mcp/tests/evidence-lifecycle.toml` as well?** **No**, and that is measured
rather than argued — this is register row `T106`'s class, where a module landed with a lane row and no
lifecycle row and went unseen because the two cases that police that catalog are integration-marked.
Running those two cases on this leaf's tree (`-m ""`, `mcp/tests/test_dependency_ownership_ast_helpers.py`,
**2 failed in 47 s**) reports `unregistered=['mcp/tests/tool_refusal_census_support.py']` — `T106`'s
own, L10-owned defect, which reproduces at this base — and **does not name this module**. The catalog's
`owner` values are governed evidence artifacts (support and test-port modules such as
`*_test_support.py`, plus three production modules), not plain test modules; this module contributes no
governed artifact and is reached through its lane row instead. It is therefore complete without a
lifecycle row, and the two integration failures on this tree belong to `T106`, not to this leaf.

## 260918-TSIP-L12 The Acceptance Module's Pins Re-Derived, And What Each One Now Asserts

The master-end adversarial review falsified the module's own acceptance pins one leaf after they
landed, and this leaf repaired them. Four things changed, and each is stated with what it now means
rather than only with its value.

**`F2` — a pin that could not fail is now a derivation.** `SUPERSEDED_DECLARED_SITES = 20` was
compared with its own literal, so no tree could move it, while the master's own producer for that
population read **101 lines / 64 outside `## Update History` / 18 documents** on the very tree the
module pinned. The constant is gone; `SUPERSEDED_PAIR` — the pair named at `:185` — is asserted
nowhere as a literal, and `history_section_flags` (`:190-225`) with `superseded_pair_sites`
(`:228-248`) carry the producer's rule in-tree instead. `NON_HISTORY_SUPERSEDED_SITES` is pinned
against the count that function returns. The replacement is proven able to fail in **both**
directions — 55 → 56 and 55 → 54 each red the case while the old form stayed green through both
(`notes/reports/tsip-instruments/l12-f2-mutation-control.sh`).

**`F3` — the pins' address moved from a branch to a commit pair.** Two branches a pin could have named
are reclaimed by their own finalize — a leaf's at leaf finalize, the master's at master cleanup
(`T89`) — and the sprint branch is written by another line besides this master. The header now names
the **commit pair** the leaf lands, with the branch only as *where the commit may be found*, and states
that a red pin on a moved or merged tree is not a regression until it is re-derived there.

**`F1` — the live claims in the memory corpus that asserted the superseded pair.** Eighteen lines in
five documents stated the pair `SUPERSEDED_PAIR` names, as the pair the repository declares **now**;
every figure was re-read from `pyproject.toml:263-264` and corrected in place, with no line count
moved anywhere, so no citation below them shifted. The module's new derivation is the check that
catches the next one — and it caught this card's own first draft, which is worth recording: the
paragraph you are reading named the superseded figures beside the declared ones and the worklist
counted it, so the draft was reworded rather than the pin moved. That is `T112`'s repair working in
the direction that matters, and it is why a documentation edit may not be assumed pin-neutral.

**`F8` / `T125` — the heading census, and the one heading that is deliberately left alone.** Two
qualified `## Update History…` headings were removed rather than made "exact", because making them
exact was **measured** to change product output: in one document it invents a `malformed_entry`
finding, and in the other it relocates the mechanical projection's insertion point and with it 617
generated bullets. A third heading arrived with the merge — `mcp/tests/overview.md:4833` — and it is
pinned as a **named population** rather than repaired, because it is the corpus's deliberate dated
form rather than wrap damage.

**What the pins read, and on which tree.** All four were re-derived on the pair this leaf lands, not
carried from the pair it was cut from `4d0fc20a`/`47570cd8`: on that earlier pair they read 47 / 123 /
0 / 3-2, and the merge moved three of them. `AR_ONBOARDING_ROOT=<the leaf tree>/onboarding` then runs
**35 passed**; with the variable unset the same module reads **30 passed, 5 skipped**, which is the
trap rather than a green light.

## Update History
- 2026-09-20T05:10+02:00 — 260918-TSIP-L12 curator (uncommitted change set on `ar/260918-tsip-l12-ar`, memory base `ec1cebe5`, code base `15e10084`): **body re-derived, not a metadata refresh.** Every claim on this card was re-read against the module's current bytes (`mcp/tests/test_memory_citation_agreement.py`, **1124 lines / 35 cases**, sha256 `34db6ea729d58833…`) and against the merged tree, because the module's four shipped pins, its header clause and its live-case prose all changed in this leaf and the card still described the pre-`L12` module. Corrected here: the case and class counts (**26 → 35 cases**, five classes → **seven**); every cited line range, re-derived from the module rather than shifted; the three constants the card named as the module's pins (**`SUPERSEDED_DECLARED_SITES = 20` is gone** — the card's claim that it was "asserted, not derived" is now history rather than state, and its rows were re-pointed at the derivation that replaced it); `T52_DEFINITION_OUTSIDE_RANGE` **123 → 130**; and above all **`T52_ENFORCED_POPULATION` was recorded as 0 and now reads 97**, which the card states as **inherited debt from the merged `260915_knowledge-substrate` line**, the same 97 register row `T141` measured, with a change in **either** direction named as a finding. The pins' address is recorded as the **commit pair**, not a branch (`F3`), and the qualified-heading census is recorded as a **named population of one** (`mcp/tests/overview.md:4833`) rather than as a zero. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` advanced because the claim re-read happened rather than instead of it — and they name the base commit the candidate was cut from, because no commit yet carries this source and the governed closeout owns the real stamp. **DISCLOSED — this card moved a pin on its first draft, and the pin was not moved to accommodate it.** The first draft's `F1`/`F2` paragraphs named the superseded figures (`2300`/`400`) beside the declared ones, outside `## Update History`; `test_the_superseded_pair_population_is_derived_from_the_tree` red **58 != 55** on three of this card's own lines, exactly as the derivation is built to. The derivation was right and the prose was wrong, so the **prose was reworded to refer to `SUPERSEDED_PAIR` by name instead of restating its figures** and the constant stayed **55** — the alternative (re-pinning 55 → 58) would have converted a documentation slip into a standing exemption. Verified after the edit by calling `superseded_pair_sites` directly: 55, and this card contributes **none**. That is `T112`'s repair working in the direction that matters, and it is why a documentation edit may not be assumed pin-neutral. No `Generated citation repair` bullet was added (`T118`) and no projection bullet was retired by adding a note (`T134`).
- 2026-09-20T01:30+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 5 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_memory_citation_agreement.py.md:156` (T52_DEFINITION_OUTSIDE_RANGE) — re-read the claim against the re-pinned constant: its value, its tree and its line all moved when 260918-TSIP-L11 re-derived the pins on the landed line; `test_memory_citation_agreement.py.md:157` (T52_ENFORCED_POPULATION) — re-read the claim against the re-pinned constant: the enforced population is 0 on the landed pair and the row says so now; `test_memory_citation_agreement.py.md:158` (T58_WRAPPED_CITATIONS) — re-read the claim against the re-pinned module: the T58 pins are unchanged in value and the cited lines moved with the header; `test_memory_citation_agreement.py.md:9` () — STAMP ADVANCE: the four constant rows were re-read against the landed commit, which is the pair this leaf closes out; `test_memory_citation_agreement.py.md:10` () — STAMP ADVANCE: date moves with the commit.
- 2026-09-19T22:52+02:00 — 260918-TSIP-L7 curator (uncommitted change set on `ar/260918-tsip-l7-ar`, memory worktree base `fd1a024e`): **created.** The module is new in this leaf (**793 lines / 26 cases**, sha256 `125d9cc414154e1c…`) and had no file-level onboarding at all. Recorded the two agreement classes it keeps (`T52`, `T45`/`T56`), the five classes and their case counts, the tree **pair** every live number is measured against with the official checkout named as refused, the three non-history stale sites and the two figure classes, and the three recorded bounds — `SUPERSEDED_DECLARED_SITES = 20` asserted rather than derived (`T112`), the header's `memory_tools.py:100` corrected to `:105` (`R2-3`) and the `T58` comment's `worktree.py.md:99` corrected to `:102` (`R2-5`), and the AST guard's narrower set (`T114`). It also records the lane and lifecycle answer for `T106`'s class: the module is reached by `unit-regression` in the default selection, and the one unregistered governed path the catalog cases name is L10's `tool_refusal_census_support.py`, not this module. Verification metadata is the recorded base commit, which does not contain this file; the candidate is uncommitted and the governed closeout stamps the real code commit.
