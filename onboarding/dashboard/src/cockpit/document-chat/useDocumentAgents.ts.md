# dashboard/src/cockpit/document-chat/useDocumentAgents.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Reads one document's agents from the launch-record route and distinguishes an unreadable host from an empty answer.

## Code Commentary

The hook posts the exact selection (with the launched request id when one is known) to `/api/role-launch/document-chats`, follows `nextOffset` pages until the answer is complete, and re-reads every five seconds while the panel is active. An unavailable response or a transport failure becomes an `AgentAnswer` with `agents: null` and a reason, which the panel renders as the shared unavailable notice with Retry; only a readable answer with an empty list is the "no agent matches" case that offers the bound launcher.

## Evidence

- The reader posts the exact selection, pages through offsets and retries while active. [1]
- An unreadable source is distinct from an empty agent list and carries its reason for Retry. [2]
