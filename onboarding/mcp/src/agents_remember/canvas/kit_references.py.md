# mcp/src/agents_remember/canvas/kit_references.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

This module resolves references from an explainer draft to the pinned canvas kit.

## Code Commentary

References are normalized relative to the referring file. The extractor reads HTML and CSS references and JavaScript import syntax. `verify_kit_assets` checks any draft copy under `kit/` against the shipped bytes and manifest. The collector carries requested files with their required companions and notices.

## Relationships

Readiness uses the same reference parser. The registered publication path stages carried kit bytes before the checks run.

## Evidence

- The draft copy verifier compares exact bytes, size and manifest digest. [1]
