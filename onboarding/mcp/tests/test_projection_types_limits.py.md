# mcp/tests/test_projection_types_limits.py

## Governing Overview

[overview](../overview.md)

## Purpose

The generated projection mirrors the served provider limit exactly, declares the served build-currentness model, and still refuses an undeclared served model.

## Code Commentary

The dashboard's contract files are generated from the Python wire schema, and the served limit states its resets as date-times: the generator must keep that constraint instead of refusing the schema or letting a hand-maintained substitute drop it.

The generated TypeScript declares `BuildCurrentness` (mode `installed` or `checkout`, state `current`, `stale` or `unknown`, optional loaded and installed digests, first-seen time, reason and remedy) together with optional `buildCurrentness` and `servingProcessId` fields. Adding an undeclared definition to the served schema makes the generator raise `ProjectionTypeGenerationError` for a changed served-schema tail rather than emit a type for it.

**INV-4T6KSE.** These cases pin the checker's behaviour; the obligation for this place is stated in the invariant named here.

## Evidence

- Build currentness is generated explicitly, and an undeclared served model is still refused. [1]
