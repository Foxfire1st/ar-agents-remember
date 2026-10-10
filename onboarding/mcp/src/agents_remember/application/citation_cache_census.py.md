# mcp/src/agents_remember/application/citation_cache_census.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

Census of orphaned citation source index slots: the publisher-owned index directories rule 3 deletes.

## Code Commentary

MIK-R82 rule 3: a citation source index is the citation publisher's own record beside its database. The managed namespace (`temp/citation-source-index/managed`) belongs to the cache authority and is never entered; every other publisher-shaped slot directory, under task notes or enclosure cache roots, is listed by `scan_citation_caches` and deleted by `delete_citation_caches` with its slot directory. The archive hook deletes `ar-cache-*` directories under an archived task folder through the same rule name.

## Evidence

- Orphaned publisher index slots are listed and deleted; the managed namespace is never entered. [1]
