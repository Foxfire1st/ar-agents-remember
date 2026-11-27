# mcp/src/agents_remember/cli/developer_messages.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Implements dashboard developer-channel composition, file-first sending and sent-log HTTP routes.

## Code Commentary

### Logic

Validates a bounded body and typed picks; resolves all written reference forms/provenance before filing; composes the developer first line, free text and numbered picks; files complete text/hashed attachments before native delivery and logs truthful per-target identity/outcome.

### Invariants And Boundaries

It sends to an existing actual AR recipient and creates no role/binding/public MCP tool. Sending needs only the recipient's address and non-empty text or picks: optional `request.repository` is non-blocking page context only, never refuses as `unknown-repository`, and filing routes solely from the recipient's own task record or unified `taskless/<agent_id>/`. Body, image and message limits are server guards independent of browser preference accounting.

## Evidence

- Implements dashboard developer-channel request contract with optional non-blocking repository context. [1]
- Implements dashboard developer-channel composition, file-first sending (taskful or unified taskless without unknown-repository refusal) and sent-log HTTP routes. [2]
- Validates message bounds, decoded images, references and provenance without refusing an unconfigured request repository. [3]
