# test_config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_config.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Runtime authority settings, repository identity and path-containment tests.

## Code Commentary

### Logic

Real temporary Git aliases cannot give two repository IDs or external memory the same Git common directory. Configuration must live outside coordination. The positive authority fixture checks derived provider paths and runtime settings; malformed certification-profile paths, escaped contract paths and globally delegated human-pinned gates refuse.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

These cases establish configuration authority, not provider startup. Historical migration-warning and broad settings matrices are no longer present.

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
| Two repository ids cannot share one git common dir. | `test_two_repository_ids_cannot_share_one_git_common_dir` | mcp/tests/test_config.py:47-60 |
| External memory cannot alias another configured code repo. | `test_external_memory_cannot_alias_another_configured_code_repo` | mcp/tests/test_config.py:62-78 |
| Config must not live inside coordination root. | `test_config_must_not_live_inside_coordination_root` | mcp/tests/test_config.py:80-87 |
| Loads authority settings. | `test_loads_authority_settings` | mcp/tests/test_config.py:89-217 |
| Repository certification profile reference fails closed. | `test_repository_certification_profile_reference_fails_closed` | mcp/tests/test_config.py:219-239 |
| Repository contract path cannot escape coordination root. | `test_repository_contract_path_cannot_escape_coordination_root` | mcp/tests/test_config.py:241-252 |
| Human pinned kind in global file fails boot. | `test_human_pinned_kind_in_global_file_fails_boot` | mcp/tests/test_config.py:283-289 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the certificationProfile parse and fail-closed tests in config tests.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: added `directExecutionEnabled` coverage
  (`parse_direct_execution_enabled` bool requirement; fail-closed default). Verified at code
  commit a9d50e08.


- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 3 citation claims; scoped result 0 findings.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_config.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 21
  line(s) with no token change whatsoever. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: `RetirementSettingsTests` now
  document the current `autoLandOnIntegration`/`autoLandOnFinalize` keys plus compatibility parsing
  for legacy `autoRetireOnIntegration`/`autoRetireOnFinalize` aliases; defaults and fail-loud
  validation stay covered. Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity +
  turn-state): added `RetirementSettingsTests` (6 tests) covering `parse_retirement_settings` —
  both-True defaults, explicit-bool parsing, unknown-key rejection, non-bool-value rejection,
  non-dict rejection, and the `McpRuntimeConfig.retirement` wiring. Verification metadata pinned
  until closeout stamps the HFX-L8 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact: added `ProviderDegradationSettingsTests`
  covering the new `providerDegradation` settings block — defaults, explicit-value round-trip,
  unknown-key rejection, non-object shape rejection, and per-field type rejection. Verification
  metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-06T22:44+02:00 — 260703-L13 (settings unification): OrchestrationSettingsTests
  rewritten for the two-source boot flow (global agentic file + legacy authority fallback,
  warning assertions both ways, new-home fail-loud for loops/roles/concurrency, malformed
  global file); memorySettingsIncludes escape test replaced by the tolerated-ignored test.
  Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): at-seams parse-path consumption test added. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: added
  `OrchestrationSettingsTests` for gate-delegation defaults, named/custom
  policies, reviewer-verdict requirements, and invalid delegation rejection.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-03T11:40+02:00 — 260703 L2: added `DashboardSettingsTests` (defaults-off, happy parse,
  fail-loud unknown key, type/port validation, non-object rejection) and imported
  `McpRuntimeConfig` for the typed `_load` helper. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-07-03T01:55+02:00 — L12 asserts the agents-remember root entry in generated settings carries cgcignorePatterns=[mcp/src/agents_remember/package_data/].
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: config/tool-schema assertions now include `parent_task` and `leaf_id` on resolver/worktree tool signatures so installed MCP metadata matches the new task resolver contract. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-10T05:30+02:00 — Added `LifecycleSettingsDerivationTests`: the settings-generated CGC runner image must equal `cgc_runner_image()` and carry the version-layerrevision suffix (regression for GitHub #50).
- 2026-05-31T12:30+02:00 — Documented the new `timeoutCaps` case rejecting unknown keys with an "unsupported timeout cap" `ConfigError` (1.0.0 review remediation).
- 2026-05-30T21:51+02:00: Documented the new `timeoutCaps` cases — `providerSetupSeconds=0` means unlimited, and the legacy `providerSeconds` key is rejected with the rename message. Verified against `825a172`.
- 2026-05-29T18:35+02:00: Narrowed optional `memory_root`/`contract_path` with `assert ... is not None` before attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after MCP config defaulted transcripts to `logs/mcp` and provider logs to `logs/providers/<provider>/<instance>`.
- 2026-05-26T13:58+02:00: Updated after authority-settings coverage asserted the generated CGC backend Docker network.
- 2026-05-25T17:40+02:00: Updated after authority-settings coverage asserted Docker-owned GrepAI runner, network, Postgres, and Ollama settings.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` moved normal Codex harness fixtures to `.codex`.
- 2026-05-24T09:23+02:00: Updated after harness-root inference tests moved to Codex `.codex/mcp` placement.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for MCP config coverage.
