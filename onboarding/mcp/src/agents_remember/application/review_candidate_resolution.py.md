# mcp/src/agents_remember/application/review_candidate_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_candidate_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T04:31:57+02:00 |
| lastVerifiedCommitHash | `d9e7e6e79ce532d16c689435ae95a63aab430f94` |
| lastVerifiedCommitDate | 2026-09-25T22:40:41+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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
- **Rank is the reason the module exists.** `serving` may not import `application`, and the adapter was
  at the file-size rail; resolution is therefore owned here and reached only through the adapter the
  composition root wires.

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
functions, the capture owner it reuses, the contract loader and slug normalizer it locates a leaf
through, the read-context rule that makes a root without a tree id unusable, the adapter that
re-exports its names, and the case module that measures the whole chain. Three details a reader should
carry: the module adds **no** second capture implementation — it wraps the shipped owner's typed
failure and its own mid-capture head check; the three `REVIEW_*` constants are published here *and*
re-exported by `knowledge_review.py`, which is the import path `cli/knowledge_ingest.py` uses; and the
recheck is deliberately not part of resolution, because it belongs at publication time.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it binds, why the two sides are immutable object identities, why the working tree is never an endpoint, and that every failure is a named state.** | `code_base_commit`; `capture_future_code_candidate` | mcp/src/agents_remember/application/review_candidate_resolution.py:1-28 |
| The published surface: the three path constants plus the nine callables the adapter re-exports — the seven it already had, `candidate_ref`, and the two unreadable-receipt names this leaf added. | `__all__`; `candidate_ref` |mcp/src/agents_remember/application/review_candidate_resolution.py:73-87; mcp/src/agents_remember/application/review_candidate_resolution.py:250-266|
| The disposable candidate root and the two directory names, inside the leaf's disposable local root so a review reads no candidate out of the live coordination tree. | `REVIEW_CANDIDATE_RELATIVE_ROOT`; `REVIEW_BASELINE_DIRECTORY`; `REVIEW_CANDIDATE_DIRECTORY` |mcp/src/agents_remember/application/review_candidate_resolution.py:98-98; mcp/src/agents_remember/application/review_candidate_resolution.py:104-104; mcp/src/agents_remember/application/review_candidate_resolution.py:105-105|
| The three capture fields with the words a refusal names them by, in the owner's own observation order, and the one recapture action three refusals share. | `_CAPTURE_INPUTS`; `_RECAPTURE_ACTION` |mcp/src/agents_remember/application/review_candidate_resolution.py:106-110; mcp/src/agents_remember/application/review_candidate_resolution.py:114-117|
| **The resolution value: the two datasets, the two code roots, the two tree ids, the carried contract and the captured identity the recheck re-derives.** | `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:106-135 |
| **The whole resolution: selector screening, the contract locator, the recorded-base precondition, the capture, and the pair composed with both sides bound.** | `resolve_review_candidate` | mcp/src/agents_remember/application/review_candidate_resolution.py:138-202 |
| **The re-publication recheck: the shipped capture owner re-run, every moved field named, and a resolution with no capture left exactly as assembled.** | `require_current_candidate_identity` |mcp/src/agents_remember/application/review_candidate_resolution.py:269-298|
| A moved capture rendered as one refusal carrying **both** complete identities, generated by the model that owns them. | `_moved_candidate_refusal` |mcp/src/agents_remember/application/review_candidate_resolution.py:301-324|
| **The pair preflight: the absent half named as `baseline` or `candidate`, so the refusal says which dataset to author and which to place.** | `missing_dataset_half` |mcp/src/agents_remember/application/review_candidate_resolution.py:327-345|
| **The record-beside-the-bytes namespace: the candidate's own sealed receipt when there is one, otherwise the before half's own `baseline-generation.json`, the requested repository used only when neither record exists, and an unreadable record refused rather than guessed past.** | `review_namespace`; `read_candidate_receipt`; `CANDIDATE_RECEIPT_NAME`; `read_baseline_generation` |mcp/src/agents_remember/application/review_candidate_resolution.py:351-399; mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:61-86; mcp/src/agents_remember/models/knowledge/snapshot.py:53-53; mcp/src/agents_remember/application/knowledge_baseline_generation.py:285-316 |
| **The one owner for the unreadable-candidate refusal: the code, the detail naming the candidate's own failure, the once-stated repair action, and the preflight form that turns the same question into a value.** | `_REPAIR_CANDIDATE_ACTION`; `unreadable_candidate_refusal`; `candidate_receipt_refusal` |mcp/src/agents_remember/application/review_candidate_resolution.py:393-399; mcp/src/agents_remember/application/review_candidate_resolution.py:402-417; mcp/src/agents_remember/application/review_candidate_resolution.py:420-433|
| **The one construction of the reviewed candidate's reference, shared by the subject review and the task-context review so the two cannot name different leaves for the same resolution.** | `candidate_ref`; `ReviewCandidateRef` |mcp/src/agents_remember/application/review_candidate_resolution.py:250-266; mcp/src/agents_remember/models/knowledge/review.py:304-315|
| The single refusal builder this surface uses, public because the adapter builds the entry route's refusal with it too. | `refusal` | mcp/src/agents_remember/application/review_candidate_resolution.py:436-450 |
| **The capture is the existing owner's and stays the owner's: this module only turns its typed failure into the surface's named state.** | `_captured_candidate`; `capture_future_code_candidate`; `FutureCodeCandidateIdentity` |mcp/src/agents_remember/application/review_candidate_resolution.py:453-467; mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:25-52; mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:15-22|
| The capture owner's own mid-capture head check, which is what makes a head that moves *during* the capture a named state rather than a stale tree. | `capture_future_code_candidate` (head re-read) | mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:25-51 |
| The surface's rendering of one capture-owner failure, naming the candidate side and the owner's own status word. | `_capture_refusal`; `_status_text` |mcp/src/agents_remember/application/review_candidate_resolution.py:470-481; mcp/src/agents_remember/application/review_candidate_resolution.py:484-487|
| The one contract locator: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. | `recorded_leaf_contract`; `load_contract`; `slugify` | mcp/src/agents_remember/application/review_candidate_resolution.py:473-500; mcp/src/agents_remember/worktrees/worktree_contract.py:437-467; mcp/src/agents_remember/worktrees/task_resolver.py:16-27 |
| **The adapter that re-exports this surface, so the ingest CLI's existing import of the three constants keeps resolving and there is no second resolution path.** | `resolve_review_candidate`; `read_knowledge_review`; `candidate_ref` | mcp/src/agents_remember/application/knowledge_review.py:75-88; mcp/src/agents_remember/application/knowledge_review.py:226-253 |
| The CLI that reads the two directory names through that re-export. | `REVIEW_BASELINE_DIRECTORY`; `REVIEW_CANDIDATE_DIRECTORY` | mcp/src/agents_remember/cli/knowledge_ingest.py:143-145 |
| **The case module that measures the bound endpoints through the real resolution, the real capture and the real comparison.** | `test_the_live_candidate_binds_the_recorded_base_and_the_captured_tree`; `test_a_capture_input_that_moves_before_publication_is_refused_by_name` |mcp/tests/test_knowledge_review_source_endpoints.py:436-478; mcp/tests/test_knowledge_review_source_endpoints.py:546-570|

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one coordination root's task tree
and one leaf's worktree, and carries no identity that ranges beyond the repository namespace the
request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T09:15:00+02:00 — 260921-ICR-L4 curator (sync-merge resolution of the parked candidate against the landed line, merged base code `d21bc8a6` / memory `75bb4d65`): **header union only.** The landed line's stamp (`8ff80ce0`) is kept and this leaf's candidate row now names the merged base; the module itself is untouched by landed siblings (still 448 lines), so every reference row already reads against the merged tree. No verification stamp was advanced.
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the one owner for the unreadable-candidate refusal (402 → 448 lines).** `unreadable_candidate_refusal` and its preflight form `candidate_receipt_refusal` are now the only place the refusal's code, detail, next action and offending input exist — the entry route, the subject route and the task-context route all read them — and the actionable repair instruction reaches the task-context body, where the previous round had measured it absent. `__all__` is nine callables. Every reference row was re-derived against this candidate. **Stamp accounting:** old verification rows name the last real commit; this leaf's claims were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; the ranges that moved belong to the leaf's other edits — the CLI's import block moved 541 → 692 lines with this leaf's destination-decision surface (the three `REVIEW_*` names this card cites are now on `:143-145` instead of `:102-103`). Each row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T15:25+02:00 — 260921-ICR-L5 curator, **the second quality pass's enforced rows re-read and re-cited; every one of them was a range that had drifted out from under its anchor.** Rows repaired here by re-deriving each range from the construct's own extent in the merged candidate, with claim wording retained because each claim still states what the code does: the CLI-that-reads-the-two-names row, which cited the pre-leaf import block `82-84` and now cites `102-103` where the merged CLI imports them. No verification stamp was advanced — the working tree still differs from every recorded stamp, so closeout owns that stamp.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this card resolved as a union, with both sides' ranges re-derived against the merged candidate and two claims corrected rather than merged.** Kept from the master line: L5's re-cited CLI row (`cli/knowledge_ingest.py:102-103`, where the merged 620-line CLI imports the two half-names) and its `0fca5c69` / `14:06:50` verification rows, which are left exactly as recorded. Kept from this leaf: `candidate_ref`, the seven-callable published surface, and the `_capture_refusal`/`_status_text` and `_leaf_contract` rows at their extents in the unchanged 402-line module. **Corrected rather than merged:** the adapter-re-export row's two ranges (`knowledge_review.py:44-52`/`116-130`) named the pre-merge import block and `__all__`, which the merged 888-line adapter has moved to `43-123` and `125-142` — the row now also names `candidate_ref`, because that re-export is part of what keeps the import path resolving; and the case-module row's first range (`336-367`) pointed at the wrong end of the case it names, so it is now the case's own declaration (`360-391`). No claim was dropped and none was invented.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **one additive helper, and the reason it is here rather than in either composition.** `candidate_ref(resolved, *, repository_id, master)` is the single construction of the surface's `ReviewCandidateRef` — task context plus the resolution's **own** leaf id, never the requested spelling, and no path in it. It exists because the subject review and the task-context review both build that value, and two constructions are how the same resolution comes to name two different leaves. `__all__` gained the one name and the adapter re-exports it; nothing else in the module changed. Consequence for a reader: the module is now the owner of the candidate *reference* as well as the candidate *resolution*, and the reference is derived from the resolution rather than passed in. The two rows this moved were re-derived against this candidate, and the row for the published surface now counts seven callables. **Stamp accounting:** the verification rows still name `702714fc05363cb28eacaf101ba8384475a6aa56`, the last real commit on this line, because nothing in this leaf is committed; the claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, base `f745e16659c5602252bb185a2ffccc356c2bde26`): created this one-to-one card for the module the leaf introduced as the review surface's one owner of exact source endpoints and of the dataset pair. The card records what the move changed rather than only where the code now lives: the resolution binds the contract's **recorded base commit** on one side and the **captured add-all candidate tree** on the other, with the candidate side supplying both a root and a tree id (before, `candidate_code_root` was deliberately `None`); a contract that records **no base commit** is now refused by name with `offending_input="baseline"` instead of degrading to a `None` tree; `candidate_identity` is carried so the composition can re-derive the whole identity immediately before publication; and the capture stays the existing `future_code_candidate` owner's, wrapped rather than re-implemented. **Stamp accounting:** the two verification rows name `f745e16659c5602252bb185a2ffccc356c2bde26`, the last real commit on this line, because the external-memory refresh gate requires verification metadata before the memory commit; every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the content those rows would otherwise claim to have verified, so the governed closeout owns the real stamp.
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

## Update History
- 2026-09-25T22:00:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, uncommitted change set on `ar/260921-icr-l34-ar`, code base `a9a1a41bba535803421470bd17d858657177cb5f` plus the working-tree delta): **the namespace is read from the record beside the bytes (D62).** `review_namespace` read `candidate-receipt.json` alone; a **before** half placed by a run handed a published `--baseline` has no receipt — a published dataset is not an admitted candidate — and carries `baseline-generation.json` instead, so the read fell back to the requested repository name while the bytes are bound to a namespace id, and the storage owner refused the mismatch. The consequence was a product defect: **every leaf on the ordinary `knowledge-ingest --baseline` route produced a comparison that could not be frozen**, refused `candidate_dataset_absent`, and no test could see it because the fixtures hand-assemble their pairs. The function now reads the receipt when there is one, otherwise the before half's own `read_baseline_generation` record, and falls back to the requested repository only when neither exists. The prose, the invariant bullet and the reference row that stated the receipt-only rule are corrected in place, and the reference row is re-anchored at the function's own extent (`:351-399`) with the second record named beside it. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so no commit carries the corrected body, and the governed closeout owns the real stamp.
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the closed enclosure resolves from its records (ICR-R12@v1).** `resolve_review_candidate` gained
`recorded=` and the closed-enclosure branch that delegates to `review_committed_leaf`, so
`candidate_not_live` now answers only the state where nothing is live **and** nothing is recorded;
`_leaf_contract` is public as `recorded_leaf_contract` because two resolutions must read the same
enclosure; `ReviewCandidateResolution` carries the `closed_leaf` record; and the live candidate root
names the **repository** that holds the object, which is what makes a reopened comparison reproduce the
live one byte for byte. The one local import is the only suppression this leaf's diff adds, with no
limit widened. **Citation accounting:** every row into this module was re-derived against the candidate,
and the rows this leaf moved are repaired in place. **Stamp accounting:** no verification stamp was
advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
