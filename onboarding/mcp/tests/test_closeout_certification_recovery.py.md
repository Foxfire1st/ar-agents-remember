# mcp/tests/test_closeout_certification_recovery.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises owner-derived R05 certification recovery decisions through real plan, result, certificate, and selected-reuse compilers. The suite distinguishes exact input deltas, unchanged interruption reuse, prior-red catalog requirements, and retained evidence mismatch refusal.

## Code Commentary

### Logic

`_snapshot`, `_catalog`, and `_chain` build exact fixture authority. The retained tests select only the required suffix after a gate-input change, reject reuse after code change, preserve exact certificates across unchanged interruption, and require complete prior-red evidence before recovery.

### Invariants And Boundaries

- Recovery decisions derive from immutable candidate/profile/plan evidence.
- Unchanged interruption reuses the exact original prefix; changed inputs reopen the required suffix.
- Prior-red recovery refuses missing, reordered, or mismatched original evidence.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- Recovery behavior is repository-owned by the exact retained tests. [1]

### Repo-Internal References

- Snapshot and certificate fixtures bind exact recovery inputs. [2]
- Gate input deltas reopen only their required suffix. [3]
- Prior-red recovery requires the exact original catalog and evidence dependencies. [4]

### Cross-Repo References

None; the tests use local certification owners.
