# test_config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_config.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-09T14:05+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009` |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_config.py` verifies MCP authority settings parsing and derived runtime
paths, including (L12) that generated CGC roots carry the per-repo managed
cgcignorePatterns for agents-remember, and (L13) the gateDelegation
boot-sourcing rules: `OrchestrationSettingsTests` drives `load_config` with an
optional authority `orchestration` block AND an optional global agentic file
(`<coordinationRoot>/system/settings.json`) — the global file sources the
policy warning-free, an authority-only value is honored as the legacy fallback
WITH the migration `UserWarning`, a shadowed authority value warns as IGNORED
while the global value wins, `loops`/`roles`/`concurrency` in the authority
file fail loud naming the new home, gate-policy semantic errors (human-pinned)
surface as `ConfigError` from either file, and a malformed global file fails
boot naming the file. `test_legacy_memory_settings_includes_key_is_tolerated_and_ignored`
replaces the old escape-boundary test: the removed dead plumbing means a
leftover `memorySettingsIncludes` key parses fine and `RepositoryScope` no
longer exposes the field.

## Code Commentary

### Logic

The tests create temporary MCP settings files and assert that config loading
rejects relative or missing paths, rejects coordinator `system/settings.json`,
rejects MCP settings inside the coordinator root, derives allowed repo/provider
ids, derives the central `logs/mcp` transcript root and `logs/providers`
provider log roots, infers `.codex/skills` from a `.codex/mcp` registration
path, honors explicit `harnessSkillRoot`, keeps
contract paths inside the coordinator, rejects memory settings includes outside
repo boundaries, and rejects provider path fields that should be server-derived.
The authority-settings test also verifies generated `grepai-memory` lifecycle
settings stay Docker-owned, including Docker mode, shared network, runner image
and container, Postgres backend root, and Ollama embedder backend. It also
checks that generated `codegraphcontext-code` backend settings include the
shared CGC Docker network. New cases cover `timeoutCaps` parsing:
`providerSetupSeconds=0` means unlimited, the legacy `providerSeconds` key is
rejected with a `ConfigError` carrying the "renamed to providerSetupSeconds"
message, and an unknown `timeoutCaps` key is rejected with an "unsupported
timeout cap" `ConfigError`. `DashboardSettingsTests` (260703 L2) covers the
optional `dashboard` object: absent → defaults off (autoStart False, port 8765),
happy parse, unknown-key rejection (`autostart` typo), non-bool `autoStart`
rejection, invalid ports (bool/0/65536/string), and non-object shapes.
`ProviderDegradationSettingsTests` (260707-HFX-L7) covers the optional `providerDegradation`
object: absent → the conservative enabled/failsafe-armed defaults
(`memoryDegradedRatio=0.80`, `memoryCriticalRatio=0.92`); a full explicit-value parse round-trips
all 15 keys; an unknown key (`memoryDegradedRato` typo) raises `ConfigError` naming it; a
non-object shape (a list) raises `ConfigError`; and four representative bad-type cases
(non-bool `enabled`, an out-of-range ratio, a zero sample count, a bool where an int is required)
each raise `ConfigError`.
`OrchestrationSettingsTests` (260703-L4) covers `orchestration.gateDelegation`:
defaults to all-human, named manager leaf-gate policy, per-kind
reviewer-verdict requirements, and fail-loud rejection for human-pinned
`push-approval` or unsupported `agent-question` delegation. `RetirementSettingsTests`
(260707-HFX2-L11, 8 tests) covers `parse_retirement_settings`: defaults are both `True` when the
`retirement` key is absent, explicit `autoLandOnIntegration`/`autoLandOnFinalize`
`False`/`False` parses through, legacy `autoRetireOnIntegration`/`autoRetireOnFinalize` aliases
parse into the new fields for compatibility, an unknown key (`autoRetireOnLaunch`) is rejected with
an "unsupported retirement setting" `ConfigError`, non-bool values for either current or legacy key
shape are rejected with a "must be a boolean" `ConfigError`, and a non-object `retirement` value (a
list) is rejected with a "retirement settings must be an object" `ConfigError`.

### Invariants And Boundaries

These tests protect the MCP authority boundary: settings live outside the
coordinator, path-rich provider settings are not duplicated, caller-provided
include paths cannot escape configured repo/memory roots, and derived provider
lifecycle settings remain server-owned instead of host-specific user setup.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tested loader lives in MCP config. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Generated lifecycle settings define the Docker-owned GrepAI and CodeGraphContext stacks consumed by provider lifecycle code. | [settings.py](agents-remember/mcp/src/agents_remember/providers/settings.py) |
| The `providerDegradation` parser under test (260707-HFX-L7). | [provider_degradation_settings.py](agents-remember/mcp/src/agents_remember/mcp/provider_degradation_settings.py) |

## Series-Contract Notes

Config/schema tests now assert the public tool surface includes `parent_task` and `leaf_id` where task-name based leaf resolution is supported.

As of the 260703-L8 seam ruling the orchestration settings tests prove the parse path consumes requireReviewerVerdictAtSeams (the delegated handover rule comes back verdict-bound; non-seam rules untouched).

## Update History

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
