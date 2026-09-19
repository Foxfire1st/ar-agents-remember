# mcp/src/agents_remember/models/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`__init__.py` re-exports the public Pydantic response-contract model surface.

## Code Commentary

### Logic

The initializer is a single import surface over twelve owning modules plus one curated package,
and it owns no model of its own. Its behaviour is entirely in what it makes nameable:

- cit:([`StrictResponseModel`], mcp/src/agents_remember/models/base.py:13-16), cit:([`FlexibleResponseModel`], mcp/src/agents_remember/models/base.py:19-30) and cit:([`ResponseModel`], mcp/src/agents_remember/models/base.py:66-88) arrive from
  `base.py` along with their envelope siblings, so a consumer can type a response without
  knowing which of the two `extra` families it belongs to.
- The domain response models arrive per route: `context_packet`, `core`, `drift`, `memory`,
  `providers`, `runtime`, `skills`, `worktree`, and the `benchmarks` pair. Each name keeps its
  owning module as the behavior authority; nothing is re-declared here.
- cit:([`PUBLIC_TOOL_RESPONSE_MODELS`], mcp/src/agents_remember/models/tools/tool_registry.py:255-259) is re-exported so a consumer reads the
  advertised tool surface without importing the `models.tools` package. It is a PROJECTION of
  the wider registry, computed by excluding the internal compatibility payload builders — which
  is why importing it here is not the same as importing the whole registry.
- cit:([`finalize_payload_tokens`], mcp/src/agents_remember/models/tokens.py:232-250) and cit:([`dump_with_token_count`], mcp/src/agents_remember/models/tokens.py:268-268) arrive with the
  counter classes and cit:([`DEFAULT_TOKEN_COUNTER`], mcp/src/agents_remember/models/tokens.py:205-205). The token fields on every response
  envelope are filled by these, not by the response models.
- cit:([`conversations`], mcp/src/agents_remember/models/__init__.py:3-5) is aliased `as conversations` under an explicit
  `# curated package surface` comment. The alias is load-bearing rather than stylistic: it is
  what keeps the subpackage reachable as an attribute of this initializer once the submodule
  has been imported, so `models.conversations` resolves for a caller that only imported
  `models`.
- cit:([`__all__`], mcp/src/agents_remember/models/__init__.py:90-165) is an explicit, alphabetically ordered list rather than a
  wildcard, so an export cannot appear by accident of an import statement.

### Conventions

- Exports only. A behavior that lives here is a behavior no sidecar owns, so the contract
  statement belongs in the concrete module and only the NAME belongs in this file.
- One import block per owning module, no `import *`.
- `__all__` stays sorted and stays complete: the tuple is the declared public surface, and
  `models.base.ResponseEnvelope` names the union every registered tool response belongs to.

### Invariants And Boundaries

- Adding a name to the import blocks without adding it to `__all__` exports nothing; adding it
  to `__all__` without importing it fails at import time.
- The public-response registry this file re-exports must stay a stable projection of the wider
  registry: cit:(["public response-model registry is not a stable projection"], mcp/src/agents_remember/mcp/public_surface.py:172-176) and
  cit:(["public tools and response-model registry disagree"], mcp/src/agents_remember/mcp/public_surface.py:177-180) are the two import-time
  assertions that hold that, and both run against this re-exported object.
- Re-exporting a name here does not make it a public TOOL. The tool roster and this model
  surface are checked against each other elsewhere; this file is the model half only.

### Todos

None recorded.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| This initializer declares the public model export list. | `__all__` | mcp/src/agents_remember/models/__init__.py:90-90 |

## 260731-EFA-L9 Change

The initializer now also re-exports the curated conversation wire-model surface from
`models/conversations/` (R6) — the shared evidence/control-wire contracts, conversation
primitives/identity/cursors/content/capabilities/status/stream/history/operation DTOs, and
telemetry — keeping the package initializer exports-only.

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: `PUBLIC_TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:255-259. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the package export only repoints the public tool registry to its moved `models.tools` package. Verified at code commit `1d446724`.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the conversation-model export
  additions; the L9 change section above documents them. Verification metadata pinned until
  closeout stamps the L9 code commit.
- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: bound the public model-export claim to exact initializer anchors and normalized scoped citation evidence.

- 2026-06-11T06:47+02:00 — No content impact: `DirectCloseoutPreviewResponse`/`DirectCloseoutApplyResponse` left the export surface (import block and `__all__`) with the issue #62 worktree-only closeout; the exports-only contract this sidecar describes is unchanged.
- 2026-06-01T20:45+02:00 — Added `WorktreeAbandonResponse` to the response-model export surface for the `worktree_abandon` tool.
- 2026-05-31T12:50+02:00 — Dropped `CodexExecutionPolicy` from the export surface (removed from the `agents_remember.models.benchmarks` import block and from `__all__`); behaviour-preserving export-surface reduction, no sidecar prose named the removed symbol (1.0.0 review remediation).
- 2026-05-30T22:29+02:00: Added `finalize_payload_tokens` to the token-helper export surface (import and `__all__`) for the S6 token-counter wiring. Verification metadata stays pinned until closeout commits the change.
- 2026-05-28T19:52+02:00: Created for the response-contract package export surface.
