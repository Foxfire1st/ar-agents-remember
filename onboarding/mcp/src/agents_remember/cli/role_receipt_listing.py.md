# mcp/src/agents_remember/cli/role_receipt_listing.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Existing taskless receipt enumeration with exact address validation.

## Code Commentary

The taskless owner rejects an unsafe or non-directory store, invalid request UUID, mismatched filename, role or selection. Every admitted record is sorted by creation time and request UUID, newest first. It delegates receipt parsing to the existing receipt owner and adds no task-bound Investigator capacity or newest-fifty policy; those belong to investigator_receipts.

## Evidence

- The source owns the documented investigation, identity or request boundary. [1]
