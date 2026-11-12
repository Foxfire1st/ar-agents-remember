# dashboard/src/panels/review/codeFacts.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Admit already-read leaf-wide code facts only for the shown comparison, count unchanged invariant records whose implementation changed and preserve local scroll on count enrichment.

## Code Commentary

`matchingTreeRead` requires a trees answer and, when a comparison number is supplied, an equal delivered number. `codeFacts` accepts only a facts state, otherwise null. `codeChangesCount` requires an admitted outline and code map and counts distinct unchanged outline invariant IDs with established implementation facts. It is not a count of changed source files or all code changes. Summary text preserves reading/unavailable state.

`CodeFactsScrollAnchor` snapshots the nearest tree scroller and root ancestors before a same-comparison count update, then restores those scroll coordinates after mutation. `useCodeFactsNotice` keys its sentence by comparison/count and never selects or focuses a row. Zero explicitly says no invariant changed only in its code; it does not say that no code changed. This module issues no fetch and infers no implementation fact.

## Evidence

- codeFacts.ts current behavior at this source owner. [11]
- codeFacts.ts current behavior at this source owner. [12]
- codeFacts.ts current behavior at this source owner. [13]
- codeFacts.ts current behavior at this source owner. [14]
