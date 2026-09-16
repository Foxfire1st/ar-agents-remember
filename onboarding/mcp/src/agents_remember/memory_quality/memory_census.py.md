# mcp/src/agents_remember/memory_quality/memory_census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/memory_census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Memory quality overview](overview.md)

## Purpose

Builds the deterministic governed-memory census from the contract-owned exact Git scope. The census reads exact code and memory trees, classifies file sidecars, inline onboarding, route overviews, and entity rows, and emits a structural worklist without making semantic acceptance or final-certification decisions. Current candidate metadata is authoritative for live mappings; historical metadata is retained only for removal context and cannot veto a valid current mapping.

## Code Commentary

### Logic

`_Tree` reads exact Git members and metadata without silently normalizing paths. `_Census.sidecars` validates current canonical mappings and carries a historical mapping forward only when its path is absent from the candidate tree. `_Census.edited_documents` treats current metadata as authoritative, blocks current missing metadata, and uses a historical-only document to retain an absent row without a removal blocker. `_Census.add` records the expected final presence and preserves pre-existing absent rows for curator accountability. `_Census` records governed identities, presence, source paths, and reasons across sidecars, inline blocks, route overviews, edited documents, and entity rows. `build_memory_census` assembles the ordered result from the route-owned `MemoryCensusScope`.

### Invariants And Boundaries

- Exact Git tree membership and UTF-8 relative paths are validated before a row is emitted.
- Current missing or contradictory sidecar metadata remains a structural blocker; a stale historical association alone does not veto a valid current mapping.
- Missing newly required artifacts remain structural blockers; pre-existing artifacts absent from the candidate remain census rows with `expectedFinalPresence=absent` for curator accountability.
- The census is a derived preparation worklist; it does not publish semantic judgments, coherence, or certification.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the repository source is the governing evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The census module has no external domain dependency. | `build_memory_census` | mcp/src/agents_remember/memory_quality/memory_census.py:501-534 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact Git members and metadata are read through the private tree reader. | `_Tree` | mcp/src/agents_remember/memory_quality/memory_census.py:45-125 |
| Current sidecar mappings are authoritative, while historical mappings survive only for paths removed from the candidate tree. | `sidecars` | mcp/src/agents_remember/memory_quality/memory_census.py:254-318 |
| Edited current metadata is checked for missing or contradictory artifact type and mapping; historical-only documents retain an absent row without a removal blocker. | `edited_documents` | mcp/src/agents_remember/memory_quality/memory_census.py:395-443 |
| Structural rows are accumulated for inline onboarding, route overviews, and entities. | `inline`; `overviews`; `entities` | mcp/src/agents_remember/memory_quality/memory_census.py:320-393; mcp/src/agents_remember/memory_quality/memory_census.py:445-498 |
| The route-owned scope is converted into one ordered census result. | `build_memory_census` | mcp/src/agents_remember/memory_quality/memory_census.py:501-534 |

## Cross-Repo References

None; this module consumes the resolved local code/memory pair only.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/memory_quality/memory_census.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the `MemoryCensusScope` import now comes from
  `memory_quality.memory_census_scope`). Re-read the card against the current source: all five cited
  ranges (45-125, 254-318, 320-393, 395-443, 445-498, 501-534) still hold and the card names no
  import path. No wording changed; verification metadata remains closeout-owned.
- 2026-09-09T23:45:19+02:00 — CCR-L42 census regression reconciliation: documented current-versus-historical metadata authority, preservation of pre-existing absent rows without a removal blocker, and the moved old/new row behavior. Verification metadata remains unchanged until closeout.

- 2026-09-09T18:57:35+02:00 — CCR-L42 census repair: documented current-candidate metadata authority, historical-only removal context, and the current source ranges for sidecar and edited-document handling. Verification metadata remains unchanged until closeout.

- 2026-09-09T02:44:55+02:00 — CCR-L38 bounded inherited citation repair: simplified the four anchors to resolvable method identifiers within the existing behavior-bearing ranges; source-sha256=2bbd75f359b0ab57e3c07ffd51253e93e9084a32905742a1a552fac0a14f52dd; verification metadata remains unchanged.

- 2026-09-09T02:43:28+02:00 — CCR-L38 bounded inherited citation repair: restored code-identifier backticks for the four `_Census` anchors so the cited ranges resolve to the behavior-bearing methods; source-sha256=2bbd75f359b0ab57e3c07ffd51253e93e9084a32905742a1a552fac0a14f52dd; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent governed sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `2bbd75f359b0ab57e3c07ffd51253e93e9084a32905742a1a552fac0a14f52dd`). No future candidate verification stamp was used.
