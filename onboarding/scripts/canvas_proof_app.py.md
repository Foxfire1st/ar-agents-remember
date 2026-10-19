# scripts/canvas_proof_app.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

The isolation proof's own web app: it composes the same middleware and policy the product composes, so the recorded browser proof measures the product's actual enforcement rather than a simplified stand-in.

## Code Commentary

- It is a developer-run witness, not product runtime code: nothing in the serving path imports it.
- Its value is the record it produces, which the proof consumer reads.

## Evidence

- This script is a proof/inspection harness, not product runtime code. [1]
