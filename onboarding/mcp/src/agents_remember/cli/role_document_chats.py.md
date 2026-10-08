# mcp/src/agents_remember/cli/role_document_chats.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The document chat's one read: from the selection, it projects the matching launch records and asks the host whether each recorded agent still exists.

## Code Commentary

`register_document_chat_route` mounts `/api/role-launch/document-chats`; `_records` selects the roles a selection admits (leaf → Worker/Reviewer/Curator, master → Manager, sprint → Orchestrator, nothing → taskless records), reads the exact receipt when a request id is given, and refuses a receipt that belongs to another document or request. `document_chats` walks records in bounded pages of three host reads, skips records that are not native agents, and asks the read-only host operation for existence and archive state; an unreachable host is returned as `unavailable` with its reason, never as an empty list. This launch-record source is the panel's single discovery source; it deliberately excludes native agents this product never started, and the host's whole hierarchy snapshot is not read by the dashboard.

## Evidence



- The launched request's agent is projected with its document labels. [3]
- Host reads are bounded and paged, existence is verified, and an unreachable host is distinct from an empty answer. [4]

## Investigator scope and request identity

An exact task-bound Investigator request is read only when explicitly selected with its UUID. Ordinary master/sprint enumeration continues to return the primary Manager/Orchestrator, so an Investigator result or frame steering never replaces the document’s coordinator. The earlier role name is normalized by the shared response decorator with its required notice.


- The current source implements this file’s stated Investigator boundary. [5]


## Refreshed current evidence

- The route resolves the admitted context and serves the read endpoint. [1]
- Record selection follows the admitted roles and refuses a foreign document or request receipt. [2]
