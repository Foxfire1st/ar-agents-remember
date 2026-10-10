# mcp/tests/test_record_landing.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Locks the pull-request landing route and the ways it must refuse. A recording that succeeds sets the terminal integration cell; a commit that landed nowhere, an unapproved call, and a missing commit argument each fail without writing the cell. The suite stays self-contained: it builds its own series contract and Git repositories rather than importing the shared lineage fixture, so this card is owned by the module it exercises instead of inheriting that suite's transitive support closure.

## Code Commentary

`_fixture` creates real code and memory repositories with `main`, `super` and `ar/master` branches, then builds an external-memory series contract over both, so the route's own logic is what is under test against a fully-backed contract. `_commit_on` commits on a named branch and returns the SHA the route records; `_record` is the explicitly-typed approved-call shorthand. `RecordLandingTests` holds seven cases: the happy path setting `completed` with the `pr` label and exact commit, the nowhere-landed anti-fabrication refusal, approval and commit-argument gates, dry-run silence, idempotent repeat, and the checkpointed series never upgrading into a reclaimable integration.

## Evidence

- External-memory series contract over real code and memory repos [7]
- Approved-call shorthand with typed arguments [8]
- Landed commit sets the terminal cell with the pr label [9]
- Nowhere-landed commit refused, cell untouched [10]
- Checkpointed series never upgraded into a reclaimable integration [11]
