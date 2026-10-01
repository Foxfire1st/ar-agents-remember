# dashboard/src/panels/GateResponderText.ts

## Governing Overview

[overview.md](overview.md)

## Purpose

Formatting helpers for `GateResponder.tsx`.

## Code Commentary

Owns the gate request preview (`requestText`), diagnostics JSON formatting, packaged agent response
body, status text, and `isWorktreeGateKind`. It accepts projection `GateNode` plus optional proto-ask
payloads and returns display strings only. Keeping these helpers here lets `GateResponder.tsx` focus on
dialog behavior, routing, and server writes.

## Invariants And Boundaries

- No network or store access; this is presentation formatting only.
- `Chat`/decision behavior stays in `GateResponder.tsx`; this module does not choose actions.
