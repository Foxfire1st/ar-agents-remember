# mcp/tests/test_durable_store_contract.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_durable_store_contract.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-08-01T14:20+02:00                       |
| lastVerifiedCommitHash |                                              `a714114ef94eedb8042fb4caa38d9469f4767dd6`|
| lastVerifiedCommitDate |                                              2026-08-01T18:06:36+02:00|
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

**`InProcessExclusivityTests` (L152-L349).**
`test_a_second_thread_is_kept_out_of_a_log_that_is_already_held` (L158-L208) runs a holder and a
follower thread and asserts the exact order `["A-holds", "B-refused", "A-leaves", "B-enters"]`.
The ordering half would pass on `flock` alone; the interesting assertion is the
`thread_mutex_for(log).acquire(blocking=False)` probe from a non-holding thread, which asks the
log's own mutex whether the log is claimed. Exceptions are collected into a list and asserted
empty on the main thread rather than swallowed in the worker.
`test_one_mutex_per_log_and_a_different_log_is_a_different_mutex` (L210-L221) pins identity in
both directions — same log, same object; different logs, different objects — because a factory
handing out a fresh lock per call would guard nothing, and one lock shared across logs would
serialise unrelated stores.
`test_taking_a_logs_exclusivity_twice_on_one_thread_does_not_deadlock` (L223-L272) asserts four
things and the absence of a hang is only the first: the nested frame can drive `rewrite_lines`
(so `require_lock_held` sees the hold through the nesting), the **outer** frame still holds after
the inner one exits (a counter that popped instead of restoring would have silently released a
lock its caller believes it holds), and the hold is genuinely gone after the outermost exit —
proven by `require_lock_held` then raising `DurableStoreError`.
`test_a_dismissal_is_not_lost_to_a_prune_sweeping_on_another_thread` (L274-L349) forces the
lost-update pair the dashboard actually runs: the projection sweep is parked at the moment of its
physical write while a dismiss runs on a second thread. Only the write moment is interposed; the
store's own read, filter and commit are the real ones. The final assertion is that **both**
survive — the dead lifecycle's row gone, the kept row still there, and the racing click not
discarded.

**`UnsafeLockFilesystemTests` (L352-L414).**
`test_a_lock_that_does_not_exclude_is_refused_and_names_what_to_fix` (L367-L393) asserts the
message names the lock path, the store, and "NFS, SMB or WSL DrvFs", that the exception is a
`DurableStoreError` so a caller catching the family catches it, and then the two that matter for
durability: the `with` body was never entered (`entered == []`) and **no log was created**.
`test_a_store_refuses_the_append_itself_and_recovers_once_the_lock_works` (L395-L414) drives the
same refusal through `GateStore.append` — an ordinary caller that never mentions locking — and
then repeats the append once `flock` excludes again, so a failed probe is not a latch that
poisons the path for the rest of the process.

**`SchemaVersionMajorTests` (L417-L503).** One rule and the two read policies it decides.
An unknown **major** is refused at the model boundary with a message naming the version and the
contract (L451-L464); an unknown **minor** of the supported major is accepted *and kept* through
the round trip rather than silently restamped (L466-L481). `test_a_future_row_stops_the_authority_
read_and_only_costs_projection_a_tick` (L483-L503) then shows the consequence on one log: the
tolerant `read_for_projection` returns the readable gate, the strict `read` raises, and — the
assertion that keeps tolerance cheap — the log's bytes are unchanged, so the future row is still
there for a build that can read it. `_append_future_major` (L439-L449) builds that row by
re-stamping a real record rather than hand-rolling JSON, so it differs from a valid row in exactly
the field under test.

**`BlankLineToleranceTests` (L506-L549).** A blank line is neither a record nor a torn line, so
**both** readers step over it — asserted on the gate log and the expectation log. Worth stating
precisely because the two policies are otherwise opposite: the strict reader skipping a blank line
is not the tolerance leaking across.

**`OrchestrationNudgeRewriteTests` (L552-L629).** `compact` drops what `keep` rejects and reports
the count, and the survivor is re-serialised whole rather than truncated (L569-L578); a compaction
that keeps everything **does not rewrite at all** and the file stays byte-identical (L580-L590),
because a rewrite that changes nothing still replaces the inode and opens an appender window for
no gain; compacting to nothing leaves an **empty file**, `is_file()` true and `read_bytes() == b""`
(L592-L600). `replace_records` succeeds under a held lock (L602-L611) and refuses an unlocked
caller **while changing nothing** (L613-L629) — the second assertion is the durability property,
since an unlocked rewrite would discard everything appended since the caller's read.

**`FailedRewriteTests` (L632-L708).** The shared `_rewrite_under` helper (L663-L679) asserts, for
every injected failure: the log is byte-identical afterwards, it still reads back as the record it
held, and no `.tmp` remains in the directory. `test_a_failed_rename_removes_the_temp_file_it_had_
already_written` (L681-L694) additionally names the exact pid-scoped path the contract promises,
and `test_an_interrupted_rewrite_cleans_up_too` (L696-L708) raises `KeyboardInterrupt` from the
`fsync` inside the temp write — a different instruction from the rename case — which is why the
production handler catches `BaseException` rather than `Exception`.

**`GateDeleteTests` (L711-L745).** A delete that missed answers `False` **and rewrites nothing**
(bytes unchanged), because rewriting for a call with nothing to do would open the
appender-versus-rewriter window gratuitously; a delete that hit answers `True`, empties the read,
and leaves the log a file.

**`ProcessRoleDeclarationTests` (L748-L792).** `server_module.main` declares the role before
`run_server` is reached — asserted by recording `declared_process_role()` from inside a patched
`run_server`, so the ordering is the property under test rather than the end state. The writer
check is then exercised in both directions: the gate log names `mcp` among its writers and
accepts, supervisor-signals names only the dashboard and raises `CompactionOwnerError`. Because
the declaration is process-global by design, `setUp` registers a cleanup that restores the
previous `durable_store._declared` contents (L753-L762).

### Conventions

**What the mutex is claimed to do, and what it is not.** The module header (L11-L20) states it
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

**The filesystem is faked, never the code.** `_IgnoredFlock` (L111-L128) is `fcntl` as WSL DrvFs
presents it: `flock` accepted and no lock taken; every other name (`LOCK_EX`, `LOCK_NB`,
`LOCK_UN`) forwards untouched through `__getattr__`. It is substituted for `durable_store`'s own
module reference only — so no other thread in the interpreter loses its locks while a test runs —
and the substitution is at the single boundary the capability probe talks to, because
`_verify_lock_capability`'s refusal only fires where a second `flock` on a second description
*succeeds*, which no correctly locking filesystem does and no test can mount. Every assertion in
those tests is on the raised type, the message text, and what is on disk; none is on the
substitution.

**`_FailingOs` (L131-L149) is the same discipline at the `os` boundary.** One named call raises;
`getpid`, `open`, `fsync`, `close` and `O_RDONLY` all forward to the real `os`, so the rewrite
under test is the shipped one everywhere except the one instruction the scenario needs to fail. A
full disk or a crashing rename is not reproducible on demand, which is why the injection exists at
all. In `_rewrite_under` the lock is taken **outside** the substitution (L666-L670) so the failure
under test is the rewrite's and not the lock's.

**`WATCHDOG_SECONDS = 15.0` (L80)** bounds every thread join and event wait, so a wedged lock is
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
- `ProcessRoleDeclarationTests` mutates process-global state (`durable_store._declared`) and must
  restore it; left standing, every later test in the interpreter would claim to be the MCP server
  and `check_declared_writer` would start refusing the dashboard-only stores.
- This file reaches two private names deliberately — `durable_store._declared` and the
  `attention_module.rewrite_lines` patch target. Both are stated in the tests' own docstrings.

### Todos

`test_a_dismissal_is_not_lost_to_a_prune_sweeping_on_another_thread` (L274-L349) proves the
dismisser is excluded with a **timing** assertion: `assertFalse(dismiss_done.wait(0.25))`. The
surrounding structure makes it sound — the sweep holds the lock until `release.set()`, so a
correct implementation cannot finish inside that window — but it is the only assertion in the file
whose failure mode is "the machine was slow" rather than "the property broke", and it is the one
to look at first if this suite ever flakes.

## Docs References

No Domain Documentation source is configured for this repository. The contract asserted here is
declared in this repository, in the front matter of `controlplane/durable_store.py`, and the
platform behaviour the unsafe-filesystem tests reproduce (NFS/SMB byte-range emulation, WSL DrvFs
ignoring `flock`) is stated there rather than cited to an external document.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

Every claim in this file is about a named function in `durable_store.py` or about one of the four
stores that compose them; the rows below are those definitions plus the sibling suites that hold
the cross-process and authority halves.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The contract front matter this file is named after, and the section that separates what prevents loss (the unconditional lock) from what merely documents (advisory ownership). | module front matter; the `WHAT PREVENTS LOSS, AND WHAT MERELY DOCUMENTS` section | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The per-log mutex under test, and its own statement that `flock` already excludes threads so the mutex closes a dependence on the handle rather than a reproducible race. | `thread_mutex_for`; `lock_path_for` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The two-lock acquisition order and the thread-local depth counter the re-entrancy test composes against. | `exclusive_access`; `_LockDepth` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The capability probe `_IgnoredFlock` defeats, and the refusal text asserted verbatim. | `_verify_lock_capability` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The rewrite invariant and the rewrite itself: refuses without the lock, never unlinks, pid-scoped temp, cleanup on `BaseException`. | `require_lock_held`; `rewrite_lines`; `append_line` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The single version rule and the validator that gives the strict and tolerant readers their behaviour without a version branch in either. | `schema_version_supported`; `DurableRecord` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The advisory ownership methods exercised in both directions by the role test, and the two registers it uses. | `check_declared_writer`; `is_compaction_owner`; `GATE_OWNERSHIP`; `SUPERVISOR_SIGNAL_OWNERSHIP` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The one place that declares a process role, asserted to do so before the server serves. | `main` L34-L57, with `declare_process_role("mcp")` at L52 | [mcp/server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The whole-file read-modify-write pair the thread lost-update test forces, and the `rewrite_lines` reference it patches. | `dismiss`; `prune_lifecycles`; `_replace` | [controlplane/attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| The nudge log's two rewrite entry points under test — the safe `compact` and the `replace_records` primitive it wraps. | `compact`; `replace_records`; `_rewrite` | [controlplane/orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py) |
| The gate store's strict and tolerant reads, its `delete`, and the `_replace` that routes both through the contract. | `read`; `read_for_projection`; `delete`; `_replace` | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The cross-process axis of the same contract, which this file's threads deliberately cannot reach. | L1-L26; L97-L168 | [test_controlplane_store_durability.py](agents-remember/mcp/tests/test_controlplane_store_durability.py) |
| The same major/minor rule applied through the same helper to the worktree contract's front matter — one policy rather than two that drift. | `ContractSchemaVersionTests` L84-L145 | [test_worktree_contract_lifecycle.py](agents-remember/mcp/tests/test_worktree_contract_lifecycle.py) |
| The settings fixture this file borrows to build a real MCP config for the role test. | `settings_payload` L29-L88 | [test_config.py](agents-remember/mcp/tests/test_config.py) |

## Cross-Repo References

No meaningful cross-repo references found. The suite imports only `agents_remember`, `pydantic`,
a sibling test fixture and the standard library; the platform behaviour it reproduces is faked at
the `fcntl` boundary rather than reached across a repository or system boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: created the card for the in-process half of the
  `ar-durable-store/1.0` contract. **The mutex is recorded as what the source says it is and not
  as a race fix:** `flock` already excludes two threads of one process (the lock lives on the open
  file description and `exclusive_access` opens a fresh one per non-reentrant acquisition), that
  was measured rather than assumed, and the thread-level lost update was therefore already closed;
  what `thread_mutex_for` (`durable_store.py`) closes is the *dependence of thread
  exclusion on where the handle came from* — cache one lockfile handle on the store, the obvious
  "stop opening two files per append" optimisation, and every thread shares one description,
  `flock` stops excluding, and nothing in the tree fails. The first test (L158-L208) asserts the
  mutex directly via a non-holding thread's `acquire(blocking=False)` probe rather than inferring
  it from an ordering `flock` alone would produce; the re-entrancy test (L223-L272) exists because
  the added mutex is a second lock a thread can hang itself on, and asserts four things beyond the
  absence of a hang. **The unsafe-filesystem tests are recorded as faking the filesystem, not the
  code:** `_IgnoredFlock` (L111-L128) reproduces WSL DrvFs literally — accept the `flock`, take no
  lock — forwards every other `fcntl` name untouched, and is substituted for `durable_store`'s own
  module reference alone so no other thread loses its locks; every assertion is on raised type,
  message text and what is on disk (including that no log was created), none on the substitution.
  `_FailingOs` (L131-L149) applies the same discipline at the `os` boundary, and `_rewrite_under`
  (L663-L679) takes the lock outside the substitution so the failure under test is the rewrite's.
  Also recorded the `schemaVersion` major/minor policy and its consequence on one log
  (L417-L503), the blank-line case that both readers skip (L506-L549), the nudge log's two rewrite
  entry points including the no-op branch that must not replace the inode (L580-L590) and the
  unlocked-caller refusal that must change nothing (L613-L629), failed-rewrite temp cleanup
  including why the handler catches `BaseException` (L696-L708), `GateStore.delete` answering
  honestly without rewriting on a miss (L711-L745), and the role declaration asserted for its
  **ordering** by recording `declared_process_role()` from inside a patched `run_server`
  (L748-L792). **Filed one Todo:** the thread lost-update test's exclusion proof is a 0.25 s
  `assertFalse(dismiss_done.wait(...))` — sound given the sweep holds the lock until released, but
  the only assertion in the file whose failure mode is a slow machine. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is
  blank because the source file is new and uncommitted; closeout owns its first stamp.
