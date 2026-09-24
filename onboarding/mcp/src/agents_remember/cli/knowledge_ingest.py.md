# mcp/src/agents_remember/cli/knowledge_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T18:09+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter: ingest an orchestrator's curator hand-off list into a leaf's candidate — the knowledge
write plane's first production caller, and the run that publishes the committed candidate through the
shipped publication owner. Since `260921-ICR-L20` it is also the surface that owns the *destination
selection*: the caller's path (`--publish-to`), the repository's **one declared published dataset
location** (`--publish`, resolved by the read route's own owner), or neither.

## Code Commentary

### Logic

Module-level surface (ranges are the current candidate's extents; leaf `260921-ICR-L20` grew this file
from 541 to **692 lines** — the destination decision surface and its refusals, which the 135-line
report renderer's extraction to `cli/knowledge_ingest_report.py` paid for — so every range below was
re-derived from its construct's own extent rather than carried):

- `add_arguments` (function, lines 171-262) — declares the operation's inputs: `--contract`
  (**required**), `--list` (**required**), `--candidate-directory` (**optional**), `--authorization-ref`
  (**required**), `--baseline`, `--rebase-baseline`, `--commit`, `--publish-to`, `--publish`,
  `--expected-destination` and `--json`.
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
- `_invocation` (function, lines 589-599) — resolves the enclosure, the candidate and the destination
  the run is admitted under.
- `_publication_route` (function, lines 602-615) — **the run's own line about its publication**: the
  destination selected, and what became of it. The selection happens before the list is read, but
  whether anything was published is a fact only the report holds, so the line is completed here from
  `report.publication`.
- `_nothing_published` (function, lines 618-623) — why a run that selected a destination published
  nothing: a planning run, or a batch that committed no entry.
- `_print_report` (function, lines 626-657) — prints the report in the form the caller asked for, by
  delegating both renderings to `cli/knowledge_ingest_report.py`.
- `run` (function, lines 660-692) — drives one ingest and prints its report; **the report IS the
  result**. It refuses by name before reading anything, resolves one `_Invocation`, hands the operation
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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Declares the contract guard, the hand-off list, the optional candidate directory, the authorization ref, the baseline this task forks from, dry-run, the two destination selectors and their exclusivity. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_ingest.py:171-262 |
| **The ordinary route's destination: the read route's own declared location, and what this run admits is already there.** | `_Destination`; `_declared_destination`; `declared_publication_location`; `admitted_destination` | mcp/src/agents_remember/cli/knowledge_ingest.py:287-298; mcp/src/agents_remember/cli/knowledge_ingest.py:359-379; mcp/src/agents_remember/application/knowledge_publication_route.py:115-132; mcp/src/agents_remember/application/knowledge_publication_route.py:135-199 |
| **The invocation's destination argument set, refused as a set: two destinations, an expectation beside the declared route, and an expectation with nothing to expect at.** | `_destination_conflict` | mcp/src/agents_remember/cli/knowledge_ingest.py:301-337 |
| **The caller-named path, admitted exactly as it was before the ordinary route existed, and the one selection the run ends up making.** | `_caller_named_destination`; `_selected_destination` | mcp/src/agents_remember/cli/knowledge_ingest.py:340-356; mcp/src/agents_remember/cli/knowledge_ingest.py:382-394 |
| **What a run that named no destination reports, in the mode it actually ran in — a planning run is not a committed run.** | `_nothing_selected` | mcp/src/agents_remember/cli/knowledge_ingest.py:397-411 |
| **The read-back, gated on the run's own report: a refused publication and a run that published nothing are both read back not at all.** | `_read_back`; `published_identity_read_back` | mcp/src/agents_remember/cli/knowledge_ingest.py:414-427; mcp/src/agents_remember/application/knowledge_publication_route.py:202-250 |
| **The run's own line about its publication, completed from the report because the selection happens before the list is read; and why a run that selected a destination published nothing.** | `_publication_route`; `_nothing_published` | mcp/src/agents_remember/cli/knowledge_ingest.py:602-615; mcp/src/agents_remember/cli/knowledge_ingest.py:618-623 |
| **The four values one run resolves, in the order it needs them — the baseline is read before the destination is selected, because the ordinary route's admission IS those bytes.** | `_Invocation`; `_invocation` | mcp/src/agents_remember/cli/knowledge_ingest.py:545-558; mcp/src/agents_remember/cli/knowledge_ingest.py:589-599 |
| **Every fact about the argument list answered before a contract, a list or a byte is touched.** | `_invocation_refusal` | mcp/src/agents_remember/cli/knowledge_ingest.py:561-586 |
| Drives one ingest and prints the report, which is the result; it refuses by name first, resolves one `_Invocation`, builds the one `IngestSelection` the operation takes, hands the loaded contract to the review handoff, reads the publication back and prints. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:660-692; mcp/src/agents_remember/cli/knowledge_ingest.py:676-690 |
| **The two renderings this module delegates rather than owns, including the two fields this leaf added to the run's answer.** | `_print_report`; `summary`; `payload` | mcp/src/agents_remember/cli/knowledge_ingest.py:626-657; mcp/src/agents_remember/cli/knowledge_ingest_report.py:32-70; mcp/src/agents_remember/cli/knowledge_ingest_report.py:73-118 |
| **The canonical review root, derived from the contract's own recorded worktree group rather than from the caller, so the directory the review resolves and the directory this run writes are the same path by construction.** | `_review_root` | mcp/src/agents_remember/cli/knowledge_ingest.py:430-439 |
| **The candidate directory: the caller's when it named one, otherwise the canonical review candidate root.** | `_candidate_directory` | mcp/src/agents_remember/cli/knowledge_ingest.py:442-451 |
| **The review handoff as a pure seam: ask the one gate whether this run may fill anything, then hand the half, the candidate directory, the captured bytes, the run's facts and the rebase flag to the placement owner.** | `_place_review_baseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:504-542 |
| **The before-snapshot capture, taken at the top of `run` before the ingest can publish over the file `--baseline` names (leaf `260915-KS-L47`). It returns the application owner's own value rather than a CLI-local dataclass.** | `_capture_baseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:454-474 |
| The two batch states that mean the candidate is on disk, and the entry list that keeps an all-refused run from reading as one of them: `no_change` is a batch whose rows were already stored, but the batch-level state also falls back to it when the batch never ran, so a run whose every entry refused reports it too. The placement therefore also requires `report.committed` to be non-empty, because a run that committed no entry has no candidate of its own and must not touch the review's before half. | `COMMITTED_BATCH_STATES`; `_placement_refusal` | mcp/src/agents_remember/cli/knowledge_ingest.py:168-168; mcp/src/agents_remember/cli/knowledge_ingest.py:477-501 |
| **The one gate both filling paths share, split so each branch states only what its own condition established.** The state half reports `the batch did not commit (<state>)`; the entry half reports `the batch committed no entry (<state>, refused N)`. They are two returns rather than one sentence because the single sentence served both halves and contradicted itself on the state-half branch -- a replayed run read `committed no entry (replayed, committed 1)` This is the only placement question left in this file. | `_placement_refusal` | mcp/src/agents_remember/cli/knowledge_ingest.py:477-501 |
| **The rules that used to be this file's, cited where they now live: the ordered answers that keep a standing baseline, and the first generation's preservation rule the rebase flag cannot override.** | `_place_or_keep`; `_place_admitted_baseline`; `_identified_first_generation` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:551-576; mcp/src/agents_remember/application/knowledge_baseline_generation.py:534-548; mcp/src/agents_remember/application/knowledge_baseline_generation.py:843-856 |
| **The application owner the handoff delegates to, and the values it hands over: the run's admitted facts and the bytes read before publication could move them.** | `fill_admitted_before_half`; `BaselineRun`; `CapturedBaseline` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:464-500; mcp/src/agents_remember/application/knowledge_baseline_generation.py:163-175; mcp/src/agents_remember/application/knowledge_baseline_generation.py:178-189 |
| **The two readers the moved guards were built on: the half's four-state read, and the bytes-read-as-a-dataset read taken before anything is written — the second of which the ordinary route's admission also derives its identity from.** | `read_before_half`; `read_captured_dataset_identity` | mcp/src/agents_remember/application/knowledge_before_half.py:257-286; mcp/src/agents_remember/application/knowledge_before_half.py:226-240 |
| **The cold-start branch, now reached through the owner: a run that named no baseline establishes the review's before half as an explicitly identified empty first generation, carrying the leaf, the contract, the authorization and the code base the report already observed.** | `_establish_first_generation` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:503-516 |
| **The application owner that act delegates to, the run it is handed, and the value it answers with.** | `establish_first_generation`; `FirstGenerationRun`; `BeforeGeneration` | mcp/src/agents_remember/application/knowledge_first_generation.py:100-124; mcp/src/agents_remember/application/knowledge_first_generation.py:82-88; mcp/src/agents_remember/application/knowledge_first_generation.py:92-97 |
| The production entry point this adapter calls — the closed write path — and the selection value it is handed, including the baseline a run forks from and the destination it selected. | `ingest_curator_list`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1034-1153; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1014-1031 |
| **The refusal a selected baseline that is missing or corrupt earns, naming its path and reason and establishing nothing.** | `selected_input_unavailable_refusal`; `_selected_baseline` | mcp/src/agents_remember/memory/knowledge/refusals.py:882-901; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1422-1559 |
| **The three published directory constants this adapter derives its default from — one spelling shared with the reader, which is what connects the write side to the review. They are defined in `application/review_candidate_resolution.py` and re-exported by `knowledge_review.py`, which is the import path this module uses (`:143-145`).** | `REVIEW_CANDIDATE_RELATIVE_ROOT`; `REVIEW_CANDIDATE_DIRECTORY`; `REVIEW_BASELINE_DIRECTORY` | mcp/src/agents_remember/application/review_candidate_resolution.py:80-80; mcp/src/agents_remember/application/review_candidate_resolution.py:87-87; mcp/src/agents_remember/application/review_candidate_resolution.py:86-86; mcp/src/agents_remember/application/knowledge_review.py:53-55; mcp/src/agents_remember/cli/knowledge_ingest.py:143-145 |
| The dataset name both halves take, so a placed baseline and an established first generation are the file the review opens. | `CANDIDATE_DATABASE_NAME`; `BASELINE_ORIGIN_NAME` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-52; mcp/src/agents_remember/application/knowledge_before_half.py:79-79 |
| The contract the one load yields, and the loader that reads it. | `WorktreeContract`; `load_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:233-286; mcp/src/agents_remember/worktrees/worktree_contract.py:437-467 |
| The subparser registration that makes this the ninth CLI subcommand. | "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:35-43 |

## Update History
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and one legacy record retired; no claim wording changed and no row deleted.** This leaf moved the module several of this card's rows cite, so those ranges were re-derived against the candidate's own bytes. The **retired** entry is the 2026-09-20 mechanical anchor-range projection that had written a range for the list-ingest entry point: a projected range is not a reading, so it is recorded as retired evidence rather than re-anchored. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **this adapter became the surface that owns the destination selection, and stopped owning the report's shape.** `260921-ICR-L20` (`ICR-R20@v1`) added `--publish`, which selects the repository's **one declared published dataset location** — resolved by the *read* route's own owner (`application/knowledge_publication_route.declared_publication_location` → `published_intent.published_dataset_path`) so the location a curator writes and the location a later task's planner selects are one spelling owned once — and the file is **692 lines** where this card last measured 541. **The 135-line report renderer left this file** for [`cli/knowledge_ingest_report.py`](knowledge_ingest_report.py.md) (`_summary`, `_payload`, `_counts`, `_targets`, `_outcome`), which is what paid for the new decision surface; those names must not be cited here any more. **New constructs:** `_Destination` (`:287-298`), `_destination_conflict` (`:301-337`, three rules), `_caller_named_destination` (`:340-356`), `_declared_destination` (`:359-379`), `_selected_destination` (`:382-394`), `_nothing_selected` (`:397-411`), `_read_back` (`:414-427`), `_Invocation` (`:545-558`), `_invocation_refusal` (`:561-586`, which absorbed the three pre-existing invocation refusals and the rebase rule), `_invocation` (`:589-599`), `_publication_route` (`:602-615`), `_nothing_published` (`:618-623`) and `_print_report` (`:626-657`); `_publication` has no successor (its one selection became three), and `run` (`:660-692`) is now the sequence of those steps rather than a body carrying four refusals and both renderings. **The rules the body now states and did not before:** the destination is one selection and is never implied by `--commit`; `--expected-destination` with no destination selector is refused by name rather than silently absorbed; the ordinary route's admitted identity is *derived* from the baseline bytes this run captured, never typed; a destination that cannot be resolved is refused rather than defaulted; exit zero is not a publication claim and `publicationRoute` / `publication` / `publishedIdentity` are where that claim lives; and the read-back is gated on the run's own report, so a refused publication is read back not at all. **Citation accounting:** every range into this file was re-derived from its construct's own extent in this candidate rather than carried — `add_arguments` `:133-209` → `:171-262`, `_review_root` `:245-254` → `:430-439`, `_candidate_directory` `:257-266` → `:442-451`, `_capture_baseline` `:269-289` → `:454-474`, `_placement_refusal` `:292-316` → `:477-501`, `_place_review_baseline` `:319-357` → `:504-542`, `run` `:360-409` → `:660-692`, `COMMITTED_BATCH_STATES` `:130-130` → `:168-168`, and the three `REVIEW_*` constants this module imports `:105-109` → `:143-145`. The same re-derivation was applied to every *other* memory document that cites this file, because a citation range is a measurement of the candidate and not a record that survives the candidate moving. **Stamp accounting:** the recorded working candidate names this leaf's candidate on production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`, which is the line this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands. No commit was made.
- 2026-09-21T15:35+02:00 — 260921-ICR-L18 curator (uncommitted change set on `ar/260921-icr-l18`, code base `0fca5c69766aa95eebe950c19fbcdc83864ec35a`): **this adapter stopped being a placement authority, and the card's body says so.** `260921-ICR-L18` (ICR-R18@v1) extracted the placement machinery into the new `application/knowledge_baseline_generation.py`, so `cli/knowledge_ingest.py` is **541 lines** where this card last measured 620 — a net −79 — and `_place_review_baseline` (`:319-357`) is now a pure seam: it asks `_placement_refusal` (`:292-316`, still the only placement question left in this file, unchanged by this leaf) whether the run may fill anything, then hands the half, the candidate directory, the captured bytes, the run's facts and the rebase flag to `fill_admitted_before_half`. **Four constructs this card used to cite no longer exist in this file** and their rows were re-pointed rather than deleted: `_CapturedBaseline` is now the owner's public `CapturedBaseline`; `_placeable_baseline` has no successor (the handoff narrows `captured` once, inline); and `_place_fork_point` and `_establish_first_generation` both moved into the owner, as `_place_or_keep`/`_place_admitted_baseline` and `_establish_first_generation` respectively — the rules they carried (the ordered keep-or-write answers, and R05's first-generation preservation the rebase flag cannot override) are now cited where they live. **The new argument is `--rebase-baseline`**, the caller's deliberate word and the only input that may replace a standing baseline; its invocation refusal lives in `run` (`:370-378`) because it is a fact about the argument list, and it fires by name before the contract or the list is read. **Citation accounting:** every range into this file was re-derived from its construct's own extent rather than carried, including the ranges no checklist row named — `add_arguments` `:129-192` → `:133-209`, `run` `:448-488` → `:360-409`, `_review_root` `:228-237` → `:245-254`, `_candidate_directory` `:240-249` → `:257-266`, `_capture_baseline` `:267-285` → `:269-289` (and its dataclass row dropped), `_placement_refusal` `:288-312` → `:292-316`, `_place_review_baseline` `:336-376` → `:319-357`, `_payload` `:530-568` → `:451-489`, `_counts` `:571-583` → `:492-504`, `COMMITTED_BATCH_STATES` `:126-126` → `:130-130`. The sibling-module rows into `knowledge_before_half.py` moved by this leaf's own docstring reconciliation (`:254-283` → `:257-286`, `:223-237` → `:226-240`, `:76-76` → `:79-79`), and the `IngestSelection` row was corrected from `:1014-1031` to `:1015-1031` — a range that was already off by one before this leaf and is re-measured here rather than carried. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the production line this reading was against (`0fca5c69`, this leaf's base), because the candidate is uncommitted and no commit contains the body as it now stands; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-21T14:30+02:00 — 260921-ICR-L5 curator, **the sync's memory-side conflict in this document resolved as a UNION, with the CLI's own ranges kept and the sibling-module facts added.** This file is 620 lines in the merged candidate — `260921-ICR-L5`'s version, which is why this side's ranges and Logic surface stand — while L1's contribution is the fact that the three `REVIEW_*` constants this module imports are now *defined* in `application/review_candidate_resolution.py` and re-exported through `knowledge_review.py`: that row names both files and this module's own import block (`:103-107`) rather than replacing the range. The 13-line adapter change this leaf landed survives the merge unchanged, and its two call sites are cited at the merged module's extents (`list_knowledge_review_entries` `:207-288`, `compose_review` `:386-496`). No verification stamp was advanced.
- 2026-09-21T13:50+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): **the cold-start branch reached this adapter, and the review handoff became two filling paths behind one gate.** `--baseline` absent used to mean "nothing is placed" and the review's before half stayed absent; it now means the run *establishes* an explicitly identified empty first generation through the new `application/knowledge_first_generation.establish_first_generation`, because a pair with one side missing is refused and the first invariant a repository ever records could not otherwise be displayed as an addition (ICR-R05@v1). The gate that decides whether either path may run was extracted into `_placement_refusal` (`:288-312`) and is now reached from **both** paths rather than only from the `--baseline` one; `_place_fork_point` (`:379-410`) carries the three rules that guard the copy — an identified first generation is never replaced, a damaged half is named and left as it is, and the captured bytes are read as a dataset before they are written; and `_establish_first_generation` (`:413-445`) is the new branch. `_review_root` (`:228-237`) now takes the loaded `WorktreeContract` because `run` loads the contract once and derives both the root and the leaf id from it. This is a body change and not a metadata-only refresh: the two paragraphs above state behaviour this card did not carry, and the Invariants section gained the one-half-per-run rule and the resume-read rule. **Citation accounting:** the file grew 513 → 620 lines, so every range this card carries into it was re-measured by construct extent rather than carried — `add_arguments` `:110-170` → `:129-192`, `run` `:335-374` → `:448-488`, `_payload` `:416-454` → `:530-568`, `_counts` `:457-469` → `:571-583`, `_review_root` `:206-215` → `:228-237`, `_candidate_directory` `:218-227` → `:240-249`, `_CapturedBaseline`/`_capture_baseline` `:231-263` → `:252-264`/`:267-285`, `_place_review_baseline` `:293-332` → `:336-376`, and `COMMITTED_BATCH_STATES` `:107-107` → `:126-126`; three rows were added for the two new branch helpers and the shared gate, and two duplicate rows that cited the same constructs twice were folded into one. The same re-measurement was applied to the three other route documents that cite this file — `mcp/overview.md`, `mcp/src/agents_remember/application/overview.md`, `mcp/tests/overview.md` and the two test cards. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made. The Todos section records one code-level observation for the owning seat (the review adapter's 1,200-line rail), which no memory change could address.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **citation repair only, forced by this leaf's move of the review resolution out of `application/knowledge_review.py` into `application/review_candidate_resolution.py`.** The rows of this document that cited `knowledge_review.py` for `REVIEW_CANDIDATE_RELATIVE_ROOT`, `REVIEW_CANDIDATE_DIRECTORY`, `REVIEW_BASELINE_DIRECTORY`, `review_namespace`, `missing_dataset_half`, `list_knowledge_review_entries` and `_recorded_identities` were re-read and re-pointed: a name the sibling module now defines is cited there, and a name the adapter still owns is cited at the extent it occupies in this candidate (the module is 1113 lines, down from 1281). No claim was re-worded beyond naming where the construct now lives, no row was deleted and no verification stamp was advanced — the candidate is uncommitted and closeout owns that stamp.
- 2026-09-21T01:40+02:00 — 260915-KS-L47 curator (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`, memory base `2f415d930d1f8122ae0226bd296add3265600749`): **the refusal sentence was split, and every citation into this file was re-measured again rather than carried.** `_place_review_baseline`'s not-placed message served both halves of the placement condition in one sentence, so a replayed run reported `not-placed: the batch committed no entry (replayed, committed 1)` -- the gate was right and the sentence was wrong for the state-half branch. It is now two returns, `_placement_refusal` (`:266-288`), one per branch. The file grew 486 -> 505 lines, so this card's ranges were re-measured by AST extent: `_place_review_baseline` `:266-311` -> `:291-330`, `run` `:314-353` -> `:333-372`, `_payload` `:395-433` -> `:414-452`, `_counts` `:436-448` -> `:455-467`; `add_arguments` `:110-170`, `_review_root` `:206-215`, `_candidate_directory` `:218-227`, `_CapturedBaseline`/`_capture_baseline` `:231-263` and `COMMITTED_BATCH_STATES` `:107-107` are unchanged by the split and were re-verified rather than assumed. The same re-measurement was applied to the three other documents that cite this file. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-21T00:40+02:00 — 260915-KS-L47 curator (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`, memory base `2f415d930d1f8122ae0226bd296add3265600749`): **re-measured against the moved candidate, and the refusal-path defect this file's own repair opened is now stated and guarded.** The code worktree moved under this curation: `cli/knowledge_ingest.py` gained the `report.committed` requirement beside `COMMITTED_BATCH_STATES`, because an all-refused run also reports `no_change` — the batch-level state falls back to it when the batch never ran — so a changed request that the retry guard turns into a *refusal* re-placed the before half from the bytes captured at the top of the run, which after the leaf published over its own fork point are the PUBLISHED dataset, and the review showed the addition present on both sides with an empty delta. The file grew from 393 to 485 lines, so **every citation this card carries into it was re-measured rather than carried**: `add_arguments` `:93-153` → `:110-170`, `run` `:248-284` → `:314-353`, `_place_review_baseline` `:256-298` → `:266-311`, the two previously range-less cells now cite `:266-311` and `:231-263`, `COMMITTED_BATCH_STATES` `:97-97` → `:107-107`, `_payload` `:326-364` → `:395-433`, and `_counts` `:423-435` → `:436-448`. The same re-measurement was applied to the three other documents that cite this file — `mcp/overview.md`, `mcp/src/agents_remember/application/overview.md` and `mcp/tests/overview.md` — because a citation range is a measurement of the candidate, not a record that survives the candidate moving. The `COMMITTED_BATCH_STATES` row's own text was extended to state the entry-list requirement and why state alone cannot carry it. This is a body change, not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-20T20:56+02:00 — 260915-KS-L48 curator (uncommitted change set on `ar/260915-ks-l48-ar`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`, memory base `c0e559efdf9f3b6ac81be1925329b04c06d27b4c`): **the one enforced citation row on this card re-read and re-cited, and its anchor re-bound to the construct this leaf left in place of the one it named.** The claim is about the split that makes each placement branch state only what its own condition established, and the helper it named — `_placement_refusal`, which exists nowhere in the tree — is `_placeable_baseline` (`mcp/src/agents_remember/cli/knowledge_ingest.py:266-297`), the narrowed `_CapturedBaseline | str` this leaf's repair made the caller branch on with a real `isinstance` before reading `payload` and `origin`. Only the anchor name and the range were corrected: the claim's wording, which describes the two returns and why one sentence could not serve both halves, still holds at the new extent and was left unchanged. No range was dropped to silence a finding, and no verification stamp was advanced — this card's stamp already names the leaf's code commit.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `COMMITTED_BATCH_STATES` repointed to mcp/src/agents_remember/cli/knowledge_ingest.py:97-97. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `_counts` repointed to mcp/src/agents_remember/cli/knowledge_ingest.py:423-435. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00 — [mechanical projection record, RETIRED 2026-09-24T07:54+02:00 by the 260921-ICR-L28 curator] A ccr-r10@v1 anchor-range projection had written a range for the list-ingest entry point under citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8. It is retired as evidence rather than re-anchored: a projected range is not a reading. The claims it was attached to were re-read against this candidate's own bytes, and the hand-derived ranges this document's tables carry are the ones in force. No content impact was claimed then and none is claimed now.

- 2026-09-20T18:45:00+02:00 — 260915-KS-L47 worker (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`): **the reviewer's before-snapshot is now captured before publication can overwrite it.** `_capture_baseline` reads `--baseline` at the top of `run`, ahead of `ingest_curator_list`, and `_place_review_baseline` writes those captured bytes. The defect this closes: `--baseline` and `--publish-to` may name one path, publication replaces that file **in place**, and the old post-ingest `shutil.copyfile(source, destination)` therefore copied the published candidate into the review's before half — the review then reported a real addition as present on both sides with `field_changes: []`, which is the rejected `KS-R22` Intent Reviewer comparison. Measured before the change on this base: the review's `before_snapshot_digest` equalled its `after_snapshot_digest` and the before statement read `present`; after the change the before half is byte-identical to the true fork point, the review answers before `absent` / after `present` over two different digests, and the retry preserves the half it was first handed. The surface table gained `_capture_baseline`/`_CapturedBaseline`; the two rows whose prose described the old copy-after-the-fact behaviour were rewritten rather than re-cited, and their ranges are dropped because those lines moved twice already. **Stamp accounting:** the recorded working candidate is this leaf's candidate on base `be325216`, which is the candidate this reading was performed against, and `lastUpdated` moved with it; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains this body and no stamp was measured on it. No commit was made.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **memory-side sync conflict resolved as a UNION; no side dropped.** The memory source branch advanced to `92f444b04` (260915-KS-L45) while this leaf's curation was in flight, so the sync's re-apply conflicted in this file. Both sides were kept because both are true: 260915-KS-L45's landed additions (the Intent-review entry path, the two published half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, the `missing_dataset_half` pair preflight, the receipt-derived `review_namespace`, and the enumerating reads) and this leaf's 260915-KS-L43 edits (the allocated-identity/derived-citation split, the retry key and its journal, the explicit anchor reuse, and the recovery's journaled decisions with the bounded cycling refusal). Where the two sides carried the same row in different line numbers, the row was re-measured against the moved line rather than picked: L45 curated against `fb719f89` and this leaf's source moves every citation below `:306` of `knowledge_curator_ingest.py` and renumbers `cli/knowledge_ingest.py` entirely, so the surviving ranges are the post-merge measurement for both. One **contradiction** is recorded rather than silently resolved: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` frontmatter pair is L45's (recorded against the moved line, the newest verification on record), while the recorded working candidate is this leaf's reading — two different claims, kept beside each other instead of one overwriting the other. No verification stamp was advanced by this leaf.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, code base `fb719f89`): **the run that authors the candidate is now the run that connects it to the review.** This card records the three facts a reader of this adapter needs. (1) `--candidate-directory` became **OPTIONAL**: omitting it derives `<worktree-group>/provider-runtime/dev-ar-coordination/knowledge/candidate` from the **contract's own recorded worktree group** through `_review_root` and the review's own **published** constants, which is what makes "the candidate this run authored" and "the candidate the review resolved" one directory instead of two conventions; naming a directory still wins and that draft is then simply not the leaf's review candidate. (2) `_place_review_baseline` is the review's other half: a committing run given `--baseline` **copies** that dataset into the baseline half, and every other outcome is a stated string (`not-placed: planning run…`, `not-placed: the batch did not commit (…)`, `not-placed: … is not a file`, `present: <path>` when the bytes already match) rather than an inferred boolean — the copy is deliberate, because the review's own recorded decision is that both halves sit in the leaf's disposable local root so a review reads nothing out of the live coordination tree. (3) The report gained `reviewBaseline` beside `candidateDirectory`, and `COMMITTED_BATCH_STATES` is the two-state set that decides whether placing is allowed at all. The module-level surface list was corrected where it had drifted (`_expected_destination`/`_outcome`/`_targets` now carry no line numbers, since those lines moved twice already) and the four reference rows whose constructs moved were re-cited. No anchor was renamed and no citation was dropped. No verification stamp was advanced, because no commit contains this body; the recorded working candidate is this leaf's candidate on base `fb719f89`.
- 2026-09-20T05:16+02:00 — 260915-KS-L39 curator (uncommitted CYCLE-01 change set on `ar/260915-ks-l39-ar`, code base `756c47b37fa16324a836a44336655413d10fffaa`): **the public baseline selection reached this adapter, and the card's own statement that it had not was corrected.** This card said the baseline "is deliberately **not** a CLI input" and that "a caller that selected none gets the cold-start behaviour" — true when it was written, false now. `add_arguments` declares `--baseline <published dataset>` (default `None`) and `run` passes it into the one `IngestSelection` as `baseline=None if args.baseline is None else Path(args.baseline)`, so a next task can begin from a prior task's published knowledge instead of from an empty candidate; omitting it is still the correct cold start for a repository's first task, which is why the argument and the selection field are one pairing rather than an option and a default. Every construct extent on this card was re-measured in this candidate, because the declaration moved the whole module: `add_arguments` `:64-114`→`:71-129`, `run` `:150-178`→`:165-194`, `_payload` `:218-252`→`:234-268`, `_counts` `:255-267`→`:271-283`, `_expected_destination` `:117-136`→`:132-151`, `_publication` `:139-147`→`:154-162`, `_summary` `:181-208`→`:197-224`, `_targets` `:211-215`→`:227-231` and `_outcome` `:270-304`→`:286-320`; the `ingest_curator_list`/`IngestSelection` row now cites the application module at `:846-952` and `:827-843`. No anchor was renamed and no citation was dropped. **Stamp accounting:** the recorded working candidate is this leaf's candidate `ar/260915-ks-l39-ar` on base `756c47b3`, which is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.
- 2026-09-20T02:05:20+00:00 — [mechanical projection record, RETIRED 2026-09-24T07:54+02:00 by the 260921-ICR-L28 curator] A ccr-r10@v1 anchor-range projection had written a range for the list-ingest entry point under citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8. It is retired as evidence rather than re-anchored: a projected range is not a reading. The claims it was attached to were re-read against this candidate's own bytes, and the hand-derived ranges this document's tables carry are the ones in force. No content impact was claimed then and none is claimed now.
- 2026-09-20T01:24+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **the publication step reached this adapter, and the card was re-read against it.** The checklist reopened two claims in this card — `run` and `_payload` — and both were re-read at their current constructs: `run` (lines 150-178) still drives one ingest and prints the report, and `_payload` (lines 218-252) is still the machine-readable report the caller consumes, so both retain their wording and only their ranges moved (`:89-116`→`:150-178`, `:149-180`→`:218-252`). The remaining reference rows were re-cited to their construct's own extent for the same reason, so every (anchor, range) pair in the table holds its own anchor: `add_arguments` `:51-86`→`:64-114`, `_counts` `:183-195`→`:255-267`, and `ingest_curator_list`/`IngestSelection` `:741-843`/`:725-739`→`:784-891`/`:764-781` in the application module. The Logic section was corrected where the source now contradicts it: `add_arguments` declares `--commit`, `--publish-to`, `--expected-destination` and `--json` (the `--dry-run` this card named is not a flag the module has), `_expected_destination` and `_publication` are added to the module-level surface, and `run` builds the one `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit, publication=_publication(args))` beside the baseline it still does not take from the CLI. No reference row, anchor or citation was deleted. Because this body now describes a working candidate no commit contains, the stale `lastVerifiedCommitHash` and `lastVerifiedCommitDate` rows were replaced by one recorded working candidate under the reopened-claim stamp rule: **no verification stamp was advanced and no commit hash was invented**; closeout owns the real code commit.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair. `ingest_curator_list` no longer accepts trailing keyword arguments: `run` now builds the one frozen `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit)` and passes it positionally, and the baseline a run may fork from is deliberately not a CLI input, so `--dry-run` still means "report what the real run would write". The Logic paragraph records the selection value, and the reference row now cites `IngestSelection` beside `ingest_curator_list`. Three citation defects this checklist reported were also cleared: the `ingest_curator_list` row carried **no range at all** (it cited the file bare) and now cites `knowledge_curator_ingest.py:741-843`; the `knowledge-ingest` anchor was a backticked non-identifier, which is not an anchor, so it is now the double-quoted literal `"knowledge-ingest"` inside `cli/__main__.py:35-43`; and the `__main__.py:36,42,43` source was not a citation form at all and is replaced by that range. The remaining rows (`add_arguments`, `run`, `_payload`, `_counts`) were re-cited to their construct extents, which moved when this leaf's `IngestSelection` construction landed. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `knowledge_ingest.py.md:81` (knowledge-ingest) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_ingest.py.md:80` — re-read: the anchor resolves exactly once in the named file at 681-780; the source cell was a bare path with no range, which the grammar refuses. Range re-derived from the file.


- 2026-09-19T17:30+02:00 — 260915-KS-L28: created this file-level onboarding card for the new source file, closing the gap the governed closeout preview reported (`onboarding_metadata_refresh.missing`). This module is the production caller that repairs review finding **M1-1** — the write plane previously had no caller outside its own module and tests. Anchors and ranges derived from the current candidate source (229 lines); verification metadata is left at this leaf's base `e7998504`, because the candidate is deliberately uncommitted and the governed closeout stamps the real code commit.
