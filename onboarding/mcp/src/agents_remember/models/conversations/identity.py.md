# mcp/src/agents_remember/models/conversations/identity.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/identity.py` (260731-EFA-L9) owns the native/active conversation identity,
role/source/producer provenance, capability state, and authorization/scope products of the
conversation wire grammar.

## Code Commentary

### Logic

`HarnessId` (line 10) is the harness union every conversation identity is typed against. It is
`Literal["codex", "claude", "pi", "eve"]`: **`eve` joined it with the eve product-integration change
set**, and this one-line widening is the *enabling* change for eve's observability — the conversation
projector protocol types `harness_id` with this union, so the eve projector could not be registered
without it.

`NativeConversationRef` (line 44) is the native identity; `ActiveConversationRef` (line 51) the
AR-session-bound active identity; `AuthorizationBinding` (line 56), `ConversationLibraryScope`
(line 61), and `ProvenanceEvidence` (line 68) fix the authorization and evidence products.

### Conventions

- Identity is evidence-bound: unresolved sub-agent identity renders as `agent <short-id>`, never
  fabricated.

### Invariants And Boundaries

- Open identity and catalog proof must agree exactly; no-launch outcomes carry no identities,
  and identity-bearing failures require phase-matching explicit rollback.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The harness union every conversation identity is typed against, widened by this change set so eve's projector could be registered. [1]
- The native and active conversation identities, and the authorization/evidence products. [2]
- Authorization identity is a declared shared wire model; deleted hostile-test fixtures are not current proof. [3]
- The dashboard mirror of this union, which must be kept in step by hand. [4]
- The projector protocol that types `harness_id` with this union, so a new member is required before a projector for it can register. [5]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
