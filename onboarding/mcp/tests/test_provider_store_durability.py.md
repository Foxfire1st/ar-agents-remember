# mcp/tests/test_provider_store_durability.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_provider_store_durability.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Runs the actual append-versus-compaction race for both provider JSONL stores through the shared durability harness. The forcing point compares successful receipt records with durable disk contents so neither concurrent record can disappear. This file retains one test method with provider cases, not the old twenty-test stress and measurement inventory.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No record is lost when an append races a compaction | `test_no_record_is_lost_when_an_append_races_a_compaction` | mcp/tests/test_provider_store_durability.py:45-52 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-06T00:42:13+00:00 — Gate-5 claim re-review against C97: reconciled current durable-store/kernel locking ownership and exact source evidence. The test or harness source bytes match the prior verified source; verification advances for the reopened claim review.

- 2026-08-26T10:44:52+02:00 — Classified provider durability proofs into explicit integration and stress evidence lanes; the underlying loss, exception, and sensitivity assertions are unchanged.

- 2026-08-24T21:23+02:00 — No content impact: the owned-state context manager moved from the test
  tree to `agents_remember_test_support.testing.global_state`; provider durability behavior is unchanged.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 citation maintenance: re-anchored shared durability and global-state-fixture evidence after the focused test cleanup; provider durability claims are unchanged.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: deduplicated the metrics/degradation
  store rows; rebound the instrument row to the renamed reclaim floor (`MIN_SUCCESSFUL_RECLAIMS`
  in `_durability_measurement.py`, replacing the deleted `MIN_RECLAIM_TICKS`) with corrected
  adapter, case-list, work-directory, stress-profile and archive extents; generated the final
  ranges for the S18-T3 preservation row (test file 630-643 + conftest.py 78-89); converted the
  19 superseded prose citations (including four inside history entries) to cit form at current
  ranges; and renamed the two live `MIN_RECLAIM_TICKS` prose mentions. Zero findings remain.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: replaced the removed fixture claim with the
  class-owned preservation scope and suite-wide leak-detection backstop. New ranges are explicit
  `:1-1` curator input.

- 2026-08-01T20:45+02:00 — 260731-EFA-L5 worker: **repointed the card onto the suite as it now
  stands — 20 tests in seven classes, not 17 in six — and recorded the substance behind the three
  renames rather than only the names.** Every line citation into this file was re-derived from the
  file itself and each range's **end** re-checked against every symbol its claim names; the reported
  anchors (≈104, 116, 204, 212, 290, 292) were not trusted, and they could not have been — the whole
  file had moved by about +145 lines, so the *entire* set of self-citations was stale, not just the
  three around the renames. (1) `test_the_dashboard_compacts_both_provider_logs` →
  cit:([`test_both_provider_logs_declare_the_dashboard_their_compaction_owner`], mcp/tests/test_provider_store_durability.py:645-662), joined by a new
  cit:([`test_each_provider_reclaim_has_exactly_one_call_site`], mcp/tests/test_provider_store_durability.py:664-689). That new test is the one that
  matters: cit:([`provider_reclaim_call_sites`], mcp/tests/test_provider_store_durability.py:162-191) is an **AST scan that resolves receivers bound
  to the two store classes** and counts **references, not calls**, because the real metrics call site
  is `await asyncio.to_thread(metrics_store.compact)` and a scan insisting on `compact()` would find
  nothing and report the property held. So the "exactly one caller"
  sentence both `PROVIDER_*_OWNERSHIP` rationales rest on is machine-checked now instead of merely
  written down. (2) `test_a_reclaim_that_keeps_nothing_leaves_the_log_in_place` →
  cit:([`test_no_reclaim_on_either_log_ever_unlinks_it`], mcp/tests/test_provider_store_durability.py:733-789), now driving **both stores through both
  paths** — the keeps-nothing early return *and* a reclaim that actually rewrites — so the assertion
  is no longer confined to code above `rewrite_lines`. (3) `ProviderReadPolicyTests` gained
  cit:([`test_the_metrics_consumer_writes_nothing_back_to_the_log_it_reads`], mcp/tests/test_provider_store_durability.py:510-548) and
  cit:([`test_nothing_outside_the_degradation_module_reads_the_event_log`], mcp/tests/test_provider_store_durability.py:550-571), which assert what
  the class docstring previously only argued; **all four Todos this card filed are therefore closed**,
  the fourth by the module docstring itself, which no longer says "four things are pinned here" over
  a file of seven classes but enumerates all seven
  cit:(["Seven classes pin seven things"], mcp/tests/test_provider_store_durability.py:29-51). The Todos section now records the
  closures and the one boundary deliberately left open — `provider_reclaim_call_sites` resolves
  receivers bound as locals only, stated in its own docstring rather than closed, and now also an
  Invariant here. **Numbers, restated as the source now has them:** neither `providers/metrics.py`
  nor `providers/degradation.py` quotes a loss rate for its own log any more; both state the
  direction only — accepted records were lost and now none are — and name
  `ProviderHarnessSensitivityTests` against a `git archive` of the base commit as what re-establishes
  it each run. No rate is quoted on this card, and the "0 of 200 across four runs" phrasing was
  replaced by what the file actually asserts (`lost == 0`, `torn_lines == 0`, `attempted` pinned to
  `STRESS_PROFILE`'s 4 × 50), since the run count was not something a reader could re-derive. The one
  percentage still in `degradation.py` is flagged for what it is: the 31.45% measured on
  *attention-dismissals and supervisor-signals*, cited as the precedent for locking a single-writer
  log, not a figure for `degradation-events.jsonl`. **Citations repaired**, each re-opened and checked
  end-first: `providers/metrics.py` — `PROVIDER_METRICS_OWNERSHIP` L65-L83, `_parse_row` L191-L228,
  `record` L254-L267, `record_index_state` L269-L283, `compact` L302-L341, `read_recent` L343-L360;
  `providers/degradation.py` — `PROVIDER_DEGRADATION_OWNERSHIP` L85-L104, `write_state` L191-L216,
  `append_event` L218-L232, `compact_events` L234-L254, `evaluate_provider_degradation` L260-L311;
  `_store_durability.py` — the case lists tightened from L525-L545 to L540-L544, which is the comment
  plus `CASES` and `PROVIDER_CASES` and ends on the second of them (the provider adapters L401-L522,
  `harness_work_dir` L790-L817, `MIN_RECLAIM_TICKS` L826-L841, `STRESS_PROFILE` L1040-L1047,
  `extract_base_commit_tree` L1069-L1093 and `run_against_source` L1096-L1118 all re-checked and
  correct); `conftest.py` — `restore_declared_process_role` L57-L87, whose cited end had stopped two
  lines short of the fixture's own body. Rows into `controlplane/durable_store.py` remain **by symbol
  name with no line range**. `serving/app.py` L806-L818 and `providers/provider_setup.py` L434-L453
  were re-opened and are correct. Verification metadata untouched — the source is uncommitted and
  closeout owns the first stamp.
- 2026-08-01T16:15+02:00 — 260731-EFA-L5 curator: created the card for the provider-store
  durability suite — 17 tests in six classes, most multiplied over `PROVIDER_CASES` as subtests,
  proving that `providers/metrics.py` and `providers/degradation.py` no longer lose records now
  that they are on `ar-durable-store/1.0`. **The property that makes the zero meaningful** is
  `ProviderHarnessSensitivityTests`
  cit:([`ProviderHarnessSensitivityTests`], mcp/tests/test_provider_store_durability.py:354-388): it `git archive`s the leaf's base commit **at test
  time**, asserts the archive really contains both provider modules, runs the forced scenario
  against it in a separate interpreter, and requires each store to lose exactly one record there —
  so the suite proves its own instrument can still detect the defect it claims to have fixed,
  rather than resting on anyone's memory of a pre-fix run in a worktree where the fix lands beside
  the test. **Numbers handled as direction, never as rate:** three mutually incompatible loss
  figures for this pair at the same base commit are in circulation because each run used a
  different pacing and none recorded it; the module docstring carries several and disclaims them,
  and this card asserts none of them. What is recorded is what is stable and what the assertions
  rest on — these stores lost records before and lose none now, 0 of 200 per store per run
  (`STRESS_PROFILE`'s 4 × 50) across four runs and 0 at four times the volume. **Recorded the
  case-list separation as a contract rather than as tidiness:** the provider adapters joined the
  shared instrument, but `CASES` stays the six control-plane stores and `PROVIDER_CASES` is its own
  disjoint set cit:([`PROVIDER_CASES`], mcp/tests/_store_durability.py:595-595), so widening the instrument cannot silently widen
  what `test_controlplane_store_durability.py` asserts — and `ProviderCaseRegistryTests`
  cit:([`ProviderCaseRegistryTests`], mcp/tests/test_provider_store_durability.py:817-826)
  is the assertion that fails if that stops holding. **Recorded the tolerance argument
  structurally**, in the two halves the leaf's rule turns on: neither rewrite parses (both drop rows
  by age from raw lines, so a row no reader can read is retained rather than deleted — pinned by
  `test_neither_reclaim_deletes_a_row_it_could_not_parse`, L322-L350), and nothing is decided on a
  row's presence, with `metrics._parse_row`'s escalation clause naming what would end that. **Filed
  four Todos, all found by reading the code rather than the test names:** (1) `ProviderReadPolicyTests`'
  docstring claims both structural facts are asserted rather than argued, but only the
  no-parsing-rewrite half has a test — the "nothing is decided on a row" half is argued in prose, and
  is true (checked against `evaluate_provider_degradation`'s rolling-window read, and against there
  being no reference to `events_path` outside `providers/degradation.py`); (2)
  `test_the_dashboard_compacts_both_provider_logs` proves the two ownership *declarations* and the
  predicate, not who calls `compact` — neither provider reclaim consults the predicate at all, as
  both rationales state; (3) `test_a_reclaim_that_keeps_nothing_leaves_the_log_in_place` drives only
  the metrics store though its docstring speaks for both, and on an empty log `compact` returns
  before reaching `rewrite_lines`, so it cannot see an unlink introduced into the shared rewrite;
  (4) the module docstring's "four things are pinned here" omits three of the six classes. Reported,
  not repaired. **Citations:** every row was opened and checked against each symbol the claim names,
  **ends included**. Rows into `controlplane/durable_store.py` are cited **by symbol name with no
  line range** — that module grew ~100 lines mid-leaf and every earlier range into it was
  invalidated, so the symbol is the durable anchor and its own file card is authoritative for line
  numbers. Verification metadata is blank because the source file is new and uncommitted; closeout
  owns its first stamp.
