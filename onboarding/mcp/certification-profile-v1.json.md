# mcp/certification-profile-v1.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/certification-profile-v1.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Declares Agents Remember's repository-owned certification selections, Gates 1–4 rails, selectors, Dagger adapter, result decoder and published-artifact inventory. The universal certification framework consumes these declarations; Gate 5 remains memory-domain authority.

## Code Commentary

### Logic

`closeout-full` and `closeout-targeted` declare all four code gates. `local-targeted` declares Gate 4 not applicable. Each rail binds identity, prerequisites, observed evidence, required-on-pass artifacts, runtime and execution policy. Selector configuration and executor runtime digests are recomputed from their actual owners; the outer profile digest binds the canonical profile.

The publication inventory is finite: 54 declared paths, including 32 stable `rail-evidence/` capture paths. Captures use `application/octet-stream` because an exact bounded byte tail may begin within a UTF-8 sequence. A rail's `requiredOnPass` artifact obligation remains distinct from an optional path's publication allowance. Exporting a result payload does not excuse absent evidence bytes.

Dashboard browser execution writes the Playwright JSON result at the explicitly configured report path with both line and JSON reporters. Provider integration writes the actual pytest phase report to `provider-integration-result.json`. For an applicable ambient scenario, the teardown verifier checks the existing clean-room summary and both successful `L5-C10` checkpoint records before writing `teardown-proof.json`. For an admitted not-applicable scenario, it requires summary absence and writes a zero-start proof with the exact source-decision digest and empty replications. Dashboard coverage retains its existing Vitest producer location and receives the stable exported name `dashboard-coverage.json`.

The profile also declares a bounded dashboard dependency census and reconstruction proof for resumed Gates 2–4, generated-input source/output scopes, and exact source applicability for the ambient-role rail. Its source-selection report remains required even when that rail is not applicable; teardown treats the ambient-role prerequisite conditionally. These declarations do not narrow the unconditional dashboard suite or turn full Python ownership into a focused population.

The Dagger emission/export owners retain real files and exact output captures on a separate report branch. The profile declares those paths and their bounds; the host validates the full published snapshot and nested evidence before certificates can reference them. These concrete producers close the earlier three Gate-4 mapping gaps.

### Conventions

Treat the JSON as canonical profile data. Refresh profile, runtime and selector digests from their actual owners after semantic source changes. The reduced test population changed selector configuration and the profile identity. Coverage and production CRAP observations are diagnostic under current repository policy; profile digests are not metric pass claims. The current declaration binds profile digest `5096c06a017e237a6a3f3cb6b9e1c703e2304d44831716cbfaf898699f9bfb1d`, selector configuration digest `e6fe17146ba4ac8ee68c3d94fc076f1de4d69c61f05080e405d12a2eef3fdc72`, and runtime digest `1ea0d21043dcc358b6f18de7a0eddaf27418122f95412b479bb066ae0bec299a`.

### Invariants And Boundaries

- The profile chooses concrete repository rails, never gate order or Gate-5 ownership.
- Every required artifact needs actual producer bytes; declarations alone do not certify execution.
- Required capture bytes remain stable report-relative references, independently of physical generation identity.
- Local Gate-4 non-applicability is not terminal master Gate-4 certification.
- Declaration changes do not certify themselves; current lifecycle composition must be established from runtime owners and execution evidence.

### Todos

No remaining producer gap is recorded for the three L30 artifacts. The profile declaration does not itself prove runtime composition or final-memory acceptance. Those facts require their canonical execution evidence.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Bounded dependency reconstruction environments | `environments` | mcp/certification-profile-v1.json:2-34 |
| Pinned Dagger execution adapter and actual runtime digest | `executorAdapters` | mcp/certification-profile-v1.json:35-57 |
| Current canonical profile digest | `profileDigest` | mcp/certification-profile-v1.json:182-182 |
| 54 report paths including 32 rail-evidence captures | `publishedArtifacts` | mcp/certification-profile-v1.json:184-679 |
| Full/targeted/local selections and explicit applicability | `selections` | mcp/certification-profile-v1.json:3117-3616 |
| Current source-owned selector configuration digest | `selectors` | mcp/certification-profile-v1.json:3617-3667 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T15:03:51+00:00 — Verified the curated profile card at actual commit c69d5171187fa1957025e393270db9f5a864ab14: exact profile/selector/runtime pins, 54 publications including 32 captures, conditional ambient/teardown behavior and active references. Preserved all earlier history; declarations remain distinct from executed certification evidence.

- 2026-09-06T14:03:43+00:00 — L33 candidate curation: Reconciled the finite environment/source-selection publications, reconstruction and generated-input declarations, conditional ambient prerequisite, and actual canonical digest pins; repaired source ranges. Existing verification commit/date and all prior history are retained pending review against a real code commit.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:20+00:00 — L30 source review: reconciled the real browser/provider/teardown producers, finite byte-capture publications and exact owner-derived digest pins; retained local applicability and later lifecycle boundaries.

- 2026-09-05T06:14:14+00:00 — Reconciled selector/runtime profile evolution and documented the unsatisfied required Gate-4 producer contracts without treating declarations as proof.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the profile regeneration for the five-gate/authority cutover - `profileDigest` `34858daa...` and adapter `runtimeDigest` `4cf0e133...` moved with the changed Dagger module bytes, every rail now declares explicit `successExitCodes`/`skippedExitCodes` arrays, and digest anchor lines were re-pointed (2733/2793).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): created the card for the checked-in canonical certification profile and recorded the three regenerated digest authorities (`profileDigest`, selector `configurationDigest`, adapter `runtimeDigest`); no prior sidecar existed.
