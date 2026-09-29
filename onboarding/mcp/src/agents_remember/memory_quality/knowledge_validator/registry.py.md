# mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The validator's single rule registry (MIK-R22 rule 9) and the context every rule reads.** A `ValidationRule` has a stable `id`, the packet rule that owns it, a summary, a `check` over the `ValidationContext`, `report_only` and, since MIK-R04, `writer_reports`. Later packets add rules with `register_rule` (MIK-R04 families, MIK-R20 census, MIK-R27 admission, MIK-R13 decision content), and every registered rule then runs wherever the validator runs.

## Code Commentary

### Logic

- `register_rule` refuses an ID registered twice; `registered_rules` returns them in registration order.
- `writer_reports` (default `False`, added by MIK-R04 in leaf 260928-MIK-L04) marks a rule that **refuses at every commit route but is only reported inside the writer**, so a leaf may break it mid-way and repair it before closeout (MIK-R04 rule 6). `writer_reported_rule_ids()` returns the IDs of the rules that carry the flag and are not report-only; the package re-exports it. MIK-R04's `R04.1-route-directory`, `R04.2-coverage` and `R04.2-non-empty` are the only rules that carry it today.
- A check yields `Finding(path, field, message)`; the validator adds the rule ID and the rule's `report_only` flag. The flag lives only here.
- `ValidationContext` holds the candidate, its `ParsedTree`, the comparison `bases`, the paired `code` tree (or `None` for a standalone conversion) and `conversion`. `record_ids` is every parsed record ID plus the IDs of unparsed record files.
- `base_anchors` (cached) collects, from every base's leniently parsed sidecars, each realization/proof entry as `(entry ID, anchor key)` and each reference anchor target as `(sidecar path, anchor key)`. `anchor_key` serialises the anchor with its own path filled in from the sidecar, so an anchor that omits `path` compares equal to one that spells it.
- `sidecar_entries` returns a file sidecar's `realizes` and `proves` entries.

### Conventions

- Rules are plain functions over the context, so a later packet's rule is one `ValidationRule` and one `register_rule` call.
- The module docstring says MIK-R22's rules register when `.rules` is imported; the actual modules are `rules_structure` and `rules_references`, imported by `validator.py`.

### Invariants And Boundaries

- One registry: there is no way to run a subset of rules at a commit route.
- A report-only rule never refuses, whatever its check returns.
- `writer_reports` changes nothing in the validator's own report: `validate_tree` and `require_valid_commit` still refuse such a finding, and no commit route may read the flag. Only a writer (MIK-R12) reads `writer_reported_rule_ids()` and treats those violations as reports; L12's leaf document records that consuming obligation.
- An anchor is carried only by an equal anchor for the same entry ID, or for a reference target in the same sidecar path; renumbering references does not break carrying.

### Todos

The docstring's `.rules` reference is slightly stale (the modules are `rules_structure`/`rules_references`); harmless, noted for a later touch. `anchor_key` fills in the path itself, while L07's `history.sidecar_entry_anchors` does the same for entries (review R1 finding 8, info).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The registry, the context and the carried-anchor computation.

| Finding | Anchor | Source |
| --- | --- | --- |
| A rule, with its `report_only` and `writer_reports` flags, and what a check returns. | `ValidationRule`; `Finding` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:56-62; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:44-49 |
| Each ID registers once; rules run in registration order. | `register_rule`; `registered_rules` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:68-74; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:77-80 |
| The refusing rules a writer reports instead; the docstring states the contract. | `writer_reported_rule_ids`; "only reported inside the" | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:83-88; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:8-13 |
| The refusing route rules are reported inside the writer, and still refuse in `validate_tree`. | `test_the_refusing_route_rules_are_reported_inside_the_writer` | mcp/tests/test_knowledge_family_routes.py:237-254 |
| The anchor comparison key and the base anchors. | `anchor_key`; `BaseAnchors`; `_base_anchors` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:99-104; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:108-118; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:121-132 |
| The context every rule reads. | `ValidationContext` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:135-157 |
| A later packet's rule runs everywhere, and report-only never refuses. | `test_a_later_packets_rule_runs_everywhere_and_report_only_never_refuses` | mcp/tests/test_knowledge_validator.py:525-542 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — `ValidationRule.writer_reports` and `writer_reported_rule_ids()` (MIK-R04 rule 6, review R1 finding 1).** Purpose, Logic and Invariants state the flag and its contract. The reopened `ValidationRule` row was re-read and reworded; its range now reaches the new field (`:56-62`). Two rows added. The other rows were re-pointed by the exact line shift. No verification stamp was advanced.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
