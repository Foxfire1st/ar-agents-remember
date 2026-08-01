# mcp/tests/_store_durability.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/_store_durability.py`      |
| doc_type               | `file-level-onboarding`               |
| lastUpdated            | 2026-08-01T19:40+02:00                |
| lastVerifiedCommitHash |                                       `a714114ef94eedb8042fb4caa38d9469f4767dd6`|
| lastVerifiedCommitDate |                                       2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                         |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The **measurement instrument** for 260731-EFA-L5, and support code rather than a test module: it
contains no assertion at all. It expresses each of **eight** JSONL record stores — the six under
`controlplane/` plus `ProviderMetricsStore` and `ProviderDegradationStore` under `providers/`,
which have the identical shape and are therefore measured by the identical instrument rather than
by a second one (module docstring, L1-L12) — as four operations, drives three concurrency
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
`self.tmp / f"stress-{case}"` (L158-L168) — so all cases shared one flag. `_reclaimer_main`
(L614-L635) checks `stop.exists()` at the bottom of every tick, so the first case to finish set
the flag and every case after it left the tick loop after **one** tick. Measured on this tree with
the shared parent: **25 reclaim ticks for the first store and exactly 1 for each of the other
seven**, with all eight dutifully reporting 0.00% loss (`harness_work_dir` docstring L790-L816;
independently restated at `test_controlplane_store_durability.py::HarnessVacuityGuardTests`,
L335-L351). A second consequence, less obvious and just as bad: the forced scenarios wrote their
receipt to `work / "forced.id"` and their errors to fixed `*.err` names (L976-L980, L1006-L1013)
that `_forced_result` (L933-L952) then reads back, so a case whose appender wrote nothing was
scored off its **predecessor's** receipts.

**The fix: `harness_work_dir(root)` (L790-L817) returns `root.with_name(root.name + "-harness")`
— a sibling.** A sibling rather than a directory inside `root`, deliberately, because **`root`
does not name one place**: the six control-plane adapters resolve their log under `root/workspace`
(`StoreAdapter.log_path`, L138-L139), the two provider adapters under
`root/logs/observer/providers` (`ProviderStoreAdapter.log_path`, L401-L411), and `GateStore`
additionally globs `root/lifecycles/*/gates.jsonl` — while the accounting reads that whole tree as
raw bytes (`surviving_ids`, L553-L578). "Inside `root`" is a different neighbourhood per store and
each of them is already owned or scanned by some store; the sibling is one rule that holds for all
eight adapters, and it keeps the harness's own bookkeeping out of the thing being weighed. A path
has exactly one name, so the sibling is unique whenever `root` is — and two cases sharing a `root`
would collide on the *log*, a collision no caller can overlook. `_prepared_work_dir`
(L820-L823) is the only creator; every scenario calls it.

**The guard: `MIN_RECLAIM_TICKS = 10` (L826-L841), raised as `VacuousRunError` (L844-L845) from
`_refuse_a_vacuous_run` (L848-L860), which wraps the return value of `run_stress` (L912-L930).**
It lives **in the instrument, not in either suite**, and that placement is the whole point: the
control-plane suite, the provider suite and a bare `main()` script run are covered by **one**
floor rather than by three copies of it, and `main` (L1136-L1149) carries no assertions at all.
The floor is evidence-based rather than round: real runs measure **22-39** ticks idle and **34-49**
under 24-way CPU load — load *raises* the count, because appender pacing stretches in wall clock
while the reclaimer keeps polling — so 10 sits an order of magnitude above a vacuous run and under
half the lowest of the 32 observed runs (8 stores × 4 runs). A floor of 20 was rejected: the
observed minimum is 22, which is no margin. Both halves are asserted rather than left in a comment
by `test_controlplane_store_durability.py::HarnessVacuityGuardTests` (L353-L378).

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
lone survivor at exactly zero. They survived because `main` (L1136-L1149) — the entry point every
base-commit run goes through — already gave each case a root under its **own** parent
(`<root>/run{n}/{case}/observer`, L1140-L1146), so `root.parent` was distinct there and the stop
flag was never shared. **The bug never corrupted the historical measurements; it hollowed out the
ongoing regression**, which is measured against the live tree and was passing over one tick per
store.

**Those six figures are this leaf's four-run means and do not appear in the source.** What the
source carries is the *ranges* they were taken from, in
`test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring (L387-L400,
the range block itself at L392-L393): attention 18.27-30.10, gate 7.50-10.50, supervisor_signal
7.50-9.00, expectation 6.50-9.50, nudge 5.50-9.00, operator_inbox 0.00 (all four runs). Each mean
above was checked against its own range and falls inside it. A reviewer grepping
`_store_durability.py` for `23.91` will find nothing, and that is expected rather than drift.

### Logic

**One adapter per store, four operations.** `StoreAdapter` (L104-L155) declares `open` / `write` /
`write_decoy` / `reclaim_now` / `read` plus three class-level facts — `log_name`, `id_field`, and
the two the scenarios branch on: `torn_line_policy` and `appends_in_place`. `write` is whatever
that store calls "record this fact" and `reclaim_now` is that store's own shipped reclaim entry
point, never a reimplementation, so what is measured is shipped behaviour. The six control-plane
adapters are `GateAdapter` (L158-L184, `compact`), `ExpectationAdapter` (L187-L230, `compact` with
a retention window), `AttentionAdapter` (L233-L271, `prune_lifecycles`), `OperatorInboxAdapter`
(L274-L307, `compact`), `NudgeAdapter` (L310-L365, `replace_records`) and
`SupervisorSignalAdapter` (L368-L398, `compact`); the two provider adapters are
`ProviderMetricsAdapter` (L414-L460, `compact`) and `ProviderDegradationAdapter` (L463-L522,
`compact_events`), both under `ProviderStoreAdapter` (L401-L411) for the different log directory.
`CONTROLPLANE_ADAPTERS` / `PROVIDER_ADAPTERS` / `ADAPTERS` / `CASES` / `PROVIDER_CASES` /
`APPEND_CASES` (L525-L545) are derived from them, so a ninth store is registered once — and
`CASES` deliberately stays the six control-plane stores beside a separate `PROVIDER_CASES`, so
adding the provider stores to the shared instrument did not silently widen what the control-plane
contract test asserts.

**`AttentionAdapter` is the one that is not an append.** It sets `appends_in_place = False`
(L238-L240) because `dismiss` is a whole-file read-modify-write with no `"a"`-mode handle to strand;
`APPEND_CASES` (L545) is what the unlink scenario iterates, so the attention store is
covered by the lost-update scenario only. That is a property of the store, derived once, not a
skip written into a test.

**Three record classes, and they are what make "loss" mean something.** `SURVIVOR_PREFIX` /
`ANCHOR_ID` / `DECOY_PREFIX` (L82-L88) partition every log into three kinds of row.
**`survivor-*`** is what policy must keep and the only class the accounting counts —
`surviving_ids` filters on exactly that prefix (L576-L577). **`decoy-*`** is what policy *should*
drop, so that a reclaim tick does real work: `StoreAdapter.reclaim` (L141-L149) writes a decoy and
*then* reclaims, because every one of these stores returns early when nothing is prunable and a
pass with nothing to drop would never open the window being measured. **`anchor-keepalive`** is
never prunable and never counted; `seed` (L151-L155) writes it only when the scenario wants the
`os.replace` path, so the kept set stays non-empty and a reclaim exercises the temp-and-rename
branch rather than the `unlink` branch — `run_forced_unlink` seeds without one (L999-L1000)
precisely so the kept set *can* reach empty. Between them, a reported "loss" means *a row nobody
decided to drop*, never ordinary bounded-store reclamation. `ProviderDegradationAdapter` is the
one adapter that departs from this and says why (L463-L475): its reclaim drops by row **count**,
so its `seed` (L514-L522) pre-fills the log to exactly `retain_rows` and its `reclaim` (L503-L505)
writes no decoy at all, since a per-tick decoy would compete with the survivors for the retention
window and turn a legitimate truncation into a reported loss.

**Loss accounting deliberately bypasses every store's own `read`.** `surviving_ids` (L553-L578)
is a raw *tolerant* JSON-lines reader that returns two quantities — the set of *survivor ids
physically present* and the count of *unparseable lines* — which are **never summed**. Both
directions matter: a strict store reader would turn a durability measurement into an exception,
and a tolerant one would report a torn line as a lost record. Loss and tearing are different
defects. The receipts are the other half — `_appender_main` (L586-L611) journals an id only
*after* the store call returned, so anything on that list and not on disk is a record the store
accepted and then lost, and a write that raised is counted as an error rather than as a loss.

**Three scenarios.** `run_stress` (L863-L930) races N appender processes against one reclaiming
process and is the one that yields a *rate*; `run_forced_lost_update` (L955-L990) forces exactly
one append into the reclaim's read→commit window and is deterministic;
`run_forced_unlink` (L993-L1029) holds one `"a"` handle open across a reclaim that empties the
log. `SCENARIOS` (L1032-L1036) is the dispatch table shared by the pytest path and the script path.

**`parked_rewrite` (L638-L683)** is the interposition the two forced scenarios are built on. It
hooks `Path.write_text` **and** `os.replace` — whichever the implementation reaches first — arms
once, fires `ready`, and waits on `released` with a timeout. The timeout is what keeps the
scenario terminating: an implementation that serialises the other process out never sets
`released`, so the parked rewrite resumes on its own instead of deadlocking. The unlink scenario
interposes at `Path.open` instead (`_unlink_appender_main`, L716-L747), outside the store, so it
measures whatever `append` currently does.

**Reclaim errors are counted, never fatal.** `_reclaimer_main` (L614-L635) records an exception
and keeps ticking; stopping on the first raise would narrow the window and understate the loss.
`run_stress` reports `reclaim_error_count` and `append_error_count` separately from `lost`
(L912-L930), which is what lets the contract test assert that a fixed store neither loses **nor**
raises. The same return is where `_refuse_a_vacuous_run` sits, so no stress result reaches a
caller without its tick count having cleared the floor.

**Pinning a run to one source tree.** `BASE_COMMIT` (L1065) is the leaf's base commit;
`extract_base_commit_tree` (L1069-L1093) `git archive`s that commit's `agents_remember` into a
scratch directory and extracts it with `tar` (the stdlib extractor's filter migration emits a
`DeprecationWarning` this suite turns into an error). `run_against_source` (L1096-L1118)
re-executes this file as a script in a fresh interpreter with `PYTHONPATH` set to that tree, and
`_require_source_root` (L1126-L1133) refuses with `SystemExit` unless `agents_remember` actually
resolved under it. `main` (L1136-L1149) reads a JSON config, loops runs × cases, and writes a JSON
result.

### Conventions

**Dual-mode by design, and the mode boundary is one function.** The module is importable
(`ADAPTERS`, `CASES`, `PROVIDER_CASES`, `APPEND_CASES`, `STRESS_PROFILE`, `MIN_RECLAIM_TICKS`,
`VacuousRunError`, `run_case`, `parked_rewrite`, `harness_work_dir`, `extract_base_commit_tree`,
`run_against_source`) and executable as a script pinned to one `mcp/src` through `PYTHONPATH`
(`main` at L1136-L1149 behind the `__main__` guard at L1152-L1153). Only the executable mode goes
through `_require_source_root` (L1126-L1133), because only that mode makes a claim about *which
tree* it measured — and a measurement that cannot name its tree is worthless, so the guard raises
`SystemExit` rather than warning. That is exactly what lets `run_against_source` measure a
`git archive` of the base commit.

**Real processes, never threads.** `_context()` (L768-L769) returns the `fork` context and every
scenario uses it. The defect is cross-process; threads would let the GIL serialise the exact
window under test, and the module docstring (L25-L26) states that as the reason rather than
leaving it to be inferred.

**One profile, two consumers.** `STRESS_PROFILE` (L1040-L1047) — 4 appenders × 50 records at 2 ms
against one reclaimer at 5 ms, an 8000-tick budget and a 120 s bound — is imported by both
contract tests *and* used by the reported baseline, so the number in the report and the number the
suite enforces cannot become two different experiments. `FORCED_PROFILE` (L1048) does the same for
the deterministic scenarios.

**The two measurement properties are enforced here rather than left to callers.** The module
docstring names them together (L28-L33): `harness_work_dir` keys the scratch space off `root` so
two cases can never share a stop flag, and `_refuse_a_vacuous_run` raises rather than report a
stress result whose reclaimer never ran. Both were written *after* the second failed silently, and
both are stated as properties of a measurement — a caller that gets either wrong reports a number
that looks like the real one.

**`durable_store` is imported locally, inside a `try`.** `NudgeAdapter._reclaim_lock`
(L333-L356) imports `exclusive_access` and `ORCHESTRATION_NUDGE_OWNERSHIP` inside the function
and yields unlocked on `ImportError`, because the same module runs against a base-commit archive
where `durable_store` does not exist. A top-level import would make the harness unable to measure
the tree it exists to measure.

**The nudge reclaim is written the way a correct owner would write it.**
`OrchestrationNudgeStore` is the one store of the six with no `compact` method, so its
read-filter half belongs to the caller; `_reclaim_lock` holds the log's lock across read, filter
and `replace_records` (L358-L362) so that a failure measured there is the store's and not the
harness's own lost update.

**An archive, never a second worktree.** `extract_base_commit_tree` (L1069-L1093) is explicit that
it runs inside a coordination worktree tree, and adding a git worktree under it is the kind of
side effect a measurement must not have.

### Invariants And Boundaries

- **A measurement must refuse to report a vacuous result.** `run_stress` returns through
  `_refuse_a_vacuous_run` (L848-L860) and raises `VacuousRunError` below `MIN_RECLAIM_TICKS`
  (L841). The floor lives in the instrument, never in a suite: a check each caller has to remember
  holds only until the next caller, and the script entry point carries no assertions at all.
- **Sibling roots under one temp directory must remain legitimate.** `harness_work_dir` (L790-L817)
  derives the scratch space from `root` itself, so no caller has to know anything. A guard that
  instead required callers to pick distinct *parents* would be the same defect rewritten as a
  convention. The only collision a caller can still cause is two cases sharing a `root`, which
  collides on the log itself and cannot be overlooked.
- Nothing the harness writes for its own bookkeeping may live inside `root`. The accounting reads
  that tree as raw bytes, and `root` resolves to a different subdirectory per store family, so the
  sibling is the only rule that holds for all eight adapters.
- Loss is counted from receipts against a raw on-disk read (`surviving_ids`, L553-L578); it must
  never be counted through a store's own `read`, in either direction. Survivors and unparseable
  lines are returned as two quantities and are never summed.
- `reclaim_now` must stay the store's real entry point. The moment an adapter reimplements a
  reclaim, the harness measures a model of the store instead of the store.
- Every wait is bounded (`parked_rewrite`'s `seconds`, `_join`'s deadline at L772-L781, the
  `handoff_seconds` waits in the forced entry points). A *fixed* store is expected to make the
  other party wait, so an unbounded wait here would hang on success rather than on failure.
- The base-commit run requires the archive step to succeed against the repository the file sits
  in (`REPO_ROOT`, L1066). This is a git-history dependency at test time, not just a code
  dependency: the sensitivity proof stops being reproducible if `e52edaf5` becomes unreachable
  from that worktree.
- The module asserts nothing and must not start. `torn_line_policy` (L116-L118) records each
  store's shipped policy so the contract test can assert it; the record and the assertion are
  deliberately in different files.

### Todos

Two parentheticals inside `parked_rewrite`'s docstring describe the **base commit**, not the
fixed tree, and now read as present-tense claims about code that changed underneath them:
"every one of these stores materialises its temp file that way" (L642-L643) and "these stores
name their temp file after the log with no pid in it" (L649). Post-fix, `rewrite_lines`
writes its temp through `tmp.open("w", …)` so it can `fsync`, and the temp name carries the pid.
The hook still lands correctly — the same docstring anticipates the restructuring and hooks
`os.replace` for it — so this is stale prose, not a defect. Reported, not repaired: this card
does not modify the code worktree.

## Docs References

No Domain Documentation source is configured for this repository; the harness is measured against
repository code and the leaf's own base commit rather than against any external specification.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The harness drives eight shipped stores through their own entry points and, for the base-commit
run, deliberately reaches none of the new contract module. The rows below are the reclaim entry
points it calls, the contract primitives it composes for the nudge log, and the three suites that
consume it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The gate reclaim the `GateAdapter` drives, and the append it races it against. `GateStore` is also why `harness_work_dir` is a sibling rather than a child: besides `<root>/workspace`, it globs `<root>/lifecycles/*/gates.jsonl` and iterates `<root>/lifecycles` for ids. | `compact`; `append`; `find`; `lifecycle_ids` | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| `dismiss` is a whole-file read-modify-write with no append handle, which is why `AttentionAdapter` sets `appends_in_place = False`; `prune_lifecycles` is its reclaim. | `dismiss`; `prune_lifecycles` | [controlplane/attention_dismissals.py](agents-remember/mcp/src/agents_remember/controlplane/attention_dismissals.py) |
| The expectation-row reclaim the adapter calls with an explicit retention window. | `compact`; `_compact_locked` | [controlplane/expectation_rows.py](agents-remember/mcp/src/agents_remember/controlplane/expectation_rows.py) |
| The nudge store has no `compact`, so `replace_records` is the declared rewrite entry point and the read-filter half belongs to the caller — which is why the adapter holds the lock across all three steps. | `read`; `replace_records` | [controlplane/orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py) |
| The lock and ownership constant the nudge adapter imports locally so the harness still runs against a tree that predates them. | `exclusive_access`; `ORCHESTRATION_NUDGE_OWNERSHIP` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The rewrite `parked_rewrite` parks inside: it commits through `os.replace` and never unlinks, and its temp name is pid-scoped — which is why the hook covers `os.replace` and not `Path.write_text` alone. | `rewrite_lines` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The inbox reclaim the `OperatorInboxAdapter` drives — the one store of the six that already took a lock at the base commit, and therefore the lone survivor at 0.00%. | `compact`; `append` | [controlplane/operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py) |
| The cooldown reclaim the `SupervisorSignalAdapter` drives with an explicit retention window. | `compact`; `append` | [controlplane/supervisor_signals.py](agents-remember/mcp/src/agents_remember/controlplane/supervisor_signals.py) |
| The first provider store measured by the same instrument. Its log sits under `<root>/logs/observer/providers`, not `<root>/workspace`, which is one half of why the harness work directory cannot be a child of `root`. | `record_index_state`; `record`; `compact`; `read_recent` | [providers/metrics.py](agents-remember/mcp/src/agents_remember/providers/metrics.py) |
| The second provider store. Its reclaim drops by row COUNT, which is why its adapter seeds a full backlog and writes no per-tick decoy. | `append_event`; `compact_events` | [providers/degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py) |
| The control-plane contract suite that imports `ADAPTERS`, `APPEND_CASES`, `CASES`, `MIN_RECLAIM_TICKS`, `STRESS_PROFILE`, `VacuousRunError`, `run_case`, `extract_base_commit_tree` and `run_against_source` and turns them into assertions. Its `self.tmp`-sibling roots are the layout the `root.parent` defect fired on; `HarnessVacuityGuardTests` proves the refusal is reachable through the shipped code path, and `HarnessSensitivityTests`' docstring carries the four-run base-commit RANGES. | imports L42-L52; R10 L119-L201; vacuity guard L335-L378; sensitivity L380-L435 | [test_controlplane_store_durability.py](agents-remember/mcp/tests/test_controlplane_store_durability.py) |
| The provider contract suite, the second consumer the in-instrument floor covers. It imports `ADAPTERS`, `PROVIDER_CASES`, `STRESS_PROFILE`, `run_case`, `extract_base_commit_tree` and `run_against_source`, and its `case_root` docstring records that the defect was discovered there and worked around locally before being fixed at the source. Cited by symbol: this file still carried unstaged edits. | `ProviderStoreDurabilityTests`; `case_root` | [test_provider_store_durability.py](agents-remember/mcp/tests/test_provider_store_durability.py) |
| The replay suite that imports `parked_rewrite` alone, to park a gate-log compaction between its read and its commit. | L44; L147-L152 | [test_gate_replay_window.py](agents-remember/mcp/tests/test_gate_replay_window.py) |

## Cross-Repo References

No meaningful cross-repo references found: the harness imports only `agents_remember` and the
standard library, and pins itself to one `mcp/src` inside this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-01T19:40+02:00 — 260731-EFA-L5 curator. **The card was silent about a defect in the
  instrument itself, which is the one thing a reader landing here needs first**, so it gained a
  section ahead of Logic: *The Instrument's Own Defect, Its Fix And Its Guard*. **The defect** —
  the harness derived its work directory, including the reclaimer's stop flag, from `root.parent`;
  `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`
  (`self.tmp / f"stress-{case}"`, L158-L168), so every case shared one flag and, since
  `_reclaimer_main` (L614-L635) tests `stop.exists()` at the bottom of each tick, every case after
  the first left the loop after ONE tick: **25 reclaim ticks for the first store and exactly 1 for
  each of the other seven, all eight reporting 0.00% loss**. Recorded the second consequence too:
  the forced scenarios shared `forced.id` and the `*.err` names (L976-L980, L1006-L1013) that
  `_forced_result` (L933-L952) reads back, so a case whose appender wrote nothing was scored off
  its predecessor's receipts. **The fix** — `harness_work_dir` (L790-L817) returns
  `root.with_name(root.name + "-harness")`, a *sibling*, chosen over a child because `root` does
  not name one place: control-plane logs resolve under `root/workspace`
  (`StoreAdapter.log_path`, L138-L139), provider logs under `root/logs/observer/providers`
  (`ProviderStoreAdapter.log_path`, L401-L411), and `GateStore` additionally globs
  `root/lifecycles/*/gates.jsonl`, while `surviving_ids` (L553-L578) reads that whole tree as raw
  bytes. **The guard** — `MIN_RECLAIM_TICKS = 10` (L826-L841) raising `VacuousRunError`
  (L844-L845) from `_refuse_a_vacuous_run` (L848-L860) at the end of `run_stress` (L912-L930),
  **in the instrument rather than in either suite**, so the control-plane suite, the provider
  suite and bare `main()` script runs (L1136-L1149) share one floor; evidence-based at 22-39 ticks
  idle and 34-49 under 24-way load — load raises the count — with 20 rejected because the observed
  minimum is 22. **The principle** is stated as an invariant: *a measurement must refuse to report
  a vacuous result*, beside its companion that *sibling roots under one temp directory must remain
  legitimate*, since a guard demanding distinct parents would be the same defect rewritten as a
  convention. **The reassuring half is recorded beside it**: the documented base-commit rates
  survived, re-measured at attention 23.91% / gate 9.38% / supervisor-signals 8.00% /
  expectation-rows 7.63% / nudges 7.50% / operator-inbox 0.00%, same ordering and same lone
  survivor — because `main` already built each case a root under its own parent
  (`<root>/run{n}/{case}/observer`, L1140-L1146). The bug never corrupted the historical
  measurements; it hollowed out the ongoing regression. **Those six figures are labelled as this
  leaf's four-run means that do NOT appear in the source**: the source carries *ranges*, in
  `test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring (L387-L400,
  range block L392-L393), and each mean was checked to fall inside its own range. Also added, per
  the leaf's request: the dual-mode boundary restated with `_require_source_root` (L1126-L1133)
  and the `__main__` guard (L1152-L1153); `surviving_ids` as a tolerant reader returning two
  quantities that are never summed; and the **three record classes** — `survivor-*` (counted,
  L576-L577), `decoy-*` (`StoreAdapter.reclaim` L141-L149) and `anchor-keepalive` (`seed`
  L151-L155, omitted by `run_forced_unlink` at L999-L1000) — which is what makes "loss" mean *a
  row nobody decided to drop*. **Drift repaired while here:** the file has grown to 1153 lines and
  **every line citation in this card was stale**, so all were re-derived against the current file;
  the card also described six stores and two consumers, where the instrument now covers **eight**
  (the two `providers/` stores through `ProviderStoreAdapter`, L401-L522) and is imported by
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
  executable as a script whose `main` (L907-L920) reads a JSON config, with `_require_source_root`
  (L897-L904) raising `SystemExit` unless `agents_remember` resolved under the tree the caller
  named, which is what let `run_against_source` (L867-L889) measure a `git archive` of
  `e52edaf5` (`BASE_COMMIT` L836, `extract_base_commit_tree` L840-L864) with `PYTHONPATH` pinned;
  (2) **separate loss and torn accounting** — `surviving_ids` (L397-L422) is a raw tolerant
  JSON-lines reader, deliberately not the store's own `read`, returning `(survivor ids present,
  unparseable line count)` so a strict reader cannot turn a measurement into an exception and a
  tolerant one cannot report a torn line as a lost record, paired with `_appender_main`
  (L430-L455) journalling an id only after the store call returned; (3) **real processes** —
  `_context()` (L612-L613) is `multiprocessing.get_context("fork")` because the defect is
  cross-process and the GIL would serialise the window (module docstring L20-L21); and (4) **one
  profile for both consumers** — `STRESS_PROFILE` (L811-L818) is 4 appenders × 50 records at 2 ms
  against one reclaimer at 5 ms, imported by the contract test and used for the reported
  baseline. Also recorded the anchor/decoy design (L60-L66, L119-L133) that forces a reclaim tick
  to actually rewrite, `AttentionAdapter.appends_in_place = False` (L212-L214) deriving
  `APPEND_CASES`, and `NudgeAdapter._reclaim_lock` (L307-L330) importing `durable_store` locally
  inside a `try/except ImportError` so the harness can still run against a tree that predates it.
  Filed one Todo: two parentheticals in `parked_rewrite`'s docstring (L486-L487, L493)
  describe the base commit's `Path.write_text` temp materialisation and non-pid-scoped temp name,
  both of which the fix changed; the hook still lands via `os.replace`, so it is stale prose and
  not a defect. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is blank because the source file is new and uncommitted;
  closeout owns its first stamp.
