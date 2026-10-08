# mcp/src/agents_remember/models/role_identity.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One exact read alias for the canonical Investigator identity.

## Code Commentary

canonical_role maps only system-specialist to investigator. role_spellings enumerates the canonical name and that one earlier spelling for existing read addresses. Every other value remains itself. ROLE_ALIAS_NOTICE is the single public notice. Normalization is input/read identity handling, not a migration, second role implementation or runtime authorization.

## Evidence

- The source owns the documented investigation, identity or request boundary. [1]
