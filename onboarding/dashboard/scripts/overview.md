# dashboard/scripts/ — Dashboard Quality Scripts Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/scripts/`                             |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-09-07T00:34+02:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

The dashboard quality-rail scripts route owns
`require-dagger-test-environment.mjs` (the canonical nonce/attestation validator), its
type declaration, `check-diff-coverage.mjs` (the per-diff changed-lines coverage diagnostic
mirroring the Python `diff_coverage.py` report), its contract test, and
`check-bundle-size.mjs` (the 32 MiB bundle budget wired into `npm run build`). The route also owns `write-suite-result.mjs`, which writes the CCR dashboard-suite result
after a successful coverage command. Vitest
collects `scripts/**/*.test.mjs` from `dashboard/vitest.config.ts`. Direct targeted
Vitest runs are supported diagnostic loops; the changed-lines CLI itself and all
acceptance remain Dagger-only.

## Code Commentary

### Logic

`check-diff-coverage.mjs` resolves the diff base in the Python resolver's candidate
order (`AR_GATE_DIFF_BASE` → `GITHUB_BASE_REF` origin/<ref> then <ref> →
`@{upstream}` → `origin/HEAD` → `main` → empty tree), diffs changed lines, and
scores them against the v8 coverage JSON using executable-statement semantics
(round-8 architect ruling OPTION 1): the denominator counts only changed lines v8
records as executable statements; comments/blanks/continuations contribute nothing.
The contract test pins that accounting plus the test/dev/types exclusions and
`dashboard/` key normalization.

`daggerTestEnvironmentError` validates one lowercase 32-hex token, reads the fixed
in-container attestation path, and requires an exact byte-for-byte match.
`requireDaggerTestEnvironment` turns that result into the route's fail-loud refusal and
accepts only a subject label for the message. `check-diff-coverage.mjs` calls it as the
first operation of direct `main()` while leaving exported pure scoring helpers open to
diagnostic imports.

### Conventions

Scripts are standalone Node ESM with pure exported helpers and a `main()` runner;
the diff pipe uses a 256 MiB buffer so series-fork diffs cannot ENOBUFS.

### Invariants And Boundaries

The admission, coverage-scoring, and bundle-budget scripts read and report facts without
writing coverage, configuration, or Git state. `write-suite-result.mjs` is the explicit
report writer: `test:coverage` invokes it only after Vitest exits successfully. It writes
`dashboard-suite-result.json` beside `AR_QUALITY_PROGRESS_REPORT`, or in the current directory
when that variable is absent. The script records `passed: true` from that command-chain
assumption; direct execution does not independently prove a test passed. Missing or unreadable
coverage leaves `totals` empty and does not suppress the suite-result file.
No changed-coverage percentage floor is enforced. No code here
writes a nonce, accepts a fake token, bypasses attestation, shadows configuration, or
falls back to a host acceptance executor.

`write-suite-result.mjs` records the coverage path and rounds numeric `coverage.total`
percentages when that optional object exists; ordinary per-file Istanbul coverage need
not contain that summary object. The suite-result record is one artifact, not independent
certification or proof that all required Gate-4 artifacts were produced.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical admission validator checks token shape, fixed-path readability, and exact nonce equality. | `daggerTestEnvironmentError`; `requireDaggerTestEnvironment` | dashboard/scripts/require-dagger-test-environment.mjs:3-34 |
| The declaration mirrors the validator's runtime exports and optional diagnostic subject. | `daggerTestEnvironmentError`; `requireDaggerTestEnvironment` | dashboard/scripts/require-dagger-test-environment.d.mts:1-9 |
| The changed-line scorer is importable for diagnostic callers. | `measureDiffCoverage` | dashboard/scripts/check-diff-coverage.mjs:14-80 |
| The executable-statement contract suite proves both CLI refusal and pure accounting. | "describe(\"check-diff-coverage executable-statement semantics\", () => {" | dashboard/scripts/check-diff-coverage.test.mjs:15-110 |
| Vitest collects the route’s script tests. | "scripts/**/*.test.mjs" | dashboard/vitest.config.ts:51-51 |

## Cross-Repo References

No cross-repository implementation source governs this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |


## Integrated IAS Recovery Contract

Changed-production coverage is diagnostic: `check-diff-coverage.mjs` reports executable changed lines and uncovered lines without a percentage floor. Its direct CLI retains genuine Dagger admission; malformed or missing coverage remains an execution failure. Bundle-size enforcement and suite-result command-chain provenance are unchanged.


## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: "scripts/**/*.test.mjs" repointed to dashboard/vitest.config.ts:51-51. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-07T00:34+02:00 — Reconciled current source anchors and diagnostic/four-worker policy; removed obsolete test-proof claims without altering verification pins.


- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


- 2026-09-05T07:05+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Added suite-result publication ownership and its command-chain, output-path, and optional-coverage limits. Current route claims were checked against the frozen candidate; this stamp records source verification, not execution or certification.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: onboarded the canonical
  Dagger admission validator and declaration, the direct-main changed-lines guard, and the
  supported diagnostic-only targeted Vitest route. Playwright, pytest, changed-lines CLI,
  direct Python wrapper, and acceptance remain Dagger-attested; acceptance verification is
  pending and closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-read the Dagger-environment guard script and its
  collection path; retained the route contract and repaired the exact Vitest anchors. Verification
  remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this route
  overview for the dashboard quality scripts after the executable-statement
  diff-coverage unit and its contract test landed. Verification pinned to `cf5ef50`
  until closeout stamps the code commit.
