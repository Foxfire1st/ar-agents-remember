# scripts/canvas_kit_proof_app.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

The kit proof's own web app: it serves the pinned kit page for the browser proof, so the kit's offline rendering is measured in a browser rather than asserted.

## Code Commentary

- It is a developer-run witness, not product runtime code: nothing in the serving path imports it.
- Its value is the record it produces, which the proof consumer reads.

## Evidence

- This script is a proof/inspection harness, not product runtime code. [1]
