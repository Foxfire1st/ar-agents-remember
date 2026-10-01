# mcp/src/agents_remember/application/knowledge_bootstrap_staging.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**A bootstrap's temporary staging: the retained progress record and the bounded cleanup owner
(ICR-R29@v1).** An interrupted bootstrap is the case this module exists for. The candidate database
and the allocation journal already survive an interruption — they are the shipped candidate owner's
files, written into a directory this bootstrap names — and what was missing is the *third* fact a
resume needs: which of the entries the hand-off list carried have actually reached the published
dataset, and which are still owed.

**The record is a projection, never a store.** Every field is derived from three things a run already
has or can read: the run's own report (the batch's outcome), the candidate's allocation journal (which
identities the operation holds), and a read of the **published destination** through the ordinary read
route's owner. Nothing here decides what is true; the dataset does.

**The retained file is read for two different reasons, and the fix round added the second.**
`read_progress` still answers the re-observation question — a record for another scope or another
destination is `moved` rather than stale, which is the explicit reconciliation condition instead of a
silent continuation — but it also **reconstructs the record it read** (`_progress_from_record`) so a
later run can carry forward the work that record left owed. That carry is a re-observation and never a
copy: each owed entry's state is re-derived against the *current* run's own store read, so an entry the
dataset has since received stops being owed, one whose absence this read establishes is still owed, and
one this read could not decide stays `unmeasured`.

**Cleanup has one owner and one guard, because it is the one irreversible act on this path.** The
packet's own non-conforming example is "bootstrap writes an unbound scratch SQLite file, loses it
during cleanup". `discard_bootstrap_staging` (`:327-388`) therefore removes the staging root only when
a **read** established one of exactly two things, and refuses by name in every other state, leaving
the bytes exactly as they are.

## Code Commentary

### Logic

**The four store states are four distinct facts and are never collapsed** (`:81-81`).
`EntryStoreState` is the `Literal["stored", "absent", "unmeasured", "not-attempted"]`: `stored` and
`absent` are measurements, `unmeasured` is a read this run could not make, and `not-attempted` is the
entry never having reached a write attempt. The vocabulary was **five** values while the module was
being written — `not-allocated` was declared and never produced by any path — and the fix round removed
it; a record carrying a `storeState` this code does not know is now reconstructed as `unmeasured`
(`:328-330`), because the honest reading of a state the reader cannot interpret is that absence was not
established, not that nothing is owed.

**The record is written by any committed run, including one whose batch wrote nothing** (`:221-226`).
Every field in it is a read of the store and of the run's own outcome, so a committed run that wrote
nothing still has something true to retain — the owed work it re-derived — and leaving the previous
record standing is how a manifest goes stale exactly when the candidate binding moved. A planning run
still writes nothing at all.

**One entry's row records the run's answer *beside* the store's** (`:90-117`). `EntryProgress.outcome`
is the operation's statement about the batch (`committed`/`refused`/`skipped`) and `store_state` is the
independent read of the published destination. The docstring states why both are kept: a run whose
report and whose store disagree is a reconciliation condition and not a success, and a record that kept
only one of them could not express that at all.

**`BootstrapProgress` carries `remaining` and `unmeasured` as two fields, not one longer list**
(`:120-183`). `remaining` is the named remaining-work manifest; `unmeasured` is the separate list whose
absence the run could **not** establish. The docstring gives the reason: a measured absence and an
unread location are different facts, and merging them would let a truncated walk manufacture remaining
work. `remaining_basis` states how both lists were derived and what the read could not reach, and
`as_record` (`:152-183`) is the exact JSON object the record stores — camel-cased keys, every path in
its posix spelling, `destinationIdentity` as `null` rather than omitted when there is none.

**Retention has four states, because three different acts are called for** (`:186-200`). `retained` is
a record for this exact operation; `moved` is a record for another operation or another destination —
the re-observation condition; `unreadable` is a file whose bytes are not this schema at all; `absent`
is no file. `read_progress` (`:242-299`) decides between them by reading, and the docstring is explicit
that none of the three is ever reported as "no progress", which would be a measurement the function did
not make.

**The write is atomic and refuses the wrong staging root** (`:302-324`). One private `.writing` file
then a `replace`, so an interruption leaves either the previous record or this one and never a
half-written file a later resume would read as truncated. `BootstrapProgressConflict` is **raised, not
returned**: the docstring states that a caller which reached here with the wrong staging root has a
defect, and a refusal value would let it continue and publish a manifest over another operation's work.

**`_recorded_text` refuses to render a missing field as the word `None`** (`:231-239`): a detail
sentence naming `scope 'None'` would be a false statement about a record that simply did not carry one.

**The cleanup guard is two reads and two measured facts** (`:327-388`). The staged candidate file is
read (`read_dataset_identity`), the location the ordinary read route selects is read through that
route's own owner (`resolve_published_intent`), and removal happens only when either the published
location holds exactly the staged dataset (`_destination_holds`, `:391-399`) **or** the staged
candidate holds no invariant revision and its walk completed (`measured_empty`). The second branch is
what keeps the owner reachable for a bootstrap that never published, and it is a measurement of zero
rather than an assumption of emptiness. Every other state refuses: `staged_candidate_unreadable`,
`destination_does_not_hold_the_staged_dataset` and `destination_holds_another_dataset`
(`_unpublished`, `:402-428`), the last one reporting how many authored revisions the candidate holds of
its own.

### Conventions

The module imports the dataset-identity reader, the contents walk, the published-intent resolver, the
coordination context model and the shipped candidate path helper. It never writes a knowledge record
and never decides what a record means.

### Invariants And Boundaries

- The retained record is a derived projection of the report, the allocation journal and a store read;
  it is never read as authority.
- `remaining` and `unmeasured` are separate fields; a measured absence is never merged with an unread
  location.
- `stored`/`absent` are measurements; `unmeasured`/`not-attempted` are not. `not-allocated` is not in
  the vocabulary at all.
- A record read back whose `storeState` is not in the shipped vocabulary becomes `unmeasured`.
- Owed entries named by an inherited record are carried forward and **re-derived**, never copied.
- `read_progress` distinguishes `absent`, `retained`, `moved` and `unreadable`; none of them is
  reported as "no progress".
- `write_progress` is atomic and raises `BootstrapProgressConflict` rather than overwriting another
  operation's retained progress.
- Cleanup removes the staging root only on one of the two measured facts and refuses by name otherwise.
- A staging root belongs to exactly one bootstrap operation.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this staging implements, and it is a task-tree document rather than a configured domain source.

No external documentation is required for the bootstrap staging and its cleanup owner.

### Repo-Internal References

- **The module's own statement that the record is a projection and that cleanup is the one irreversible act.** [1]
- The published surface: the three constants, the values, the readers and the cleanup owner. [2]
- The one staged-candidate directory name and the one progress file name, constants so the places agree. [3]
- **The five store states, never collapsed into one another.** [4]
- **Why a wrong staging root raises rather than returning a refusal.** [5]
- **One entry's row: the run's outcome beside the store's independent answer.** [6]
- **The retained progress, with `remaining` and `unmeasured` as two facts and `remaining_basis` naming the derivation.** [7]
- The exact JSON object the record stores, with a null identity rather than an omitted one. [8]
- **The four retention states and why each calls for a different act.** [9]
- One cleanup request's outcome: what was removed, or the fact that refused it. [10]
- The record's exact path inside one staging root, and the candidate directory beside it. [11]
- The instant one observation is recorded at, in the shipped normalized-UTC spelling. [12]
- **Why a missing field is reported as absent rather than rendered as the word `None`.** [13]
- **The read that keeps `retained`, `moved`, `unreadable` and `absent` apart, and never reports "no progress".** [14]
- **The atomic write that raises rather than overwriting another operation's retained progress.** [15]
- **The cleanup guard: two reads, two measured facts, and a named refusal in every other state.** [16]
- Whether the ordinary read route's own read found exactly the staged dataset at the location. [17]
- The two refusal codes for staging that still holds work nobody can select. [18]
- The two result constructors, so one outcome is built in one place. [19]
- **The one bounded four-valued contents read both this cleanup and the run's readback use.** [20]
- The staged candidate's identity, read from the candidate file rather than inferred. [21]
- The ordinary read route's owner, which is what makes the destination comparison a read. [22]
- The shipped candidate database path helper this staging names its candidate through. [23]
- The identity type both the retained record and the cleanup comparison carry. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file: it reads one staging root and one repository's
own published location. The resolved settings' `crossRepo.allow` is empty, so nothing here names, reads
or writes another repository.

No meaningful cross-repo references found.
