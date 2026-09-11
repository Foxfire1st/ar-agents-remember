# mcp/src/agents_remember/controlplane/durable_store.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/controlplane/durable_store.py`   |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated | 2026-09-07T00:42+02:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview      | `overview.md`                                             |

## Governing Overview

[overview.md](overview.md)

## Purpose

`durable_store.py` declares `ar-durable-store/1.0`, the common record, ownership and I/O contract for six control-plane JSONL stores. It owns schema validation, advisory writer/compaction policy, guarded access, durable appends, and the requirement to hold a log lock across read-filter-rewrite. Mechanical file exclusion belongs to `kernel.file_lock`; atomic temp publication belongs to `kernel.atomic_write`.

This concentration was introduced after independent store implementations lost whole records through unprotected read-modify-write and unlink races. Reader validation could not recover records that never remained in the log. The historical evidence account below remains separate from the current owner map.

## Code Commentary

### Historical 260731-EFA-L5 Evidence Account

The original curation recorded base-commit rates as historical source claims, not retained run artifacts. The detailed historical module docstring has since been reduced to the current contract, so the rates below are preserved as earlier observations; they are not claims that the present docstring contains those measurements. The original account and its qualification remain in Update History. The current harness sensitivity and durability assertions remain separately checkable.

| Store                | Historical base-commit loss attribution                      | Compaction owner declared here |
| --- | --- | --- |
| attention-dismissals | 31.45 percent — corroborated at four sites (the historical docstring, `agent_notifier_signals.py`, `test_durable_store_contract.py`, `test_observer_projection.py`). The "127 of 2000 writes raising `FileNotFoundError`" beside it is the historical docstring only | dashboard |
| gate                 | 11.50 percent — corroborated at three sites (the historical docstring, `store.py`, `test_interaction_retention.py`). The "100 percent in the forced-window scenario" beside it is `store.py` only, but see the note below: that one is asserted by a test | mcp |
| supervisor-signals   | 10.50 percent — the historical docstring only                           | dashboard |
| expectation-rows     | 10.20 percent — the historical docstring only                           | dashboard |
| orchestration-nudges | 9.20 percent — the historical docstring only                            | dashboard |
| operator-inbox       | 0.00 percent — the historical docstring only; it already held a lock    | none, the declared exception |

**The one base-commit fact a reader can check in one step** is not a rate:
`test_controlplane_store_durability.py::HarnessSensitivityTests::test_the_forced_scenario_detects_loss_in_the_base_commit`
`git archive`s `e52edaf5` and asserts `lost == 1` for each of the five unlocked stores in
`forced_lost_update`, and `0` for operator-inbox. That the scenario attempts exactly one record is
structural (`run_forced_lost_update` forces a single append into the read-to-replace window) and is
pinned against the current tree by `MultiProcessDurabilityTests`' `attempted == 1`, so the gate
row's "100 percent in the forced window" is that assertion read as a rate. It is also what proves
the harness measures the defect rather than something else.

**Against the current tree**, `test_controlplane_store_durability.py::MultiProcessDurabilityTests`
asserts less than "all six stores", and both narrowings matter. `lost == 0` (with
`stragglers == []`) holds in all three scenarios — but over six stores in `forced_lost_update` and
`stress`, and over **five** in `forced_unlink`, which runs over `APPEND_CASES`. Attention-dismissals
is excluded there by construction: it has no `append` at all, so it cannot be stranded in an
unlinked inode, and its lost-update exposure is covered by the first scenario instead.
`torn_lines == 0` is asserted in the **`stress` scenario only**, as are `append_error_count == 0`
and `reclaim_error_count == 0` — the latter two in their own stress run against their own root, with
the "the run actually happened" guards repeated so a zero is never reported over zero write calls.

The store that looked safest was the worst, and the reason is worth keeping. Attention-dismissals
has a single writer, so an earlier draft of this leaf left it unlocked on exactly that ground. But
`AttentionDismissalStore.dismiss` is a whole-file read-modify-write, not an append, and it is
reached from the dashboard's HTTP dismiss route through the serving HTTP dismiss route. Two concurrent dismisses
therefore lose each other with **no compactor involved and no second writer required**. That is why
`StoreOwnership` deliberately has no `serialized` field: "only one process writes this file" is a
deployment fact, not a structural one.

### Logic

**The contract identity.** `DURABLE_STORE_CONTRACT` is the literal `ar-durable-store/1.0`.
`SCHEMA_VERSION` is the `MAJOR.MINOR` string stamped on every record; `SUPPORTED_SCHEMA_MAJOR` is
`1`. `schema_version_supported(value)` splits on the dot and compares the major for **equality**
with `SUPPORTED_SCHEMA_MAJOR` — not `<=`. Unknown means "not this one" in both directions, so
`"0.9"` is refused exactly as `"2.0"` is, and an unparseable version is refused outright.
`worktrees/worktree_contract.py` imports the same constant and the same predicate, so the tree has
one version policy rather than two that can drift.

Equality rather than `<=` is settled, and the reason is what makes it safe to keep: nothing in this
tree has ever written a 0.x record. `SCHEMA_VERSION` has been `1.0` since the contract existed and a
record with no version field defaults to it, so a row claiming a 0.x major is corruption or a
foreign artifact rather than an older record of ours — the same reason to refuse it as `"2.0"`, that
the record says it means something this code was not written to interpret. If a major 0 format is
ever genuinely introduced, accepting it is a deliberate change here plus the migration to go with
it, not a comparison operator that already quietly said yes.

**`DurableRecord`** is the pydantic base all six record types inherit. It carries
`model_config = ConfigDict(extra="forbid")` (previously repeated in each of the six) and a
`schemaVersion` field validated on the way in. This is the whole mechanism behind the two read
policies: an unknown major raises `ValidationError` at parse time, so a strict reader surfaces it
and a tolerant reader skips the row, and **no reader anywhere contains a version branch**. Verified
directly against all six record classes: minor `1.99` accepted, major `2.0` rejected, `banana`
rejected. Undo the validator and every reader silently accepts a record it cannot be trusted to
interpret.

**Process role and checkout execution.** `ProcessRole` includes `mcp`, `dashboard`, and `lifecycle-operation`; compaction ownership remains `mcp`/`dashboard`. `declare_process_role` delegates execution-mode state to `kernel.primitives.checkout_coordination`, and `declared_process_role` narrows that state to those three shared-store writer roles. Explicit test mode and an undeclared CLI return `None`. Declarations belong to actual process entry points: MCP, the dashboard foreground/reload worker, and the detached lifecycle-operation worker. Factories invoked in-process do not impersonate those processes.

The dashboard `_dev_app` reload factory declares its actual worker role; the reason for that special entry point was recorded in the earlier incident review. `--reload` serves the app from a
uvicorn reload worker, and uvicorn 0.49.0 starts that worker through
`multiprocessing.get_context("spawn")`; a spawn child re-imports this module, so it begins with an
**empty declaration dict** and never runs `run`. Measured before the fix: the reload worker read as
"declared nothing", therefore answered `True` to `is_compaction_owner` for **every** log, and so a
`--reload` dashboard ran the gate reclaim a foreground dashboard deliberately skips.

Record that at the right weight: it is an **ownership gap, not a durability defect**. The per-log
lock is unconditional and covered the rewrite throughout, so no record was ever at risk. What broke
was the stated reason for the undeclared-is-owner default — and the fix was to make the reload
worker declare rather than to invert the default, because inverting it would have turned the
predicate `False` in every process that legitimately declares nothing (every CLI invocation, every
script, the whole test suite) and left gate logs nobody reclaims. `_dev_app` can carry a declaration
that `create_app` cannot because it is reload-only: it reads its config from
`AR_DASHBOARD_DEV_CONFIG` and refuses `--sim`. Foreground, `--daemon` and `--reload` now agree about
what the process is.

**`StoreOwnership`** is a frozen dataclass naming, per log, the measured `writers` set, the single
`compaction_owner` (or `None`), and a prose `rationale`. Two methods, and their difference is the
load-bearing part of this module:

- `check_declared_writer()` **raises** `CompactionOwnerError` — but only in a process that declared
  a role, and only when that role is not in the log's `writers`. It is silent in every CLI
  invocation, script and test.
- `is_compaction_owner()` is a **question that never raises**. It returns `True` in a process that
  declared nothing and `True` for a store whose `compaction_owner` is `None`.

**The ownership register** holds all six constants side by side so the differences are comparable:
`GATE_OWNERSHIP`, `EXPECTATION_ROW_OWNERSHIP`, `ATTENTION_DISMISSAL_OWNERSHIP`,
`OPERATOR_INBOX_OWNERSHIP`, `ORCHESTRATION_NUDGE_OWNERSHIP`, `AGENT_NOTIFIER_SIGNAL_OWNERSHIP`. Four
logs accept MCP and dashboard writers; gate also accepts the detached lifecycle-operation writer. Attention-dismissals and supervisor-signals accept the dashboard alone. Locking is *not* one of the differences — all six lock, always.

**Checkout target containment precedes locking.** `exclusive_access`, `append_line`, and
`rewrite_lines` all call `require_durable_write_target`. In an undeclared linked checkout, the only
allowed targets are the leaf's `provider-runtime/dev-ar-coordination` for coordinator rows and its enclosure `reports/` for operational artifacts; an escape raises before the target parent or lockfile exists. Declared MCP/dashboard/lifecycle-operation and explicit test execution follow their actual declaration policy. This is the second half of checkout isolation: synthetic runtime config routes normal
CLI construction, while this I/O choke point refuses a manually constructed live log path.

**The locking primitive and policy boundary.** `exclusive_access(log, ownership)` first calls `checkout_coordination.require_durable_write_target`, before the kernel can create the lock parent. It then delegates to `kernel.file_lock.exclusive_file_lock`, whose single owner provides `lock_path_for`, `thread_mutex_for`, `_LockDepth`, capability probing and hold inspection. The kernel holds the mutex before `flock`, nests only on the same thread, and raises `LockCapabilityError` when the double-open probe does not exclude. This adapter translates that failure to `UnsafeLockFilesystemError` without changing the durable-store error contract. `require_lock_held` asks the kernel for the calling thread's hold and refuses an unlocked rewrite.

Host Dagger registry ownership uses the same kernel mechanics through its own `AuthorityRegistry.exclusive_access`; it does not pass host paths through this coordinator policy or declare a trusted process role. No compatibility alias for the moved lock helpers remains here.

**The I/O.** `read_log_text` returns raw UTF-8 text or `""` when absent. `append_line` and `append_lines` authorize the target, append under the caller's held lock and fsync before closing; the batched helper performs one flush/fsync for the batch. `rewrite_lines` authorizes the target and requires the hold, then delegates to `atomic_write_text`. Its kernel owner writes a hidden per-call pid-and-UUID temp, fsyncs it, replaces the destination, then fsyncs the directory on POSIX. Empty content remains an empty file; the destination is never unlinked.

`migrate_jsonl_records` is a bounded explicit migration: transform each raw JSON object, validate all records before replacement, and rewrite only if at least one record changes. It is not a parallel permissive reader.

### The Lock Is The Mechanism, Ownership Is Advisory

The contract keeps the distinction between serialization and advisory ownership explicit:

- **The lock is unconditional.** Every append and every rewrite of every one of the six logs takes
  that log's lock, in every process, whether or not that process declared anything. There is no
  flag that turns it off and no store exempt from it. The `serialized` opt-out an earlier draft
  carried was deleted. This is what took the measured loss to zero.
- **Ownership is advisory and opt-in.** `check_declared_writer` raises only for a declared shared-store writer;
  `is_compaction_owner` never raises at all. Where ownership does real work it does it
  *structurally*, by moving code: the projection tick no longer rewrites a gate log, and the shared
  decide path asks before reclaiming.

`require_lock_held` is the exception that proves the rule — it **does** raise, from inside
`rewrite_lines`, so no store can rewrite a log it has not locked however the call was reached. It
can afford to raise because it asks about the calling thread's own lock rather than about a
process-wide declaration, so it is true or false for real in every process, test hosts included.

### The Two Read Policies, And What Makes Them Safe Rather Than Merely Different

The split is deliberate and must not be filed as an inconsistency.

- **Strict, for authority.** A torn line raises. Silently skipping a malformed record in the gate
  enforcement fold could drop an `applied` marker, and the fold would conclude the approval was
  never consumed — re-opening the replay window a human approval exists to close.
- **Tolerant, for projection.** The dashboard tick must degrade, not crash: one unparseable row
  must not 500 an endpoint or freeze the fleet-wide projection. A tolerant read never writes back
  what it read, so a skipped line is skipped for the duration of one tick.

By store: gate, expectation-rows and operator-inbox are the strict three (their rows change a
decision); attention-dismissals, orchestration-nudges and supervisor-signals are the tolerant three
(their rows only render or rate-limit). Gate **and** expectation-rows additionally expose a
projection-only tolerant reader alongside the strict one — `GateStore.read_for_projection` and
`ExpectationRowStore.read_for_projection` / `pending_for_projection` — used by
`observer/snapshots.py` and by nothing that decides.

**Every rewrite of an authority-bearing log reads strictly**, and that is the property that makes
two policies safe rather than merely different: a compaction can never be the thing that erases a
record it could not parse. Stated exactly, because the code is more specific than the slogan: each
of the three strict stores drives its rewrites from its strict `read`, and each of the three
tolerant stores drives its rewrites from its tolerant `read`. The tolerant three therefore *do*
drop an unparseable row on compaction — which is safe only because none of them carries authority,
and would stop being safe the moment one of them did.

### The Process-Wide Mutex — What It Adds And What It Does Not

The kernel-owned `thread_mutex_for` supplies a second lock taken before the flock, and the contract is careful about the
claim, as this card must be. **It does not fix an existing thread race.** A worker measured that
`flock` already serialises two threads of one process on POSIX: the lock lives on the open file
description and `exclusive_access` opens a fresh description on every non-reentrant acquisition, so
thread B blocks on thread A exactly as a second process would. The same property is what
`_verify_lock_capability` depends on to probe the filesystem at all.

What the mutex closes is that the thread-level exclusion rested on *where the handle came from*
rather than on anything the contract declared. Cache one lockfile handle on the store — the obvious
"stop opening two files per append" optimisation — and every thread would share one file
description, `flock` would silently stop excluding them, and nothing in the tree would fail. That
regression was simulated and does lose records without the mutex. So the mutex defends a specific
plausible future change, not a reproducible loss today, and describing it otherwise would be a
false claim.

The mutex is an `RLock` because `exclusive_access` already spends a thread-local depth counter
tolerating re-entry (a nested `flock` on a second file description would deadlock a thread against
itself), and pairing that with a non-re-entrant mutex would put the deadlock back one layer down
where the counter cannot reach it. The nested acquisition returns before either lock is touched, so
the outermost frame owns the mutex for the whole nest.

### The Ordering Of The Two Locks

Mutex first, flock inside it, always. Taking the flock first would leave a thread holding a lock
every other *process* waits on while it queues behind a thread of its own, and it would put the
once-per-path capability probe — which takes that same flock twice — behind a hold this process
already has.

### The Ordering Across Stores (260731-EFA-L16)

The intra-store order above is not sufficient. `exclusive_access`'s docstring now declares ONE
ORDER ACROSS STORES, TOO: no thread may hold one store's lock — mutex, RLock, or flock — while
acquiring another store's lock. Evidence a transaction needs from a second store is gathered
BEFORE entering this one, or the side effect runs AFTER leaving it; never nested. The two nestings
this rule forbids were each locally documented and locally defensible: the liveness sweep held the
catalog batch lock across the hosted-interaction synchronizer's operator-inbox/gate acquisitions
(260718-CHATS-L5 had quarantined that call's failure mode, not its placement), and the
agent-notifier's lock-held reconcile read the catalog under the inbox lock (260712-TRH-L5's
"intentionally held across catalog/tmux evidence"). On 2026-08-05 the two deadlocked ABBA in
production, twice and py-spy-verified, and the uvicorn event loop then queued on the same catalog
RLock via async endpoints doing synchronous catalog reads, so the daemon stopped accepting. Both
nestings are un-nested now — `terminal_liveness` defers the synchronizer to after the batch
commit, the supervisor pre-fetches the catalog before the inbox transaction — and
`mcp/tests/test_cross_store_lock_order.py` pins the rule with a placement property and a
rendezvous-parked ABBA reproduction over the real sweeps.

### Capability, Enforced At The Shared Owner

The kernel's double-open probe checks actual exclusion on each lock path instead of inferring safety from a mount name. If the second file description can acquire the same exclusive lock, this adapter raises `UnsafeLockFilesystemError`. The diagnostic names NFS, SMB and WSL DrvFs as the unsupported examples in the implementation; this card does not establish a universal claim about every mount or platform configuration. The check proves the required exclusion behavior on the probed path, not the physical number of hosts.

### Conventions

- One rewrite entry point, with the log's lock held unbroken across the read, the filter **and** the
  rewrite. That invariant holds in all six stores. The *code shape* it is written in does not, so do
  not read the shape as the rule — this was checked store by store rather than taken from the
  module's own summary. Three stores use a named locked half: `ExpectationRowStore.compact` →
  `_compact_locked`, `AgentNotifierSignalCooldownStore.compact` → `_compact_locked`, and
  `AttentionDismissalStore.prune_lifecycles` → `_prune_locked`. The other three inline the read, the
  filter and the rewrite in one method body under a single `exclusive_access`: `GateStore.compact`
  and `GateStore.delete`, `OrchestrationNudgeStore.compact`, and every `OperatorInboxStore` rewrite
  (which is the near miss — it has `_read_unlocked` and `_replace_unlocked` halves, but filters
  between them in the public method). Even the split store splits only one of its two rewrites:
  `AttentionDismissalStore.dismiss` inlines. What must never happen is locking the write half alone:
  that looks safe and loses records, and `require_lock_held` is where it is caught.
- Errors are a small tree rooted at `DurableStoreError(RuntimeError)`, with `CompactionOwnerError`
  and `UnsafeLockFilesystemError` beneath it. None is ever downgraded to a warning or a no-op.
- Atomic publication owns hidden pid-and-UUID temp names (`.<log>.<pid>.<uuid>.tmp`), so calls use distinct temporary paths and the watcher skips them through its dot-prefix and `.tmp` filters.
- The lockfiles are kept out of the projection watch by a **derived** rule, not a name list.
  `serving/change_watcher.py` computes
  `_DURABLE_LOG_LOCK_SUFFIX = lock_path_for(Path("log.jsonl")).name.removeprefix("log")` and drops
  any watched basename ending in it, in every watched directory. Deriving the suffix from
  `lock_path_for` is what keeps the filter in step when a lockfile is renamed — the literal
  `"operator-inbox.lock"` this replaced had silently stopped matching anything once `lock_path_for`
  moved to `operator-inbox.jsonl.lock`. Matching by suffix rather than by basename is what a list
  structurally could not do: five of the six logs live only under `workspace/`, but `gates.jsonl`
  lives there **and** once per lifecycle, so `gates.jsonl.lock` appears in every lifecycle directory
  too. No projection input is named `*.jsonl.lock` — the inputs are the `.jsonl` logs themselves and
  their `.json` sidecars — so the suffix rule cannot over-match.
- Schema interpretation remains one explicit major-version rule. `migrate_jsonl_records` performs bounded, fully validated migrations under the existing log lock; it does not silently accept an unsupported record schema.

### Invariants And Boundaries

- **Unconditional locking.** Every append and every rewrite of every one of the six logs holds that
  log's lock. Add a store, a writer or a code path that skips it and the lost-update window this
  module was created to close re-opens silently.
- **The lock is held across the read AND the rewrite.** A record list chosen by a read that
  happened outside the lock is already stale, and rewriting from it is the same lost update under
  a different name. `require_lock_held` is the one place this is checked rather than remembered.
- **`rewrite_lines` never unlinks.** An empty kept set is an empty file. The old `unlink` on empty
  let a concurrent appender holding an `"a"`-mode handle write into an inode with no remaining
  links — the record vanished with no torn line and no trace.
- **Ownership never decides whether to lock.** `exclusive_access` takes an `ownership` argument
  only to name the log in the refusal when the filesystem turns out not to support locking.
- **One compaction owner per log, with one declared exception.** operator-inbox carries
  `compaction_owner=None` because both processes must physically remove rows and neither move
  travels without the decision it implements.
- This module owns coordinator write policy, durable I/O composition and the record base class. Kernel owners provide exclusion and atomic publication. It owns no record
  vocabulary, no retention policy and no MCP surface; those stay in the per-store modules and in
  `interaction_retention.py`.

### Todos

The earlier Todo about `thread_mutex_for` claiming that all six stores split reclaim into named locked halves is obsolete: the helper moved to the shared kernel and its current docstring no longer makes that claim. The invariant is uninterrupted exclusion across read-filter-rewrite, independent of method shape.

## Docs References

No external Domain Documentation source is configured. The current contract is repository-owned; historical observations above remain qualified historical provenance.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain documentation source. | N/A | N/A |

## Repo-Internal References

The current owner map is verified against the prepared source. Kernel mechanics, coordinator authorization, and caller-specific host registry policy are separate.

| Finding | Anchor | Source |
| --- | --- | --- |
| Current writer declaration, advisory ownership and compaction roles. | `declare_process_role`; `declared_process_role`; `StoreOwnership` | mcp/src/agents_remember/controlplane/durable_store.py:79-88; mcp/src/agents_remember/controlplane/durable_store.py:91-95; mcp/src/agents_remember/controlplane/durable_store.py:98-138 |
| Major equality and validated record base; tolerant rewrite policy is declared in the module front matter. | `schema_version_supported`; `DurableRecord` | mcp/src/agents_remember/controlplane/durable_store.py:232-253; mcp/src/agents_remember/controlplane/durable_store.py:256-279 |
| Guarded coordinator entry translates the shared capability failure. | `exclusive_access` | mcp/src/agents_remember/controlplane/durable_store.py:319-360 |
| The kernel owns lock naming, thread mutexes, nesting, capability and hold observation. | `lock_path_for`; `thread_mutex_for`; `_LockDepth`; `_verify_lock_capability`; `exclusive_file_lock`; `lock_held` | mcp/src/agents_remember/kernel/file_lock.py:36-38; mcp/src/agents_remember/kernel/file_lock.py:41-55; mcp/src/agents_remember/kernel/file_lock.py:19-27; mcp/src/agents_remember/kernel/file_lock.py:58-84; mcp/src/agents_remember/kernel/file_lock.py:87-114; mcp/src/agents_remember/kernel/file_lock.py:117-119 |
| Rewrite refuses without a hold; append and rewrite targets retain containment. | `require_lock_held`; `_prepare_append_target`; `_require_rewrite_access` | mcp/src/agents_remember/controlplane/durable_store.py:363-381; mcp/src/agents_remember/controlplane/durable_store.py:431-433; mcp/src/agents_remember/controlplane/durable_store.py:436-438 |
| Current raw read, single/batched durable append and atomic rewrite. | `read_log_text`; `append_line`; `append_lines`; `rewrite_lines` | mcp/src/agents_remember/controlplane/durable_store.py:384-388; mcp/src/agents_remember/controlplane/durable_store.py:391-402; mcp/src/agents_remember/controlplane/durable_store.py:405-418; mcp/src/agents_remember/controlplane/durable_store.py:421-428 |
| Explicit migration validates every transformed record before replacement. | `migrate_jsonl_records` | mcp/src/agents_remember/controlplane/durable_store.py:282-316 |
| Per-call temporary names and atomic publication have one kernel owner. | `_temp_path_for`; `atomic_write_bytes`; `atomic_write_text`; `_fsync_directory` | mcp/src/agents_remember/kernel/atomic_write.py:21-29; mcp/src/agents_remember/kernel/atomic_write.py:51-70; mcp/src/agents_remember/kernel/atomic_write.py:73-75; mcp/src/agents_remember/kernel/atomic_write.py:32-48 |
| The host registry has its own domain policy over the same exclusion primitive. | `AuthorityRegistry` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-846 |
| Watcher exclusion derives the shared lock suffix and filters every directory. | `is_projection_input_event` | mcp/src/agents_remember/serving/change_watcher.py:189-207 |
| Undeclared host admission leaves live coordinator lock and append writes refused. | `test_host_admission_keeps_undeclared_checkout_coordinator_writes_refused` | mcp/tests/test_dagger_registry_lock.py:89-114 |

## Cross-Repo References

No meaningful cross-repo references found. This contract governs one package inside this
repository; nothing outside it reads these logs.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## 260815-DAG-L3 Detached Writer Census

`lifecycle-operation` is now an explicit shared-store writer role, distinct from the MCP/dashboard
compaction roles. Detached workers declare that execution mode and are admitted only to stores
whose ownership record includes them; the gate and lifecycle-operation/queue paths therefore no
longer rely on the earlier undeclared-process bypass.


## Update History
- 2026-09-07T00:42+02:00 — Removed remaining obsolete suite-proof citations; current production invariants and historical records remain preserved.

- 2026-09-06T22:41:21+00:00: Generated citation repair: `test_host_admission_keeps_undeclared_checkout_coordinator_writes_refused` repointed to mcp/tests/test_dagger_registry_lock.py:89-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.



- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Reconciled the shared kernel lock extraction, retained guard-before-filesystem ordering and error translation, corrected current writer and atomic-publication ownership, repaired source references, and preserved qualified incident provenance and prior history.


- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 bounded local type-parameter migration in `migrate_jsonl_records` and confirmed that durable-record migration semantics remain as documented. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: added the lifecycle-operation writer role and
  separated writer identity from compaction ownership; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current control-plane card for `durable_store.py` with plane-owned seat identity, routing, and enforcement boundaries.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21: process declaration moved to the kernel checkout-policy
  owner; lock, append, and rewrite primitives now fail closed against live/outside targets for
  undeclared linked-checkout code before creating filesystem state. Verification metadata remains
  pinned until approved closeout.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T19:26+02:00 — 260731-EFA-L16 curator: recorded the cross-store lock-order doctrine
  (`exclusive_access` docstring: ONE ORDER ACROSS STORES, TOO — evidence before entry, side effects
  after exit, never nested) next to the intra-store ordering, with the 2026-08-05 ABBA incident
  provenance (two py-spy-verified production deadlocks; the event loop parked on the catalog
  RLock). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-03T10:05+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 13 live citation findings (6 missing anchors, 6 malformed sources, and 1 duplicate source; the duplicate was live-only drift beyond the 12-item manifest); final scoped check is clean.

- 2026-08-01T19:10+02:00 — Measured-claim repair, confined to the defect section; the contract,
  lock/ownership, read-policy and reclaim prose was not touched, because the 18:45 pass had it right.
  The section opened "Ten runs per store at the base commit… Zero torn lines in every run… After the
  contract landed: 0 lost, 0 raised, 0 torn, all six stores, all scenarios", and the loss column was
  headed "Measured loss at the base commit" — all of it asserted as findings a reader could check.
  **Nothing in the tree lets a reader check any of it:** no base-commit measurement artifact is
  committed, `_store_durability.py::main` can write a JSON payload but none is stored, no test
  asserts a rate, and no committed test invocation even passes `runs`. That is now said once, at the
  top of the section. The rates are split by corroboration: 31.45 percent (four sites) and 11.50
  percent (three) are quoted plainly on the sources' authority; 10.50 / 10.20 / 9.20 / 0.00 percent,
  "127 of 2000", "ten runs per store" and the whole-not-torn property exist only in this file's own
  module docstring, which is the text this card documents, and are attributed to it. **The post-fix
  claim was wrong in both directions and is corrected against the test source, with the class named
  so the next reader gets there in one step.** `MultiProcessDurabilityTests` asserts `lost == 0` in
  all three scenarios but over *five* stores in `forced_unlink` (it iterates `APPEND_CASES`;
  attention-dismissals has no `append`, so it is excluded by construction) and six in the other two;
  `torn_lines == 0`, `append_error_count == 0` and `reclaim_error_count == 0` are asserted in the
  `stress` scenario only. Added the one base-commit fact that *is* checkable —
  `HarnessSensitivityTests` `git archive`s `e52edaf5` and asserts 1-of-1 loss for each unlocked store
  and 0 for operator-inbox — which is also the only support for `store.py`'s "100 percent in the
  forced-window scenario". Section heading renamed accordingly; no citation into `durable_store.py`
  gained a line number. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` left blank, as closeout owns
  them.
- 2026-08-01T18:45+02:00 — Citation and accuracy repair; no prose about the read-policy split, the
  mutex or the lock ordering was changed, because it was right. Converted every citation into
  `durable_store.py` to symbol-name and docstring-heading form with no line range: the file grew
  598 → 699 lines mid-leaf and thirteen of the fourteen rows pointing into it had drifted onto
  other symbols, one claiming to show the six-store ownership register while covering only
  `GATE_OWNERSHIP`. Added the previously uncited `DO NOT GENERALISE "EVERY REWRITE READS STRICTLY"
  TO ALL SIX` block, which this card's body already paraphrased. Corrected three false statements
  about the code: the `declare_process_role` callers are three, not two (`mcp/server.py` `main`,
  `cli/dashboard.py` `run` and `_dev_app`), with `_dev_app` recorded as the deliberate exception
  and the only factory that declares, and the uvicorn spawn-child reload worker recorded at its
  measured weight — an ownership gap, not a durability defect, since the unconditional lock always
  covered the write; `schema_version_supported` now compares the major for equality and refuses
  `"0.9"`, so the Todo claiming it accepts `0.x` is gone and the settled rule is recorded instead;
  and `serving/change_watcher.py` derives `_DURABLE_LOG_LOCK_SUFFIX` from `lock_path_for` and
  matches by suffix in every watched directory, so the Todo and the reference row claiming it still
  names `operator-inbox.lock` are both gone and the derivation is recorded. Restated the
  reclaim-splitting convention against what the six stores actually do — three use a named locked
  half, three inline read, filter and rewrite under one `exclusive_access` — and filed the one
  remaining Todo, that `thread_mutex_for`'s docstring claims all six split. Blanked
  `lastVerifiedCommitHash` and `lastVerifiedCommitDate`, which closeout owns and which the four
  sibling test cards correctly leave empty.
- 2026-08-01T18:30+02:00 — Created for 260731-EFA-L5 (durable store integrity): the new
  `ar-durable-store/1.0` contract module every control-plane JSONL store now routes its file I/O
  through. Recorded the unconditional per-log lock as the mechanism and ownership as advisory
  (`check_declared_writer` raises only inside a declared process, `is_compaction_owner` never
  raises, `require_lock_held` raises from `rewrite_lines` about the calling thread's own lock); the
  six-store ownership register including the operator-inbox `compaction_owner=None` exception; the
  deletion of the `serialized` opt-out and the 31.45 percent an unlocked single-writer draft
  measured; `rewrite_lines` never unlinking; the strict/tolerant read split with the
  rewrite-reads-strictly property stated per store rather than as a blanket; and the process-wide
  `RLock` described as defending a simulated regression rather than fixing an existing thread race.
