# mcp/src/agents_remember/cli/knowledge_ingest.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter: ingest an orchestrator's curator hand-off list into a leaf's candidate — the knowledge
write plane's first production caller, and the run that publishes the committed candidate through the
shipped publication owner. Since `260921-ICR-L20` it is also the surface that owns the *destination
selection*: the caller's path (`--publish-to`), the repository's **one declared published dataset
location** (`--publish`, resolved by the read route's own owner), or neither.
**Since `260921-ICR-L32` its own docstring says it is one of the *two* shipped entry points that reach
that writer**, the other being `agents-remember knowledge-bootstrap` on the taskless
repository-foundation route — the module docstring was completed rather than shortened, because the
singular form ("the write plane's production entry point") was true when it was written and incomplete
once the second route shipped.

**Since `260928-MIK-L12` (MIK-R12 rule 7) the memory tree decides which writer runs.** When the
contract's memory worktree is **converted** (it holds `knowledge/layout.json`), `run` hands the whole run
to the curator file writer through `cli/knowledge_write_route.run_leaf_write`: records, sidecar entries and
the leaf's history file are written into the memory worktree, validated, and the database-only arguments
are refused by name. An **unconverted** memory worktree takes everything this card describes below,
byte-for-byte as before, but only in a repository that holds no converted memory. Since the cutover (L37,
MIK-R37) `run` asks `unconverted_write_refusal(loaded)` first: an unconverted worktree whose official line is
converted, or whose memory repository holds converted memory anywhere, is refused, naming the crossing sync
(MIK-R24 rule 9, MIK-R09 rule 6). The database writer itself is frozen on a converted tree
(`knowledge_write_admission`). The database route's removal is MIK-R26's (L26).

**`--crossing <task-id>-crossing-<n>` (L37, MIK-R24 rule 8 step 4).** When the flag is given, `run` hands the
run to `cli/knowledge_write_route.run_crossing_write` before anything else: `--contract` then names the
master's series contract, the sync's memory worktree is written, a record both sides changed is resolved at
one more than the higher side's revision, and the rows go into the crossing history file the sync opened.

**Since `260928-MIK-L24` (MIK-R24 rule 9) an unconverted memory worktree is refused first when its official
line is converted.** `run` computes `unconverted_write_refusal(loaded) or _invocation_refusal(args)`, so the
rule 9 refusal (from `cli/knowledge_write_route.py`) comes before any argument refusal and names the crossing
sync. It fires only when the official memory branch's tip holds `knowledge/layout.json`, and no line does
before MIK-R37, so today it is inert (architect ruling, 2026-09-29) and the database route runs unchanged.

**Since `260928-MIK-L14` (MIK-R14 rule 4) the converted route takes an optional `--config`.** It names the MCP
authority settings through which a `raise` row's question is appended to the leaf's task document (`task_doc`);
omitted, the settings are discovered from the working directory, and without any a `raise` is refused
(`cli/knowledge_write_route.LeafQuestions` reads them only when a `raise` needs them). `still_rejected` rows need no
settings. On the unconverted route the argument is accepted and ignored (review F10 note); whether installed mode
honours it for a real `raise` after the cutover is carried to L37 (ruling 2026-09-30T05:31:11 F10).

## Code Commentary

### Logic

Module-level surface (ranges are the current candidate's extents; leaf `260921-ICR-L20` grew this file
from 541 to **692 lines** — the destination decision surface and its refusals, which the 135-line
report renderer's extraction to `cli/knowledge_ingest_report.py` paid for — so every range below was
re-derived from its construct's own extent rather than carried):

- `add_arguments` (function, lines 171-262) — declares the operation's inputs: `--contract`
  (**required**), `--list` (**required**), `--candidate-directory` (**optional**), `--authorization-ref`
  (**required**), `--baseline`, `--rebase-baseline`, `--commit`, `--publish-to`, `--publish`,
  `--expected-destination`, `--json` and, since MIK-R14, `--config` (converted memory only).
- `_expected_destination` (function, lines 265-284) — the destination identity the caller admitted, read
  from its JSON object; a malformed value is refused by name rather than read as "absent".
- `_Destination` (dataclass, lines 287-298) — the destination this invocation selected, the report's own
  line about that selection, and the `DeclaredPublicationLocation` when the selection was the declared
  route. `location` is present only for the ordinary route, because the read-back is a read of *that*
  declared location through the read route's own owner: a caller-named path is not the repository's
  publication, so there is no declared location to read and no reader route to bind it to.
- `_destination_conflict` (function, lines 301-337) — why this invocation's destination argument set is
  not one coherent selection, or `None`. Three rules, all stated before anything is read: `--publish`
  and `--publish-to` together (`:320-324`), `--expected-destination` beside `--publish` (`:325-329`),
  and `--expected-destination` with **no** destination selector at all (`:330-336`).
- `_caller_named_destination` (function, lines 340-356) — the caller's path and the caller's
  expectation, unchanged from before the ordinary route; reported as `caller-named: <path>`.
- `_declared_destination` (function, lines 359-379) — the repository's declared location plus what this
  run admits is there, reported as `declared-location: <path> (<admission detail>)`.
- `_selected_destination` (function, lines 382-394) — the one selection: named by the caller, declared,
  or none.
- `_nothing_selected` (function, lines 397-411) — what a run that named no destination reports, **in the
  mode it actually ran in**, because a line claiming a commit the run did not make would be its own
  small fabrication.
- `_read_back` (function, lines 414-427) — reads the published location back, or reports that this run
  published nothing to read back. *Whether* it may run is read from the run's own report, exactly as the
  before-half placement is.
- `_review_root` (function, lines 430-439) — the leaf's canonical review knowledge root, derived from
  the **contract's own recorded worktree group** rather than from the caller or the process's working
  directory.
- `_candidate_directory` (function, lines 442-451) — the directory this run writes into: the caller's
  if it named one, otherwise `<review root>/candidate`.
- `_capture_baseline` (function, lines 454-474) — the fork-point bytes read **at the top of the run**,
  returned as the application owner's `CapturedBaseline`, carrying the path they came from beside them.
- `_placement_refusal` (function, lines 477-501) — **the one gate both ways of filling the before half
  share**: `not-placed` for a planning run, for a batch that did not commit, and for a batch that
  committed no entry.
- `_place_review_baseline` (function, lines 504-542) — the run's review handoff, and since
  `260921-ICR-L18` a pure seam into `application.knowledge_baseline_generation.fill_admitted_before_half`.
- `_Invocation` (dataclass, lines 545-558) — everything one run resolves before it hands the list to the
  operation: the contract, the candidate directory, the captured baseline and the destination. The
  order is the run's own: the contract names the enclosure, the review root comes from that contract,
  and **the baseline is read before the destination is selected**, because the ordinary route's
  admission IS the identity of those captured bytes.
- `_invocation_refusal` (function, lines 561-586) — why this invocation is refused before anything is
  read, or `None`. Every one is a fact about the argument list: a hand-off list that is not a file
  (`:571-572`), a blank authorization (`:573-574`), a destination conflict (`:575-577`), and
  `--rebase-baseline` without `--baseline` (`:578-585`).
- `_invocation` (function, lines 601-611) — resolves the enclosure, the candidate and the destination
  the run is admitted under. Since `260928-MIK-L12` it takes the contract `run` already loaded
  (`loaded`) and loads it itself only when that load failed, so a load error is still reported exactly as
  before and the contract is read once per run.
- `_publication_route` (function, lines 602-615) — **the run's own line about its publication**: the
  destination selected, and what became of it. The selection happens before the list is read, but
  whether anything was published is a fact only the report holds, so the line is completed here from
  `report.publication`.
- `_nothing_published` (function, lines 618-623) — why a run that selected a destination published
  nothing: a planning run, or a batch that committed no entry.
- `_print_report` (function, lines 626-657) — prints the report in the form the caller asked for, by
  delegating both renderings to `cli/knowledge_ingest_report.py`.
- `run` (function, lines 673-709) — drives one ingest and prints its report; **the report IS the
  result**. Since `260928-MIK-L12` it first loads the leaf contract once (`load_leaf_contract`) and, when
  that contract's memory worktree is converted, returns `run_leaf_write`'s exit status instead (0 written or
  planned, 1 refused, 2 invocation refused). On unconverted memory it refuses by name before reading anything (the MIK-R24 rule 9 refusal first, then the invocation refusal), resolves one `_Invocation`, hands the operation
  the one `IngestSelection` (including the selected destination), places the review baseline, reads the
  publication back, and prints.
- `EXIT_REPORTED` / `EXIT_REFUSED` (lines 151-152) — the two exit codes, unchanged: a per-entry refusal
  is a result (0), an invocation refusal is not (2).
- `COMMITTED_BATCH_STATES` (line 168) — the two batch states that mean a candidate is on disk
  (`changed`, `no_change`), which together with the committed-entry list decides whether either filling
  path may run.

**`--publish` is the ordinary route's destination selection, and it is never implied.** It selects the
repository's one declared published dataset location — `<this enclosure's resolved memory root>/
knowledge.sqlite`, resolved through `application/knowledge_publication_route.declared_publication_location`
and therefore through the read route's own declaration rather than through a second spelling of the
same path. It is mutually exclusive with `--publish-to`, it refuses `--expected-destination` beside it
(the ordinary route **derives** the identity it may replace from its own admitted baseline, so a
caller-typed identity would be a second, unchecked claim about the one fact the derivation
establishes), and `--commit` does not imply it: the commit word stays the knowledge-batch write and
acquires no publication meaning. A caller that names no destination at all and passes no `--publish`
still commits without publishing, which is why the destination is a selection rather than a default.

**The read-back is the route's, and it is gated on the run's own report.** When the ordinary route
published, `_read_back` reads the declared location through `published_identity_read_back` — the owner
the ordinary read route itself uses, in the same scope the write was made in — and the report carries
the dataset a *reader* will select: `confirmed`, `mismatch` naming both, or `unavailable` with the
shipped refusal code. A publication the owner refused is read back not at all: nothing was
established about the destination, and reporting an identity for it would be the fabricated success
the requirement forbids.

**Exit zero is not a publication claim, and three fields are where that claim lives.** A run whose
entries all committed can still have published nothing — because it named no destination, because a
publication was refused, or because the read-back found something other than what was written. Each is
stated as its own fact (`publicationRoute`, the `publication` result, and `publishedIdentity`), which
is what makes the requirement's forbidden inference impossible rather than merely discouraged.

`--contract` is **REQUIRED and is the write guard**, exactly as `memory-citations` and `memory-backfill`
use it: the operation reads the code and memory repositories the contract names and writes into the
candidate directory the caller supplies, so **there is no argument list that can aim a knowledge write
at another leaf's line**. `--authorization-ref` is required for the same reason the underlying operation
requires one. `run` builds the one `IngestSelection(candidate_directory, authorization_ref,
dry_run=not args.commit, baseline=..., publication=invocation.destination.publication)` the operation
now takes and passes it positionally, so the adapter names exactly the selection the operation consumes
(`:676-690`). Since `260921-ICR-L20` the destination field is resolved by `_selected_destination`
rather than by a two-line `_publication` helper, and the whole invocation — contract, candidate,
captured baseline, destination — travels as one `_Invocation` value resolved **in that order**, because
the ordinary route's admission is the identity of the bytes `_capture_baseline` read.

**`--candidate-directory` is now OPTIONAL and defaults to the leaf's canonical review candidate root.**
That default is what connects the write side to the read side: the directory is
`<worktree-group>/provider-runtime/dev-ar-coordination/knowledge/candidate`, derived from the contract's
own recorded worktree group through **the same published constants the Intent Reviewer resolves with**
(`REVIEW_CANDIDATE_RELATIVE_ROOT`, `REVIEW_CANDIDATE_DIRECTORY`), so an ingest that names no directory
authors the candidate the review then opens — one spelling, not two conventions that happen to agree
today. Naming a directory still wins, because a caller that wants a scratch draft should get one; that
draft is then simply not the leaf's review candidate, and the report echoes the directory either way.
A contract that cannot be loaded is refused before the list is read, by name.

**The review handoff: one run fills exactly one half, and since `260921-ICR-L18` this file owns only
*whether* it may.** `_capture_baseline` runs at the top of `run`, ahead of `ingest_curator_list`, and
carries the bytes; `_place_review_baseline` then asks `_placement_refusal` — **the one gate both ways of
filling the before half share**, because the question is one question: the half belongs to the run that
committed, and a planning run, a refused batch and a batch that committed nothing all leave it exactly
as they found it. That gate was `260921-ICR-L5`'s change to the earlier structure (reachable from both
filling paths rather than only from the `--baseline` one) and it is unchanged by this leaf. What *did*
change is everything downstream of it: the question **"what is the half afterwards"** now belongs to
[`application/knowledge_baseline_generation.py`](../application/knowledge_baseline_generation.py.md),
which composes the before-half layout owner and the first-generation owner. This function carries the
run's facts across that seam and nothing else, so the CLI stays a surface rather than a second placement
authority. The half is derived from the contract's own recorded worktree group through `_review_root`,
exactly as the review resolves it, so the directory this run fills and the directory the comparison
opens are one path by construction.

**`--rebase-baseline` is the caller's deliberate word, and since `260921-ICR-L20` its refusal is one of
four invocation rules read from one function.** It reaches the owner as `rebase=args.rebase_baseline`
(`:541-541`) and is the only input that may replace a standing baseline. It is a flag rather than a
default because a deliberately new baseline is a **new comparison generation with recorded lineage**,
never an overwrite behind the identity the comparison already had. Two invocation-level rules live here
rather than in the owner, because both are facts about the argument list: `_invocation_refusal` refuses
the flag without `--baseline` by name and returns `EXIT_REFUSED` **before the contract or the list is
read** (`:578-585`), since a rebase is a transition *from* one admitted baseline to another and a run
that names the action without the dataset has stated no generation to begin from; and the flag cannot
do two things the help text says it cannot — replace an identified first generation, or repair a
damaged half — because those are named states with their own owners, and a flag that silently overrode
them would be a second, quieter way to rewrite what a comparison is *of*. The two rules this leaf added
beside it are the destination argument set's own coherence: `--publish` with `--publish-to` (`:320-324`)
and `--expected-destination` with no destination selector at all (`:330-336`).

**The rules that used to live in this file are still the rules; they are cited where they now are.**
With `--baseline` and a half that already holds something, the owner keeps what stands rather than
copying over it — the same `260915-KS-L47` repair (a copy taken after the run published would place the
*candidate* in the before half, so the bytes are captured at the top of the run and carried) is what
makes a retry keep the fork point it was first handed. The three guards that used to be `_place_fork_point`
are now `_place_or_keep`'s ordered answers in the owner: a damaged half is named and left exactly as it
is, the half's own dataset being the one this run was handed is a no-op rather than a placement, and the
captured bytes are read as a dataset **before** anything is written so a corrupt expected dataset is
never reported as *placed*. Without `--baseline`, the run is still the repository's **first
generation** and the half is *established* rather than left absent — `ICR-R05@v1`'s repair, whose
tempting wrong answer (an empty dataset with no record) is the one the packet's non-conforming example
forbids — but the establishment is now reached through the owner's `_establish_first_generation`, which
calls `application.knowledge_first_generation.establish_first_generation` with the leaf's own observed
facts: the contract's `leaf_id`, the contract path, `--authorization-ref`, and the code base commit the
report already prints (an *observation* of the run, not a second source-endpoint resolution; how a
comparison binds a source side stays the review's own resolution). Its detail line still reaches the
caller as `established: …`.

**A *selected* baseline that is missing or corrupt is a different fact and is never answered either
way.** `_admitted_candidate` (in the application layer) now reads the selected baseline **on every run,
resume included**, and before anything else is decided: an existing candidate is a resume attempt, and
a resume that names a dataset it cannot read is still an unavailable selected input rather than a run
that proceeds without it. The refusal is the shipped `selected_input_unavailable` naming the path and
the reason. Reading it only on the clone path made a corrupt fork point invisible exactly where a later
run would go on to act on it — the run committed, and the before half was then filled from the captured
bytes, replacing an identified first generation with a corrupt file and reporting it *placed*. Every
way out of `_place_review_baseline` is therefore explicit rather than inferred, and the result reaches
the caller as the report's `reviewBaseline` field (and as a `review baseline:` line in the human
summary); it is a **string and not a boolean** because "not placed" has several reasons and a caller
that has to guess which one is being given a message rather than a result.

**`--baseline <published dataset>` is the continuity half of that one decision, and it is this leaf's
CYCLE-01 repair.** It names the published dataset the task forks FROM and reaches
`IngestSelection.baseline` as a `Path`, so the next task begins from the knowledge the repository already
published instead of from an empty candidate. Omitting it is not a failure but the other honest case — a
repository's first task has no prior dataset to select and still creates an empty candidate, and since
this leaf that case also **establishes the review's before half** rather than leaving it absent, so the
first invariant is reviewable as an addition. Naming a baseline that is missing or unreadable is the
third case and is refused by name, establishing nothing. The argument and the selection field are one
pairing rather than an option and a default because a candidate named without the baseline it starts
from holds only this task's new entry, so the repository's existing invariants are absent from it and
the next task begins blind to what was already recorded. Nothing else about the surface changed, and
the publication remains the second half of the same act, reached from this surface without a second
write path: the committed candidate is published by the run that already holds it, either to the path
the caller names (`--publish-to`, with `--expected-destination` as the exact identity the caller
observed there) or to the repository's one declared location (`--publish`, whose admitted identity is
derived from the baseline this run read). The CLI adds no write path of its own — it calls
`application.knowledge_curator_ingest.ingest_curator_list` and reports what that closed write path did.

This module exists because the write plane had no production caller: at `e7998504` the ingest was
reachable only from its own tests, which is finding **M1-1** of this master's review round 1.

### Conventions

Module-level definitions follow the package conventions, matching its seven sibling CLI adapters; names
prefixed with `_` are private to this module. Argument declaration and dispatch are split the same way
they are in `memory_citations.py` and `memory_backfill.py`: `add_arguments` owns the parser surface and
`run` owns the behaviour, so the parser can be exercised without running the operation.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **Every write is bounded by the contract.** The module cannot be pointed at another leaf's line: the
  repositories come from `--contract` and the destination is either the caller's directory or the
  canonical root derived from that same contract, and `--authorization-ref` is mandatory.
- **The write side and the read side name one directory.** The default candidate directory is derived
  from the contract through the review's own published constants, so an ingest that names nothing
  authors the candidate the Intent Reviewer resolves.
- Nothing is placed on a way out that did not commit. A planning run and a batch that committed no
  entry (including an all-refused one, which reports `no_change` because the batch-level state falls
  back to it when the batch never ran) each fill nothing through **either** path, and each says which
  case it was; no baseline is invented, there is no `HEAD` fallback and no coordination-tree
  resolution.
- **One run fills one half, and never over one that is already there.** The gate decides *whether*; the
  owner decides *what*. Neither path replaces an identified first generation, rewrites a damaged half,
  or places bytes that do not read as a dataset, and the only input that may replace a standing baseline
  is the caller's explicit `--rebase-baseline`.
- **A rebase flag without a dataset is refused at the surface.** `--rebase-baseline` with no `--baseline`
  exits `EXIT_REFUSED` by name before the contract is loaded, because the action states no generation to
  begin from.
- **The fork-point dataset is copied, not moved and not linked.** The published dataset keeps serving its
  own lane; the leaf's disposable root gets its own bytes.
- **A selected baseline is read on every run, resume included.** An unreadable fork point is refused by
  name (`selected_input_unavailable`) rather than treated as "no baseline selected", which is the
  reading under which a missing historical dataset came to be silently replaced by a newly empty one.
- **The report is the result.** Nothing is inferred from exit status alone — the counts, the per-entry
  outcomes, the refusal reasons, the `reviewBaseline` line, the `publicationRoute` line, the
  `publication` result and the `publishedIdentity` read-back are the operation's evidence.
- **The destination is one selection, and it is never implied.** `--publish-to` and `--publish` are
  mutually exclusive (the ordinary route's declared location and a caller-named path are different
  selections, and a run that named both has not said which it means); `--expected-destination` belongs
  to the caller-named path alone; and `--commit` acquires no publication meaning. All three rules are
  stated in `_destination_conflict` before a contract, a list or a byte is read.
- **An ignored argument is a refusal, not a silence.** `--expected-destination` with no destination
  selector at all is refused by name, exactly as `--rebase-baseline` without `--baseline` is, because
  a caller whose argument was absorbed believes it was honoured.
- **The ordinary route's admitted identity is derived, not typed.** When `--baseline` names the
  declared location, the bytes captured at the top of the run are the dataset standing there and their
  identity is what the publication may replace; every other case is admitted as nothing being there,
  and the publication owner refuses by name if the location turns out to hold something.
- **Exit zero is not a publication claim.** A run whose entries all committed can still have published
  nothing, and `publicationRoute` / `publication` / `publishedIdentity` are the three fields that state
  which of those happened. Nothing in this module rounds a selection up into a publication.
- **The read-back is gated on the run's own report, and it never raises.** A publication the owner
  refused established nothing about the destination, and a run that published nothing has no location
  of its own to read; the reader's owner answers with named states rather than raising, so a read-back
  can never cost a run the report it already has.
- **A destination that cannot be resolved is refused, never defaulted.** An enclosure whose memory
  layer does not resolve raises, and `run` turns that into the invocation refusal it is; there is no
  fallback path and no guessed location.
- **This adapter adds no knowledge behaviour, and since `260921-ICR-L18` no placement behaviour, and
  since `260921-ICR-L20` no rendering or publication behaviour.** It declares arguments, resolves one
  invocation value, selects the destination from the argument set, reads the caller's baseline bytes
  into the owner's own value, asks the one gate whether this run may fill anything, delegates the
  decision to the application layer, and delegates both renderings to
  `cli/knowledge_ingest_report.py`; every refusal, route resolution, row count, generation record and
  published identity originates below this module.

### Todos

None requested of this card. One code-level observation belonged to this leaf's owning seat and is
**resolved in the merged candidate** rather than carried: `application/knowledge_review.py` was 1,281
lines at this leaf's base against the seam policy's **1,200-line hard rail**
(`notes/03-adapter-seam.md` in this task tree), and this leaf added 13 lines to it (an import and two
call sites) — the new before-half readers did land in their own module, so the rule was followed for the
responsibility itself, but the adapter was left over the rail, and that was reported rather than
hand-fixed because no memory change could address it. Leaf `260921-ICR-L1`'s landed extraction then
moved the resolution out, and the sync brought it into this candidate: the adapter is now **1,126
lines**, under the rail, with this leaf's 13 lines on top of L1's 1,113. Nothing remains for the
orchestrator here.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Declares the contract guard, the hand-off list, the optional candidate directory, the authorization ref, the baseline this task forks from, dry-run, the two destination selectors and their exclusivity. [1]
- MIK-R14's optional MCP settings for a `raise` row's task-document question (converted memory only). [2]
- **The ordinary route's destination: the read route's own declared location, and what this run admits is already there.** [3]
- **The invocation's destination argument set, refused as a set: two destinations, an expectation beside the declared route, and an expectation with nothing to expect at.** [4]
- **The caller-named path, admitted exactly as it was before the ordinary route existed, and the one selection the run ends up making.** [5]
- **What a run that named no destination reports, in the mode it actually ran in — a planning run is not a committed run.** [6]
- **The read-back, gated on the run's own report: a refused publication and a run that published nothing are both read back not at all.** [7]
- **The run's own line about its publication, completed from the report because the selection happens before the list is read; and why a run that selected a destination published nothing.** [8]
- **The four values one run resolves, in the order it needs them — the baseline is read before the destination is selected, because the ordinary route's admission IS those bytes. `_invocation` reuses the contract `run` already loaded, and loads it itself only when that load failed.** [9]
- **A converted memory worktree is written by the curator file writer: `run` loads the contract once and dispatches on the layout marker before any database-route refusal (MIK-R12 rule 7).** [10]
- **The unconverted refusal comes first on unconverted memory: MIK-R24 rule 9 when the official line is converted and, since L37, the cutover lock once the repository holds converted memory.** [11]
- **Every fact about the argument list answered before a contract, a list or a byte is touched.** [12]
- Drives one ingest and prints the report, which is the result; after the converted-memory dispatch it refuses by name first, resolves one `_Invocation`, builds the one `IngestSelection` the operation takes, hands the loaded contract to the review handoff, reads the publication back and prints. [13]
- **The two renderings this module delegates rather than owns, including the two fields this leaf added to the run's answer.** [14]
- **The canonical review root, derived from the contract's own recorded worktree group rather than from the caller, so the directory the review resolves and the directory this run writes are the same path by construction.** [15]
- **The candidate directory: the caller's when it named one, otherwise the canonical review candidate root.** [16]
- **The review handoff as a pure seam: ask the one gate whether this run may fill anything, then hand the half, the candidate directory, the captured bytes, the run's facts and the rebase flag to the placement owner.** [17]
- **The before-snapshot capture, taken at the top of `run` before the ingest can publish over the file `--baseline` names (leaf `260915-KS-L47`). It returns the application owner's own value rather than a CLI-local dataclass.** [18]
- The two batch states that mean the candidate is on disk, and the entry list that keeps an all-refused run from reading as one of them: `no_change` is a batch whose rows were already stored, but the batch-level state also falls back to it when the batch never ran, so a run whose every entry refused reports it too. The placement therefore also requires `report.committed` to be non-empty, because a run that committed no entry has no candidate of its own and must not touch the review's before half. [19]
- **The one gate both filling paths share, split so each branch states only what its own condition established.** The state half reports `the batch did not commit (<state>)`; the entry half reports `the batch committed no entry (<state>, refused N)`. They are two returns rather than one sentence because the single sentence served both halves and contradicted itself on the state-half branch -- a replayed run read `committed no entry (replayed, committed 1)` This is the only placement question left in this file. [20]
- **The rules that used to be this file's, cited where they now live: the ordered answers that keep a standing baseline, and the first generation's preservation rule the rebase flag cannot override.** [21]
- **The application owner the handoff delegates to, and the values it hands over: the run's admitted facts and the bytes read before publication could move them.** [22]
- **The two readers the moved guards were built on: the half's four-state read, and the bytes-read-as-a-dataset read taken before anything is written — the second of which the ordinary route's admission also derives its identity from.** [23]
- **The cold-start branch, now reached through the owner: a run that named no baseline establishes the review's before half as an explicitly identified empty first generation, carrying the leaf, the contract, the authorization and the code base the report already observed.** [24]
- **The application owner that act delegates to, the run it is handed, and the value it answers with.** [25]
- The production entry point this adapter calls — the closed write path — and the selection value it is handed, including the baseline a run forks from and the destination it selected. [26]
- **The refusal a selected baseline that is missing or corrupt earns, naming its path and reason and establishing nothing.** [27]
- **The three published directory constants this adapter derives its default from — one spelling shared with the reader, which is what connects the write side to the review. They are defined in `application/review_candidate_resolution.py` and re-exported by `knowledge_review.py`, which is the import path this module uses (`:146-146`). Every range in this row was re-derived against this leaf's candidate, whose import block moved the constants by four lines.** [28]
- The dataset name both halves take, so a placed baseline and an established first generation are the file the review opens. [29]
- The contract the one load yields, and the loader that reads it. [30]
- The subparser registration that makes this the ninth CLI subcommand. [31]

- The run's order: the crossing route, the file writer for a converted tree, the unconverted refusal, then the database ingest. [32]
