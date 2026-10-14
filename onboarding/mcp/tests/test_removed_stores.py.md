# mcp/tests/test_removed_stores.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects install’s report-only preservation of old stores and the separate explicit cleanup command, including stored-gate recovery and incomplete removal.

## Code Commentary

### Logic

Fixtures create representative stores beside retained events, dismissals and gate locks. Cases assert exact store membership, copies/locks and sizes, installation nondeletion, registered install report contents, dry-run byte preservation, successful deletion, link-target preservation, escaped-root refusal and continued processing after discovery/file/folder failures. Permission-denial cases skip for superuser because mode closure cannot constrain that account.

### Invariants And Boundaries

The registered-tool case always reads the full filed report. It checks an inline/full-answer or detail-reference payload only when _answer_whole can obtain one: an extreme-width overflow without log carries no readable whole answer. Do not promote the conditional assertion to an all-inline or universal detail-reference guarantee. Fixtures/settings paths stay in pytest-owned isolation; this card attests assertions, not execution.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Removed-store reporting and explicit deletion tests: implementation/assertion boundary described above. [1]
