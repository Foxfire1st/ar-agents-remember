# mcp/tests/test_durable_store_contract.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_durable_store_contract.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

In-process durable-store exclusion, rewrite and strict-read contracts.

## Code Commentary

### Logic

Real threads prove per-log exclusion, same-thread reentrancy and dismissal preservation during prune. A non-excluding flock double causes append refusal until locking works. Future-major rows block authority reads while projection retains readable rows. Compaction reports dropped records, unlocked replace refuses and interrupted rewrite preserves the old log without temp leftovers.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Thread mutex behavior is explicit rather than inferred from a shared file descriptor. Fault injection stays at the locking or atomic OS seam; it does not replace store logic.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| A second thread is kept out of a log that is already held. | `test_a_second_thread_is_kept_out_of_a_log_that_is_already_held` | mcp/tests/test_durable_store_contract.py:150-200 |
| Taking a logs exclusivity twice on one thread does not deadlock. | `test_taking_a_logs_exclusivity_twice_on_one_thread_does_not_deadlock` | mcp/tests/test_durable_store_contract.py:202-251 |
| A dismissal is not lost to a prune sweeping on another thread. | `test_a_dismissal_is_not_lost_to_a_prune_sweeping_on_another_thread` | mcp/tests/test_durable_store_contract.py:255-330 |
| A store refuses the append itself and recovers once the lock works. | `test_a_store_refuses_the_append_itself_and_recovers_once_the_lock_works` | mcp/tests/test_durable_store_contract.py:349-368 |
| A future row stops the authority read and only costs projection a tick. | `test_a_future_row_stops_the_authority_read_and_only_costs_projection_a_tick` | mcp/tests/test_durable_store_contract.py:405-425 |
| Compact drops what keep rejects and reports the count. | `test_compact_drops_what_keep_rejects_and_reports_the_count` | mcp/tests/test_durable_store_contract.py:446-455 |
| Replace records refuses an unlocked caller and changes nothing. | `test_replace_records_refuses_an_unlocked_caller_and_changes_nothing` | mcp/tests/test_durable_store_contract.py:457-473 |
| An interrupted rewrite cleans up too. | `test_an_interrupted_rewrite_cleans_up_too` | mcp/tests/test_durable_store_contract.py:527-539 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the current twelve contract claims, made delete/entry-order evidence explicit, and corrected the per-call UUID temp-cleanup description. Preserved the complete 2026-08-01 entry verbatim as a labelled historical quotation after independent review; its old citations are retained as history.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Reconciled test imports and injection with kernel.file_lock, retained the durable error-family and real exclusion assertions, corrected owned-state cleanup and atomic temp semantics, and reopened named source extents against prepared code.


- 2026-08-24T21:23+02:00 — No content impact: the owned-state context manager moved from the test
  tree to `agents_remember_test_support.testing.global_state`; durable-store assertions are unchanged.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the startup import move and confirmed the tested
  durable-store contract is unchanged; final provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T19:57:55+02:00 — Closeout citation review: retained the shared-write-boundary claim
  after re-reading the candidate and replaced ambiguous function-name anchors with exact unique
  signatures plus the incident-shaped regression name. Verification metadata remains pinned until
  closeout.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: re-read the shared write boundary after checkout-target confinement was added ahead of lock/append/rewrite filesystem effects; linked the focused isolation regressions. Verification metadata remains pinned until approved closeout stamps the L21 code commit.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired and normalized the durable-store test citations; final exact frozen-snapshot check is clean.
- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: repaired 26 citations, corrected 1 anchor-in-range error, and removed 6 duplicate source segments; no unresolved Tier-3 claims.

Historical quotation: the complete 2026-08-01 entry is preserved verbatim below. Its then-current citations and implementation notes are historical; current evidence is in the active body above.

~~~~text
- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: created the card for the in-process half of the
  `ar-durable-store/1.0` contract. **The mutex is recorded as what the source says it is and not
  as a race fix:** `flock` already excludes two threads of one process (the lock lives on the open
  file description and `exclusive_access` opens a fresh one per non-reentrant acquisition), that
  was measured rather than assumed, and the thread-level lost update was therefore already closed;
  what `thread_mutex_for` (`durable_store.py`) closes is the *dependence of thread
  exclusion on where the handle came from* — cache one lockfile handle on the store, the obvious
  "stop opening two files per append" optimisation, and every thread shares one description,
  `flock` stops excluding, and nothing in the tree fails. The first test
  cit:([`test_a_second_thread_is_kept_out_of_a_log_that_is_already_held`], mcp/tests/test_durable_store_contract.py:174-224) asserts the
  mutex directly via a non-holding thread's `acquire(blocking=False)` probe rather than inferring
  it from an ordering `flock` alone would produce; the re-entrancy test
  cit:([`test_taking_a_logs_exclusivity_twice_on_one_thread_does_not_deadlock`], mcp/tests/test_durable_store_contract.py:239-288) exists because
  the added mutex is a second lock a thread can hang itself on, and asserts four things beyond the
  absence of a hang. **The unsafe-filesystem tests are recorded as faking the filesystem, not the
  code:** cit:([`_IgnoredFlock`], mcp/tests/test_durable_store_contract.py:124-141) reproduces WSL DrvFs literally — accept the `flock`, take no
  lock — forwards every other `fcntl` name untouched, and is substituted for `durable_store`'s own
  module reference alone so no other thread loses its locks; every assertion is on raised type,
  message text and what is on disk (including that no log was created), none on the substitution.
  cit:([`_FailingOs`], mcp/tests/test_durable_store_contract.py:144-164) applies the same discipline at the `os` boundary, and `_rewrite_under`
  cit:([`_rewrite_under`], mcp/tests/test_durable_store_contract.py:683-699) takes the lock outside the substitution so the failure under test is the rewrite's.
  Also recorded the `schemaVersion` major/minor policy and its consequence on one log
  cit:([`SchemaVersionMajorTests`], mcp/tests/test_durable_store_contract.py:434-520), the blank-line case that both readers skip cit:([`BlankLineToleranceTests`], mcp/tests/test_durable_store_contract.py:523-566), the nudge log's two rewrite
  entry points including the no-op branch that must not replace the inode cit:([`test_compact_that_keeps_everything_leaves_the_file_byte_identical`], mcp/tests/test_durable_store_contract.py:598-608) and the
  unlocked-caller refusal that must change nothing cit:([`test_replace_records_refuses_an_unlocked_caller_and_changes_nothing`], mcp/tests/test_durable_store_contract.py:631-647), failed-rewrite temp cleanup
  including why the handler catches cit:([`test_an_interrupted_rewrite_cleans_up_too`], mcp/tests/test_durable_store_contract.py:716-728), `GateStore.delete` answering
  honestly without rewriting on a miss cit:([`test_deleting_an_id_that_is_not_there_is_false_and_rewrites_nothing`], mcp/tests/test_durable_store_contract.py:746-759), and the role declaration asserted for its
  **ordering** by recording `declared_process_role()` from inside a patched `run_server`
  cit:([`test_main_declares_the_mcp_role_before_the_server_starts_serving`], mcp/tests/test_durable_store_contract.py:785-813). **Filed one Todo:** the thread lost-update test's exclusion proof is a 0.25 s
  `assertFalse(dismiss_done.wait(...))` — sound given the sweep holds the lock until released, but
  the only assertion in the file whose failure mode is a slow machine. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is
  blank because the source file is new and uncommitted; closeout owns its first stamp.
~~~~
