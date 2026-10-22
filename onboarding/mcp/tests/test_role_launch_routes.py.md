# mcp/tests/test_role_launch_routes.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Launcher routes retain canonical report links, immutable request content, projection-before-launch and operation admission. The projection-ordering case builds its prepared dictionary inside the test: it plans the hand-over with the product's own planner (`planned_handover_file`) and stubs `_compile_handover` to return that dictionary, so the added `handoverFile` and `handoverFileContent` carry the builder's shape — the two fields the real builder returns at `role_launch_preparation.py:855-869` — and the write-once and projection-before-launch assertions read them. Public execution whitelists host fields, keeps saved calls private and separates report availability from status. Request replay and bounded matching taskless-history migration retain existing identity rather than minting replacement topology.

## Evidence

- The scoped current source carries the module/document behavior described above, and the projection case's prepared dictionary now carries `handoverFile` and `handoverFileContent` in the builder's shape, planned with the product's planner and returned by a stubbed compile. [1]
