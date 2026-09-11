# test_install_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_install_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Runtime installation preservation and watcher recovery tests.

## Code Commentary

### Logic

Installing managed assets preserves provider state, database data and central logs while removing obsolete generated runtime assets. Dependency installation failure still attempts watcher restart and status recovery. Existing global settings remain byte-identical; dry run counts a seed without writing it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Temporary fixtures and watcher doubles do not operate live providers. Copy-if-missing settings behavior must not overwrite developer configuration.

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
| Runtime install preserves docker provider state. | `test_runtime_install_preserves_docker_provider_state` | mcp/tests/test_install_runtime.py:55-109 |
| Runtime install provider dependency failure attempts watcher recovery. | `test_runtime_install_provider_dependency_failure_attempts_watcher_recovery` | mcp/tests/test_install_runtime.py:111-161 |
| Existing settings file is never clobbered. | `test_existing_settings_file_is_never_clobbered` | mcp/tests/test_install_runtime.py:167-185 |
| Dry run counts the seed without writing. | `test_dry_run_counts_the_seed_without_writing` | mcp/tests/test_install_runtime.py:187-203 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 7 citation claims; scoped result 0 findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass deleted a keyword this card
  named, so the body was corrected rather than attested. `install_runtime` no longer accepts
  `install_provider_deps=` or `provider_settings=`; both entry points this suite drives now take a
  frozen `ProviderDependencyInstall(settings, timeout, enabled, no_cache)` — `install_runtime` as a
  keyword-only `provider_deps=`, and `install_provider_dependencies_from_settings` in its second
  positional slot with `dry_run` still keyword-only. The `no_cache` paragraph was rewritten
  accordingly: the flag is now a field of that object, not a keyword of the helper, and it still
  defaults to `False` and still reaches both the GrepAI and CGC provider args. Fourteen call sites
  changed, which moved every own-file range in the references table; all seven were recomputed
  against the current source and re-read at their new positions, and a row was added for the
  parameter object itself. While re-anchoring, corrected the Purpose section's
  `AgenticSettingsSeedTests (L13)` to L466 — that anchor was already wrong before this leaf. No
  behaviour moved: the timeout is passed explicitly as 1800 where the old calls relied on the same
  effective budget, `enabled=False` reproduces the former `install_provider_deps=False`, and every
  assertion about preserved runner state, pruned `_bin`/`_venvs`, watcher stop/start ordering,
  dry-run reporting, degraded-status retry and failure recovery is untouched. Verification metadata
  stays pinned until closeout stamps the code commit.

- 2026-07-06T22:50+02:00 — 260703-L13 (settings unification): added
  `AgenticSettingsSeedTests` — seed-when-missing, never-clobber, dry-run-no-write.
  Verification metadata pinned until closeout stamps the L13 commit.

- 2026-06-04T22:15+02:00: Documented the new provider-deps watcher rebind regression coverage: sequencing, dry-run reporting, degraded-status retry, unrecovered recovery action, and dependency-failure recovery.
- 2026-05-30T21:51+02:00: Documented the new `no_cache` threading coverage in `ProviderDependencyHelperTests` — `no_cache=True` reaches both provider args and defaults to `False`. Verified against `8927f03`.
- 2026-05-29T20:25+02:00: Documented the new `ProviderDependencyHelperTests` and `ReadSkillNameTests` coverage added to clear the install helpers' CRAP threshold (`dry_run`-default flip task).
- 2026-05-28T12:32+02:00: Updated after runtime install moved operator logs from `providers/logs/` into the central `logs/` tree and tests asserted the new directories.
- 2026-05-26T12:51+02:00: Updated after runtime install began pruning provider venvs because providers are Docker-owned.
- 2026-05-25T18:07+02:00: Updated after dependency-skipped runtime install began pruning legacy `providers/_bin` while preserving live venv and runner state.
- 2026-05-23T14:20+02:00: Updated after tests switched from the deleted `installer/install-runtime.py` to MCP package-local `agents_remember.install.runtime` and asserted stale coordinator `scripts/` cleanup.
- 2026-05-23T05:32+02:00: Updated after source-installer tests stopped using provider-dependency install switches and asserted provider dependency/runtime roots are preserved.
- 2026-05-23T04:29+02:00: Updated after installer tests moved provider instances under `providers/runners` and asserted default data/log/runner folders.
- 2026-05-21T23:55+02:00: Created after adding the dependency-skipped provider-runtime preservation regression test.
