# mcp/test_support/agents_remember_test_support/testing/capsule_audience_structure.py

## Governing Overview

[Overview](overview.md)

## Purpose

Builds independent source-section projections for capsule audience assertions.

## Code Commentary

The helper filters common and addressed role sections, excludes audience control markers and foreign leading prose, and compares the result with delivered operation text. It selects a foreign-role passage for the audience test to inject, and counts detail links outside fences. These are structural assertions; they do not establish semantic equivalence of arbitrary prose.

## Relationships

Capsule audience tests use these projections instead of current-text seal tables. Compiler output remains the observed side of the comparison.

## Evidence



- Audience assertions compare delivered text with independently projected source sections. [1]
- Detail links are counted outside fenced blocks. [2]

### Repo-Internal References (renewed)

- The helper selects a foreign-role passage; the audience test appends it to the observed stage and expects comparison to fail. [3]
