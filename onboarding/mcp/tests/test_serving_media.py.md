# mcp/tests/test_serving_media.py

## Governing Overview

[overview](overview.md)

## Purpose

Checks shared media responses and their serving-route selection boundaries.

## Code Commentary

Cases cover fixed types, byte bounds, ranges, typed refusal statuses and the 416 Content-Range header, working media, injected knowledge transport, metadata-only diff sides and historical lexical path handling. Assertions distinguish metadata reads from media payload reads.

## Relationships

Route-specific file, notes and comparison tests complement this shared media suite. Test declarations supply proof facets; execution is recorded in candidate-bound check evidence.

## Evidence

- Checks shared media responses and their serving-route selection boundaries. [1]
