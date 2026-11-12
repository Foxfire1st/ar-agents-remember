# mcp/tests/test_role_capsule_moved_piece_reach.py

## Governing Overview

[overview](overview.md)

## Purpose

The test proves that a compiled capsule keeps the pointer or inline paragraph that a moved piece of role text needs: each case mutates one source in a copied corpus and shows that the compile then loses the reach, while the unmutated corpus keeps it.

## Code Commentary

`_compile_moved_piece_witness` routes an admission for one role and operation through the copied corpus's manifest, compiles it with the shipped binding and returns the rendered instructions.

The Architect case runs for the requirement-packet, leaf and master templates. The pointer `<action> [<label>](../templates/<name>.md)` must occur once in `roles/architect.md`, the template must hold its pinned clause, and the compiled planning capsule must carry the pointer. Removing the pointer, or replacing its action with unrelated wording, fails with `missing template action pointer`, and restoring the source passes again.

The Curator case takes the two `operations/curation.md` paragraphs that begin with the `worktree_status` read before writing memory and with the intake-staleness rule. Each must stand in the delivered `## Normal workflow` section of the Curator's curation capsule, and removing it fails with `missing inline workflow paragraph`.

## Relationships

Compilation goes through `compile_admitted_capsule` and `routed_admission_for`; `LIFECYCLE_ROOT`, `MANIFEST_RELATIVE` and `_shipped_binding` come from `test_role_capsule_admission.py`. `test_role_capsule_manifest_edges.py` holds the manifest, source-admission and shared-digest edge cases.

## Evidence

- The witness compiles one admitted role and operation from a copied corpus. [1]
- The Architect's template pointers must survive compilation; a removed or displaced pointer fails. [2]
- The Curator's inline workflow paragraphs must reach its delivered Normal workflow; a removed paragraph fails. [3]
