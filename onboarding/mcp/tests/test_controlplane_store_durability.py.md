# mcp/tests/test_controlplane_store_durability.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_controlplane_store_durability.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Control-plane append/compaction durability and gate torn-line policy.

## Code Commentary

### Logic

A deterministic multi-process race runs each retained store case and requires one attempted append, zero lost records and no stragglers. Gate enforcement reads reject a torn JSONL row; dashboard projection still returns the intact gate beside it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The measurement helper owns the mechanism and this suite asserts its outcome. The reduced source does not retain sustained stress, unlink races or historical-baseline failure demonstrations.

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
| No record is lost when an append races a compaction. | `test_no_record_is_lost_when_an_append_races_a_compaction` | mcp/tests/test_controlplane_store_durability.py:91-103 |
| Gate enforcement fold refuses a torn line. | `test_gate_enforcement_fold_refuses_a_torn_line` | mcp/tests/test_controlplane_store_durability.py:133-152 |
| Gate projection fold degrades instead of crashing. | `test_gate_projection_fold_degrades_instead_of_crashing` | mcp/tests/test_controlplane_store_durability.py:154-171 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:42:13+00:00 — Gate-5 claim re-review against C97: reconciled current durable-store/kernel locking ownership and exact source evidence. The test or harness source bytes match the prior verified source; verification advances for the reopened claim review.

- 2026-08-26T10:44:52+02:00 — Reconciled the durability suite with explicit integration/stress evidence lanes and moved vacuous-measurement assertions to the focused `test_durability_measurement.py` owner.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 added direct `GateState` resolver tests for current, historical-fixture-only, and unrelated-error paths as part of the master CRAP/diff-coverage repair.
- 2026-08-11T14:29+02:00 — Re-read `rewrite_lines` and regenerated its citation around the
  current declaration while retaining the lock and record evidence; verification metadata remains
  unchanged for governed closeout.

- 2026-08-10T10:40+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 139 repeated path:start-end Citation objects from 3 same-claim citation group(s) at card line(s) 223, 228, 232; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:27+02:00 — W2-B08 curator: anchored 25 citation findings; preserved the deleted historical names `reclaim_ticks`, `MIN_RECLAIM_TICKS`, and `_refuse_a_vacuous_run` visibly as Tier 3 with current-source evidence for the surviving instrument names. Verification metadata stays pinned until closeout.
- 2026-08-01T16:29+02:00 — 260731-EFA-L5 curator: re-derived every self-citation against the
  15:48 file and recorded the class the card was missing. **cit:([`DurabilityMeasurementTests`], mcp/tests/test_durability_measurement.py:34-99)
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
  (class docstring table), preserving the documented ordering store for store with the same
  lone survivor at exactly zero — because `main()`, the entry point the base-commit work runs
  through, already gave each case a root with its own parent. The bug never corrupted the
  historical measurements; it hollowed out the ongoing regression. **The 14:20 Todo is closed by
  the shipped code, not deferred:** `test_expectation_row_projection_degrades_instead_of_crashing`
  (cit:([`test_expectation_row_projection_degrades_instead_of_crashing`], mcp/tests/test_controlplane_store_durability.py:297-336)) now seeds a torn line mid-log via `_tear_mid_log`, asserts the three surviving ids by
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
  mechanism. Cross-file: `_store_durability.py`'s `ADAPTERS`/`CASES`/`APPEND_CASES`,
  `STRESS_PROFILE`, `run_case`, `extract_base_commit_tree` and `run_against_source` now have
  symbol-anchored rows in Repo-Internal References, plus a new row for the vacuity guard;
  `enforcement.py`'s `evaluate_gate` row now covers the applied branch, which
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
  **R10** — four tests in cit:([`MultiProcessDurabilityTests`], mcp/tests/test_controlplane_store_durability.py:123-205): the forced lost-update window
  over all six stores, the forced unlink window over the five that really append (`APPEND_CASES`;
  `AttentionDismissalStore.dismiss` is a whole-file read-modify-write, so there is no `"a"` handle
  to strand), the unforced stress case that also pins `attempted` to
  `appenders × per_appender` so a raising store cannot shrink its own denominator, and — kept
  deliberately separate — cit:([`test_concurrent_operation_never_raises_out_of_a_store_call`], mcp/tests/test_controlplane_store_durability.py:174-205),
  because a store that raises instead of losing has moved the failure rather than fixed it.
  **R8** — cit:([`TornLinePolicyTests`], mcp/tests/test_controlplane_store_durability.py:208-336) holds the two folds over one `GateStore.read` to
  opposite policies (strict `read`/`current`/`all_current` raise `ValidationError`; `read_gates`
  must still surface the intact gate *by id*, which is what separates "one row missing" from "no
  gates at all"), generalised across the other five stores through `STRICT_READ_CASES` /
  `TOLERANT_READ_CASES` (cit:([`TOLERANT_READ_CASES`], mcp/tests/test_controlplane_store_durability.py:77-77)) whose membership the source derives from named call sites in the
  comment block above them (cit:([`STRICT_READ_CASES`], mcp/tests/test_controlplane_store_durability.py:76-76)), not from docstrings. **R14** —
  `HarnessSensitivityTests` (cit:([`HarnessSensitivityTests`], mcp/tests/test_controlplane_store_durability.py:345-401)) asserts both directions against the base-commit archive:
  the five unlocked stores each lose exactly one record, and `operator_inbox` — the one store that
  already held an `fcntl` lock at `e52edaf5` — loses zero, which is the guard that the harness is
  measuring the defect. Also recorded `_TempRootTest._tear` (cit:([`_tear`], mcp/tests/test_controlplane_store_durability.py:102-104)) seeding through the store's
  own `write` before appending `TORN_LINE` (cit:([`TORN_LINE`], mcp/tests/test_controlplane_store_durability.py:63-63)), and `_seed_gate` (cit:([`_seed_gate`], mcp/tests/test_controlplane_store_durability.py:218-228)) using state `open`
  because the projection keep-filter prunes the terminal states. **Filed one Todo, found by
  reading the cited source rather than the test:**
  `test_expectation_row_projection_degrades_instead_of_crashing` (cit:([`test_expectation_row_projection_degrades_instead_of_crashing`], mcp/tests/test_controlplane_store_durability.py:297-336)) says in its docstring
  that the tolerance lives in `observer/snapshots.read_expectation_rows`'s
  `contextlib.suppress(OSError, ValueError)` and that "today it degrades to the WHOLE log rather
  than to one row". That is the pre-fix arrangement. This leaf moved that wrapper onto
  `pending_for_projection()` (`snapshots.py` L592-L627; `expectation_rows.read_for_projection` /
  `pending_for_projection`), so degradation is now per row, and the source states the `suppress` "is no longer
  load-bearing for a malformed row". The test's only assertion is `assertIsInstance(rows, list)`,
  which passes under both behaviours — so the docstring is stale and the assertion does not pin
  what the leaf shipped. Reported, not repaired. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is blank because the source
  file is new and uncommitted; closeout owns its first stamp.