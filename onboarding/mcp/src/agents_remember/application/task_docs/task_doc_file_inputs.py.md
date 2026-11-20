# mcp/src/agents_remember/application/task_docs/task_doc_file_inputs.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Reads task-document text input from a bounded absolute file and identifies the exact bytes.

## Evidence

- The helper admits readable UTF-8 from an absolute regular file, applies the size bound and returns its SHA-256 digest. [1]
