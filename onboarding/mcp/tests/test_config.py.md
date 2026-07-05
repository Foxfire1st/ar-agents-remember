# test_config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_config.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T16:30+02:00 |
| lastVerifiedCommitHash | `19d76dbd73673ffc72d0ee1b6a868ac2fdf15ad0` |
| lastVerifiedCommitDate | 2026-07-05T16:23:40+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_config.py` verifies MCP authority settings parsing and derived runtime
paths, including (L12) that generated CGC roots carry the per-repo managed
cgcignorePatterns for agents-remember.

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
`OrchestrationSettingsTests` (260703-L4) covers `orchestration.gateDelegation`:
defaults to all-human, named manager leaf-gate policy, per-kind
reviewer-verdict requirements, and fail-loud rejection for human-pinned
`push-approval` or unsupported `agent-question` delegation.

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

## Series-Contract Notes

Config/schema tests now assert the public tool surface includes `parent_task` and `leaf_id` where task-name based leaf resolution is supported.

As of the 260703-L8 seam ruling the orchestration settings tests prove the parse path consumes requireReviewerVerdictAtSeams (the delegated handover rule comes back verdict-bound; non-seam rules untouched).

## Update History

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
