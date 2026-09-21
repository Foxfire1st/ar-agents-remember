# mcp/src/agents_remember/application/review_candidate_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_candidate_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T15:17:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l2`, uncommitted; base `0fca5c69766aa95eebe950c19fbcdc83864ec35a` |
| lastVerifiedCommitHash | `71a4433e686b3380af97a0836bb82bab2c8f2aad` |
| lastVerifiedCommitDate | 2026-09-21T16:29:06+02:00|
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

**`review_namespace` reads the namespace from the candidate's own receipt, and that is the only
authority for it.** A request names a *repository* (`agents-remember`); a candidate the write plane
admitted is bound to a *namespace id* derived from it (`uuid5(namespace, "repository:<name>")`). A
side opened under the requested spelling therefore refuses against the dataset's own binding — the
fixture measured `the dataset … is bound to 40d350a6-…, not to the requested repository namespace
agents-remember` — which in the live product would have failed the review of every real candidate. So
the candidate's own **receipt** (`CANDIDATE_RECEIPT_NAME`, written and sealed beside the working
database by the admission that created it) is read, and `repository_id` from that receipt is the
namespace both sides are opened under. A candidate with **no** receipt beside its database is a dataset
handed directly rather than admitted (a fixture, or a pair a caller assembled from two named files):
for that shape the requested repository is the available identity and is read as it always was. A
receipt that **exists but cannot be read** is a different fact and is refused, because standing in the
caller's word for the dataset's own record is exactly how a review comes to read a namespace nothing
admitted.

**`refusal(...)` is the single builder of a `ReviewRefusal` in this surface.** It is public because
both modules build refusals: this module builds the resolution's own, and `knowledge_review` imports it
to build the entry route's. `_status_text` exists only so a capture failure's detail can carry the
owner's own status word rather than a phrase invented here.

### Conventions

The module holds no vocabulary of its own: `ReviewCandidateResolution` is a frozen dataclass rather
than a pydantic model because it carries live paths and a loaded contract rather than a wire shape,
while `FutureCodeCandidateIdentity` stays the owner's own pydantic model and is passed through
unchanged. `__all__` publishes exactly the names the adapter re-exports — the three `REVIEW_*` path
constants, `ReviewCandidateResolution`, `candidate_ref`, `missing_dataset_half`, `refusal`,
`require_current_candidate_identity`, `resolve_review_candidate` and `review_namespace` — so the
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
- **The namespace is the dataset's own, read from its receipt.** The requested repository name is used
  only when no receipt exists, and a receipt that exists but cannot be read is refused rather than
  guessed past.
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
| The published surface: the three path constants plus the seven callables the adapter re-exports — the six it already had, and `candidate_ref`, which this leaf added. | `__all__`; `candidate_ref` | mcp/src/agents_remember/application/review_candidate_resolution.py:58-76; mcp/src/agents_remember/application/review_candidate_resolution.py:202-218 |
| The disposable candidate root and the two directory names, inside the leaf's disposable local root so a review reads no candidate out of the live coordination tree. | `REVIEW_CANDIDATE_RELATIVE_ROOT`; `REVIEW_BASELINE_DIRECTORY`; `REVIEW_CANDIDATE_DIRECTORY` | mcp/src/agents_remember/application/review_candidate_resolution.py:77-87 |
| The three capture fields with the words a refusal names them by, in the owner's own observation order, and the one recapture action three refusals share. | `_CAPTURE_INPUTS`; `_RECAPTURE_ACTION` | mcp/src/agents_remember/application/review_candidate_resolution.py:88-99 |
| **The resolution value: the two datasets, the two code roots, the two tree ids, the carried contract and the captured identity the recheck re-derives.** | `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:97-127 |
| **The whole resolution: selector screening, the contract locator, the recorded-base precondition, the capture, and the pair composed with both sides bound.** | `resolve_review_candidate` | mcp/src/agents_remember/application/review_candidate_resolution.py:130-194 |
| **The re-publication recheck: the shipped capture owner re-run, every moved field named, and a resolution with no capture left exactly as assembled.** | `require_current_candidate_identity` | mcp/src/agents_remember/application/review_candidate_resolution.py:197-226 |
| A moved capture rendered as one refusal carrying **both** complete identities, generated by the model that owns them. | `_moved_candidate_refusal` | mcp/src/agents_remember/application/review_candidate_resolution.py:253-276 |
| **The pair preflight: the absent half named as `baseline` or `candidate`, so the refusal says which dataset to author and which to place.** | `missing_dataset_half` | mcp/src/agents_remember/application/review_candidate_resolution.py:279-297 |
| **The receipt-derived namespace: read from the candidate's own sealed receipt, the requested repository used only when no receipt exists, and an unreadable receipt refused rather than guessed past.** | `review_namespace`; `read_candidate_receipt`; `CANDIDATE_RECEIPT_NAME` | mcp/src/agents_remember/application/review_candidate_resolution.py:276-301; mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:61-88; mcp/src/agents_remember/models/knowledge/snapshot.py:52-72 |
| **The one construction of the reviewed candidate's reference, shared by the subject review and the task-context review so the two cannot name different leaves for the same resolution.** | `candidate_ref`; `ReviewCandidateRef` | mcp/src/agents_remember/application/review_candidate_resolution.py:202-218; mcp/src/agents_remember/models/knowledge/review.py:178-189 |
| The single refusal builder this surface uses, public because the adapter builds the entry route's refusal with it too. | `refusal` | mcp/src/agents_remember/application/review_candidate_resolution.py:328-342 |
| **The capture is the existing owner's and stays the owner's: this module only turns its typed failure into the surface's named state.** | `_captured_candidate`; `capture_future_code_candidate`; `FutureCodeCandidateIdentity` | mcp/src/agents_remember/application/review_candidate_resolution.py:345-359; mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:14-51 |
| The capture owner's own mid-capture head check, which is what makes a head that moves *during* the capture a named state rather than a stale tree. | `capture_future_code_candidate` (head re-read) | mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:25-51 |
| The surface's rendering of one capture-owner failure, naming the candidate side and the owner's own status word. | `_capture_refusal`; `_status_text` | mcp/src/agents_remember/application/review_candidate_resolution.py:362-373; mcp/src/agents_remember/application/review_candidate_resolution.py:376-379 |
| The one contract locator: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. | `_leaf_contract`; `load_contract`; `slugify` | mcp/src/agents_remember/application/review_candidate_resolution.py:382-402; mcp/src/agents_remember/worktrees/worktree_contract.py:430-472; mcp/src/agents_remember/worktrees/task_resolver.py:16-27 |
| **The adapter that re-exports this surface, so the ingest CLI's existing import of the three constants keeps resolving and there is no second resolution path.** | `resolve_review_candidate`; `read_knowledge_review`; `candidate_ref` | mcp/src/agents_remember/application/knowledge_review.py:43-123; mcp/src/agents_remember/application/knowledge_review.py:125-142; mcp/src/agents_remember/application/knowledge_review.py:161-189 |
| The CLI that reads the two directory names through that re-export. | `REVIEW_BASELINE_DIRECTORY`; `REVIEW_CANDIDATE_DIRECTORY` | mcp/src/agents_remember/cli/knowledge_ingest.py:102-103 |
| **The case module that measures the bound endpoints through the real resolution, the real capture and the real comparison.** | `test_the_live_candidate_binds_the_recorded_base_and_the_captured_tree`; `test_a_capture_input_that_moves_before_publication_is_refused_by_name` | mcp/tests/test_knowledge_review_source_endpoints.py:360-391; mcp/tests/test_knowledge_review_source_endpoints.py:459-483 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one coordination root's task tree
and one leaf's worktree, and carries no identity that ranges beyond the repository namespace the
request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T15:25+02:00 — 260921-ICR-L5 curator, **the second quality pass's enforced rows re-read and re-cited; every one of them was a range that had drifted out from under its anchor.** Rows repaired here by re-deriving each range from the construct's own extent in the merged candidate, with claim wording retained because each claim still states what the code does: the CLI-that-reads-the-two-names row, which cited the pre-leaf import block `82-84` and now cites `102-103` where the merged CLI imports them. No verification stamp was advanced — the working tree still differs from every recorded stamp, so closeout owns that stamp.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **the sync's memory-side conflict in this card resolved as a union, with both sides' ranges re-derived against the merged candidate and two claims corrected rather than merged.** Kept from the master line: L5's re-cited CLI row (`cli/knowledge_ingest.py:102-103`, where the merged 620-line CLI imports the two half-names) and its `0fca5c69` / `14:06:50` verification rows, which are left exactly as recorded. Kept from this leaf: `candidate_ref`, the seven-callable published surface, and the `_capture_refusal`/`_status_text` and `_leaf_contract` rows at their extents in the unchanged 402-line module. **Corrected rather than merged:** the adapter-re-export row's two ranges (`knowledge_review.py:44-52`/`116-130`) named the pre-merge import block and `__all__`, which the merged 888-line adapter has moved to `43-123` and `125-142` — the row now also names `candidate_ref`, because that re-export is part of what keeps the import path resolving; and the case-module row's first range (`336-367`) pointed at the wrong end of the case it names, so it is now the case's own declaration (`360-391`). No claim was dropped and none was invented.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **one additive helper, and the reason it is here rather than in either composition.** `candidate_ref(resolved, *, repository_id, master)` is the single construction of the surface's `ReviewCandidateRef` — task context plus the resolution's **own** leaf id, never the requested spelling, and no path in it. It exists because the subject review and the task-context review both build that value, and two constructions are how the same resolution comes to name two different leaves. `__all__` gained the one name and the adapter re-exports it; nothing else in the module changed. Consequence for a reader: the module is now the owner of the candidate *reference* as well as the candidate *resolution*, and the reference is derived from the resolution rather than passed in. The two rows this moved were re-derived against this candidate, and the row for the published surface now counts seven callables. **Stamp accounting:** the verification rows still name `702714fc05363cb28eacaf101ba8384475a6aa56`, the last real commit on this line, because nothing in this leaf is committed; the claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, base `f745e16659c5602252bb185a2ffccc356c2bde26`): created this one-to-one card for the module the leaf introduced as the review surface's one owner of exact source endpoints and of the dataset pair. The card records what the move changed rather than only where the code now lives: the resolution binds the contract's **recorded base commit** on one side and the **captured add-all candidate tree** on the other, with the candidate side supplying both a root and a tree id (before, `candidate_code_root` was deliberately `None`); a contract that records **no base commit** is now refused by name with `offending_input="baseline"` instead of degrading to a `None` tree; `candidate_identity` is carried so the composition can re-derive the whole identity immediately before publication; and the capture stays the existing `future_code_candidate` owner's, wrapped rather than re-implemented. **Stamp accounting:** the two verification rows name `f745e16659c5602252bb185a2ffccc356c2bde26`, the last real commit on this line, because the external-memory refresh gate requires verification metadata before the memory commit; every construct this card cites exists only in this leaf's uncommitted candidate and no commit contains the content those rows would otherwise claim to have verified, so the governed closeout owns the real stamp.