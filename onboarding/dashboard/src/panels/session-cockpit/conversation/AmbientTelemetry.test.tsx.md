# dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.test.tsx

## Governing Overview

[overview](overview.md)

## Purpose

Vitest coverage for `AmbientTelemetry` retained-chat activity: the retained surface aborts its in-flight telemetry read as soon as the surface becomes inactive.

## Code Commentary

### Logic

- `describe("AmbientTelemetry retained-chat activity")` (line 10) groups the retained-chat tests.
- `it("aborts the in-flight telemetry read as soon as its retained surface becomes inactive")` (line 11) stubs global `fetch`, renders `AmbientTelemetry` active, asserts one request is in flight and not yet aborted, then rerenders inactive and asserts the request signal is aborted.

### Conventions

Uses `@testing-library/react` `render`/`waitFor` and vitest `vi.stubGlobal`; `afterEach` unstubs globals.

### Invariants And Boundaries

- The test asserts abort-on-inactive, not fetch cancellation semantics of the server.

### Todos

None.

## Evidence

### Repo-Internal References

- Group of retained-chat telemetry tests for `AmbientTelemetry`. [1]
- Test that an inactive retained surface aborts the in-flight telemetry read. [2]
