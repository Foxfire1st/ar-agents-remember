# mcp/src/agents_remember/models/conversations/identity.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/models/conversations/identity.py`    |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-09-16T13:26+02:00                                       |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f`                   |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
| governingOverview      | `overview.md`                                                |

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

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The harness union every conversation identity is typed against, widened by this change set so eve's projector could be registered. | `HarnessId` | mcp/src/agents_remember/models/conversations/identity.py:10-10 |
| The native and active conversation identities, and the authorization/evidence products. | `NativeConversationRef`; `ActiveConversationRef`; `AuthorizationBinding`; `ConversationLibraryScope`; `ProvenanceEvidence` | mcp/src/agents_remember/models/conversations/identity.py:44-48; mcp/src/agents_remember/models/conversations/identity.py:51-53; mcp/src/agents_remember/models/conversations/identity.py:56-58; mcp/src/agents_remember/models/conversations/identity.py:61-65; mcp/src/agents_remember/models/conversations/identity.py:68-74 |
| Authorization identity is a declared shared wire model; deleted hostile-test fixtures are not current proof. | `AuthorizationBinding` | mcp/src/agents_remember/models/conversations/identity.py:56-58 |
| The dashboard mirror of this union, which must be kept in step by hand. | `HarnessId` | dashboard/src/data/conversation/types.ts:13-13 |
| The projector protocol that types `harness_id` with this union, so a new member is required before a projector for it can register. | `_EveProjector`; `PROJECTORS` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:115-125; mcp/src/agents_remember/serving/conversation/projectors/__init__.py:128-133 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: `HarnessId` gained `"eve"`. The union is what the
  conversation projector protocol types `harness_id` with, so the eve projector could not be registered
  without it — this one-line widening is the *enabling* change for eve's observability, and it is the
  only reason a native session backend appears in the wire identity union. Body updated on Logic; the
  five inline `cit:(…)` prose citations in the Purpose section were converted to prose plus reference
  rows in the required `Finding | Anchor | Source` shape. Verification metadata moves to the leaf's
  synced base `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout stamps
  the real code commit and no hash or fingerprint was invented here.
- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the identity layer moved from
  `serving/conversation/_models_wire.py`. Verification metadata pinned until closeout stamps the
  L9 code commit.
