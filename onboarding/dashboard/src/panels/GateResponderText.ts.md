# dashboard/src/panels/GateResponderText.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/GateResponderText.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-25T13:10+02:00                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`|
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-06-25T13:10+02:00 — Created for task 23/24 extraction from the oversized gate responder component.
