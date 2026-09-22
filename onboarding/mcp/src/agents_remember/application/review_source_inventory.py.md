# mcp/src/agents_remember/application/review_source_inventory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_source_inventory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; base `702714fc05363cb28eacaf101ba8384475a6aa56` |
| lastVerifiedCommitHash | `d21bc8a6c5d30e2394a72d056bff216b766407c2` |
| lastVerifiedCommitDate | 2026-09-22T08:22:57+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The one owner of the **source half** of a review: the exact, status-bearing change inventory of a
bound tree pair, and the pane that renders it. A review is a comparison between two bound Git object
identities and, independently of that, between two knowledge datasets; this module owns the first
half only, and it owns it as **one measurement**.

Three properties are the reason the module exists rather than living inside the review adapter:

1. **The inventory is measured from the pair, not from a knowledge selection.** Nothing here reads a
   database, a claim or an invariant, so a candidate that records no subject — or whose datasets do
   not exist at all — still has its complete source change inventory. That is the packet's entry
   requirement: the task context is the entry, and knowledge availability cannot remove a source
   change from the list.
2. **Every path is an address, so the Git interface is delimiter-safe.** Git quotes and escapes a
   pathname containing a tab or a newline when it prints lines, and a reader that split those lines
   would hold a *different* string from the one the file is reached by. The observation therefore
   reads NUL-delimited records and never splits on whitespace inside a name.
3. **Status, mode and renderability are three separate facts, and a failed measurement is a state
   rather than an empty list.** An addition, a deletion, a modification, a type change, a mode-only
   change, a symlink and a submodule pointer each keep their own entry, and one whose content cannot
   be rendered says so instead of disappearing. A failed measurement publishes `unavailable` with the
   reason; a partially-carried one publishes `partial` with its entries intact — never a fabricated
   empty list labelled complete.

The pane projection lives here too, because it is the same responsibility seen from the surface: the
source pane is the inventory plus the attribution facts the shipped comparison already owns. Nothing
in this module selects a record, ranks a path or states what a change means.

**Why it is a module and not a function in the adapter.** The review adapter is over the repository's
file-size rail, its Scope required the touched responsibility to move out before behavior was added,
and the extraction had a second reason of its own: `application/knowledge_diff.py`'s
`git_tree_difference_probe` used to be a *second* implementation of "what did these two trees change"
(line-oriented, `--name-only`). It is now a one-line delegation to
`tree_difference_observation`, so the comparison's expansion and the review's inventory read one
observation rather than two that could disagree.

## Code Commentary

### Logic

**`tree_difference_observation` is the production `TreeDifferenceProbe`, and it answers with a
status-bearing entry per path.** It compares two sides only when each named an exact tree **and** is
resolvable in the root it named; anything else is reported as an observation this run could not make,
never as an empty change set, and the two trees are addressed by object id and never by a branch, a
working tree or `HEAD`. It runs `git diff --raw -z --no-renames` once for status and modes and
`git diff --numstat -z --no-renames` once for whether content is text at all; a failure of the second
run does not lose the path set — the entries stay, each stating that its content was not classified,
and the observation is `partial`. `--no-renames` is deliberate and is the shipped comparison's own
policy: a rename is a deletion of one path and an addition of another, and reporting a rename would
attribute the candidate's *new* path to a baseline path no recorded anchor names.

**`_raw_records` refuses the whole observation rather than skipping a record.** The `-z` form is a
NUL-terminated alternation of one metadata field and one path, so it is read as exactly that: an odd
token count, a metadata row that does not begin with `:`, a row that does not carry Git's five fields
or an empty path each mean the output is not this interface's and the observation is `unavailable`.
Paths are carried verbatim — split on NUL and never trimmed — because the name *is* the address the
same file is expanded with. Two trees that agree print nothing at all, and that one case is read as a
**measured empty** change set rather than as a malformed one.

**The content classification consults the mode first, then the measurement.** A gitlink (`160000`) is
a submodule pointer and a symlink (`120000`) is a link target; neither is text or binary in the sense
`--numstat` measures, so the mode decides those two and everything else is answered by the numstat
measurement. A path that measurement did not cover is `unknown` — with the reason stated on the
entry — rather than assumed to be text.

**Two honesty rules make one measured population out of two lists.** A changed path whose **name** is
not valid UTF-8 decodes to lone surrogates (`U+DC80`-`U+DCFF`), which this surface's own text fields
refuse; `is_text_path` is where that is observed and `byte_form` renders such a path as its exact
bytes in an ASCII-safe spelling (`b'src/caf\xe9-latin1.py'`). The measured changes are partitioned
into `entries`/`paths` (the text-representable ones) and `unrepresentable` (the rest, kept in full),
`partial` is set, and `detail` names the byte form. Nothing is re-encoded — a re-encoded name would
address a file this repository does not hold — and nothing is dropped, because a partial change set
must never read as a whole one.

**`review_inventory` is the review's own value for one pair, and it is honest about resolution.**
`probe` is the same injectable observation seam the comparison takes, so a case that substitutes an
observation measures one review rather than two. An observation that reported paths *without* the
statuses beside them is still listed — one entry per path, each stating that its status and content
were not measured — because the alternative is a measured-empty list, which is the one thing a
partial observation must never become. `listed_total` is the length of the list beside it, and an
unavailable observation lists nothing.

**The states, and what each one says.** `state="measured"` means this list is the whole change set of
the pair, including the measured empty set two identical trees produce, and a measured empty set says
so in its own words ("the two requested code trees hold identical content … which is a measured empty
change set and not an unmeasured one"). `state="unavailable"` means nothing was observed, and the
`detail` carries the reason — an unresolvable root, a tree this repository does not hold, an output
that is not the declared format. `partial=True` is the third fact and is not a weaker measurement of
the path set: every changed path is listed and one field of some entries could not be reported.

**`inventory_command` names the two requested object ids and the root they were compared in**, never a
branch, a working tree or `HEAD`, so a caller can reproduce the whole change set from the value
without reading this module — and reproducing it cannot silently become a comparison of whatever is
checked out now. A side that named no tree is stated as such rather than substituted.

**`inventory_limitations` declares the inventory's own state at the top level of a response**, which
is what `knowledge_review._limitations` calls: `limitation:source_inventory_unavailable` or
`limitation:source_inventory_partial`, plus nothing when there is no limit. A limit a reader has to
open a pane to discover is a limit the response did not state.

**`source_pane` is the inventory plus the comparison's own attribution facts, in that order.** The
inventory is the pane's first required field and is present whether or not a knowledge comparison was
made; the selected locations, the five published remaining counts, the expansion reference and command
and the attributed/unattributed path lists are carried from the shipped comparison **verbatim** when
there is one, and stated as *not measured* — each with its own reason — when there is not. A selection
filters attribution, never the source changes in the declared comparison.

### Conventions

`__all__` publishes the nine names the adapter consumes: `SOURCE_INVENTORY_REFERENCE`, `byte_form`,
`inventory_command`, `inventory_limitations`, `is_text_path`, `review_inventory`, `source_pane`,
`source_tree_side` and `tree_difference_observation`. `_RawRecord` and `TreeChange` are frozen
dataclasses, not pydantic models: they are the observation's own value while it is being built, and
only `ReviewSourceInventory` (in `models/knowledge/review.py`) is a wire shape. The module's detail
strings are module-level constants rather than inline sentences (`_UNCOMPARABLE_DETAIL`,
`_UNPARSED_DETAIL`, `_NO_ROOT_DETAIL`, `_UNCLASSIFIED_DETAIL`, `_UNSTATED_DETAIL`,
`_UNLISTED_CONTENT_DETAIL`, `_UNREPRESENTABLE_DETAIL`), because two callers and three states have to
state the same limit identically. `_count(count, noun)` is the one counted-noun phrase, so a stated
limit reads as a measurement. There is no state: every function is pure apart from the two Git
subprocesses, and nothing here writes a file.

### Invariants And Boundaries

- **It reads Git and nothing else.** No database, no claim, no invariant and no knowledge selection
  reaches this module, which is exactly why a task with no knowledge still has a source review.
- **A pathname is bytes.** The observation is NUL-delimited, a path is carried whole, and a name that
  is not valid text is carried by its exact byte form rather than re-encoded, dropped or raised on.
- **A failed measurement is a state, never an empty list.** `unavailable` carries its reason and lists
  nothing; `measured` with zero entries is the different sentence for two trees that agree.
- **Paths and entries are one measurement.** `TreePaths.__post_init__` (in
  `memory/knowledge/diff_display.py`) refuses a value whose `paths` are not exactly its entry paths,
  and refuses an `unrepresentable` path on an observation that is not `partial`.
- **`listed_total` is the length of the list beside it**, enforced by
  `ReviewSourceInventory`'s validator, so a count can never describe a population the response does
  not carry.
- **The advertised command is the interface the measurement used.** `inventory_command` prints
  `git diff --raw -z --no-renames …`, and `memory/knowledge/diff_display.py`'s `TREE_DIFF_COMMAND`
  was changed to the same spelling for the same reason: the address a reader acts on must be the one
  the response preserved.
- **The pane is the inventory plus the comparison's own values.** This module adds no selection,
  no ranking and no meaning; where the comparison is absent, the counts state that they were not
  measured rather than reporting zero.
- **Rank.** `serving` may not import `application`, so the pane the HTTP surface renders is composed
  at this tier and reached through the adapter the composition root wires.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the `TreePaths`/`TreeChange`/`TreeDifferenceProbe` vocabulary it fills in
`memory/knowledge/diff_display.py`, the review models it builds, the adapter that calls it, and the
cases that measure it against real repositories. Three details a reader should carry: the observation
is **one** implementation now, shared with the comparison's expansion through
`knowledge_diff.git_tree_difference_probe`; the two Git questions are `--raw -z` for status and modes
and `--numstat -z` for renderability, each asked once per measurement; and a non-UTF-8 name is a
*partial* result rather than a refusal, because the alternative discards a whole source review for one
odd name.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the three properties it exists for — measured from the pair, delimiter-safe, three separate facts with a failed measurement as a state — and of why the pane lives beside it. | `partial`; `available` | mcp/src/agents_remember/application/review_source_inventory.py:1-30 |
| The published surface: the one reference constant, the probe, the inventory, the pane projection and the two limit helpers. | `__all__`; `SOURCE_INVENTORY_REFERENCE` | mcp/src/agents_remember/application/review_source_inventory.py:65-79 |
| **The two Git questions, once each, with `--no-renames` and `-z` and the reason for both.** | `_RAW_ARGS`; `_NUMSTAT_ARGS` | mcp/src/agents_remember/application/review_source_inventory.py:81-87 |
| The status vocabulary that names Git's letters and states `unknown` for a letter outside it, and the two modes that decide a path's kind before any byte is read. | `_STATUS_NAMES`; `_SUBMODULE_MODE`; `_SYMLINK_MODE` | mcp/src/agents_remember/application/review_source_inventory.py:89-102 |
| The stated reasons an inventory carries: an uncomparable pair, an output that is not the declared format, a tree without its root, an unclassified content, an unstated status and an unrepresentable name. | `_UNCOMPARABLE_DETAIL`; `_UNPARSED_DETAIL`; `_NO_ROOT_DETAIL`; `_UNCLASSIFIED_DETAIL`; `_UNSTATED_DETAIL`; `_UNREPRESENTABLE_DETAIL` | mcp/src/agents_remember/application/review_source_inventory.py:104-140 |
| The observation's own record: Git's two modes, the change letter, the raw path, and the two properties the mode answers (submodule, symlink) plus the one that separates "the bytes moved" from "only the permission word moved". | `_RawRecord` | mcp/src/agents_remember/application/review_source_inventory.py:143-164 |
| **One bound endpoint as the observation's own side: an object id and the root it resolves in, travelling together or not at all.** | `source_tree_side`; `TreeSide` | mcp/src/agents_remember/application/review_source_inventory.py:167-175; mcp/src/agents_remember/memory/knowledge/diff_display.py:87-98 |
| **The declared limits: unavailable, partial, or neither — stated at the top level of the response because a limit a reader has to open a pane to find was not stated.** | `inventory_limitations` | mcp/src/agents_remember/application/review_source_inventory.py:178-190 |
| **The measurement itself: the two object ids, the delimiter-safe read, the content classification, the partition into carried and uncarried changes, and the unavailable answers that are never empty change sets.** | `tree_difference_observation`; `_raw_records`; `_content_classification`; `_changes` | mcp/src/agents_remember/application/review_source_inventory.py:193-235; mcp/src/agents_remember/application/review_source_inventory.py:296-321; mcp/src/agents_remember/application/review_source_inventory.py:341-363; mcp/src/agents_remember/application/review_source_inventory.py:366-383 |
| **The non-UTF-8 boundary: the predicate that observes a surrogate-escaped byte and the exact byte form that carries the name instead of re-encoding it.** | `is_text_path`; `byte_form` | mcp/src/agents_remember/application/review_source_inventory.py:238-260 |
| **The kind of one entry, decided by mode first and measurement second, and the reason an `unknown` is unknown.** | `_content`; `_content_reason` | mcp/src/agents_remember/application/review_source_inventory.py:386-407 |
| **The command that reproduces the inventory, naming the two requested objects and never a branch, a working tree or `HEAD`.** | `inventory_command`; `TREE_DIFF_COMMAND` | mcp/src/agents_remember/application/review_source_inventory.py:410-425; mcp/src/agents_remember/memory/knowledge/diff_display.py:75-78 |
| **The review's own inventory value: the injectable probe seam, the paths-without-statuses rendering, the measured/unavailable state, the count that is the list's own length, and the unrepresentable remainder.** | `review_inventory`; `_entries`; `_unrepresentable_path` | mcp/src/agents_remember/application/review_source_inventory.py:457-465 |
| The sentence a measured inventory publishes about itself, including the one that separates a measured empty set from an unmeasured one. | `_measured_detail` | mcp/src/agents_remember/application/review_source_inventory.py:515-531 |
| **Pane 2: the inventory first and unconditionally, then the comparison's own locations, counts, expansion and attribution lists — carried verbatim, or stated as not measured with a reason.** | `source_pane`; `_remaining` | mcp/src/agents_remember/application/review_source_inventory.py:540-580; mcp/src/agents_remember/application/review_source_inventory.py:583-652 |
| The selected source location with its recorded role kept `None` rather than guessed, and the change state derived from the comparison's own observation. | `_location`; `_change_state`; `_realization_read_item` | mcp/src/agents_remember/application/review_source_inventory.py:655-678; mcp/src/agents_remember/application/review_source_inventory.py:688-694; mcp/src/agents_remember/application/review_source_inventory.py:681-685 |
| **The wire value this module builds, with the count checked against the list and the unrepresentable rule enforced at construction.** | `ReviewSourceInventory`; `ReviewChangedFile`; `ReviewUnrepresentablePath`; `ReviewSourcePane` | mcp/src/agents_remember/models/knowledge/review.py:552-613; mcp/src/agents_remember/models/knowledge/review.py:497-527; mcp/src/agents_remember/models/knowledge/review.py:530-549; mcp/src/agents_remember/models/knowledge/review.py:616-633 |
| **The comparison's own expansion, which had been the second implementation of this question and is now a delegation to this module's observation.** | `git_tree_difference_probe`; `_expansion_detail` | mcp/src/agents_remember/application/knowledge_diff.py:158-173; mcp/src/agents_remember/memory/knowledge/diff_display.py:479-503 |
| The adapter's composition: the inventory measured first and unconditionally, before any dataset is opened and before the selector branch, and its limits declared at the top level. | `compose_review`; `_limitations` | mcp/src/agents_remember/application/knowledge_review.py:371-453; mcp/src/agents_remember/application/knowledge_review.py:644-667 |
| **The cases that measure this module against real repositories: population and per-path status against an independent Git observation, the tab/newline name, one entry per renderability kind, unavailable versus measured-empty with its control, the paths-only partial rendering, and the non-UTF-8 byte form.** | `InventoryFixture`; `build_inventory_fixture`; `test_the_inventory_lists_every_changed_path_of_the_bound_pair_with_gits_own_status`; `test_a_tab_and_a_newline_in_a_filename_survive_as_the_address_of_the_change`; `test_a_path_whose_content_cannot_be_rendered_is_still_listed_with_its_own_kind`; `test_a_measurement_that_could_not_be_made_is_unavailable_and_never_a_measured_empty_set`; `test_a_pathname_that_is_not_valid_text_is_carried_by_its_bytes_and_never_dropped` | mcp/tests/test_knowledge_diff_boundaries.py:898-916; mcp/tests/test_knowledge_diff_boundaries.py:919-967; mcp/tests/test_knowledge_diff_boundaries.py:971-1007; mcp/tests/test_knowledge_diff_boundaries.py:1010-1035; mcp/tests/test_knowledge_diff_boundaries.py:1038-1063; mcp/tests/test_knowledge_diff_boundaries.py:1066-1093; mcp/tests/test_knowledge_diff_boundaries.py:1118-1170 |
| The independent, byte-safe Git observation both review suites compare against, deliberately a different Git question and deliberately read through the production runner. | `independent_changed_records` | mcp/tests/diff_scope_test_support.py:499-513 |
| **The cases that measure the inventory through the real composition and the real route: no knowledge at all, an unusual name carried by the shipped capture, non-text and mode-changed paths, and a non-UTF-8 name that leaves the review openable and partial.** | `test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all`; `test_the_production_inventory_keeps_an_unusual_filename_as_the_address_it_expands_by`; `test_the_production_inventory_lists_non_text_and_mode_changed_paths_it_cannot_render`; `test_a_non_utf8_pathname_leaves_the_review_openable_and_states_why_it_is_partial` | mcp/tests/test_knowledge_review_source_endpoints.py:733-811; mcp/tests/test_knowledge_review_source_endpoints.py:812-855; mcp/tests/test_knowledge_review_source_endpoints.py:856-889; mcp/tests/test_knowledge_review_source_endpoints.py:902-961 |
| The surface that renders the inventory in all three of its states, with the byte-form rows beside the named ones. | `Inventory`; `inventoryEntry`; `byteNamedEntry` | dashboard/src/panels/review/ReviewSurface.tsx:291-335; dashboard/src/panels/review/ReviewSurface.tsx:214-260; dashboard/src/panels/review/ReviewSurface.tsx:270-282 |
| **The row that is now also the way into its own content: the named entry carries the two generation ids the surface is showing, an open control that is present exactly when both ids are, and the rendered content beside it — while the byte-form row states that no expansion request can name it.** | `inventoryEntry`; `byteNamedEntry`; `SourceContent` | dashboard/src/panels/review/ReviewSurface.tsx:214-260; dashboard/src/panels/review/ReviewSurface.tsx:270-282; dashboard/src/panels/review/ReviewSurface.tsx:248-256; dashboard/src/panels/review/ReviewSurface.tsx:298-298; dashboard/src/panels/review/ReviewSurface.tsx:352-352 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's Git objects through
the shipped runner and carries no identity that ranges beyond the repository namespace the request
names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the three enforced findings on this card were re-read and cleared — the module itself did not change; the lines this card cites into other owners did.** (1) The wire-value row cited four ranges into `models/knowledge/review.py` that this leaf's one-line insertion pushed down by one; each range was re-derived from the construct's own extent rather than shifted — `ReviewSourceInventory` `551-612` → `552-613`, `ReviewChangedFile` `496-526` → `497-527`, `ReviewUnrepresentablePath` `529-548` → `530-549`, `ReviewSourcePane` `615-632` → `616-633` — and each anchor verified to occur literally inside its new range. (2) The reopened claim about the dashboard surface was re-read against the current construct and its **wording was retained**: `Inventory` still renders all three inventory states and the byte-form rows still sit beside the named ones. Its ranges were regenerated, because the surface's helpers moved and changed shape when this leaf added the entry-content path: `Inventory` `291-335`, `inventoryEntry` `214-260`, `byteNamedEntry` `270-282` (the old `238-264`/`207-223`/`224-237` held none of the three). (3) Because the claim was reopened by a real structural change, one row was **added** rather than folding the new behaviour into the old claim: the named entry is now also the way into its own content — it carries the two generation ids the surface is showing and an open control present exactly when both ids exist, rendering `SourceContent` beside itself, while the byte-form row states that no expansion request can name it. No existing claim wording was changed, and the two verification rows are deliberately **not** advanced: nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T16:10+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l2`: the governed closeout refused the memory leg because this card for a module that exists only in this leaf's uncommitted candidate carried no verification stamp in its header metadata (`external-memory closeout requires onboarding verification metadata before memory commit`). The two fields were added naming the **production line this card was read against** — `c755cec6…`, the master line after this leaf's resolved syncs brought in the ICR-L5 and ICR-L19 landings, at that closeout's recorded time `2026-09-21T15:29:12+02:00` — and the candidate row was left as it was. This states what the reading was against, not that the module exists in that commit; the closeout's own metadata refresh re-stamps the card against the code commit this transaction creates. No range, claim or anchor was changed by this repair.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): created this one-to-one card for the module this leaf introduced as the review surface's one owner of the **source-change inventory** of a bound tree pair. The card records what the module is for rather than only where the code lives: the inventory is measured from the two bound tree ids and from nothing else, so knowledge availability cannot remove a source change from the list; the Git interface is NUL-delimited (`--raw -z`, `--numstat -z`) because a pathname containing a tab or a newline is an *address* and a line-oriented reader would hold a different string; status, mode and renderability are three separate facts, with binary, symlink, submodule, type-change and mode-only entries all listed; a failed measurement is `unavailable` with a stated reason and never a fabricated empty list; and a changed path whose name is not valid UTF-8 is carried by its **exact byte form** in `unrepresentable_paths` with the inventory marked measured **and** partial, so the two lists together are the whole measured population. It also records the seam the extraction closed: `knowledge_diff.git_tree_difference_probe` is now a one-line delegation to this module's `tree_difference_observation`, so the comparison's expansion and the review's inventory read one observation instead of two. **Stamp accounting:** this card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**, because every construct it cites exists only in this leaf's uncommitted candidate and no real commit contains the content a stamp would claim to have verified; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.
