# mcp/src/agents_remember/application/review_candidate_resolution.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The one owner of the **exact source endpoints** and the **dataset pair** a live curator review binds.
A review reads two things at once — the records two knowledge datasets hold, and the source the
candidate's recorded anchors are resolved against — and this module derives the second half: a pair of
immutable Git object identities plus the two code roots that travel with them.

The **baseline** is the enclosure contract's recorded `code_base_commit`; the **candidate** is the
tree `capture_future_code_candidate` derives through a private index (the leaf's `HEAD` with every
staged, unstaged and eligible untracked change applied, ignored paths still excluded by the existing
policy, the real Git index left byte-identical). The working tree is therefore never the endpoint, and
"HEAD to unstaged" published under the name of the full task diff is exactly what this binding
prevents.

It exists as its own module for two recorded reasons, both stated in the module's own docstring and
in the packet that required it: resolution is a responsibility of its own, and the adapter that used
to hold it (`application/knowledge_review.py`) is at the repository's file-size rail. There is no
second resolution path: `knowledge_review` re-exports these names, so the ingest CLI's existing import
of the three path constants keeps resolving and two spellings cannot drift apart.

**Every failure is a named state, never a `None` endpoint.** A contract that records no base commit, a
capture the shipped owner refused, and a capture whose inputs moved while the review was being composed
each produce a typed `ReviewRefusal` naming the offending side and the action that yields a reviewable
candidate. `HEAD`, another branch and a different working tree are all unavailable as substitutes.

## Code Commentary

### Logic

**`resolve_review_candidate` screens the three selectors, locates the leaf's own contract, binds the
recorded baseline, captures the candidate, and composes the pair — in that order.** Each of
`repository_id`, `master` and `leaf_id` must be a single path segment: a value that is empty, contains
`/` or `\`, or starts with `.` is refused as `candidate_unresolved` naming the segment, the offending
input and the next action. `_leaf_contract` globs
`<coordination_root>/tasks/<repository>/<master>/enclosures/*/series-contract.md`, loads each through
the shipped `load_contract`, skips a contract whose `repo_name` differs or whose cleanup is
`abandoned`, and returns the one whose `parent_task_name`/`task_name` matches the master and whose
`slugify(leaf_id)` matches. A contract that does not resolve is refused as `candidate_unresolved`; a
contract with no live `code_worktree` is refused as `candidate_not_live` and the refusal says the
landed leaf's committed change-set is **not this surface**.

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
and arrives here as that same named refusal. `candidate_code_root` is `contract.code_worktree` and
`candidate_code_tree_id` is `captured.codeCandidateTree`: the read context refuses a root without a
tree id, and supplying the root with a deliberately absent tree id — what the adapter did while a live
leaf's uncommitted line had no tree id — made every comparison raise instead of reporting the source
expansion it could not make.

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
it by returning a typed result. Both callers run this before they compare: `read_knowledge_review`
(through `compose_review`) and `list_knowledge_review_entries`. It returns the offending
`(half, database)` pair — `baseline` or `candidate` — because "author a candidate" and "place the
dataset this candidate forks from" are different next actions a reader cannot choose between from the
words "the datasets are absent".

**`review_namespace` reads the namespace from the record standing beside the bytes, and that is the
only authority for it.** A request names a *repository* (`agents-remember`); a dataset the write plane
placed is bound to a *namespace id* derived from it (`uuid5(namespace, "repository:<name>")`). A side
opened under the requested spelling therefore refuses against the dataset's own binding — the fixture
measured `the dataset … is bound to 40d350a6-…, not to the requested repository namespace
agents-remember` — which in the live product would have failed the review of every real candidate. So
the dataset's own **record** is read, and `repository_id` from that record is the namespace both sides
are opened under.

**Two records answer, because the two halves of a comparison are placed by two different acts.**
`260921-ICR-L34` corrected this function: it read `candidate-receipt.json` **alone**, which was right
for a *candidate* half — an admission writes and seals that receipt beside the working database — and
wrong for a **before** half placed by a run handed a published `--baseline`. A published dataset is
not an admitted candidate, so no receipt exists beside it; it carries `baseline-generation.json`
instead, written by `knowledge_baseline_generation`, and that record names the namespace its captured
bytes belong to. The corrected rule reads `CANDIDATE_RECEIPT_NAME` first, then the before half's own
`read_baseline_generation` record, and only then falls back to the requested repository. The
consequence is a **product** one and not a tidiness one: before the correction the before half of
every continuity run was opened under the requested repository name while its bytes were bound to a
namespace id, the storage owner refused that mismatch, and the freeze answered
`candidate_dataset_absent` — so **every leaf on the ordinary `knowledge-ingest --baseline` route
produced a comparison that could not be frozen**, and no test could see it because the fixtures
hand-assemble their pairs and so exercise the no-record shape. The first-generation path hid it too:
the empty before half it creates is built by the candidate-creation owner, which does leave a receipt
beside it.

A dataset with **neither** record beside it is one handed directly rather than placed by the write
plane (a fixture, or a pair a caller assembled from two named files): for that shape the requested
repository is the available identity and is read as it always was, which is what keeps the
hand-assembled caller-assembled contract intact. A record that **exists but cannot be read** is a
different fact and is refused — including a record *path* occupied by something that is not a record
file — because standing in the caller's word for the dataset's own record is exactly how a review
comes to read a namespace nothing admitted.

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
unchanged. `__all__` publishes exactly the names the adapter re-exports — the three `REVIEW_*` path
constants, `ReviewCandidateResolution`, `candidate_receipt_refusal`, `candidate_ref`,
`missing_dataset_half`, `refusal`, `require_current_candidate_identity`, `resolve_review_candidate`,
`review_namespace` and `unreadable_candidate_refusal` — so the
adapter's `__all__` and this one state the same surface. `candidate_ref` is this leaf's one addition:
it builds the surface's `ReviewCandidateRef` from the resolution's own leaf id, so the subject review
and the task-context review cannot name different leaves for one resolution. Private helpers are
one-purpose: `_leaf_contract`
locates the contract, `_captured_candidate` captures or refuses, `_capture_refusal` renders the
capture owner's failure, `_status_text` reads the owner's status, `_moved_candidate_refusal` renders a
moved input. Nothing here writes a file: the capture's private index lives in a temporary directory the
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
- **The two published directory names are this surface's one spelling.** `REVIEW_BASELINE_DIRECTORY`
  and `REVIEW_CANDIDATE_DIRECTORY` are the names the ingest CLI also reads, so "the candidate the leaf
  authored" and "the candidate the review resolved" are one directory rather than two conventions.
- **The namespace is the dataset's own, read from the record beside the bytes.** Either record answers
  — the candidate's admission receipt, or the before half's own generation record — and the requested
  repository name is used only when **neither** exists. A record that exists but cannot be read is
  refused rather than guessed past.
- **An absent dataset half is a named state, never an exception.** `missing_dataset_half` runs before
  any comparison and the refusal names which half is missing.
- **Unconverted memory reads are unchanged (MIK-R25; candidate invariant, not ingested).** `_live_resolution`
  asks `live_review_trees` first, which answers `None` for a leaf whose memory is unconverted; the dataset pair is
  then composed byte for byte as before, and `_index_namespace` answers `None` for any file that is not a derived
  index. Proved by `test_an_unconverted_leaf_keeps_the_dataset_review` and the worker's and reviewer's
  base-against-worktree comparison of 29 payloads (byte-identical).
- **Rank is the reason the module exists.** `serving` may not import `application`, and the adapter was
  at the file-size rail; resolution is therefore owned here and reached only through the adapter the
  composition root wires.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the capture owner it reuses, the contract loader and slug normalizer it locates a leaf
through, the read-context rule that makes a root without a tree id unusable, the adapter that
re-exports its names, and the case module that measures the whole chain. Three details a reader should
carry: the module adds **no** second capture implementation — it wraps the shipped owner's typed
failure and its own mid-capture head check; the three `REVIEW_*` constants are published here *and*
re-exported by `knowledge_review.py`, which is the import path `cli/knowledge_ingest.py` uses; and the
recheck is deliberately not part of resolution, because it belongs at publication time.

- **The module's own statement of what it binds, why the two sides are immutable object identities, why the working tree is never an endpoint, and that every failure is a named state.** [1]
- The published surface: the three path constants plus the nine callables the adapter re-exports — the seven it already had, `candidate_ref`, and the two unreadable-receipt names this leaf added. [2]
- The disposable candidate root and the two directory names, inside the leaf's disposable local root so a review reads no candidate out of the live coordination tree. [3]
- The three capture fields with the words a refusal names them by, in the owner's own observation order, and the one recapture action three refusals share. [4]
- **The resolution value: the two datasets (for a tree comparison, the two memory trees' derived indexes), the two code roots, the two tree ids, the carried contract, the captured identity the recheck re-derives, and MIK-R25's `trees` and `knowledge_unavailable`.** [5]
- **The whole resolution: selector screening, the contract locator, the recorded-base precondition, the capture, and the live pair handed to `_live_resolution` (four trees for a converted leaf, else the dataset pair) with both sides bound.** [6]
- **The re-publication recheck: for a tree comparison the memory candidate is recaptured first (MIK-R25), then the shipped capture owner re-run, every moved field named, and a resolution with no capture left exactly as assembled.** [7]
- A moved capture rendered as one refusal carrying **both** complete identities, generated by the model that owns them. [8]
- **The pair preflight: the absent half named as `baseline` or `candidate`, so the refusal says which dataset to author and which to place.** [9]
- **The record-beside-the-bytes namespace: the candidate's own sealed receipt when there is one, otherwise the before half's own `baseline-generation.json`, otherwise a derived knowledge index's own namespace (MIK-R25, `_index_namespace`), the requested repository used only when none of these answers, and an unreadable record refused rather than guessed past.** [10]
- **The one owner for the unreadable-candidate refusal: the code, the detail naming the candidate's own failure, the once-stated repair action, and the preflight form that turns the same question into a value.** [11]
- **The one construction of the reviewed candidate's reference, shared by the subject review and the task-context review so the two cannot name different leaves for the same resolution.** [12]
- The single refusal builder this surface uses, public because the adapter builds the entry route's refusal with it too. [13]
- **The capture is the existing owner's and stays the owner's: this module only turns its typed failure into the surface's named state.** [14]
- The capture owner's own mid-capture head check, which is what makes a head that moves *during* the capture a named state rather than a stale tree. [15]
- The surface's rendering of one capture-owner failure, naming the candidate side and the owner's own status word. [16]
- The one contract locator: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. [17]
- **The adapter that re-exports this surface, so the ingest CLI's existing import of the three constants keeps resolving and there is no second resolution path.** [18]
- The CLI that reads the two directory names through that re-export. [19]
- **The case module that measures the bound endpoints through the real resolution, the real capture and the real comparison.** [20]

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
[`review_committed_leaf`](review_committed_leaf.py.md)'s `resolve_committed_leaf_review` — the leaf's
published generation, or the source range its contract recorded. `candidate_not_live` is therefore no
longer the answer for a closed enclosure: it survives only for the one state in which it is true, a
leaf that is **neither live nor recorded**, and that state is now produced by the resolution that can
tell the difference. The import is local and is the only suppression this leaf's diff adds
(`# noqa: PLC0415 - cycle`), because the committed-leaf module resolves through this module's contract
accessor, so a module-level import would be a cycle with a type annotation on it.

**`_leaf_contract` is now public as `recorded_leaf_contract`, and nothing else about it changed.** Two
resolutions read the leaf's enclosure and they must read the *same* record: two scans of the enclosure
directory would be two answers to "which contract is this leaf's", and the second one is how a review
comes to be composed for a leaf nobody addressed. Every name importers used is still exported, so the
ingest CLI's existing import of the three `REVIEW_*` constants keeps resolving.

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

## 260921-ICR-L34 The Namespace Comes From The Record Beside The Bytes, And A Continuity Run's Before Half Becomes Freezable

`260921-ICR-L34` (D62 — recording a leaf's comparison generation and the families it binds) made the
review comparison **producible at all**, and this module carries one of the two defects that stood in
the way. The producer itself is the CLI's `review-record-comparison`
([`cli/review_comparison_record.py`](../../cli/review_comparison_record.py.md)), which composes the
review exactly as the surface does and publishes through the freeze owner.

**One rule changed, in one place.** `review_namespace` read `candidate-receipt.json` alone. A
*candidate* half has one — an admission wrote it — but a **before** half placed by a run handed a
published `--baseline` never does, because a published dataset is not an admitted candidate: it
carries `baseline-generation.json` instead, written by
[`knowledge_baseline_generation.py`](knowledge_baseline_generation.py.md). The read therefore fell
back to the *requested repository name* while the bytes were bound to a namespace id, and the storage
owner refused the mismatch. The function now reads **the record beside the bytes** — the receipt when
there is one, otherwise the before half's own generation record — and falls back to the requested
repository only when **neither** record exists, which is exactly the caller-assembled fixture shape
the docstring already carved out.

**The consequence was a product defect, not a tidiness one.** Every continuity run of
`knowledge-ingest --baseline` — the ordinary leaf route — produced a leaf whose comparison could not
be frozen, refused `candidate_dataset_absent` with the detail *"the candidate database is not bound to
repository namespace agents-remember"*. Nothing could see it while nothing called the freeze: the
seven test modules that pass hand-assembled pairs exercise the *no-record* shape, and the
first-generation path hides it because the empty before half it creates is built by the
candidate-creation owner, which does leave a receipt beside it. The one case this leaf added
(`test_the_placed_baseline_is_opened_under_its_own_recorded_namespace`, in
`mcp/tests/test_knowledge_ingest_comparison_generation.py`) drives the real placed-baseline journey and
bites: reverted in a scratch copy, it fails with `+ agents-remember`, the value that produced the
refusal.

**Nothing changes for the hand-assembled shape.** A directory with *no* record still answers with the
requested repository, so the modules that assemble a pair from two named files are untouched; and a
record that exists but cannot be read — including a record *path* occupied by something that is not a
record file — is still refused rather than read as absent.

**Boundary this leaf did not cross.** `knowledge-ingest` authors the candidate half and places the
dataset the leaf forks from; this leaf made that half *openable*, and it authors nothing itself. The
`# noqa: PLC0415 - cycle` local import L12 added is still the module's only suppression.

## 260928-MIK-L25 A Converted Leaf's Live Review Is Four Git Trees

**MIK-R25 rules 1, 2 and 6.** `resolve_review_candidate` now hands the captured pair to `_live_resolution`, which
asks `review_tree_comparison.live_review_trees` first: for a leaf whose memory is converted it captures, pins and
records the four trees and returns `tree_resolution(...)`, whose two databases are the derived indexes of the two
memory trees (never a copy); a pin failure or an unreadable side is a `ReviewRefusal`. For every other leaf it
returns `None` and the dataset pair below is composed exactly as before.

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

- The live pair: four trees for a converted leaf, else the dataset pair byte for byte. [21]
- A derived index answers its own namespace; any other file answers none. [22]
