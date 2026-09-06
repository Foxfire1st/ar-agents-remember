# mcp/tests/_store_durability.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                       |
| path                   | `mcp/tests/_store_durability.py`      |
| doc_type               | `file-level-onboarding`               |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview      | `overview.md`                         |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces one append into the read-to-replace compaction window of eight real JSONL stores. It is shared test support, not an assertion suite. Six controlplane adapters and two provider adapters call each store’s actual write/reclaim owners; the harness reports receipts versus durable records.

## Code Commentary

### Logic

`run_forced_lost_update` seeds a non-prunable anchor, forks a reclaimer and appender, and parks the
actual rewrite at a controlled rendezvous. The decoy is written before arming so a write that is
itself read-modify-write cannot trigger the hook prematurely. Bounded handoff and joins allow
correct locking to serialize the append without leaving child processes hung.

Successful append receipts are stored separately from store bytes. `surviving_ids` parses durable
records and counts torn lines; `_forced_result` reports attempted/surviving/lost records, errors
and stragglers. `harness_work_dir` derives a unique sibling directory from each exact root, so
sibling stores do not share receipt state. A zero-loss figure must be read alongside the actual
attempted count and errors.

### Invariants And Boundaries

- The anchor is never counted and keeps reclamation on the rewrite path instead of empty-log deletion.
- All eight adapters exercise real store behavior; no copied reclaim algorithm substitutes for it.
- Historical source extraction, model-path compatibility, stress loops and measurement CLI were removed.
- There is no import fallback for GateState; the canonical structural model is imported directly.
- Current controlplane/provider durability tests own the assertions, not this harness.

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared real-store write/reclaim boundary | `StoreAdapter` | mcp/tests/_store_durability.py:76-107 |
| Provider stores share the same instrument | `ProviderStoreAdapter` | mcp/tests/_store_durability.py:328-338 |
| Independent durable-record/torn-line accounting | `surviving_ids` | mcp/tests/_store_durability.py:461-486 |
| Controlled actual rewrite rendezvous | `parked_rewrite` | mcp/tests/_store_durability.py:495-539 |
| Per-root receipt isolation | `harness_work_dir` | mcp/tests/_store_durability.py:603-605 |
| Forked append/reclaim orchestration and bounded joins | `run_forced_lost_update` | mcp/tests/_store_durability.py:636-669 |

## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T00:42:13+00:00 — Gate-5 claim re-review against C97: reconciled current durable-store/kernel locking ownership and exact source evidence. The test or harness source bytes match the prior verified source; verification advances for the reopened claim review.

- 2026-09-05T22:25+00:00 — L30 incoming-reference review: projected the retained source-backed claim to its current owner extent; preserved this unchanged source file's genuine verification hash/date.


- 2026-08-13T12:53+02:00 — No content impact: the stabilized test-root form reads the already
  imported package from `sys.modules["agents_remember"].__file__` instead of adding either a bare
  package import or a direct member import. The same source-root refusal and durability scenarios
  remain unchanged; this supersedes the 12:26 import-shape note and leaves provenance closeout-owned.

- 2026-08-13T12:26+02:00 — No content impact: the final Ruff-safe form imports
  `agents_remember.__file__` directly as `agents_remember_file` and uses that alias for the same
  source-root refusal. This avoids environment-dependent bare-package classification without
  changing any measured store, fixture, assertion, or durability contract; verification
  provenance remains closeout-owned.

- 2026-08-13T11:57+02:00 — No content impact: Ruff I001 moved the `agents_remember` import below
  the test-helper and package imports without changing any executable statement, fixture, adapter,
  assertion, or durability contract. Sanctioned citation repair updated the resulting line-only
  shifts; verification provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 extracted and directly tested the cross-version `GateState` resolver: current structural models win, only the precisely absent structural package selects the historical sensitivity-fixture path, and unrelated import errors remain loud.
- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: documented the
  `TYPE_CHECKING`-safe current `GateState` import and the narrowly justified historical-archive
  runtime fallback; this is test-harness compatibility, not a production compatibility surface.

- 2026-08-11T14:29+02:00 — Re-read the shared `rewrite_lines` implementation and regenerated
  its range around the current declaration; verification metadata remains unchanged for governed
  closeout.

- 2026-08-10T10:40+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-09T21:54+02:00 — 260713-TES master integration repair: split source-tree pinning,
  base-archive rename compatibility, and pinned-subprocess execution into the new bounded
  `_store_durability_source.py` helper. This module remains the executable harness and preserves
  its import surface by re-exporting `extract_base_commit_tree` and `run_against_source`; the
  split is structural only and clears the 1,200-line integration rail.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 23 repeated path:start-end Citation objects from 4 same-claim citation group(s) at card line(s) 306, 308, 309, 317; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0. Preserved the two separate line-157 prose citations byte-for-byte; neither was part of this single-claim dedupe.
- 2026-08-02T20:52:54+02:00 — 260731-EFA-L6 W2-B12 Luna-max curator. Curated **50 citation findings** in this card: 40 legacy prose citations, 8 anchors absent from their cited ranges, 1 missing table anchor, and 1 malformed table source. Scoped `--fix` repaired 77 claims and normalised 4; the pinned scoped recheck now reports **0 findings**. Verification metadata was not refreshed, and no code, shared index, route index, entity register, task state, or other onboarding document was changed.
- 2026-08-01T19:40+02:00 — 260731-EFA-L5 curator. **The card was silent about a defect in the
  instrument itself, which is the one thing a reader landing here needs first**, so it gained a
  section ahead of Logic: *The Instrument's Own Defect, Its Fix And Its Guard*. **The defect** —
  the harness derived its work directory, including the reclaimer's stop flag, from `root.parent`;
  `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`
  (`self.tmp / f"stress-{case}"`, cit:(["stress-"], mcp/tests/test_controlplane_store_durability.py:169-169)), so every case shared one flag and, since
  cit:([`_reclaimer_main`], mcp/tests/_store_durability.py:654-680) tests `stop.exists()` at the bottom of each tick, every case after
  the first left the loop after ONE tick: **25 reclaim ticks for the first store and exactly 1 for
  each of the other seven, all eight reporting 0.00% loss**. Recorded the second consequence too:
  the forced scenarios shared `forced.id` and the `*.err` names (cit:([`run_forced_lost_update`, `run_forced_unlink`], mcp/tests/_store_durability.py:987-1022; mcp/tests/_store_durability.py:1025-1061)) that
  cit:([`_forced_result`], mcp/tests/_store_durability.py:987-1006) reads back, so a case whose appender wrote nothing was scored off
  its predecessor's receipts. **The fix** — cit:([`harness_work_dir`], mcp/tests/_store_durability.py:853-880) returns
  `root.with_name(root.name + "-harness")`, a *sibling*, chosen over a child because `root` does
  not name one place: control-plane logs resolve under `root/workspace`
  (`StoreAdapter.log_path`, cit:([`StoreAdapter`], mcp/tests/_store_durability.py:115-172)), provider logs under `root/logs/observer/providers`
  (`ProviderStoreAdapter.log_path`, cit:([`ProviderStoreAdapter`], mcp/tests/_store_durability.py:447-457)), and `GateStore` additionally globs
  `root/lifecycles/*/gates.jsonl`, while cit:([`surviving_ids`], mcp/tests/_store_durability.py:583-608) reads that whole tree as raw
  bytes. **The guard** — `MIN_SUCCESSFUL_RECLAIMS = 10` (cit:([`MIN_SUCCESSFUL_RECLAIMS`], mcp/tests/_durability_measurement.py:11-11)) raising `VacuousRunError`
  (cit:([`VacuousRunError`], mcp/tests/_durability_measurement.py:14-15)) from cit:([`require_stress_measurement`], mcp/tests/_durability_measurement.py:18-55) at the end of `run_stress` (cit:([`run_stress`], mcp/tests/_store_durability.py:889-962)),
  **in the instrument rather than in either suite**, so the control-plane suite, the provider
  suite and bare `main()` script runs (cit:([`main`], mcp/tests/_store_durability.py:1123-1136)) share one floor; evidence-based at 22-39 ticks
  idle and 34-49 under 24-way load — load raises the count — with 20 rejected because the observed
  minimum is 22. **The principle** is stated as an invariant: *a measurement must refuse to report
  a vacuous result*, beside its companion that *sibling roots under one temp directory must remain
  legitimate*, since a guard demanding distinct parents would be the same defect rewritten as a
  convention. **The reassuring half is recorded beside it**: the documented base-commit rates
  survived, re-measured at attention 23.91% / gate 9.38% / supervisor-signals 8.00% /
  expectation-rows 7.63% / nudges 7.50% / operator-inbox 0.00%, same ordering and same lone
  survivor — because `main` already built each case a root under its own parent
  (`<root>/run{n}/{case}/observer`, cit:([`main`], mcp/tests/_store_durability.py:1123-1136)). The bug never corrupted the historical
  measurements; it hollowed out the ongoing regression. **Those six figures are labelled as this
  leaf's four-run means that do NOT appear in the source**: the source carries *ranges*, in
  `test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring (cit:([`HarnessSensitivityTests`], mcp/tests/test_controlplane_store_durability.py:345-401)), and each mean was checked to fall inside its own range. Also added, per
  the leaf's request: the dual-mode boundary restated with cit:([`_require_source_root`], mcp/tests/_store_durability.py:1118-1125)
  and the `__main__` guard (cit:(["__main__"], mcp/tests/_store_durability.py:1145-1145)); `surviving_ids` as a tolerant reader returning two
  quantities that are never summed; and the **three record classes** — `survivor-*` (counted,
  cit:([`surviving_ids`], mcp/tests/_store_durability.py:583-608)), `decoy-*` (`StoreAdapter.reclaim`, cit:([`StoreAdapter`], mcp/tests/_store_durability.py:115-172)) and `anchor-keepalive` (`seed`,
  cit:([`StoreAdapter`], mcp/tests/_store_durability.py:115-172), omitted by `run_forced_unlink` at cit:([`run_forced_unlink`], mcp/tests/_store_durability.py:1025-1061)) — which is what makes "loss" mean *a
  row nobody decided to drop*. **Drift repaired while here:** the file has grown to 1153 lines and
  **every line citation in this card was stale**, so all were re-derived against the current file;
  the card also described six stores and two consumers, where the instrument now covers **eight**
  (the two `providers/` stores through `ProviderStoreAdapter`, cit:([`ProviderDegradationAdapter`], mcp/tests/_store_durability.py:489-551)) and is imported by
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
  executable as a script whose `main` (cit:([`main`], mcp/tests/_store_durability.py:1123-1136)) reads a JSON config, with `_require_source_root`
  (cit:([`_require_source_root`], mcp/tests/_store_durability.py:1118-1125)) raising `SystemExit` unless `agents_remember` resolved under the tree the caller
  named, which is what let `run_against_source` (cit:([`run_against_source`], mcp/tests/_store_durability_source.py:108-132)) measure a `git archive` of
  `e52edaf5` (`BASE_COMMIT`, cit:([`BASE_COMMIT`], mcp/tests/_store_durability_source.py:14-14), `extract_base_commit_tree`, cit:([`extract_base_commit_tree`], mcp/tests/_store_durability_source.py:79-105)) with `PYTHONPATH` pinned;
  (2) **separate loss and torn accounting** — `surviving_ids` (cit:([`surviving_ids`], mcp/tests/_store_durability.py:583-608)) is a raw tolerant
  JSON-lines reader, deliberately not the store's own `read`, returning `(survivor ids present,
  unparseable line count)` so a strict reader cannot turn a measurement into an exception and a
  tolerant one cannot report a torn line as a lost record, paired with `_appender_main`
  (cit:([`_appender_main`], mcp/tests/_store_durability.py:617-650)) journalling an id only after the store call returned; (3) **real processes** —
  `_context()` (cit:([`_context`], mcp/tests/_store_durability.py:852-853)) is `multiprocessing.get_context("fork")` because the defect is
cross-process and the GIL would serialise the window (module docstring cit:([`GIL`], mcp/tests/_store_durability.py:26-26)); and (4) **one
  profile for both consumers** — `STRESS_PROFILE` (cit:([`STRESS_PROFILE`], mcp/tests/_store_durability.py:1094-1101)) is 4 appenders × 50 records at 2 ms
  against one reclaimer at 5 ms, imported by the contract test and used for the reported
  baseline. Also recorded the anchor/decoy design (cit:([`DECOY_PREFIX`], mcp/tests/_store_durability.py:121-121); cit:([`StoreAdapter`], mcp/tests/_store_durability.py:119-176)) that forces a reclaim tick
  to actually rewrite, `AttentionAdapter.appends_in_place = False` (cit:([`AttentionAdapter`], mcp/tests/_store_durability.py:252-291)) deriving
  `APPEND_CASES`, and `NudgeAdapter._reclaim_lock` (cit:([`_reclaim_lock`], mcp/tests/_store_durability.py:377-401)) importing `durable_store` locally
  inside a `try/except ImportError` so the harness can still run against a tree that predates it.
  Filed one Todo: two parentheticals in `parked_rewrite`'s docstring (cit:([`parked_rewrite`], mcp/tests/_store_durability.py:683-732))
  describe the base commit's `Path.write_text` temp materialisation and non-pid-scoped temp name,
  both of which the fix changed; the hook still lands via `os.replace`, so it is stale prose and
  not a defect. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is blank because the source file is new and uncommitted;
  closeout owns its first stamp.