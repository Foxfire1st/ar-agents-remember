# mcp/src/agents_remember/kernel/primitives/named_choices.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Match a configured choice against a supplied catalog without inventing aliases.

## Code Commentary

### Logic

`named` first searches IDs and then labels, comparing with casefold. It returns the first matching host row, preserving the row’s actual ID, or None. It does not maintain a catalog or map fast to priority independently of the supplied rows.

## Repo-Internal References

- Matching tests IDs before labels without case and returns the offered row. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
