# mcp/src/agents_remember/application/knowledge_writer/file_publication.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Publishes an already validated file candidate and reports both the original filesystem failure and any incomplete rollback.

## Code Commentary

publish_files calculates sorted changed/deleted paths, captures their actual disk preimages and writes replacements through adjacent .ar-writer temporary files before replacement. Deleted files are unlinked after writes. On OSError it rolls back completed paths in reverse order, deleting newly created files or restoring original bytes, then reads each destination to verify restoration and removes the temporary. PublicationError preserves the original errno/target and exposes rollback_failures; restored is true only when that list is empty.

## Invariants And Boundaries

This is filesystem publication, not Git commit or validation authority. Rollback is verified best-effort rather than an unconditional atomicity promise: an incomplete restore is explicitly reported, never disguised as a clean refusal.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Publishes an already validated file candidate and reports both the original filesystem failure and any incomplete rollback. This is filesystem publication, not Git commit or validation authority. Rollback is verified best-effort rather than an unconditional atomicity promise: an incomplete restore is explicitly reported, never disguised as a clean refusal. [1]
