# mcp/src/agents_remember/application/review_source_inventory.py

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

The pane projection lives here too, because it is the same responsibility seen from the surface:
the source pane is the inventory plus the measured attribution partition of that same inventory.
Nothing in this module selects a record, ranks a path or states what a change means.

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
observation measures one review rather than two. `observed` is the measurement to render for a caller
that has already made exactly this one: the attribution partition counts that same observation as its
denominator, and handing it in is what keeps the inventory and the partition two renderings of one
measurement rather than two measurements that have to agree. An observation that reported paths
*without* the statuses beside them is still listed — one entry per path, each stating that its status
and content were not measured — because the alternative is a measured-empty list, which is the one
thing a partial observation must never become. `listed_total` is the length of the list beside it,
and an unavailable observation lists nothing.

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

**`source_pane` is the inventory plus the measured partition of that same inventory, in that
order.** The inventory is the pane's first required field and is present whether or not a knowledge
comparison was made. `attribution` is the partition of those same changes — one accounting at the
changed-path granularity of which of them either bound snapshot registers a valid mapping for — and
every attribution field and count below is read from it rather than recomputed from the displayed
items. That is the correction this pane needed: the three buckets are disjoint and exhaustive over
the measured changes, so an unchanged mapped file can no longer appear in a list of changed ones,
and a path whose attribution a side's silence left undetermined is carried beside the two
conclusions instead of being folded into either. A selection filters attribution, never the source
changes in the declared comparison.

**The pane's recorded-association half is `ICR-R08@v1`'s, and this module composes it rather than
re-deriving it.** `source_pane` takes the traversed `relationships` sequence (defaulting to the empty
tuple, so the module still renders a pane for a caller that traversed nothing) and renders the
address view through the traversal module's own `source_locations`, which is exactly what this module
used to build itself: one location per recorded realization side, each carrying the identity both
sides sit under and the movement it belongs to. The three private helpers that built it here —
`_location`, `_realization_read_item` and `_change_state` — **moved out** when the relationship
vocabulary arrived; `_location` and its address helpers now live in
`application/review_relationship_display.py`, and the change state is
`application/review_recorded_relationships.py`'s `recorded_change_state`. Nothing is duplicated: the
pane composes one implementation, and the local helpers that measured the source change set
(`_RawRecord`, `_raw_records`, `_content_classification`, the limit helpers) are untouched.

**The counts state their unit and their scope, or their reason.** `_remaining` gained the sixth row,
`unknown_attribution_changed_paths`, so the confirmed-unregistered zero and the undetermined count
are visible together in the list the dashboard already renders; `_outside_selection_total` renders
the outside-selection count only when a subject was selected, `_unregistered_reason` and
`_undetermined_reason` state each count's scope, and each count with no value carries its own
reason constant rather than sharing one spelling. `attribution_limitations` renders the partition's
two facts in the same spelling the comparison route uses
(`limitation:unknown_attribution_changed_paths` plus `omitted:attribution_not_determined:N`), and an
unmeasured partition declares the limitation with **no** counted omission — a count of 0 would be
the measured zero the requirement forbids.

### Conventions

`__all__` publishes the ten names the adapter consumes: `SOURCE_INVENTORY_REFERENCE`,
`attribution_limitations`, `byte_form`, `inventory_command`, `inventory_limitations`, `is_text_path`,
`review_inventory`, `source_pane`, `source_tree_side` and `tree_difference_observation`. `_RawRecord` and `TreeChange` are frozen
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
  `memory/knowledge/tree_observation.py`, re-exported by `memory/knowledge/diff_display.py`) refuses
  a value whose `paths` are not exactly its entry paths, and refuses an `unrepresentable` path on an
  observation that is not `partial`.
- **`listed_total` is the length of the list beside it**, enforced by
  `ReviewSourceInventory`'s validator, so a count can never describe a population the response does
  not carry.
- **The advertised command is the interface the measurement used.** `inventory_command` prints
  `git diff --raw -z --no-renames …`, and `memory/knowledge/diff_display.py`'s `TREE_DIFF_COMMAND`
  was changed to the same spelling for the same reason: the address a reader acts on must be the one
  the response preserved.
- **The pane is the inventory plus the measured partition.** This module adds no selection,
  no ranking and no meaning; every attribution field is read from the partition value rather than
  recomputed, and an unmeasured partition declares its limit with no counted omission rather than
  reporting zero.
- **Rank.** `serving` may not import `application`, so the pane the HTTP surface renders is composed
  at this tier and reached through the adapter the composition root wires.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the `TreePaths`/`TreeChange`/`TreeDifferenceProbe` vocabulary it fills in
`memory/knowledge/diff_display.py`, the review models it builds, the adapter that calls it, and the
cases that measure it against real repositories. Three details a reader should carry: the observation
is **one** implementation now, shared with the comparison's expansion through
`knowledge_diff.git_tree_difference_probe`; the two Git questions are `--raw -z` for status and modes
and `--numstat -z` for renderability, each asked once per measurement; and a non-UTF-8 name is a
*partial* result rather than a refusal, because the alternative discards a whole source review for one
odd name.

- The module's own statement of the three properties it exists for — measured from the pair, delimiter-safe, three separate facts with a failed measurement as a state — and of why the pane lives beside it. [1]
- The published surface: the one reference constant, the probe, the inventory, the pane projection and the three limit helpers. [2]
- **The two Git questions, once each, with `--no-renames` and `-z` and the reason for both.** [3]
- The status vocabulary that names Git's letters and states `unknown` for a letter outside it, and the two modes that decide a path's kind before any byte is read. [4]
- The stated reasons an inventory carries: an uncomparable pair, an output that is not the declared format, a tree without its root, an unclassified content, an unstated status and an unrepresentable name. [5]
- The observation's own record: Git's two modes, the change letter, the raw path, and the two properties the mode answers (submodule, symlink) plus the one that separates "the bytes moved" from "only the permission word moved". [6]
- **One bound endpoint as the observation's own side: an object id and the root it resolves in, travelling together or not at all.** [7]
- **The declared limits: unavailable, partial, or neither — stated at the top level of the response because a limit a reader has to open a pane to find was not stated.** [8]
- **The measurement itself: the two object ids, the delimiter-safe read, the content classification, the partition into carried and uncarried changes, and the unavailable answers that are never empty change sets.** [9]
- **The non-UTF-8 boundary: the predicate that observes a surrogate-escaped byte and the exact byte form that carries the name instead of re-encoding it.** [10]
- **The kind of one entry, decided by mode first and measurement second, and the reason an `unknown` is unknown.** [11]
- **The command that reproduces the inventory, naming the two requested objects and never a branch, a working tree or `HEAD`.** [12]
- **The review's own inventory value: the injectable probe seam, the already-made observation a caller hands in, the paths-without-statuses rendering, the measured/unavailable state, the count that is the list's own length, and the unrepresentable remainder.** [13]
- The sentence a measured inventory publishes about itself, including the one that separates a measured empty set from an unmeasured one. [14]
- **Pane 2: the inventory first and unconditionally, then the measured partition it is read from, the address view the recorded-relationship traversal renders, the relationships themselves, the six remaining counts, expansion and the three bucket lists.** [15]
- **The scope of each count and the two partition facts in the comparison route's spelling.** [16]
- The selected source location, now rendered by the recorded relationship's own display owner from the movement side (this module no longer builds it): the recorded role kept `None` rather than guessed, the comparison's own change state carried, and the counterpart address named only when the other side records exactly one. [17]
- The comparison's own statement about one claim's source observation, carried verbatim by the recorded-relationship owner (the moved `_change_state`), and the union-item payload the recorded side is read from. [18]
- **The wire value this module builds, with the count checked against the list and the unrepresentable rule enforced at construction.** [19]
- **The comparison's own expansion, which had been the second implementation of this question and is now a delegation to this module's observation.** [20]
- The adapter's composition: the observation made once and handed to both renderings, before any dataset is opened and before the selector branch, and its limits declared at the top level. [21]
- **The cases that measure this module against real repositories: population and per-path status against an independent Git observation, the tab/newline name, one entry per renderability kind, unavailable versus measured-empty with its control, the paths-only partial rendering, and the non-UTF-8 byte form.** [22]
- The independent, byte-safe Git observation both review suites compare against, deliberately a different Git question and deliberately read through the production runner. [23]
- **The cases that measure the inventory through the real composition and the real route: no knowledge at all, an unusual name carried by the shipped capture, non-text and mode-changed paths, and a non-UTF-8 name that leaves the review openable and partial.** [24]
- The surface that renders the inventory in all three of its states, with the byte-form rows beside the named ones. [25]
- The complete inventory remains navigable at its listed generation; source expansion is centralized and byte-form names stay explicitly unaddressable. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's Git objects through
the shipped runner and carries no identity that ranges beyond the repository namespace the request
names.

No meaningful cross-repo references found.
