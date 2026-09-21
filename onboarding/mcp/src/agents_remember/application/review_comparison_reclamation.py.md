# mcp/src/agents_remember/application/review_comparison_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_comparison_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T19:40:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l11`, uncommitted; base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75` |
| lastVerifiedCommitHash | `d80a0513e928ef29a973527d09597c82c96fde87` |
| lastVerifiedCommitDate | 2026-09-21T19:51:20+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The two operations that may delete a durable comparison generation's content, and therefore the
bounded reclamation path every artifact created by a freeze points at.** `review_comparison_freeze`
records a `deletion_owner` and a `cleanup_scope` on each pin and each retained snapshot; the two
constants in this module *are* those owners, and the two functions are those operations.

The module exists because of the packet's own rule — *a new snapshot or pin that cannot name its bounded
reclamation path is unbounded durable state* — and its whole design follows from two properties the
reopen depends on:

1. **The record comes first.** Each operation writes its unavailable-history record into the generation's
   own directory **before** it deletes anything, so an interruption leaves the honest ordering (a record
   for content that is still there) rather than the misleading one. The record is what lets a later
   reopen answer *"this was deleted deliberately, here is why"* instead of reporting an unexplained loss.
2. **Only what the manifest named, inside the scope the manifest recorded.** A code release deletes
   exactly the ref the manifest recorded and refuses a ref that has moved; a snapshot discard deletes
   exactly the recorded `cleanup_scope` of each retained half. Neither touches the manifest — the
   manifest is the record *that the generation existed*, and a reopen has to be able to say so — and
   neither reaches into another generation's directory or another leaf's namespace.

**Nothing here decides *when* a comparison is finished with.** Release and discard are explicit acts a
caller performs: the freeze and reopen paths never call them, so *when* a comparison may be reclaimed is
a lifecycle decision with no owner in this leaf.

## Code Commentary

### Logic

**`release_comparison_code_object` (`:77-124`) — the deletion owner for one generation's code pin.** It
reads the generation's manifest through `_read_manifest_for_owner` (`:244-250`), and if the record names
**no pin** it raises `CodeObjectRetentionError("code-object-ref-absent")` rather than reporting a
successful no-op: a tree that committed history already held has nothing this owner may release. It then:

- **fails fast before recording anything.** `_require_the_ref_names_the_record` (`:150-165`) refuses when
  the ref no longer points at the recorded commit, checked *ahead of* the record for the reason the
  record exists — "a deletion record written for a release that was then refused would claim a history
  this owner never made unavailable, and a later reopen would report that claim". The retention owner
  re-checks under its own call, so this is a fail-fast rather than the authority.
- **measures custody before deleting it.** The record's `released_custody` is
  `code_object_observation(repository, retained.tree, names)`, taken *before* the ref is deleted, because
  "neither can be recovered after the fact" — and a reader of the record cannot tell afterwards whether a
  release discarded the last copy of a tree or merely stopped duplicating history a branch already holds.
  `_custody_names` (`:127-138`) reads the names back **from the manifest**, not from a live contract,
  because a release happens long after the leaf's enclosure may be gone and the record is the only thing
  that still knows which refs were asked.
- **writes the record, then deletes, and takes the record back if the deletion refuses.** If
  `release_retained_code_object` raises, the already-written record is unlinked (`record.unlink`) so the
  operation leaves neither a false record nor a half state.

**`discard_comparison_snapshots` (`:174-210`) — the deletion owner for the retained knowledge
snapshots.** For each `retained` binding it writes one `ComparisonHistoryDeletion` per half, in the
record's own vocabulary (`_knowledge_target`, `:144-147`: `knowledge-before` / `knowledge-after`), inside
that half's own recorded `cleanup_scope`, and returns the records it wrote. A half that is not `retained`
is skipped: it has no artifact to delete. The manifest file itself is never removed.

**The deleted digest is *measured*, never copied from the manifest.** `_measure_and_remove` (`:213-241`)
reads the snapshot, digests it, and compares against `binding.artifact.sha256`
**before** unlinking anything. A mismatch raises
`ComparisonReclamationError("snapshot-bytes-mismatch")` with both digests named and *nothing* recorded or
removed — because a deletion record that named content this owner did not delete would be a false record
of its own act. A snapshot that is already gone is recorded as `deleted_digest=None`, so a retry of an
interrupted discard **converges** instead of failing, and the record still states what was found. An
unreadable file (anything but `FileNotFoundError`) is `snapshot-unreadable` rather than a silent skip.

**The two error types are raised rather than returned, deliberately.** `ComparisonReclamationError` is
raised because "the caller is a deletion: the caller must not proceed to record a deletion, and a
returned value would make 'nothing was removed' easy to overlook at the one place where removing the
wrong bytes is irreversible" (its own docstring in `errors.py`); `CodeObjectRetentionError` is reused for
the ref-shaped failures because the same typed failure already owns them.

### Conventions

`__all__` publishes the two owner constants and the two operations — exactly the surface a freeze needs
to *name* its deletion owner and a caller needs to *perform* the deletion. `CodeObjectTarget` and
`KnowledgeTarget` (`:67-68`) are `Literal` types spelled with the record's own literal vocabulary, so a
release and a discard cannot come to name a target the record does not have. `_now()` (`:71-74`) is the
module's one clock read, used only when the caller supplies no `recorded_at`; both operations accept one
so a caller can make a batch of deletions share a timestamp.

### Invariants And Boundaries

- **The record precedes the deletion**, in both operations, so an interruption never leaves deleted
  content with no explanation.
- **A deletion record is withdrawn if the deletion it describes does not happen.** The code release
  unlinks its record when the retention owner refuses.
- **A released ref must still name the recorded commit.** A moved ref is refused and the ref is left in
  place.
- **A discarded snapshot must still hold the recorded bytes.** A mismatch is refused with nothing
  removed and nothing recorded; an already-absent snapshot is recorded honestly as `None`.
- **The manifest is never deleted** — a reopen has to be able to say the generation existed.
- **Scope is per-generation and per-half.** Nothing here reaches into another generation's directory,
  another leaf's namespace, or a path outside a recorded `cleanup_scope`.
- **No policy.** *When* a comparison may be released or discarded is not decided here; this module
  provides the acts, and no owner in this leaf calls them.
- **Boundary: retained-history deletion is explicit and leaves an unavailable-history record rather than
  aliasing today's data** — the reopen reports `unavailable-history` from these records, never by
  resolving whatever the path holds now.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the manifest fields
it is bounded by, and in the cases that measure both deletions. Three details a reader should carry: the
record is written **before** the deletion and withdrawn if the deletion refuses; the deleted digest is
**measured**, not copied, and an already-absent snapshot converges as `None`; and the custody recorded at
release is taken *before* the ref is removed, because it cannot be recovered afterwards.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the two properties the reopen depends on, and of what it deliberately does not decide. | *(module docstring)* | mcp/src/agents_remember/application/review_comparison_reclamation.py:1-23 |
| **The two canonical deletion owners the manifest names on everything a freeze creates.** | `CODE_OBJECT_DELETION_OWNER`; `SNAPSHOT_DELETION_OWNER`; `__all__` | mcp/src/agents_remember/application/review_comparison_reclamation.py:50-63 |
| The deletion targets, spelled with the record's own literal vocabulary. | `CodeObjectTarget`; `KnowledgeTarget`; `_knowledge_target`; `_CODE_OBJECT_TARGET` | mcp/src/agents_remember/application/review_comparison_reclamation.py:67-68; mcp/src/agents_remember/application/review_comparison_reclamation.py:141-147 |
| **The code release: no pin → refuse; moved ref → refuse before recording; custody measured before deletion; record written first and withdrawn if the release refuses.** | `release_comparison_code_object`; `_require_the_ref_names_the_record`; `_ref_exists` | mcp/src/agents_remember/application/review_comparison_reclamation.py:77-124; mcp/src/agents_remember/application/review_comparison_reclamation.py:150-171 |
| **The custody names read back from the record rather than re-derived from a live contract, because the enclosure may be gone.** | `_custody_names` | mcp/src/agents_remember/application/review_comparison_reclamation.py:127-138 |
| **The snapshot discard: one record per retained half, inside its own recorded cleanup scope, and the manifest left in place.** | `discard_comparison_snapshots` | mcp/src/agents_remember/application/review_comparison_reclamation.py:174-210 |
| **The digest that is measured rather than copied, the mismatch that records nothing, and the already-absent snapshot that converges as `None`.** | `_measure_and_remove` | mcp/src/agents_remember/application/review_comparison_reclamation.py:213-241 |
| The record the two operations write, and the manifest read that bounds them. | `ComparisonHistoryDeletion`; `write_history_deletion`; `read_manifest` | mcp/src/agents_remember/application/review_comparison_generation.py:472-489; mcp/src/agents_remember/application/review_comparison_generation.py:650-665; mcp/src/agents_remember/application/review_comparison_generation.py:586-620 |
| The retention owner whose ref the code release deletes, and the two failure statuses it raises. | `release_retained_code_object`; `retained_object_readable`; `code_object_observation` | mcp/src/agents_remember/worktrees/modules/code_object_retention.py:270-316; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:259-267; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:243-256 |
| **The two typed failures this module raises, with their stated reason for being raised rather than returned.** | `CodeObjectRetentionError`; `ComparisonReclamationError` | mcp/src/agents_remember/errors.py:180-204 |
| **The case that measures the discard: a mismatch refused with both files in place and no record, then recorded digests equal to the frozen ones, then both halves reported `unavailable-history`, then the retry recording `None`.** | `test_discarding_snapshots_records_the_bytes_it_measured_and_refuses_a_mismatch` | mcp/tests/test_knowledge_review_comparison_generation.py:1060-1124 |
| **The case that measures the release: an unavailable-history record, the custody measured before and after reclamation, and a reopen that reports the deletion rather than today's data.** | `test_an_explicit_release_records_unavailable_history_and_is_measured_not_assumed` | mcp/tests/test_knowledge_review_comparison_generation.py:483-550 |
| **The case that refuses to delete a ref that moved.** | `test_a_retention_ref_that_moved_is_never_deleted` | mcp/tests/test_knowledge_review_comparison_generation.py:969-1016 |
| The reopen that consumes these records: the per-channel states and the unavailable-history channel. | `reopen_comparison_generation`; `ComparisonSourceChannel`; `ComparisonKnowledgeChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:196-217; mcp/src/agents_remember/application/review_comparison_reopen.py:96-122; mcp/src/agents_remember/application/review_comparison_reopen.py:124-140 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It runs Git against the repository the
manifest names and unlinks files under the coordination task root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T19:40:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as the **two bounded reclamation paths ICR-R11@v1 requires** ("every new snapshot/pin names its deletion owner and bounded temporary-storage cleanup"). It records the properties a reader has to act on rather than the function list: the unavailable-history record is written **before** the deletion so an interruption leaves the honest ordering, and the code release *withdraws* its record if the retention owner then refuses, so no false record of a deletion that did not happen survives; the ref must still name the recorded commit and the snapshot must still hold the recorded bytes, so a moved ref is left in place and a mismatched snapshot is refused with nothing removed and nothing recorded; the deleted digest is **measured** rather than copied from the manifest, and an already-absent snapshot converges as `None` so a retry of an interrupted discard does not fail; and custody at release is measured *before* the ref disappears, because the record's reader cannot recover that distinction afterwards. Two stated boundaries: the manifest is never deleted (a reopen must be able to say the generation existed), and *when* a comparison may be reclaimed has **no owner in this leaf** — these are explicit acts nothing in the freeze or reopen path calls. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.
