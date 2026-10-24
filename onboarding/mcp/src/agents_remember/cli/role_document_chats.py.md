# mcp/src/agents_remember/cli/role_document_chats.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The selected-document read is the correcting authority for a document’s launch-record chats. It checks each recorded native agent’s existence/archive state; the separate tree read preloads the same receipt-derived discovery before a selection click.

## Code Commentary

A clicked hosted target promotes that pending agent in the shared active warmup pass before the pane is drawn. Already in-flight work retains its slot; the route still discovers only canonical recorded chats through read-only host evidence.


`/api/role-launch/document-chats` keeps exact-request admission, primary roles and bounded pages of three per-agent reads. Missing receipts and well-shaped records without hosted agent/workspace identity yield no chat; unreadable or malformed receipt/projection data refuses with HTTP 409, never an empty discovery result. The shared projection retains role, stored selection, creation time and execution kind/IDs. Tree discovery uses a separate read-only live-ID census, not the host’s whole hierarchy or unrecorded agents.

## Evidence




## Investigator scope and request identity

An exact task-bound Investigator request is read only when explicitly selected with its UUID. Ordinary master/sprint enumeration continues to return the primary Manager/Orchestrator, so an Investigator result or frame steering never replaces the document’s coordinator. The earlier role name is normalized by the shared response decorator with its required notice.




## Refreshed current evidence


## Current contract evidence

- The route resolves the admitted context and serves the read endpoint.  Anchor: `register_document_chat_route` [1]
- Record selection follows the admitted roles and refuses a foreign document or request receipt.  Anchor: `_records` [2]
- The launched request's agent is projected with its document labels. [3]
- Host reads are bounded and paged, existence is verified, and an unreachable host is distinct from an empty answer. [4]
- The current source implements this file’s stated Investigator boundary. [5]
- The selected-document read is the correcting authority for a document’s launch-record chats. It checks each recorded native agent’s existence/archive state; the separate tree read preloads the same receipt-derived discovery before a selection click. [6]

## Role blocks and the pages that follow them

Records are grouped one block per role, newest first, and `_role_records` reads a taskless role through its own receipts. `_PAGE_SIZE` bounds the host reads of one page at three, not the records it may step over: a page that already answered a role steps past that role's older records without asking the host again, and `nextOffset` continues from the record the walk stopped on. A document-free selection lists the architect and the free agent, and a selection that names the free agent lists that role alone, so a bootstrap seat behind architect records is reached instead of being answered with the architect's seat.

- The paged walk over role blocks, with one host read bound per page. [7]
- The end of a role's block, which a continuation resumes after. [8]
- A bootstrap seat behind architect records is reached across pages, and naming the free agent answers with its own seat. [9]
