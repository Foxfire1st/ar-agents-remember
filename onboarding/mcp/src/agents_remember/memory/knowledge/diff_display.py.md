# mcp/src/agents_remember/memory/knowledge/diff_display.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/diff_display.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-21T14:59:00+02:00 |
| lastVerifiedCommitHash | `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` |
| lastVerifiedCommitDate | 2026-09-21T16:05:56+02:00|
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; base `702714fc05363cb28eacaf101ba8384475a6aa56` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**What the comparison shows, what it leaves out, and the reference to the whole of it.** Three jobs that
are one job: **a response must never be readable as more than it is.** The display filter selects only
recorded vocabulary, every suppression is counted with its reason, and the expansion is a **value**
rather than a promise.

## Code Commentary

### Logic

`build_display(comparison, *, display_filter, probe, before, after) -> DiffDisplay` returns the shown
items, the omissions, the limitations and the expansion, in that order:

1. **`_apply_filter`** splits the union into shown items and at most **one** omission. The guard is
   *"was a display decision declared at all"* and not *"what does the display decision do"*: an absent
   filter and a filter that named no roles are the same state, so both return the comparison whole and
   neither produces an omission. What actually narrows the display is the suppression branch beneath
   it — and the filter suppresses **realization items only**, keyed by the role the author recorded
   (`_authored_role` reads it from whichever side holds the claim, so one rule covers both directions of
   a change). Both halves were measured in fix round 1: inverting the guard raises `AttributeError` on
   the unfiltered comparison, and neutering the suppression branch leaves every displayed total equal to
   its comparison total — the state the role-filter case kills on `displayed_total < items_total`.
2. **`_unselected_omissions`** emits one omission **per kind** for records carrying
   `present_outside_selection`, with a counted noun phrase and the sentence that says this is a fact
   about the two selections and **not a deletion**.
3. **`_unattributed_omission`** emits the packet's other named gap: the changed paths that **no**
   recorded realization claim attributes, when the probe observed a change set at all.
4. **`_expansion`** builds the reference from the **same one observation** the omission was counted
   from, so the omission count and the expansion's own path list are two renderings of one measurement
   rather than two measurements that could disagree.

**Filtering reduces what is displayed and never what was compared.** `comparison.items` is the whole
selected union and stays that way; the raw and displayed totals are carried separately by
`KnowledgeDiffCounts`, so no caller can read a filtered response as a smaller comparison.

**The limitations are derived, not asserted.** `DIFF_LIMITATION_ORDER` fixes the presentation order, and
`_declared` establishes each limitation from the omissions beside it through `_LIMITATION_REASONS` —
except `no_semantic_assessment_performed`, which is unconditional because it is a statement about the
operation's own contract. A limitation with no reason row would be one this response declared without
having established it, which `KnowledgeDiffResult` refuses at construction, so **the absence of a row
here is never a quiet pass**.


**A changed path is now an address, a status and a renderability, and the observation says when it is partial.** This leaf added `TreeChange` — the raw filename exactly as Git recorded it, Git's status letter, whether the content can be rendered (`text`/`binary`/`symlink`/`submodule`/`unknown`), a mode-change flag and the reason an `unknown` is unknown — and three fields on `TreePaths`: `entries` (the same measurement at full resolution, held in agreement with `paths` by a `__post_init__` that refuses a value whose paths are not exactly the entry paths), `partial` (the path set was measured while part of it could not be reported whole) and `unrepresentable` (the changed paths whose *name* is not valid UTF-8, kept in full rather than dropped, with `unrepresentable ⇒ partial` enforced at construction). `TREE_DIFF_COMMAND` changed with it: it is now `git diff --raw -z --no-renames {before_tree} {after_tree}` — the same delimiter-safe interface the measurement itself reads — because the line-oriented `--name-only` form quotes and escapes a pathname containing a tab or a newline, so a caller who ran the advertised command would hold a different string from the address the response lists and the address the same file is expanded by. `_expansion_detail` states a partial observation's own limit beside its counts, so the two counts are never read as the whole change set.

### The expansion, and why the probe is a seam

`TreeDifferenceProbe` is `Callable[[TreeSide, TreeSide], TreePaths]`, and the production implementation
lives in the application layer (`git_tree_difference_probe`). The reason is stated in the module
docstring: **a storage module that shelled out would put a subprocess on a read path whose whole
persistence argument is that it only ever issues a `SELECT`.** Anchor observation is delegated the same
way.

`TreePaths.available` is separate from its `paths` on purpose: a probe that could not run (an absent
root, a tree this repository does not hold) has **not** observed *no changes*, and reporting its silence
as "nothing changed between the trees" would be a fabricated fact. An unavailable probe therefore
contributes **no expansion at all** and says so through its `detail`. `no_tree_difference_probe` is the
honest answer for a comparison whose sides named no code tree: the record half is complete and the
source half was not requested.

**The published command carries the two tree ids and never a branch, a working tree or `HEAD`**
(`git diff --name-only --no-renames {before_tree} {after_tree}`), so a caller can reproduce the full
source diff even when this operation did not observe it, and the reference
(`diff_knowledge_scope:full-selected-candidate-source-diff`) is a request a caller can act on rather
than a cached artifact whose freshness would have to be trusted.

### `attributed_paths`, and the union rule that matters

A path is **attributed** when a realization claim the comparison selected names it, on **either** side —
the two sides are **unioned rather than intersected**, and that is exactly what the packet's omission is
about. A path the baseline's claim names and the candidate's selection no longer reaches **is**
attributed: the relationship's removal is its own item in the union, reported with its before-side
source, so counting it as unattributed would tell a reviewer that the earlier code had no recorded
attribution **when it had exactly that**. The four changed paths of the fixture are classified exactly
once across the two lists.

### Conventions

- `_KIND_NOUNS` and `_KIND_ORDER` are tables rather than f-strings or inline chains, so a kind added
  later is named by its own word instead of a neighbouring kind's.
- `_count` returns a counted noun phrase, so a `detail` reads as a measurement rather than as a template.
- Every `detail` in this module is prose written **for a reader**; nothing in it is parsed by the
  package, and the typed fields are what a caller branches on.

### Invariants And Boundaries

- **A filter narrows the display; it never narrows the comparison.** The filtered and raw totals both
  travel, so "displayed less" and "compared less" can never be confused.
- **No omission is ever described as harmless.** Each names the mechanism that removed the item from the
  display, and the unattributed-path detail says explicitly that **no assessment of consequence is made
  or implied**.
- **An unavailable observation is never reported as an empty change set.** `available=False` yields no
  omission and no path list, with the probe's own `detail` carried into the expansion.
- **Boundary.** This module decides what is displayed, what was omitted and what the expansion points
  at. It does not select, does not compare records, does not open a database and does not run a Git
  command — the one Git seam it needs arrives as a callable.

### Todos

None recorded. The increment reports the **attribution** of source and never source text; a document
dump is a different operation with a different limit. The richer display filters and the authored
neutrality annotations the packet defers are later increments (`KS-Q17`, `KS-Q18`), and until the
annotation lifecycle is specified the data stays visible and expandable rather than collapsed.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The expansion reference and the reproducing command, stated in full so neither needs this module to be read.** | `DIFF_EXPANSION_REFERENCE`; `TREE_DIFF_COMMAND` | mcp/src/agents_remember/memory/knowledge/diff_display.py:56-62; mcp/src/agents_remember/memory/knowledge/diff_display.py:75-78 |
| The fixed presentation order of the limitations. | `DIFF_LIMITATION_ORDER` | mcp/src/agents_remember/memory/knowledge/diff_display.py:79-84 |
| **One side's source binding: the exact tree and the root the command runs in, with `tree_id=None` a supported state.** | `TreeSide`; `TreePaths`; `TreeDifferenceProbe` | mcp/src/agents_remember/memory/knowledge/diff_display.py:75-106; mcp/src/agents_remember/memory/knowledge/diff_display.py:123-169; mcp/src/agents_remember/memory/knowledge/diff_display.py:170-170 |
| **The probe that observes nothing, for a comparison whose sides named no code tree.** | `no_tree_difference_probe` | mcp/src/agents_remember/memory/knowledge/diff_display.py:173-190 |
| The built display as one value: shown items, omissions, limitations, expansion. | `DiffDisplay` | mcp/src/agents_remember/memory/knowledge/diff_display.py:193-200 |
| **The one entry point and the order it builds in — filter, omissions, limitations, expansion from one observation.** | `build_display` | mcp/src/agents_remember/memory/knowledge/diff_display.py:203-233 |
| **The limitation table that establishes each declared limit from the omissions beside it.** | `_declared`; `_LIMITATION_REASONS` | mcp/src/agents_remember/memory/knowledge/diff_display.py:236-253; mcp/src/agents_remember/memory/knowledge/diff_display.py:254-261 |
| **The display filter, its two halves both measured in fix round 1, and the role read from whichever side holds the claim.** | `_apply_filter`; `_authored_role` | mcp/src/agents_remember/memory/knowledge/diff_display.py:200-258; mcp/src/agents_remember/memory/knowledge/diff_display.py:311-325 |
| **The per-kind omission for records the other side held but did not select, stated as a selection fact and not a deletion.** | `_unselected_omissions` | mcp/src/agents_remember/memory/knowledge/diff_display.py:328-347 |
| **The omission for changed paths no recorded realization attributes.** | `_unattributed_omission` | mcp/src/agents_remember/memory/knowledge/diff_display.py:350-376 |
| The noun and order tables, and the counted noun phrase. | `_KIND_NOUNS`; `_KIND_ORDER`; `_count` | mcp/src/agents_remember/memory/knowledge/diff_display.py:377-383; mcp/src/agents_remember/memory/knowledge/diff_display.py:385-391; mcp/src/agents_remember/memory/knowledge/diff_display.py:398-404 |
| **The attributed-path union and the unattributed remainder.** | `attributed_paths`; `_claim_paths`; `_unattributed_paths` | mcp/src/agents_remember/memory/knowledge/diff_display.py:343-377; mcp/src/agents_remember/memory/knowledge/diff_display.py:407-421; mcp/src/agents_remember/memory/knowledge/diff_display.py:424-432 |
| **The expansion builder: both trees, both roots, the four path lists and the detail that states what was observed.** | `_expansion`; `_item` | mcp/src/agents_remember/memory/knowledge/diff_display.py:380-444; mcp/src/agents_remember/memory/knowledge/diff_display.py:506-523 |
| The production probe, and the read-only handle the row counts are taken through. | `git_tree_difference_probe`; `open_diff_side`; `diff_row_counts` | mcp/src/agents_remember/application/knowledge_diff.py:162-196; mcp/src/agents_remember/application/knowledge_diff.py:128-159; mcp/src/agents_remember/application/knowledge_diff.py:124-155; mcp/src/agents_remember/application/knowledge_diff.py:803-819 |
| **The node that measures the expansion naming both trees and every differing path, and the node that measures the unattributed gap surviving a filter.** | "test_the_expansion_names_both_requested_trees_and_every_path_they_differ_at"; "test_a_changed_path_no_recorded_realization_attributes_is_listed_as_a_visible_gap" | mcp/tests/test_knowledge_diff_boundaries.py:145-182; mcp/tests/test_knowledge_diff_boundaries.py:185-218 |
| **The node that measures the filter narrowing the display and never the comparison.** | "test_a_role_filter_narrows_the_display_and_never_the_comparison" | mcp/tests/test_knowledge_diff_scope.py:536-573 |
| The two nodes that measure an unavailable observation reported as unavailable and a real probe making the gap visible. | "test_an_unavailable_observation_is_reported_as_unavailable_and_never_as_a_change_set"; "test_a_probe_that_measured_the_trees_is_what_makes_a_gap_visible" | mcp/tests/test_knowledge_diff_boundaries.py:774-814; mcp/tests/test_knowledge_diff_boundaries.py:817-840 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The two sides' `root` values are where the
application layer runs the published command, and this module never runs it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the display vocabulary learned to keep a path it cannot print.** `TreePaths` gained `entries`/`partial`/`unrepresentable` with the two construction rules that keep them honest (paths must equal the entry paths; an unrepresentable path implies a partial observation), and `TreeChange` was added as the status-bearing entry the review's inventory renders. The advertised command changed from `--name-only` to `--raw -z` for the reason stated in the module: the command a reader acts on must be the same interface that preserved the identity, or the boundary claim "a tab/newline filename remains the same address used for file expansion" is false in the one place it matters. `_expansion_detail` was extracted so a partial observation declares its limit rather than quietly counting fewer paths. All rows in the reference table were re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.


- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the comparison's display half. It records the three jobs as one job — **a response must never be readable as more than it is** — the ordered build (filter, omissions, limitations, expansion from **one** observation so the omission count and the path list cannot disagree), the filter that narrows the display and **never** the comparison, the limitation table that establishes each declared limit from the omissions beside it with `no_semantic_assessment_performed` unconditional, and the two limitations the packet names explicitly (records the other selection missed, and changed paths no recorded realization attributes). It states the two contracts a successor must not flatten: **`attributed_paths` unions the two sides rather than intersecting them**, because a path the baseline attributed and the candidate no longer reaches **is** attributed — counting it as unattributed would claim the earlier code had no recorded attribution when it had exactly that; and **`available=False` is not an empty change set**, so an unavailable probe contributes no expansion and no omission and says so through its `detail`. It also records why the probe is a seam rather than a subprocess inside this module (a storage module that shelled out would put a subprocess on a read path whose persistence argument is that it only issues `SELECT`) and that the published command names the two tree ids and never a branch, a working tree or `HEAD`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
