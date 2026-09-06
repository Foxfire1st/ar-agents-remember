# mcp/certification-profile-v1.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/certification-profile-v1.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:03:51+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
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

Treat the JSON as canonical profile data. Refresh profile, runtime and selector digests from their actual owners after semantic source changes. The current declaration binds profile digest `da307cd8d609068479ca24c9c0d4c4cadfb6f04f4e215ee5f0170916a7131117`, selector configuration digest `5a6c02980b9428702808d770c2961d55b73c51990509f84b584a0daaa1c39309`, and runtime digest `c3a5108ddf6c1fc519cf6f52bf570bc956c4ac31a045a543e2e05a2ef4383b63`.

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
| The exact canonical profile digest is declared. | "profileDigest" | mcp/certification-profile-v1.json:182-182 |
| Closeout and local selections carry explicit gate applicability. | "selections" | mcp/certification-profile-v1.json:3117-3616 |
| Selectors bind the exact configuration owner digest. | "selectors" | mcp/certification-profile-v1.json:3617-3667 |
| The Dagger adapter and result decoder are explicit profile contracts. | "executorAdapters"; "resultDecoders" | mcp/certification-profile-v1.json:35-57; mcp/certification-profile-v1.json:3032-3115 |
| The finite publication inventory declares actual report paths and byte bounds. | "publishedArtifacts" | mcp/certification-profile-v1.json:184-679 |
| The profile declares bounded reconstruction and generated source/input ownership. | "environments"; "generatedInputs" | mcp/certification-profile-v1.json:2-34; mcp/certification-profile-v1.json:58-181 |
| Ambient source applicability retains explicit evidence and teardown depends on it conditionally. | "sourceApplicability"; "conditionalPrerequisites" | mcp/certification-profile-v1.json:767-805; mcp/certification-profile-v1.json:2934-2939 |
| Real rail files and exact captures are retained without mutating the execution handle. | `attach_rail_terminal_bindings` | .dagger/src/agents_remember_quality/rail_emission.py:71-107 |
| Teardown verifies started evidence or proves admitted zero-start with no summary. | `_verify_teardown`; `_write_unstarted_teardown` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:253-263; mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:266-276 |
| The report branch persists retained bytes before validating/exporting the final payload. | `prepare_profile_reports`; `export_profile_reports` | .dagger/src/agents_remember_quality/profile_publication.py:18-44; .dagger/src/agents_remember_quality/profile_publication.py:47-67 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-06T15:03:51+00:00 — Verified the curated profile card at actual commit c69d5171187fa1957025e393270db9f5a864ab14: exact profile/selector/runtime pins, 54 publications including 32 captures, conditional ambient/teardown behavior and active references. Preserved all earlier history; declarations remain distinct from executed certification evidence.

- 2026-09-06T14:03:43+00:00 — L33 candidate curation: Reconciled the finite environment/source-selection publications, reconstruction and generated-input declarations, conditional ambient prerequisite, and actual canonical digest pins; repaired source ranges. Existing verification commit/date and all prior history are retained pending review against a real code commit.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:20+00:00 — L30 source review: reconciled the real browser/provider/teardown producers, finite byte-capture publications and exact owner-derived digest pins; retained local applicability and later lifecycle boundaries.

- 2026-09-05T06:14:14+00:00 — Reconciled selector/runtime profile evolution and documented the unsatisfied required Gate-4 producer contracts without treating declarations as proof.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the profile regeneration for the five-gate/authority cutover - `profileDigest` `34858daa...` and adapter `runtimeDigest` `4cf0e133...` moved with the changed Dagger module bytes, every rail now declares explicit `successExitCodes`/`skippedExitCodes` arrays, and digest anchor lines were re-pointed (2733/2793).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): created the card for the checked-in canonical certification profile and recorded the three regenerated digest authorities (`profileDigest`, selector `configurationDigest`, adapter `runtimeDigest`); no prior sidecar existed.
