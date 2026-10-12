# models/conversations/ — Responsibility-Owned Conversation Wire Models Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/conversations/` |
| onboardingRoute | `mcp/src/agents_remember/models/conversations/overview.md` |
| parentOverview | [`models/overview.md`](../overview.md) |

## What This Area Is

This package owns the conversation wire grammar for active reads, dormant native history, operation/control projections and their consumers. It also owns the evidence and control-wire contracts shared with the harness control plane. These are type, validation and serialization authorities; conversation serving behavior and control execution belong to their services.

## Hot Path Summary

Start with `__init__.py` for the curated `__all__` export surface and `primitives.py` for `WireModel` and opaque tokens. `evidence.py` and `control_wire.py` own shared harness-control contracts. `status.py` and `capabilities.py` validate status and capability evidence; `content.py` owns `ConversationItem` and the sub-agent grammar. Follow `history.py` for page/library products and `stream_events.py` for SSE mutations and envelopes.

## Construction And Ownership

The Pydantic products inherit an immutable, camel-case `WireModel` configuration that forbids unknown fields. Opaque tokens instead use purpose-branded root models. The shared evidence and control-wire products include frozen dataclasses and explicit serializers, so the package is not uniformly composed of Pydantic models.

Within the Pydantic model graph, primitives support identity, identity and primitives support cursor bindings, and domain products build on these contracts. History and stream models compose content, status and cursor products. The shared control-wire module imports the evidence serialization-size helper; evidence is a separate shared-contract foundation. `__init__.py` gathers public names into a curated export surface.

The canonical serving ports import the owning submodules and declare read/control interfaces using their products. The harness control client and its control-plane-only models also import shared contracts from this package. These imports keep shared wire declarations below their serving consumers; the ports do not implement control behavior.

### What Belongs Here

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

### Structures Found Here

- Purpose-branded active page/event, library list/read/key, native resume and operation-fingerprint tokens.
- Typed content blocks and first-class sub-agent products: `ConversationAgentRef`, per-item `agent`, library agent rows and `agents_note`.
- Status, capability, operation and telemetry products with field constraints and coherence validators.
- Shared evidence frames/pages/truncation and control-wire state/submission/provenance families.

### Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `__init__.py` | export surface | Curated facade; no forwarding shim allowed. | covered |
| `primitives.py` | layer bottom | `WireModel` and token branding authority. | covered |
| `evidence.py` | shared contract | Evidence wire shapes consumed across control/conversation. | covered |
| `control_wire.py` | shared contract | Control state/submission/provenance vocabulary. | covered |
| `status.py` | state authority | Waiting/terminal evidence cross-products. | covered |
| `capabilities.py` | capability authority | Contract-only gating, no version demotion. | covered |

## Invariants And Boundaries

Cursor/token brands, authorization, identity/scope, generations, revisions and ordinals carry distinct contracts. Token classes validate their purpose prefixes; bindings carry authorization and generation information. Token signing, persistence and authorization decisions are not implemented by the token declarations.

`ConversationStatus` rejects `ready` when evidence strength is `unknown`. Turn validators require waiting/interaction evidence and terminal outcomes to agree with the turn state. `FeatureCapability` requires runtime-fixture evidence with a fixture ID for `supported` or `partial`; it does not compare runtime/helper versions to demote a capability. Separately, `RuntimeFixtureEvidence` fixes `enablesCapabilities` to false. These predicates do not establish an exact fixture/version match between the two products.

Fields whose null value may be omitted by active/control serialization need defaults that permit the emitted body to be read again. The active page window, event predecessor and status fields encode this with nullable defaults. Library `next_cursor` and historical `older_cursor` remain required nullable fields, preserving their explicit null contract.

Operation validators own coherence within their wire products. Withdrawal projections constrain phase/outcome/recovery combinations and recovery expiry; they do not perform withdrawal execution. Submission queue rows expose withdrawal identity only for queued cockpit operations. Content validators preserve the declared input lane/producer/provenance authority.

Keep imports directed toward the owning model submodules rather than the package initializer. This route contains no imports of `serving.harness_control_models`, `harness_control_client` or `terminal_catalog`. Preserve that boundary and do not recreate forwarding shims at the former `serving/conversation/models.py` or `_models_*` paths.

### What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Serving behavior, projectors, stores, control services | `serving/conversation/` and `serving/projections/` |
| Response envelopes/tool payload models | `models/` siblings (`base.py`, `tool_registry.py`, …) |
| Control-plane-only records | `serving/harness_control_models.py` (until L11) |

## How To Use This Area

When changing a wire contract, read this overview and the owning module's sidecar. Keep model imports acyclic and directed toward their owners. Check the intended validation and serialization behavior without recreating an implementation-shape snapshot. This overview does not promise enforcement by the absent `test_conversation_model_architecture.py` suite or report test execution.

## Onboarding Metadata

The coverage labels below and in the load-bearing-file table are preserved onboarding metadata, not operative validation or lifecycle promises. Current lifecycle or acceptance status is not established by the source owners examined here. The inherited "until L11" qualifier is retained metadata, not a current milestone promise.

### File-Level Onboarding Map

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

### Child Overviews

None.

## Evidence

- Current withdrawal models own phase/outcome/recovery consistency. [1] [2]
- The canonical ports consume these models without owning behavior. [3]
