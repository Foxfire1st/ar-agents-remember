# mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The validator's single rule registry (MIK-R22 rule 9) and the context every rule reads.** A `ValidationRule` has a stable `id`, the packet rule that owns it, a summary, a `check` over the `ValidationContext`, and `report_only`. Later packets add rules with `register_rule` (MIK-R04 families, MIK-R20 census, MIK-R27 admission, MIK-R13 decision content), and every registered rule then runs wherever the validator runs.

## Code Commentary

### Logic

- `register_rule` refuses an ID registered twice; `registered_rules` returns them in registration order.
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
| A rule and what a check returns. | `ValidationRule`; `Finding` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:49-54; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:37-42 |
| Each ID registers once; rules run in registration order. | `register_rule`; `registered_rules` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:60-66; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:69-72 |
| The anchor comparison key and the base anchors. | `anchor_key`; `BaseAnchors`; `_base_anchors` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:83-88; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:92-102; mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:105-116 |
| The context every rule reads. | `ValidationContext` | mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py:120-141 |
| A later packet's rule runs everywhere, and report-only never refuses. | `test_a_later_packets_rule_runs_everywhere_and_report_only_never_refuses` | mcp/tests/test_knowledge_validator.py:520-537 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
