# mcp/src/agents_remember/controlplane/durable_store.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/controlplane/durable_store.py`   |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-08-01T19:10+02:00                                    |
| lastVerifiedCommitHash |                                                           `1c1629fc97dd4daf352cf9b3529d210be167d2af`|
| lastVerifiedCommitDate |                                                           2026-08-08T22:29:45+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[overview.md](overview.md)

## Purpose

`durable_store.py` declares `ar-durable-store/1.0`, the one contract the six control-plane JSONL
stores implement, and owns every byte of their file I/O. Before this leaf the six were written
independently against the same shape and their safety properties were distributed almost at
random: one of six took a lock, three of six used a pid-scoped temp name, none fsynced. Records
were lost whole — never torn — so no reader-side validation could have detected it, and the caller
was told the write succeeded. This module is where "how a control-plane log behaves on disk"
stopped being six separate accidents and became one declared contract with a literal
`CONTRACT FRONT MATTER` block at its head.

The point of concentration is checkable: after this leaf the whole `controlplane/` package
contains exactly one `open("a", ...)` append, one `os.replace`, one temp-path construction and one
`import fcntl`, and all four are in this file.

## Code Commentary

### 260731-EFA-L5 The Defect, And What Of It A Reader Can Check

**No base-commit measurement artifact is committed anywhere in this tree.** The harness
(`mcp/tests/_store_durability.py`) can be re-pointed at a `git archive` of `e52edaf5` and its `main`
can write a JSON payload, but no such file is committed, no test asserts a rate, and no committed
test invocation passes `runs` at all — so every base-commit rate in the table below is checkable
only as "the source says so", and the source is this file's own module docstring. Two of the rates
are carried at several independent sites and are quoted on that authority; the rest are single-site
and are attributed rather than restated. "Ten runs per store" and "records disappeared whole, never
torn" have the same single-site standing.

| Store                | Base-commit loss as the sources state it                      | Compaction owner declared here |
| --- | --- | --- |
| attention-dismissals | 31.45 percent — corroborated at four sites (this docstring, `agent_notifier_signals.py`, `test_durable_store_contract.py`, `test_observer_projection.py`). The "127 of 2000 writes raising `FileNotFoundError`" beside it is this docstring only | dashboard |
| gate                 | 11.50 percent — corroborated at three sites (this docstring, `store.py`, `test_interaction_retention.py`). The "100 percent in the forced-window scenario" beside it is `store.py` only, but see the note below: that one is asserted by a test | mcp |
| supervisor-signals   | 10.50 percent — this docstring only                           | dashboard |
| expectation-rows     | 10.20 percent — this docstring only                           | dashboard |
| orchestration-nudges | 9.20 percent — this docstring only                            | dashboard |
| operator-inbox       | 0.00 percent — this docstring only; it already held a lock    | none, the declared exception |

**The one base-commit fact a reader can check in one step** is not a rate:
`test_controlplane_store_durability.py::HarnessSensitivityTests::test_the_forced_scenario_detects_loss_in_the_base_commit`
`git archive`s `e52edaf5` and asserts `lost == 1` for each of the five unlocked stores in
`forced_lost_update`, and `0` for operator-inbox. That the scenario attempts exactly one record is
structural (`run_forced_lost_update` forces a single append into the read-to-replace window) and is
pinned against the current tree by `MultiProcessDurabilityTests`' `attempted == 1`, so the gate
row's "100 percent in the forced window" is that assertion read as a rate. It is also what proves
the harness measures the defect rather than something else.

**Against the current tree**, `test_controlplane_store_durability.py::MultiProcessDurabilityTests`
asserts less than "all six stores, all scenarios", and both narrowings matter. `lost == 0` (with
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
reached from the dashboard's HTTP dismiss route at `serving/app.py:1164`. Two concurrent dismisses
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

**Process role.** `ProcessRole` is the two long-lived writers, mcp and dashboard.
`declare_process_role(role)` is called once at a process entry point and `declared_process_role()`
reports it, or `None` for a CLI invocation, script or test that declared nothing. There are exactly
**three** callers, and together they cover the two long-lived processes in all their launch modes:
`mcp/server.py` `main`, `cli/dashboard.py` `run`, and `cli/dashboard.py` `_dev_app`. The first two
sit at the true process entry point rather than inside `create_server` / `create_app`, which the
test suite calls in-process — declaring there would stamp a role onto every later test in the same
interpreter.

`_dev_app` is what the module itself calls "the deliberate exception and the only factory that
declares", and the reason was measured rather than inferred. `--reload` serves the app from a
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
`OPERATOR_INBOX_OWNERSHIP`, `ORCHESTRATION_NUDGE_OWNERSHIP`, `SUPERVISOR_SIGNAL_OWNERSHIP`. Four
logs accept both processes as writers; attention-dismissals and supervisor-signals accept the
dashboard alone. Locking is *not* one of the differences — all six lock, always.

**The locking primitives.** `lock_path_for(log)` is the sibling lockfile, named after the log.
`thread_mutex_for(log)` returns the per-log process-wide `RLock`, created once under a registry
lock so two threads reaching an unseen log get the same object. `_LockDepth` is a
`threading.local` nesting counter — per-thread and required to be, because `flock` is held by an
open file description, so two threads that each open the lockfile genuinely exclude one another
and a shared counter would let the second thread skip a lock it does not hold.
`_verify_lock_capability(path, store)` proves once per lockfile that `flock` on that path really
excludes, by taking it twice from two file descriptions in this one process; a success means the
lock is decorative and raises `UnsafeLockFilesystemError`. `exclusive_access(log, ownership)` is
the context manager every append and every rewrite passes through: **mutex first, then the flock**,
never the other order. `require_lock_held(log, store)` refuses a rewrite whose calling thread does
not hold the log's lock.

**The I/O.** `read_log_text(log)` returns the raw text or `""` when absent — the one read both
policies share. `append_line(log, line)` writes one record and `fsync`s before the handle closes.
`rewrite_lines(log, lines, ownership)` is the only destructive rewrite in the control plane: it
calls `require_lock_held` first, **never unlinks** (an empty record set is an empty file), builds a
pid-scoped hidden temp name, fsyncs the temp, `os.replace`s it, then fsyncs the parent directory so
the rename either happened or did not.

### The Lock Is The Mechanism, Ownership Is Advisory

The module states this under its own heading, `WHAT PREVENTS LOSS, AND WHAT MERELY DOCUMENTS`, and
the distinction must not blur when this card is summarised:

- **The lock is unconditional.** Every append and every rewrite of every one of the six logs takes
  that log's lock, in every process, whether or not that process declared anything. There is no
  flag that turns it off and no store exempt from it. The `serialized` opt-out an earlier draft
  carried was deleted. This is what took the measured loss to zero.
- **Ownership is advisory and opt-in.** `check_declared_writer` raises only inside the two daemons;
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

`thread_mutex_for` is a second lock taken before the flock, and the module is careful about the
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

### Same Host, Enforced Rather Than Assumed

The MCP process and the dashboard share a host, and `_verify_lock_capability` is how that stops
being an assumption. NFS and SMB emulate `flock` with per-process byte-range locks and WSL's DrvFs
ignores it outright; all three let the second acquisition succeed and are refused loudly by
`UnsafeLockFilesystemError`. A remote or DrvFs coordination root is also the only way a second host
could be writing these logs, so probing the lock's capability enforces the same-host assumption and
the local-POSIX platform constraint in one check. A lock is never downgraded to a silent no-op:
where it is required and unavailable, this refuses to run.

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
  that looks safe and loses records, and `require_lock_held` is where it is caught. The module's own
  `thread_mutex_for` docstring states this convention as holding for all six; see Todos.
- Errors are a small tree rooted at `DurableStoreError(RuntimeError)`, with `CompactionOwnerError`
  and `UnsafeLockFilesystemError` beneath it. None is ever downgraded to a warning or a no-op.
- The temp name is hidden and pid-scoped (`.<log>.<pid>.tmp`), so it is skipped by the dot-prefix
  and `.tmp` filters in `serving/change_watcher.py` and two rewriters cannot collide on one path.
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
- There is deliberately no migration framework. The capability that is cheap now and unbuildable
  later is telling an old record from a new one, and `schemaVersion` is that capability.

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
- This module owns serialization, durability and the record base class. It owns no record
  vocabulary, no retention policy and no MCP surface; those stay in the per-store modules and in
  `interaction_retention.py`.

### Todos

- `thread_mutex_for`'s docstring asserts that "every one of the six splits its reclaim into a public
  method that takes the lock and a `_locked`/`_unlocked` half that does the work, precisely so it
  cannot [nest]". Checked against the six: three do, three inline the read, the filter and the
  rewrite under one `exclusive_access` (see Conventions). Note what is and is not wrong here — the
  claim the `RLock` argument actually rests on, that no store nests exclusivity today, is still
  true, and an inlined read-filter-rewrite does not nest either, so the re-entrancy rationale
  stands. Only the stated reason for it is inaccurate. Recorded, not repaired, by this card: the fix
  is a source docstring edit, outside a memory card's reach.

## Docs References

No external or domain documentation proves this behaviour: the contract is internal, and its
authority is the module's own front matter plus the two proof suites under `mcp/tests/`. Checked
the repository's design docs under `docs/design/` for a durable-store or JSONL-serialization
document and found none.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | N/A | N/A |

## Repo-Internal References

Citations into `durable_store.py` are **symbol names and docstring heading names, deliberately with
no line range** — the same form the leaf's test cards use. The file grew from 598 to 699 lines
during this leaf while curators were reading it, so every line number written against it was stale
within the hour; a symbol name is not. No range into this file adds anything a name cannot carry,
because each of its non-symbol blocks is a titled section of the module docstring. Ranges are kept
only for other files, and every one below was re-verified against the working tree on
2026-08-01 at 699 lines.

| Finding | Anchor | Source |
| --- | --- | --- |
| The `CONTRACT FRONT MATTER` block declaring `ar-durable-store/1.0`, the unconditional per-log serialization, single-owner compaction, the local-POSIX platform constraint and the two read policies. | "Contract:"; `DURABLE_STORE_CONTRACT` | mcp/src/agents_remember/controlplane/durable_store.py:3-8; mcp/src/agents_remember/controlplane/durable_store.py:42-42 |
| The heading that separates the two mechanisms: the lock is unconditional and is what took the loss to zero, while ownership is advisory and opt-in and works structurally rather than at runtime. Also where the module names all three `declare_process_role` call sites, the third being the `--reload` spawn worker. | `declare_process_role`; `StoreOwnership`; `is_compaction_owner`; `exclusive_access` | mcp/src/agents_remember/controlplane/durable_store.py:76-84; mcp/src/agents_remember/controlplane/durable_store.py:92-132; mcp/src/agents_remember/controlplane/durable_store.py:348-394 |
| The read-policy section: strict for authority because a skipped record could drop an `applied` marker, tolerant for projection because a tick must degrade rather than crash. Both bullets, TOLERANT included — an earlier range in this card stopped five lines short of it and cited only the strict half. | "Read policy is part of each store's authority contract:" | mcp/src/agents_remember/controlplane/durable_store.py:14-24 |
| The leaf's most important statement, and the one this card's read-policy body paraphrases: the three tolerant stores drop an unparseable row permanently rather than for one tick, which is a cost and not a defect only because none of the three carries authority — and if one ever does, its rewrite must be moved onto a strict read first, in the same change. | "Their rewrites may permanently drop malformed" | mcp/src/agents_remember/controlplane/durable_store.py:19-24 |
| The version rule as implemented: the major is compared for equality, so `"0.9"` is refused exactly as `"2.0"` is and an unparseable version is refused outright; `DurableRecord` validates `schemaVersion` on the way in so neither reader needs a version branch. | `schema_version_supported`; `SUPPORTED_SCHEMA_MAJOR`; `DurableRecord` | mcp/src/agents_remember/controlplane/durable_store.py:55-55; mcp/src/agents_remember/controlplane/durable_store.py:224-245; mcp/src/agents_remember/controlplane/durable_store.py:248-271 |
| `declare_process_role` and `declared_process_role`: the opt-in declaration the two advisory checks read, absent in every CLI invocation and test. Its docstring names the three call sites and states why `_dev_app` is the deliberate exception and the only factory that declares. | `declare_process_role`; `declared_process_role` | mcp/src/agents_remember/controlplane/durable_store.py:76-84; mcp/src/agents_remember/controlplane/durable_store.py:87-89 |
| `StoreOwnership` with no `serialized` field, `check_declared_writer` which raises only inside a declared process, and `is_compaction_owner` which is a question and never throws — including why the undeclared-is-owner default was re-decided and kept rather than inverted. | `StoreOwnership` | mcp/src/agents_remember/controlplane/durable_store.py:92-132 |
| The ownership register: all six constants side by side, four logs written by both processes and two by the dashboard alone. All six are named here because no single range covers them. | `GATE_OWNERSHIP`; `EXPECTATION_ROW_OWNERSHIP`; `ATTENTION_DISMISSAL_OWNERSHIP`; `OPERATOR_INBOX_OWNERSHIP`; `ORCHESTRATION_NUDGE_OWNERSHIP`; `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:138-150; mcp/src/agents_remember/controlplane/durable_store.py:152-162; mcp/src/agents_remember/controlplane/durable_store.py:164-180; mcp/src/agents_remember/controlplane/durable_store.py:182-198; mcp/src/agents_remember/controlplane/durable_store.py:200-210; mcp/src/agents_remember/controlplane/durable_store.py:212-221 |
| `OPERATOR_INBOX_OWNERSHIP` carries `compaction_owner=None`, the leaf's declared exception, because both processes must physically remove rows. | `OPERATOR_INBOX_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:182-198 |
| `ATTENTION_DISMISSAL_OWNERSHIP` records why a single-writer store is still locked, naming the 31.45 percent an unlocked draft measured. | `ATTENTION_DISMISSAL_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:164-180 |
| `thread_mutex_for` states that `flock` already excludes two threads of one process, so the mutex closes a plausible regression rather than a reproducible loss, and explains why it is re-entrant. Its account of how the six shape their reclaims is the one recorded under Todos. | `thread_mutex_for` | mcp/src/agents_remember/controlplane/durable_store.py:301-315 |
| `_verify_lock_capability` takes the lock twice from two file descriptions and raises `UnsafeLockFilesystemError` when the second acquisition succeeds. | `_verify_lock_capability` | mcp/src/agents_remember/controlplane/durable_store.py:318-345 |
| `exclusive_access` takes the per-log mutex before the flock, and the thread-local `_LockDepth` counter makes a nested acquisition return before either lock is touched. `lock_path_for` names the lockfile after the whole log and states why renaming it makes a rolling restart unsafe, with no compatibility path. | `exclusive_access`; `_LockDepth`; `lock_path_for` | mcp/src/agents_remember/controlplane/durable_store.py:274-282; mcp/src/agents_remember/controlplane/durable_store.py:348-394; mcp/src/agents_remember/controlplane/durable_store.py:291-298 |
| `require_lock_held` raises from inside `rewrite_lines`, so no store can rewrite a log it has not locked however the call was reached. | `require_lock_held`; `rewrite_lines` | mcp/src/agents_remember/controlplane/durable_store.py:397-415; mcp/src/agents_remember/controlplane/durable_store.py:439-446 |
| The one read both policies share; the only append in the package, which fsyncs before the handle closes; and the only rewrite, which never unlinks the log, uses a pid-scoped hidden temp, and fsyncs both the temp and the parent directory. | `read_log_text`; `append_line`; `rewrite_lines` | mcp/src/agents_remember/controlplane/durable_store.py:427-431; mcp/src/agents_remember/controlplane/durable_store.py:434-445; mcp/src/agents_remember/controlplane/durable_store.py:448-455 |
| The MCP process declares its role at the true entry point, not in the `create_server` factory a test would call in-process. | `main` | mcp/src/agents_remember/mcp/server.py:35-57 |
| The dashboard declares its role in `run`, for the same reason. | `run` | mcp/src/agents_remember/cli/dashboard.py:161-196 |
| The third call site and the only factory that declares: `--reload` serves from a uvicorn `multiprocessing` spawn child that re-imports the module with an empty declaration dict and never reaches `run`, so it answered owner for every log. The docstring records this as an ownership gap and not a durability defect — the unconditional lock covered the rewrite — and why `create_app` still must not declare. | `_dev_app` | mcp/src/agents_remember/cli/dashboard.py:52-81 |
| `_reclaim_gate_log` guards on `is_compaction_owner` before compacting, because the dashboard calls `gate_decide_payload` directly; without the guard an MCP-side reclaim runs inside the dashboard. | `_reclaim_gate_log` | mcp/src/agents_remember/controlplane/gate_decisions.py:74-80 |
| The dashboard's HTTP dismiss route calls `AttentionDismissalStore.dismiss`, the whole-file read-modify-write that made the single-writer store the worst loser. | "class AttentionDismissalStore"; "def dismiss" | mcp/src/agents_remember/controlplane/attention_dismissals.py:45-78 |
| `read_gates` no longer rewrites on the projection tick; it uses the tolerant `projected_current`, and physical reclamation moved to the gate log's owner. | "def read_gates(coordination_root: Path, *, now: date" | mcp/src/agents_remember/observer/snapshots_impl/_runtime.py:104-104 |
| The worktree series contract imports this module's `SCHEMA_VERSION` and `schema_version_supported`, so the tree carries one version policy rather than two. | `SCHEMA_VERSION`; `schema_version_supported` | mcp/src/agents_remember/worktrees/worktree_contract.py:16-16; mcp/src/agents_remember/worktrees/worktree_contract.py:40-40 |
| The control-plane lockfiles are excluded from the projection watch by a rule DERIVED from `lock_path_for` rather than spelled out, and matched by suffix in every watched directory — which is what covers the per-lifecycle `gates.jsonl.lock` a basename list structurally could not. `_EXCLUDED_WORKSPACE_NAMES` no longer names any lockfile; the comment above the derived constant records that spelling it out is exactly what broke. | `_DURABLE_LOG_LOCK_SUFFIX`; `is_projection_input_event` | mcp/src/agents_remember/serving/change_watcher.py:156-156; mcp/src/agents_remember/serving/change_watcher.py:187-205 |

## Cross-Repo References

No meaningful cross-repo references found. This contract governs one package inside this
repository; nothing outside it reads these logs.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

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
