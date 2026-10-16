# mcp/src/agents_remember/cli/role_launch_choices.py

## Purpose

Record host-observed launch choices without overwriting requested provenance.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

observe_launch_choices replaces a step-up’s displayed model with a non-null host-applied model and preserves requestedModel (including None for an unstated model). It does not rewrite the saved sessionOptions or replay call.

Model, effort and mode choices gain observedValue; only host-default choices adopt that observation as value. Feature choices gain observedValue. Stated mode/feature mismatches append warnings; this is disclosure, not permission adjustment or a guarantee that the host applied the request.

The former receipt-local observer is imported under its old private name, so existing receipt/outcome callers keep one implementation. record_step_up later reconciles the observed destination to task metadata through its own owner.

## Evidence

- Observed model and requestedModel remain distinct. [1]
- Observed values and mode/feature warnings retain source attribution. [2]
- A created outcome invokes the imported receipt seam. [3]
- Test source preserves requested default, observed model and same-request correction. [4]
