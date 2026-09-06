# mcp/tests/test_durable_store_contract.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_durable_store_contract.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview      | `overview.md`                                |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`ar-durable-store/1.0` asserted **inside one process**: the per-log in-process mutex and its
re-entrancy, the `schemaVersion` major/minor policy and the two read policies that follow from it,
the refusal on a filesystem whose `flock` does not exclude, the nudge log's two rewrite entry
points, failed-rewrite temp cleanup, `GateStore.delete`, and the MCP entry point's process-role
declaration.

It is the other axis of the same contract that `test_controlplane_store_durability.py` cannot
reach. That suite uses `multiprocessing` deliberately — the GIL would serialise the very window it
forces — so nothing in it can observe two **threads** of one process, which is what the dashboard
actually is: `AttentionDismissalStore.dismiss` is reached from the HTTP dismiss route and
`prune_lifecycles` from the projection sweep, both whole-file read-modify-writes over the same
log.

## Code Commentary

### Logic

**cit:([`InProcessExclusivityTests`], mcp/tests/test_durable_store_contract.py:165-363).**
cit:([`test_a_second_thread_is_kept_out_of_a_log_that_is_already_held`], mcp/tests/test_durable_store_contract.py:172-222) runs a holder and a
follower thread and asserts the exact order `["A-holds", "B-refused", "A-leaves", "B-enters"]`.
The ordering half would pass on `flock` alone; the interesting assertion is the
`thread_mutex_for(log).acquire(blocking=False)` probe from a non-holding thread, which asks the
log's own mutex whether the log is claimed. Exceptions are collected into a list and asserted
empty on the main thread rather than swallowed in the worker.
cit:([`test_one_mutex_per_log_and_a_different_log_is_a_different_mutex`], mcp/tests/test_durable_store_contract.py:224-235) pins identity in
both directions — same log, same object; different logs, different objects — because a factory
handing out a fresh lock per call would guard nothing, and one lock shared across logs would
serialise unrelated stores.
cit:([`test_taking_a_logs_exclusivity_twice_on_one_thread_does_not_deadlock`], mcp/tests/test_durable_store_contract.py:237-286) asserts four
things and the absence of a hang is only the first: the nested frame can drive `rewrite_lines`
(so `require_lock_held` sees the hold through the nesting), the **outer** frame still holds after
the inner one exits (a counter that popped instead of restoring would have silently released a
lock its caller believes it holds), and the hold is genuinely gone after the outermost exit —
proven by `require_lock_held` then raising `DurableStoreError`.
cit:([`test_a_dismissal_is_not_lost_to_a_prune_sweeping_on_another_thread`], mcp/tests/test_durable_store_contract.py:288-363) forces the
lost-update pair the dashboard actually runs: the projection sweep is parked at the moment of its
physical write while a dismiss runs on a second thread. Only the write moment is interposed; the
store's own read, filter and commit are the real ones. The final assertion is that **both**
survive — the dead lifecycle's row gone, the kept row still there, and the racing click not
discarded.

**cit:([`UnsafeLockFilesystemTests`], mcp/tests/test_durable_store_contract.py:366-429).**
cit:([`test_a_lock_that_does_not_exclude_is_refused_and_names_what_to_fix`], mcp/tests/test_durable_store_contract.py:382-408) asserts the
message names the lock path, the store, and "NFS", that the exception is a
`DurableStoreError` so a caller catching the family catches it, and then the two that matter for
durability: the `with` body was never entered (`entered == []`) and **no log was created**.
cit:([`test_a_store_refuses_the_append_itself_and_recovers_once_the_lock_works`], mcp/tests/test_durable_store_contract.py:410-429) drives the
same refusal through `GateStore.append` — an ordinary caller that never mentions locking — and
then repeats the append once `flock` excludes again, so a failed probe is not a latch that
poisons the path for the rest of the process.

**cit:([`SchemaVersionMajorTests`], mcp/tests/test_durable_store_contract.py:432-518).** One rule and the two read policies it decides.
An unknown **major** is refused at the model boundary with a message naming the version and the
contract cit:([`test_a_record_stamped_with_an_unknown_major_is_refused_at_the_boundary`], mcp/tests/test_durable_store_contract.py:466-479); an unknown **minor** of the supported major is accepted *and kept* through
the round trip rather than silently restamped cit:([`test_an_unknown_minor_of_the_supported_major_is_accepted_and_kept`], mcp/tests/test_durable_store_contract.py:481-496). `test_a_future_row_stops_the_authority_
read_and_only_costs_projection_a_tick` cit:([`test_a_future_row_stops_the_authority_read_and_only_costs_projection_a_tick`], mcp/tests/test_durable_store_contract.py:498-518) then shows the consequence on one log: the
tolerant `read_for_projection` returns the readable gate, the strict `read` raises, and — the
assertion that keeps tolerance cheap — the log's bytes are unchanged, so the future row is still
there for a build that can read it. cit:([`_append_future_major`], mcp/tests/test_durable_store_contract.py:454-464) builds that row by
re-stamping a real record rather than hand-rolling JSON, so it differs from a valid row in exactly
the field under test.

**cit:([`BlankLineToleranceTests`], mcp/tests/test_durable_store_contract.py:521-564).** A blank line is neither a record nor a torn line, so
**both** readers step over it — asserted on the gate log and the expectation log. Worth stating
precisely because the two policies are otherwise opposite: the strict reader skipping a blank line
is not the tolerance leaking across.

**cit:([`OrchestrationNudgeRewriteTests`], mcp/tests/test_durable_store_contract.py:567-645).** `compact` drops what `keep` rejects and reports
the count, and the survivor is re-serialised whole rather than truncated cit:([`test_compact_drops_what_keep_rejects_and_reports_the_count`], mcp/tests/test_durable_store_contract.py:585-594); a compaction
that keeps everything **does not rewrite at all** and the file stays byte-identical cit:([`test_compact_that_keeps_everything_leaves_the_file_byte_identical`], mcp/tests/test_durable_store_contract.py:596-606),
because a rewrite that changes nothing still replaces the inode and opens an appender window for
no gain; compacting to nothing leaves an **empty file**, `is_file()` true and `read_bytes() == b""`
cit:([`test_compact_empties_the_log_without_unlinking_it`], mcp/tests/test_durable_store_contract.py:608-616). `replace_records` succeeds under a held lock cit:([`test_replace_records_rewrites_the_log_when_the_caller_holds_the_lock`], mcp/tests/test_durable_store_contract.py:618-627) and refuses an unlocked
caller **while changing nothing** cit:([`test_replace_records_refuses_an_unlocked_caller_and_changes_nothing`], mcp/tests/test_durable_store_contract.py:629-645) — the second assertion is the durability property,
since an unlocked rewrite would discard everything appended since the caller's read.

**cit:([`FailedRewriteTests`], mcp/tests/test_durable_store_contract.py:648-726).** The shared `_rewrite_under` helper cit:([`_rewrite_under`], mcp/tests/test_durable_store_contract.py:681-697) asserts, for
every injected failure: the log is byte-identical afterwards, it still reads back as the record it
held, and no `.tmp` remains in the directory. `test_a_failed_rename_removes_the_temp_file_it_had_
already_written` cit:([`test_a_failed_rename_removes_the_temp_file_it_had_already_written`], mcp/tests/test_durable_store_contract.py:699-712) additionally asserts that no temporary file remains under the pid-scoped prefix; the trailing UUID is per call,
and cit:([`test_an_interrupted_rewrite_cleans_up_too`], mcp/tests/test_durable_store_contract.py:714-726) raises `KeyboardInterrupt` from the
`fsync` inside the temp write — a different instruction from the rename case — which is why the
production handler catches `BaseException` rather than `Exception`.

**cit:([`GateDeleteTests`], mcp/tests/test_durable_store_contract.py:729-763).** A delete that missed answers `False` **and rewrites nothing**
(bytes unchanged), because rewriting for a call with nothing to do would open the
appender-versus-rewriter window gratuitously; a delete that hit answers `True`, empties the read,
and leaves the log a file. The no-op method is anchored explicitly by cit:([`test_deleting_an_id_that_is_not_there_is_false_and_rewrites_nothing`], mcp/tests/test_durable_store_contract.py:744-757).

**cit:([`ProcessRoleDeclarationTests`], mcp/tests/test_durable_store_contract.py:766-811).** `server_module.main` declares the role before
`run_server` is reached — asserted by recording `declared_process_role()` from inside a patched
`run_server`, so the ordering is the property under test rather than the end state. The ordering assertion is cit:([`test_main_declares_the_mcp_role_before_the_server_starts_serving`], mcp/tests/test_durable_store_contract.py:783-811). The writer
check is then exercised in both directions: the gate log names `mcp` among its writers and
accepts, supervisor-signals names only the dashboard and raises `CompactionOwnerError`. Because
the declaration is process-global by design, `setUp` registers a cleanup that restores the
previous kernel-owned mutable state through `preserve_owned_mutable_state` cit:([`_contain_process_role`], mcp/tests/test_durable_store_contract.py:97-100).

### Conventions

**What the mutex is claimed to do, and what it is not.** The module header cit:([`exclusive_access`], mcp/src/agents_remember/controlplane/durable_store.py:319-360) states it
before any test runs, and the tests are written to match. `flock` **does** exclude two threads of
one process — the lock lives on the open file description and `exclusive_access` opens a fresh one
per non-reentrant acquisition, so thread B blocks on thread A exactly as another process would.
That was measured before this file was written, which means the thread-level lost update was
already closed and **the mutex is not fixing a reproducible race**. What was not closed is that
the exclusion rested on *where the handle came from* rather than on anything the contract stated:
cache that handle on the store — the obvious fix for an append path that opens two files per
record — and every thread would share one description, `flock` would silently stop excluding them,
and no test in the tree would have noticed. `thread_mutex_for` makes the in-process half a stated
property, and the first test asserts it directly instead of inferring it from an ordering `flock`
alone would also produce. The re-entrancy case exists because that mutex is a second lock a thread
can hang itself on, and the thread-local depth counter that already tolerates the first one has to
compose with it.

**The filesystem is faked, never the code.** cit:([`_IgnoredFlock`], mcp/tests/test_durable_store_contract.py:122-139) is `fcntl` as WSL DrvFs
presents it: `flock` accepted and no lock taken; every other name (`LOCK_EX`, `LOCK_NB`,
`LOCK_UN`) forwards untouched through `__getattr__`. It is substituted for `file_lock`'s module reference; direct imports of the standard-library `fcntl` module elsewhere are not replaced —
and the substitution is at the single boundary the capability probe talks to, because
`_verify_lock_capability`'s refusal only fires where a second `flock` on a second description
*succeeds*, which no correctly locking filesystem does and no test can mount. Every assertion in
those tests is on the raised type, the message text, and what is on disk; none is on the
substitution.

**cit:([`_FailingOs`], mcp/tests/test_durable_store_contract.py:142-162) is the same discipline at the `os` boundary.** One named call raises;
`getpid`, `open`, `fsync`, `close` and `O_RDONLY` all forward to the real `os`, so the rewrite
under test is the shipped one everywhere except the one instruction the scenario needs to fail. A
full disk or a crashing rename is not reproducible on demand, which is why the injection exists at
all. In `_rewrite_under` the lock is taken **outside** the substitution cit:([`_rewrite_under`], mcp/tests/test_durable_store_contract.py:681-697) so the failure
under test is the rewrite's and not the lock's.

**`WATCHDOG_SECONDS = 15.0` cit:([`WATCHDOG_SECONDS`], mcp/tests/test_durable_store_contract.py:85-85)** bounds every thread join and event wait, so a wedged lock is
reported in seconds as a test failure rather than as a suite that never returns.

### Invariants And Boundaries

- The mutex must be described as what it is: a **stated** in-process exclusion that removes a
  dependence on how the lockfile handle happens to be obtained. It does not repair a
  reproducible thread race, and a card or comment that says otherwise is wrong.
- `exclusive_access` must stay re-entrant on both locks or on neither. A non-re-entrant mutex
  would reintroduce the self-deadlock one layer below where the thread-local depth counter can
  see it.
- A lock that cannot exclude is refused loudly and never downgraded to a no-op; the refusal must
  happen **before** anything is written, which is why "no log was created" is asserted alongside
  the exception.
- `rewrite_lines` never unlinks: an empty record set is an empty file. Both the nudge compaction
  test and `GateDeleteTests` assert emptiness rather than absence.
- `ProcessRoleDeclarationTests` mutates the kernel-owned execution declaration and must restore it through the owned-state helper; left standing, every later test in the interpreter would claim to be the MCP server
  and `check_declared_writer` would start refusing the dashboard-only stores.
- Test seams follow the actual owner: mutex and capability probes use `kernel.file_lock`, atomic failure injection uses `kernel.atomic_write`, and the dismissal race patches `attention_module.rewrite_lines`. The source no longer reaches a durable-store declaration dictionary.

### Todos

cit:([`test_a_dismissal_is_not_lost_to_a_prune_sweeping_on_another_thread`], mcp/tests/test_durable_store_contract.py:288-363) proves the
dismisser is excluded with a **timing** assertion: `assertFalse(dismiss_done.wait(0.25))`. The
surrounding structure makes it sound — the sweep holds the lock until `release.set()`, so a
correct implementation cannot finish inside that window — but it is the only assertion in the file
whose failure mode is "the machine was slow" rather than "the property broke", and it is the one
to look at first if this suite ever flakes.

## Docs References

No Domain Documentation source is configured. The suite exercises the repository-owned durable-store contract and injects an ineffective `flock` at the shared kernel owner; it does not certify external mount implementations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite imports the moved mechanics from their shared kernel owner while retaining the durable-store policy and error adapter. Other store and process-state scenarios keep their existing behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| Contract policy, advisory ownership and held-lock entry. | `StoreOwnership`; `exclusive_access` | mcp/src/agents_remember/controlplane/durable_store.py:98-138; mcp/src/agents_remember/controlplane/durable_store.py:319-360 |
| Actual per-log mutex and unchanged whole-resource suffix. | `thread_mutex_for`; `lock_path_for` | mcp/src/agents_remember/kernel/file_lock.py:41-55; mcp/src/agents_remember/kernel/file_lock.py:36-38 |
| Reentrant two-lock acquisition and ineffective-filesystem probe. | `_LockDepth`; `exclusive_file_lock`; `_verify_lock_capability` | mcp/src/agents_remember/kernel/file_lock.py:19-27; mcp/src/agents_remember/kernel/file_lock.py:87-114; mcp/src/agents_remember/kernel/file_lock.py:58-84 |
| Translated durable-store refusal and guarded write paths. | `exclusive_access`; `require_lock_held`; `append_line`; `rewrite_lines`; `_require_rewrite_access` | mcp/src/agents_remember/controlplane/durable_store.py:319-360; mcp/src/agents_remember/controlplane/durable_store.py:363-381; mcp/src/agents_remember/controlplane/durable_store.py:391-402; mcp/src/agents_remember/controlplane/durable_store.py:421-428; mcp/src/agents_remember/controlplane/durable_store.py:436-438 |
| One major-version rule and validated record base. | `schema_version_supported`; `DurableRecord` | mcp/src/agents_remember/controlplane/durable_store.py:232-253; mcp/src/agents_remember/controlplane/durable_store.py:256-279 |
| Owned-state cleanup and lock injection target. | `_contain_process_role`; `_IgnoredFlock` | mcp/tests/test_durable_store_contract.py:97-100; mcp/tests/test_durable_store_contract.py:122-139 |
| Real in-process exclusion and capability refusal scenarios. | `InProcessExclusivityTests`; `UnsafeLockFilesystemTests` | mcp/tests/test_durable_store_contract.py:165-363; mcp/tests/test_durable_store_contract.py:366-429 |
| Atomic publication failure injection and per-call temp cleanup. | `_FailingOs`; `FailedRewriteTests` | mcp/tests/test_durable_store_contract.py:142-162; mcp/tests/test_durable_store_contract.py:648-726 |
| Atomic bytes/text owner and unique temporary path. | `_temp_path_for`; `atomic_write_bytes`; `atomic_write_text` | mcp/src/agents_remember/kernel/atomic_write.py:21-29; mcp/src/agents_remember/kernel/atomic_write.py:51-70; mcp/src/agents_remember/kernel/atomic_write.py:73-75 |
| Strict/tolerant reads, blank lines and whole-file rewrites retain their behavior. | `SchemaVersionMajorTests`; `BlankLineToleranceTests`; `OrchestrationNudgeRewriteTests`; `GateDeleteTests` | mcp/tests/test_durable_store_contract.py:432-518; mcp/tests/test_durable_store_contract.py:521-564; mcp/tests/test_durable_store_contract.py:567-645; mcp/tests/test_durable_store_contract.py:729-763 |
| Actual process-entry declaration and cross-test restoration remain explicit. | `ProcessRoleDeclarationTests`; `ProcessRoleIsolationTests` | mcp/tests/test_durable_store_contract.py:766-811; mcp/tests/test_durable_store_contract.py:814-854 |
| Cross-process forced/stress durability is covered by the sibling suite. | `MultiProcessDurabilityTests` | mcp/tests/test_controlplane_store_durability.py:125-211 |

## Cross-Repo References

No meaningful cross-repo references found. The suite imports only `agents_remember`, `pydantic`,
a sibling test fixture and the standard library; the platform behaviour it reproduces is faked at
the `fcntl` boundary rather than reached across a repository or system boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## L23 Runtime Package Review

The suite now imports startup through `application.runtime.startup`, matching the production
composition-root move. Its durable-store ownership, fail-closed startup, and validation assertions
are unchanged.

## Update History

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
