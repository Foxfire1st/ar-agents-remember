# mcp/src/agents_remember/memory/knowledge/diff_display.py

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
3. **`_attribution_omissions`** emits the packet's other named gaps from the partition: the
   changed paths confirmed to have no valid registered attribution, and — separately — the changed
   paths whose attribution could not be determined because a required snapshot was not completely
   inspected. The two are different facts and travel as two limitations with two reasons.
4. **`_expansion`** builds the reference from the **same one observation** the partition was decided
   from (`SourceObservation`: the probe observes once, and the attribution reader is handed exactly
   that observation), so the partition's denominator and the expansion's own path lists are two
   renderings of one measurement rather than two measurements that could disagree. The expansion
   carries the partition itself, and `build_display` returns it beside the expansion so a caller
   never re-derives it.

**Filtering reduces what is displayed and never what was compared.** `comparison.items` is the whole
selected union and stays that way; the raw and displayed totals are carried separately by
`KnowledgeDiffCounts`, so no caller can read a filtered response as a smaller comparison.

**The limitations are derived, not asserted.** `DIFF_LIMITATION_ORDER` fixes the presentation order, and
`_declared` establishes each limitation from the omissions beside it through `_LIMITATION_REASONS` —
except `no_semantic_assessment_performed`, which is unconditional because it is a statement about the
operation's own contract. A limitation with no reason row would be one this response declared without
having established it, which `KnowledgeDiffResult` refuses at construction, so **the absence of a row
here is never a quiet pass**.


**A changed path is now an address, a status and a renderability, and the observation says when it is partial.** This leaf added `TreeChange` — the raw filename exactly as Git recorded it, Git's status letter, whether the content can be rendered (`text`/`binary`/`symlink`/`submodule`/`unknown`), a mode-change flag and the reason an `unknown` is unknown — and three fields on `TreePaths`: `entries` (the same measurement at full resolution, held in agreement with `paths` by a `__post_init__` that refuses a value whose paths are not exactly the entry paths), `partial` (the path set was measured while part of it could not be reported whole) and `unrepresentable` (the changed paths whose *name* is not valid UTF-8, kept in full rather than dropped, with `unrepresentable ⇒ partial` enforced at construction). `TREE_DIFF_COMMAND` changed with it: it is now `git diff --no-color --no-ext-diff --src-prefix=a/ --dst-prefix=b/ --raw -z --no-renames {before_tree} {after_tree}`, built from the exported `TREE_DIFF_ARGS` tuple so the advertised text and the measurement's executed arguments share one source (`PARSED_DIFF_OPTIONS` plus `--raw -z --no-renames`) — the same delimiter-safe interface the measurement itself reads — because the line-oriented `--name-only` form quotes and escapes a pathname containing a tab or a newline, so a caller who ran the advertised command would hold a different string from the address the response lists and the address the same file is expanded by. `_expansion_detail` states a partial observation's own limit beside its counts, so the two counts are never read as the whole change set.

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
(`git diff --no-color --no-ext-diff --src-prefix=a/ --dst-prefix=b/ --raw -z --no-renames {before_tree} {after_tree}`), so a caller can reproduce the full
source diff even when this operation did not observe it, and the reference
(`diff_knowledge_scope:full-selected-candidate-source-diff`) is a request a caller can act on rather
than a cached artifact whose freshness would have to be trusted.

### Attribution is one partition, and the deleted name is deliberately gone

A path is **attributed** when a registered realization claim **resolves** at it — the recorded bytes
are at the recorded path — in **either** bound snapshot. The measured change population is the
denominator: both snapshots' registered mappings are intersected with it, several links to one path
count it once, and an unchanged mapped path is context and never a change. A path with no resolved
mapping is confirmed unregistered only when every required snapshot/scope was completely inspected
or is a legitimately known-empty side; otherwise its attribution is undetermined, because a side
nobody read is not a side that registered nothing.

**One name left and is deliberately not replaced.** This module used to define
`attributed_paths(comparison)` — every path a *selected* claim named, with no intersection against
the measured change set — and `_unattributed_paths` beside it. That calculation is the one ICR-R04
corrects (an unchanged mapped file incremented the changed-file counter), so both are **deleted**,
not moved: what replaces them is `SourceAttribution.attributed_paths`, the partition value's own
bucket accessor, and no module in the repository imported the old name. The partition arithmetic
itself lives in `memory/knowledge/diff_attribution.py` (`partition_attribution`,
`unavailable_attribution`, `licenses_absence`, `MappingFact`, `SideInspection`, `AttributionReader`)
and the observation vocabulary in `memory/knowledge/tree_observation.py` (`TreeSide`, `TreeChange`,
`TreePaths`, `TreeDifferenceProbe`, `no_tree_difference_probe`); this module re-exports every moved
name, so no importer changed.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The expansion reference and the reproducing command, stated in full so neither needs this module to be read.** [1]
- The fixed presentation order of the limitations. [2]
- **One side's source binding, the changed path, the observation and the seam — the shared vocabulary, re-exported at this seam.** [3]
- **The partition arithmetic, re-exported at this seam: the reader, the mapping fact, the side inspection, the partition and the licensing predicate.** [4]
- **The source half one display is built from: the two sides and the two seams travelling as one measurement.** [5]
- **The one entry point and the order it builds in — filter, omissions from the partition, limitations, expansion from the same one observation.** [6]
- **The limitation table that establishes each declared limit from the omissions beside it, with the undetermined limit's second producer.** [7]
- **The display filter, its two halves both measured in fix round 1, and the role read from whichever side holds the claim.** [8]
- **The per-kind omission for records the other side held but did not select, stated as a selection fact and not a deletion.** [9]
- **The two attribution omissions from the partition: confirmed-unregistered and undetermined, with their two limitations and two reasons.** [10]
- **The deleted selection-only calculation, deliberately not replaced: what replaces it is the partition value's own bucket.** [11]
- The noun and order tables, and the counted noun phrase. [12]
- **The expansion builder: both trees, both roots, the path lists from the same observation, the carried partition and the detail that states what was observed.** [13]
- The production probe, and the read-only handle the row counts are taken through. [14]
- **The node that measures the expansion naming both trees and every differing path, and the node that measures the unattributed gap surviving a filter.** [15]
- **The node that measures the filter narrowing the display and never the comparison.** [16]
- The two nodes that measure an unavailable observation reported as unavailable and a real probe making the gap visible. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The two sides' `root` values are where the
application layer runs the published command, and this module never runs it.

No meaningful cross-repo references found.
