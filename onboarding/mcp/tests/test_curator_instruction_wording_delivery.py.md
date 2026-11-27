# mcp/tests/test_curator_instruction_wording_delivery.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Compiled-capsule delivery, refused-write ladder, composition-manifest, and Curator writer-admission wording proofs split out from `test_curator_instruction_wording.py`.

## Code Commentary

`_deliver_indexed_detail` compiles a `(role, operation)` capsule, checks its `{{detail:...}}` Reference-index pointer and byte identity, and runs `compose_launch_instructions` to verify emitted detail files. Shared assertion helpers verify coordination routes and `held` kernel/reference delivery (`assert_coordination_routes`), Git comparison scope (`assert_git_comparison_scope`), cross-role message-handover delivery (`assert_message_handover_delivery`), and harness permission delivery with mutation teeth (`_require_permission_delivery`). `CuratorInstructionWordingDeliveryTests` covers the eight historical failed scenario steps, Reviewer initial-mode wait before intake enforcement, refused-write ladder delivery versus hard stops, manifest coordination descriptions and role tool grants, and Curator writer admission plus CLI `knowledge-ingest` flag parsing (`--commit` admitted; `--baseline`, `--publish`, and `--publish-to` rejected).

## Relationships

Split from `mcp/tests/test_curator_instruction_wording.py`. Uses `_compiled_outcome` from `test_l84_capsule_delivery_proofs.py`, `compose_launch_instructions`, `filter_shared_block`, `shipped_composition_corpus`, `cli.__main__.build_parser`, and `PUBLIC_TOOLS`.

## Evidence

- `_deliver_indexed_detail` proves compiled detail-pointer emission, byte parity with canonical skills, and launch-instruction link rewriting. [1]

- Coordination-route, Git-comparison, and cross-role message-handover helpers verify compiled shared-block clauses and detail links with mutation checks. [2]

- `CuratorInstructionWordingDeliveryTests` pins the 8 failed scenario steps, Reviewer intake wait, refused-write ladder, manifest role descriptions/tools, and `knowledge-ingest` CLI admission. [3]
