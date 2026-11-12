# test_role_instruction_corpus.py

## Governing Overview

[overview](overview.md)

## Purpose

The shipped behavioral guard for the canonical lifecycle corpus: every role and operation
resolves to a readable source, the role registry has no ambient-launcher seat, and the
manifest carries routing metadata without copied payloads. Role sources are concise,
parseable and self-contained; the retired fixed section order, inherited Core declaration
and operator knob block are absent. Relative repository references resolve, while
coordination-owned and symbolic names retain their stated resolution limits.

## Current source account

Compact native role/operation sources remain manifest-resolved. Positive compact-curation checks use CURATION_POLICY_STATEMENTS; the exact retired-sentence guard retains seeded re-insertion/removal controls and developer-request doctrine. The handoff-contract test declares canonical-plus-one-packaged-copy containment checks on `templates/curator-handoff-ingestion.md` for current onboarding rows, no counted-card-edit-alone answer and references-only counted sidecar edits; in both trees the ingestion template and `reference/curator/card-formats-and-citations.md` are checked for the card and overview row subjects and the updated/no_impact dispositions, each ingestion clause with a deletion control. These narrow text assertions are not propagation-owner byte equality.

Two separate witnesses cover task authoring. test_new_series_guidance_requires_json_primary_master_before_dependencies delegates to `task_document_instruction_contracts.assert_contract` over the canonical lifecycle tree and every declared generated skill-copy root. The architect role and the leaf, master and requirement-packet templates must carry their pointer to `reference/tasks/document-authoring.md` outside example fences and none of the three obsolete guidance fragments; that reference must state its task-field clauses under one heading, `operations/orientation.md` must keep its `task_doc`-first clauses, and the manifest's task-authoring references must keep their sources, roles and injection flags, with deletion controls on the pointers and clauses. This is text containment, not proof of generated-copy byte equality.

The separate test_native_new_master_then_indexed_leaf_dependencies uses the real application task_doc_tool on temporary coordination data. Its legacy control seeds a leaf through write_task_doc and a Markdown-only master, expects a master-naming refusal for waitsFor, and compares the pre-existing fixture files’ bytes. In a fresh sibling series it then calls create for a JSON-primary master and two leaves, asserts parent row IDs [A, B], accepts A waiting for B, and checks persisted waitsFor and the generated Order heading. It does not migrate the legacy series, assert every possible write artifact is absent, or execute a role/worktree lifecycle. These are source assertions, not a run result.

The undeclared-surface negative control follows `fragment_one_surfaces()`; its carrier is derived from the declared fragment. The canonical corpus plus its sole packaged projection are the checked roots; byte equality remains the propagation owner's separate obligation.

## Code Commentary

### Logic

The module resolves its subject from the repository root (`REPOSITORY_ROOT` → `SKILLS_ROOT` →
`LIFECYCLE_ROOT` → `MANIFEST_PATH`), so it always tests the worktree it runs from. Its declared
vocabulary is the corpus contract in miniature: `ROLE_ORDER` and `OPERATION_KEYS` bind the
role and operation registries. `MACHINE_SECTION` identifies a retired knob block that
concise role sources must not carry. The JSON-primary authoring case separately builds disposable coordination fixtures and invokes task_doc_tool; it is not a pure corpus-text check.

The resolver is deliberately split into small cohesive helpers — `_check_core`, `_check_operations`,
`_check_roles` (with `_check_role_order` and `_check_one_role`), and `_check_launcher_and_references` —
and `_resolve_sources` returns a list of human-readable problems rather than a boolean, so a manifest entry
that names a missing source, an unknown core block, an unknown operation, or a missing criteria catalog is
**reported**, never skipped.

`test_manifest_resolves_every_role_and_operation_source` additionally asserts the exact
`ROLE_ORDER` registry, that `launcher` is absent from `manifest["roles"]`, and that the routing
conditions are exactly `supplied-native-role-binding` and `manual-taskless-projects-role`.
`ambient-launcher` belongs separately to `manifest["launcher"]["routing_condition"]`. The router
checks require `composition-manifest.json` and `one applicable operation`, not every role-file
name; the manifest must have no mechanically detected prose lines.

`test_manifest_carries_routing_metadata_not_copied_payloads` is the metadata-plane case: it walks every
JSON string in the manifest (`_iter_json_strings`), applies the `manifest_copy_indicators` heuristics, and
fails on copied payload content, so the manifest cannot quietly become a second copy of a source section.
It is staged against a `tmp_path` copy so it can also prove the detector fires on a deliberately copied
payload without failing the healthy tree.

`test_every_role_source_is_concise_and_well_formed` checks canonical YAML name and
description, readable headings, no inherited Core line, no machine/operator knob block
or knob table rows, and no per-level override instructions in the role file. Sanctioned sibling
references are the architect/orchestrator referrals to
`roles/manager.md` for the single questions-received policy; other sibling references remain
forbidden.

`test_manifest_reports_a_missing_source_instead_of_accepting_it` stages a copy of the tree in `tmp_path`
and breaks the manifest several ways — a renamed role file, a moved operation source, an unknown
operation, an unknown core block, a missing criteria catalog — asserting each is reported, then
re-resolving the healthy staged copy so the negatives are not false alarms. That last assertion is the
load-bearing negative: a validator that would silently accept a missing source would make every other
manifest assertion meaningless.

`test_every_relative_path_the_corpus_cites_resolves` walks every Markdown file under the lifecycle root,
extracts path tokens through `cited_paths` (backticked paths plus `PATH_TOKEN` matches, filtered by
`NON_LOCATION_RE` and `SYMBOLIC_FILE_NAMES`), and resolves each either relative to the citing file or
against `CORPUS_LOCATIONS`. The `COORDINATION_ROOT_RE` guard keeps
paths that belong to the coordination tree (`system/`, `tasks/`, `notes/`, `runtime/`, `worktrees/`,
`memory-repos/`) out of the repository-relative resolution space instead of reporting them as dangling.
Bootstrap's bare `memory.md` ledger is skipped only in `operations/bootstrap.md` and only on a line that
places it at the memory repository root.

`test_link_check_reports_a_repo_relative_anchor_pointed_at_nothing` is that check's own negative: it
stages a tree whose document cites a repo-relative path that exists nowhere and asserts
`unresolved_references` reports it, so the link check cannot silently pass by resolving nothing. It also
reports Bootstrap's ledger once its location wording or path changes, and reports a missing backticked path
in a shared file (`core/acceptance.md`) and a deleted target.

### The Compact-Curation Policy And Retired-Wording Guard

The exact retired-sentence census reaches the canonical tree and its sole declared packaged
copy, with seeded re-insertion controls and a preserved developer-request-doctrine
control. `CURATION_POLICY_STATEMENTS` names the two compact curation sources. The
canonical positive case and the generated-copy helper both require every declared clause; the
generated-copy case also seeds the canonical bodies into a temporary tree and proves that deleting
any declared clause, or weakening either Curator role pointer to `operations/curation.md`, is
reported. Seeds for retired sentences whose source file is gone (the designer and strategist roles
and the worker-brief template) still exercise their source-confined reader, and the case asserts
those files stay absent. Exact canonical projection equality in
`test_sync_scripts.py` provides the stronger copy-delivery facet. Whole retired
sentences are matched only on surfaces that shipped them; fresh semantic contradiction
wording remains outside this matcher.

### Conventions

Corpus helpers and disposable fixtures declare no network/provider access. Corpus-shape cases read the canonical tree; curation, handoff-contract and task-authoring guidance cases declare generated-copy reads. A temporary task_doc authoring/refusal case is distinct from those text loops.

### Invariants And Boundaries

- Corpus-shape cases read canonical sources; retired-curation wording and the handoff-contract test
  also declare generated-copy reads. The latter checks canonical plus the sole packaged copy of both the
  Curator ingestion template and the card-format reference for the R53 answer sentences. Narrow normalized-text
  containment is distinct from propagation-owner byte equality (`scripts/sync-skills.py --check`
  and the projection suite).
- Each positive case has a paired negative (a broken manifest, a copied payload, a dangling anchor), so a
  check that resolves nothing cannot pass as green.
- Corpus-shape assertions target structural properties; the explicit handoff R53 containment
  assertions also pin selected prose contract sentences, not every possible semantic contradiction.
- The module must never weaken `SANCTIONED_SIBLING_REFERENCES` to accommodate a new cross-reference — a
  new sibling reference is a corpus design change, not a test fix.
- A manifest that names a missing source must keep failing: that assertion is what makes the manifest
  trustworthy.

### Todos

None recorded.

Packet-alignment and independent-preparation cases bind each clause to its actual step and reject deletion or relocation. Separate cases require knowledge worklist and landing-gate explanations at their current owners and check the admitted parser/tool surfaces; they do not grant relay artifact-inspection authority. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

The Architect's formal-permission rule must sit in its own Architect-owned section of `operations/orientation.md`, with a deletion or relocation control per clause. `test_each_public_command_requires_its_documentation_owner` runs once per public CLI command and proves that the reference check fails when the command's row is taken out of the agents' command table, or, for a name of the set `UNDOCUMENTED_COMMANDS`, when a row for it is added to that table.

`test_root_instructions_name_no_retired_job_lens_or_phase` requires that `lenses.md` is absent and that neither the lifecycle tree nor the root `AGENTS.md` contains `reframe-research` or `as a *lens*`. `test_role_names_its_publication_moments` requires, in the canonical and the packaged copies of `roles/manager.md` and `roles/architect.md`, exactly one publication clause that names the role's moments, exactly one mention of `system/task-publication.md` and no "When publishing task work" sentence. The Manager clause assigns the leaf's issue and sets In progress when it claims the leaf before the start, and closes the issue after the landing and both pushes; the Architect clause creates the leaf's open linked issue when it registers the leaf.

## Evidence
### Docs References

No external or domain documentation governs this repository-local corpus check.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The resolver under test reports missing manifest sources rather than silently accepting them. [1]

- The corpus this module is the behavioral check for: the canonical root `skills/l-01-agent-lifecycles/` tree, whose declared contract is `ROLE_ORDER`, `MACHINE_SECTION` and `OPERATION_KEYS`. [2]

- The manifest this module resolves, and the corpus it governs. [3]

### Cross-Repo References

No sibling-repository contract defines this corpus check.

No meaningful cross-repo references found.


- This module declares narrow normalized-text R53 assertions over canonical plus the sole packaged copies of the Curator ingestion template and card-format reference; the propagation owner separately checks projection byte equality. [4]


- Task-authoring guidance checks delegate to the shared task-document instruction contract across the canonical and declared generated roots, and a separate real task_doc fixture covers the legacy-master refusal and new JSON-master authoring. Neither is a copy-equality result or executed acceptance; existing retired-sentence controls and propagation-owner equality responsibility remain. [5]

- Neither the lifecycle tree nor the root `AGENTS.md` names the retired job lens or reframe-research phase, and `lenses.md` is absent. [8]
- Each copy of the Manager and Architect roles holds its publication clause once, names `system/task-publication.md` once and has no generic publishing sentence. [9]

## Current source evidence

- The handoff checks consume the canonical corpus and declared generated roots; the fragment-one control derives its surface through `fragment_one_surfaces` rather than naming a fixed skill. [6]

- Packet-alignment and independent-preparation cases bind each clause to its actual step and reject deletion or relocation. Separate cases require knowledge worklist and landing-gate explanations at their current owners and check the admitted parser/tool surfaces; they do not grant relay artifact-inspection authority. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [7]
