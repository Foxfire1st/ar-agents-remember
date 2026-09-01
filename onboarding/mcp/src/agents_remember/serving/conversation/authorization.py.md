# mcp/src/agents_remember/serving/conversation/authorization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/authorization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate |  2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

Defines the explicit authorization seam every `ConversationRuntime` binds (260718-CHATS-L0, leaf
ruling R4). The production resolver represents ONE local operator/workspace authority under the
local single-user posture: identity is resolved on the server from the OS and the canonical
workspace scope, never accepted from a browser-supplied principal or tenant field, and non-loopback
serving fails closed. The module does not claim that the identity is authenticated; any remote or
multi-user requirement invalidates this local ruling and requires a separately designed
authentication subsystem.

## Code Commentary

### Logic

`ConversationAuthorizationResolver` is the protocol: `resolve(client_host=...)` mints the
server-resolved operator binding for one request or fails closed by raising, and
`require(authorization)` verifies an externally supplied binding (cursor, operation, or scope)
against the resolver's exact identity — the cross-principal rejection contract. `resolve` has no
principal/tenant parameter, so a browser identity claim has no channel into resolution.

`LocalOperatorAuthorizationResolver.for_workspace` resolves the identity once at composition:
the principal is the kernel uid (`local-operator:<uid>`, with a `getpass` fallback on non-POSIX
platforms that itself raises `AuthorityError` rather than fabricating an identity), and the tenant
is the canonical `workspace_root.resolve()` path. Request-time `resolve` then only proves the
request arrived over loopback: `_is_loopback_peer` accepts only literal loopback IPs
(`127.0.0.0/8`, `::1`) via `ipaddress`, and hostnames, absent peers, and non-loopback addresses all
raise `AuthorityError`. `require` rejects any binding whose principal/tenant is not exactly the
server-resolved identity.

### Conventions

Identity resolution happens once at composition, not per request; the per-request check is only
peer classification. The resolver is a frozen dataclass holding one `AuthorizationBinding`, so the
identity is constant for the app's lifetime. Injected resolvers exist only as a test/application
seam (bound through `ConversationRuntime` construction) and must honor the same cross-principal
rejection contract.

### Invariants And Boundaries

- Browser-supplied principal/tenant claims are never read; resolution has no identity input
  channel (signature-pinned by contract tests).
- Non-loopback, non-literal-IP, or absent peers fail closed — never a silent mapping onto the
  local identity.
- Cursor, operation, and scope bindings are non-transferable between principals/tenants.
- This module does not authenticate; it binds one local posture. Do not add remote, multi-user,
  token, or header-based identity here — that invalidation requires a separate authentication
  design.
- HTTP status mapping of the raised `AuthorityError` is deliberately left to the child leaves that
  own behavior routes.

### Todos

None; L1/L2/L3 map `AuthorityError` to the serving status idiom at their own routes.

## Docs References

No Domain Documentation source is configured for this repository-local authorization ruling.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The resolver binds the strict `AuthorizationBinding` wire type from the conversation contract and
is driven per request by the narrow authorization dependency; the production composition constructs
it from the workspace root it already holds.

| Finding | Anchor | Source |
| --- | --- | --- |
| `AuthorizationBinding` is the strict principal/tenant wire type the resolver mints and verifies. | "class AuthorizationBinding(WireModel):" | mcp/src/agents_remember/models/conversations/identity.py:56-56 |
| The request dependency consults only the ASGI TCP peer and delegates to the bound resolver. | `resolve_conversation_authorization` | mcp/src/agents_remember/serving/conversation/dependencies.py:26-36 |
| The production composition binds `LocalOperatorAuthorizationResolver.for_workspace(workspace_root)` into the one runtime. | "LocalOperatorAuthorizationResolver.for_workspace(config.workspace_root)" | mcp/src/agents_remember/serving/app.py:299-299 |
| `AuthorityError` is the typed refusal raised for non-loopback peers and cross-principal bindings. | `AuthorityError` | mcp/src/agents_remember/errors.py:68-74 |
| Contract tests prove local-operator identity, loopback resolution, non-loopback/unknown fail-closed, the signature-pinned no-identity-channel, ignored browser claims, cross-principal cursor/scope/operation rejection, and injected-resolver separation in both directions. | `test_server_resolves_one_local_operator_workspace_identity`; `test_loopback_peers_resolve`; `test_non_loopback_peers_fail_closed`; `test_unknown_peer_fails_closed`; `test_server_resolves_one_local_operator_workspace_identity`; `test_browser_identity_claims_are_never_read`; `test_cross_principal_cursor_binding_rejected`; `test_cross_principal_scope_binding_rejected`; `test_cross_principal_operations_have_distinct_fingerprints`; `test_injected_resolver_proves_cross_principal_rejection` | mcp/tests/test_conversation_authorization.py:117-126; mcp/tests/test_conversation_authorization.py:129-134; mcp/tests/test_conversation_authorization.py:137-152; mcp/tests/test_conversation_authorization.py:155-158; mcp/tests/test_conversation_authorization.py:168-189; mcp/tests/test_conversation_authorization.py:217-235; mcp/tests/test_conversation_authorization.py:238-255; mcp/tests/test_conversation_authorization.py:258-267; mcp/tests/test_conversation_authorization.py:270-290 |

## Cross-Repo References

No cross-repository boundary participates in this server-local identity ruling.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: created the local-operator authorization
  sidecar for the server-resolved single-user ruling. Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
