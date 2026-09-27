# mcp/src/agents_remember/application/review_comparison_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_comparison_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:30:43+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a` |
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The read-back: what reopening one durable comparison generation reports, channel by channel.**
`review_comparison_generation` owns the record; this module owns *resolving what it points at*, which is
the separate act the record's own docstring names.

`reopen_comparison_generation` (`:213-234`) resolves a leaf's generation **from the task artifact plane
alone** — no enclosure contract, no worktree, no live process state — and then measures every channel the
record binds against the world it names:

- the two code objects, asked of the repository the record names, **plus the custody the repository shows
  now** rather than the custody recorded at freeze time;
- each retained knowledge snapshot, re-read as a dataset and compared against the exact logical identity
  that was frozen, with a digest read-back beside it;
- each cited owner-produced artifact, re-read and compared against the digest it was cited for;
- **what the task's own closeout and integration recorded for it (ICR-R21@v1)** — the code, memory and
  published-knowledge outputs the task actually delivered, read through that record's own owner, one entry
  per phase that recorded anything and in phase order.

**Every channel answers with its own state and never with one verdict for the generation.** The states
are deliberately distinct because a consumer acts on them differently:

| Channel state | What it says |
| --- | --- |
| `available` | the exact recorded content resolves |
| `not-recorded` / `not-selected` | a typed absence the record *states* — not a failure, and it does not make the generation unavailable |
| `missing` | expected content is not there and nothing records a deletion |
| `corrupt` | the bytes are there and are not the content the record binds |
| `unavailable-history` | the record's own deletion record says this was deleted deliberately |

**The fourth channel is what the task delivered, and it is deliberately not part of the
generation-level state.** `final_output` (`:190`) is a tuple — one entry per phase, in phase order,
whenever the reopen **measured a generation** — rather than an optional single value, because closeout and
integration are separate measurements taken at separate moments and a reader handed only one of them would
have to guess which. Three facts about it are stated rather than implied:

- **a phase that recorded nothing is still an entry**, carrying `not-recorded`, because omitting it would
  make "nothing was recorded" and "no phase was asked about" the same answer;
- **the tuple is empty exactly when the reopen measured no generation at all** — the `absent`, `ambiguous`
  and `manifest-unreadable` states, which ask no phase anything — so an empty tuple is a fact about the
  reopen, never about a phase;
- **a recorded measurement is not an availability requirement**: `_all_resolved` (`:345-356`) decides the
  generation-level state from the source, knowledge and evidence channels alone, so a leaf that closed out
  before a comparison existed — or whose receipt the retention owner removed — still reopens `available`
  with its inputs intact.

The **generation-level** state is separate again (`:184`): `available`, `unavailable`, `absent` (nothing
was published), `ambiguous` (more than one record claims the index asked for — stated rather than
resolved by directory order) and `manifest-unreadable` (a record is there and cannot be read, so nothing
about it is claimed). `unavailable_channels()` (`:199-211`) names exactly which channels did not resolve,
in the order they are reported, so a consumer can keep the channels that *did* resolve instead of
discarding the generation — which is the whole reason the generation-level state is not one boolean.

## Code Commentary

### Logic

**Addressing.** A named `generation_id` goes to `_reopen_named` (`:237-250`), which reports an absent
directory by name with its own next action. An unnamed reopen goes to `_reopen_latest` (`:252-290`),
which takes `read_generation_refs` (readable generations only, ordered by recorded index):
no readable refs but **exactly one** directory → that directory is read anyway, so the record's *own*
reason is reported rather than a summary of it ("which field is wrong" is the only thing an operator can
act on); several unreadable directories → `manifest-unreadable` naming all of them; none at all →
`absent`. A highest index claimed by two different bindings is `_ambiguous` (`:658-679`) with the remedy
the packet's own revision rule uses — name the exact generation id.

**The source channel measures three separate facts.** `_source_channel` (`:359-401`) reports
`baseline_code_tree_id` / `candidate_code_tree_id`, `custody_recorded` (what the manifest stored),
`custody_observed` (what the repository shows **now**, `None` when the repository itself could not be
read — a different fact from a measured `retained`, and never filled with the recorded value), and:

- `pin_present` (`:378-382`) — whether the recorded pin resolves to the commit it recorded, measured now;
- `release_recorded` (`:399`) — whether an explicit release of this generation's pin is on record.

The two are separate because a third fact exists: a comparison frozen again after a release has a live
pin **and** a release on record. `_current_first` (`:402-424`) therefore composes the detail with the
live measurement **first** and the release history after it, because "a detail that led with the release
would read as though the content were gone while the reader is looking straight at it".

**Readability is measured before the deletion record decides anything.** `_source_state` (`:425-460`): a
repository that is not there is `missing`; both objects readable is `available` (whatever a release
record says — a release may have discarded nothing because a branch already held the history);
otherwise the objects that no longer resolve are named, and the state is `unavailable-history` **only
when a deletion record exists for this target** (`_deletion_or_raise`, `:625-630`), else `missing`.
`_resolved_source_detail` (`:461-485`) states which of the two resolved shapes this generation is in —
"no pin was needed, committed history held the tree at freeze time" versus "held under the explicit pin
`<ref>` … which the later release discarded nothing of".

**A knowledge channel is decided by the record's own state before any file is touched.**
`_knowledge_channel` (`:486-520`) returns the recorded `not-recorded` / `not-selected` state (with the
record's own reason) with no identity and no path; a deletion record for that target gives
`unavailable-history` naming the deletion owner and scope; otherwise `_measure_snapshot` (`:521-553`)
reads the file — an absent file with **no** deletion record is `missing`, and its detail says the thing
that keeps the two apart: *"a missing expected dataset is unavailable, not absent history"*. A file that
is not readable as a dataset of this code is `corrupt`; a readable one goes to `_compare_snapshot`
(`:554-587`), which compares the observed `SnapshotIdentity` against the frozen one and reports `corrupt`
naming **both** logical digests when they disagree.

**The evidence channel re-reads and re-digests.** `_evidence_channel` (`:597-640`) resolves the
task-relative reference through `_confined_reference` (`:641-649`) — an absolute path or any `..` part
is `corrupt`, "so it is not a reference this record may resolve" — reads the bytes (`missing` on an
`OSError`) and compares the sha256 against the recorded one, reporting `corrupt` with both digests named
on a mismatch. That is what makes a citation a checkable claim rather than a recorded string.

**The generation-level state is computed from the channels, not guessed.** `_all_resolved` (`:345-356`)
requires the source channel `available`, every knowledge channel in `TYPED_ABSENCE_STATES | {"available"}`
— a typed absence is not an unavailability — and every evidence channel `available`.

### Conventions

`__all__` publishes exactly the three channel dataclasses, the outcome and the one operation. All are
**frozen dataclasses** rather than pydantic models: a reopen's answer is a reading, not a stored wire
shape, and it never gets written back. `_Addressed` (`:91-102`) packages the three loose strings a reopen
is asked for, so the private helpers take one value. `_SIDES: tuple[KnowledgeSide, ...] = ("before",
"after")` (`:342`) is the one place the two halves are enumerated. `_refusal` (`:716-726`) builds every
refusal from the shipped `ReviewRefusal` with the reused `comparison_refused` code. `apsw.Error` is
caught alongside the storage errors in `_observed_snapshot` (`:588-596`), because "this file is not a
database" is a state this channel reports rather than a crash.

### Invariants And Boundaries

- **Nothing here writes.** No file, no ref, no record; it reads bytes and object ids and reports what it
  found.
- **A channel's state is its own.** There is no single verdict that hides which input stopped resolving;
  `unavailable_channels()` is the machine-readable half of that rule.
- **A typed absence never makes a generation unavailable.** `not-recorded` and `not-selected` are
  statements the record made.
- **A missing expected dataset is never reported as absent history.** The distinction is carried in the
  channel's own words, and the two are decided by the presence of a deletion record.
- **Custody is reported twice, and neither value is a substitute for the other**: `custody_recorded` is
  history, `custody_observed` is a measurement now, and `None` is "the repository could not be read"
  rather than a guess.
- **The live pin's measurement leads the release history** in the composed detail.
- **Nothing is resolved by directory order.** An ambiguous index is a state with a remedy.
- **An unreadable record yields `manifest-unreadable` and no claim about the generation** — not an empty
  generation and not a partial one.
- **Boundary: the absolute `task_root` / `contract_path` / `code_repository_root` a record stores mean a
  relocated coordination root degrades durability to the knowledge and evidence channels.** The retained
  snapshot bytes and the cited task artifacts travel with the tree, while the source channel resolves
  against the recorded absolute repository path and reports `missing` when that path is not there. This
  is a **stated boundary owned by ICR-R12 and ICR-R13**, which consume `reopen_comparison_generation` and
  own historical resolution — not a defect of this leaf. A consuming leaf that needs relocation-stable
  resolution must record a relative repository identity or add a resolution input; either is compatible
  with this record, whose fields are already identities plus one path.
- **Boundary: this module's production consumer is the closed-leaf review route, and its per-channel
  states still have no rendering surface.** The reopen is reached from
  `application/review_committed_leaf.py`, so the states *are* read in production (ICR-R12/R13 landed that
  route); what remains owned elsewhere is mapping the per-channel states into an HTTP route, a dashboard
  pane or a CLI entry.
- **Boundary: the fourth channel is a measurement, not an availability requirement.** A generation whose
  task recorded no receipt still reopens `available`; `_all_resolved` (`:345-356`) deliberately decides
  the generation-level state from the source, knowledge and evidence channels alone, so "the task
  recorded nothing for this generation" can never be reported as "the comparison cannot be reopened".

### Todos

None recorded.

### The Fifth Channel: What The Leaf's Own Syncs Measured, Checked Against The Generation (ICR-R22@v1)

`260921-ICR-L22` (`ICR-R22@v1`) adds a **fifth channel** to the outcome, and it is the second one a
task's own transactions write. `ComparisonReopen.sync_rebinding` (`:202`) carries what this leaf's
managed syncs measured against this generation. The docstring states its two shapes of absence
(`:182-189`): it is `None` exactly when the reopen measured no generation at all — the same three
states that leave `final_output` empty — and `not-recorded` rather than `None` when a generation *was*
measured and no sync has reported against it, because omitting it would make "no managed sync has run"
and "a sync ran and recorded nothing" the same answer. It is one value rather than a tuple because a
rebinding measures one generation and a later sync replaces it — one file per (leaf, generation) — while
the generations themselves are retained history, so a reader that wants the earlier measurements reads
the earlier generations.

**It is read at the location and then checked against the generation itself.** `_measured_rebinding`
(`:367-390`) reads the record with `read_review_sync_rebinding` and keeps it only when
`rebinding_names_the_generation(read, manifest)` (`:379`) returns it. A record whose identity fields
were forged is *internally consistent* — the record's own validator re-derives every verdict from the
fields it carries, and comparing two fabricated identities is still a comparison — so reading the
location alone would let such a record read as a measurement of **this** generation. A record that does
not describe this generation is replaced by the honest answer (`:381-390`): `not-recorded`,
`rebinding=None`, and a detail naming the location and the generation id, because nothing was measured
here whatever is at the location.

**The channel is a measurement, not an availability requirement, and the call site says so.** It is
built in `_read_and_measure` (`:360`) beside the fourth channel, so a reader resolving a recorded
comparison learns whether the pair it bound is still the pair the task holds without re-deriving that
from a live worktree it may no longer have. `_all_resolved` (`:393-404`) and `unavailable_channels()`
(`:210-225`) are unchanged: the generation-level state and the list of channels that did not resolve
still follow from the source, knowledge and evidence channels alone, so "no sync has reported" can
never be reported as "the comparison cannot be reopened".

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the record it
resolves, and in the cases that inject damage per channel. Three details a reader should carry:
`custody_observed` is a **three-valued** measurement (`retained` / `committed-history` / `absent`) taken
now, while `custody_recorded` is history; a missing dataset and a deliberately deleted one are told apart
by the **presence of a deletion record**, not by the file's absence; and the unresolved absolute
repository path is a stated relocation boundary owned by ICR-R12/R13.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the four channels, the six channel states and the five generation states, with the fourth one named as what the task delivered (ICR-R21@v1).** | `reopen_comparison_generation` | mcp/src/agents_remember/application/review_comparison_reopen.py:1-35 |
| The published surface and the value that packages the three addressing strings. | `__all__`; `_Addressed` | mcp/src/agents_remember/application/review_comparison_reopen.py:82-102 |
| **The source channel's five facts, including `pin_present` (measured now) beside `release_recorded` (history) and the three-valued `custody_observed`.** | `ComparisonSourceChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:104-129 |
| The knowledge channel's six states and its optional identity and path. | `ComparisonKnowledgeChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:132-147 |
| The evidence channel: one cited artifact re-read against its recorded digest. | `ComparisonEvidenceChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:150-157 |
| **The outcome: one state per channel, the generation-level state, and `unavailable_channels()` naming exactly what did not resolve.** | `ComparisonReopen`; `available`; `unavailable_channels` | mcp/src/agents_remember/application/review_comparison_reopen.py:160-211 |
| **The fourth channel: what the task's own closeout and integration recorded for this generation, one entry per phase in phase order (ICR-R21@v1).** | `final_output`; `FinalOutputReceiptRead` | mcp/src/agents_remember/application/review_comparison_reopen.py:186-201; mcp/src/agents_remember/application/review_final_output_receipt.py:160-176 |
| **The operation: addressed from the task artifact plane alone, with a named generation or the highest recorded index.** | `reopen_comparison_generation` | mcp/src/agents_remember/application/review_comparison_reopen.py:213-234 |
| **The named reopen, and the latest-index reopen with its three honest answers (one unreadable record read anyway, several unreadable records, none at all).** | `_reopen_named`; `_reopen_latest` | mcp/src/agents_remember/application/review_comparison_reopen.py:237-290 |
| **The read-and-measure pass that builds every channel, including the fourth one read in the one place a generation is resolved, and computes the generation-level state from the channels that were expected to resolve.** | `_read_and_measure`; `_SIDES`; `_all_resolved` | mcp/src/agents_remember/application/review_comparison_reopen.py:293-356 |
| **The source channel's measurement: both objects, the pin, the current custody, and the composed detail that leads with the live fact.** | `_source_channel`; `_current_first` | mcp/src/agents_remember/application/review_comparison_reopen.py:359-446 |
| **The state order that matters: readability first, the deletion record only for objects that are really gone.** | `_source_state`; `_resolved_source_detail` | mcp/src/agents_remember/application/review_comparison_reopen.py:425-491 |
| **A knowledge half: the recorded typed absence, the deletion record, then the file — with "a missing expected dataset is unavailable, not absent history" stated in the code.** | `_knowledge_channel`; `_measure_snapshot`; `_compare_snapshot`; `_observed_snapshot` | mcp/src/agents_remember/application/review_comparison_reopen.py:486-599 |
| **The evidence read-back and its task-root confinement.** | `_evidence_channel`; `_confined_reference` | mcp/src/agents_remember/application/review_comparison_reopen.py:597-650 |
| The three non-measured answers: ambiguous, unreadable, absent — each with its own remedy. | `_deletion_or_raise`; `_ambiguous`; `_unreadable`; `_absent`; `_refusal` | mcp/src/agents_remember/application/review_comparison_reopen.py:698-703; mcp/src/agents_remember/application/review_comparison_reopen.py:706-726; mcp/src/agents_remember/application/review_comparison_reopen.py:729-743; mcp/src/agents_remember/application/review_comparison_reopen.py:746-761; mcp/src/agents_remember/application/review_comparison_reopen.py:764-772 |
| The record, its discovery pass and its deletion record: the three things this module reads and never writes. | `read_manifest`; `read_generation_refs`; `read_history_deletion`; `task_root_for_review` | mcp/src/agents_remember/application/review_comparison_generation.py:615-649; mcp/src/agents_remember/application/review_comparison_generation.py:725-753; mcp/src/agents_remember/application/review_comparison_generation.py:652-676; mcp/src/agents_remember/application/review_comparison_generation.py:564-572 |
| **The three-valued observation this module reports, and the pin's own readability question.** | `code_object_observation`; `CodeObjectObservation`; `object_readable`; `retained_object_readable` | mcp/src/agents_remember/worktrees/modules/code_object_retention.py:243-267; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:79-84; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:165-175; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:259-267 |
| The dataset identity reader a knowledge channel compares against the frozen identity. | `dataset_identity` | mcp/src/agents_remember/memory/knowledge/logical.py:153-176 |
| **The cases that measure damage per channel: injected missing and corrupt inputs, and the release path's `custody_observed="absent"` beside `unavailable-history`.** | `test_a_missing_or_damaged_retained_input_is_reported_per_channel`; `test_an_explicit_release_records_unavailable_history_and_is_measured_not_assumed` | mcp/tests/test_knowledge_review_comparison_generation.py:558-600; mcp/tests/test_knowledge_review_comparison_generation.py:485-552 |
| **The case that reports the live pin before the release history after a re-freeze.** | `test_a_frozen_again_comparison_reports_its_live_pin_before_the_release_history` | mcp/tests/test_knowledge_review_comparison_generation.py:1129-1172 |
| **The case that reopens in a real child process after the worktree group is removed and Git objects are reclaimed.** | `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation`; `_reopen_in_a_new_process` | mcp/tests/test_knowledge_review_comparison_generation.py:279-315; mcp/tests/test_knowledge_review_comparison_generation.py:336-387 |
| **The fifth channel: what this leaf's own managed syncs measured against this generation (`ICR-R22@v1`), one value whose absence is stated in two shapes, read at the location and then checked against the generation itself — so a forged-but-internally-consistent record reads back `not-recorded` with the reason rather than as a measurement of this generation.** | `sync_rebinding`; `_measured_rebinding`; `rebinding_names_the_generation` | mcp/src/agents_remember/application/review_comparison_reopen.py:182-202; mcp/src/agents_remember/application/review_comparison_reopen.py:367-390; mcp/src/agents_remember/application/review_sync_rebinding.py:441-476 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a repository path the record names
and files under the coordination task root; the relocation boundary that follows from the recorded
absolute path is stated above and owned by ICR-R12/R13.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 3 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 1 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_deletion_or_raise`; `_ambiguous`; `_unreadable`; `_absent`; `_refusal` repointed to mcp/src/agents_remember/application/review_comparison_reopen.py:698-703; mcp/src/agents_remember/application/review_comparison_reopen.py:706-726; mcp/src/agents_remember/application/review_comparison_reopen.py:729-743; mcp/src/agents_remember/application/review_comparison_reopen.py:746-761; mcp/src/agents_remember/application/review_comparison_reopen.py:764-772. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **the read-back gained a fifth channel — what the leaf's own managed syncs measured against this generation (`ICR-R22@v1`).** `ComparisonReopen.sync_rebinding` (`:202`) is `ReviewSyncRebindingRead | None`, populated by `_measured_rebinding` (`:367-390`) in the one place a generation is resolved and measured. The two-part read is the substance rather than a range refresh: the location is read first and then checked against the generation by `rebinding_names_the_generation` (`:379`), because a record whose identity fields were forged is internally consistent and would otherwise read as a measurement of *this* generation; a record that does not describe it reads back `not-recorded` with the reason (`:381-390`). The new body section also records the channel's two shapes of absence and the boundary it keeps — a measurement is not an availability requirement, and `_all_resolved` (`:393-404`) and `unavailable_channels()` (`:210-225`) are untouched — and the module is 730 → 778 lines. **Citation accounting:** one row was **added** for this leaf's construct (`review_comparison_reopen.py:182-202` and `:367-390`, `application/review_sync_rebinding.py:441-476`); no existing row, anchor or range on this card was moved, re-pointed, re-worded or dropped, because the curator's citation pass owns that work row by row. **Stamp accounting:** the header's verification pair is left exactly as recorded — `3103e1142a3ded8a843c3e5bbefca14861ba4a58` with its own date — and it is **not** advanced here: the fifth channel exists only in this leaf's uncommitted working tree, whose recorded base is `e605822eb3bf83bf63a45963c5f51d5fc28859ee`, so the header's pair still names the last real commit the reading was taken against (this card's own L21 entry) and the governed closeout owns the real stamp.
- 2026-09-23T09:25:00+02:00 — 260921-ICR-L21 curator (uncommitted change set on `ar/260921-icr-l21`, base `972b44cc07b307929535fe7974d6a30d53c9c4f1`): **the read-back gained a fourth channel, and this card was re-read against the new bytes rather than annotated.** `ComparisonReopen.final_output` now carries what the task's own closeout and integration recorded for the generation (ICR-R21@v1), one entry per phase in phase order, read through `read_final_output_receipts` — so the recorded comparison a reader opens identifies the code, memory and published-knowledge outputs the task *delivered* beside the inputs it was *compared against*, which is that requirement's own sentence. Three content-level facts are recorded rather than a range refresh: the tuple is deliberate (closeout and integration are separate measurements taken at separate moments, and a reader handed one would have to guess which); **a recorded measurement is not an availability requirement** — `_all_resolved` still decides the generation-level state from the source, knowledge and evidence channels alone, so a leaf that closed out before a comparison existed still reopens `available`; and this module is no longer a read path with no consumer, because the closed-leaf review route reaches it. Every cited range on this card was recomputed against the new bytes (the module moved from 699 to 730 lines), and the **two inline ranges that are not table rows** — the addressing pair and `unavailable_channels()` — were corrected with them. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` were advanced to `972b44cc07b307929535fe7974d6a30d53c9c4f1` (this leaf's recorded base, which is the commit the current production line actually carries) with the date of the worker report's own reading, because every construct cited here exists only in this leaf's uncommitted working tree; the header records the honest basis and no commit that does not contain the code is named.
- 2026-09-23T09:20:00+02:00 — 260921-ICR-L21 curator, **second pass on the round-2 (`pass-with-findings`) bytes: this card quoted the ``final_output`` docstring's earlier, less exact semantics and now matches the corrected text.** The paragraph at `:168-175` was corrected in the candidate (the round-2 verifier's F5) to say that an entry exists **per phase whenever the reopen measured a generation** — a phase that recorded nothing is still an entry carrying `not-recorded` — and that the tuple is empty **exactly when the reopen measured no generation at all** (`absent`, `ambiguous`, `manifest-unreadable`, which ask no phase anything). The card's prose said an empty tuple meant "neither phase recorded a receipt", which named the common case but not the exact rule; it now carries all three facts (a recorded-nothing phase is still an entry; the tuple is empty only for the three no-generation states; and a recorded measurement is not an availability requirement). This is the curator's own read of the corrected bytes, not a quotation of the verifier's finding. The correction is line-neutral — the module is 730 lines before and after and the paragraph occupies `:168-175` in both — so **no cited range on this card moved**, and the fourth-channel row's range (`:186-190`) is unaffected. No new gate finding is expected from it; the citation range covering the corrected paragraph is already cited.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **one inherited citation defect repaired — it is not this leaf's own.** The row carrying the module's own statement of the three channels, the six channel states and the five generation states cited `review_comparison_reopen.py:1-32` with an Anchor cell reading `*(module docstring)*`, which is italic prose rather than an anchor: nothing in the row said what those lines were supposed to contain. The defect predates this leaf (the row was written by 260921-ICR-L11) and is repaired here only because this leaf's curation pass owns the gate finding. The Anchor cell now names the real identifier `reopen_comparison_generation`, which occurs **literally inside the cited range** at line 4 — the operation the docstring's channel list describes — so the claim is checkable. The Finding wording, the cited range and every other row are unchanged; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T19:45:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as **the read-back half of ICR-R11@v1** — what reopening a durable comparison generation reports. It records what a consumer has to act on: every channel answers with its own state rather than one verdict, and `unavailable_channels()` names exactly which input stopped resolving so a consumer can keep the rest; a typed absence (`not-recorded` / `not-selected`) is a statement and never an unavailability; a **missing expected dataset is not absent history** — the two are told apart by the presence of a deletion record, not by a file's absence; custody is reported twice and neither substitutes for the other (`custody_recorded` is history, `custody_observed` is a three-valued measurement now, and `None` means the repository could not be read); and the live pin measurement leads the release history in the composed detail, because a re-frozen comparison legitimately has both. Two stated boundaries are carried as boundaries and not defects: an **absolute** recorded repository path means a relocated coordination root degrades the source channel to `missing` while the knowledge and evidence channels travel with the tree — ruled the boundary of ICR-R12/R13, which own historical resolution; and this read path has **no consumer yet** (no route, pane or CLI entry), which ICR-R12/R13 own. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate; what was actually read is this leaf's uncommitted working tree, and closeout owns the real stamp once the code commit exists.
