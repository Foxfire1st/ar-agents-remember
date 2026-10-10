# mcp/src/agents_remember/application/review_candidate_resolution.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Resolves a canonical review selection into its exact before and candidate source/memory trees, with typed refusals when that selection cannot be resolved.

## Code Commentary

`resolve_review_candidate` admits only the declared selectors and enclosure identity. For a live leaf, `_live_resolution` obtains the source tree through the existing capture owner and resolves converted memory through `tree_resolution`. Its baseline_database and candidate_database fields name derived indexes of the selected trees. An unconverted half is explicitly legacy-unavailable, not an empty or substituted dataset. Recorded/closed leaf selection delegates to the retained generation owner. `require_current_candidate_identity` detects a candidate that moved after admission. The old REVIEW_BASELINE_DIRECTORY and REVIEW_CANDIDATE_DIRECTORY layout and dataset receipts are retired.

### Logic

**`resolve_review_candidate` screens the three selectors, locates the leaf's own contract, binds the
recorded baseline, captures the candidate, and composes the pair — in that order.** Each of
`repository_id`, `master` and `leaf_id` must be a single path segment: a value that is empty, contains
`/` or `\`, or starts with `.` is refused as `candidate_unresolved` naming the segment, the offending
input and the next action. `recorded_leaf_contract` globs
`<coordination_root>/tasks/<repository>/<master>/enclosures/*/series-contract.md`, loads each through
the shipped `load_contract`, skips a contract whose `repo_name` differs or whose cleanup is
`abandoned`, and returns the one whose `parent_task_name`/`task_name` matches the master and whose
`slugify(leaf_id)` matches. A contract that does not resolve is refused as `candidate_unresolved`.

**The recorded base is a precondition, and a contract that records none is refused by name rather than
half-resolved.** This leaf added that check: with `contract.code_base_commit` empty there is no
baseline endpoint to bind, so the operation returns `candidate_unresolved` with
`offending_input="baseline"` and a next action that says to repair the leaf's recorded base in its
enclosure contract. Before it, the baseline tree id was written as `code_base_commit or None` and the
side silently degraded to "no tree" — a state the resolution could not distinguish from a contract
that records nothing.

**The candidate side resolves to both a root and a tree id, from one capture.** `_captured_candidate`
calls the existing owner `capture_future_code_candidate(contract)` and turns its typed
`FutureCodeCandidateError` into this surface's refusal through `_capture_refusal`, which names the
`candidate` side, carries the owner's own status spelling (`getattr(error, "status", "unavailable")`)
and the one recapture action. The owner already re-derives `observedCodeHead` after the tree is
written, so a head that moves *during* the capture is caught there (`future-code-candidate-head-moved`)
and arrives here as that same named refusal.

**The resolution now carries the capture's own complete identity, and the recheck is a separate
operation because it belongs at a different moment.** `candidate_identity` is the
`FutureCodeCandidateIdentity` this resolution derived, kept so `require_current_candidate_identity`
can re-derive it at the *end* of composition, immediately before a payload would be published.
`None` for `candidate_identity` (or for `contract`) means a hand-assembled pair naming two files: it
has nothing to re-derive and is left exactly as it was assembled. The recheck does not re-implement
the capture — it calls the same owner again and compares the three fields the owner observes, in the
owner's own order, so a refusal lists the moved inputs left to right.

**`_moved_candidate_refusal` carries both complete identities rather than a summary.**
`expected` and `observed` are `accepted.model_dump_json()` and `current.model_dump_json()`, rendered
by the model that owns them, so a reader compares the side the detail names against the exact object
ids it changed from and to. `_CAPTURE_INPUTS` pairs each of the three fields with the words the
refusal needs for it (`observedCodeHead` → "the leaf worktree's code HEAD", `codeBaseCommit` → "the
contract's recorded task base commit", `codeCandidateTree` → "the captured candidate tree").
`_RECAPTURE_ACTION` is stated once because three refusals need it and a caller acts on all three the
same way: reopen the review so the candidate is captured again — no `HEAD`, branch or working-tree
substitution.

**The dataclass keeps its `| None` field types even though this module never produces one.** A
resolution assembled by hand (a caller comparing two named files) still names no root and no tree for
a side, and the composition still has to read that shape; but a resolution *this* module returns has
both sides bound, because a side that could not be bound is refused before a resolution exists. The
`contract` and `candidate_identity` fields are carried for callers that need the recorded task facts
and the recheck respectively, not re-derived by them.

**`missing_dataset_half` is the pair preflight, and it is what keeps an absent half a named state
rather than a storage exception.** A comparison is *between* two datasets, so an absent half is not a
smaller comparison — the shipped operation refuses a side whose database is not a file, and it refuses
it by returning a typed result. It returns the offending
`(half, database)` pair — `baseline` or `candidate` — because "author a candidate" and "place the
dataset this candidate forks from" are different next actions a reader cannot choose between from the
words "the datasets are absent".

A dataset with **neither** record beside it (a fixture, or a pair a caller assembled from two named files) is resolved by `review_namespace`: a derived index answers its own namespace, and any other file — or none — answers the requested namespace, as before. A record that **exists but cannot be read** keeps the requested namespace too — the index open fails and the same fallback applies. Refusal belongs to the namespace read, not to any receipt capture: `candidate_receipt_refusal` calls `review_namespace` (`mcp/src/agents_remember/application/review_candidate_resolution.py:419`) and converts a namespace error into `unreadable_candidate_refusal`; the source performs no receipt capture (`review_candidate_resolution.py:409-422`).

**`refusal(...)` is the single builder of a `ReviewRefusal` in this surface.** It is public because
both modules build refusals: this module builds the resolution's own, and `knowledge_review` imports it
to build the entry route's. `_status_text` exists only so a capture failure's detail can carry the
owner's own status word rather than a phrase invented here.

**One owner for the unreadable-candidate refusal, and the action is carried.** `unreadable_candidate_refusal(resolved, reason)` and
its preflight form `candidate_receipt_refusal(resolved)` are the only place the refusal's code,
detail, next action and offending input exist — the entry route, the subject route and the
task-context route all read them, so the three routes cannot drift apart about the same bytes. The
code is the shipped `candidate_dataset_absent` (this vocabulary's code for a pair input that cannot
be opened) and the detail names the candidate's own failure rather than the caller's; the next
action (`_REPAIR_CANDIDATE_ACTION`, stated once because three copies of the sentence is how the
routes stop agreeing) reaches the task-context body too, where the round-3 verification had measured
it absent. `candidate_receipt_refusal` is the preflight form for a caller that wants the state as a
value instead of an exception; a caller that would rather catch the storage error builds the
identical value from it with `unreadable_candidate_refusal`.

### Conventions

The module holds no vocabulary of its own: `ReviewCandidateResolution` is a frozen dataclass rather
than a pydantic model because it carries live paths and a loaded contract rather than a wire shape,
while `FutureCodeCandidateIdentity` stays the owner's own pydantic model and is passed through
unchanged. `candidate_ref` is this leaf's one addition:
it builds the surface's `ReviewCandidateRef` from the resolution's own leaf id, so the subject review
and the task-context review cannot name different leaves for one resolution. Nothing here writes a file: the capture's private index lives in a temporary directory the
owner creates under the worktree group's `reports/`, and the real index is never touched.

### Invariants And Boundaries

- **The endpoints are immutable Git object identities, never a working tree.** The baseline is the
  contract's recorded base commit; the candidate is a `write-tree` result. `HEAD`, a branch tip and a
  working directory are unreachable as endpoints.
- **The candidate is the whole add-all tree, and the real index is untouched.** The capture owner
  derives it through a private index; this module adds no second capture path and no index write.
- **No endpoint is ever `None` in a resolution this module produced.** An unbound side is a typed
  refusal before a resolution exists, so a caller never reads an absence it cannot distinguish from a
  measured value.
- **A moved capture input is a refusal, not a substitution.** The recheck re-derives the complete
  identity immediately before publication and refuses by name, carrying both identities.
- **An absent dataset half is a named state, never an exception.** `missing_dataset_half` runs before
  any comparison and the refusal names which half is missing.
- **Rank is the reason the module exists.** `serving` may not import `application`, and the adapter was
  at the file-size rail; resolution is therefore owned here and reached only through the adapter the
  composition root wires.

### Todos

None recorded.

## Evidence

### Repo-Internal References

- `resolve_review_candidate` owns the current boundary described above. [23]
- `_live_resolution` owns the current boundary described above. [24]
- `require_current_candidate_identity` owns the current boundary described above. [25]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of what it binds, why the two sides are immutable object identities, why the working tree is never an endpoint, and that every failure is a named state.** [26]
- The three capture fields with the words a refusal names them by, in the owner's own observation order, and the one recapture action three refusals share. [27]
- **The resolution value: the two datasets (for a tree comparison, the two memory trees' derived indexes), the two code roots, the two tree ids, the carried contract, the captured identity the recheck re-derives, and MIK-R25's `trees` and `knowledge_unavailable`.** [28]
- **The whole resolution: selector screening, the contract locator, the recorded-base precondition, the capture, and the live pair handed to `_live_resolution` (four trees for a converted leaf, else the dataset pair) with both sides bound.** [29]
- **The re-publication recheck: for a tree comparison the memory candidate is recaptured first (MIK-R25), then the shipped capture owner re-run, every moved field named, and a resolution with no capture left exactly as assembled.** [30]
- A moved capture rendered as one refusal carrying **both** complete identities, generated by the model that owns them. [31]
- **The pair preflight: the absent half named as `baseline` or `candidate`, so the refusal says which dataset to author and which to place.** [32]
- **The one owner for the unreadable-candidate refusal: the code, the detail naming the candidate's own failure, the once-stated repair action, and the preflight form that turns the same question into a value.** [33]
- **The one construction of the reviewed candidate's reference, shared by the subject review and the task-context review so the two cannot name different leaves for the same resolution.** [34]
- The single refusal builder this surface uses, public because the adapter builds the entry route's refusal with it too. [35]
- **The capture is the existing owner's and stays the owner's: this module only turns its typed failure into the surface's named state.** [36]
- The capture owner's own mid-capture head check, which is what makes a head that moves *during* the capture a named state rather than a stale tree. [37]
- The surface's rendering of one capture-owner failure, naming the candidate side and the owner's own status word. [38]
- The one contract locator: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. [39]
- **The case module that measures the bound endpoints through the real resolution, the real capture and the real comparison.** [40]
- The live pair: four trees for a converted leaf, else source-only identities for the legacy-unavailable side (canonical datasets retired). [41]
- A derived index answers its own namespace; any other file answers none. [42]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one coordination root's task tree
and one leaf's worktree, and carries no identity that ranges beyond the repository namespace the
request names.

No meaningful cross-repo references found.

## 260921-ICR-L12 A Closed Enclosure Resolves From Its Records Instead Of Being Refused

`260921-ICR-L12` (`ICR-R12@v1`) removes the intake defect this module's liveness screen was:
a cleaned leaf's review answered `candidate_not_live` ("the leaf's enclosure has no live worktree, so
there is no candidate to review"), so the ordinary committed diff succeeded while Intent Review could
not be opened at all.

**What changed.** `resolve_review_candidate` gained one keyword, `recorded=False`, and one branch: when
the caller names the leaf's recorded comparison **or** the enclosure is closed (`code_worktree` absent
or gone), the resolution is delegated to
[`review_committed_leaf`](review_committed_leaf.py.md)'s `resolve_committed_leaf_review` `candidate_not_live` is therefore no
longer the answer for a closed enclosure: it survives only for the one state in which it is true, a
leaf that is **neither live nor recorded**, and that state is now produced by the resolution that can
tell the difference. The import is local and is the only suppression this leaf's diff adds
(`# noqa: PLC0415 - cycle`), because the committed-leaf module resolves through this module's contract
accessor, so a module-level import would be a cycle with a type annotation on it.

**`ReviewCandidateResolution` gained one field, `closed_leaf`.** It is `None` for a live resolution —
"this candidate has a worktree and was captured from it" — and carries the record a closed leaf's
review was reopened from otherwise; its own owner constructs it, and the surface reads it to declare
which record answered.

**The live candidate root is now the repository that holds the object (`contract.code_repo_path`).**
A linked worktree shares its repository's object store, so both bound objects resolve in either root,
and the repository is the root a durable comparison generation records — which is what lets a closed
leaf's review reproduce the live one **byte for byte** instead of publishing an inventory whose
reproduction command names a checkout that cleanup removes. This is a behavioural change to a landed
path and it is recorded as one: the capture itself still reads the live worktree, and only the root the
two bound objects are read in moved. The R01 case that asserted the worktree path was strengthened to
measure the stronger fact (`git cat-file -t` in the named repository) rather than merely re-pointed.

## 260928-MIK-L25 A Converted Leaf's Live Review Is Four Git Trees

**MIK-R25 rules 1, 2 and 6.** `resolve_review_candidate` now hands the captured pair to `_live_resolution`, which
asks `review_tree_comparison.live_review_trees` first: for a leaf whose memory is converted it captures, pins and
records the four trees and returns `tree_resolution(...)`, whose two databases are the derived indexes of the two
memory trees (never a copy); a pin failure or an unreadable side is a `ReviewRefusal`.

- `ReviewCandidateResolution` gains `trees` (the four-tree comparison, `None` for the dataset review) and
  `knowledge_unavailable` (`(side, state, detail)` for each knowledge side a recorded comparison can no longer read,
  e.g. `legacy-unavailable`; such a side names no file).
- `require_current_candidate_identity` recaptures a live tree comparison's memory worktree
  (`recheck_memory_candidate`) before the code recheck, so a memory candidate that moved during composition is
  refused by name.
- `review_namespace` falls back to `_index_namespace`, which opens a file as a `KnowledgeIndex` and returns its
  own namespace; any other file (or none) answers `None` and keeps the requested repository, as before.
- **Rulings.** 2026-09-29T22:22:37 Q1 (the derived index is the permitted read path; no knowledge dataset or copy
  is opened) and Q5 (a review GET writes refs and objects, idempotently); review F6 (23:15:34) extends Q5 to the
  comparison record and the index and converted-base caches.
