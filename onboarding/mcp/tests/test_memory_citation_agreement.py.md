# mcp/tests/test_memory_citation_agreement.py

## Governing Overview

[mcp/tests overview](overview.md)

**Historical L7/L12 provenance, not current verification metadata.** When this module was new in `260918-TSIP-L7`, no commit yet carried those working bytes, so the former `lastVerifiedCommitHash` stamped their base and closeout owned the later real stamp. The L12 reread and working-candidate digest account belong to that earlier epoch. Converted cards carry no such verification-stamp field, and this account authenticates neither A005 nor its current live populations.

**Shipped source address.** The retained source header names the `260918-TSIP-L13` pair: memory `682bbdfd` plus that leaf’s change set, paired with code `1bcf73e7` plus its change set. `BudgetAgreementTests.NON_HISTORY_SUPERSEDED_SITES` is **53**, with the source recording the historical L13 change from 55. These are source-header and constant facts, not a new live-population measurement or L59 acceptance. The L7/L12 pair and measured 55 observations below remain explicitly historical.

## Purpose

Retained agreement checks protect GFM pipe escapes, budget declaration/prose agreement, the source-derived superseded-pair worklist, qualified history-heading census and the module’s bounded AST/environment behavior. The legacy T52 range-resolution and T58 wrapped-citation populations are historical, not executable pins in the candidate.

The historical agreement work retains its budget/worklist and heading-census obligations. Exact pair-specific T52/T58 and inherited-debt figures below record past measurements only: their constants do not make removed classes executable. The surviving live budget/heading checks still require AR_ONBOARDING_ROOT and must not be advertised as measured when skipped.

Historical L7/L12 origin account (not current executable T52/T58 populations):

The following origin account describes the historical `260918-TSIP-L7` agreement leaf, extended by
`260918-TSIP-L12` when the master-end review falsified its own acceptance pins. It pins four
populations and one census: the product change the leaf lands (a report-only
`citation_anchor_definition_outside_range` finding, plus GFM's `\|` escape resolved where cell text
becomes anchor text), the live populations of both classes as **exact equalities** — including the
**enforced** population, which is **97 and inherited from the merged `260915_knowledge-substrate`
line**, not this master's — the classification of every stale budget figure the sweep found, the
superseded-pair worklist **derived from the tree** rather than remembered, and the census of
qualified `## Update History…` headings. The older-budget cases inspect a fixed three-site dictionary and the figures recorded for those sites; they do not discover new, unlisted older-budget sites. Separately, the superseded-pair worklist is derived by walking the named tree and can detect a change in that derived population. A changed listed figure and a newly discovered superseded-pair site therefore have different detection paths.

## Code Commentary

### Logic

Five unittest classes contain 26 statically observed test-method definitions, not a collected/executed case total: EscapedPipeAnchorTests, BudgetAgreementTests, SupersededPairDerivationTests, QualifiedHistoryHeadingTests and RepoStateTests.

- **`T57`, the escape** (`EscapedPipeAnchorTests`, `:282-375`). A literal pipe in a GFM table cell must
  be written `\|`, so `` `useEffect(cb, [a \| b])` `` reached the anchor grammar carrying a character
  the source does not have and was silently counted as an *unchecked span* — reading as checked and
  not being checked. Seven cases cover the code-span anchor, the same escape in the **Source** cell, a
  **quote** anchor, and the documented bound: `unescaped` is one literal `\|` → `|` replacement, so
  with two backslashes the second is the one consumed and the source's `a | b` stays unmatched, which
  is GFM's own reading.

- **The budget screen** (`BudgetAgreementTests`, `:378-654`). The declared pair is read from
  `pyproject.toml` at run time. The current declaration assertion pins 10,000/2,000, and the stub mirror must follow it; the repaired sentence must state that pair and the declaration's line range as computed by `declared_lines` (currently `pyproject.toml:333-334`). This corrects the changed budget assertion only; the retained pair-specific census and historical pin accounts below are not new measurements or current-candidate acceptance. The
  declarations on `conftest.py` must register both names and state no value; the two stale-figure
  classes are counted separately; and the superseded-pair worklist is pinned as **the count
  `superseded_pair_sites` returns**, not as a literal.
- **`T112`/`F2`, the derivation itself** (`SupersededPairDerivationTests`, `:657-711`). Five hermetic
  arms prove the worklist rule fires: a live site outside history is counted (`:676-679`); the same
  line inside `## Update History` is not (`:681-687`); a qualified `## Update History…` heading cannot
  hide a live line (`:689-701`); the comma-grouped spelling of the superseded unit ceiling is
  counted, where a plain grep for the digits alone under-counts (`:703-706`); and the declared pair
  is not itself a site (`:708-711`).
- **`T125`/`F8`, the heading census** (`QualifiedHistoryHeadingTests`, `:714-779`). The corpus writes
  `## Update History` and the checker accepts only that spelling, so a qualified title renders as a
  section boundary while every entry beneath it is invisible to the order check — and the corpus
  carried two with no diagnostic at all. Four arms: the detector fires on the backtick-mangled title
  (`:753-755`) and on a dated title (`:757-760`), an exact heading — and a deeper `###` one — is
  not reported (`:762-765`), and a live arm asserts the named tree carries exactly the pinned list.
- **The module's own boundary** (`RepoStateTests`, `:782-844`). The module under test is the working
  tree's, no memory tree is reached for by default, and no `subprocess` is used.

### Conventions

Every root is derived from `__file__` — `MCP_SRC`, `MCP_TESTS`, `REPOSITORY_ROOT` (`:50-50`) — and
**never from the working directory**, which is the rule register row `T102`(d) states: a
repository-root-relative path literal makes a suite's result a fact about the directory it ran in.
The live-population cases are **hermetic by construction**: with no `AR_ONBOARDING_ROOT` they **skip**
rather than reach for a checkout that may not exist on the machine running them
(`live_onboarding_root`, `:268-279`), and the mechanism cases build their worlds under
`tempfile.TemporaryDirectory`.

The lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:248-248`), so the module is in
the **default selection** and the unit population a full run collects — it is not an integration-only
or manually-invoked lane. The surviving live budget/worklist/heading cases additionally require `AR_ONBOARDING_ROOT` to name a
memory tree ; without it they skip, and the retained mechanism cases still enforce their own budget/heading derivations. **A green lane run is therefore never evidence that the pins
hold** — that sentence is in the module's own header, and it is the answer to `T122`'s trap.

### Invariants And Boundaries

- **Historical L12 pair account (superseded by the shipped L13 header above).** At that epoch the live numbers were measured against the pair
  `260918-TSIP-L12` landed: memory `ec1cebe5` — the `260918_tool-surface-and-process-integrity`
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
- Historical T52/T58 account only, not current executable coverage: **The pins are exact and pair-specific, and that is falsifiable.** `T52_DEFINITION_OUTSIDE_RANGE`
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
  (shipped value **53**) is pinned against the count `superseded_pair_sites` returns on the named tree, and
  that function is red when the defect grows and when the derivation stops seeing. The constant it
  replaces — `SUPERSEDED_DECLARED_SITES = 20` — was compared with its own literal, so **no change to
  any tree could move it**: a hard-coded fact wearing the clothes of a measurement, in the module
  written to enforce agreement (law 4). Its named producer read **64** outside `## Update History` on
  the very tree the module pinned, and `F1` of the master-end review is the class it was blind to.
  Historically at L12 the worklist read 64 at base, 47 after that leaf repaired the seventeen lines that stated the
  superseded pair as current, and **55** on its merged tree; the +8 was the sibling line's own budget
  prose. It is a **worklist, not a verdict**: each line is a dated or as-of reading reviewed row by
  row, and none is asserted to be wrong by being counted.
- **The qualified-heading census is a NAMED population, not a zero.**
  `QualifiedHistoryHeadingTests.QUALIFIED_HEADINGS` (`:741`) pins one entry —
  `mcp/tests/overview.md:4833`, the sibling `260915_knowledge-substrate` line's dated heading, which
  arrived with the merge. It is pinned rather than repaired deliberately, and the reading behind that
  is recorded on the document: the heading is the corpus's **deliberate dated form**, structurally
  intact and the last of its kind in the tree, so `T125`'s ruling — *normalise only when the heading
  is accidental* — does not apply to it. The census case therefore reds when the population moves in
  **either** direction.
- **The tree is a worklist with two bounds, both measured.** `history_section_flags` (`:185-220`) uses
  the exact-title rule `update_history_sections` accepts, where the producer uses a prefix match; and
  it ends a section only at a level-2 heading where the product ends it at level ≤ 2. Measured on
  planted documents (`notes/reports/tsip-instruments/l12-sv3-bound.py`): against the **product** the
  worklist can *under*-count (a level-1 heading inside a history section), and against the **producer**
  it can *over*-count (a qualified heading) — the second direction is deliberate, because it is the
  one a mangled heading cannot blind. Neither bound is reached on the pinned pair.
- Historical T52/T58 account only, not current executable coverage: **The `T58` comment's second site is off by three lines.** The header names
  `models/worktree.py.md` line 99; the wrapped construct begins at **`:102`** (line 99 is the previous
  claim's anchor, line 100 its one-line citation). `service.py.md` `:30` and `:43` are exact. Nothing
  asserts the comment, so nothing fails — recorded so a reader following it lands on the construct.
- Historical T52/T58 account only, not current executable coverage: **The two zero-populations are `T58`'s and the repository's, and they are different files.**
  `test_the_repository_carries_none` (`:631-643`) walks the **code** repository's markdown and asserts
  `0`; the three wrapped constructs live in the **memory** tree and are counted by
  `test_the_live_memory_tree_matches_the_pins` (`:645-695`), which enumerates documents with the same
  detector rather than reading the fixer's own counter — a case that reads its subject's counter cannot
  falsify it.
- **The AST guard's name is wider than its set.** `test_this_module_shells_out_to_nothing`
  (`:811-844`) flags the attributes `run`/`system`/`popen`/`check_output`/`Popen`, the bare names
  `system`/`popen` and any `subprocess` import; `os.posix_spawn`, `os.exec*` and `os.spawn*` are
  outside it, which the successor verification demonstrated by mutation. No such call exists; the
  honest statement of the property is the narrower one, and this bound is register row `T114`.
- Historical T52/T58 account only, not current executable coverage: **Scope boundary.** The module proves the *mechanism* on trees it builds and *pins* the live
  populations; it does not repair them. The `T52` rows, the 97 enforced rows and the stale budget
  figures are worklists for the route curators. Derived populations are checked against enumeration; the older-budget dictionary checks only its recorded sites and does not discover additional unlisted sites.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only. The
comment-level findings above (`T58`'s second site, `T114`'s guard bound, `SV-3`'s two derivation
bounds) belong to whatever change next touches the module. `T138` — the tool reference's 20-row table
divergence — is registered and not this module's.

The escaped-pipe row case derives stripped cell text from the live cell_spans offsets after removal of the unused split_row wrapper. The same row still has three cells and yields the original useEffect anchor; its inputs and assertions are preserved. This source-path maintenance adds no population measurement or execution claim.

## Evidence






### Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References



- The current declaration assertion pins 10,000 unit/2,000 integration and checks the matching stub mirrors.  Anchor: `unit_case_budget` [33]


The anchors below identify current behaviour of this module; they are not execution evidence and they
make no acceptance claim.


- The product citation-mutation guard refuses the official memory repository. [1]

The product refusal is definition-addressed rather than the old module-header location; no fresh mutation execution is claimed.
- The live tree, named by the run and skipped when no run names one. [3]
- The escape resolved where cell text becomes anchor text, which is where the `T57` blind spot was. [9]







- Every stale site the sweep found, with the pair it states and the ceiling it was written against. [14]
- The subset a repair moves, counted separately from the worklist the next curation inherits. [15]

- The shipped superseded-pair constant is 53; the live case compares it with the tree-derived worklist. Historical L12 measured 55, and the source header attributes 55-to-53 to L13 rather than to L59. [16]

- The derived rule itself, so the pin can fail when the derivation stops seeing. [17]
- The five hermetic arms that prove the derivation fires: counted outside history, dated inside it, not hidden by a qualified heading, the comma-grouped spelling, and the declared pair excluded. [18]
- The live arm: the worklist count on the named tree equals the derived count. [19]
- The qualified-heading census: a NAMED population pinned at one entry, the merged sibling line's deliberate dated heading. [20]
- The census constant: the pinned tuple the live arm compares against, and what each entry means. [21]
- The live arm that reds when the pinned population moves in either direction. [22]
- The two section-boundary bounds of the worklist rule, each with its direction, measured on planted documents. [23]




- The budget screen dynamically reads declaration line positions, pins 10,000/2,000 and matching stubs, and bounds the live overview sentence check. [24]







- Both figures asserted separately at every pinned site, so a site that has moved on is red. [26]
- The two figure classes counted separately: a live claim is not a dated record, and the worklist is larger than the set a repair moves. [27]
- The module's own mutation boundary, read from its own AST (`T114`'s bound). [28]









### Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

No repository or external-system boundary is proved by this module.

## 260918-TSIP-L7 The Agreement Leaf's Own Acceptance Module

Recorded historical source/run account, not current executable coverage: This card is created by the leaf's **curator**, not by the worker who wrote the module: a worker
editing the memory tree is the role boundary this master registered as `T105`, and the worker was
sanctioned only for the one budget sentence in `onboarding/mcp/overview.md` it disclosed. The module
is **new in that leaf** — 793 lines, 26 cases, sha256 `125d9cc414154e1c…` — and before this card it
had **no file-level onboarding and no mention anywhere in the memory tree**, while every other test
module in the route carries a card.

Recorded historical source/run account, not current executable coverage: Two register questions this card answers rather than assumes.

Recorded historical source/run account, not current executable coverage: **Does a lane someone actually runs reach it?** Yes, and by two independent routes. The lane row is
`mcp/tests/test-evidence-lanes.toml:248-248` in **`unit-regression`**, which is the lane the default
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
nowhere as a literal, and `history_section_flags` (`:185-220`) with `superseded_pair_sites`
(`:223-243`) carry the producer's rule in-tree instead. `NON_HISTORY_SUPERSEDED_SITES` is pinned
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

Recorded historical source/run account, not current executable coverage: **What the pins read, and on which tree.** All four were re-derived on the pair this leaf lands, not
carried from the pair it was cut from `4d0fc20a`/`47570cd8`: on that earlier pair they read 47 / 123 /
0 / 3-2, and the merge moved three of them. `AR_ONBOARDING_ROOT=<the leaf tree>/onboarding` then runs
**35 passed**; with the variable unset the same module reads **30 passed, 5 skipped**, which is the
trap rather than a green light.





- The repaired sentence held by a case now that its stale entry is gone, so a repair is not a gap.  Anchor: `test_the_repaired_site_states_the_declared_pair` [25]

- The declaration assertion and stub screen use 10,000 unit and 2,000 integration cases; the overview citation range is derived from the actual declaration lines.  Anchor: `unit_case_budget` [34]

- Both cells and the quote path preserve escaped/plain anchor agreement; the row case derives text from live cell spans. The separately retained budget-test range covers the declared-pair sentence, constant, marker-registration and older-budget-site assertions. [10]

- The retained L192 instruction-parameter row is separate from this module's own unit-regression entry. The added citation-agreement row establishes its default-selection membership. [29]
