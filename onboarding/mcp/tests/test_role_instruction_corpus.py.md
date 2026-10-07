# test_role_instruction_corpus.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

The shipped behavioral guard for the canonical lifecycle corpus: every role and operation
resolves to a readable source, the role registry has no ambient-launcher seat, and the
manifest carries routing metadata without copied payloads. Role sources are concise,
parseable and self-contained; the retired fixed section order, inherited Core declaration
and operator knob block are absent. Relative repository references resolve, while
coordination-owned and symbolic names retain their stated resolution limits.

## Current source account

Compact native role and operation sources remain well-formed and manifest-resolved. Positive curation checks now address two policy surfaces through CURATION_POLICY_STATEMENTS while the exact retired-sentence census still reaches canonical and generated trees. The guard teeth now re-insert every registered retired sentence on each surface that shipped it and assert the finding names it, plus a real removal witness, so a guard that resolves nothing cannot pass. Preserve the handoff template contract and mutation controls; remove descriptions of the retired all-surface positive helper.

## Code Commentary

### Logic

The module resolves its subject from the repository root (`REPOSITORY_ROOT` → `SKILLS_ROOT` →
`LIFECYCLE_ROOT` → `MANIFEST_PATH`), so it always tests the worktree it runs from. Its declared
vocabulary is the corpus contract in miniature: `ROLE_ORDER` and `OPERATION_KEYS` bind the
role and operation registries. `MACHINE_SECTION` identifies a retired knob block that
concise role sources must not carry.

The resolver is deliberately split into small cohesive helpers — `_check_core`, `_check_operations`,
`_check_roles` (with `_check_role_order` and `_check_one_role`), and `_check_launcher_and_references` —
because the earlier single-function version tripped ruff's complexity limits. That split is the point:
`_resolve_sources` returns a list of human-readable problems rather than a boolean, so a manifest entry
that names a missing source, an unknown core block, an unknown operation, or a missing criteria catalog is
**reported**, never skipped.

`test_manifest_resolves_every_role_and_operation_source` additionally asserts the router still registers
every `roles/<role>.md`, that `launcher` is absent from `manifest["roles"]`, that `ambient-launcher` is one
of the routing conditions, and that the manifest carries no prose lines.

`test_manifest_carries_routing_metadata_not_copied_payloads` is the metadata-plane case: it walks every
JSON string in the manifest (`_iter_json_strings`), applies the `manifest_copy_indicators` heuristics, and
fails on copied payload content, so the manifest cannot quietly become a second copy of a source section.
It is staged against a `tmp_path` copy so it can also prove the detector fires on a deliberately copied
payload without failing the healthy tree.

`test_every_role_source_is_concise_and_well_formed` checks canonical YAML name and
description, readable headings, no inherited Core line, no machine/operator knob block
or knob table rows, and no per-level override instructions in the role file. Sibling
role references are allowed only for the architect designer hat; this does not restore
retired orchestration/strategy/manager cross-references.

`test_manifest_reports_a_missing_source_instead_of_accepting_it` stages a copy of the tree in `tmp_path`
and breaks the manifest several ways — a renamed role file, a moved operation source, an unknown
operation, an unknown core block, a missing criteria catalog — asserting each is reported, then
re-resolving the healthy staged copy so the negatives are not false alarms. That last assertion is the
load-bearing negative: a validator that would silently accept a missing source would make every other
manifest assertion meaningless.

`test_every_relative_path_the_corpus_cites_resolves` walks every Markdown file under the lifecycle root,
extracts path tokens through `cited_paths` (backticked paths plus `PATH_TOKEN` matches, filtered by
`NON_LOCATION_RE` and `SYMBOLIC_FILE_NAMES`), and resolves each either relative to the citing file or
against `CORPUS_LOCATIONS`. It caught a real defect during the consolidation — a
`../w-02-light-task-workflow/requirement-packet-template.md` reference in `core/loop.md` that resolved
inside the wrong skill until it was corrected to `../../`. A new `COORDINATION_ROOT_RE` guard keeps
paths that belong to the coordination tree (`system/`, `tasks/`, `notes/`, `runtime/`, `worktrees/`,
`memory-repos/`) out of the repository-relative resolution space instead of reporting them as dangling.

`test_link_check_reports_a_repo_relative_anchor_pointed_at_nothing` is that check's own negative: it
stages a tree whose document cites a repo-relative path that exists nowhere and asserts
`unresolved_references` reports it, so the link check cannot silently pass by resolving nothing.

### The Compact-Curation Policy And Retired-Wording Guard

The exact retired-sentence census reaches the canonical tree and all nine generated
copies, with seeded re-insertion controls and a preserved developer-request-doctrine
control. `CURATION_POLICY_STATEMENTS` names the two compact curation sources. The
canonical positive case checks every declared marker; the generated-copy helper accepts
any one marker, so that case alone cannot prove both the complete-curation sentence and
`prepare → publish → validate`. Exact canonical projection equality in
`test_sync_scripts.py` provides the stronger copy-delivery facet. Whole retired
sentences are matched only on surfaces that shipped them; fresh semantic contradiction
wording remains outside this matcher.

### Conventions

Module-level helpers and disposable tree fixtures use no network or provider access.
The manifest/role cases read the canonical tree; curation cases also inspect the declared
generated trees. A new corpus invariant belongs
here as a new assertion rather than in a separate ad-hoc script.

### Invariants And Boundaries

- Corpus-shape cases read canonical sources; curation-wording cases also read generated
  copies. `scripts/sync-skills.py --check` and the projection suite guard byte equality.
- Each positive case has a paired negative (a broken manifest, a copied payload, a dangling anchor), so a
  check that resolves nothing cannot pass as green.
- Assertions are property-based on the corpus, so they stay valid as role prose changes; only a change to
  the corpus **shape** should require editing this module.
- The module must never weaken `SANCTIONED_SIBLING_REFERENCES` to accommodate a new cross-reference — a
  new sibling reference is a corpus design change, not a test fix.
- A manifest that names a missing source must keep failing: that assertion is what makes the manifest
  trustworthy.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local corpus check.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The resolver under test and the six shipped cases. [1]
- The corpus this module is the behavioral check for: the canonical root `skills/l-01-agent-lifecycles/` tree, whose declared contract is `ROLE_ORDER`, `REQUIRED_SECTIONS`, `MACHINE_SECTION` and `OPERATION_KEYS`. [2]
- The manifest this module resolves, and the corpus it governs. [3]
- Generated copies are checked by the propagation owner, not by this module. [4]

### Cross-Repo References

No sibling-repository contract defines this corpus check.

No meaningful cross-repo references found.
