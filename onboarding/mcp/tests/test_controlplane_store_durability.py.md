# mcp/tests/test_controlplane_store_durability.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_controlplane_store_durability.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-08-01T16:29+02:00                             |
| lastVerifiedCommitHash |                                                    `a714114ef94eedb8042fb4caa38d9469f4767dd6`|
| lastVerifiedCommitDate |                                                    2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The durability contract for the six control-plane JSONL stores, and the suite that closed the
measured record loss of 260731-EFA-L5. It holds three separate claims: **no record an appender was
told was written is missing afterwards** (R10), **the per-store torn-line policy is the one its
consumers need, and is not uniform** (R8), and — R14, in two halves — **the contract above is able
to fail** (proven against a `git archive` of the leaf's base commit) and **the instrument refuses
to report a run that measured nothing** (`HarnessVacuityGuardTests`; the module docstring states
both halves at L27-L30).

All assertion lives here; all mechanism lives in `_store_durability.py`, which is imported. That
split is why the suite can assert a number it did not itself produce — and why the vacuity floor
that decides whether a number is worth reporting sits in the instrument rather than in this file.

## Code Commentary

### Logic

**`MultiProcessDurabilityTests` (L119-L201) — R10, four tests over real processes.**
`test_no_record_is_lost_when_an_append_races_a_compaction` (L122-L134) drives the deterministic
lost-update scenario over all six `CASES`, asserting `attempted == 1`, `lost == 0` and no
stragglers. `test_no_record_is_lost_when_a_compaction_empties_and_unlinks_the_log` (L136-L149)
drives the unlink scenario over `APPEND_CASES` only — five stores, because
`AttentionDismissalStore` has no append to strand — and asserts the same three.
`test_no_record_is_lost_under_sustained_multi_process_write_and_compaction` (L151-L168) is the
unforced one: it also requires `attempted` to equal `appenders × per_appender` from
`STRESS_PROFILE`, which is what makes a store that *raised* instead of losing fail here rather
than silently shrinking the denominator, and it requires `torn_lines == 0`.
`test_concurrent_operation_never_raises_out_of_a_store_call` (L170-L201) is deliberately separate
from the loss assertions: a store that starts raising instead of losing has not been fixed, it
has moved the failure. Its docstring names the base-commit symptom — two concurrent
`AttentionDismissalStore` rewriters colliding on one non-pid-scoped temp path and one of them
taking `FileNotFoundError` out of `os.replace`. Because it runs its **own** stress root, it does
not inherit its sibling's "the run actually happened" guard and repeats it (L187-L191): without
that, an appender that died before reaching its loop would write no error file and "zero write
calls raised" would be reported over zero write calls — the same shape of empty green that
`HarnessVacuityGuardTests` below generalises.

**`TornLinePolicyTests` (L204-L332) — R8, and the two folds over one `GateStore.read`.** The
central pair is `test_gate_enforcement_fold_refuses_a_torn_line` (L231-L250), which drives
`read` / `current` / `all_current` as subtests and requires `ValidationError` from each, and
`test_gate_projection_fold_degrades_instead_of_crashing` (L252-L269), which requires
`observer/snapshots.read_gates` to still return the intact gate beside the torn line. The
assertion is on the surviving *ids*, not on "did not raise": degrading to one missing row is a
dashboard degrading, degrading to no gates at all is the projection losing its content, and only
the id list separates those. `test_correctness_bearing_reads_refuse_a_torn_line` (L271-L278) and
`test_display_only_reads_skip_a_torn_line` (L280-L291) generalise the split across the other five
stores through `STRICT_READ_CASES` / `TOLERANT_READ_CASES` (L74-L75).
`test_expectation_row_projection_degrades_instead_of_crashing` (L293-L332) is the same argument
one level up, and it now pins what the leaf actually shipped. It seeds two survivors, a torn line
and a third survivor *after* it (`_tear_mid_log`), then asserts the projection returns all three
ids by name — the trailing row is reachable only if the skip resumes, which is what separates
per-row tolerance from a reader that stops at the first bad line. Its control arm (L316-L332)
reconstructs the whole-log tolerance this leaf removed — the strict `pending()` under the same
`contextlib.suppress(OSError, ValueError)`, against the same log — and asserts it yields *nothing*:
three deadlines an operator is shown as due become an empty dashboard with no error. That contrast
is the test; "3 of 4 rows" and "0 of 4 rows" are both lists.

**`HarnessVacuityGuardTests` (L335-L377) — R14's other half, and the generalisable lesson of this
leaf: a measurement must refuse to report a vacuous result.** `_store_durability.harness_work_dir`
used to derive a run's working directory — including the reclaimer's **stop flag** — from
`root.parent`, and every `run_case` in this file passes a sibling root under one `self.tmp`. So all
six cases shared one stop flag: the first to finish set it, and every case after it found it
already set and left the tick loop after ONE tick. Measured directly on this tree, across all eight
stores the instrument covers: **25 reclaim ticks for the first store and exactly 1 for each of the
other seven**, with all eight dutifully reporting 0.00% loss and all eight green. The same layout
also let one case's receipt and `*.err` files stand in for the next case's, so a run that wrote
nothing was scored off its predecessor's files.

The fix is `harness_work_dir(root) = root.with_name(root.name + "-harness")` — a sibling, chosen
over a child deliberately. `root` does not name one place: the six control-plane adapters resolve
their log under `root/workspace`, the two provider adapters under `root/logs/observer/providers`,
and `GateStore` walks `root/lifecycles` besides; "inside `root`" is a different neighbourhood per
store, each one a directory some store already owns or scans. `root` is also the tree under
measurement and the accounting reads it as raw bytes, so nothing the harness writes for its own
bookkeeping belongs inside the thing being weighed. A path has exactly one name, so the sibling is
unique whenever `root` is — and two cases sharing a `root` would collide on the log itself, which
is a collision no caller can overlook.

`test_a_stress_run_whose_reclaimer_barely_ticked_is_refused` (L353-L360) drives `run_case` with
`max_ticks=1` and requires `VacuousRunError` out of the shipped code path rather than out of a
hand-built result dict, checking the message names both the tick count and the floor.
`test_the_floor_is_far_enough_below_what_a_real_run_produces` (L362-L377) asserts the constant from
both sides — greater than 2, less than 22 — because both halves are load-bearing and neither is
readable off the number: too low re-admits the run that measured nothing, too high turns a slow
machine red for a durability defect that is not there. The floor itself lives in the instrument
(`_store_durability.MIN_RECLAIM_TICKS = 10`, enforced by `_refuse_a_vacuous_run` on every stress
result), so the control-plane suite, the provider suite and bare script runs through `main()` are
covered by one floor instead of by an assertion each caller has to remember — a check each caller
must remember holds only until the next caller, and `main()` carries no assertions at all.

The floor is evidence-based, not round: over all eight stores, four runs each, real runs give
**22-39 reclaim ticks idle and 34-49 under 24 spinning CPU hogs on a 20-core box**. Load *raises*
the count — appender pacing stretches in wall clock while the reclaimer keeps polling — so the idle
figure is the one a floor has to clear, and a loaded CI box moves the number away from the floor
rather than into it. 10 sits an order of magnitude above a vacuous run and under half the lowest of
the 32 observed runs. A floor of 20 was rejected: the observed minimum is 22, which is no margin.

**`HarnessSensitivityTests` (L380-L435) — R14.** It extracts the base commit, asserts the archive
actually contains `controlplane/store.py`, runs the forced lost-update scenario against it
through a separate interpreter, and then asserts two different things: that the five unlocked
stores each lost exactly one record (`dict.fromkeys(unlocked, 1)`), and that `operator_inbox` lost
**zero** — the one store that already took an `fcntl` lock at the base commit. The second
assertion is the interesting one: it is the guard that says the harness is measuring the defect
rather than measuring something.

**The documented base-commit rates survived the harness fix — this is the reassuring half.**
Re-measured through the same archive under a working `harness_work_dir`, four runs, the class
docstring's own table (L392-L393): attention 18.27-30.10, gate 7.50-10.50, supervisor_signal
7.50-9.00, expectation 6.50-9.50, nudge 5.50-9.00, operator_inbox 0.00 in all four. The leaf's
re-measured four-run means (23.91 / 9.38 / 8.00 / 7.63 / 7.50 / 0.00) fall inside each of those
ranges, and both preserve the ordering and the lone survivor at exactly zero that this card
recorded before the instrument was fixed (31.45 / 11.50 / 10.50 / 10.20 / 9.20 / 0.00 — at or just
above the top of each range rather than outside it). They survived because `main()`, the entry
point the base-commit work runs through, already gave each case a root with its own parent, so the
archive runs were never the ones the shared flag silenced. **The bug never corrupted the historical
measurements; it hollowed out the ongoing regression** — the contract above, which is measured
against the live tree and was passing over one tick per store.

### Conventions

**The read-policy partition is derived from call sites, not from docstrings.** The comment block
above `STRICT_READ_CASES` (L63-L75) names, per store, the code that folds it and whether a dropped
row changes a decision: gate → `worktrees/modules/closeout.py`, `worktrees/modules/integrate.py`,
`serving/hosted_interactions.py`, none of them wrapping the read in a suppression;
expectation → the L2 overdue sweep; operator inbox → a consume is the ack of record; against
attention / nudge / supervisor, which only paint a screen or bound a rate.

**Forced rather than raced, where a yes/no is wanted.** `test_no_record_is_lost_when_an_append_
races_a_compaction`'s docstring states the reason: a stochastic reproduction of a narrow window
passes on a loaded CI box and proves nothing. The stress case is kept alongside precisely because
it is the one that produces a *rate* and carries the number in its failure text through
`_describe` (L78-L87) — which since the vacuity fix also reports `reclaim_ticks` (L86), so a
failure text states how much racing the rate was measured over, not only the rate.

**One seeded survivor plus one torn line, built by the adapters — and the torn line is not always
last.** `_TempRootTest._tear` (L96-L98) is now a one-call wrapper over `_tear_mid_log` (L100-L116),
which writes the `before` records through the store's own `write`, appends `TORN_LINE` (L61)
directly — a line cut off mid-write, which is what a crash or an interleaved append actually
leaves — and then writes the `after` records. Using the adapter for the good records means the
fixture cannot drift from the store's real shape; a non-empty `after` puts the torn line *inside*
the log, and the trailing records are reachable only if a tolerant reader's skip resumes.

**Every store is reached through `ADAPTERS`, never re-hardcoded.** The only store this file
constructs directly is `GateStore`, and only in `TornLinePolicyTests._seed_gate` (L214-L224),
which needs a gate in state `open` specifically because the projection keep-filter prunes
`applied`/`cancelled`/`expired` and a filtered-out gate would prove nothing about torn lines.
(`ExpectationRowStore` is constructed directly too, but only in the control arm at L321, to
rebuild a read policy the shipped code no longer uses.)

### Invariants And Boundaries

- Loss and raising are asserted separately and must stay that way. A fix that converts silent
  loss into an exception is not a fix, and only `test_concurrent_operation_never_raises_out_of_a_
  store_call` can see that.
- The torn-line policies are deliberately not uniform and must not be homogenised. The strict
  side exists because a skipped malformed row in the enforcement fold could drop an `applied`
  marker and re-open the replay window; the tolerant side exists because the dashboard's 1 s tick
  must not 500.
- The sensitivity proof depends on `e52edaf5` being reachable from this worktree's repository at
  test time (`_store_durability.extract_base_commit_tree`). That is a git-history dependency, not
  only a code one.
- This suite spawns real processes and runs a stress profile per store; it is not a unit test and
  its wall-clock cost is bounded by `STRESS_PROFILE['timeout']` per store plus the reclaimer's
  tick budget.
- **A green here is only evidence over a run that actually happened, and that is enforced rather
  than remembered.** Every stress result returns through `_refuse_a_vacuous_run`, so a reclaimer
  that barely ticked raises `VacuousRunError` instead of reporting 0.00% loss. `MIN_RECLAIM_TICKS`
  must stay in `_store_durability.py`: moved into this file it would stop covering the provider
  suite and the `main()` script path, which is how it went unguarded the first time.
- Every `run_case` root in this file is a sibling under one `self.tmp`, which is legitimate and must
  stay workable — the harness, not the caller, is responsible for keeping runs apart
  (`harness_work_dir`). A guard that instead required callers to choose distinct parents would be
  the same defect rewritten as a convention.
- `test_expectation_row_projection_degrades_instead_of_crashing` must keep asserting the surviving
  ids *by name*, including the row appended after the torn line, and must keep its whole-log
  control arm. Weakened back to "a list came back", it stops distinguishing per-row tolerance from
  whole-log tolerance and pins neither.

### Todos

None. The Todo this card carried at 14:20 is closed by the shipped test.
`test_expectation_row_projection_degrades_instead_of_crashing` (L293-L332) no longer describes the
pre-fix arrangement: its docstring now names `pending_for_projection()` and per-row degradation and
says the surrounding `contextlib.suppress(OSError, ValueError)` "is there for the I/O it was always
there for", matching `observer/snapshots.read_expectation_rows`; and its assertion now names the
three surviving ids and adds the whole-log control arm, so the regression the old
`assertIsInstance(rows, list)` could not see would now fail it.

## Docs References

No Domain Documentation source is configured for this repository; the contract asserted here is
the repository-local `ar-durable-store/1.0` front matter in `controlplane/durable_store.py`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite asserts against the six shipped stores and the two folds over the gate log, through one
shared instrument; the rows below are the code each claim is about.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The measurement instrument this file imports: adapters, case lists, the shared stress profile, the scenario dispatch, the base-commit archive, and the pinned re-execution. | `ADAPTERS`/`CASES`/`APPEND_CASES` L525-L545; `STRESS_PROFILE` L1040-L1047; `run_case` L1051-L1055; `extract_base_commit_tree` L1069-L1093; `run_against_source` L1096-L1118 | [_store_durability.py](agents-remember/mcp/tests/_store_durability.py) |
| The vacuity guard `HarnessVacuityGuardTests` exercises, and the sibling work directory whose absence made it necessary: the per-`root` harness directory holding the stop flag, the evidence-based floor, the refusal, and the single funnel every stress result returns through. | `harness_work_dir` L790-L817; `MIN_RECLAIM_TICKS` L826-L841; `VacuousRunError` L844-L845; `_refuse_a_vacuous_run` L848-L860; `run_stress`'s return through it L912-L930 | [_store_durability.py](agents-remember/mcp/tests/_store_durability.py) |
| The two `GateStore` read policies the R8 tests hold apart: `read` is strict, `read_for_projection` skips a torn or unknown-major line. | `read`; `read_for_projection` | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The projection fold asserted to survive a torn line — and which, since this leaf, no longer rewrites anything on the tick. | `read_gates` L514-L537 | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| The expectation-row projection wrapper, which this leaf moved onto the per-row tolerant read; its comment records that the surrounding `suppress(OSError, ValueError)` used to swallow one torn line by discarding every deadline, and is no longer load-bearing for a malformed row. | `read_expectation_rows` L592-L627 | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| The per-row tolerant expectation reads that wrapper now folds, and the strict `read` the L2 overdue sweep keeps. | `read`; `read_for_projection`; `pending_for_projection` | [controlplane/expectation_rows.py](agents-remember/mcp/src/agents_remember/controlplane/expectation_rows.py) |
| The unconditional lock and the never-unlinking rewrite that take the measured loss to zero, plus the schema-version validator that gives both read policies their behaviour with no version branch. | `exclusive_access`; `rewrite_lines`; `DurableRecord` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| Why the gate log is the one that matters: `apply_gate` is the appended snapshot and `evaluate_gate`'s `applied` branch is what refuses a second consume of one approval. | `apply_gate` L224-L233 | [controlplane/records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The refusal branch a dropped `applied` record would silently remove. | `evaluate_gate`'s `applied` branch L82-L88 | [controlplane/enforcement.py](agents-remember/mcp/src/agents_remember/controlplane/enforcement.py) |
| The replay-specific companion suite: same defect, asserted at the level of one human approval rather than of six record types. | `GateReplayWindowTests` L176-L324 | [test_gate_replay_window.py](agents-remember/mcp/tests/test_gate_replay_window.py) |
| The in-process axis of the same contract — threads, re-entrancy, the unsafe-filesystem refusal and failed-rewrite cleanup — which this file's `multiprocessing` harness deliberately cannot see. | L1-L24; `InProcessExclusivityTests` L155-L352; `UnsafeLockFilesystemTests` L355-L417; `FailedRewriteTests` L635-L711 | [test_durable_store_contract.py](agents-remember/mcp/tests/test_durable_store_contract.py) |

## Cross-Repo References

No meaningful cross-repo references found: every store, fold and archive this suite touches is
inside `agents-remember`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-01T16:29+02:00 — 260731-EFA-L5 curator: re-derived every self-citation against the
  15:48 file and recorded the class the card was missing. **`HarnessVacuityGuardTests` (L335-L377)
  added to Logic, with the principle and not only the class: a measurement must refuse to report a
  vacuous result.** `_store_durability.harness_work_dir` derived the run's working directory —
  including the reclaimer's stop flag — from `root.parent`, and every `run_case` here passes a
  sibling root under one `self.tmp`, so all six cases shared one stop flag and every case after the
  first left the tick loop after one tick. Measured across the eight stores the instrument covers:
  25 reclaim ticks for the first store, exactly 1 for each of the other seven, all eight reporting
  0.00% loss and all eight green. The fix is a sibling work directory
  (`root.with_name(root.name + "-harness")`), sibling rather than child because `root` does not
  name one place — control-plane adapters under `root/workspace`, provider adapters under
  `root/logs/observer/providers`, `GateStore` walking `root/lifecycles` besides — and because the
  accounting reads the whole `root` tree as raw bytes. The recurrence guard is
  `MIN_RECLAIM_TICKS = 10` raising `VacuousRunError` from inside the instrument, so the
  control-plane suite, the provider suite and bare `main()` runs share one floor rather than one
  assertion each; the floor is evidence-based (22-39 ticks idle, 34-49 under 24-way load, because
  load raises the count) — 10 is an order of magnitude above a vacuous run and under half the
  lowest of 32 observed runs, and 20 was rejected because the observed minimum of 22 is no margin.
  Also recorded the reassuring half: the documented base-commit rates **survived**. Re-measured
  under the working harness they are attention 18.27-30.10, gate 7.50-10.50, supervisor_signal
  7.50-9.00, expectation 6.50-9.50, nudge 5.50-9.00, operator_inbox 0.00 across all four runs
  (class docstring L392-L393), preserving the documented ordering store for store with the same
  lone survivor at exactly zero — because `main()`, the entry point the base-commit work runs
  through, already gave each case a root with its own parent. The bug never corrupted the
  historical measurements; it hollowed out the ongoing regression. **The 14:20 Todo is closed by
  the shipped code, not deferred:** `test_expectation_row_projection_degrades_instead_of_crashing`
  (L293-L332) now seeds a torn line mid-log via `_tear_mid_log`, asserts the three surviving ids by
  name, and carries a control arm that reconstructs the removed whole-log tolerance and pins it to
  an empty result — so the regression the old `assertIsInstance(rows, list)` could not see now
  fails it. Todos set to None and the "weakest assertion in the file" invariant replaced with the
  invariants that now hold. **Citations repaired (old → new), each opened and read at the new
  range, ends checked against every symbol the claim names:** `MultiProcessDurabilityTests`
  L97-L168 → L119-L201 (and its four tests L100-L112 → L122-L134, L114-L127 → L136-L149,
  L129-L146 → L151-L168, L148-L168 → L170-L201); `TornLinePolicyTests` L171-L267 → L204-L332 (and
  L191-L210 → L231-L250, L212-L229 → L252-L269, L231-L238 → L271-L278, L240-L251 → L280-L291,
  L253-L267 → L293-L332, `_seed_gate` L174-L184 → L214-L224); `HarnessSensitivityTests`
  L270-L310 → L380-L435; `_describe` L69-L78 → L78-L87; the read-policy comment block
  L54-L66 → L63-L75; `STRICT_READ_CASES`/`TOLERANT_READ_CASES` L65-L66 → L74-L75; `TORN_LINE`
  L52 → L61; `_tear` L87-L94 → L96-L98 plus the new `_tear_mid_log` L100-L116 that now holds the
  mechanism. Cross-file: `_store_durability.py` L375-L389/L397-L422/L803-L826/L840-L889 → symbol
  ranges for `ADAPTERS`/`CASES`/`APPEND_CASES` (L525-L545), `STRESS_PROFILE` (L1040-L1047),
  `run_case` (L1051-L1055), `extract_base_commit_tree` (L1069-L1093) and `run_against_source`
  (L1096-L1118), plus a new row for the vacuity guard; `enforcement.py` L80-L87 → L82-L88, which
  had begun two lines inside the `open` branch and stopped one line short of the `applied` branch's
  close; `test_gate_replay_window.py` L130-L205 → `GateReplayWindowTests` L176-L324, the old range
  having covered module helpers and ended mid-`_tear_the_applied_record` without reaching a test;
  `test_durable_store_contract.py` L152-L349 → `InProcessExclusivityTests` L155-L352 plus
  `UnsafeLockFilesystemTests` L355-L417 and `FailedRewriteTests` L635-L711, the old range having
  stopped three lines inside the first class and never reached the unsafe-filesystem or
  failed-rewrite halves its own claim names. Verified unchanged and left alone:
  `snapshots.read_gates` L514-L537, `snapshots.read_expectation_rows` L592-L627, `records.apply_gate`
  L224-L233, `test_durable_store_contract.py` L1-L24. Rows into `durable_store.py`, `store.py` and
  `expectation_rows.py` stay symbol-name-only by rule; every named symbol was confirmed present.
  The source file's mtime and byte count were identical before and after this pass, so ranges
  rather than symbol-only citations are safe for it. Verification metadata untouched.
- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: created the card for the leaf's durability
  contract suite. Recorded the three claims it holds and, for each, what breaks if it is deleted.
  **R10** — four tests in `MultiProcessDurabilityTests` (L97-L168): the forced lost-update window
  over all six stores, the forced unlink window over the five that really append (`APPEND_CASES`;
  `AttentionDismissalStore.dismiss` is a whole-file read-modify-write, so there is no `"a"` handle
  to strand), the unforced stress case that also pins `attempted` to
  `appenders × per_appender` so a raising store cannot shrink its own denominator, and — kept
  deliberately separate — `test_concurrent_operation_never_raises_out_of_a_store_call` (L148-L168),
  because a store that raises instead of losing has moved the failure rather than fixed it.
  **R8** — `TornLinePolicyTests` (L171-L267) holds the two folds over one `GateStore.read` to
  opposite policies (strict `read`/`current`/`all_current` raise `ValidationError`; `read_gates`
  must still surface the intact gate *by id*, which is what separates "one row missing" from "no
  gates at all"), generalised across the other five stores through `STRICT_READ_CASES` /
  `TOLERANT_READ_CASES` (L65-L66) whose membership the source derives from named call sites in the
  comment block above them (L54-L66), not from docstrings. **R14** —
  `HarnessSensitivityTests` (L270-L310) asserts both directions against the base-commit archive:
  the five unlocked stores each lose exactly one record, and `operator_inbox` — the one store that
  already held an `fcntl` lock at `e52edaf5` — loses zero, which is the guard that the harness is
  measuring the defect. Also recorded `_TempRootTest._tear` (L87-L94) seeding through the store's
  own `write` before appending `TORN_LINE` (L52), and `_seed_gate` (L174-L184) using state `open`
  because the projection keep-filter prunes the terminal states. **Filed one Todo, found by
  reading the cited source rather than the test:**
  `test_expectation_row_projection_degrades_instead_of_crashing` (L253-L267) says in its docstring
  that the tolerance lives in `observer/snapshots.read_expectation_rows`'s
  `contextlib.suppress(OSError, ValueError)` and that "today it degrades to the WHOLE log rather
  than to one row". That is the pre-fix arrangement. This leaf moved that wrapper onto
  `pending_for_projection()` (`snapshots.py` L592-L627; `expectation_rows.read_for_projection` /
  `pending_for_projection`), so degradation is now per row, and the source states the `suppress` "is no longer
  load-bearing for a malformed row". The test's only assertion is `assertIsInstance(rows, list)`,
  which passes under both behaviours — so the docstring is stale and the assertion does not pin
  what the leaf shipped. Reported, not repaired. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is blank because the source
  file is new and uncommitted; closeout owns its first stamp.
