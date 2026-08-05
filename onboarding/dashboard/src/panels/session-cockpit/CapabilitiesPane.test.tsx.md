# dashboard/src/panels/session-cockpit/CapabilitiesPane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CapabilitiesPane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Protects the capability authority split and proves that refresh controls use only the established
exact-session and harness read routes.

## Code Commentary

### Logic

- The first case distinguishes live focused-session truth from the pre-session envelope, including
  model-local effort options and honest missing-echo copy.
- The refresh case spies the existing capability routes and rejects invented mutation or alternate
  transport behavior.

### Invariants And Boundaries

- Tests keep the two authorities independently assertable.
- Native-process cost copy remains qualitative unless observed timing exists.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Authority-separation regression for `SNAPSHOT`. | `SNAPSHOT` | dashboard/src/panels/session-cockpit/CapabilitiesPane.test.tsx:11-58 |
| Existing-read-route regression for "uses only the existing exact-session and harness refresh routes". | "uses only the existing exact-session and harness refresh routes" | dashboard/src/panels/session-cockpit/CapabilitiesPane.test.tsx:124-151 |
| Component under test, `CapabilitiesPane`. | `CapabilitiesPane` | dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:84-240 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 3 table citations for the capability snapshot, route assertion, and pane component; fixer-generated ranges verified.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
