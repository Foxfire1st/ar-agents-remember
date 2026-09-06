# mcp/src/agents_remember/models/conversations/identity.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/models/conversations/identity.py`    |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                   |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/identity.py` (260731-EFA-L9) owns the native/active conversation identity,
role/source/producer provenance, capability state, and authorization/scope products of the
conversation wire grammar.

## Code Commentary

### Logic

`NativeConversationRef` (cit:(["class NativeConversationRef"], mcp/src/agents_remember/models/conversations/identity.py:44-44)) is the native identity;
`ActiveConversationRef` (cit:(["class ActiveConversationRef"], mcp/src/agents_remember/models/conversations/identity.py:51-51)) the AR-session-bound active identity;
`AuthorizationBinding` (cit:(["class AuthorizationBinding"], mcp/src/agents_remember/models/conversations/identity.py:56-56)), `ConversationLibraryScope`
(cit:(["class ConversationLibraryScope"], mcp/src/agents_remember/models/conversations/identity.py:61-61)), and `ProvenanceEvidence`
(cit:(["class ProvenanceEvidence"], mcp/src/agents_remember/models/conversations/identity.py:68-68)) fix the authorization and evidence products.

### Conventions

- Identity is evidence-bound: unresolved sub-agent identity renders as `agent <short-id>`, never
  fabricated.

### Invariants And Boundaries

- Open identity and catalog proof must agree exactly; no-launch outcomes carry no identities,
  and identity-bearing failures require phase-matching explicit rollback.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Authorization identity is a declared shared wire model; deleted hostile-test fixtures are not current proof. | `AuthorizationBinding` | mcp/src/agents_remember/models/conversations/identity.py:56-58 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the identity layer moved from
  `serving/conversation/_models_wire.py`. Verification metadata pinned until closeout stamps the
  L9 code commit.
