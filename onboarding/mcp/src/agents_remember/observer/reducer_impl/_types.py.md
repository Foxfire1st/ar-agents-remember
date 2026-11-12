# mcp/src/agents_remember/observer/reducer_impl/_types.py

## Governing Overview

[overview](../overview.md)

## Purpose

Input bundles shared by the reducer's assembly and its split builders. ``WorkspaceStructure`` is the slice-3a pre-image (enclosures + admitted worktree groups); ``AnalyticalInputs`` is the slice-3b pre-image the analytical surfaces are built from. Both remain the design’s own two slices and are re-exported by `agents_remember.observer.reducer`. Both dataclasses are frozen; `WorkspaceStructure` requires enclosures and defaults active groups, while `AnalyticalInputs` supplies default-empty feeds. Neither bundle carries a provider or setup feed. `AnalyticalInputs` includes `closeout_queues` and the five native attention fact collections (`native_attention`, defaulting empty); verification-age `sidecar_staleness` and `stalest_limit` are removed.

## Code Commentary

- `WorkspaceStructure`
- `AnalyticalInputs`

The frozen bundles retain enclosures and admitted groups separately from analytical inputs. `AnalyticalInputs.task_sources` and a default-unknown `HostActivitySnapshot` replace task_documents/series inputs. Attention acknowledgements remain supplied data for pure ranking; these carriers neither infer task stage nor grant action authority.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_types.py`.

## Evidence


- Frozen structural and analytical bundles retain their separate owners without removed gate/pickup/expectation or verification-age inputs. [1]


- Frozen structural and analytical bundles retain their separate owners without removed gate/pickup/expectation or verification-age inputs. [2]







### Repo-Internal References
