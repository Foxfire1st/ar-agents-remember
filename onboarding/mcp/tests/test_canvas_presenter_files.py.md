# mcp/tests/test_canvas_presenter_files.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Native IO keeps the admitted physical parent: a directory swapped after admission cannot redirect a read, a write or a removal.

## Code Commentary

- The held-descriptor route is exercised through the real IO owners rather than a double.

## Evidence

- The case `test_native_io_keeps_the_admitted_physical_parent` protects this behaviour. [1]
