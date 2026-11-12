# mcp/src/agents_remember/package_data/paseo_plugin/client/page.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The adapter is the single browser-object and injected test seam for canonical plugin helpers.

## Code Commentary

The shared prototype setItem wrapper preserves receiver/arguments and original refusal before notifying a current listener. Quiet plugin storage bypasses that observer. Cleanup restores the original only while the same wrapper owns the slot. currentPage gathers web objects/storage or returns no page.

## Invariants And Boundaries

Only the observed app write path has provenance; captured originals/property assignment do not. Observation cannot break writes or unwrap a later foreign wrapper. Native/non-web/unavailable storage supplies no page.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `watchWrites` | `mcp/src/agents_remember/package_data/paseo_plugin/client/page.ts:44-74` |
| Current source owner or exact assertion described above. | `quietStorage` | `mcp/src/agents_remember/package_data/paseo_plugin/client/page.ts:93-123` |
| Current source owner or exact assertion described above. | `currentPage` | `mcp/src/agents_remember/package_data/paseo_plugin/client/page.ts:106-124` |

## MIK-R95 Storage Write Transform

`watchWrites` accepts an optional string-pair transform, applies it only to direct `localStorage.setItem` calls with two string arguments (preserving receiver and arity for every other call, including native refusals), and observes only writes whose first two arguments are already primitive so an object value is not coerced a second time. This is the seam the document sidebar policy uses to keep the shared stored sidebar choice.
