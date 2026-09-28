# mcp/tests/test_automatic_post_integration_cleanup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-27T05:30:43+00:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` |
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| path | `mcp/tests/test_automatic_post_integration_cleanup.py` |
| doc_type | `file-level-onboarding` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pins **which procedure reclaims a landed leaf**, and proves the whole path end to end over real Git
repositories: a landing retires nothing and routes to `lifecycle_finalize_task`, finalization reclaims
and completes the task edge, a cleanup that cannot complete refuses before that edge closes, and a
refused integration leaves every target exactly where it was.

The developer ruling is unchanged — a completed leaf is reclaimed automatically rather than by a
prompt. What this lane now pins is ownership, because the old ownership made the terminal edge
unreachable: integration reclaimed inside itself, so the enclosure was already at
`cleanup: completed` when the one guard that routes a landed leaf onward
(`next_step.py::_gate_after`, keyed on that exact cell) looked at it. A real landing therefore
reported `done` while the leaf's task document stayed `planning` and its master row stayed
`inProgress`. The module name is historical: reclamation is no longer a "post integration" step,
finalization owns it.

## Code Commentary

### Logic

The fixture chain builds a genuinely landed external-memory leaf:
`bound_worktree_services` cit:([`bound_worktree_services`], mcp/tests/test_automatic_post_integration_cleanup.py:74-83)
binds the default service bundle, `_landed_leaf` cit:([`_landed_leaf`], mcp/tests/test_automatic_post_integration_cleanup.py:85-88)
publishes a real closeout through the shared authority fixture, and `_integrate_apply`
cit:([`_integrate_apply`], mcp/tests/test_automatic_post_integration_cleanup.py:120-127)
drives the public integrate tool with `auto_land_on_integration=True`. Three small readers keep the
assertions about the task edge honest:
`_leaf_document` cit:([`_leaf_document`], mcp/tests/test_automatic_post_integration_cleanup.py:103-109)
resolves the contractually bound leaf document through `resolve_terminal_leaf_doc` and reads it,
`_master_row_status` cit:([`_master_row_status`], mcp/tests/test_automatic_post_integration_cleanup.py:111-118)
finds the one master row naming this leaf, and
`_local_branch_exists` / `_work_branch_sides`
cit:([`_local_branch_exists`, `_work_branch_sides`], mcp/tests/test_automatic_post_integration_cleanup.py:90-101)
drive real Git.

Four cases:

- `test_a_landed_leaf_is_reclaimed_by_finalization_and_never_by_integration` cit:(["test_a_landed_leaf_is_reclaimed_by_finalization_and_never_by_integration"], mcp/tests/test_automatic_post_integration_cleanup.py:129-129)
  — the load-bearing case. The landing's `cleanup` key is the untouched contract cell (`"pending"`),
  `"removed"`/`"notRemoved"` are absent from the payload, the summary promises reclamation at the task
  edge, and the projection names the terminal move (`phase: cleanup-pending`, `nextOperation:
  finalize`, `nextTool: lifecycle_finalize_task`, `nextRequiredArgs == ["contract_path"]`). It then
  proves **nothing was retired** — every worktree, branch, the reports directory and the enclosure
  root are still present, and the leaf document is still not `Completed` — and only then calls
  `lifecycle_finalize_task_tool`, which must produce the shaped operator report
  (`"Automatic cleanup removed 2 worktrees, 2 local branches, 1 reports directory, 1 enclosure root;
  nothing was left in place."`) with `notRemoved` empty, and must leave both the leaf document and the
  master row `Completed`.
- `test_a_refused_cleanup_blocks_finalization_and_leaves_the_task_edge_open` cit:(["test_a_refused_cleanup_blocks_finalization_and_leaves_the_task_edge_open"], mcp/tests/test_automatic_post_integration_cleanup.py:221-221)
  — the other half of the ownership split. `finalize.cleanup_result` is patched to raise
  `RuntimeError`, and the assertion is that finalization reports `cleanup-blocked` with cleanup's own
  payload passed through whole (`{"state": "blocked", "summary": "refused"}`) rather than re-shaped,
  that the leaf document and the master row stay open, and that every reclamation target is still on
  disk. Without this case the split could "succeed" by closing a task edge over work that was never
  reclaimed.
- `test_a_dry_run_finalization_reports_the_cleanup_plan_and_shapes_nothing` cit:(["test_a_dry_run_finalization_reports_the_cleanup_plan_and_shapes_nothing"], mcp/tests/test_automatic_post_integration_cleanup.py:260-260)
  — pins the report shaper's dry-run gate. A preview's payload lists what cleanup *would* remove, so
  shaping it with "removed … nothing was left in place" would assert a reclamation that never
  happened; the case asserts `state: would-finalize` with cleanup's own `would-cleanup` plan, no
  `automatic` key, and nothing retired.
- `test_refused_integration_leaves_every_worktree_and_branch_in_place` cit:(["test_refused_integration_leaves_every_worktree_and_branch_in_place"], mcp/tests/test_automatic_post_integration_cleanup.py:300-300)
  — the pre-existing negative control, extended: the dry run's `cleanup_reminder` now promises only
  the landing, the refused apply produces no reclamation report (`cleanup == "pending"`, no
  `"removed"`), no source ref moved, and the leaf document is not `Completed`.

### Conventions

Plain module-level `pytest` functions with one fixture, and the module is registered in the
`integration` lane of `mcp/tests/test-evidence-lanes.toml` (line 130) because these cases drive real
application tools over real repositories.

**The file name is historical and deliberately not renamed.** This path is declared by name in three
manifests and only one of them is fail-closed:
`mcp/tests/test-evidence-lanes.toml:131` (the lane manifest a consumer refuses to load without),
`mcp/tests/evidence-lifecycle.toml` (nine rows), and
`mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:65`. Renaming the
module would be a cross-manifest change for no behavioural gain, so the docstring records the
historical name and points readers at the real subjects instead:
`finalize::_run_or_verify_cleanup`, which runs reclamation, and
`cleanup_report::cleanup_report`, which shapes the report the first case asserts. Do not "fix" the
name on the strength of the file's contents; `finalize.py` is where the behaviour this lane tests now
lives.

### Invariants And Boundaries

- **A landing must not reclaim.** Asserting only the final state would pass for a route that reclaimed
  early and then reported correctly, so the first case asserts the *intermediate* state — every target
  still present, the leaf document open, `cleanup == "pending"` — before it finalizes.
- **A refusal must never close the task edge.** The second case exists because the ownership split
  turns a cleanup failure from "reported beside a completed landing" into "blocks finalization"; if a
  future change let finalization mark documents `Completed` on a failed cleanup, only these assertions
  would notice.
- **The shaped report is asserted by exact sentence**, because the sentence is what an operator reads
  and the counts in it are the only proof that the inventory was derived rather than synthesized.
- **A preview is never shaped.** The third case is the dry-run gate; a shaper that ran on preview
  payloads would report removals that did not happen.
- **The lane row is not optional metadata.** The manifest is fail-closed, so an unregistered tracked
  module is a hard load failure rather than a silent gap.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own application tools over real Git fixtures, so the retained source is the
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring that records the ownership story and the historical name. | "Reclamation is automatic and unprompted, and finalization is what runs it." | mcp/tests/test_automatic_post_integration_cleanup.py:1-28 |
| The reclamation runner and report-shaping gate these cases exercise through `lifecycle_finalize_task`. | `_run_or_verify_cleanup`; "cleanup_report(contract, result.payload)" | mcp/src/agents_remember/worktrees/modules/finalize.py:277-311; mcp/src/agents_remember/worktrees/modules/finalize.py:310-310 |
| The report shaper whose exact sentence and inventory the first case asserts. | `cleanup_report`; "ALREADY_CLEAN = \"already-clean\"" | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:23-53 |
| The landing route whose no-reclamation the cases assert, including the payload's untouched `cleanup` cell. | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:574-607 |
| The projection that names the finalization move. | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:245-328 |
| The terminal operation the first case calls. | `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:855-904 |
| The fail-closed lane this module must be listed in, and the dependency-classification entry that also names it. | "integration = ["; "AMBIENT_ROLE_RUNNER_PATH: frozenset("; `AMBIENT_ROLE_RUNNER_PATH`; "mcp/tests/test_automatic_post_integration_cleanup.py" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:236-241; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:62-62; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:65-65 |
| The fail-closed lane this module must be listed in, and the dependency-classification entry that also names it. | "integration = ["; "AMBIENT_ROLE_RUNNER_PATH: frozenset("; `AMBIENT_ROLE_RUNNER_PATH`; "mcp/tests/test_automatic_post_integration_cleanup.py" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:236-241; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:62-62; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:65-65 |
| The fail-closed lane this module must be listed in, and the dependency-classification entry that also names it. | "integration = ["; "AMBIENT_ROLE_RUNNER_PATH: frozenset(" | mcp/tests/test-evidence-lanes.toml:250-250; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:62-62 |

## Cross-Repo References

These are in-process application-tool assertions against real repositories created in a temporary
directory; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 3 citations into `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 3 citations into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 3 citations into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py`, `mcp/tests/test-evidence-lanes.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T16:25:39+02:00 — 260921-ICR-L42 curator: No content impact: re-pointed this card's citations into `test-evidence-lanes.toml` after this leaf's line insertions (candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`). Each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 1 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "integration = ["; "AMBIENT_ROLE_RUNNER_PATH: frozenset(" repointed to mcp/tests/test-evidence-lanes.toml:233-233; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:62-62. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **sync-merge resolution of the parked candidate against the landed ICR-L7 curation (2 regions).** Additive union: merged production-line header with this leaf's re-derived candidate row; the three lane rows collapsed to current merged-tree ranges (`integration` `:218`, module row `:231`, dependency `:47`/`:62`) — the third row's `dependency_ownership.py:215` range held no anchor on either side and now cites the frozenset line like its siblings. Both sides' history preserved. No verification stamp was advanced.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **citation repair: the dependency-classification anchors never lived in the manifest, and the rows said they did.** The two lane rows cited `test-evidence-lanes.toml:217/:230` for all four anchors, but `AMBIENT_ROLE_RUNNER_PATH` and `"AMBIENT_ROLE_RUNNER_PATH: frozenset("` resolve only in `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py` (`:47` the declaration, `:62` the frozenset entry that names this module) — verified by reading both files, not by delta. The rows now cite the lane key and the module row (`:217`, `:230`) plus the two dependency lines (`:47`, `:62`); claim wording and anchors unchanged. The nine mechanical projection bullets below that recorded superseded lanes ranges for these anchors are retired by this reading. No verification stamp was advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by the lane row this leaf inserted.** This file is not a changed source file. Both of its lane rows cited the pre-insertion lines for two different anchors; each was re-read and re-derived from the line that carries its own anchor on this candidate: the `integration = [` key moved `:210`/`:211` → `:214`, and the module's own row moved to `:227`. No claim wording or anchor was changed, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; this leaf appended one row to `mcp/tests/test-evidence-lanes.toml` at `:89` and two consumer rows to `mcp/tests/evidence-lifecycle.toml` at `:733` and `:1271`, so every lane row below `:88` shifted by one and every evidence-catalog line below those rows by one and two respectively. Each affected row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file — and, where a row's anchor is a lane or consumer entry, from the line that actually carries it — rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **citation repair only.** `260921-ICR-L1` inserted one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:105`, so every row and lane key below it moved one line lower; this card's claim rows that cite that manifest were re-derived under that mapping from the anchor's real position (the ranges are shifted exactly where they cross `:105`, and left alone where they do not). No claim was re-worded, no row was deleted, and the generated history entries in this card keep the ranges they were written with. No verification stamp was advanced.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **citation repair only.** `260921-ICR-L1` inserted one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:105`, so every row and lane key below it moved one line lower; this card's claim rows that cite that manifest were re-derived under that mapping from the anchor's real position (the ranges are shifted exactly where they cross `:105`, and left alone where they do not). No claim was re-worded, no row was deleted, and the generated history entries in this card keep the ranges they were written with. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_automatic_post_integration_cleanup.py.md:140` (integration = [) — re-read the row against the merged registry: the anchor is at the line named in the checker's own message, and the cited range was widened to the line that carries it.
- 2026-09-18T19:53:17+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The lane row's `"integration = ["` cell walked the previous lane's entries and its closing `]` at `196` but stopped one line short of the lane key at `201`; that range was widened to `196-201`. The sibling row in this document already carried `test-evidence-lanes.toml:201-201` for the same key, so this row now agrees with it. The claim, the anchors and the dependency-classification ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 10 generated projection bullet(s) by hand while resolving the memory sync** — `AMBIENT_ROLE_RUNNER_PATH`, `integration = [`, `Path(\`, `)`, `_integrated_result`, `_post_integration_phase`, `lifecycle_finalize_task_tool`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand** — `AMBIENT_ROLE_RUNNER_PATH`, `integration = [`, `Path(\`, `)`, `_integrated_result`, `_post_integration_phase`, `lifecycle_finalize_task_tool`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``AMBIENT_ROLE_RUNNER_PATH`; "integration = ["` → `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:162-162`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:160-160` -> `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:161-161`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "integration = ["; "Path(\"mcp/tests/test_automatic_post_integration_cleanup.py\")" repointed to mcp/tests/test-evidence-lanes.toml:161-161; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:855-886. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Hand retirement by the 260918-TSIP-L11 closing seat of the mechanical repair this timestamp recorded. The range it wrote for `_post_integration_phase` (mcp/src/agents_remember/worktrees/modules/guidance.py:245-328) was re-read against the module on the merged tip and re-cited by hand, and the machine marker is removed so the range is no longer read as an unverified projection. No claim wording changed; no verification stamp is advanced over prose that was not re-read. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:574-607. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:862-893. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43:00+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:598-633. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — Created by the 260831-LOCR-L31 curator pass. This module had no card
  before, and its change set is exactly where the leaf's central decision lives, so the record belongs
  beside it: the four cases (landing retires nothing and routes to finalization; finalization reclaims,
  publishes the shaped report and completes the leaf document and master row; a refused cleanup blocks
  finalization and leaves the edge open; a dry run is never shaped), the fixture chain that makes the
  first case a real end-to-end path, and **the historical file name** — this path is declared in three
  manifests (only `mcp/tests/test-evidence-lanes.toml` is fail-closed) and is deliberately not renamed,
  with the docstring pointing at `finalize::_run_or_verify_cleanup` and
  `cleanup_report::cleanup_report` as the real subjects. Verification metadata is pinned to the leaf
  base commit and remains closeout-owned; source documentation only, no acceptance claim.
- 2026-09-12T17:50:00+00:00 — Created by the 260831-LOCR-L31 curator pass. This module had no card
