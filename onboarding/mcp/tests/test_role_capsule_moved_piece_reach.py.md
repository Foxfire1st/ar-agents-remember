# mcp/tests/test_role_capsule_moved_piece_reach.py

## Governing Overview

[overview](overview.md)

## Purpose

The test proves that a compiled capsule keeps the pointer or inline paragraph that a moved piece of role text needs: each case mutates one source in a copied corpus and shows that the compile then loses the reach, while the unmutated corpus keeps it.

## Code Commentary

`_compile_moved_piece_witness` routes an admission for one role and operation through the copied corpus's manifest, compiles it with the shipped binding, and returns `(rendered_instructions, detail_paths)` where `detail_paths` is the set of `detail_references` source paths.

The Architect case runs for the `requirement-packet`, `leaf-task`, and `master-task` templates through two-tier progressive disclosure: `[authoring]({{detail:reference/tasks/document-authoring.md}})` must occur once in `roles/architect.md` and resolve in `detail_references`, and `[<label>](../../templates/<name>.md)` must occur once in `reference/tasks/document-authoring.md` pointing to the template holding its pinned clause. Mutating either layer fails with `missing authoring detail pointer` or `missing template link`, and restoring the source passes again.

The Curator case takes the two `operations/curation.md` paragraphs that begin with `Verify writer outputs resolve in \`workspace.memoryRoot\`. Read \`worktree_status\`` and with the intake-staleness rule (`Record staleness known at task intake as the task’s curation work.`). Each must stand in the delivered `## Workflow` section of the Curator's curation capsule, and removing it fails with `missing inline workflow paragraph`.

## Relationships

Compilation goes through `compile_admitted_capsule` and `routed_admission_for`; `LIFECYCLE_ROOT`, `MANIFEST_RELATIVE` and `_shipped_binding` come from `test_role_capsule_admission.py`. `test_role_capsule_manifest_edges.py` holds the manifest, source-admission and shared-digest edge cases.

## Evidence


- The witness compiles one admitted role and operation from a copied corpus and returns its rendered instructions and detail reference paths. [1]


- The Architect's template links remain reachable through its Tier-2 document-authoring detail reference; dropping either layer fails. [2]


- The Curator's inline workflow paragraphs must reach its delivered Workflow section; a removed paragraph fails. [3]
