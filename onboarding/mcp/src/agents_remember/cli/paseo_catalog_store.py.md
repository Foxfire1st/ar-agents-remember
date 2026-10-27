# mcp/src/agents_remember/cli/paseo_catalog_store.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Stores successful Paseo catalog answers per part across process restarts.

## Code Commentary

### Logic

`catalog_store_path` names launcher-catalog.json under the runtime home’s agents-remember directory. `CatalogParts.observe` records only successful answers with their read time, retaining the saved answer for an unanswered part and distinguishing fresh, saved and unknown origins. A successful inventory retires parts of providers or models it no longer names. Merges hold an exclusive file lock and publish atomically; an older read time cannot replace a newer saved part. `saved_catalog_parts` only reads the snapshot and reports no fabricated network failure.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
