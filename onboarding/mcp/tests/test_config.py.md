# test_config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_config.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_config.py` verifies MCP authority settings parsing and derived runtime
paths.

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
shared CGC Docker network.

### Invariants And Boundaries

These tests protect the MCP authority boundary: settings live outside the
coordinator, path-rich provider settings are not duplicated, caller-provided
include paths cannot escape configured repo/memory roots, and derived provider
lifecycle settings remain server-owned instead of host-specific user setup.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tested loader lives in MCP config. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Generated lifecycle settings define the Docker-owned GrepAI and CodeGraphContext stacks consumed by provider lifecycle code. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-05-29T18:35+02:00: Narrowed optional `memory_root`/`contract_path` with `assert ... is not None` before attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-28T12:32+02:00: Updated after MCP config defaulted transcripts to `logs/mcp` and provider logs to `logs/providers/<provider>/<instance>`.
- 2026-05-26T13:58+02:00: Updated after authority-settings coverage asserted the generated CGC backend Docker network.
- 2026-05-25T17:40+02:00: Updated after authority-settings coverage asserted Docker-owned GrepAI runner, network, Postgres, and Ollama settings.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` moved normal Codex harness fixtures to `.codex`.
- 2026-05-24T09:23+02:00: Updated after harness-root inference tests moved to Codex `.codex/mcp` placement.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for MCP config coverage.
