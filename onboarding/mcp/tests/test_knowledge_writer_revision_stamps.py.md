# mcp/tests/test_knowledge_writer_revision_stamps.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Checks provenance and revision behavior of the shared writer using bound fixture callers.

## Evidence

- The stored stamp uses the bound caller and its receipt. [1]
- A repeated write of one owned revision renews its attribution. [2]
- A reopened attempt leaves the earlier attempt's stamp intact. [3]
