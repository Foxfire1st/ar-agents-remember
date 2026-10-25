# mcp/tests/test_sync_parked_candidate.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise the parked worktree candidate inside the existing sync transaction and prove its return, retained conflicts, cancellation, and recovery.

## Code Commentary

### Logic

The transaction witnesses reuse SyncFixture's real repositories and contracts. Clean code carry restores modified/untracked WIP and advances the recorded base. The external-memory case now includes staged cache data beside a real onboarding draft: only the draft appears in parked WIP, and the draft returns with no remaining stash.

Other cases preserve a genuine reapply conflict and its wipRestore marker, return the candidate on cancel, resume a crash before restoration, continue a staged source conflict without losing parked content, and refuse a pre-existing genuine unmerged index without creating a stash. The module validates the public resolution projection as well as the dictionary so producer/model drift is visible.

The module now protects complete reapply proof, already-held edits, truly missing parked bytes, untracked/deleted entries and memory-side cache separation. Cancellation saves later/index-only/marker/symlink/unproved state before completing. New cases cover renames, observed SIGKILL cuts, save failures and live-lock handling. Full-inventory failure cannot accept the capped journal sample. Paired restoration and cancellation-retry assertions protect already-restored code work across a memory stop. The named retained/terminal phase cuts now hold the native child at the legacy-journal unlink audit event after the durable replacement. Partial-restore cuts use serial native Git checkout and a required, identity-preserving filter on the second bulk path, held before it returns bytes; the first path is restored, and the parent kills the actual process group. These specific holds remain open under parent scheduling delay without replacing product functions or Git operations. Other kill cuts still poll and fail or retry on a missed window; this is source structure, not new execution evidence.

`ResumedConvertedMemoryMergeTests` reproduces an interrupted converted-memory merge with real structural crossing. The untouched witness checks cancellation and its asserted memory state; the owner-write control saves patches/path list containing OWNER AFTER INTERRUPT, cancels with unchanged memory HEAD, retires the stash, and journals cancelled. The separately sealed Reviewer paired companion supplies executed both-tree/head/index evidence: the file card does not upgrade the positive test's name into a stronger assertion than its body makes.

The same class's identical-byte carried-line case records a reviewed pair, parks `SAME = 1`, lands exactly those bytes, and invokes the real public sync tool. Its explicit assertion is that the returned `review_rebinding.state` is `current`; it does not assert `covers_resolved_pair` or every successful-response field. The sibling different-byte case retains the original refused-sync `not-measured` and non-covering assertions. These complementary scenarios do not change a production owner or strengthen the historical cancellation proof facets; execution evidence remains separately attributed.


- An identical-byte carried line is tested through the public sync tool with an exact current-block assertion. [6]


### Conventions

Intentional fault injection stops restoration once; native Git creates the genuine conflict. Assertions cover exact payload state, candidate bytes, stash identity/emptiness, and recorded bases. These are transaction-level scenarios, not a full closeout acceptance claim.

### Invariants And Boundaries

- Real parked content must return; a memory cache is not part of that candidate.
- A genuine reapply conflict retains the stash until resolution or cancellation.
- Resume must return an already-parked candidate without inventing another merge.
- Pre-existing real conflicts still refuse admission.
- Code-domain files keep ordinary semantics.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- Code and memory WIP return, with cache excluded from the memory candidate. [1]

- Genuine reapply conflict and cancellation preserve candidate content. [2]

- Crash recovery and retained-source continuation return parked work. [3]

- Pre-existing genuine conflicts remain a refusal. [4]



- Production parked-content boundary and exact restore proof. [5]

- Named retained/terminal journal cuts hold the native child after durable journal replacement and before the legacy unlink, then require a stopped child and SIGKILL its actual process group; other polling cuts are not upgraded by this source observation. [7]
- Partial-restore cuts use serial native Git and a required identity filter on the second bulk path, stopping before returning bytes so the first path is restored while Git waits; recovery passes unchanged bytes via the one-use marker. This is source-only, not a new test pass. [8]

### Cross-Repo References

No additional configured cross-repository contract is asserted.
