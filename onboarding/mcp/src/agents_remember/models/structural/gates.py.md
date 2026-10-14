# mcp/src/agents_remember/models/structural/gates.py

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Re-exports the retained gate vocabulary used by control-plane records from kernel.primitives.gate_vocab. This20-line compatibility module owns no delegated-gate request/response classes, public/internal identity DTOs, caller authorization or recording operation.

## Code Commentary

Its only exports are GATE_KINDS, GateKind, GateState and coerce_gate_kind. The primitive module is the vocabulary owner; re-exporting those names does not restore the removed model-facing session/gate tools.

### Historical delegated-gate DTO account (superseded by R113)

The former relocated models/gates.py implementation separated structural requests from internal exact-correlation responses and used Internal* as a nonpublic marker. R113 removes that request/response implementation from this carrier. Its declared-caller/decision-recording account is historical, not authorization performed by this module.

## Evidence

- Only gate-vocabulary re-exports remain; no delegated-gate request/response classes or recording owner. [1]

- The former public gate-summary DTO is no longer owned here; the current carrier only exports primitive vocabulary. [2]
