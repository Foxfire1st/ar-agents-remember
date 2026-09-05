# mcp/certification-profile-v1.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/certification-profile-v1.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `8f670ceecd75323600c873d40c47c4a1cc946ab3` |
| lastVerifiedCommitDate | 2026-09-05T06:48:24+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Declares Agents Remember's repository-owned certification selections, Gates 1–4 rails, selectors, Dagger adapter, result decoder and published-artifact inventory. The universal certification framework consumes these declarations; Gate 5 remains memory-domain authority.

## Code Commentary

### Logic

The closeout-full, closeout-targeted and local-targeted selections declare their gate populations explicitly. Each rail binds identity, prerequisites, evidence, required-on-pass artifacts, runtime and execution policy. Selector configuration and executor runtime digests are recomputed authorities; they cannot be copied from another source revision.

The current artifact inventory includes the dashboard suite-result file produced after the ordinary Vitest suite. Optional publication of a file in `publishedArtifacts` and a rail's `requiredOnPass` artifact requirement are different contracts. A rail cannot mint a green certificate merely because the overall export completed.

Three Gate-4 rails declare `dashboard-e2e-result`, `provider-integration-result` and `teardown-proof`. The inspected executor mapping has no producer binding for these three artifacts. Their declaration therefore remains an unsatisfied production obligation, even if the underlying browser/provider/teardown commands return success. Python coverage artifacts also require an actual coverage-producing scope.

### Conventions

Treat the JSON as canonical profile data. Refresh profile, runtime and selector digests from their actual owners after semantic source changes; never hand-author replacement digest values to pass admission.

### Invariants And Boundaries

- The profile may choose concrete repository rails, not redefine gate order or Gate-5 ownership.
- Every required artifact must be backed by observed producer bytes.
- An artifact publication allowance does not prove its producer exists.
- Local Gate-4 non-applicability is not terminal master Gate-4 certification.

### Todos

Implement the three missing Gate-4 result producers and their executor bindings before claiming a complete green certificate chain.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical repository profile identity | "profileDigest"; "agents-remember-certification" | mcp/certification-profile-v1.json:1-15 |
| Required dashboard browser result | "dashboard-e2e-result" | mcp/certification-profile-v1.json:779-801 |
| Required provider integration result | "provider-integration-result" | mcp/certification-profile-v1.json:1803-1825 |
| Required teardown proof | "teardown-proof" | mcp/certification-profile-v1.json:2681-2703 |
| Selector, executor and decoder contracts | "selectors"; "executorAdapters"; "resultDecoders" | mcp/certification-profile-v1.json:2728-2885 |
| Dashboard suite artifact publication allowance | "dashboard-suite-result.json" | mcp/certification-profile-v1.json:2968-2981 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Reconciled selector/runtime profile evolution and documented the unsatisfied required Gate-4 producer contracts without treating declarations as proof.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the profile regeneration for the five-gate/authority cutover - `profileDigest` `34858daa...` and adapter `runtimeDigest` `4cf0e133...` moved with the changed Dagger module bytes, every rail now declares explicit `successExitCodes`/`skippedExitCodes` arrays, and digest anchor lines were re-pointed (2733/2793).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): created the card for the checked-in canonical certification profile and recorded the three regenerated digest authorities (`profileDigest`, selector `configurationDigest`, adapter `runtimeDigest`); no prior sidecar existed.
