# scripts/canvas-publication-proof.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

The publication proof harness: it drives a revision from an attempt folder through the confined writer and records what published, so a publication claim can be checked outside the test suite.

## Code Commentary

- It is a developer-run witness, not product runtime code: nothing in the serving path imports it.
- Its value is the record it produces, which the proof consumer reads.

## Evidence

- This script is a proof/inspection harness, not product runtime code. [1]
