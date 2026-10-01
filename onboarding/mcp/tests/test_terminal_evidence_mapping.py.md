# test_terminal_evidence_mapping.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Protects the canonical native terminal-evidence lift at its no-claim boundary. The focused cases
keep malformed and open Pi frames from producing terminal evidence and prove that an unmappable
frame cannot hide a later canonically mapped terminal outcome.

## Code Commentary

### Logic

`CanonicalNativeTerminalMappingTests` builds the existing `NativeEvidenceFrame` and
`NativeEvidencePage` contracts and calls `latest_native_terminal_evidence` directly. The first
case combines a malformed native message with an assistant message that has no stop reason and
expects no projection. The second places the same malformed frame before a Pi `stop` message and
checks the later canonical projection's native identity, completed outcome, and stop reason.

### Conventions

The helpers keep native frame construction and Pi assistant payloads small and explicit. This
module tests the public terminal-evidence lift and its registered projector boundary; it does not
reimplement vendor mapping or the liveness sweeper.

### Invariants And Boundaries

- Unmappable and nonterminal native frames produce no terminal claim.
- A later canonical terminal frame remains observable after an earlier unmappable frame.
- The test does not add a parser, fallback, durable unknown-evidence row, cursor behavior, or
  lifecycle ownership claim; those remain with the existing mapper, LOCR-R20, and the assembled
  lifecycle candidate respectively.
- Focused host results are diagnostic evidence only; leaf acceptance and master review remain
  lifecycle-owned.

### Todos

Re-run this focused proof against the assembled observer candidate and preserve the separate R20
cursor proof before any master-level acceptance decision.

## Evidence

### Docs References

No configured domain documentation is needed for this repository-owned mapper regression.

No relevant external documentation was configured for this test contract.

### Repo-Internal References

The test exercises the existing native-page lift and the registered Pi projector's terminal stop
mapping without changing production code.

- The native lift skips `UnmappableShape`, ignores non-terminal mapper outputs, and retains the latest mapped projection. [1]
- A malformed or open frame makes no claim. [2]
- A later Pi stop frame remains canonical and identifiable after an unmappable frame. [3]
- Pi `stop` maps to a completed terminal outcome through the registered projector. [4]

### Cross-Repo References

This test has no implementation boundary outside the agents-remember repository.

No meaningful cross-repository references found.
