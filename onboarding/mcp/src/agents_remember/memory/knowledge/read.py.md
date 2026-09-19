# mcp/src/agents_remember/memory/knowledge/read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The recorded-scope selection: the requirement's finite selection policy, executed once over one
database snapshot — plus whole-item paging over an already-selected scope.** One function answers *what
is the selected set* for one seed; one answers *which page of it fits*. They are deliberately separate,
because they are separate claims: the selection is a fact about the recorded graph and does not depend on
a budget, while a page is a presentation of it that must never be readable as a different scope.

**The load-bearing design fact is the stopping rule.** A membership is added for the families the seed
**reached**, not for the families it **discovered**: the directly containing family set `F0` is **frozen
before** membership expansion. That is what makes the traversal finite, and it is why the advertised
frontier is computed against the frozen family set rather than against the invariants.

## Code Commentary

### Logic

`select_recorded_scope(connection, SelectionQuery(repository_id, seed, resolve_anchor))` runs the
requirement's table in one fixed order, all on the caller's connection so every statement observes one
snapshot:

1. **`I0` — the seed's own invariant revisions** (`_seed_invariant_revisions`). A path seed selects
   through its recorded claims at that path; an invariant identity seed selects **every retained
   revision** of the identity; an explicit revision seed selects exactly one; a family seed selects none
   here.
2. **`F0` — the directly containing family revisions** (`_directly_containing_families`), for a path or
   invariant seed only, read from the **recorded membership rows** that cite one of `I0` rather than from
   a second, possibly disagreeing index. A family seed's `F0` is the family revisions it named and
   nothing else.
3. **`I = I0 ∪ members(F0)`**, with `F0` passed in **already frozen** (`_member_revision_ids`). This is
   the whole stopping rule: the function reads the memberships *of those family revisions* and never asks
   which other families a member belongs to.
4. **Claims** for every revision in `I` (`_realization_items`), with the seed's own revisions and the
   family-added members carrying different selection stages.
5. **Frontier** (`_frontier_expansions`): `memberships_of(I) − F0`, deduplicated, sorted, **advertised
   and never traversed**. For a path or invariant seed this is a sibling's membership in another family;
   for a family seed it is each member's membership elsewhere.

**The `P → I1`, `F → {I1, J1}`, `G → {J1, K1}` measurement, in the direction a consumer relies on:**
reading `P`, `I1` or exact `F` returns **I1's and J1's realizations**, **advertises J1's `G` membership**,
and **excludes K1** until `G` is selected explicitly in a subsequent expansion. Selecting `G` explicitly
is then what reaches K1. This is the property five separate nodes measure
(`mcp/tests/test_knowledge_read_scope.py:139`, `:170`, `:206`, `:246`, `:275`).

A path seed for a path with no recorded claim returns the **empty scope** (`_empty_scope`) and the
application reports `registration_absent`; the selection layer does not decide that refusal, because
"nothing is registered here" and "the registered set is empty" are different facts.

`_item_stream` builds the complete ordered stream, one item per indivisible record, and it is **the whole
declared set** — never a page of it:

- the stream's order is `(kind order, stable identity, revision/relation key, item_id)` (`_sort_key`),
  built **only from stored identifiers**. No authored label, no display version and no insertion counter
  participates, so the same graph authored in another insertion order pages identically.
- If the stream exceeds `SELECTION_ITEM_LIMIT` (5000) it raises `SelectionIncomplete` rather than emitting
  invented totals or a partial manifest; the application turns that into `selection_incomplete`.
- `_manifest_digest` covers each item's **kind, identity and selection reasons**, and **nothing about how
  the page was cut** — so the union of the pages of one selection is one manifest, and two selections that
  reach the same records **by different routes** get different manifests.

`SelectedScope` is the frozen result a lower-ranked consumer (L8's comparison) can hold: `items` (whole
set, ordered), `counts`, `directly_containing_families`, `revision_groups`, the three frozen sets
(`selected_invariant_revision_ids`, `selected_family_revision_ids`, `advertised`) and `manifest_digest`,
with `item_ids()` for the union-versus-declared-set comparison.

### The one thing L8 added to this module: `SelectionQuery.seed_override`

**`SelectionQuery` gained one field and one derived property, and that is the whole of L8's change to
this module** (the module's other edits are docstring prose; measured against the leaf's own change set,
21 added lines of which 17 are docstring):

- `seed_override: KnowledgeReadSeed | None = None`;
- `effective_seed` — `self.seed if self.seed_override is None else self.seed_override`;
- and `select_recorded_scope` reads `seed = query.effective_seed` as its **single** seed read
  (`:205`), with every later step — the seed's own revisions, the frozen directly-containing families,
  the closed member union, the advertised frontier, the item stream and the assembled scope — computed
  from that one local. No branch, no flag and no second code path was added.

**Why it exists, and the closed question it answers.** A two-snapshot comparison runs this one policy
**twice**, once per snapshot, and its two sides may address **different exact revisions of one identity**
(the packet's own words: *"an explicit revision selector may address different before/after revision
IDs"*). The override lets a side address its own revision without the policy learning a diff-shaped
branch. The reviewer attacked the packet's *"R07's policy is the ONLY policy owner"* clause head-on and
**could not falsify it**: the single read above is the whole mechanism; `grep -rn "diff\|Diff" read.py
read_queries.py` returns only docstring prose; the only production construction site is
`application/knowledge_diff.py:496 seed_override=side.selector`; every existing caller leaves the field
`None`, so `effective_seed is seed` on every read path; and the override is **load-bearing rather than
decorative** — mutation `R30` (`effective_seed` → `self.seed`) kills a named node on an assertion (the
explicit-per-side-selector node, `test_knowledge_diff_scope.py:390` on the frozen bytes; `:389` on the
pre-round 741-line file the mutation was measured against). **A per-side exact-revision address is a
parameterisation of R07's one rule, not a second relevance rule; the owner recorded the acceptance and
this question must not be re-opened.**

A second construction site belongs in the same sentence: `application/knowledge_read.py` passes no
override at all, so the read path is provably unaffected.

### Paging, and the count semantics review corrected

`page_of_scope(scope, PageRequest(context, seed, max_items, max_utf8_bytes, position))` cuts one
**whole-item** page: items are added while the complete serialized page still fits, so a governing
statement is never separated from its conditions, and the continuation a page would carry is **measured
with the page** rather than estimated. If even the first remaining item does not fit, `_too_small_page`
returns an empty page with `minimum_utf8_bytes` naming what the item needs and the position unchanged.

**`_page_counts` is the correction round 1 got wrong, and it is the single most important thing to read
here.** A continuation page's counts describe the **declared selected set**, not the remaining tail:

| Field | What it means |
| --- | --- |
| `primary_items_total` | the **declared selection total**, and the same number on every page of the walk |
| `primary_items_returned` | the **cumulative** figure for the pages up to and including this one |
| `primary_items_remaining` | what is still ahead |
| `len(page.items)` | **this page's slice** — the only place "how many came back this time" is readable |

The three still satisfy `returned + remaining == total`, now true **at every position** rather than only
at position 0. Restating the total as "this page's items plus the tail" is exactly what makes a
continuation lie: page 2 of a 17-item walk would report 16 and the last page 1, while the same counts
object still reports every kind total over all 17 — the requirement's own non-conforming example, *"a
one-item page implies that the invariant has only one implementation"*.

`KnowledgeReadCounts` also separates **claim identities from distinct source locations**
(`distinct_source_locations_total` counts `(path, locator)` pairs, `distinct_source_paths_total` counts
paths, `unresolved_anchor_total` counts anchors whose resolution is not `exact_recorded_blob`), because
two claims at one location are two claims and one location.

### Conventions

- **Nothing here writes.** Every statement is a `SELECT` on a connection the caller opened read-only; the
  one bounded integer this module adds to any statement counts rows. "A refused read persisted nothing"
  is therefore a property of the handle rather than a rollback the code has to remember.
- A `ReadItem` is one homogeneous model with optional kind-specific fields, so a page is one sequence a
  caller pages over without discriminating a second union.
- The `resolve_anchor` seam is a `Callable[[dict, ...], AnchorResolution | None]` rather than `Any`: the
  selection layer decides *which* anchors a seed exposes and never *how* a path is resolved. No anchor
  resolution happens when the caller passes nothing.
- `SelectionSets` keeps `seed_revisions`, `families` and `selected_invariants` distinct as one value,
  because the stopping rule is a statement about which of the three a lookup may use.

### Invariants And Boundaries

- **The family set is frozen before membership expansion.** Any change that re-feeds the frontier into
  `F0` converts a finite neighbourhood into a recursive closure and voids the requirement's stopping rule.
- **An identity seed is not a revision choice.** Every retained revision of the named identity is
  selected and grouped under its identity; nothing in the stream is an ordering, a version comparison or
  an insertion time that could be read as "this one is current". A display version never selects a
  revision.
- **The manifest digest covers the selection, not the page cut.** Two runs that select the same records
  produce the same `manifest_digest` whatever budget they were paged with — which is what makes a
  continuation checkable and what a cursor's `manifest_digest` binding rests on.
- **A truncation is never presentable as a complete family.** A page carries `has_more` and
  `enumeration_complete` as opposites, and `KnowledgeReadPage` refuses to exist if they disagree or if
  `has_more` disagrees with the presence of a continuation.
- **The known limit, stated rather than implied.** `_manifest_digest`'s inclusion of each item's
  `selection_reasons` is a **reachable covered gap**: the line is reachable and removing the reasons
  changes observable output, and no case asserts the digest's contents. It is disclosed (L9 ledger entry
  **A4**) rather than quietly closed after the freeze.
- **Boundary.** This module selects and pages. It does not open a database, does not resolve a source
  anchor, does not decide a refusal identity (that is `read_refusals.py` / `knowledge_read.py`), does not
  know what a task is, and writes nothing.

### Todos

None recorded. One carried observation belongs to the owning seat: `_manifest_digest`'s composition is a
reachable covered gap against this leaf (L9 ledger **A4**). The forward constraint L7 recorded here —
**L8 must split `mcp/tests/test_knowledge_read_scope.py` before adding cases** — was **paid**: L8 did not
add a case to that module; it added two new modules of its own, so the read unit module is unchanged at
1 163 lines and 37 lines of headroom.

**The one extension this module carries for L8 is `SelectionQuery.seed_override`, and it is documented in
full above** — including the closed reviewer question — because a successor who changes
`select_recorded_scope` has to know that the override is a parameterisation of the one policy and not a
second rule.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The selection policy in its declared order, with `F0` frozen before membership expansion, and the one seed read L8 added.** | `select_recorded_scope`; `SelectionSets`; `SelectionQuery` | mcp/src/agents_remember/memory/knowledge/read.py:193-238; mcp/src/agents_remember/memory/knowledge/read.py:179-189; mcp/src/agents_remember/memory/knowledge/read.py:150-175 |
| The seed half: a path selects through its claims, an identity selects every retained revision, an exact revision selects one, a family seed selects none here. | `_seed_invariant_revisions` | mcp/src/agents_remember/memory/knowledge/read.py:270-304 |
| **`F0` read from the recorded membership rows**, and the family seed's own revisions. | `_directly_containing_families` | mcp/src/agents_remember/memory/knowledge/read.py:307-339 |
| **The stopping rule itself: members of the frozen family set, never "which other families a member belongs to".** | `_member_revision_ids` | mcp/src/agents_remember/memory/knowledge/read.py:342-352 |
| **The advertised frontier: `memberships_of(I) − F0`, deduplicated, sorted, never traversed.** | `_frontier_expansions` | mcp/src/agents_remember/memory/knowledge/read.py:355-390 |
| **The declared item order, built only from stored identifiers.** | `_item_stream`; `_sort_key`; `_KIND_ORDER` | mcp/src/agents_remember/memory/knowledge/read.py:411-447; mcp/src/agents_remember/memory/knowledge/read.py:469-480; mcp/src/agents_remember/memory/knowledge/read.py:77-83 |
| The realization items and the anchor seam, and the two selection stages a per-side diff reads. | `_realization_items`; `_SEED_STAGES`; `_seed_stage` | mcp/src/agents_remember/memory/knowledge/read.py:594-626; mcp/src/agents_remember/memory/knowledge/read.py:454-466 |
| The assembled scope, the counts and the revision groups. | `_assembled_scope`; `_revision_groups`; `SelectedScope` | mcp/src/agents_remember/memory/knowledge/read.py:632-675; mcp/src/agents_remember/memory/knowledge/read.py:710-728; mcp/src/agents_remember/memory/knowledge/read.py:126-146 |
| **The manifest digest: kind, identity and selection reasons — and not how the page was cut.** | `_manifest_digest` | mcp/src/agents_remember/memory/knowledge/read.py:731-748 |
| **Whole-item paging, and the corrected count semantics: the declared total on every page, `returned` cumulative, the slice size in `len(page.items)`.** | `page_of_scope`; `_page_counts`; `_too_small_page`; `_page_bytes` | mcp/src/agents_remember/memory/knowledge/read.py:762-816; mcp/src/agents_remember/memory/knowledge/read.py:842-866; mcp/src/agents_remember/memory/knowledge/read.py:819-839; mcp/src/agents_remember/memory/knowledge/read.py:869-885 |
| The exception the application turns into `selection_incomplete`, raised when the selected set exceeds the declared bound. | `SelectionIncomplete` | mcp/src/agents_remember/memory/knowledge/read.py:109-122 |
| The declared execution bound itself. | `SELECTION_ITEM_LIMIT` | mcp/src/agents_remember/models/knowledge/read.py:94-96 |
| **The nodes that measure the packet's `P/I1/F/J1/G/K1` rule, including the explicit `G` expansion that reaches K1.** | "test_a_path_seed_returns_the_sibling_realizations_and_advertises_the_unreached_family"; "test_selecting_the_advertised_family_explicitly_is_what_reaches_the_further_realizations"; "test_an_exact_family_revision_seed_stops_after_its_own_members" | mcp/tests/test_knowledge_read_scope.py:139-169; mcp/tests/test_knowledge_read_scope.py:246-274; mcp/tests/test_knowledge_read_scope.py:206-245 |
| **The nodes that measure the corrected page counts: a one-item page still advertising the second location, and the union of all pages equalling the declared set.** | "test_a_page_budget_of_one_item_still_advertises_the_second_location"; "test_every_page_declares_the_same_snapshot_and_manifest_and_the_union_equals_the_selection" | mcp/tests/test_knowledge_read_scope.py:547-657; mcp/tests/test_knowledge_read_scope.py:658-721 |
| The ordering, truncation, budget, bound and absence nodes. | "test_the_item_stream_is_ordered_by_stored_identity_and_never_by_an_authored_label"; "test_a_truncated_page_states_that_items_remain_rather_than_claiming_completeness"; "test_a_page_budget_that_cannot_hold_one_item_refuses_and_keeps_the_position"; "test_a_selection_that_reaches_its_declared_bound_refuses_rather_than_reporting_a_total" | mcp/tests/test_knowledge_read_scope.py:722-837; mcp/tests/test_knowledge_read_scope.py:838-871; mcp/tests/test_knowledge_read_scope.py:872-901; mcp/tests/test_knowledge_read_scope.py:902-929 |
| **The node that kills mutation `R30` — the per-side exact-revision address the override exists for.** | "test_explicit_side_selectors_address_a_different_exact_revision_on_each_side" | mcp/tests/test_knowledge_diff_scope.py:390-421 |
| The fixture the policy is measured on, and the one cell decoder a read page and the logical digest share. | `read_scope_test_support.py`; `cell_value` | mcp/tests/read_scope_test_support.py:1-51; mcp/src/agents_remember/memory/knowledge/logical.py:240-248 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every statement runs against the connection the
caller opened; no second repository, ledger or coordination path is read.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): **extended this card with the one change L8 made to this module and re-derived every citation range against the new bytes.** The change is `SelectionQuery.seed_override` plus its derived `effective_seed`, and the card now carries it as a **closed question with the reviewer's evidence** so nobody re-opens it: `select_recorded_scope` reads `seed = query.effective_seed` as its single seed read (`:205`) and every later step is computed from that one local, no diff-shaped branch entered the policy owner, the only production construction site is `application/knowledge_diff.py:496`, every existing caller leaves the field `None` so `effective_seed is seed` on the read path, and mutation `R30` kills a named node on an assertion — so a per-side exact-revision address is a **parameterisation of R07's one rule, not a second relevance rule**. The card also records that L7's forward constraint was **paid rather than waived**: L8 added two new test modules and did not add a case to the read unit module, which stays at 1 163 of the 1 200-line limit. Every storage-module citation moved by the 19 lines the docstring addition inserted, so all of them were re-measured rather than shifted, and the `P/I1/F/J1/G/K1`, count-semantics, ordering, truncation and budget rows were re-read at their new positions. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the recorded-scope selection and its paging. It states the leaf's **load-bearing design fact** — the containing-family set is **frozen before membership expansion**, which is what makes the traversal finite and what produces the requirement's `P → I1`, `F → {I1, J1}`, `G → {J1, K1}` result (I1's and J1's realizations returned, J1's `G` membership **advertised**, K1 excluded until `G` is selected explicitly) — and it states the **count semantics the review corrected**, in the form a consumer must read them: a continuation page's `primary_items_total` is the declared selection total on every page, `primary_items_returned` is the walk's cumulative figure, and the slice size is `len(page.items)`, so a truncated page can never state a smaller scope. It records the declared item order (stored identifiers only), the manifest digest's coverage of selection reasons and not of the page cut, the seven-member anchor vocabulary this module only reports into, and the disclosed **reachable covered gap** in `_manifest_digest`'s composition (L9 ledger **A4**). It also carries the forward constraint that L8 must split this leaf's unit module before adding cases. Verification metadata remains empty until closeout stamps the code commit.
