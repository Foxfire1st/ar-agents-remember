# mcp/src/agents_remember/models/conversations/__init__.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/models/conversations/__init__.py`    |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                   |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                |

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

The initializer re-exports every public name from the fifteen owning modules into one explicit
`__all__` (cit:([`__all__`], mcp/src/agents_remember/models/conversations/__init__.py:212-386)). The
owning modules keep the behavior; this file is exports only.

The module import layering is acyclic and declaration-order-validated: `primitives` → `identity`
→ `cursors` → `content`, `capabilities`, `status`, `submissions`, `withdrawals`, `opening`,
`interrupts`, `attachments`, `telemetry` → `stream_events`, `history`. Pydantic forward
references are closed by `model_rebuild()` in that order and pinned by
`test_model_split_baseline.py::test_model_rebuild_ordering_is_complete`
(cit:([`test_model_rebuild_ordering_is_complete`], mcp/tests/test_model_split_baseline.py:226-226)).

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
- Declaration bodies moved verbatim from the monolith (R4); the serialization/schema baseline
  fixture `mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json` pins zero drift.

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
  `terminal_catalog` (R8 — enforced by the armed layering rail and `test_removed_paths_receive_no_forwarding_shim`).

### Todos

If the export surface grows, keep it curated; behavior still belongs in the owning modules.

## Docs References

No Domain Documentation source is configured. The repository-owned hostile contract matrix and the
baseline fixture are the authoritative behavioral evidence for this internal grammar.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The curated export surface lists every public conversation-wire name. | `__all__` | mcp/src/agents_remember/models/conversations/__init__.py:212-386 |
| The zero-drift baseline proves schema/serialization equality and rebuild ordering for every moved model. | `test_conversation_schemas_and_dataclass_fields_match_baseline` | mcp/tests/test_model_split_baseline.py:144-144 |
| Removed monolith paths receive no forwarding shim. | `test_removed_paths_receive_no_forwarding_shim` | mcp/tests/test_model_split_baseline.py:239-239 |
| Hostile contract tests still pin cursor/provenance/status/capability products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |
| The canonical conversation read/control ports consume these models without owning behavior. | `ControlPlanePort` | mcp/src/agents_remember/serving/ports.py:189-269 |
| The response-contract declarations that make these models the routes' stated contract. | `WireResponse` | mcp/src/agents_remember/serving/response_contract.py:89-101 |

## Cross-Repo References

No cross-repository implementation governs these contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: replaced the `serving/conversation/models.py`
  sidecar (and the `_models_*` split cards) with this package-initializer card after the monolith
  moved into the responsibility-owned modules under `models/conversations/`. Preserved the
  contract grammar, invariant, and hostile-test knowledge from the deleted cards; citations
  re-anchored to the new module paths. Verification metadata pinned until closeout stamps the L9
  code commit.
