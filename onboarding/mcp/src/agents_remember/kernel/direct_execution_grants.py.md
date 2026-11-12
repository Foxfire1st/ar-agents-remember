# mcp/src/agents_remember/kernel/direct_execution_grants.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

## Purpose

Owns the shared file representation, addressing, live reads and publication primitives for direct-execution grants.

## Contract

A grant carries a canonical leaf reference, giver, time and optional architect agent ID in the coordination root controlplane store, outside task documents and harness settings. Addressed filenames select one repository/master/leaf; retained bare-digest files are read as a legacy fallback and migrate on writes. require_grant fails closed on missing or unreadable records; plan census skips broken records. The advisory process-shared lock protects read/proof phases; exclusive file creation and post-publication/revocation proof complete the application writers' concurrency protocol. The store is a product-interface boundary, not protection from arbitrary shell file writes.

## Evidence


- Owns the shared file representation, addressing, live reads and publication primitives for direct-execution grants [1]
