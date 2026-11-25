# mcp/src/agents_remember/application/knowledge_writer/typed_state.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Defines the knowledge handoff's refusal for product-owned revision state.

## Code Commentary

The handoff reader rejects proposed, accepted, reviewed and consolidated when typed into a status field. The refusal identifies the product as the state owner and directs the writer to omit the field except for retirement or a decision's own lifecycle.

## Relationships

Handoff parsing calls the shared check for invariant entry status and record field status. Existing stored records keep their own conversion rules.

## Evidence

- The refusal names the four reserved inputs and gives the admitted status uses. [1]
