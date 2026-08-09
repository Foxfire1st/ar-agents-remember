# mcp/tests/_store_durability.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/_store_durability.py`      |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash |                                       `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                         |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The **measurement instrument** for 260731-EFA-L5, and support code rather than a test module: it
contains no assertion at all. It expresses each of **eight** JSONL record stores — the six under
`controlplane/` plus `ProviderMetricsStore` and `ProviderDegradationStore` under `providers/`,
which have the identical shape and are therefore measured by the identical instrument rather than
by a second one (module docstring, cit:([`ProviderStoreAdapter`], mcp/tests/_store_durability.py:419-429)) — as four operations, drives three concurrency
scenarios against them in real processes, and returns a counted result — attempted / surviving /
lost / torn / raised. The suites that assert live elsewhere:
`test_controlplane_store_durability.py` imports the six control-plane cases, the shared profile
and the vacuity guard; `test_provider_store_durability.py` imports `PROVIDER_CASES` and the same
profile; `test_gate_replay_window.py` imports one primitive (`parked_rewrite`).

Separating the two is what makes the numbers usable. The same module, run as a script against a
`git archive` of the leaf's base commit, produced the reported loss rates; run as a pytest import
against the live worktree it produces the zeroes the contract test asserts. Report and gate are
therefore the same experiment rather than two that happen to agree.

**Read *The Instrument's Own Defect, Its Fix And Its Guard* below before trusting any number this
file produced.** The
harness had a bug that made the *ongoing* regression far weaker than it looked — every stress case
after the first ran for roughly one reclaim tick and dutifully reported 0.00% loss. It is fixed
(`harness_work_dir`), guarded (`MIN_RECLAIM_TICKS`) and re-measured. The documented base-commit
rates survived it; the contract assertions did not.

## Code Commentary

### The Instrument's Own Defect, Its Fix And Its Guard

This is the part a reader investigating the mechanism needs first, because it is the difference
between the leaf's evidence and the appearance of evidence.

**The defect: the work directory was derived from `root.parent`, so sibling roots shared one stop
flag.** A stress run keeps its stop flag, appender receipts and `*.err` files in a scratch
directory, and that directory used to come from `root.parent`. Every `run_case` in
`test_controlplane_store_durability.py` passes **sibling roots under one `self.tmp`** — e.g.
`self.tmp / f"stress-{case}"` (cit:(["stress-"], mcp/tests/test_controlplane_store_durability.py:164-164)) — so all cases shared one flag. `_reclaimer_main`
(cit:([`_reclaimer_main`], mcp/tests/_store_durability.py:627-653)) checks `stop.exists()` at the bottom of every tick, so the first case to finish set
the flag and every case after it left the tick loop after **one** tick. Measured on this tree with
the shared parent: **25 reclaim ticks for the first store and exactly 1 for each of the other
seven**, with all eight dutifully reporting 0.00% loss (cit:([`harness_work_dir`], mcp/tests/_store_durability.py:847-874);
independently restated at `test_controlplane_store_durability.py::HarnessVacuityGuardTests`,
cit:([`HarnessVacuityGuardTests`], mcp/tests/test_controlplane_store_durability.py:339-386)). A second consequence, less obvious and just as bad: the forced scenarios wrote their
receipt to `work / "forced.id"` and their errors to fixed `*.err` names (cit:([`run_forced_lost_update`, `run_forced_unlink`], mcp/tests/_store_durability.py:981-1016; mcp/tests/_store_durability.py:1019-1055))
that cit:([`_forced_result`], mcp/tests/_store_durability.py:959-978) then reads back, so a case whose appender wrote nothing was
scored off its **predecessor's** receipts.

**The fix: cit:([`harness_work_dir`], mcp/tests/_store_durability.py:847-874) returns `root.with_name(root.name + "-harness")`
— a sibling.** A sibling rather than a directory inside `root`, deliberately, because **`root`
does not name one place**: the six control-plane adapters resolve their log under `root/workspace`
(`StoreAdapter.log_path`, cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160)), the two provider adapters under
`root/logs/observer/providers` (`ProviderStoreAdapter.log_path`, cit:([`ProviderStoreAdapter`], mcp/tests/_store_durability.py:419-429)), and `GateStore`
additionally globs `root/lifecycles/*/gates.jsonl` — while the accounting reads that whole tree as
raw bytes cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583). "Inside `root`" is a different neighbourhood per store and
each of them is already owned or scanned by some store; the sibling is one rule that holds for all
eight adapters, and it keeps the harness's own bookkeeping out of the thing being weighed. A path
has exactly one name, so the sibling is unique whenever `root` is — and two cases sharing a `root`
would collide on the *log*, a collision no caller can overlook. `_prepared_work_dir`
(cit:([`_prepared_work_dir`], mcp/tests/_store_durability.py:877-880)) is the only creator; every scenario calls it.

**The guard: `MIN_SUCCESSFUL_RECLAIMS = 10` (cit:([`MIN_SUCCESSFUL_RECLAIMS`], mcp/tests/_durability_measurement.py:11-11)), raised as cit:([`VacuousRunError`], mcp/tests/_durability_measurement.py:14-15) from
cit:([`require_stress_measurement`], mcp/tests/_durability_measurement.py:18-55), which wraps the return value of `run_stress` (cit:([`run_stress`], mcp/tests/_store_durability.py:844-917)).**
It lives **in the instrument, not in either suite**, and that placement is the whole point: the
control-plane suite, the provider suite and a bare `main()` script run are covered by **one**
floor rather than by three copies of it, and cit:([`main`], mcp/tests/_store_durability.py:1231-1244) carries no assertions at all.
The floor is evidence-based rather than round: real runs measure **22-39** ticks idle and **34-49**
under 24-way CPU load — load *raises* the count, because appender pacing stretches in wall clock
while the reclaimer keeps polling — so 10 sits an order of magnitude above a vacuous run and under
half the lowest of the 32 observed runs (8 stores × 4 runs). A floor of 20 was rejected: the
observed minimum is 22, which is no margin. Both halves are asserted rather than left in a comment
by `test_controlplane_store_durability.py::HarnessVacuityGuardTests` (cit:([`HarnessVacuityGuardTests`], mcp/tests/test_controlplane_store_durability.py:339-386)).

**The principle: a measurement must refuse to report a vacuous result.** A loss figure is a figure
about a window — the one between a reclaim's read and its commit. Open it twice instead of two
hundred times and "0 records lost" costs the store nothing to earn. A check every caller has to
remember holds only until the next caller, so the refusal belongs to the instrument that produces
the number, beside the accounting that produces it.

**The invariant the guard must not quietly replace: sibling roots under one temp directory stay
legitimate.** A guard that required callers to pick distinct *parents* would be the same defect
rewritten as a convention — correct only while every caller remembered it, and silent when one did
not. The fix is a derivation that cannot be got wrong, not a rule that has to be obeyed.

**What survived, and what did not.** The documented base-commit rates were **not** corrupted by
this bug. Re-measured through the same `git archive` under the working harness, four runs each,
percentage of records the store reported written and then did not have: attention **23.91%**,
gate **9.38%**, supervisor-signals **8.00%**, expectation-rows **7.63%**, nudges **7.50%**,
operator-inbox **0.00%**. That preserves the documented ordering store for store, with the same
lone survivor at exactly zero. They survived because cit:([`main`], mcp/tests/_store_durability.py:1231-1244) — the entry point every
base-commit run goes through — already gave each case a root under its **own** parent
(`<root>/run{n}/{case}/observer`, cit:([`main`], mcp/tests/_store_durability.py:1231-1244)), so `root.parent` was distinct there and the stop
flag was never shared. **The bug never corrupted the historical measurements; it hollowed out the
ongoing regression**, which is measured against the live tree and was passing over one tick per
store.

**Those six figures are this leaf's four-run means and do not appear in the source.** What the
source carries is the *ranges* they were taken from, in
`test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring (cit:([`HarnessSensitivityTests`], mcp/tests/test_controlplane_store_durability.py:389-444)): attention 18.27-30.10, gate 7.50-10.50, supervisor_signal
7.50-9.00, expectation 6.50-9.50, nudge 5.50-9.00, operator_inbox 0.00 (all four runs). Each mean
above was checked against its own range and falls inside it. A reviewer grepping
`_store_durability.py` for `23.91` will find nothing, and that is expected rather than drift.

### Logic

**One adapter per store, four operations.** cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160) declares `open` / `write` /
`write_decoy` / `reclaim_now` / `read` plus three class-level facts — `log_name`, `id_field`, and
the two the scenarios branch on: `torn_line_policy` and `appends_in_place`. `write` is whatever
that store calls "record this fact" and `reclaim_now` is that store's own shipped reclaim entry
point, never a reimplementation, so what is measured is shipped behaviour. The six control-plane
adapters are `GateAdapter` (cit:([`GateAdapter`], mcp/tests/_store_durability.py:163-189), `compact`), `ExpectationAdapter` (cit:([`ExpectationAdapter`], mcp/tests/_store_durability.py:192-235), `compact` with
a retention window), `AttentionAdapter` (cit:([`AttentionAdapter`], mcp/tests/_store_durability.py:238-276), `prune_lifecycles`), `OperatorInboxAdapter`
(cit:([`OperatorInboxAdapter`], mcp/tests/_store_durability.py:279-312), `compact`), `NudgeAdapter` (cit:([`NudgeAdapter`], mcp/tests/_store_durability.py:315-370), `replace_records`) and
`AgentNotifierSignalAdapter` (cit:([`AgentNotifierSignalAdapter`], mcp/tests/_store_durability.py:385-414), `compact`); the two provider adapters are
`ProviderMetricsAdapter` (cit:([`ProviderMetricsAdapter`], mcp/tests/_store_durability.py:419-465), `compact`) and `ProviderDegradationAdapter` (cit:([`ProviderDegradationAdapter`], mcp/tests/_store_durability.py:468-527),
`compact_events`), both under cit:([`ProviderStoreAdapter`], mcp/tests/_store_durability.py:419-429) for the different log directory.
`CONTROLPLANE_ADAPTERS` / `PROVIDER_ADAPTERS` / `ADAPTERS` / `CASES` / `PROVIDER_CASES` /
cit:([`APPEND_CASES`], mcp/tests/_store_durability.py:568-568) are derived from them, so a ninth store is registered once — and
`CASES` deliberately stays the six control-plane stores beside a separate `PROVIDER_CASES`, so
adding the provider stores to the shared instrument did not silently widen what the control-plane
contract test asserts.

**`AttentionAdapter` is the one that is not an append.** It sets `appends_in_place = False`
(cit:([`AttentionAdapter`], mcp/tests/_store_durability.py:238-276)) because `dismiss` is a whole-file read-modify-write with no `"a"`-mode handle to strand;
cit:([`APPEND_CASES`], mcp/tests/_store_durability.py:568-568) is what the unlink scenario iterates, so the attention store is
covered by the lost-update scenario only. That is a property of the store, derived once, not a
skip written into a test.

**Three record classes, and they are what make "loss" mean something.** `SURVIVOR_PREFIX` /
`ANCHOR_ID` / cit:([`DECOY_PREFIX`], mcp/tests/_store_durability.py:93-93) partition every log into three kinds of row.
**`survivor-*`** is what policy must keep and the only class the accounting counts —
`surviving_ids` filters on exactly that prefix (cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583)). **`decoy-*`** is what policy *should*
drop, so that a reclaim tick does real work: `StoreAdapter.reclaim` (cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160)) writes a decoy and
*then* reclaims, because every one of these stores returns early when nothing is prunable and a
pass with nothing to drop would never open the window being measured. **`anchor-keepalive`** is
never prunable and never counted; cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160) writes it only when the scenario wants the
`os.replace` path, so the kept set stays non-empty and a reclaim exercises the temp-and-rename
branch rather than the `unlink` branch — `run_forced_unlink` seeds without one (cit:([`run_forced_unlink`], mcp/tests/_store_durability.py:1019-1055))
precisely so the kept set *can* reach empty. Between them, a reported "loss" means *a row nobody
decided to drop*, never ordinary bounded-store reclamation. `ProviderDegradationAdapter` is the
one adapter that departs from this and says why (cit:([`ProviderDegradationAdapter`], mcp/tests/_store_durability.py:468-527)): its reclaim drops by row **count**,
so its cit:([`ProviderDegradationAdapter`], mcp/tests/_store_durability.py:468-527) pre-fills the log to exactly `retain_rows` and its cit:([`ProviderDegradationAdapter`], mcp/tests/_store_durability.py:468-527)
writes no decoy at all, since a per-tick decoy would compete with the survivors for the retention
window and turn a legitimate truncation into a reported loss.

**Loss accounting deliberately bypasses every store's own `read`.** cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583)
is a raw *tolerant* JSON-lines reader that returns two quantities — the set of *survivor ids
physically present* and the count of *unparseable lines* — which are **never summed**. Both
directions matter: a strict store reader would turn a durability measurement into an exception,
and a tolerant one would report a torn line as a lost record. Loss and tearing are different
defects. The receipts are the other half — cit:([`_appender_main`], mcp/tests/_store_durability.py:591-624) journals an id only
*after* the store call returned, so anything on that list and not on disk is a record the store
accepted and then lost, and a write that raised is counted as an error rather than as a loss.

**Three scenarios.** cit:([`run_stress`], mcp/tests/_store_durability.py:844-917) races N appender processes against one reclaiming
process and is the one that yields a *rate*; cit:([`run_forced_lost_update`], mcp/tests/_store_durability.py:981-1016) forces exactly
one append into the reclaim's read→commit window and is deterministic;
cit:([`run_forced_unlink`], mcp/tests/_store_durability.py:1019-1055) holds one `"a"` handle open across a reclaim that empties the
log. cit:([`SCENARIOS`], mcp/tests/_store_durability.py:1058-1062) is the dispatch table shared by the pytest path and the script path.

**cit:([`parked_rewrite`], mcp/tests/_store_durability.py:656-701)** is the interposition the two forced scenarios are built on. It
hooks `Path.write_text` **and** `os.replace` — whichever the implementation reaches first — arms
once, fires `ready`, and waits on `released` with a timeout. The timeout is what keeps the
scenario terminating: an implementation that serialises the other process out never sets
`released`, so the parked rewrite resumes on its own instead of deadlocking. The unlink scenario
interposes at `Path.open` instead cit:([`_unlink_appender_main`], mcp/tests/_store_durability.py:766-800), outside the store, so it
measures whatever `append` currently does.

**Reclaim errors are counted, never fatal.** cit:([`_reclaimer_main`], mcp/tests/_store_durability.py:627-653) records an exception
and keeps ticking; stopping on the first raise would narrow the window and understate the loss.
`run_stress` reports `reclaim_error_count` and `append_error_count` separately from `lost`
(cit:([`run_stress`], mcp/tests/_store_durability.py:844-917)), which is what lets the contract test assert that a fixed store neither loses **nor**
raises. The same return is where `require_stress_measurement` sits (cit:([`require_stress_measurement`], mcp/tests/_durability_measurement.py:18-55)), so no stress result reaches a
caller without its tick count having cleared the floor.

**Pinning a run to one source tree.** cit:([`BASE_COMMIT`], mcp/tests/_store_durability.py:1091-1091) is the leaf's base commit;
cit:([`extract_base_commit_tree`], mcp/tests/_store_durability.py:1157-1183) `git archive`s that commit's `agents_remember` into a
scratch directory and extracts it with `tar` (the stdlib extractor's filter migration emits a
`DeprecationWarning` this suite turns into an error). cit:([`run_against_source`], mcp/tests/_store_durability.py:1187-1211)
re-executes this file as a script in a fresh interpreter with `PYTHONPATH` set to that tree, and
cit:([`_require_source_root`], mcp/tests/_store_durability.py:1220-1227) refuses with `SystemExit` unless `agents_remember` actually
resolved under it. cit:([`main`], mcp/tests/_store_durability.py:1231-1244) reads a JSON config, loops runs × cases, and writes a JSON
result.

### Conventions

**Dual-mode by design, and the mode boundary is one function.** The module is importable
(`ADAPTERS`, `CASES`, `PROVIDER_CASES`, `APPEND_CASES`, `STRESS_PROFILE`, `MIN_SUCCESSFUL_RECLAIMS`,
`VacuousRunError`, `run_case`, `parked_rewrite`, `harness_work_dir`, `extract_base_commit_tree`,
`run_against_source`) and executable as a script pinned to one `mcp/src` through `PYTHONPATH`
(`main`, cit:([`main`], mcp/tests/_store_durability.py:1231-1244), behind the `__main__` guard, cit:(["__main__"], mcp/tests/_store_durability.py:1247-1247)). Only the executable mode goes
through cit:([`_require_source_root`], mcp/tests/_store_durability.py:1220-1227), because only that mode makes a claim about *which
tree* it measured — and a measurement that cannot name its tree is worthless, so the guard raises
`SystemExit` rather than warning. That is exactly what lets `run_against_source` measure a
`git archive` of the base commit.

**Real processes, never threads.** `_context()` (cit:([`_context`], mcp/tests/_store_durability.py:824-825)) returns the `fork` context and every
scenario uses it. The defect is cross-process; threads would let the GIL serialise the exact
window under test, and the module docstring (cit:([`GIL`], mcp/tests/_store_durability.py:26-26)) states that as the reason rather than
leaving it to be inferred.

**One profile, two consumers.** cit:([`STRESS_PROFILE`], mcp/tests/_store_durability.py:1066-1073) — 4 appenders × 50 records at 2 ms
against one reclaimer at 5 ms, an 8000-tick budget and a 120 s bound — is imported by both
contract tests *and* used by the reported baseline, so the number in the report and the number the
suite enforces cannot become two different experiments. cit:([`FORCED_PROFILE`], mcp/tests/_store_durability.py:1074-1074) does the same for
the deterministic scenarios.

**The two measurement properties are enforced here rather than left to callers.** The implementation
points are `harness_work_dir` for scratch-space isolation and cit:([`require_stress_measurement`], mcp/tests/_durability_measurement.py:18-55) for refusing a
stress result whose reclaimer never ran. `harness_work_dir` keys the scratch space off `root` so
two cases can never share a stop flag, and `require_stress_measurement` raises rather than report a
stress result whose reclaimer never ran. Both were written *after* the second failed silently, and
both are stated as properties of a measurement — a caller that gets either wrong reports a number
that looks like the real one.

**`durable_store` is imported locally, inside a `try`.** `NudgeAdapter._reclaim_lock`
(cit:([`_reclaim_lock`], mcp/tests/_store_durability.py:338-361)) imports `exclusive_access` and `ORCHESTRATION_NUDGE_OWNERSHIP` inside the function
and yields unlocked on `ImportError`, because the same module runs against a base-commit archive
where `durable_store` does not exist. A top-level import would make the harness unable to measure
the tree it exists to measure.

**The nudge reclaim is written the way a correct owner would write it.**
`OrchestrationNudgeStore` is the one store of the six with no `compact` method, so its
read-filter half belongs to the caller; `_reclaim_lock` holds the log's lock across read, filter
and cit:([`NudgeAdapter`], mcp/tests/_store_durability.py:315-370) so that a failure measured there is the store's and not the
harness's own lost update.

**An archive, never a second worktree.** cit:([`extract_base_commit_tree`], mcp/tests/_store_durability.py:1157-1183) is explicit that
it runs inside a coordination worktree tree, and adding a git worktree under it is the kind of
side effect a measurement must not have.

### Invariants And Boundaries

- **A measurement must refuse to report a vacuous result.** `run_stress` returns through
  cit:([`require_stress_measurement`], mcp/tests/_durability_measurement.py:18-55) and raises `VacuousRunError` below `MIN_SUCCESSFUL_RECLAIMS`
  (cit:([`MIN_SUCCESSFUL_RECLAIMS`], mcp/tests/_durability_measurement.py:11-11)). The floor lives in the instrument, never in a suite: a check each caller has to remember
  holds only until the next caller, and the script entry point carries no assertions at all.
- **Sibling roots under one temp directory must remain legitimate.** cit:([`harness_work_dir`], mcp/tests/_store_durability.py:847-874)
  derives the scratch space from `root` itself, so no caller has to know anything. A guard that
  instead required callers to pick distinct *parents* would be the same defect rewritten as a
  convention. The only collision a caller can still cause is two cases sharing a `root`, which
  collides on the log itself and cannot be overlooked.
- Nothing the harness writes for its own bookkeeping may live inside `root`. The accounting reads
  that tree as raw bytes, and `root` resolves to a different subdirectory per store family, so the
  sibling is the only rule that holds for all eight adapters.
- Loss is counted from receipts against a raw on-disk read cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583); it must
  never be counted through a store's own `read`, in either direction. Survivors and unparseable
  lines are returned as two quantities and are never summed.
- `reclaim_now` must stay the store's real entry point. The moment an adapter reimplements a
  reclaim, the harness measures a model of the store instead of the store.
- Every wait is bounded (`parked_rewrite`'s `seconds`, `_join`'s deadline at cit:([`_join`], mcp/tests/_store_durability.py:829-838), the
  `handoff_seconds` waits in the forced entry points). A *fixed* store is expected to make the
  other party wait, so an unbounded wait here would hang on success rather than on failure.
- The base-commit run requires the archive step to succeed against the repository the file sits
  in cit:([`REPO_ROOT`], mcp/tests/_store_durability.py:1092-1092). This is a git-history dependency at test time, not just a code
  dependency: the sensitivity proof stops being reproducible if `e52edaf5` becomes unreachable
  from that worktree.
- The module asserts nothing and must not start. cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160) records each
  store's shipped policy so the contract test can assert it; the record and the assertion are
  deliberately in different files.

### Todos

Two parentheticals inside `parked_rewrite`'s docstring describe the **base commit**, not the
fixed tree, and now read as present-tense claims about code that changed underneath them:
witnessed in cit:([`parked_rewrite`], mcp/tests/_store_durability.py:656-701) and "these stores
name their temp file after the log with no pid in it" (cit:([`parked_rewrite`], mcp/tests/_store_durability.py:656-701)). Post-fix, `rewrite_lines`
writes its temp through `tmp.open("w", …)` so it can `fsync`, and the temp name carries the pid.
The hook still lands correctly — the same docstring anticipates the restructuring and hooks
`os.replace` for it — so this is stale prose, not a defect. Reported, not repaired: this card
does not modify the code worktree.

## Docs References

No Domain Documentation source is configured for this repository; the harness is measured against
repository code and the leaf's own base commit rather than against any external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The harness drives eight shipped stores through their own entry points and, for the base-commit
run, deliberately reaches none of the new contract module. The rows below are the reclaim entry
points it calls, the contract primitives it composes for the nudge log, and the three suites that
consume it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The gate reclaim the `GateAdapter` drives, and the append it races it against. `GateStore` is also why `harness_work_dir` is a sibling rather than a child: besides `<root>/workspace`, it globs `<root>/lifecycles/*/gates.jsonl` and iterates `<root>/lifecycles` for ids. | `compact`; `append`; `find`; `lifecycle_ids` | mcp/src/agents_remember/controlplane/store.py:112-118; mcp/src/agents_remember/controlplane/store.py:148-165; mcp/src/agents_remember/controlplane/store.py:247-277; mcp/src/agents_remember/controlplane/store.py:302-314 |
| `dismiss` is a whole-file read-modify-write with no append handle, which is why `AttentionAdapter` sets `appends_in_place = False`; `prune_lifecycles` is its reclaim. | `dismiss`; `prune_lifecycles` | mcp/src/agents_remember/controlplane/attention_dismissals.py:58-77; mcp/src/agents_remember/controlplane/attention_dismissals.py:102-111 |
| The expectation-row reclaim the adapter calls with an explicit retention window. | `compact`; `_compact_locked` | mcp/src/agents_remember/controlplane/expectation_rows.py:286-297; mcp/src/agents_remember/controlplane/expectation_rows.py:299-325 |
| The nudge store has no `compact`, so `replace_records` is the declared rewrite entry point and the read-filter half belongs to the caller — which is why the adapter holds the lock across all three steps. | `read`; `replace_records` | mcp/src/agents_remember/controlplane/orchestration_nudges.py:52-62; mcp/src/agents_remember/controlplane/orchestration_nudges.py:145-155 |
| The lock and ownership constant the nudge adapter imports locally so the harness still runs against a tree that predates them. | `exclusive_access`; `ORCHESTRATION_NUDGE_OWNERSHIP` | mcp/src/agents_remember/controlplane/durable_store.py:200-210; mcp/src/agents_remember/controlplane/durable_store.py:348-394 |
| The rewrite `parked_rewrite` parks inside: it commits through `os.replace` and never unlinks, and its temp name is pid-scoped — which is why the hook covers `os.replace` and not `Path.write_text` alone. | `rewrite_lines` | mcp/src/agents_remember/controlplane/durable_store.py:448-455 |
| The inbox reclaim the `OperatorInboxAdapter` drives — the one store of the six that already took a lock at the base commit, and therefore the lone survivor at 0.00%. | `compact`; `append` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:67-71; mcp/src/agents_remember/controlplane/operator_inbox_store.py:221-232 |
| The cooldown reclaim the `AgentNotifierSignalAdapter` drives with an explicit retention window. | "def append("; "def compact(" | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:108-119; mcp/src/agents_remember/controlplane/agent_notifier_signals.py:162-213 |
| The first provider store measured by the same instrument. Its log sits under `<root>/logs/observer/providers`, not `<root>/workspace`, which is one half of why the harness work directory cannot be a child of `root`. | `record_index_state`; `record`; `compact`; `read_recent` | mcp/src/agents_remember/providers/metrics.py:254-267; mcp/src/agents_remember/providers/metrics.py:269-283; mcp/src/agents_remember/providers/metrics.py:302-341; mcp/src/agents_remember/providers/metrics.py:343-360 |
| The second provider store. Its reclaim drops by row COUNT, which is why its adapter seeds a full backlog and writes no per-tick decoy. | `append_event`; `compact_events` | mcp/src/agents_remember/providers/degradation.py:217-231; mcp/src/agents_remember/providers/degradation.py:233-253 |
| The control-plane contract suite that imports `ADAPTERS`, `APPEND_CASES`, `CASES`, `MIN_SUCCESSFUL_RECLAIMS`, `STRESS_PROFILE`, `VacuousRunError`, `run_case`, `extract_base_commit_tree` and `run_against_source` and turns them into assertions. Its `self.tmp`-sibling roots are the layout the `root.parent` defect fired on; `HarnessVacuityGuardTests` proves the refusal is reachable through the shipped code path, and `HarnessSensitivityTests`' docstring carries the four-run base-commit RANGES. | `HarnessVacuityGuardTests`; `HarnessSensitivityTests` | mcp/tests/test_controlplane_store_durability.py:339-386; mcp/tests/test_controlplane_store_durability.py:389-444 |
| The provider contract suite, the second consumer the in-instrument floor covers. It imports `ADAPTERS`, `PROVIDER_CASES`, `STRESS_PROFILE`, `run_case`, `extract_base_commit_tree` and `run_against_source`, and its `case_root` docstring records that the defect was discovered there and worked around locally before being fixed at the source. Cited by symbol: this file still carried unstaged edits. | `ProviderStoreDurabilityTests`; `case_root` | mcp/tests/test_provider_store_durability.py:262-277; mcp/tests/test_provider_store_durability.py:280-351 |
| The replay suite that imports `parked_rewrite` alone, to park a gate-log compaction between its read and its commit. | `parked_rewrite` | mcp/tests/test_gate_replay_window.py:44-44 |

## Cross-Repo References

No meaningful cross-repo references found: the harness imports only `agents_remember` and the
standard library, and pins itself to one `mcp/src` inside this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 23 repeated path:start-end Citation objects from 4 same-claim citation group(s) at card line(s) 306, 308, 309, 317; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0. Preserved the two separate line-157 prose citations byte-for-byte; neither was part of this single-claim dedupe.
- 2026-08-02T20:52:54+02:00 — 260731-EFA-L6 W2-B12 Luna-max curator. Curated **50 citation findings** in this card: 40 legacy prose citations, 8 anchors absent from their cited ranges, 1 missing table anchor, and 1 malformed table source. Scoped `--fix` repaired 77 claims and normalised 4; the pinned scoped recheck now reports **0 findings**. Verification metadata was not refreshed, and no code, shared index, route index, entity register, task state, or other onboarding document was changed.
- 2026-08-01T19:40+02:00 — 260731-EFA-L5 curator. **The card was silent about a defect in the
  instrument itself, which is the one thing a reader landing here needs first**, so it gained a
  section ahead of Logic: *The Instrument's Own Defect, Its Fix And Its Guard*. **The defect** —
  the harness derived its work directory, including the reclaimer's stop flag, from `root.parent`;
  `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`
  (`self.tmp / f"stress-{case}"`, cit:(["stress-"], mcp/tests/test_controlplane_store_durability.py:164-164)), so every case shared one flag and, since
  cit:([`_reclaimer_main`], mcp/tests/_store_durability.py:627-653) tests `stop.exists()` at the bottom of each tick, every case after
  the first left the loop after ONE tick: **25 reclaim ticks for the first store and exactly 1 for
  each of the other seven, all eight reporting 0.00% loss**. Recorded the second consequence too:
  the forced scenarios shared `forced.id` and the `*.err` names (cit:([`run_forced_lost_update`, `run_forced_unlink`], mcp/tests/_store_durability.py:981-1016; mcp/tests/_store_durability.py:1019-1055)) that
  cit:([`_forced_result`], mcp/tests/_store_durability.py:959-978) reads back, so a case whose appender wrote nothing was scored off
  its predecessor's receipts. **The fix** — cit:([`harness_work_dir`], mcp/tests/_store_durability.py:847-874) returns
  `root.with_name(root.name + "-harness")`, a *sibling*, chosen over a child because `root` does
  not name one place: control-plane logs resolve under `root/workspace`
  (`StoreAdapter.log_path`, cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160)), provider logs under `root/logs/observer/providers`
  (`ProviderStoreAdapter.log_path`, cit:([`ProviderStoreAdapter`], mcp/tests/_store_durability.py:419-429)), and `GateStore` additionally globs
  `root/lifecycles/*/gates.jsonl`, while cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583) reads that whole tree as raw
  bytes. **The guard** — `MIN_SUCCESSFUL_RECLAIMS = 10` (cit:([`MIN_SUCCESSFUL_RECLAIMS`], mcp/tests/_durability_measurement.py:11-11)) raising `VacuousRunError`
  (cit:([`VacuousRunError`], mcp/tests/_durability_measurement.py:14-15)) from cit:([`require_stress_measurement`], mcp/tests/_durability_measurement.py:18-55) at the end of `run_stress` (cit:([`run_stress`], mcp/tests/_store_durability.py:844-917)),
  **in the instrument rather than in either suite**, so the control-plane suite, the provider
  suite and bare `main()` script runs (cit:([`main`], mcp/tests/_store_durability.py:1231-1244)) share one floor; evidence-based at 22-39 ticks
  idle and 34-49 under 24-way load — load raises the count — with 20 rejected because the observed
  minimum is 22. **The principle** is stated as an invariant: *a measurement must refuse to report
  a vacuous result*, beside its companion that *sibling roots under one temp directory must remain
  legitimate*, since a guard demanding distinct parents would be the same defect rewritten as a
  convention. **The reassuring half is recorded beside it**: the documented base-commit rates
  survived, re-measured at attention 23.91% / gate 9.38% / supervisor-signals 8.00% /
  expectation-rows 7.63% / nudges 7.50% / operator-inbox 0.00%, same ordering and same lone
  survivor — because `main` already built each case a root under its own parent
  (`<root>/run{n}/{case}/observer`, cit:([`main`], mcp/tests/_store_durability.py:1231-1244)). The bug never corrupted the historical
  measurements; it hollowed out the ongoing regression. **Those six figures are labelled as this
  leaf's four-run means that do NOT appear in the source**: the source carries *ranges*, in
  `test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring (cit:([`HarnessSensitivityTests`], mcp/tests/test_controlplane_store_durability.py:389-444)), and each mean was checked to fall inside its own range. Also added, per
  the leaf's request: the dual-mode boundary restated with cit:([`_require_source_root`], mcp/tests/_store_durability.py:1220-1227)
  and the `__main__` guard (cit:(["__main__"], mcp/tests/_store_durability.py:1247-1247)); `surviving_ids` as a tolerant reader returning two
  quantities that are never summed; and the **three record classes** — `survivor-*` (counted,
  cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583)), `decoy-*` (`StoreAdapter.reclaim`, cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160)) and `anchor-keepalive` (`seed`,
  cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160), omitted by `run_forced_unlink` at cit:([`run_forced_unlink`], mcp/tests/_store_durability.py:1019-1055)) — which is what makes "loss" mean *a
  row nobody decided to drop*. **Drift repaired while here:** the file has grown to 1153 lines and
  **every line citation in this card was stale**, so all were re-derived against the current file;
  the card also described six stores and two consumers, where the instrument now covers **eight**
  (the two `providers/` stores through `ProviderStoreAdapter`, cit:([`ProviderDegradationAdapter`], mcp/tests/_store_durability.py:468-527)) and is imported by
  **three** suites. **Citations:** every range above was opened and checked against each symbol the
  claim names, ends included. `_store_durability.py`, `test_controlplane_store_durability.py` and
  `test_gate_replay_window.py` are staged with no unstaged edits, so they are cited by line;
  `test_provider_store_durability.py` and every `controlplane/` and `providers/` source module
  still carry unstaged edits and are cited **by symbol name only**. Verification metadata
  untouched; closeout owns the first stamp.
- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: created the card for the leaf's measurement
  instrument. *(Every line number in this entry is a citation into a shorter version of the file
  and is superseded by the 19:40 entry above, which re-derived all of them; the symbols it names
  are still the right ones.)* Recorded the four properties that make its numbers trustworthy, each verified
  against the source rather than restated: (1) **dual-mode** — importable by the two suites and
  executable as a script whose `main` (cit:([`main`], mcp/tests/_store_durability.py:1231-1244)) reads a JSON config, with `_require_source_root`
  (cit:([`_require_source_root`], mcp/tests/_store_durability.py:1220-1227)) raising `SystemExit` unless `agents_remember` resolved under the tree the caller
  named, which is what let `run_against_source` (cit:([`run_against_source`], mcp/tests/_store_durability.py:1187-1211)) measure a `git archive` of
  `e52edaf5` (`BASE_COMMIT`, cit:([`BASE_COMMIT`], mcp/tests/_store_durability.py:1091-1091), `extract_base_commit_tree`, cit:([`extract_base_commit_tree`], mcp/tests/_store_durability.py:1157-1183)) with `PYTHONPATH` pinned;
  (2) **separate loss and torn accounting** — `surviving_ids` (cit:([`surviving_ids`], mcp/tests/_store_durability.py:558-583)) is a raw tolerant
  JSON-lines reader, deliberately not the store's own `read`, returning `(survivor ids present,
  unparseable line count)` so a strict reader cannot turn a measurement into an exception and a
  tolerant one cannot report a torn line as a lost record, paired with `_appender_main`
  (cit:([`_appender_main`], mcp/tests/_store_durability.py:591-624)) journalling an id only after the store call returned; (3) **real processes** —
  `_context()` (cit:([`_context`], mcp/tests/_store_durability.py:824-825)) is `multiprocessing.get_context("fork")` because the defect is
cross-process and the GIL would serialise the window (module docstring cit:([`GIL`], mcp/tests/_store_durability.py:26-26)); and (4) **one
  profile for both consumers** — `STRESS_PROFILE` (cit:([`STRESS_PROFILE`], mcp/tests/_store_durability.py:1066-1073)) is 4 appenders × 50 records at 2 ms
  against one reclaimer at 5 ms, imported by the contract test and used for the reported
  baseline. Also recorded the anchor/decoy design (cit:([`DECOY_PREFIX`], mcp/tests/_store_durability.py:93-93); cit:([`StoreAdapter`], mcp/tests/_store_durability.py:109-160)) that forces a reclaim tick
  to actually rewrite, `AttentionAdapter.appends_in_place = False` (cit:([`AttentionAdapter`], mcp/tests/_store_durability.py:238-276)) deriving
  `APPEND_CASES`, and `NudgeAdapter._reclaim_lock` (cit:([`_reclaim_lock`], mcp/tests/_store_durability.py:338-361)) importing `durable_store` locally
  inside a `try/except ImportError` so the harness can still run against a tree that predates it.
  Filed one Todo: two parentheticals in `parked_rewrite`'s docstring (cit:([`parked_rewrite`], mcp/tests/_store_durability.py:656-701))
  describe the base commit's `Path.write_text` temp materialisation and non-pid-scoped temp name,
  both of which the fix changed; the hook still lands via `os.replace`, so it is stale prose and
  not a defect. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is blank because the source file is new and uncommitted;
  closeout owns its first stamp.
