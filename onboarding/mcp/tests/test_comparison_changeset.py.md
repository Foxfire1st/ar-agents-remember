# mcp/tests/test_comparison_changeset.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_comparison_changeset.py` proves the viewer's comparison selector reads immutable trees through the actual HTTP routes: exact file lists with renames and scoped memory, dirty-worktree immunity, converted-base handling, alias-proof paths, and the refusal/400 boundaries.

## Code Commentary

The fixture builds four immutable trees with a real rename and an unchanged sidecar, records them as comparison 5, and serves `register_changeset_routes` over a `TestClient`. The exactness test validates the body against `ComparisonChangeSet`, asserts `mode == "comparison"` with echoed trees, counts exactly two `diff` children and no blob reads, checks `hasSidecar` pairing, excludes `notes/outside.md` from the memory half, and proves a later dirty edit never replaces the captured candidate. It then walks the refusal ladder: `comparison`+`mode` is a 400, unknown numbers and lost trees are 404s naming the tree, and a converted base wins over the legacy memory tree. The alias test (F01) shows historical file and symlink blobs stay addressed by their requested Git path while absolute, `..` and off-root memory paths are `bad-path` 400s.

## Evidence

- The body validates as the new comparison contract [1]
- Exact lists, renames, scoped memory and refusal ladder [2]
- Git calls are counted through the serving owner module [3]
- Historical paths ignore current filesystem aliases [4]
