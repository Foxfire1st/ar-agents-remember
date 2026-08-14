# dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Group of retained-chat telemetry tests for `AmbientTelemetry`. | "AmbientTelemetry retained-chat activity" | dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.test.tsx:10-10 |
| Test that an inactive retained surface aborts the in-flight telemetry read. | "aborts the in-flight telemetry read as soon as its retained surface becomes inactive" | dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.test.tsx:11-11 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new test file; anchors derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
