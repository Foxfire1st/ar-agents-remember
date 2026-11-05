# scripts/agent_evals/trial_credentials.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Records credential borrowing declarations and comparison outcomes without serializing selected auth contents.

## Code Commentary

### Invariants And Boundaries

A GPT comparison difference or observation error becomes a binding failure. Other-arm differences remain reported comparisons; GPT expiry is revalidated before actor execution.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
