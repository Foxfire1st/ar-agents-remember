# mcp/src/agents_remember/application/review_comparison_reopen.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Reopens one immutable comparison generation and reports its current source custody, historical channel availability and retained evidence.

## Code Commentary

Source channels measure whether the exact recorded objects and pins resolve now; recorded release history is a separate fact. `_knowledge_channel` does not open a historical canonical dataset: an explicit deletion is unavailable-history, otherwise the historical dataset is legacy-unavailable. Evidence channels independently read their confined retained references and hashes. No current candidate substitutes for a missing historical object. The former unavailable_channels helper and dataset measurement promise are retired. Snapshot reclamation ordering is owned by review_comparison_reclamation, not inferred from this reader.

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

**The evidence channel re-reads and re-digests.** `_evidence_channel` (`:597-640`) resolves the
task-relative reference through `_confined_reference` (`:641-649`) — an absolute path or any `..` part
is `corrupt`, "so it is not a reference this record may resolve" — reads the bytes (`missing` on an
`OSError`) and compares the sha256 against the recorded one, reporting `corrupt` with both digests named
on a mismatch. That is what makes a citation a checkable claim rather than a recorded string.

**The generation-level state is computed from the channels, not guessed.** `_all_resolved` (`:345-356`)
requires the source channel `available`, every knowledge channel in `TYPED_ABSENCE_STATES | {"available"}`
— a typed absence is not an unavailability — and every evidence channel `available`.

### Invariants And Boundaries

- **Nothing here writes.** No file, no ref, no record; it reads bytes and object ids and reports what it
  found.
- **A typed absence never makes a generation unavailable.** `not-recorded` and `not-selected` are
  statements the record made.
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

## Evidence

### Repo-Internal References

- `reopen_comparison_generation` owns the current boundary described above. [23]
- `_source_channel` owns the current boundary described above. [24]
- `_knowledge_channel` owns the current boundary described above. [25]
- `_evidence_channel` owns the current boundary described above. [26]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the record it
resolves, and in the cases that inject damage per channel. Three details a reader should carry:
`custody_observed` is a **three-valued** measurement (`retained` / `committed-history` / `absent`) taken
now, while `custody_recorded` is history; a missing dataset and a deliberately deleted one are told apart
by the **presence of a deletion record**, not by the file's absence; and the unresolved absolute
repository path is a stated relocation boundary owned by ICR-R12/R13.

- The published surface and the value that packages the three addressing strings. [27]
- **The source channel's five facts, including `pin_present` (measured now) beside `release_recorded` (history) and the three-valued `custody_observed`.** [28]
- The evidence channel: one cited artifact re-read against its recorded digest. [29]
- **The fourth channel: what the task's own closeout and integration recorded for this generation, one entry per phase in phase order (ICR-R21@v1).** [30]
- **The operation: addressed from the task artifact plane alone, with a named generation or the highest recorded index.** [31]
- **The named reopen, and the latest-index reopen with its three honest answers (one unreadable record read anyway, several unreadable records, none at all).** [32]
- **The read-and-measure pass that builds every channel, including the fourth one read in the one place a generation is resolved, and computes the generation-level state from the channels that were expected to resolve.** [33]
- **The source channel's measurement: both objects, the pin, the current custody, and the composed detail that leads with the live fact.** [34]
- **The state order that matters: readability first, the deletion record only for objects that are really gone.** [35]
- **The evidence read-back and its task-root confinement.** [36]
- The three non-measured answers: ambiguous, unreadable, absent — each with its own remedy. [37]
- The record, its discovery pass and its deletion record: the three things this module reads and never writes. [38]
- **The three-valued observation this module reports, and the pin's own readability question.** [39]
- **The fifth channel: what this leaf's own managed syncs measured against this generation (`ICR-R22@v1`), one value whose absence is stated in two shapes, read at the location and then checked against the generation itself — so a forged-but-internally-consistent record reads back `not-recorded` with the reason rather than as a measurement of this generation.** [40]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a repository path the record names
and files under the coordination task root; the relocation boundary that follows from the recorded
absolute path is stated above and owned by ICR-R12/R13.

No meaningful cross-repo references found.
