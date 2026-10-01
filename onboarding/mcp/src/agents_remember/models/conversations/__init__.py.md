# mcp/src/agents_remember/models/conversations/__init__.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/__init__.py` is the curated export surface for the responsibility-owned
conversation wire-model package created by 260731-EFA-L9 (R1/R6). It replaced
`serving/conversation/models.py` and its five `_models_*` split files; the old paths receive no
forwarding shim. The package owns the stable, strict, native-authoritative wire grammar shared by
active conversation reads, dormant native history, operation/control projection, browser
consumers, and orchestration — plus the shared evidence and control-wire contracts the harness
control plane also consumes (R2/R8).

## Code Commentary

### Logic

The initializer re-exports every public domain name from the fifteen owning modules into one
explicit `__all__` (cit:([`__all__`], mcp/src/agents_remember/models/conversations/__init__.py:211-384)).
The owning modules keep the behavior; this file is exports only. Generic type parameters are
lexically owned by their declarations and are not package-level domain exports.

The module import layering is acyclic and declaration-order-validated: `primitives` → `identity`
→ `cursors` → `content`, `capabilities`, `status`, `submissions`, `withdrawals`, `opening`,
`interrupts`, `attachments`, `telemetry` → `stream_events`, `history`. Pydantic forward
references are closed by `model_rebuild()` in that order. The stable post-migration requirement is
checked by `test_conversation_models_have_resolved_forward_references`; the former task/date
shape snapshot is deleted.

Key domain modules (each with its own sidecar in this route): `primitives.py` defines `WireModel`
and the opaque purpose-branded token root; `identity.py` the conversation/authorization identity
and provenance products; `cursors.py` the non-interchangeable cursor/key families; `content.py`
the typed blocks and `ConversationItem`; `capabilities.py` the fixture-evidence-bound capability
contract; `status.py` the evidence-to-turn-state vocabulary; `stream_events.py` and `history.py`
the page/event grammar; `opening.py`, `interrupts.py`, `submissions.py`, `withdrawals.py`,
`attachments.py` the operation DTOs; `telemetry.py` the metric/evidence products and
`operation_fingerprint`; `evidence.py` and `control_wire.py` the shared harness-control wire
contracts (R2).

### Conventions

- Exports only: contract behavior lives in the concrete modules, never in this initializer.
- Curated `__all__` with no `import *` (R6); production imports target the owning submodules, not
  this package initializer (R7 — the census found zero production package-`__init__` imports).
- Declaration bodies moved from the monolith (R4); current serialization/schema behavior is owned
  by focused contract suites rather than a permanent migration snapshot.

### Invariants And Boundaries

- Strict immutable camel-case `WireModel` contracts with unknown fields forbidden; cursor/token
  brands, authorization, identity/scope, generations, revisions, and ordinals are authority
  boundaries, not decoration.
- Exact producer/lane/strength evidence is required for cockpit, durable bus, controlled-terminal,
  interaction, and control sources; unknown input stays native-only/unknown and producer-free.
- A model must be able to validate its own emitted body: anything a route dumps with
  `exclude_none=True` must be nullable AND defaulted (the L4 six-field rule).
- No forwarding shim may reappear at `serving/conversation/models.py` or `_models_*`; no module
  may import these names from `serving.harness_control_models`/`harness_control_client`/
  `terminal_catalog` (R8 — enforced by the armed layering rail and
  `test_removed_conversation_model_modules_have_no_compatibility_shims`).

### Todos

If the export surface grows, keep it curated; behavior still belongs in the owning modules.

## Evidence

### Docs References

No Domain Documentation source is configured. Repository-owned hostile contract and stable
architecture tests are the authoritative evidence for this internal grammar.

No configured domain documentation was available.

### Repo-Internal References

- The curated export surface lists every public conversation-wire name. [1]
- The canonical conversation read/control ports consume these models without owning behavior. [2]
- The response-contract declarations that make these models the routes' stated contract. [3]

### Cross-Repo References

No cross-repository implementation governs these contracts.

No meaningful cross-repo references found.
