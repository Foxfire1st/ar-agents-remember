# mcp/src/agents_remember/controlplane/signal_routing.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/signal_routing.py`           |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-08T14:25+02:00                                             |
| lastVerifiedCommitHash | `45708bbddf1ddb8a2045faa9fad88fe72603b674`|
| lastVerifiedCommitDate | 2026-07-08T05:51:44+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R4 (260707-HFX2-L1): derive a signal's routed owner address from catalog spawn provenance — one
hop up the spawn edge (worker -> its manager, manager -> its orchestrator), never further (a
developer ruling: no layer is addressed its grandchildren's noise).

## Code Commentary

### Logic

`_OWNER_ROLE_BY_SENDER_SPAWN_ROLE` maps the SENDER's own spawned-as role to its owner's role:
`worker -> manager`, `manager -> orchestrator`. Any other spawn role (orchestrator, strategist,
reviewer, designer, ...) has no entry, so `derive_signal_owner` returns an empty `RoutedOwner()` —
"no route derived, keep the caller's explicit `recipient_role`" — this module never fabricates an
address.

`derive_signal_owner(catalog, sender_agent_id=, message_kind=)`: a `message_kind ==
"decision-item"` always routes to the reserved `architect` role regardless of provenance (the
routing TARGET is reserved here; the decision-item QUEUE itself is a different leaf's job, AQR
Q3). Otherwise it looks up `sender_agent_id` in the catalog and reads the address straight off the
SENDER's own row: `spawned_by_session` / `spawned_by_lifecycle`
(`serving/terminal_catalog.py:48-59`) — no second catalog lookup is needed to resolve "the
manager's own session id" because that field IS it.

`RoutedOwner` is a frozen dataclass, not a Pydantic model — this module is pure derivation logic
with no wire/persistence concern of its own; the caller (`mcp/tools/operator_inbox.py::
operator_inbox_post_payload`) stamps the result onto the durable `OperatorInboxEntry`'s
`ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields at post time.

### Conventions

Every "no route" case returns the same empty `RoutedOwner()` sentinel (all fields `None`) rather
than raising — routing derivation is best-effort surfacing, never a hard requirement a caller must
satisfy before posting.

### Invariants And Boundaries

- One hop only: a worker's signal never chases the chain past its manager to the orchestrator,
  even though the manager's OWN `spawned_by_session` is the orchestrator — routing reads only the
  SENDER's provenance, never recurses.
- Pure and catalog-read-only: never mutates the catalog, never posts an inbox entry itself.
- `decision-item` routing to `architect` is unconditional — it does not consult the catalog at all.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf); the "no layer is
addressed its grandchildren's noise" rule is a developer ruling recorded in the leaf spec, not an
existing design doc.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The owner address is read straight off the sender's own `spawned_by_session`/`spawned_by_lifecycle` catalog fields. | L48-L59 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T14:25+02:00 — 260707-HFX2-L1: created for R4 hierarchical routing derivation (worker
  -> manager, manager -> orchestrator, decision-item -> architect). Verification metadata pinned
  until closeout stamps the 260707-HFX2-L1 commit.
