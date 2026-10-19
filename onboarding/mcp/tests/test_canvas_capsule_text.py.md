# mcp/tests/test_canvas_capsule_text.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The capability text's packaging: it is read from the installed package-data copy, its budget and wording are enforced at the read, and the installed copy is the generated copy of the canonical source.

## Code Commentary

- The installed copy is generated from the canonical source, so a hand-edited copy fails.
- The launch record names whether the baseline, an addition or a replacement was used.

## Evidence

- The case `test_the_installed_copy_is_the_generated_copy_of_the_canonical_source` protects this behaviour. [1]
- The case `test_the_launch_record_names_the_baseline_the_addition_or_the_replacement` protects this behaviour. [2]
