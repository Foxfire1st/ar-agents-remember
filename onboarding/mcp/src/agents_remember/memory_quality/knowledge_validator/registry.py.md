# mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The validator's single rule registry (MIK-R22 rule 9) and the context every rule reads.** A `ValidationRule` has a stable `id`, owning packet rule, summary, a `check` over `ValidationContext`, `writer_reports` and the named route policies `merge_reports` or `migration_debt`. The legacy `report_only` field must remain false; report/refuse is computed per finding and route, not fixed for a whole rule. Later packets add rules with `register_rule` (MIK-R04 families, MIK-R20 census, MIK-R27 admission, MIK-R13 decision content), and every registered rule then runs wherever the validator runs.

## Code Commentary

### Logic

- `register_rule` refuses a duplicate ID, plain `report_only=True`, or both `merge_reports` and `migration_debt` together. `registered_rules` returns all rules in registration order; every check still runs.
- `writer_reports` (default `False`, introduced by MIK-R04) marks findings the writer may report during authoring rather than refuse, so a leaf can repair them before closeout. `writer_reported_rule_ids()` returns the registered IDs carrying it (with the legacy report-only flag false); the package re-exports it. This is not a fixed three-rule inventory: later registrations, including existing-record admission and judgment checks, also use the flag. Commit validation ignores the writer relaxation and applies each finding's named route policy.
- A check yields `Finding(path, field, message, carried=False)`. `carried` means a comparison base already holds the finding's state. The validator adds the rule ID and computes `Violation.report_only` for this finding at this route.
- `merge_reports`, subject to `merge_requires_carried` when set, reports at a sync merge (`is_sync_merge`: at least two comparison bases, no leaf publication) or explicit standalone conversion; ordinary publication/landing refuses. Its note names why deferral is needed and the next refusing publication/landing.
- `migration_debt` reports base-carried findings only while migration is incomplete. New debt refuses immediately at ordinary routes, and all debt refuses once migration is complete. Explicit standalone conversion reports the debt it authors. `migration_state` unions census inventory/status routes with the candidate's actual onboarding routes, takes each route's latest status across censuses, and requires a nonempty population, no census problems, and every route `migrated` or `excluded`. Absent/bad censuses and new unmarked routes are not completion. `onboarding_routes` now comes directly from the lower `memory_quality/knowledge_census/files.py` reader, beside `read_censuses`, rather than from the Git census inventory. The actual-route union, latest status test, completion conditions and `closed_before` realization remain unchanged. Debt notes name the migration condition and remaining routes, rather than an unnamed permanent reporting exemption.
- `ValidationContext` holds the candidate, its `ParsedTree`, the comparison `bases`, the paired `code` tree (or `None` for a standalone conversion), `conversion` and, since MIK-R09 (leaf 260928-MIK-L09), `leaf_publication` (default `False`): the commit publishes a leaf (its closeout, direct landing or recorded landing), so MIK-R09's history-row rule (`rules_history`) re-anchor-checks every history file not closed in a base, whatever its own `closed` flag (review R1 F1, ruling 2026-09-30T16:07:55). `record_ids` is every parsed record ID plus the IDs of unparsed record files.
- `base_anchors` (cached) collects, from every base's leniently parsed sidecars, each realization/proof entry as `(entry ID, anchor key)` and each reference anchor target as `(sidecar path, anchor key)`. `anchor_key` serialises the anchor with its own path filled in from the sidecar, so an anchor that omits `path` compares equal to one that spells it.
- `sidecar_entries` returns a file sidecar's `realizes` and `proves` entries.
- `ValidationContext.frozen` (L37, INV-MS9BMJ) holds the history files of the commit(s) the candidate sits on
  when they are not comparison bases: a leaf's base is its parent line's tip, so a leaf that continues after a
  closeout that was not integrated sits on a commit that is no base. `closed_before` is the bases plus `frozen`:
  every tree whose closed history files are frozen. The freeze rule and the re-anchor rule read it.

### Conventions

- Rules are plain functions over the context, so a later packet's rule is one `ValidationRule` and one `register_rule` call.
- The module docstring says MIK-R22's rules register when `.rules` is imported; the actual modules are `rules_structure` and `rules_references`, imported by `validator.py`.

### Invariants And Boundaries

- One registry: there is no way to run a subset of rules at a commit route.
- There is no permanently report-only rule registration. `merge_reports` and `migration_debt` are bounded per-route/finding reasons; without an applicable reason the finding refuses. A standalone conversion is explicit reporting context, not a commit or CLI bypass.
- `writer_reports` does not change the validator's own report: `validate_tree` and `require_valid_commit` use the named route policy and no commit route may turn a refusal into a report from this flag. Only the writer reads `writer_reported_rule_ids()` for its authoring relaxation; outside a named route exception those findings still refuse.
- An anchor is carried only by an equal anchor for the same entry ID, or for a reference target in the same sidecar path; renumbering references does not break carrying.

### Todos

The docstring's `.rules` reference is slightly stale (the modules are `rules_structure`/`rules_references`); harmless, noted for a later touch. `anchor_key` fills in the path itself, while L07's `history.sidecar_entry_anchors` does the same for entries (review R1 finding 8, info).

`merge_requires_carried` defaults false; when true it narrows merge reporting to a finding with `carried=True`, preserving refusal of newly authored missing link targets. The shared cached `route_families` tuple belongs to this one parsed candidate/context and is read by every route rule; this is not a process-global candidate memo.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The registry, the context and the carried-anchor computation.



- The refusing route rules are reported inside the writer, and still refuse in `validate_tree`. [4]



### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.

- A rule may carry `writer_reports` and a named route policy; `Finding.carried` distinguishes base debt. Plain report-only registration and both named policies together refuse. [1]
- Current source delta inspected statically: Replace blanket reporting and stale writer inventory with named route/finding policy, migration completion and explicit conversion context. [10]
- Each ID registers once; rules run in registration order. [2]
- The refusing rules a writer reports instead; the docstring states the contract. [3]
- The anchor comparison key and the base anchors. [5]
- The shared context includes `is_sync_merge` and cached migration state over census and actual onboarding routes, beside candidate/bases/code/publication. [6]
- The flag a leaf-publication commit sets (MIK-R09). [7]
- Every registered check runs; per-finding report/refuse depends on sync-merge/standalone-conversion context or carried debt and migration completeness, never a blanket report-only registration. [8]
- The context's frozen trees, and every tree whose closed history files are frozen. [9]
- Migration completeness uses the lower census reader and the same actual-route/status union. [11]

- Rule-local carried-only merge reporting and shared per-validation family states remain separate from writer reporting. [12]
