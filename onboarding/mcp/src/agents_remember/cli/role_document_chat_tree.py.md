# mcp/src/agents_remember/cli/role_document_chat_tree.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

`POST /api/role-launch/document-chats/tree` answers one row per admitted tree selection in request order from canonical primary-role receipts and one `agents-live` host census. It is pre-click discovery only; the single-document read remains the correcting authority.

## Code Commentary

A request accepts at most 256 selections, reads each distinct receipt path once, retains its chat projection and releases all readings at request end. Accepted records are bounded by 1 MiB each and a 16 MiB request budget, consumed in selection order; a bounded read allows one sentinel byte to detect growth. No cross-request receipt or host-result cache is created.

`agents: null` means unknown: documentless/Projects scope, unreadable/non-regular/damaged/foreign receipt, exceeded receipt budget, or a recorded agent absent from an incomplete listing. Missing role receipts or absence from a complete census can yield `agents: []`; listed live IDs remain usable even on an incomplete census. Corruption affects only its document, whereas unreachable/unreadable host census returns request-level `unavailable` with its reason and no per-selection rows.

## Evidence

- Preclick discovery preserves unknown rather than claiming absence from incomplete host evidence. [1]
- Receipt reads are once per path and request-local with bounded bytes and retained projection only. [2]
