# mcp/tests/test_stored_operation_record_seat_fields.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects read compatibility of stored operation-result mappings after automatic seat-close/land fields disappear from current integrate/finalize responses.

## Code Commentary

### Logic

An independently composed schema3.0 integration record includes autoClosedSeats, autoCloseDeferredSeats, autoCloseFailedSeats and autoLandedSeats in result. The test writes it to pytest scratch, reads through LifecycleOperationStore and asserts values and stored bytes unchanged. A separate test checks both current answer models declare none of these four fields.

### Invariants And Boundaries

The stored result remains a free mapping, not validated against today’s response DTO. Successful reading does not restore automatic seat execution, modify an old record or guarantee compatibility for arbitrary older schemas.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Old seat-field record compatibility: implementation/assertion boundary described above. [1]
