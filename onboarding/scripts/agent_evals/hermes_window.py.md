# scripts/agent_evals/hermes_window.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Resolves the selected model window through a source-bound native Hermes probe.

## Code Commentary

### Invariants And Boundaries

The probe restricts writes and network access. Its admitted GPT catalog lookup has a specific host/path; lookup refusal remains a binding failure.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
