# dashboard/src/cockpit/roleChatExecutionView.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Project stored options and exact selected execution into launcher display facts.

## Code Commentary

Pure helpers select loading/busy/error state, receipt and pending/failure context, and retained retry selection. A pending options request hides the previous fresh answer. Settled options supply their own defaults and catalog; otherwise only the saved disk catalog supplies displayed agents, origin and discovery state, with empty defaults and Start not ready. Catalogs from different answers are never merged. Loading suppresses an execution display; selected request identity wins over a newer sibling receipt.

## Boundaries

No HTTP, storage mutation, callback dispatch or backend admission. The projections do not infer task acceptance from a completed execution.

## Evidence

- resolveRequestExecution is a current owner of the behavior described above. [1]

- resolveLauncherCatalog uses one settled options answer or the saved disk catalog, never merged inventories; pending display carries no role defaults and is not ready. [2]
