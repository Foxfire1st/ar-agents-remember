# mcp/certification-profile-v1.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/certification-profile-v1.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Declares Agents Remember's repository-owned certification selections, Gates 1–4 rails, selectors, Dagger adapter, result decoder and published-artifact inventory. The universal certification framework consumes these declarations; Gate 5 remains memory-domain authority.

## Code Commentary

### Logic

`closeout-full` and `closeout-targeted` declare all four code gates. `local-targeted` declares Gate 4 not applicable. Each rail binds identity, prerequisites, observed evidence, required-on-pass artifacts, runtime and execution policy. Selector configuration and executor runtime digests are recomputed from their actual owners; the outer profile digest binds the canonical profile.

The publication inventory is finite: 51 declared paths, including 32 stable `rail-evidence/` capture paths. Captures use `application/octet-stream` because an exact bounded byte tail may begin within a UTF-8 sequence. A rail's `requiredOnPass` artifact obligation remains distinct from an optional path's publication allowance. Exporting a result payload does not excuse absent evidence bytes.

Dashboard browser execution writes the Playwright JSON result at the explicitly configured report path with both line and JSON reporters. Provider integration writes the actual pytest phase report to `provider-integration-result.json`. The teardown rail requests a proof artifact from the report verifier, which checks the existing clean-room summary and both successful `L5-C10` checkpoint records before writing `teardown-proof.json`. Dashboard coverage retains its existing Vitest producer location and receives the stable exported name `dashboard-coverage.json`.

The Dagger emission/export owners retain real files and exact output captures on a separate report branch. The profile declares those paths and their bounds; the host validates the full published snapshot and nested evidence before certificates can reference them. These concrete producers close the earlier three Gate-4 mapping gaps.

### Conventions

Treat the JSON as canonical profile data. Refresh profile, runtime and selector digests from their actual owners after semantic source changes. The inspected candidate binds profile digest `8a3385ad68a89ebdc1e6ffc64296ad7a2eb7039cd5ba20384790150a60ec498b`, selector configuration digest `c140e8eb3623b81676de126c5d3cf07698c18a3a1519cc464622c7ec2ec8eaaf`, and runtime digest `f45228d2bf00df9e4d0894e0cf3b8f4c977f00e5b46931245ba4343f68b205d4`.

### Invariants And Boundaries

- The profile chooses concrete repository rails, never gate order or Gate-5 ownership.
- Every required artifact needs actual producer bytes; declarations alone do not certify execution.
- Required capture bytes remain stable report-relative references, independently of physical generation identity.
- Local Gate-4 non-applicability is not terminal master Gate-4 certification.
- L30 publication support does not compose R05/R16/R07/R08 into the ordinary lifecycle.

### Todos

No remaining producer gap is recorded for the three L30 artifacts. Ordinary lifecycle and final-memory composition remain owned by their separate production recovery leaves.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact canonical profile digest is declared. | "profileDigest" | mcp/certification-profile-v1.json:6-6 |
| Closeout and local selections carry explicit gate applicability. | "selections" | mcp/certification-profile-v1.json:7-506 |
| Selectors bind the exact configuration owner digest. | "selectors" | mcp/certification-profile-v1.json:2736-2786 |
| The Dagger adapter and result decoder are explicit profile contracts. | "executorAdapters" | mcp/certification-profile-v1.json:2787-2809 |
| The finite publication inventory declares actual report paths and byte bounds. | "publishedArtifacts" | mcp/certification-profile-v1.json:2894-3360 |
| Real rail files and exact captures are retained without mutating the execution handle. | `attach_rail_terminal_bindings` | .dagger/src/agents_remember_quality/rail_emission.py:66-100 |
| The report branch persists retained bytes before validating/exporting the final payload. | `prepare_profile_reports`; `export_profile_reports` | .dagger/src/agents_remember_quality/profile_publication.py:18-44; .dagger/src/agents_remember_quality/profile_publication.py:47-67 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:20+00:00 — L30 source review: reconciled the real browser/provider/teardown producers, finite byte-capture publications and exact owner-derived digest pins; retained local applicability and later lifecycle boundaries.

- 2026-09-05T06:14:14+00:00 — Reconciled selector/runtime profile evolution and documented the unsatisfied required Gate-4 producer contracts without treating declarations as proof.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the profile regeneration for the five-gate/authority cutover - `profileDigest` `34858daa...` and adapter `runtimeDigest` `4cf0e133...` moved with the changed Dagger module bytes, every rail now declares explicit `successExitCodes`/`skippedExitCodes` arrays, and digest anchor lines were re-pointed (2733/2793).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): created the card for the checked-in canonical certification profile and recorded the three regenerated digest authorities (`profileDigest`, selector `configurationDigest`, adapter `runtimeDigest`); no prior sidecar existed.
