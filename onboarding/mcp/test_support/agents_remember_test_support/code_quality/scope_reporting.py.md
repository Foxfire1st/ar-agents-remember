# mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Quality support overview](overview.md)

## 260824-PDLS Current Contract

Targeted reports now print the complete `TestImpact` disposition from the canonical ownership
graph: selected paths, whether ownership is complete, whether a global input invalidated the
population, any explicit conservative-full decision, and every stable selection reason. The output may truthfully be
broad; it must explain why rather than optimizing the count. Coverage provenance separately names
product measurement units, so executed tests/support are not misreported as CRAP inputs.

## 260831-CCR-L19 Change

L19 updated the targeted-ownership wording to the exact-ownership contract: the incomplete line now
reads `targeted ownership: incomplete; Gate 2 blocked without population expansion` (it never
prints a safe-full population), and the printed ownership reasons are the flattened set of every
`test_impact.reasons` rather than only reasons nested per owned path. The report remains
read-only.

## Purpose

Render truthful scope, input, config, and unit provenance for quality rails.

## Code Commentary

### Logic

Scope lines explain actual inputs and units for full/targeted Python, hooks and dashboard rails.
`crap_scope_line` labels production scores and the diagnostic review threshold;
`diff_scope_line` labels diagnostic changed coverage without a floor. The reporting owner never
changes selection or grants acceptance.

`tsconfig_project_inputs` (function, lines 430-458)
- `tsconfig_inputs` (function, lines 459-482)
- `config_input_files` (function, lines 483-505)
- `dashboard_lint_scope_line` (function, lines 506-524)
- `dashboard_test_scope_line` (function, lines 525-546)
- `dashboard_typecheck_scope_line` (function, lines 547-555)
- `dashboard_build_scope_line` (function, lines 556-583)
- `dashboard_scope_line` (function, lines 584-626)
- `build_parser` (function, lines 627-653)
- `main` (function, lines 690-704)

`tsconfig_project_inputs` accepts both direct JSON references and directory references containing
`tsconfig.json`. Each referenced project's `files` and `include` entries resolve from that config's
own directory, so nested TypeScript projects cannot be silently measured against the dashboard root.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- This owner is verification support under `mcp/test_support`, not shipped product source.
- Targeted reporting never claims a safe-full population; incomplete ownership is reported as a
  Gate-2 block (L19).

### Todos

None.

## Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact selection reasons and incomplete ownership | `targeted_scope_lines` | mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py:278-312 |
| Production-only diagnostic review threshold label | `crap_scope_line` | mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py:342-354 |
| Diagnostic diff inputs without a floor | `diff_scope_line` | mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py:381-394 |
| Project-relative TypeScript file resolution | `tsconfig_project_inputs` | mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py:481-509 |
| Read-only provenance reporting dispatch | `main` | mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py:743-753 |

## 260731-EFA-L9 Change

The scope report gained the `layering` tier: the armed package-layering step reports violation
and cycle counts/edges alongside the other quality steps, and the wrapper's invocation labels
carry the layering result.

## Docs References

No configured Domain Documentation source applies to this read-only reporting module.

## Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

## Update History

- 2026-09-06T21:35:26+00:00 — Reconciled the d3610903 test-policy reduction against the current source, preserved integrity/ownership boundaries, and replaced stale forcing-suite citations with current owner evidence. Existing verification hash/date retained; source comparison is not final acceptance.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 targeted-report
  wording change — incomplete ownership is reported as a Gate-2 block with no population
  expansion, and ownership reasons are printed from the flattened `test_impact.reasons` set.
  Verification is pinned to the owning commit.

- 2026-08-28T14:18+02:00 — Reconciled scope-reporting source ranges against the committed PDLS
  candidate after final helper movement; the documented semantics are unchanged.

- 2026-08-28T11:32+02:00 — Added directory-form TypeScript project references and resolved each
  referenced project's inputs from its own config directory.

- 2026-08-25T01:56+02:00 — 260824-PDLS added canonical ownership completeness, global/fallback
  disposition, and all selection reasons to targeted scope reporting; verification remains
  closeout-owned.
- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the layering tier in the scope
  report; the L9 change section above documents it. Verification metadata pinned until closeout
  stamps the L9 code commit.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the targeted tier
  (invocation labels, targeted scope lines, integration-tree diff labels, the
  `targeted` hook tier), refreshed every function anchor to the post-L17
  ranges, and added the `targeted_scope_lines` row. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the file-size scope contract was added to scope reporting, and the TypeScript-input count now matches the live tsconfig project-input union (426). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the dashboard rail steps and pinned TS input count. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T13:06:07+02:00 — 260731-EFA-L6 residual curator: corrected the `main` citation from the stale range 549-575 (which holds no `main`) to the current definition extent 586-596 in the frozen code tree (HEAD 5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060).

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
