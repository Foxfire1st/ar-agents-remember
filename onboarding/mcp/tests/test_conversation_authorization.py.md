# mcp/tests/test_conversation_authorization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_authorization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Authorization contract suite for the server-resolved local single-user operator ruling
(260718-CHATS-L0, leaf R4/R5). It proves the production resolver mints exactly one OS-resolved
local operator/workspace identity, resolves only for loopback peers, fails closed for
non-loopback, unknown, or hostname peers, exposes no principal/tenant input channel, never reads
browser identity claims, and rejects cross-principal cursor, scope, and operation bindings —
including through an injected resolver seam in both directions.

## Code Commentary

### Logic

Identity cases pin the `local-operator:<uid>` principal (kernel uid, with the `getpass` fallback
branch tolerated off-POSIX) and the canonical resolved workspace root as tenant, constant for the
resolver's lifetime. Parametrized peer cases accept `127.x` and `::1` loopback forms and fail
closed with `AuthorityError` for private/remote IPv4, remote v4-mapped IPv6, `testclient`,
`localhost`, and `None`. Signature pins prove `resolve` takes only `self` and a keyword-only
`client_host` on both the protocol and the production resolver. A forged-headers case installs the
runtime on a real app and proves `x-principal-id`, `x-tenant-id`, `x-forwarded-for`, and
`authorization` headers are never read. Cross-principal cases build own and foreign
`ActiveCursorBinding`, `ConversationLibraryScope`, and `operation_fingerprint` values and prove
`require` rejects the foreign binding while accepting the resolver's own. The `_InjectedResolver`
seam double drives the request dependency with a foreign identity and proves cross-principal
rejection holds in both directions between production and injected resolvers.

### Conventions

Plain `pytest` functions over `tmp_path`, hand-built ASGI `Request` scopes (with raw header lists
for the forgery case), and strict wire models from the conversation contract as binding carriers.
The injected seam double deliberately skips loopback enforcement, which the docstring flags as
test-only; production enforcement stays in `LocalOperatorAuthorizationResolver`.

### Invariants And Boundaries

- Identity is server-resolved from the OS and canonical scope; the wire has no identity channel.
- Non-loopback, non-literal-IP, hostname, and absent peers always fail closed.
- Cursor, scope, and operation bindings are non-transferable between principals/tenants.
- Injected resolvers are a test/application seam only and must honor cross-principal rejection.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation source is configured. The repository authorization sources are direct
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The production resolver, loopback classification, and OS-resolved principal under test. | "class LocalOperatorAuthorizationResolver" | mcp/src/agents_remember/serving/conversation/authorization.py:72-72 |
| The request dependency that forwards only the ASGI TCP peer. | "def resolve_conversation_authorization" | mcp/src/agents_remember/serving/conversation/dependencies.py:28-28 |
| The strict binding, cursor, scope, and fingerprint carriers used as own/foreign evidence. |"class ConversationEventEnvelope"|mcp/src/agents_remember/models/conversations/stream_events.py:88-88|
| The typed `AuthorityError` refusal asserted across the suite. | `AuthorityError` | mcp/src/agents_remember/errors.py:17-23 |

## Cross-Repo References

No neighboring repository participates in this authorization suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: created the authorization contract suite
  sidecar. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
