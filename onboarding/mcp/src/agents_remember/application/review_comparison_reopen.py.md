# mcp/src/agents_remember/application/review_comparison_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_comparison_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l11`, uncommitted; base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75` |
| lastVerifiedCommitHash | `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` |
| lastVerifiedCommitDate | 2026-09-22T00:48:09+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The read-back: what reopening one durable comparison generation reports, channel by channel.**
`review_comparison_generation` owns the record; this module owns *resolving what it points at*, which is
the separate act the record's own docstring names.

`reopen_comparison_generation` (`:196-217`) resolves a leaf's generation **from the task artifact plane
alone** — no enclosure contract, no worktree, no live process state — and then measures every channel the
record binds against the world it names:

- the two code objects, asked of the repository the record names, **plus the custody the repository shows
  now** rather than the custody recorded at freeze time;
- each retained knowledge snapshot, re-read as a dataset and compared against the exact logical identity
  that was frozen, with a digest read-back beside it;
- each cited owner-produced artifact, re-read and compared against the digest it was cited for.

**Every channel answers with its own state and never with one verdict for the generation.** The states
are deliberately distinct because a consumer acts on them differently:

| Channel state | What it says |
| --- | --- |
| `available` | the exact recorded content resolves |
| `not-recorded` / `not-selected` | a typed absence the record *states* — not a failure, and it does not make the generation unavailable |
| `missing` | expected content is not there and nothing records a deletion |
| `corrupt` | the bytes are there and are not the content the record binds |
| `unavailable-history` | the record's own deletion record says this was deleted deliberately |

The **generation-level** state is separate again (`:162`): `available`, `unavailable`, `absent` (nothing
was published), `ambiguous` (more than one record claims the index asked for — stated rather than
resolved by directory order) and `manifest-unreadable` (a record is there and cannot be read, so nothing
about it is claimed). `unavailable_channels()` (`:178-193`) names exactly which channels did not resolve,
in the order they are reported, so a consumer can keep the channels that *did* resolve instead of
discarding the generation — which is the whole reason the generation-level state is not one boolean.

## Code Commentary

### Logic

**Addressing.** A named `generation_id` goes to `_reopen_named` (`:220-232`), which reports an absent
directory by name with its own next action. An unnamed reopen goes to `_reopen_latest` (`:235-273`),
which takes `read_generation_refs` (readable generations only, ordered by recorded index):
no readable refs but **exactly one** directory → that directory is read anyway, so the record's *own*
reason is reported rather than a summary of it ("which field is wrong" is the only thing an operator can
act on); several unreadable directories → `manifest-unreadable` naming all of them; none at all →
`absent`. A highest index claimed by two different bindings is `_ambiguous` (`:633-653`) with the remedy
the packet's own revision rule uses — name the exact generation id.

**The source channel measures three separate facts.** `_source_channel` (`:334-374`) reports
`baseline_code_tree_id` / `candidate_code_tree_id`, `custody_recorded` (what the manifest stored),
`custody_observed` (what the repository shows **now**, `None` when the repository itself could not be
read — a different fact from a measured `retained`, and never filled with the recorded value), and:

- `pin_present` (`:353-357`) — whether the recorded pin resolves to the commit it recorded, measured now;
- `release_recorded` (`:372`) — whether an explicit release of this generation's pin is on record.

The two are separate because a third fact exists: a comparison frozen again after a release has a live
pin **and** a release on record. `_current_first` (`:377-397`) therefore composes the detail with the
live measurement **first** and the release history after it, because "a detail that led with the release
would read as though the content were gone while the reader is looking straight at it".

**Readability is measured before the deletion record decides anything.** `_source_state` (`:400-433`): a
repository that is not there is `missing`; both objects readable is `available` (whatever a release
record says — a release may have discarded nothing because a branch already held the history);
otherwise the objects that no longer resolve are named, and the state is `unavailable-history` **only
when a deletion record exists for this target** (`_deletion_or_raise`, `:625-630`), else `missing`.
`_resolved_source_detail` (`:436-458`) states which of the two resolved shapes this generation is in —
"no pin was needed, committed history held the tree at freeze time" versus "held under the explicit pin
`<ref>` … which the later release discarded nothing of".

**A knowledge channel is decided by the record's own state before any file is touched.**
`_knowledge_channel` (`:461-493`) returns the recorded `not-recorded` / `not-selected` state (with the
record's own reason) with no identity and no path; a deletion record for that target gives
`unavailable-history` naming the deletion owner and scope; otherwise `_measure_snapshot` (`:496-526`)
reads the file — an absent file with **no** deletion record is `missing`, and its detail says the thing
that keeps the two apart: *"a missing expected dataset is unavailable, not absent history"*. A file that
is not readable as a dataset of this code is `corrupt`; a readable one goes to `_compare_snapshot`
(`:529-560`), which compares the observed `SnapshotIdentity` against the frozen one and reports `corrupt`
naming **both** logical digests when they disagree.

**The evidence channel re-reads and re-digests.** `_evidence_channel` (`:572-613`) resolves the
task-relative reference through `_confined_reference` (`:616-622`) — an absolute path or any `..` part
is `corrupt`, "so it is not a reference this record may resolve" — reads the bytes (`missing` on an
`OSError`) and compares the sha256 against the recorded one, reporting `corrupt` with both digests named
on a mismatch. That is what makes a citation a checkable claim rather than a recorded string.

**The generation-level state is computed from the channels, not guessed.** `_all_resolved` (`:320-331`)
requires the source channel `available`, every knowledge channel in `TYPED_ABSENCE_STATES | {"available"}`
— a typed absence is not an unavailability — and every evidence channel `available`.

### Conventions

`__all__` publishes exactly the three channel dataclasses, the outcome and the one operation. All are
**frozen dataclasses** rather than pydantic models: a reopen's answer is a reading, not a stored wire
shape, and it never gets written back. `_Addressed` (`:84-90`) packages the three loose strings a reopen
is asked for, so the private helpers take one value. `_SIDES: tuple[KnowledgeSide, ...] = ("before",
"after")` (`:317`) is the one place the two halves are enumerated. `_refusal` (`:691-699`) builds every
refusal from the shipped `ReviewRefusal` with the reused `comparison_refused` code. `apsw.Error` is
caught alongside the storage errors in `_observed_snapshot` (`:563-569`), because "this file is not a
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
- **Boundary: this module is a read path with no consumer yet.** No HTTP route, no dashboard pane and no
  CLI entry calls it in this leaf; ICR-R12/R13 own mapping the per-channel states into a surface.

### Todos

None recorded.

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
| The module's own statement of the three channels, the six channel states and the five generation states. | `reopen_comparison_generation` | mcp/src/agents_remember/application/review_comparison_reopen.py:1-32 |
| The published surface and the value that packages the three addressing strings. | `__all__`; `_Addressed` | mcp/src/agents_remember/application/review_comparison_reopen.py:75-90 |
| **The source channel's five facts, including `pin_present` (measured now) beside `release_recorded` (history) and the three-valued `custody_observed`.** | `ComparisonSourceChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:96-122 |
| The knowledge channel's six states and its optional identity and path. | `ComparisonKnowledgeChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:124-140 |
| The evidence channel: one cited artifact re-read against its recorded digest. | `ComparisonEvidenceChannel` | mcp/src/agents_remember/application/review_comparison_reopen.py:142-150 |
| **The outcome: one state per channel, the generation-level state, and `unavailable_channels()` naming exactly what did not resolve.** | `ComparisonReopen`; `available`; `unavailable_channels` | mcp/src/agents_remember/application/review_comparison_reopen.py:152-193 |
| **The operation: addressed from the task artifact plane alone, with a named generation or the highest recorded index.** | `reopen_comparison_generation` | mcp/src/agents_remember/application/review_comparison_reopen.py:196-217 |
| **The named reopen, and the latest-index reopen with its three honest answers (one unreadable record read anyway, several unreadable records, none at all).** | `_reopen_named`; `_reopen_latest` | mcp/src/agents_remember/application/review_comparison_reopen.py:220-273 |
| **The read-and-measure pass that builds all three channels and computes the generation-level state.** | `_read_and_measure`; `_SIDES`; `_all_resolved` | mcp/src/agents_remember/application/review_comparison_reopen.py:276-331 |
| **The source channel's measurement: both objects, the pin, the current custody, and the composed detail that leads with the live fact.** | `_source_channel`; `_current_first` | mcp/src/agents_remember/application/review_comparison_reopen.py:334-397 |
| **The state order that matters: readability first, the deletion record only for objects that are really gone.** | `_source_state`; `_resolved_source_detail` | mcp/src/agents_remember/application/review_comparison_reopen.py:400-458 |
| **A knowledge half: the recorded typed absence, the deletion record, then the file — with "a missing expected dataset is unavailable, not absent history" stated in the code.** | `_knowledge_channel`; `_measure_snapshot`; `_compare_snapshot`; `_observed_snapshot` | mcp/src/agents_remember/application/review_comparison_reopen.py:461-569 |
| **The evidence read-back and its task-root confinement.** | `_evidence_channel`; `_confined_reference` | mcp/src/agents_remember/application/review_comparison_reopen.py:572-622 |
| The three non-measured answers: ambiguous, unreadable, absent — each with its own remedy. | `_deletion_or_raise`; `_ambiguous`; `_unreadable`; `_absent`; `_refusal` | mcp/src/agents_remember/application/review_comparison_reopen.py:625-699 |
| The record, its discovery pass and its deletion record: the three things this module reads and never writes. | `read_manifest`; `read_generation_refs`; `read_history_deletion`; `task_root_for_review` | mcp/src/agents_remember/application/review_comparison_generation.py:586-620; mcp/src/agents_remember/application/review_comparison_generation.py:696-724; mcp/src/agents_remember/application/review_comparison_generation.py:623-647; mcp/src/agents_remember/application/review_comparison_generation.py:535-543 |
| **The three-valued observation this module reports, and the pin's own readability question.** | `code_object_observation`; `CodeObjectObservation`; `object_readable`; `retained_object_readable` | mcp/src/agents_remember/worktrees/modules/code_object_retention.py:243-267; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:79-84; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:165-175; mcp/src/agents_remember/worktrees/modules/code_object_retention.py:259-267 |
| The dataset identity reader a knowledge channel compares against the frozen identity. | `dataset_identity` | mcp/src/agents_remember/memory/knowledge/logical.py:153-176 |
| **The cases that measure damage per channel: injected missing and corrupt inputs, and the release path's `custody_observed="absent"` beside `unavailable-history`.** | `test_a_missing_or_damaged_retained_input_is_reported_per_channel`; `test_an_explicit_release_records_unavailable_history_and_is_measured_not_assumed` | mcp/tests/test_knowledge_review_comparison_generation.py:556-598; mcp/tests/test_knowledge_review_comparison_generation.py:483-550 |
| **The case that reports the live pin before the release history after a re-freeze.** | `test_a_frozen_again_comparison_reports_its_live_pin_before_the_release_history` | mcp/tests/test_knowledge_review_comparison_generation.py:1127-1170 |
| **The case that reopens in a real child process after the worktree group is removed and Git objects are reclaimed.** | `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation`; `_reopen_in_a_new_process` | mcp/tests/test_knowledge_review_comparison_generation.py:336-387; mcp/tests/test_knowledge_review_comparison_generation.py:279-315 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a repository path the record names
and files under the coordination task root; the relocation boundary that follows from the recorded
absolute path is stated above and owned by ICR-R12/R13.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **one inherited citation defect repaired — it is not this leaf's own.** The row carrying the module's own statement of the three channels, the six channel states and the five generation states cited `review_comparison_reopen.py:1-32` with an Anchor cell reading `*(module docstring)*`, which is italic prose rather than an anchor: nothing in the row said what those lines were supposed to contain. The defect predates this leaf (the row was written by 260921-ICR-L11) and is repaired here only because this leaf's curation pass owns the gate finding. The Anchor cell now names the real identifier `reopen_comparison_generation`, which occurs **literally inside the cited range** at line 4 — the operation the docstring's channel list describes — so the claim is checkable. The Finding wording, the cited range and every other row are unchanged; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T19:45:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as **the read-back half of ICR-R11@v1** — what reopening a durable comparison generation reports. It records what a consumer has to act on: every channel answers with its own state rather than one verdict, and `unavailable_channels()` names exactly which input stopped resolving so a consumer can keep the rest; a typed absence (`not-recorded` / `not-selected`) is a statement and never an unavailability; a **missing expected dataset is not absent history** — the two are told apart by the presence of a deletion record, not by a file's absence; custody is reported twice and neither substitutes for the other (`custody_recorded` is history, `custody_observed` is a three-valued measurement now, and `None` means the repository could not be read); and the live pin measurement leads the release history in the composed detail, because a re-frozen comparison legitimately has both. Two stated boundaries are carried as boundaries and not defects: an **absolute** recorded repository path means a relocated coordination root degrades the source channel to `missing` while the knowledge and evidence channels travel with the tree — ruled the boundary of ICR-R12/R13, which own historical resolution; and this read path has **no consumer yet** (no route, pane or CLI entry), which ICR-R12/R13 own. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.
