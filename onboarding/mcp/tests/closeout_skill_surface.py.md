# mcp/tests/closeout_skill_surface.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Names, once, the canonical closeout workflow text and the packaged copy of it. A landing publishes nothing without the check (MIK-R152 rule 10), and the cases that assert the corrected wording read both copies from here, so a rename of the skill tree is one edit rather than a search.

## Code Commentary

`PACKAGE` resolves to `mcp/src/agents_remember` and `CHECKOUT` to the checkout above `mcp`, so the two copies are addressed from one module. `SKILL` is `skills/w-02-light-task-workflow/workflows/closeout.md`; `PACKAGED_SKILL` is the same relative path rooted at `package_data/runtime/skills`, the tree the capsule compiler reads. `closeout_texts` reads both files as UTF-8 and returns them canonically-first. The module holds no assertion itself: it is the surface the wording cases compare.

## Invariants And Boundaries

Reading only, and no fallback: an absent copy raises from `read_text` rather than answering empty. The packaged copy is not live until the sync has run, which is why the cases read both and not one.

## Evidence

### Repo-Internal References

- The canonical and packaged closeout texts are read from the one named skill path. [1]

- The packaged copy is addressed under the runtime package data tree the compiler reads. [2]
