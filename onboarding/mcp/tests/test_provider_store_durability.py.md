# mcp/tests/test_provider_store_durability.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_provider_store_durability.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |                                                `df36127113619f4e85522eb615cc20c7eb637405`|
| lastVerifiedCommitDate | 2026-08-12T08:57:17+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The durability contract for the two JSONL record stores under `providers/` — `metrics.py`'s
`ProviderMetricsStore` and `degradation.py`'s `ProviderDegradationStore` — which 260731-EFA-L5's
first pass left off `ar-durable-store/1.0` on the strength of nothing but their directory. Same
shape as the six control-plane logs (append-only JSONL plus a reclaim pass that rewrites the file
whole), therefore the same defect. 20 tests in seven classes, most of them multiplied over
`PROVIDER_CASES` as subtests so a failure names the store.

The claim the suite exists to support is narrow and is worth stating in the form the suite can
defend: **these two stores lost records before and lose none now.** It supports that claim in the
only way a same-worktree fix allows — by extracting the leaf's base commit with `git archive` at
test time and proving the same instrument still detects loss there
cit:([`ProviderHarnessSensitivityTests`], mcp/tests/test_provider_store_durability.py:354-388). Without that class the zero is an unfalsifiable green; with it, the zero is a
measurement against a control the reviewer can re-run.

All assertion lives here; all mechanism lives in `_store_durability.py`, which is imported —
the same split as `test_controlplane_store_durability.py`.

## Code Commentary

### Logic

**cit:([`ProviderStoreDurabilityTests`], mcp/tests/test_provider_store_durability.py:280-351) — R10, three tests over real processes.**
cit:([`test_no_record_is_lost_when_an_append_races_a_compaction`], mcp/tests/test_provider_store_durability.py:283-294) drives the deterministic
`forced_lost_update` scenario over both `PROVIDER_CASES` and asserts `attempted == 1`, `lost == 0`
and no stragglers — forced rather than raced so the yes/no is the same on every machine.
cit:([`test_no_record_is_lost_under_sustained_multi_process_write_and_compaction`], mcp/tests/test_provider_store_durability.py:296-319) is the
unforced one: real processes, no interposition, and it additionally pins `attempted` to
`STRESS_PROFILE`'s `appenders × per_appender` (4 × 50 = 200) so a store that *raises* instead of
losing cannot shrink its own denominator, plus `torn_lines == 0`.
cit:([`test_concurrent_operation_never_raises_out_of_a_store_call`], mcp/tests/test_provider_store_durability.py:321-351) is deliberately separate
from the loss assertions and gets its own run against its own root, so the sibling's
"the run actually happened" guards do not cover it and are repeated. Its docstring names the
base-commit symptom for this pair specifically: `metrics.jsonl.compact.tmp`,
`metrics-current.json.tmp` and `degradation-events.jsonl.compact.tmp` carried no pid, so two
rewriters shared one temp path and one of them took `FileNotFoundError` out of a store call that
had reported nothing wrong.

**cit:([`ProviderHarnessSensitivityTests`], mcp/tests/test_provider_store_durability.py:354-388) — R14, and the property that makes the zero mean
anything.** cit:([`test_the_forced_scenario_detects_loss_in_the_base_commit`], mcp/tests/test_provider_store_durability.py:362-388) calls
`extract_base_commit_tree` to `git archive` `e52edaf5` into a temp directory **at test time**,
asserts the archive really contains `providers/metrics.py` and `providers/degradation.py`, runs
the forced scenario against it in a separate interpreter through `run_against_source`, and then
requires `dict.fromkeys(PROVIDER_CASES, 1)` — **each store loses exactly one record on the base
commit.** That is the whole argument for trusting the three zeros above: the suite proves its own
instrument can still detect the defect it claims to have fixed, in a worktree where the fix lands
beside the test and "I ran it before the fix" is not a thing a reviewer can re-check.

**cit:([`ProviderReadPolicyTests`], mcp/tests/test_provider_store_durability.py:391-571) — R8, why TOLERANT is the right answer for both logs.**
The leaf's rule is that every rewrite of an authority-bearing log reads strictly, and that a store
may rewrite from a tolerant read only when it carries no authority, because such a rewrite drops
the unreadable row *permanently*. Two structural facts put this pair outside the rule, and **both
are now asserted** — the class docstring
cit:(["each of them has a test here rather than a paragraph"], mcp/tests/test_provider_store_durability.py:391-414) claims that standard of evidence and now meets
it, having previously argued the second in prose:

1. **Neither rewrite parses.** `metrics.compact` reclaims from a raw byte tail (`_tail_lines`) and
   `degradation.compact_events` slices raw lines; both drop rows by **age**, never by content. So a
   row no reader can read is *retained* by the reclaim rather than deleted by it, and the
   permanent-drop cost the rule is about never arises.
   cit:([`test_neither_reclaim_deletes_a_row_it_could_not_parse`], mcp/tests/test_provider_store_durability.py:480-508) is the assertion that holds
   this: it appends `TORN_LINE` cit:([`TORN_LINE`], mcp/tests/test_provider_store_durability.py:117-117) to each log, runs each reclaim, and requires the torn line to
   still be present afterwards, on both logs, as subtests.
2. **Nothing is decided on the presence of a row**, in two halves with a test each.
   cit:([`test_the_metrics_consumer_writes_nothing_back_to_the_log_it_reads`], mcp/tests/test_provider_store_durability.py:510-548) runs the real
   consumer — `evaluate_provider_degradation` over a real config — and compares `metrics.jsonl`'s
   **bytes** before and after, so "nothing marks a row spent" is measured rather than asserted about.
   It is deliberately a *non-transition*: the previous state is seeded to `degraded` and the three
   seeded samples classify `degraded`, so the test also pins `verdict["state"] == "degraded"` (these
   rows really did decide something) and `verdict["event"] is None` (no event/alert/delivery path is
   dragged into a read-policy test).
   cit:([`test_nothing_outside_the_degradation_module_reads_the_event_log`], mcp/tests/test_provider_store_durability.py:550-571) covers the other
   half — `degradation-events.jsonl` has no production reader at all — as a claim about the
   *package* rather than the store: it walks every `*.py` under `PACKAGE_ROOT` and requires the set
   mentioning `events_path` or `degradation-events` to be exactly `["providers/degradation.py"]`.
   Neither log carries a marker whose *absence* permits something, which is what made a dropped
   `applied` gate row re-open a replay window.

The remaining three tests pin the tolerance itself:
cit:([`test_the_metrics_read_skips_only_the_row_it_cannot_read`], mcp/tests/test_provider_store_durability.py:427-448) interleaves a torn line, a non-object (`[1, 2, 3]`), a
cit:([`FUTURE_MAJOR_ROW`], mcp/tests/test_provider_store_durability.py:117-123) and whitespace between two real samples and requires the read to
return **both** real samples — per row, not per file, so an intact row written *after* a bad one
still survives; cit:([`test_a_row_with_no_schema_version_is_read_as_1_0`], mcp/tests/test_provider_store_durability.py:450-464) proves the stamping
is additive rather than a migration, on `metrics.jsonl` and `metrics-current.json` alike; and
cit:([`test_read_current_reports_nothing_it_cannot_interpret`], mcp/tests/test_provider_store_durability.py:466-478) requires a newer-major
current-state file to read as "no current sample" rather than be handed to the status packet as
though it were understood.

**cit:([`ProviderSchemaVersionTests`], mcp/tests/test_provider_store_durability.py:574-627).**
cit:([`test_every_row_this_build_writes_carries_its_schema_version`], mcp/tests/test_provider_store_durability.py:577-601) checks all three writes that produce a record — `record`,
`record_index_state`, `append_event` — plus `metrics-current.json`. Its counterpart,
cit:([`test_the_state_document_carries_no_schema_version`], mcp/tests/test_provider_store_durability.py:603-627), asserts the *absence* of the
field on `degradation-state.json` and states why: that file is a recomputed position rather than a
record, so a version on it would have no reader able to act on it, and the honest handling of an
unknown major on a state file is a decision this leaf did not make. It also asserts no `*.tmp` file
survives the rewrite.

**cit:([`ProviderOwnershipTests`], mcp/tests/test_provider_store_durability.py:630-723) — R2, the ownership decisions as assertions rather than as
prose in a rationale string.**
cit:([`test_both_provider_logs_declare_the_dashboard_their_compaction_owner`], mcp/tests/test_provider_store_durability.py:645-662) requires `compaction_owner == "dashboard"` on both `StoreOwnership` declarations and
that `is_compaction_owner()` tracks the declared process role in both directions — **named for what
it proves, after being named for what it did not**. Neither provider reclaim consults the predicate,
so this test alone would stay green if a second `compact` call site appeared in the MCP process.
cit:([`test_each_provider_reclaim_has_exactly_one_call_site`], mcp/tests/test_provider_store_durability.py:664-689) is what closes that: it asserts
cit:([`provider_reclaim_call_sites`], mcp/tests/test_provider_store_durability.py:162-191) equals exactly
`{"ProviderMetricsStore": ["serving/app.py::_metrics_loop"], "ProviderDegradationStore":
["providers/degradation.py::evaluate_provider_degradation"]}`, so the structural fact both
`PROVIDER_*_OWNERSHIP` rationales rest on is machine-checked rather than merely written down.
The scan counts **references, not calls** — `_metrics_loop` reaches `compact` through
`asyncio.to_thread(metrics_store.compact)`, and a scan insisting on `compact()` would find nothing
and report the property held. It resolves the receiver first (`_provider_store_locals`, L136-L157,
via `PROVIDER_RECLAIMS`, L105-L108) so that a bare `.compact` on one of the six other stores in the
tree that have one is not miscounted, and cit:([`_own_scope`], mcp/tests/test_provider_store_durability.py:126-135) refuses to descend into nested
functions so a reference is never attributed to two enclosing scopes.
cit:([`test_the_metrics_log_accepts_a_write_from_either_daemon`], mcp/tests/test_provider_store_durability.py:691-703) is the one that encodes the
two-process pairing: `record` (the dashboard's sampling loop) and `record_index_state` (the MCP's
provider-setup thread) must both pass the writer check, because both really happen.
cit:([`test_the_degradation_log_refuses_a_write_from_the_mcp_process`], mcp/tests/test_provider_store_durability.py:705-723) is the check that can
actually fire in this pair — `writers=("dashboard",)` — and it covers both of that store's writes,
the append and the state document.

**cit:([`ProviderReclaimShapeTests`], mcp/tests/test_provider_store_durability.py:726-801).** The reclaim's edges, including the failure mode this
pair never had:
cit:([`test_a_reclaim_with_no_log_yet_is_a_no_op`], mcp/tests/test_provider_store_durability.py:737-739) over both stores,
cit:([`test_no_reclaim_on_either_log_ever_unlinks_it`], mcp/tests/test_provider_store_durability.py:733-789), and
cit:([`test_the_reclaim_keeps_the_newest_rows_and_returns_how_many`], mcp/tests/test_provider_store_durability.py:791-801), which pins that
retention goes by age (`seq` 15-19 kept of 20) and is unchanged by this leaf.
The unlink test drives **both stores through both paths**, which is what makes it worth its name:
an empty log first, where `compact` returns at `if not kept` and `compact_events` at its row cap —
*before* either reaches `rewrite_lines` — and then twenty rows apiece so the same `exists()`
assertion is made over a reclaim that really does rewrite. Its docstring states precisely what it
cannot catch: an `unlink` placed immediately before `rewrite_lines`' `os.replace` is invisible to
`exists()` and indistinguishable from the inode swap the rewrite performs by design. Safety against
that is a property of `append_line` re-opening under the lock per record, not of this test.

**cit:([`ProviderCaseRegistryTests`], mcp/tests/test_provider_store_durability.py:804-813).** One test, and it is a boundary rather than a
behaviour: `PROVIDER_CASES == ("provider_metrics", "provider_degradation")`, it is **disjoint from
`CASES`**, and both adapters declare `torn_line_policy == "tolerant"`. It imports `CASES` inside
the test body rather than at module import.

### Conventions

**`PROVIDER_CASES` is kept separate from `CASES` on purpose, and this file owns the assertion that
keeps it so.** The two provider adapters were added to the *shared* instrument
cit:([`ProviderMetricsAdapter`, `ProviderDegradationAdapter`], mcp/tests/_store_durability.py:419-465; mcp/tests/_store_durability.py:468-527), which is what lets them reuse the scenarios, the raw on-disk
accounting and the base-commit archive. But `CASES` still enumerates only the six control-plane
adapters and `PROVIDER_CASES` only the two provider ones
cit:([`PROVIDER_CASES`], mcp/tests/_store_durability.py:596-596) — so widening the instrument
does not silently widen what `test_controlplane_store_durability.py` asserts. Each suite names the
stores it speaks for, and `ProviderCaseRegistryTests` fails the moment that stops being true.

**The numbers are a direction, not a rate, and nothing here asserts one.** Three mutually
incompatible loss figures for this pair at the same base commit are in circulation, and the module
docstring cit:(["Seven classes pin seven things"], mcp/tests/test_provider_store_durability.py:1-59) carries several of them and then disclaims them in the same breath: an early
two-appender / 800-record measurement, a re-measurement of that *same named shape* against a
`git archive` once `harness_work_dir` was fixed, and a third against `STRESS_PROFILE` as shipped.
They disagree by more than an order of magnitude because each run used a different pacing and none
of them recorded it — the figures do not follow from the two knobs the file does declare. **This
card asserts none of them, and neither does any test in the file.** What is stable, and what every
assertion actually rests on: these stores lost records at the base commit and lose none now. That is
exactly what the file pins â `lost == 0` and `torn_lines == 0` against an `attempted` fixed to
`STRESS_PROFILE`'s `appenders × per_appender` (4 × 50 = 200), so a store that *raises* instead of
losing cannot shrink its own denominator into a green. The rate was never the finding; the direction
was, and `ProviderHarnessSensitivityTests` is what re-establishes the direction on every run.

**`providers/metrics.py` and `providers/degradation.py` quote no loss rate either, and say why.**
Both module headers now state the direction only â accepted records were lost and now none are â
and name `ProviderHarnessSensitivityTests` against a `git archive` of the base commit as what
re-establishes it each run. The one percentage still in `degradation.py` is not this log's: it is
the 31.45% the earlier draft measured on *attention-dismissals and supervisor-signals* when it left
them unlocked on the strength of single-writer, cited as the precedent for locking a single-writer
log rather than as a figure for `degradation-events.jsonl`.

**One throwaway store tree per (scenario, case).** `_TempRootTest.case_root`
cit:([`_TempRootTest`, `case_root`], mcp/tests/test_provider_store_durability.py:256-277) returns
`tmp/<scenario>/<case>/observer`, and its docstring records that the *parent* used to matter too —
`run_stress` kept its stop flag in `root.parent/harness`, so sibling roots under one parent shared
one flag and every case after the first left the tick loop after a single tick, reporting a green
measured over almost nothing on the unfixed tree as readily as on the fixed one. Discovered here,
worked around here, then fixed at the source: `harness_work_dir`
cit:([`harness_work_dir`], mcp/tests/_store_durability.py:876-903) now derives the
scratch directory from `root` itself, and `MIN_SUCCESSFUL_RECLAIMS`
cit:([`MIN_SUCCESSFUL_RECLAIMS`], mcp/tests/_durability_measurement.py:11-11) refuses a result whose
reclaimer barely ran for any other reason. What remains in this file is the ordinary requirement
that separate runs get separate stores.

**The reclaim-tick floor is not asserted locally, deliberately.** This file's original
`reclaim_ticks > 1` moved into the instrument as `MIN_SUCCESSFUL_RECLAIMS = 10`, so it now applies to
every caller of `run_stress` — including the control-plane suite that did not have it and the
base-commit script entry point that could not have had it. cit:([`_describe`], mcp/tests/test_provider_store_durability.py:242-253) carries the tick
count into every failure message regardless.

**`forced` and `stress` are kept as separate scenarios for separate jobs.** The forced one produces
a yes/no a loaded CI box cannot blur; the stress one is the only one that produces a rate.

### Invariants And Boundaries

- Loss and raising are asserted separately and must stay that way. A fix that converts silent loss
  into an exception has moved the failure, not repaired it, and only
  `test_concurrent_operation_never_raises_out_of_a_store_call` can see that.
- The tolerant read policy on both logs is conditional on the two structural facts above. If either
  reclaim ever starts filtering by parsing, or if any consumer starts deciding on a row's presence,
  the read on that store has to become strict **in the same change**. `metrics._parse_row` carries
  that escalation clause in its own docstring, and
  `test_neither_reclaim_deletes_a_row_it_could_not_parse` is the assertion that fires on the first
  half of it.
- Neither store appears in the harness's `forced_unlink` scenario, and that is a finding rather
  than an omission: neither reclaim has an unlink branch to begin with — `compact` returns 0 when
  the kept set is empty and `compact_events` when the log is under its cap, at the base commit
  included. Failure mode #2 was never present in this pair.
- The sensitivity proof depends on `e52edaf5` being reachable from this worktree's repository at
  test time. That is a git-history dependency, not only a code one.
- This suite spawns real processes and runs a stress profile per store; it is not a unit test, and
  its wall-clock cost is bounded by `STRESS_PROFILE['timeout']` per store plus the reclaimer's tick
  budget.
- The `setUp` method on `ProviderOwnershipTests` opens `preserve_owned_mutable_state()` and registers its closeout,
  explicitly containing the class's direct `declare_process_role` calls. The suite-wide
  `reject_owned_global_state_leaks` autouse guard remains a backstop that restores registered state
  and fails any test that leaks it outside an explicit preservation scope.
- `test_each_provider_reclaim_has_exactly_one_call_site` is STATED, NOT CLOSED, and the boundary is
  recorded in `provider_reclaim_call_sites`' own docstring rather than only here. The scan attributes
  a reclaim to a store only when the receiver is a **local of the same function** — a parameter
  annotated with the class, or an assignment from its constructor. Both call sites in the tree today
  take one of those two shapes. A reclaim reached through an attribute (`self._store.compact()`),
  through a module-level global, or from a nested closure relying on an enclosing binding would not
  be attributed to a store and would not be seen. Which half of the ownership claim is
  machine-checked is therefore a property of that resolver, and it is the half the tree exercises.

### Todos

**None open. The four this card previously filed are all closed in the source, and each was closed
by the assertion it asked for rather than by rewording the claim.** Recorded here because the fix
is the useful fact, not the ticket:

1. *`ProviderReadPolicyTests` claimed both structural facts were asserted and only fact 1 was.*
   Fact 2 now has both halves under test —
   cit:([`test_the_metrics_consumer_writes_nothing_back_to_the_log_it_reads`], mcp/tests/test_provider_store_durability.py:510-548) and
   cit:([`test_nothing_outside_the_degradation_module_reads_the_event_log`], mcp/tests/test_provider_store_durability.py:550-571) — and the class
   docstring cit:(["each of them has a test here rather than a paragraph"], mcp/tests/test_provider_store_durability.py:391-414) says so in the same words it used to argue in.
2. *`test_the_dashboard_compacts_both_provider_logs` was named for a claim it did not make.* Renamed
   cit:([`test_both_provider_logs_declare_the_dashboard_their_compaction_owner`], mcp/tests/test_provider_store_durability.py:645-662), which is what
   it actually proves, and the claim it did not make is now made by
   cit:([`test_each_provider_reclaim_has_exactly_one_call_site`], mcp/tests/test_provider_store_durability.py:664-689). The second `compact` call site
   from the MCP process that used to leave the pair green now fails it.
3. *`test_a_reclaim_that_keeps_nothing_leaves_the_log_in_place` drove one store through one path.*
   Renamed cit:([`test_no_reclaim_on_either_log_ever_unlinks_it`], mcp/tests/test_provider_store_durability.py:733-789) and widened to both stores
   through both paths — the keeps-nothing early return *and* a reclaim that actually rewrites — so
   the assertion is no longer confined to code above `rewrite_lines`.
4. *The module docstring enumerated "four things pinned here" while the file had seven classes.* It
   now reads "Seven classes pin seven things" and enumerates all seven
   cit:(["Seven classes pin seven things"], mcp/tests/test_provider_store_durability.py:29-51), stating outright
   that a list naming four of seven reads as coverage for the three it omits.

The one thing deliberately left open is a **boundary rather than a defect**, and it is recorded in
the Invariants above and in `provider_reclaim_call_sites`' own docstring: the call-site scan resolves
receivers bound as locals only. It is stated in the source rather than closed, because threading
enclosing scopes and attribute chains through the resolver would buy a guard against call-site
shapes nothing in this tree writes.

## Docs References

No Domain Documentation source is configured for this repository; the contract asserted here is the
repository-local `ar-durable-store/1.0` front matter in `controlplane/durable_store.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite asserts against the two shipped provider stores through one shared instrument; the rows
below are the code each claim is about.

| Finding | Anchor | Source |
| --- | --- | --- |
| The metrics store under test: the tolerant per-row read and its escalation clause, the reclaim that holds one lock across stat + tail + rewrite and drops rows by age only, the two appends that make the pairing two-process, the lock-free tail read, and the ownership declaration. | `_parse_row`; `compact`; `record`; `record_index_state`; `read_recent`; `PROVIDER_METRICS_OWNERSHIP` | mcp/src/agents_remember/providers/metrics.py:65-83; mcp/src/agents_remember/providers/metrics.py:302-341; mcp/src/agents_remember/providers/metrics.py:191-228; mcp/src/agents_remember/providers/metrics.py:254-267; mcp/src/agents_remember/providers/metrics.py:269-283; mcp/src/agents_remember/providers/metrics.py:343-360 |
| The degradation store under test: the single-writer ownership declaration whose `check_declared_writer` can actually fire, the count-based reclaim under one held lock, the stamped append, and the state document that is deliberately unversioned. | `PROVIDER_DEGRADATION_OWNERSHIP`; `write_state`; `append_event`; `compact_events` | mcp/src/agents_remember/providers/degradation.py:84-103; mcp/src/agents_remember/providers/degradation.py:233-253; mcp/src/agents_remember/providers/degradation.py:190-215; mcp/src/agents_remember/providers/degradation.py:217-231 |
| The contract both stores were moved onto: the unconditional per-log lock, the never-unlinking rewrite, the version policy the reads implement, and the role declaration the ownership tests drive. | `exclusive_access`; `append_line`; `rewrite_lines`; `SCHEMA_VERSION`; `schema_version_supported`; `StoreOwnership`; `declare_process_role`; `CompactionOwnerError` | mcp/src/agents_remember/controlplane/durable_store.py:46-46; mcp/src/agents_remember/controlplane/durable_store.py:66-67; mcp/src/agents_remember/controlplane/durable_store.py:77-85; mcp/src/agents_remember/controlplane/durable_store.py:93-133; mcp/src/agents_remember/controlplane/durable_store.py:227-248; mcp/src/agents_remember/controlplane/durable_store.py:391-446; mcp/src/agents_remember/controlplane/durable_store.py:477-488; mcp/src/agents_remember/controlplane/durable_store.py:491-498 |
| The two-process pairing asserted by `ProviderOwnershipTests`, as it actually runs: the dashboard loop that samples, records, evaluates degradation and then compacts. It is also the metrics reclaim's one call site, and it reaches it as `await asyncio.to_thread(metrics_store.compact)` — a reference rather than a call, which is why `provider_reclaim_call_sites` counts references. | "async def _metrics_loop(config: McpRuntimeConfig" | mcp/src/agents_remember/serving/_app_lifespan.py:57-57 |
| The other half of that pairing: the MCP process's provider-setup thread appending index-lifecycle rows into the same log. | `_record_index_state` | mcp/src/agents_remember/providers/provider_setup.py:434-453 |
| The consumer that makes the metrics log's tolerant read structurally safe: the whole state machine is re-derived from a rolling window of live samples and nothing is consumed. | `evaluate_provider_degradation` | mcp/src/agents_remember/providers/degradation.py:268-323 |
| The control-plane suite over the same instrument, whose `CASES` this file's `PROVIDER_CASES` is asserted to be disjoint from, and whose base-commit class this file's mirrors. | `MultiProcessDurabilityTests`; `HarnessVacuityGuardTests`; `HarnessSensitivityTests` | mcp/tests/test_controlplane_store_durability.py:123-205; mcp/tests/test_controlplane_store_durability.py:339-386; mcp/tests/test_controlplane_store_durability.py:389-444 |
| The `setUp` method on `ProviderOwnershipTests` explicitly contains its direct process-role declarations with `preserve_owned_mutable_state`; the autouse `reject_owned_global_state_leaks` guard is the suite-wide backstop. | "class ProviderOwnershipTests(_TempRootTest):"; "from _global_state import preserve_owned_mutable_state"; `reject_owned_global_state_leaks` | mcp/tests/conftest.py:118-129; mcp/tests/test_provider_store_durability.py:71-71; mcp/tests/test_provider_store_durability.py:638-638 |

## Cross-Repo References

No meaningful cross-repo references found: both stores, the instrument and the base-commit archive
are inside `agents-remember`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
  disjoint set cit:([`PROVIDER_CASES`], mcp/tests/_store_durability.py:596-596), so widening the instrument cannot silently widen
  what `test_controlplane_store_durability.py` asserts — and `ProviderCaseRegistryTests`
  cit:([`ProviderCaseRegistryTests`], mcp/tests/test_provider_store_durability.py:804-813)
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
