# mcp/tests/test_knowledge_reader_media.py

## Governing Overview

[overview](overview.md)

## Purpose

Checks media classification and invalid selection refusal through the knowledge application's real selected-tree path.

## Code Commentary

The cases cover a UTF-8 SVG as media and an option-shaped knowledge commit that must be refused. They preserve the intended knowledge-reader commit-selection exception while rejecting invalid selectors.

## Relationships

These cases exercise the application reader. Shared transport tests separately check bytes, range responses and error mapping.

## Evidence

- Checks media classification and invalid selection refusal through the knowledge application's real selected-tree path. [1]
