# mcp/tests/test_memory_citation_fix_scopes.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Document-scoped citation repair isolation and normalization, plus the refusal to retarget a claim across the tree while its cited file is still live or its continuity is unproven.

## Code Commentary

### Logic

A scoped repair leaves another document byte-identical. Invalid exact paths refuse before discovery or source acquisition. Expanded source ranges deduplicate and a second run writes nothing. A malformed source segment blocks normalization while retaining the original evidence and typed finding.

`LiveCitedFileRetargetTests` records the production defect and pins BOTH refusal directions on one tree shape: a claim cited two adjacent tool names in `mcp/tools/base.py` and the tuple holding them was relocated while the cited file kept existing, so the wider-tree lookup found each name's single definition — the registrar functions that declared them — and rebound the claim to a different fact that never supported it. An anchor that left a live cited file is now declined as `anchor_left_live_file`; a deleted cited file whose extent is not readable at the card's stamp is declined as `anchor_continuity_unproven`; the legitimate relocation still repairs once the cited file is gone and continuity holds; and a mention rebound to that name's declaration is declined as `anchor_kind_changed` (the `PUBLIC_TOOLS` tuple mention versus the `@server.tool()` registrar definition). `DocumentScopeTests._two_failing_cards` was rewritten to build real provenance: `kernel/gone.py` held both anchors at the recorded stamp, that stamp is committed, the file is then deleted, and both cards carry that stamp. The four existing scoped-fix tests remain.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Scope is a write boundary in a shared memory worktree. Failure to normalize must not delete the malformed claim or broaden to neighboring documents. An exact name match elsewhere is not by itself a safe retarget: the cited file must be gone and the extent the claim was verified against must be readable at its stamp with the same kind, or the claim is declined instead of rebound.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- An anchor that left a still-existing cited file is declined instead of retargeted. [1]
- A deleted cited file without continuity at the stamp is declined. [2]
- The same anchor relocates once the cited file is gone and continuity holds. [3]
- A mention rebound to that name's declaration is declined as a kind change. [4]
- Two anchors that left one cited file, each still declared where the move put it. [5]
- A scoped fix leaves every other document byte identical. [6]
- Invalid exact paths refuse without memory discovery or source acquisition. [7]
- Expanded sources are deduplicated and the second run is byte identical. [8]
- A malformed source segment blocks normalisation without deleting evidence. [9]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
