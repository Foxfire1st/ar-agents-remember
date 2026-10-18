# mcp/tests/test_stored_gates.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects the retained stored-gate data and landing refusal semantics after public gate creation/decision/wait tools and agent hosting are removed.

## Code Commentary

### Logic

Pure GateRecord snapshots and append/last-wins folding remain testable data operations. Existing open/applied logs refuse retained closeout, direct landing and integration with their existing statuses/reasons plus the explicit removed-stores way out. The removed prepared-finalization helper/case is replaced by surviving closeout gate-read/gate-claim coverage, not restored as a finalization channel. Parameterized refusal assertions forbid removed tool names, fresh gate channels and unregistered nextTool values; queue repair names only retained selection tools.

### Invariants And Boundaries

Creating a fixture record is not a restored production gate channel. Refused claims spend no gate state. Stored logs are removed only on the user’s explicit command, never silently ignored to admit a landing. This is static assertion documentation, not acceptance of a Git transaction.

The stored-gate refusal matrix now includes closeout-preview and integration-dry-run alongside real integration and prior refusal cases. Each requires the removed-stores way out and forbids removed tools/new gate channels; direct handover refusal retains its exact coded blocker, reason and non-tool nextOperation. These are source/assertion facts, not new executed evidence.

At two absent-subject sizes, claim_approval permits a gateless claim without creating even the store root or a lock. A real fixture approval is permitted once, then applied and unavailable to a second claim. This retained record contract restores no public gate tool.

## Evidence

- Absent approval has no store footprint; an existing approval is spent exactly once. [3]
- Stored gate read and claim refusal stays on the retained closeout route. [5]
- The retained closeout refusal assertion preserves the exact gate-enforcement reason and removed-stores way out. [4]


No Domain Documentation source is configured for this repository-specific boundary.

- Stored-gate refusal preservation: implementation/assertion boundary described above. [1]


- The stored-gate refusal matrix now includes closeout-preview and integration-dry-run alongside real integration and prior refusal cases. Each requires the removed-stores way out and forbids removed tools/new gate channels; direct handover refusal retains its exact coded blocker, reason and non-tool nextOperation. These are source/assertion facts, not new executed evidence. [2]
