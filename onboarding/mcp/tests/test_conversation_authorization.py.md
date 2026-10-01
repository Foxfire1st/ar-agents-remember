# mcp/tests/test_conversation_authorization.py

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

## Evidence

### Docs References

No Domain Documentation source is configured. The repository authorization sources are direct
evidence.

No configured domain documentation was available.

### Repo-Internal References

- The production resolver, loopback classification, and OS-resolved principal under test. [1]
- The request dependency that forwards only the ASGI TCP peer. [2]
- The strict binding, cursor, scope, and fingerprint carriers used as own/foreign evidence. [3]
- The typed `AuthorityError` refusal asserted across the suite. [4]

### Cross-Repo References

No neighboring repository participates in this authorization suite.

No meaningful cross-repo references found.
