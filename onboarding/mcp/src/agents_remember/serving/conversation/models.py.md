# mcp/src/agents_remember/serving/conversation/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Owns the stable, strict, native-authoritative wire grammar shared by active conversation reads,
dormant native history, operation/control projection, browser consumers, and orchestration. The
module represents truth and rejects contradictory authority products; it is not a projector,
history store, or control service.

## Code Commentary

### Logic

- `WireModel` makes public DTOs immutable, camel-case on the wire, and closed to unknown fields.
- Purpose-prefixed opaque types keep active-page, active-event, library-list, library-read,
  library-key, private native-resume, and SHA-256 operation identities non-interchangeable.
- Conversation items carry stable ids, monotonic revisions/global ordinals, typed content blocks,
  explicit lane/source/producer provenance, and unknown-vendor/input evidence.
- Status models fix the evidence-to-turn-state vocabulary and validate waiting and terminal
  cross-products; unknown evidence cannot establish ready.
- Capability models require exact evidence products. Since 260718-CHATS-L5F R4 (developer ruling
  2026-07-21) `FeatureCapability` carries a documenting NOTE (L653-L658) that there is deliberately
  NO `for_observed_runtime` version-demotion: the contract is the only gate, a capability is never
  demoted because an installed runtime/helper version drifts from a fixture's captured version, and
  the runtime/helper version survives on `CapabilityEvidence` as informational metadata only.
- Page/event models carry cursor continuity and explicit gap/repage semantics.
- Open, interrupt, queue, withdrawal, attachment, telemetry, and runtime-fixture DTOs validate the
  full semantic product rather than relying on callers to combine individually valid fields.
- `operation_fingerprint` hashes canonical immutable request identity plus authorization without
  retaining raw request content.

### Conventions

This is intentionally a declaration-heavy single contract owner. Use literal discriminators and
Pydantic validators for intrinsic cross-field authority. Add production behavior in focused service
modules behind these types, not in this file.

### Invariants And Boundaries

- Cursor/token brands, authorization, identity/scope, generations, revisions, and ordinals are
  authority boundaries, not decorative typing.
- Exact producer/lane/strength products are required for cockpit, durable bus, controlled-terminal,
  interaction, and control sources. Unknown input stays native-only/unknown and producer-free.
- Supported or partial capability states require runtime-fixture evidence and a fixture id;
  fixture evidence itself has `enablesCapabilities=false`.
- Open identity and catalog proof must agree exactly. No-launch results cannot carry identities;
  identity-bearing failures require phase-matching explicit rollback.
- Only queued cockpit work exposes withdrawal identity. Raw draft and attachment recovery exist
  only in the authoritative successful withdrawal response.
- Metrics always retain scope, freshness, precision, runtime, and evidence origin.

### Todos

If this declaration module grows with behavior, split that behavior behind a stable models facade;
do not fragment the accepted wire vocabulary prematurely.

## Docs References

No Domain Documentation source is configured. The repository-owned hostile contract matrix is the
authoritative behavioral evidence for this internal grammar.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Hostile tests cover cursor purpose, provenance, status, capability, identity/rollback, recovery, attachment, metrics, and fixture products. | L208-L1185 | [test_conversation_contracts.py](agents-remember/mcp/tests/test_conversation_contracts.py) |
| Foundation tests prove the types participate in exactly two ports and fixture non-promotion. | L21-L28; L102-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| The two read protocols consume these normalized models without owning control behavior. | L8-L87 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |

## Cross-Repo References

No cross-repository implementation governs these contracts.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: version-gate REMOVAL (developer ruling
  2026-07-21, R4). Corrected the now-false "demote mismatched runtime/helper versions" claim:
  `FeatureCapability.for_observed_runtime` is removed; a documenting NOTE (L653-L658) records the
  deliberate absence and the contract-only gate; the runtime/helper version is informational
  `CapabilityEvidence` metadata only. Uncommitted; closeout re-stamps verification.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the contract sidecar after same-reviewer
  PASS closed six authority findings. Verification is blank until closeout commits and stamps the
  new source.
