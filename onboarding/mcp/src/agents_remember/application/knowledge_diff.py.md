# mcp/src/agents_remember/application/knowledge_diff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_diff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T08:30:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The application seam for the baseline-to-candidate comparison (`KS-R08`): one selector, two explicit
sides, one bounded display.** It is the **sixth** composition seam over the experimental knowledge
substrate, beside the candidate write (`knowledge.py`), the candidate lifecycle/publication
(`knowledge_snapshot.py`), the guarded merge (`knowledge_merge.py`), the portable export/import
(`knowledge_export.py`) and the selective read (`knowledge_read.py`). Like them it decides no authority
and holds no durable state.

## Code Commentary

### Logic

Four entry points, and each answers a different caller:

| Entry point | What it does |
| --- | --- |
| `open_diff_side(database_path, repository_id, *, repository_root, code_tree_id)` | resolves **one side** from the identity the file at that path actually holds — the same discipline as `open_read_context`, so a caller cannot hand-write the snapshot a side is verified against. A worktree candidate database is a supported side: nothing here requires a commit, a ledger row or a leaf |
| `git_tree_difference_probe(before, after)` | the production `TreeDifferenceProbe`, now **one call**: the observation is `application/review_source_inventory.py`'s `tree_difference_observation`, which the review's own inventory reads too. Two implementations of "what did these two trees change" would be two answers to one question, and re-parsing paths is how a name containing a tab or a newline stops being an address |
| `diff_knowledge_scope(request, *, before_path, after_path, probe=None)` | the operation itself |
| `diff_row_counts(database_path)` | one row count per canonical table, read through the same read-only handle — the measurement half of "a refused comparison persisted nothing" |

**The two database paths are separate arguments rather than fields of the sides**, because a side is an
*identity* and a path is *where the bytes currently are*; a request whose sides carried paths would make
a resolved context and a filesystem location the same value.

**The ordered sequence inside `diff_knowledge_scope`**, and each step runs before the next:

1. Both files must exist, or the result is `selected_input_unavailable` **without a binding** (a side
   that never resolved to a file cannot be bound to one).
2. The binding is computed, and a continuation is decoded and checked **before either file is opened**.
3. Both files are opened read-only, and **both sides are verified before either is selected** — so a
   comparison cannot report a union built from one verified snapshot and one file that turned out not to
   be the snapshot it declared.
4. `select_recorded_scope` runs **once per side**, on that side's own connection.
5. `compare_selected_scopes` builds the union; the per-side absences are collected beside it.
6. An empty union refuses; otherwise `build_display` runs with one `SourceObservation` — the probe,
   the two sides and the registered-mapping reader over this comparison's own two open snapshots —
   and the page is cut at the cursor's position.

**The partition is decided from exactly the bytes the selection was made from.**
`_registered_mapping_reader` closes over the two connections this comparison already opened, so there
is no second open, no second namespace and no possibility of the two halves being read at two
different instants. The reader is a closure rather than a value computed here because the measured
paths are not known until the source observation has been made, and that observation belongs to the
display.

**The one Git question this seam asks is now asked in one place.** `git_tree_difference_probe` delegates to
`tree_difference_observation`, so the comparison's expansion and the review's status-bearing inventory read
the *same* observation rather than two that could disagree: the paths an expansion lists are the paths the
inventory measured, from the same two object ids, through the same NUL-delimited interface. What this
module still owns is the seam's *shape* — a callable `TreeDifferenceProbe` a caller may substitute — not
the measurement behind it.

### The four boundaries this seam owns

1. **The selection is R07's, run twice.** Each side goes through
   `select_recorded_scope(connection, SelectionQuery(seed=…, resolve_anchor=…, seed_override=side.selector))`.
   This module contributes **no relevance rule**: the only thing it adds to the selection contract is
   that a side may name its own exact revision.
2. **A candidate change invalidates a continuation, because the binding says so.** The cursor binds a
   digest over both declared snapshots, both resolved contexts, both code trees and both selectors, so a
   candidate whose bytes moved presents another `after` identity and is refused with
   `continuation_binding_mismatch` **rather than continued**. The invalidation is the binding, not a
   check someone has to remember to write.
3. **A missing side refuses, and no `HEAD` is substituted.** An absent or unreadable database, or a side
   naming a snapshot the file does not hold, is refused by name. Nothing here reaches for a working
   tree, a branch or `HEAD`: the expansion's command names the two **requested** trees, and a side that
   named no tree is reported as having requested none.
4. **Absence on one side is reported, not raised.** A selection that refuses on one side while the other
   holds records still serves the union and carries that side's absence on the result — which is what
   "the removed before-side realization remains in the diff" means at the seam. The operation refuses
   outright only when **neither** side selected anything.

**`_side_snapshot_refusal` runs three separate comparisons per side** — namespace binding, schema
generation, logical digest — and the schema check is its own statement rather than a corollary of the
digest, because a context can declare a generation the file does not hold while keeping a digest that
happens to match. All three surface as `snapshot_unavailable` with the comparison that fired in `detail`.

**The cursor's request-level bindings are decided first.** `_cursor_mismatch` checks the policy, then the
selector digest, then the display filter, then the comparison binding digest, in that order, so a caller
who changed the **question** is told that rather than being sent to re-select a dataset they selected
correctly. A caller who changed both is told about the question — the part they can see — and the
snapshot pair is reported once the request agrees.

**`_page` states the walk's arithmetic honestly.** `items_total` is the whole comparison on every page,
`items_returned` is cumulative, `items_remaining` is what is ahead, and `displayed_total` /
`suppressed_total` are the display's own two numbers travelling on every page, so a filter cannot be
mistaken for a shorter comparison. `has_more` is `returned > 0 and leftover > 0`, so a page that returned
nothing does not advertise a continuation it cannot serve.

**The two absence codes are R07's own, applied per side.** `_side_absence_refusal` returns
`registration_absent` for a path selector (a right question whose answer is that nothing is recorded
there) and `selector_absent` when the side's snapshot does not record the named identity or revision —
and `_selector_is_recorded` asks the same question R07's seam asks, so a **recorded** identity whose
selected revisions carry no memberships and no claims is an empty but real selection rather than an
absence.

**`diff_knowledge_scope` never raises for a caller to catch.** `SelectionIncomplete`,
`KnowledgeStorageError`, `apsw.Error` and `OSError` are each caught and mapped by `_reading_failure` onto
a typed refusal that names its own fact: the declared selection bound, a file that is not the declared
snapshot, a SQLite failure, or a file that could not be read at all.

### Conventions

- `_effective_selector(side, request.selector)` is the one place the per-side override is resolved for
  the binding, so the digest a continuation is checked against is the digest of the selector that side
  **actually selects with**.
- `SnapshotPair` / `OpenPair` / `OpenComparison` group values that must not be crossed: a helper handed
  a request, a binding, a connection pair and a probe separately could be handed one comparison's binding
  with another's connection.
- `_SELECTOR_KINDS` names each seed kind by its own discriminator, so a selector kind added later is
  reported by its own name rather than as a neighbouring one, and `_selector_id` writes the narrowing out
  rather than reaching through `getattr`.
- `_TREE_DIFF_ARGS` used to carry the probe's Git arguments here; **this leaf deleted it**, because the
  observation moved to `application/review_source_inventory.py` and the two Git questions it asks
  (`--raw -z` for status and modes, `--numstat -z` for whether content is text) are now stated once,
  beside the measurement the review's own inventory reads. `--no-renames` is still deliberate and still
  lives there: a rename is a deletion of one path and an addition of another, and reporting a rename would
  attribute the candidate's **new** path to a baseline path that no recorded anchor names.

### Invariants And Boundaries

- **Read-only by construction.** Both connections are opened through `open_read_only_database`, so the
  strongest statement available is a `SELECT`; "a refused comparison persisted nothing" is a property of
  the handle, not a rollback the code remembers.
- **No task, no leaf, no enclosure.** Nothing on this path resolves a task reference; a comparison of a
  baseline and a worktree candidate needs no final memory commit.
- **The wiring boundary did not move.** Like its five siblings, this module has **no non-test importer in
  `mcp/src`**, and no MCP tool name is introduced here — the requirement's own boundary keeps the public
  tool name separate from the concrete application function.
- **The request shape cannot carry a second relevance rule.** See `models/knowledge/diff.py`'s card for
  the closed `seed_override` question; the alternative the packet forbids is not constructible here
  either.
- **Boundary.** This module composes: it resolves sides, verifies snapshots, delegates selection and
  comparison, builds the display, pages it and types every failure. It does not select records itself,
  does not compare them itself and does not decide what a change means.

### Todos

None recorded. The two carried forward obligations belong to the owning seat and are recorded in the
ledger rather than here: the **`M23` reachability bound** (a non-experiment whose closing input is named
in `memory/knowledge/diff.py`'s card) and the fixture debt that the **family half of rule 2 is
unexercised** because no fixture authors a `family_predecessor` row. The leaf's contested evidence items
were carried to `KS-R09`/`L9` (ledger entries **A9**/**A10**).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The row-count measurement, and the one statement shape this module runs that changes nothing.** | `diff_row_counts`; `ROW_COUNT_TEMPLATE` | mcp/src/agents_remember/application/knowledge_diff.py:850-864; mcp/src/agents_remember/application/knowledge_diff.py:129-129 |
| **The side resolver: the identity comes from the file, and the root/tree pair is supplied together or not at all.** | `open_diff_side` | mcp/src/agents_remember/application/knowledge_diff.py:132-163 |
| **The production probe, now a one-line delegation: the two trees addressed by object id, the never-substitute-`HEAD` rule, and the delimiter-safe observation the review's own inventory reads too.** | `git_tree_difference_probe`; `tree_difference_observation`; `source_tree_side` | mcp/src/agents_remember/application/knowledge_diff.py:166-181; mcp/src/agents_remember/application/review_source_inventory.py:194-236; mcp/src/agents_remember/application/review_source_inventory.py:168-176 |
| **The one operation: the ordered sequence, the injectable probe default and the typed catch of selection/storage/SQLite/OS failures.** | `diff_knowledge_scope` | mcp/src/agents_remember/application/knowledge_diff.py:184-238 |
| The four input classes a failed read is mapped onto, each naming its own fact. | `_reading_failure` | mcp/src/agents_remember/application/knowledge_diff.py:241-264 |
| The binding computed before either file is opened, and the per-side effective selector it digests. | `_binding`; `_effective_selector`; `_resolve_sides` | mcp/src/agents_remember/application/knowledge_diff.py:295-320; mcp/src/agents_remember/application/knowledge_diff.py:315-320; mcp/src/agents_remember/application/knowledge_diff.py:267-293 |
| The values that must not be crossed: the snapshot pair, the connection pair and the whole opened comparison. | `SnapshotPair`; `OpenPair`; `OpenComparison`; `_compare_inside_one_snapshot_pair` | mcp/src/agents_remember/application/knowledge_diff.py:322-380 |
| **The ordered body: verify both sides before either selection, select each side with R07's own policy, compare, collect absences, display with the comparison's own mapping reader, page.** | `_select_and_compare`; `_select_side` | mcp/src/agents_remember/application/knowledge_diff.py:382-449; mcp/src/agents_remember/application/knowledge_diff.py:506-523 |
| **The registered-mapping reader over this comparison's own two open snapshots — the partition decided from exactly the bytes the selection was made from.** | `_registered_mapping_reader` | mcp/src/agents_remember/application/knowledge_diff.py:451-486 |
| **Both sides verified before either is selected, and the three separate comparisons inside each.** | `_any_side_snapshot_refusal`; `_side_snapshot_refusal` | mcp/src/agents_remember/application/knowledge_diff.py:487-504; mcp/src/agents_remember/application/knowledge_diff.py:768-802 |
| **The page arithmetic: the comparison total on every page, the cumulative returned, the display's own two numbers, and no continuation a page cannot serve.** | `_page` | mcp/src/agents_remember/application/knowledge_diff.py:525-577 |
| The per-side absence vocabulary and the recorded-but-empty selection served rather than refused. | `_side_absences`; `_side_absence_refusal`; `_selector_is_recorded`; `_identity_is_recorded` | mcp/src/agents_remember/application/knowledge_diff.py:580-608; mcp/src/agents_remember/application/knowledge_diff.py:610-623; mcp/src/agents_remember/application/knowledge_diff.py:625-652; mcp/src/agents_remember/application/knowledge_diff.py:654-697 |
| **The empty comparison refused rather than reported as "nothing changed", with the contributing side absences named.** | `_empty_comparison`; `_absence_naming_both` | mcp/src/agents_remember/application/knowledge_diff.py:699-731; mcp/src/agents_remember/application/knowledge_diff.py:724-731 |
| **The cursor check order: policy, selector, filter, then the snapshot pair.** | `_cursor_mismatch` | mcp/src/agents_remember/application/knowledge_diff.py:733-766 |
| The typed refusal constructors that bind a refusal to the comparison identity, and the one that cannot bind because a side never resolved. | `_unusable`; `_refused`; `_refused_without_binding` | mcp/src/agents_remember/application/knowledge_diff.py:804-812; mcp/src/agents_remember/application/knowledge_diff.py:814-831; mcp/src/agents_remember/application/knowledge_diff.py:833-848 |
| **The storage layer this seam delegates to: R07's one selection policy, applied per side.** | `select_recorded_scope` | mcp/src/agents_remember/memory/knowledge/read.py:193-238 |
| **The union comparison and the display builder this seam calls.** | `compare_selected_scopes` | mcp/src/agents_remember/memory/knowledge/diff.py:200-264 |
| **The display builder, which turns one comparison into a page's items, omissions, expansion and carried partition.** | `build_display` | mcp/src/agents_remember/memory/knowledge/diff_display.py:157-200 |
| **The node that measures a real candidate write refusing its continuation, and the node that measures a side naming another snapshot of its own file refusing before any page.** | "test_a_candidate_that_changed_after_a_continuation_refuses_the_continuation"; "test_a_side_naming_another_snapshot_of_its_own_file_refuses_before_any_page" | mcp/tests/test_knowledge_diff_boundaries.py:325-363; mcp/tests/test_knowledge_diff_boundaries.py:438-475 |
| The nodes that measure a missing side refusing without a substitute, a continuation against another selector returning no page, and a small budget not shrinking the totals. | "test_a_missing_side_refuses_and_substitutes_no_other_snapshot"; "test_a_continuation_presented_against_another_selector_refuses_and_returns_no_page"; "test_a_small_display_budget_pages_the_comparison_without_shrinking_its_totals" | mcp/tests/test_knowledge_diff_boundaries.py:303-322; mcp/tests/test_knowledge_diff_boundaries.py:408-435; mcp/tests/test_knowledge_diff_boundaries.py:257-297 |
| **The node that measures the paging rule through the public seam: a page of a selection is what the comparison displays, not what it selected.** | "test_a_page_of_a_selection_is_what_the_comparison_displays_not_what_it_selected" | mcp/tests/test_knowledge_diff_boundaries.py:708-749 |
| The last nodes of the population: no mounted UI and no approval the comparison cannot make. | "test_a_comparison_names_no_mounted_ui_and_no_approval_it_cannot_make" | mcp/tests/test_knowledge_diff_boundaries.py:752-771 |
| The comparison request, the side that names one snapshot and its selector, and the typed result. | `KnowledgeDiffRequest` | mcp/src/agents_remember/models/knowledge/diff.py:260-269 |
| The result that is a page or a refusal, never both. | `KnowledgeDiffResult` | mcp/src/agents_remember/models/knowledge/diff.py:733-829 |
| One side of a comparison: the exact snapshot and the per-side selector. | `KnowledgeDiffSide` | mcp/src/agents_remember/models/knowledge/diff.py:197-220 |
| **The one operation member this seam's results carry.** | "diff_knowledge_scope" | mcp/src/agents_remember/models/knowledge/result.py:87-87 |

## Cross-Repo References

The comparison names two **code trees** by object id and runs one Git command in the root a side named.
Both are values the caller resolved; no ledger, coordination path or second repository is read here, and
the module never consults a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **three enforced rows re-cited.** `_resolve_sides`, `_identity_is_recorded` and `_refused_without_binding` now cite their declarations (`267-293`, `654-697`, `833-848`) instead of neighbouring ranges. Wording unchanged; no stamp advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the comparison supplies the attribution reader (819 → 866 lines).** `_select_and_compare` builds one `SourceObservation` — probe, two sides, and `_registered_mapping_reader` over this comparison's own two open connections — so the partition is decided from exactly the bytes the selection was made from, with no second open and no second namespace. The ordered-sequence section records the new step 6 and the closure's reason (the measured paths are not known until the display observes them). Every reference row was re-derived against this candidate. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the probe became a delegation, and the line-oriented Git interface left this module.** `git_tree_difference_probe` is now one call to `application/review_source_inventory.py`'s `tree_difference_observation`, so the comparison's expansion and the review's own inventory read one measurement instead of two that could disagree; the private `_TREE_DIFF_ARGS` (`diff --name-only --no-renames`) and the `splitlines()` that consumed it are **deleted**, and the two Git questions the observation now asks (`--raw -z` for status and modes, `--numstat -z` for renderability) are stated once, beside the measurement. The consequence the card now records: a name containing a tab or a newline survives as the address it is expanded by, because the interface that reads paths is NUL-delimited; over the same real pair the removed `--name-only` interface returned `"src/tab\tnewline\nname.py"` (quoted and escaped) for a file the leaf holds. The two ranges this moved were re-derived against this candidate: the deleted constant's paragraph in Conventions and the reference row for the probe, which now cites the observation it delegates to. **Stamp accounting:** the verification rows still name `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`, the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; the claims whose evidence this leaf's own change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the comparison's application seam — the route's **sixth** composition seam, with four entry points (`open_diff_side`, `git_tree_difference_probe`, `diff_knowledge_scope`, `diff_row_counts`). It records the four boundaries the seam owns: **R07's selection run twice** with the per-side exact-revision address as the only addition to the selection contract; **the binding as the invalidation** (a candidate whose bytes moved presents another `after` identity and is refused rather than continued); **a missing side refuses with no `HEAD` substituted** and an absent/unreadable file refused without a binding at all; and **one side's absence reported, not raised**, with the operation refusing outright only when neither side selected anything. It states the ordered sequence with the two properties that make it safe (both sides verified **before either is selected**; the request-level cursor checks decided **before** the comparison binding so a caller who changed the question is told that), the three separate snapshot comparisons per side, the page arithmetic (`items_total` on every page, the display's own two numbers travelling beside it), the two R07 absence codes with the recorded-but-empty selection served rather than refused, the four typed failure classes `_reading_failure` maps, and the two non-claims the module's own docstring carries. It also records that the wiring boundary did **not** move — like its five siblings the seam has **no non-test importer in `mcp/src`** and introduces no MCP tool name. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
