# mcp/tests/test_onboarding_trace_gate.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R30@v1 gate cases, amended by MIK-R53, on converted-format fixtures (15 unparameterized top-level test definitions, measured statically; not a new collection or execution).** The `leaf` fixture is a real code
repository and a real converted memory repository (`main` is the official line, its commit carries the
`Code-Commit` trailer naming the leaf's base) plus a leaf series contract. The executable cases
call the trace gate and memory-quality controller; they do not exercise a closeout trace validator. The file runs in the unit lane
(`test-evidence-lanes.toml`).

## Code Commentary

### Logic

- **Rule 3.** `test_only_an_anchors_blob_line_numbers_and_content_do_not_count` checks the counted-change
  rule field by field, including reference changes versus realizes-only rationale/locator/list edits
  (the latter do not count; MIK-R53 excludes realizes/proves-only change); `test_the_writers_mechanical_anchor_update_is_not_a_trace` runs the real writer carry
  and the item stays open.
- **Rule 2 and the examples.** `test_the_conforming_example_and_the_route_case` (a prose edit with its `updated` row, plus a
  "test-only rename" `no_impact` row; only the nearest route; `onboarding:overview` for a root-level file) and
  `test_a_missing_trace_is_one_named_repair_finding_and_the_closeout_refuses`.
- **Rows.** `test_rows_are_only_about_changed_files_and_the_registry_rule_is_both_halves` (unnecessary rows
  remain report-only; the registered kind now declares five facts including `sourceBlobs`;
  `onboarding_item_open` rejects counted-edit-only and `satisfiedBy: counted-change` identities);
  `test_a_moved_marker_row_binds_its_sources_and_reopens_on_change` asserts source-bound currency,
  preservation of ID/markers and the unchanged candidate source binding across rewrite, an explicit
  reason update from `Moved by the crossing sync.` to `Re-reviewed.`, and reopening after another source edit.
  `_gate` captures candidate blobs and writer calls for overview rows receive recomputed worklists.
- **Fail closed.** `test_mixed_formats_are_an_incomplete_side_never_a_vacuous_pass` (both mixed cases: the
  reason, the trace gate result's refusal and the persisted `incomplete` worklist);
  `test_an_unreadable_sidecar_never_satisfies_a_trace` (a K_C sidecar corrupted beside a row and a Markdown
  edit: open, `countedChange` false, and `onboarding_item_open` open in both cases);
  `test_an_unreadable_base_sidecar_is_an_incomplete_input_and_a_repair_counts`;
  `test_unreadable_history_and_unestablished_sides_are_findings_never_a_pass`.
- **The converting leaf.** `test_the_conversion_itself_counts_for_nothing_at_the_converting_leaf` builds a
  legacy K_B (`_legacy_card`), converts it, and shows that only a change beyond the conversion counts. It also
  writes a `knowledge-worklist-base/v1` cache file and shows it is ignored and rewritten as v2.
- **Enforcement.** `test_the_memory_quality_run_counts_each_missing_trace_toward_the_actionable_count`
  drives the controller (`_run_controller`). Since MIK-R09 (leaf 260928-MIK-L09) `_run_controller` captures the real
  candidate trees (the gate judges exact trees), and the case asserts `curatorActionableCount` 4 beside
  `knowledgeGate.openItemCount` 3: the card's and the route's traces are joined by the uncovered file's
  `unexplained_hunk` (MIK-R10), and the appended source also makes the card's reference anchor stale. After
  writing the traces, the stale reference remains one actionable item;

> Retained earlier card wording; superseded by the current account above:
>   candidate trees (the gate judges exact trees), and the case asserts `curatorActionableCount` 3 and
>   `knowledgeGate.openItemCount` 3, not 2: the gate counts each open item once, so the card's and the route's traces
>   are joined by the uncovered file's `unexplained_hunk` (MIK-R10), which the card's own trace answers once it is
>   written;
 `onboardingTrace.open` still names the two traces; `test_the_persisted_worklist_carries_the_onboarding_items_in_its_one_list`
  pins ruling Q2 and the `(kind, subject)` order; the gate-message case independently checks that trace names remain visible when the gate’s changed paths exceed the reported census; `test_an_unconverted_leaf_is_refused_before_any_gate_runs` asserts that sides and worklist remain `None`, but the controller refuses (`state: refused`, `code: unconverted-memory`) with the central `legacy-format` message and conversion command before either gate runs; the legacy gate is not called and no `onboardingTrace` is delivered.
- **L37 (review R3-1).** `_run_controller` patches `run_memory_quality_check` with the module-level mock
  `_QUALITY_RUN`, and `test_the_memory_quality_run_counts_each_missing_trace_toward_the_actionable_count` now also
  asserts that the run's drift context carries a callable `knowledge_base`: the converted check is given its
  comparison base (MIK-R24 rule 7). No case was added.

### Conventions

- The file builds its own legacy fixture instead of consuming `knowledge_conversion_test_support.py`, so it
  adds no census-tracked consumer and needs no dependency-ownership re-pin.

### Invariants And Boundaries

- **The current ordinary-candidate cases supersede the older counted-edit-or-row ruling.**
  MIK-R53 requires an eligible row bound to current source blobs; `updated` additionally requires
  counted Markdown/reference change, `no_impact` covers unchanged contracts, and entry-only
  realizes/proves edits do not count. A later source edit reopens the bound answer. Earlier rulings
  18:49:50 (persisted items, `onboarding:overview`, cache Markdown), 19:23:45 (N1–N5) and
  19:53:54 (R2-1–R2-3) remain historical context; only the old standalone-counted-edit answer is
  superseded. Amended L53 rule 1 separately permits this leaf's counted changed cards under the
  old MAIN-LINE producer without updated or changed-card no_impact/backfill; that rollout exception
  is not a conflict blocker and is not what these ordinary-candidate tests assert.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R30@v1` of task
`260928_maintained-invariant-knowledge`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The fixture builds real code and converted memory repositories plus a leaf contract; the executable cases call the trace gate and controller, not a closeout trace entry. [1]


- The leaf fixture. [2]




- A missing trace produces named open findings, result.ok=false and refusal() naming both file and route. [5]


- The writer's carry is not a trace. [6]


- Mixed-format sides return not-ok gate results with named refusal and persist incomplete worklists, never vacuous success. [9]


- An unreadable K_C sidecar keeps its item open. [10]
- An unreadable K_B sidecar is an input problem; a repair counts. [11]

- Unreadable history and unestablished sides are findings. [12]


- The conversion counts for nothing; a v1 cache file is rewritten. [13]



- Each open item counts once toward `curatorActionableCount`: the three gate items — the two traces and the uncovered file's `unexplained_hunk` — plus the card's reference anchor that the appended source makes stale, so four beside a gate `openItemCount` of three. [15]


- The items are in the persisted worklist. [16]
- An unconverted leaf is refused before either gate runs, with the conversion step. [17]




- The unit-lane registration. Source caption: "mcp/tests/test_onboarding_trace_gate.py" [18]






- The memory-quality run gives the converted check its comparison base. [19]



### Cross-Repo References

No meaningful cross-repo references found: the fixtures are temporary repositories.

No cross-repo boundary is crossed by this file.

- Mechanical anchor fields and realizes-only edits never count; reference/prose edits are separate counted changes. [3]
- The conforming example pairs prose with updated and source-current no_impact rows, using the nearest route and candidate blobs. [4]
- Unnecessary rows, five registry facts including sourceBlobs, and rejection of counted-change-only satisfaction. [7]
- test_a_moved_marker_row_binds_its_sources_and_reopens_on_change preserves row identity/markers and the unchanged candidate source binding on rewrite, updates the reason to `Re-reviewed.`, then reopens after source movement. [8]
- Current source delta inspected statically: Repair current-row/counting doctrine, moved-marker caption and worklist/blob inputs; keep historical rulings explicitly superseded. [20]
