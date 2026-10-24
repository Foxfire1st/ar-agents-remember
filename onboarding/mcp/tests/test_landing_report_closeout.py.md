# mcp/tests/test_landing_report_closeout.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Drives the real consumers on a landed candidate: the quality check, the invariant gate, the closeout quality phase, the workspace adapter and the curator checklist (F06 of MIK-R120@v1).

## Code Commentary

A landed candidate is one cut card and one added file, which the shared fixture leaves uncommitted. The count-reporting consumers read both populations over those working edits: the check reports both with `ok` true, the closeout adapter passes with both aboard, and the checklist renders the real payloads with equal actionability. The two validation consumers commit the landed candidate first and then require no refusal: the gate refuses nothing it is ready for and the leaf gate evaluation holds no refusal. Two controls keep the cases honest: an existing refusal fires identically with and without the populations, and the closeout adapter reports both on uncommitted work and none otherwise, which is the contract binding the leaf base through the shared contract.

## Invariants And Boundaries

The populations are read from the real consumers' payloads, not from a helper's summary, and every case names the fixture's landing rather than building its own. The refusal control is what makes a clean result meaningful.

## Evidence

### Repo-Internal References

- Every real consumer judges a landed candidate exactly as a clean one. [1]

- An existing refusal fires identically with and without the landing populations. [2]
