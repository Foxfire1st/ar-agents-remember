# mcp/src/agents_remember/observer/reducer_impl/_types.py

## Governing Overview

[overview](../overview.md)

## Purpose

Input bundles shared by the reducer's assembly and its split builders. ``WorkspaceStructure`` is the slice-3a pre-image (enclosures + providers + admitted worktree groups); ``AnalyticalInputs`` is the slice-3b pre-image the analytical surfaces are built from. Both are the design's own two slices, so they live together and are re-exported by :mod:`agents_remember.observer.reducer`.

## Code Commentary

- `WorkspaceStructure`
- `AnalyticalInputs`

The frozen bundles retain structural enclosures/providers/admitted worktree groups separately from analytical inputs. R113 removes analytical gate, agent-pickup and expectation-row inputs; their old DTOs are not accepted here or materialized through this bundle. Attention dismissals remain an input for the surviving attention queue; this data carrier itself grants no action authority.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_types.py`.

## Evidence

- Frozen structural and analytical bundles retain their separate owners without removed gate/pickup/expectation inputs. [1]



### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
