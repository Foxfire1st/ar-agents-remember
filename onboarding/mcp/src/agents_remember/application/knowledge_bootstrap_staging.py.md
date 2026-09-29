# mcp/src/agents_remember/application/knowledge_bootstrap_staging.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_bootstrap_staging.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T09:20+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba` |
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this staging implements, and it is a task-tree document rather than a configured domain source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the bootstrap staging and its cleanup owner. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement that the record is a projection and that cleanup is the one irreversible act.** | "The record is a projection, never a store"; "loses it during cleanup" | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:1-26 |
| The published surface: the three constants, the values, the readers and the cleanup owner. | `__all__` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:53-67 |
| The one staged-candidate directory name and the one progress file name, constants so the places agree. | `BOOTSTRAP_CANDIDATE_DIRECTORY`; `BOOTSTRAP_PROGRESS_NAME`; `BOOTSTRAP_PROGRESS_SCHEMA` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:72-74 |
| **The five store states, never collapsed into one another.** | `EntryStoreState` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:82-82 |
| **Why a wrong staging root raises rather than returning a refusal.** | `BootstrapProgressConflict` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:89-95 |
| **One entry's row: the run's outcome beside the store's independent answer.** | `EntryProgress`; `store_state`; `as_record` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:98-125 |
| **The retained progress, with `remaining` and `unmeasured` as two facts and `remaining_basis` naming the derivation.** | `BootstrapProgress`; `remaining`; `unmeasured` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:128-193 |
| The exact JSON object the record stores, with a null identity rather than an omitted one. | `destinationIdentity`; `destinationPath`; `remainingBasis` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:152-191 |
| **The four retention states and why each calls for a different act.** | `ProgressRetention` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:196-211 |
| One cleanup request's outcome: what was removed, or the fact that refused it. | `StagingCleanup` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:214-221 |
| The record's exact path inside one staging root, and the candidate directory beside it. | `progress_path`; `staged_candidate_directory` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:224-227; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:230-233 |
| The instant one observation is recorded at, in the shipped normalized-UTC spelling. | `observed_now` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:236-239 |
| **Why a missing field is reported as absent rather than rendered as the word `None`.** | `_recorded_text` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:242-250 |
| **The read that keeps `retained`, `moved`, `unreadable` and `absent` apart, and never reports "no progress".** | `read_progress`; "moved" | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:242-299 |
| **The atomic write that raises rather than overwriting another operation's retained progress.** | `write_progress`; `BootstrapProgressConflict` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:89-95; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:393-415 |
| **The cleanup guard: two reads, two measured facts, and a named refusal in every other state.** | `discard_bootstrap_staging`; "measured_empty" | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:418-479 |
| Whether the ordinary read route's own read found exactly the staged dataset at the location. | `_destination_holds` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:482-490 |
| The two refusal codes for staging that still holds work nobody can select. | `_unpublished`; "destination_does_not_hold_the_staged_dataset"; "destination_holds_another_dataset" | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:493-519 |
| The two result constructors, so one outcome is built in one place. | `_discarded`; `_cleanup_refusal` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:522-528; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:531-532 |
| **The one bounded four-valued contents read both this cleanup and the run's readback use.** | `dataset_revisions`; `measured_empty`; `absence_established` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:80-89; mcp/src/agents_remember/application/knowledge_dataset_contents.py:91-100; mcp/src/agents_remember/application/knowledge_dataset_contents.py:103-182 |
| The staged candidate's identity, read from the candidate file rather than inferred. | `read_dataset_identity` | mcp/src/agents_remember/application/knowledge_before_half.py:210-223 |
| The ordinary read route's owner, which is what makes the destination comparison a read. | `resolve_published_intent`; `PublishedIntentSelection`; `PublishedIntentUnavailable` | mcp/src/agents_remember/application/published_intent.py:258-258; mcp/src/agents_remember/application/published_intent.py:176-207 |
| The shipped candidate database path helper this staging names its candidate through. | `candidate_database_path` | mcp/src/agents_remember/models/knowledge/snapshot.py:58-61 |
| The identity type both the retained record and the cleanup comparison carry. | `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:195-204 |

## Cross-Repo References

No cross-repository behavior is implemented in this file: it reads one staging root and one repository's
own published location. The resolved settings' `crossRepo.allow` is empty, so nothing here names, reads
or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. `PublishedIntentSelection` gained an optional `memory_tree` field and `published_intent.py` grew by 160 lines (MIK-R23); the claim naming the ordinary read route's owner was re-read and still holds, and its ranges were re-pointed by exact base-to-working line mapping.
- 2026-09-24T10:50+02:00 — 260921-ICR-L29 curator, **micro-round-2 bytes (documentation only)** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`): **re-read against the
  corrected docstrings; the card and the source agree.** The module docstring now states both reasons the
  retained file is read and names `_progress_from_record` as the reconstruction, matching this card's
  Purpose; the four-value `EntryStoreState` literal and the unknown-state-becomes-`unmeasured` rule are
  stated in the docstring as well as enforced in `_progress_from_record`. The card's own note that the
  docstring was stale is retired. All ranges were re-derived for the docstring-only line shift. **No
  verification stamp was advanced.**
- 2026-09-24T10:20+02:00 — 260921-ICR-L29 curator, **fix-round bytes** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`; gate `verify-l29-round2.md`,
  first line `pass-with-findings`): **two sentences this card stated were falsified by the fix round and
  are rewritten, not annotated.** (a) The card said the only thing the retained file is *read* for is to
  notice that it describes another operation. That is no longer true: `read_progress` now reconstructs
  the record (`_progress_from_record`) so `_carried_forward` can carry the owed entries it names into
  the next run's record, re-derived against that run's own store read. The Purpose now states both
  reasons the file is read, and the reconstruction rule. (b) The card described a **five**-value store
  vocabulary including `not-allocated`. The fix round removed it — no path ever produced it — so the
  vocabulary is four values, and a record carrying an unknown `storeState` is reconstructed as
  `unmeasured` rather than read as "nothing owed". A third addition records that **a committed run whose
  batch wrote nothing now writes the record**, because leaving the previous one standing is how a
  manifest goes stale when the candidate binding moved. The module's own docstring then still carried the
  pre-fix "the only thing the old file is *read* for" sentence; **the micro round corrected it**, and the
  docstring now states both reasons the file is read — the re-observation question and the carry-forward —
  which is what this card says. **No verification stamp was advanced** — the candidate is uncommitted and
  the governed closeout owns the real code and memory commits.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): created this one-to-one card for the module
  `ICR-R29@v1` introduced as **the bootstrap staging, its retained progress record and its bounded
  cleanup owner**. The stamp basis is the leaf's base commit, because the module is untracked there.
  Two sentences carry the correctness this card exists to protect: the retained record is a
  **projection derived from the store** and is never read as authority (only a scope/destination
  mismatch is read, and that is the re-observation condition), and **`remaining` and `unmeasured` are
  two different facts** — a measured absence (`stored`/`absent`) is never merged with an unread location
  (`unmeasured`), because merging them would let a bounded walk manufacture remaining work. Cleanup is
  the one irreversible act and is guarded by two reads, refusing by name in every other state. No
  verification stamp beyond the leaf's base is advanced: the candidate is uncommitted and the governed
  closeout owns the real commit.
