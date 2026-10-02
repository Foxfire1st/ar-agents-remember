# mcp/src/agents_remember/memory_quality/knowledge_validator/registry.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The validator's single rule registry (MIK-R22 rule 9) and the context every rule reads.** A `ValidationRule` has a stable `id`, the packet rule that owns it, a summary, a `check` over the `ValidationContext`, `report_only` and, since MIK-R04, `writer_reports`. Later packets add rules with `register_rule` (MIK-R04 families, MIK-R20 census, MIK-R27 admission, MIK-R13 decision content), and every registered rule then runs wherever the validator runs.

## Code Commentary

### Logic

- `register_rule` refuses an ID registered twice; `registered_rules` returns them in registration order.
- `writer_reports` (default `False`, added by MIK-R04 in leaf 260928-MIK-L04) marks a rule that **refuses at every commit route but is only reported inside the writer**, so a leaf may break it mid-way and repair it before closeout (MIK-R04 rule 6). `writer_reported_rule_ids()` returns the IDs of the rules that carry the flag and are not report-only; the package re-exports it. MIK-R04's `R04.1-route-directory`, `R04.2-coverage` and `R04.2-non-empty` are the only rules that carry it today.
- A check yields `Finding(path, field, message)`; the validator adds the rule ID and the rule's `report_only` flag. The flag lives only here.
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
- A report-only rule never refuses, whatever its check returns.
- `writer_reports` changes nothing in the validator's own report: `validate_tree` and `require_valid_commit` still refuse such a finding, and no commit route may read the flag. Only a writer (MIK-R12) reads `writer_reported_rule_ids()` and treats those violations as reports; L12's leaf document records that consuming obligation.
- An anchor is carried only by an equal anchor for the same entry ID, or for a reference target in the same sidecar path; renumbering references does not break carrying.

### Todos

The docstring's `.rules` reference is slightly stale (the modules are `rules_structure`/`rules_references`); harmless, noted for a later touch. `anchor_key` fills in the path itself, while L07's `history.sidecar_entry_anchors` does the same for entries (review R1 finding 8, info).

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

- A rule, with its `report_only` and `writer_reports` flags, and what a check returns. [1]
- Each ID registers once; rules run in registration order. [2]
- The refusing rules a writer reports instead; the docstring states the contract. [3]
- The refusing route rules are reported inside the writer, and still refuse in `validate_tree`. [4]
- The anchor comparison key and the base anchors. [5]

- The context every rule reads. [6]

- The flag a leaf-publication commit sets (MIK-R09). [7]
- A later packet's rule runs everywhere, and report-only never refuses. [8]

- The context's frozen trees, and every tree whose closed history files are frozen. [9]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
