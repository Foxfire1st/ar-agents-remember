# models/conversations/ — Responsibility-Owned Conversation Wire Models Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/models/conversations/` |
| onboardingRoute | `mcp/src/agents_remember/models/conversations/overview.md` |
| parentOverview | [`models/overview.md`](../overview.md) |
| lastUpdated | 2026-08-08T14:38+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|

## What This Area Is

The responsibility-owned conversation wire-model package created by 260731-EFA-L9 (R1/R2/R6).
It owns the stable, strict, native-authoritative wire grammar shared by active conversation
reads, dormant native history, operation/control projection, browser consumers, and
orchestration, plus the shared evidence and control-wire contracts the harness control plane
also consumes. It replaces `serving/conversation/models.py` and its five `_models_*` split files;
the old paths receive no forwarding shim.

## Hot Path Summary

Start with `__init__.py` (the curated `__all__` export surface) and `primitives.py` (`WireModel`,
opaque tokens). `evidence.py` and `control_wire.py` are the shared harness-control contracts;
`status.py`/`capabilities.py` are the evidence-bound status/capability authorities; `content.py`
owns `ConversationItem` and the sub-agent grammar. The zero-drift proof is
`mcp/tests/test_model_split_baseline.py` against
`mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json`.

## What Belongs Here

| Path | Role |
| --- | --- |
| `primitives.py` | Strict `WireModel` base and opaque purpose-branded tokens. |
| `identity.py` | Native/active identity, provenance, authorization/scope products. |
| `cursors.py` | Non-interchangeable cursor/key/resume families. |
| `content.py` | Typed content blocks, correlation, sub-agent ref, conversation items. |
| `capabilities.py` | Fixture-evidence-bound capability contract. |
| `status.py` | Evidence-to-turn-state vocabulary. |
| `stream_events.py` | Mutation/envelope grammar for the SSE stream. |
| `history.py` | Dormant library/page grammar with sub-agent rows. |
| `opening.py`/`interrupts.py`/`submissions.py`/`withdrawals.py`/`attachments.py` | Operation DTOs. |
| `telemetry.py` | Metric/evidence products and `operation_fingerprint`. |
| `evidence.py`/`control_wire.py` | Shared harness-control wire contracts (R2). |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Serving behavior, projectors, stores, control services | `serving/conversation/` and `serving/projections/` |
| Response envelopes/tool payload models | `models/` siblings (`base.py`, `tool_registry.py`, …) |
| Control-plane-only records | `serving/harness_control_models.py` (until L11) |

## Structures Found Here

- Strict immutable camel-case Pydantic wire models with unknown fields forbidden.
- Purpose-branded opaque token families (active page/event, library list/read/key, native
  resume, operation fingerprint).
- First-class sub-agent grammar (`ConversationAgentRef`, per-item `agent`, library agent rows,
  `agents_note`).
- Shared evidence frames/pages/truncation and control-wire state/submission/provenance families.

## Operating Model

1. Modules import only from lower layers (primitives → identity → cursors → domains →
   stream_events/history); the acyclic order is proven by `model_rebuild()` completeness.
2. Public names are re-exported through `__init__.py`'s curated `__all__`; production callers
   import from the owning submodule, not the package initializer.
3. Shared evidence/control contracts are consumed by the control plane from `models` (legal:
   `serving` is above `models`), removing the backwards `conversation → harness_control` edges.
4. Schema/serialization equality against the S1.3 baseline is proven before any change lands.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `__init__.py` | export surface | Curated facade; no forwarding shim allowed. | covered |
| `primitives.py` | layer bottom | `WireModel` and token branding authority. | covered |
| `evidence.py` | shared contract | Evidence wire shapes consumed across control/conversation. | covered |
| `control_wire.py` | shared contract | Control state/submission/provenance vocabulary. | covered |
| `status.py` | state authority | Waiting/terminal evidence cross-products. | covered |
| `capabilities.py` | capability authority | Contract-only gating, no version demotion. | covered |

## Local Invariants And Traps

- Cursor/token brands, authorization, identity/scope, generations, revisions, and ordinals are
  authority boundaries, not decoration.
- `ready` cannot be derived from unknown evidence; `supported`/`partial` require exact
  runtime-fixture evidence (`enablesCapabilities=false` on fixture evidence itself).
- A model must validate its own emitted body: `exclude_none=True`-reached fields must be nullable
  AND defaulted; library-only nulls stay meaningful.
- No forwarding shim at `serving/conversation/models.py` or `_models_*`; no production import of
  `serving.harness_control_models`/`harness_control_client`/`terminal_catalog` from this route.
- Do not import from the package `__init__` in production code (R7).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The zero-drift baseline pins schemas, signatures, samples, and rebuild order. | `test_conversation_schemas_and_dataclass_fields_match_baseline` | mcp/tests/test_model_split_baseline.py:144-144 |
| Hostile contract tests pin the grammar products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |
| The canonical ports consume these models without owning behavior. | `ControlPlanePort` | mcp/src/agents_remember/serving/ports.py:189-269 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Docs References

No Domain Documentation source is configured; the repository-owned contract matrix and baseline
fixture are the evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Curated export surface. |
| `primitives.py` | [`primitives.py.md`](primitives.py.md) | covered | Layer bottom. |
| `identity.py` | [`identity.py.md`](identity.py.md) | covered | Identity/provenance products. |
| `cursors.py` | [`cursors.py.md`](cursors.py.md) | covered | Cursor families. |
| `content.py` | [`content.py.md`](content.py.md) | covered | Blocks/items/sub-agents. |
| `capabilities.py` | [`capabilities.py.md`](capabilities.py.md) | covered | Capability contract. |
| `status.py` | [`status.py.md`](status.py.md) | covered | Status vocabulary. |
| `stream_events.py` | [`stream_events.py.md`](stream_events.py.md) | covered | Stream grammar. |
| `history.py` | [`history.py.md`](history.py.md) | covered | Library/page grammar. |
| `opening.py` | [`opening.py.md`](opening.py.md) | covered | Open operation. |
| `interrupts.py` | [`interrupts.py.md`](interrupts.py.md) | covered | Interrupt operation. |
| `submissions.py` | [`submissions.py.md`](submissions.py.md) | covered | Queue/submit DTOs. |
| `withdrawals.py` | [`withdrawals.py.md`](withdrawals.py.md) | covered | Withdrawal DTOs. |
| `attachments.py` | [`attachments.py.md`](attachments.py.md) | covered | Attachment DTOs. |
| `telemetry.py` | [`telemetry.py.md`](telemetry.py.md) | covered | Telemetry products. |
| `evidence.py` | [`evidence.py.md`](evidence.py.md) | covered | Shared evidence wire. |
| `control_wire.py` | [`control_wire.py.md`](control_wire.py.md) | covered | Shared control wire. |

## Child Overviews

None.

## How To Use This Area

When changing a wire contract under this route:

1. Read this overview, then the owning module's sidecar.
2. Keep the acyclic import order; never import upward or from the package `__init__`.
3. Prove zero drift: update the baseline only when the wire contract intentionally changes.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created the route overview for the new
  `models/conversations/` package; supersedes the `serving/conversation` contract-model
  governance for the moved grammar. Verification metadata pinned until closeout stamps the L9
  code commit.
