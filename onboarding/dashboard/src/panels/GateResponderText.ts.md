# dashboard/src/panels/GateResponderText.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/GateResponderText.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-25T13:10+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

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

## Update History

- 2026-06-25T13:10+02:00 — Created for task 23/24 extraction from the oversized gate responder component.
