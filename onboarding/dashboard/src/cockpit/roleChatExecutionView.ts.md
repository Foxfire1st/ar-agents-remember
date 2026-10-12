# dashboard/src/cockpit/roleChatExecutionView.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Project stored options and exact selected execution into launcher display facts.

## Code Commentary

Pure helpers select loading/busy/error state, receipt and pending/failure context, retained retry selection and origin-keyed agent inventory. Loading suppresses an execution display; selected request identity wins over a newer sibling receipt.

## Boundaries

No HTTP, storage mutation, callback dispatch or backend admission. The projections do not infer task acceptance from a completed execution.

## Evidence

- resolveRequestExecution is a current owner of the behavior described above. [1]
- resolveLauncherCatalog is a current owner of the behavior described above. [2]
