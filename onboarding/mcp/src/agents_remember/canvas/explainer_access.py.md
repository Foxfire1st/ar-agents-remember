# mcp/src/agents_remember/canvas/explainer_access.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The checks the four kept tools pass before they act: the environment's binding, the caller's seat, the claim that a call names the binding the environment holds, and the shape of a revision or a path inside a tree.

## Code Commentary

- The module serves no read surface. The explainer reads with its harness's own tools, so what stays is what a grade, a category change and a render need to know before they act.
- `binding_claim` spells one comparison identity in full — the owner, the number and all four trees, or `planned@` with the two tips and their trees — so a claim and a binding are compared as identities rather than as a number that happens to match.
- `require_binding` refuses `explainer-missing` when the environment holds no `binding.json` and `binding-unreadable` when it cannot be read: no tool acts without one, and only a build writes one.
- `require_seat` delegates to `require_current_seat`, which refuses a launch marker pointing at another workspace, a server built with no caller identity, and an id that is not the one this workspace and generation derive: a stale generation or another leaf's marker is not this leaf's explainer.
- `require_claim` refuses `binding-moved` with the label, the digest and the `binding.json` the environment holds, and `binding-unknown` when the claim names no binding of this environment at all, instead of resolving the nearest one; the refusal carries no binding block.
- Between them, `relative_parts`, `object_name` and `tree_path` refuse traversal, an absolute path, an empty segment, a drive letter, a backslash and an option in a revision's place, as typed refusals answered as data; they are also the spellings the fingerprint reader builds its object names with.

## Evidence

- One comparison identity token names the owner, the number and all four trees, and a planned binding names its two tips instead [1]
- Traversal, an absolute path, an empty segment and a drive letter are refused as `path-refused` [3]
