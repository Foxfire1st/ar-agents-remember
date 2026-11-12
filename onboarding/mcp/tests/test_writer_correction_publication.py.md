# mcp/tests/test_writer_correction_publication.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Describes filesystem-failure rollback assertions for validated writer publication.

## Code Commentary

An injected third replacement failure must restore earlier writes and return no published records. A separate rollback deletion failure must preserve the original publication error, name the surviving file and continue independent restoration, without claiming the write was undone. Direct publisher cases cover replacement, creation and deletion restoration together and require the exact previous directory bytes.

## Invariants And Boundaries

The successful-restore and incomplete-rollback cases are distinct contracts. They do not justify retrying a native write that actually succeeded before an unrelated wrapper failed.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Describes filesystem-failure rollback assertions for validated writer publication. The successful-restore and incomplete-rollback cases are distinct contracts. They do not justify retrying a native write that actually succeeded before an unrelated wrapper failed. [1]
