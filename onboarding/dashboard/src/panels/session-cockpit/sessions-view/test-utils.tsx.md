# dashboard/src/panels/session-cockpit/sessions-view/test-utils.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/test-utils.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

Shared fixture builders for the split SessionsView test files, extracted from
`SessionsView.test.tsx` by the 260731-EFA-L8 split. Exports the lazy-loaded
terminal mount/unmount ledgers and the session seeding helpers the split suites use.

## Code Commentary

### Logic

`mockTerminalMounts` / `mockTerminalUnmounts` record Terminal lifecycle calls;
`seedReadyComposerSession` / `seedLegacyRawSession` / `seedLiveProjection` seed the
cockpit store; `stubHangingFetch` installs the hanging-fetch stub. The `vi.mock`
factory imports these lazily to avoid hoisting TDZ.

### Conventions

Test-only; never imported by production code.

### Invariants And Boundaries

The ledgers must be imported by any split file that asserts Terminal mount/unmount
behavior.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared seeds and terminal ledgers. | `seedReadyComposerSession`; `seedLiveProjection`; `mockTerminalMounts` | dashboard/src/panels/session-cockpit/sessions-view/test-utils.tsx:26-57; dashboard/src/panels/session-cockpit/sessions-view/test-utils.tsx:81-93 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shared
  test fixtures extracted from `SessionsView.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
