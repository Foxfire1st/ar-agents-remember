# mcp/tests/test_memory_citation_agreement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_agreement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T22:52+02:00 |
| lastVerifiedCommitHash | `d9214edf3388ee862f8c8f2ed59cf40af710d8bb`|
| lastVerifiedCommitDate | 2026-09-19T22:45:38+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l7-ar` uncommitted source (new file, **793 lines / 26 cases**, sha256 `125d9cc414154e1c…`); base `7879f5b2` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

Working candidate verification: this file is new in `260918-TSIP-L7` and **no commit carries its
bytes**, so `lastVerifiedCommitHash` names the base the leaf was cut from rather than a commit that
contains this source; it does not claim the uncommitted content was verified at that commit. The
`reviewedWorkingCandidate` row names the exact candidate and its digest, and the governed closeout
owns the real stamp. Every claim below was read against that candidate.

## Purpose

The two agreement classes the memory layer's own checks cannot see, kept green by cases rather than
by a report. **`T52`** is a construct that moved *inside* its cited range: `range_resolution` asks
whether an anchor **occurs** in a cited range, and a construct's name occurs at every call site, so a
range the definition has left stays green for as long as anything inside it still spells the name.
**`T45`/`T56`** is a case budget written in prose: no checker reads a prose numeral against the file
that declares it, so a route overview can advertise a budget the repository stopped declaring and
every check stays green.

This module is the durable form of the `260918-TSIP-L7` agreement leaf, and it pins three things: the
product change the leaf lands (a report-only `citation_anchor_definition_outside_range` finding, plus
GFM's `\|` escape resolved where cell text becomes anchor text), the live populations of both classes
as **exact equalities**, and the classification of every stale budget figure the sweep found. A pin
asserted in both directions is the point: a repair that is not carried into the pin fails the suite,
and a new stale site fails it until it is classified.

## Code Commentary

### Logic

Five classes, 26 cases, `unittest.TestCase` throughout, no `pytest` marks.

- **`T52`, the mechanism** (`DefinitionOutsideCitedRangeTests`, `:188-305`). The world is the measured
  shape reduced to its smallest form: a construct defined at `mcp/sample.py:20-21`, a **call** to it
  inside `:5-12`, and a claim citing `:5-12` for the construct's name. The membership test is
  satisfied by the call, so the claim reads current while pointing at the wrong lines
  (`test_the_moved_range_is_reported_and_stays_a_report`, `:215-229`). Three negatives bound it: a
  corrected range clears it (`:230-240`), an ambiguous anchor is not reported (`:241-253`), and a
  non-`SYMBOL` anchor has no definition to be outside of (`:254-292`) — the last pinning the **fact**
  the redundancy rests on rather than the redundant guard.
- **`T57`, the escape** (`EscapedPipeAnchorTests`, `:307-401`). A literal pipe in a GFM table cell must
  be written `\|`, so `` `useEffect(cb, [a \| b])` `` reached the anchor grammar carrying a character
  the source does not have and was silently counted as an *unchecked span* — reading as checked and
  not being checked. Six cases cover the code-span anchor, the same escape in the **Source** cell, a
  **quote** anchor, and the documented bound: `unescaped` is one literal `\|` → `|` replacement, so
  with two backslashes the second is the one consumed and the source's `a | b` stays unmatched, which
  is GFM's own reading.
- **`T58`, the population the fixer can only count** (`WrappedCitationPopulationTests`, `:403-513`). A
  wrapped `cit:` is parsed by the checker (it joins the paragraph) and counted by the fixer in
  `claimsNotOnOneLine`, and the fixer can rewrite none of them. The detector is proven by planting the
  shape in a temporary document (`:438-447`) so the zero it reports over the repository is a measured
  zero rather than an instrument that never fires.
- **The budget screen** (`BudgetAgreementTests`, `:515-724`). The declared pair is read from
  `pyproject.toml` at run time, never restated; the repaired sentence must state that pair; the
  declarations on `conftest.py` must register both names and state no value; and the two stale-figure
  classes are counted separately.
- **The module's own boundary** (`RepoStateTests`, `:727-789`). The module under test is the working
  tree's, no memory tree is reached for by default, and no `subprocess` is used.

### Conventions

Every root is derived from `__file__` — `MCP_SRC`, `MCP_TESTS`, `REPOSITORY_ROOT` (`:39-54`) — and
**never from the working directory**, which is the rule register row `T102`(d) states: a
repository-root-relative path literal makes a suite's result a fact about the directory it ran in.
The live-population cases are **hermetic by construction**: with no `AR_ONBOARDING_ROOT` they **skip**
rather than reach for a checkout that may not exist on the machine running them
(`live_onboarding_root`, `:94-105`), and the mechanism cases build their worlds under
`tempfile.TemporaryDirectory`.

The lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:120-120`), so the module is in
the **default selection** and the unit population a full run collects — it is not an integration-only
or manually-invoked lane. Both live cases additionally require `AR_ONBOARDING_ROOT` to name a memory
tree; without it they skip, and the mechanism cases still enforce the behaviour they count.

### Invariants And Boundaries

- **The tree is a pair, and both halves are named.** Every live number is measured against the **leaf
  memory worktree** at `fd1a024e` paired with the **code checkout the suite runs in** (base
  `7879f5b2`). The **official** memory checkout is a different tree on a different commit and is
  refused by the product: the row below cites `_refuse_official_memory` at
  `mcp/src/agents_remember/application/memory_tools.py:105-105`. The module header's comment cites the
  same symbol at `:100`; **that line number is wrong** — `:100` is
  `"onboardingRoot": scope.onboarding_root.as_posix(),` — and is recorded as finding `R2-3` of this
  leaf's successor verification. Naming one half of the pair without the other is the defect class
  (`T65`) this module exists to stop.
- **The pins are exact and pair-specific, and that is falsifiable in one direction.** The same module
  run against the official checkout is **red** (`123 != 120`); a pin widened to accept both trees would
  pass there. It passes on exactly one tree, and that is the one the enclosure contract names.
- **`SUPERSEDED_DECLARED_SITES = 20` is asserted, not derived** (`:555-560`, asserted at `:674`). The
  constant's own docstring says the instrument derives the sites; it does not, and no rule reproduces
  `20` — the leaf's instrument prints **50 LIVE / 27 REPORT** and its pair rule yields **24**. This is
  register row `T112`, recorded so nobody quotes the `20` as a derived population. A third, wider rule
  (the leaf's curator enumeration, `notes/reports/tsip-instruments/l7-curator-stale-pair-enum.py`)
  counts **98** lines carrying the superseded unit ceiling on the same tree, **63** of them outside
  `## Update History`. Three rules, three numbers: the constant is a hard-coded fact, and the worklist
  it stands for is understated rather than pinned.
- **The `T58` comment's second site is off by three lines.** `:84` names
  `models/worktree.py.md` line 99; the wrapped construct begins at **`:102`** (line 99 is the previous
  claim's anchor, line 100 its one-line citation). `service.py.md` `:30` and `:43` are exact. Nothing
  asserts the comment, so nothing fails — recorded as finding `R2-5` so a reader following it lands on
  the construct.
- **The two pinned zero-populations are `T58`'s and the repository's, and they are different files.**
  `test_the_repository_carries_none` (`:452-464`) walks the **code** repository's markdown and asserts
  `0`; the three wrapped constructs live in the **memory** tree and are counted by
  `test_the_live_memory_tree_matches_the_pins` (`:466-512`), which enumerates documents with the same
  detector rather than reading the fixer's own counter — a case that reads its subject's counter cannot
  falsify it.
- **The AST guard's name is wider than its set.** `test_this_module_shells_out_to_nothing` (`:756-789`)
  flags the attributes `run`/`system`/`popen`/`check_output`/`Popen`, the bare names `system`/`popen`
  and any `subprocess` import; `os.posix_spawn`, `os.exec*` and `os.spawn*` are outside it, which the
  successor verification demonstrated by mutation. No such call exists; the honest statement of the
  property is the narrower one, and this bound is register row `T114`.
- **Scope boundary.** The module proves the *mechanism* on trees it builds and *pins* the live
  populations; it does not repair them. The `T52` rows and the stale budget figures are worklists for
  the route curators, and the module's job is to make them move when they move.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only. The three
comment-level findings above (`R2-3`, `R2-5`, `T114`'s guard bound) belong to whatever change next
touches the module.

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
| The memory tree the product refuses, cited at the definition rather than at the module header's wrong line (`R2-3`). | `_refuse_official_memory` | mcp/src/agents_remember/application/memory_tools.py:105-105 |
| The world: a code tree and the memory tree that documents it, both under one temporary root, with the citation cache slot its census was built in removed. | `World` | mcp/tests/test_memory_citation_agreement.py:108-178 |
| The live tree, named by the run and skipped when no run names one. | `live_onboarding_root` | mcp/tests/test_memory_citation_agreement.py:94-105 |
| The `T52` population pin on the leaf memory worktree. | `T52_DEFINITION_OUTSIDE_RANGE` | mcp/tests/test_memory_citation_agreement.py:88-91 |
| The enforced population on the same tree, so the counter and the row list must agree. | `T52_ENFORCED_POPULATION` | mcp/tests/test_memory_citation_agreement.py:88-91 |
| The `T58` pins, derived by enumeration rather than from the fixer's counter. | `T58_WRAPPED_CITATIONS` | mcp/tests/test_memory_citation_agreement.py:88-91 |
| The `T52` shape: green membership, definition outside the range, one report-only finding. | `DefinitionOutsideCitedRangeTests` | mcp/tests/test_memory_citation_agreement.py:188-305 |
| The negative that makes the check a check: a corrected range clears it. | `test_a_corrected_range_clears_it` | mcp/tests/test_memory_citation_agreement.py:230-240 |
| The escape resolved where cell text becomes anchor text, which is where the `T57` blind spot was. | `unescaped` | mcp/src/agents_remember/memory_quality/style/citations/cells.py:40-53 |
| Both cells and the quote path: the escaped spelling must yield the anchor the plain spelling yields. | `EscapedPipeAnchorTests` | mcp/tests/test_memory_citation_agreement.py:307-401 |
| The wrapped-`cit:` detector, proven by a planted shape so the corpus zero is measured. | `wrapped_constructs` | mcp/tests/test_memory_citation_agreement.py:423-436 |
| The code repository's own markdown, enumerated: zero wrapped constructs is the pin. | `test_the_repository_carries_none` | mcp/tests/test_memory_citation_agreement.py:452-464 |
| The live case: `T52` 120, enforced 283, `T58` 3 constructs in 2 documents, on the pair. | `test_the_live_memory_tree_matches_the_pins` | mcp/tests/test_memory_citation_agreement.py:466-512 |
| Every stale site the sweep found, with the pair it states and the ceiling it was written against. | `NON_HISTORY_SITES` | mcp/tests/test_memory_citation_agreement.py:541-551 |
| The subset a repair moves, counted separately from the worklist the next curation inherits. | `LIVE_SITE_COUNT` | mcp/tests/test_memory_citation_agreement.py:552-554 |
| The superseded pair held as a count: **asserted, not derived** (`T112`). | `SUPERSEDED_DECLARED_SITES` | mcp/tests/test_memory_citation_agreement.py:555-560 |
| The budget screen: the declared pair read from `pyproject.toml`, never restated here. | `BudgetAgreementTests` | mcp/tests/test_memory_citation_agreement.py:515-724 |
| The repaired sentence held by a case now that its stale entry is gone, so a repair is not a gap. | `test_the_repaired_site_states_the_declared_pair` | mcp/tests/test_memory_citation_agreement.py:572-603 |
| Both figures asserted separately at every pinned site, so a site that has moved on is red. | `test_the_live_sites_still_state_the_figures_they_are_pinned_to` | mcp/tests/test_memory_citation_agreement.py:681-713 |
| The two figure classes counted separately: a live claim is not a dated record. | `test_the_two_figure_classes_are_counted_separately` | mcp/tests/test_memory_citation_agreement.py:715-724 |
| The module's own mutation boundary, read from its own AST (`T114`'s bound). | `test_this_module_shells_out_to_nothing` | mcp/tests/test_memory_citation_agreement.py:756-789 |
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
is **new in this leaf** — 793 lines, 26 cases, sha256 `125d9cc414154e1c…` — and before this card it
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

## Update History
- 2026-09-19T22:52+02:00 — 260918-TSIP-L7 curator (uncommitted change set on `ar/260918-tsip-l7-ar`, memory worktree base `fd1a024e`): **created.** The module is new in this leaf (**793 lines / 26 cases**, sha256 `125d9cc414154e1c…`) and had no file-level onboarding at all. Recorded the two agreement classes it keeps (`T52`, `T45`/`T56`), the five classes and their case counts, the tree **pair** every live number is measured against with the official checkout named as refused, the three non-history stale sites and the two figure classes, and the three recorded bounds — `SUPERSEDED_DECLARED_SITES = 20` asserted rather than derived (`T112`), the header's `memory_tools.py:100` corrected to `:105` (`R2-3`) and the `T58` comment's `worktree.py.md:99` corrected to `:102` (`R2-5`), and the AST guard's narrower set (`T114`). It also records the lane and lifecycle answer for `T106`'s class: the module is reached by `unit-regression` in the default selection, and the one unregistered governed path the catalog cases name is L10's `tool_refusal_census_support.py`, not this module. Verification metadata is the recorded base commit, which does not contain this file; the candidate is uncommitted and the governed closeout stamps the real code commit.
