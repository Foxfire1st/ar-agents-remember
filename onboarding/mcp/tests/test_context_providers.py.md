# test_context_providers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_context_providers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Managed CGC runtime layout and provider-source hygiene tests.

## Code Commentary

### Logic

Ambient FALKORDB host/port variables do not replace default authority. The layout writes pinned requirements and managed defaults without persisting process-only backend keys. Source-artifact detection reports forbidden files and an unexpected patch source refuses.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Temporary layout checks do not start providers or demonstrate live indexing. Removed cleanup, GrepAI and Windows matrices are not current assertions in this file.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cgc layout ignores host falkordb environment defaults. | `test_cgc_layout_ignores_host_falkordb_environment_defaults` | mcp/tests/test_context_providers.py:26-45 |
| Ensure cgc runtime layout writes pinned defaults. | `test_ensure_cgc_runtime_layout_writes_pinned_defaults` | mcp/tests/test_context_providers.py:47-96 |
| Detects forbidden source provider artifacts. | `test_detects_forbidden_source_provider_artifacts` | mcp/tests/test_context_providers.py:98-110 |
| Patch rejects unexpected source. | `test_patch_rejects_unexpected_source` | mcp/tests/test_context_providers.py:112-118 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-28T10:03:40+02:00 — Reconciled the historical extraction with Candidate A retirement;
  provider-ID assertions survive in the ordinary certifying regression module, not a direct cohort.
- 2026-08-24T21:23+02:00 — Moved provider-ID normalization assertions to the bounded direct cohort.

- 2026-08-02T18:15+02:00 — 260731-EFA-L6 curator W1-B06: anchored 7 Repo-Internal reference rows; scoped result 0 findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: both layout builders now take one value object
  — `cgc_runtime_layout(CgcRepo(...))` and `grepai_runtime_layout(GrepaiWorkspace(...))`, the
  latter renaming the caller-side `workspace_name` keyword to `name` while the layout attribute
  the tests read back keeps its old spelling — so the Logic section names both objects and that
  asymmetry. The rewrapped call sites shifted every test in the file, and all six own-file
  reference rows were re-verified against the current line numbers and re-anchored (for example
  the GrepAI row from L243-L420 to L416-L577 and the patch-helper row from L423-L726 to
  L578-L784); a row was added for the Windows-host container-path tests the table never covered.
  No test case or assertion changed.

- 2026-07-03T01:55+02:00 — L12: timer-pop patch idempotency test, patch-script drift guard, and the materialize test asserts the global/.cgcignore copy is byte-identical to the runtime-root copy.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-02T01:15+02:00: Replaced the mirror-sync and `.grepai/` artifact detection/removal tests with `ensure_grepai_root_gitignore` coverage (append/create/idempotent) and switched layout expansion expectations to live in-place roots (watch-live).
- 2026-05-29T07:19+02:00: Added coverage for `to_container_path`, driveless `container_runtime_root` / `container_code_repo_root` properties, and `env(for_container=True)` (driveless path values, omitted host-only Windows env) for Windows-host provider support.
- 2026-05-28T13:40+02:00: Updated after CGC layout tests removed host venv executable expectations, added stale `venvRoot` rejection coverage, and removed venv module lookup tests.
- 2026-05-28T12:32+02:00: Updated after GrepAI context layout tests moved operator logs under `logs/providers/grepai`.
- 2026-05-25T19:16+02:00: Updated after tests imported the direct `providers.context` facade and provider context implementation moved into `context_modules/`.
- 2026-05-24T19:25+02:00: Added coverage that CGC FalkorDB host/port defaults ignore ambient host `FALKORDB_*` environment variables.
- 2026-05-23T17:50+02:00: Moved onboarding to `mcp/tests` after the tests moved out of `runtime/skills/tests` and updated imports to the MCP package provider module.
- 2026-05-23T05:32+02:00: Updated provider layout expectations to `providers/runners` plus `providers/data`.
- 2026-05-21T23:18+02:00: Updated after adding GrepAI disposable root artifact removal coverage.
- 2026-05-21T13:22+02:00: Updated CGC patch tests for visualizer server route handling, CLI default-route propagation, CLI helper lookup, and the two new patch ids.
- 2026-05-21T12:40+02:00: Updated CGC patch tests for the visualizer repo-query patch, `viz/server.py` module lookup, and patch id stability.
- 2026-05-21T12:35+02:00: Updated GrepAI tests for provider-owned mirror-root expansion and mirror sync that excludes source `.grepai/` artifacts.
- 2026-05-21T12:20+02:00: Updated GrepAI workspace config test notes for explicit local Ollama endpoint and dimensions.
- 2026-05-21T11:50+02:00: Updated for GrepAI workspace-mode tests covering multi-root memory indexing, PostgreSQL data roots, provider-owned config, and `.grepai/` containment.
- 2026-05-21T02:10+02:00: Updated expected CGC backend data layout from provider-owned `_backends` to durable `provider-data/`.
- 2026-05-21T01:47+02:00: Updated for FalkorDB-only CGC layout, managed `.cgcignore` inheritance, missing-root rejection, stale runtime cleanup, GrepAI pin coverage, and the second CGC patch.
- 2026-05-20T19:11+02:00: Created onboarding for the provider layout and patch helper unit tests. Verification metadata remains pinned to the current committed source revision until closeout commits these source changes.
