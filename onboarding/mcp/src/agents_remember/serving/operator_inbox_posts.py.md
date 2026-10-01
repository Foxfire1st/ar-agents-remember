# mcp/src/agents_remember/serving/operator_inbox_posts.py

## Governing Overview

[overview](overview.md)

## Purpose

Creates, persists, optionally delivers, and reports one whole operator-inbox post. Owner-addressed
traffic is re-resolved through the current structural seat before persistence.

## Code Commentary

### Logic

The post path derives task-document/role ownership from the sender and topology, rebinds only proven
owner addresses, stamps stable subject/routing plus private correlations, appends before delivery,
then records adapter outcome. Arbitrary peer addresses are not hijacked by owner derivation.
Dispatch briefs remain exact-pinned.
When a structural caller already supplies a complete document-and-role address with no runtime
coordinates, `_post_address` preserves it verbatim instead of densifying the durable envelope with
the current occupant id. Private delivery correlation remains separate.
`_persist_post` names `store.append` as the durable commit point. Compaction and expectation
publication follow that boundary, so a later exception is post-commit evidence that the structural
dispatch caller must reconcile rather than permission to retire the recipient.

### Conventions

Task topology and catalog are injected collaborators. A returned entry id is plane correlation and
never required for ordinary agent replies.

### Invariants And Boundaries

- Persistence precedes any delivery attempt.
- Post-time and delivery-time resolution both honor occupant replacement.
- Decision items require a current sprint owner.
- One post contains the complete ask/response boundary.
- A complete structural address is not rewritten into a dead-session-id address at post time.
- Append is the durable commit point; failures from later maintenance or delivery do not prove the
  brief absent.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Post-time owner rebinding preserves a complete canonical structural address. [1]
- Append is the durable commit point before compaction and expectation publication. [2]
- The shared post path derives, stamps, persists, and delivers the row. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260918-TSIP-L4 — The Refusal Payload And The Success `status` (`T15`)

Two edits in `post_operator_inbox_entry`, both to satisfy the response contract this leaf
extended.

**The decision-item refusal now returns a typed envelope** (**`:304-314`**): beside
`ok=False`/`operation`/`status="sprint-owner-required"` it adds `messageKind` (the one
queued-projection field already known at that point) and a `detail` sentence naming why nothing was
queued. The refusal fires **before the first write**, so it carries no entry identity and invents
none.

**The success path now sets `status="queued"`** (**`:358`**), because
`OperatorInboxPostResponse.status` is required and names which of the two outcomes the response
is. Net `+9/-1`; the file runs **382 lines** and every line at or below the old `:304` moved
(`+3` from `:304`, `+8` from `:308`, `+9` from `:350`).

The registered tool's response model is unchanged in name — it is the same
`OperatorInboxPostResponse`, now with a refusal half. Pinned by
`mcp/tests/test_tool_response_conformance.py::test_operator_inbox_post_sprint_owner_refusal_is_a_typed_payload`,
which drives the real tool over a real catalog and asserts
`produced["status"] == "sprint-owner-required"`.
