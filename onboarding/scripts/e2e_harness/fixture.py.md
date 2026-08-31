# fixture.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/fixture.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T09:45+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Builds the disposable repository, coordination topology, canonical task documents, architect brief,
runtime settings, and Codex/MCP configuration needed for each clean-room replication.

## Code Commentary

### Logic

`create_fixture` lays out isolated code, memory, coordination, Codex-home, and tmux roots. It compiles
the real architect template from canonical doctrine, writes validated task topology and settings,
initializes the disposable Git repository, and points Codex at the deterministic Responses server
plus candidate MCP command. The generated MCP registration explicitly whitelists the dynamic
`TMUX_TMPDIR`, so Codex's stdio child creates role sessions in the same fixture-owned tmux server
used by liveness checks and teardown.

### Conventions

Fixture paths are deliberately short because hosted control uses Unix sockets. Generated values are
explicit inputs to the returned frozen `E2EFixture`; later phases do not rediscover them by scanning.

### Invariants And Boundaries

- The architect brief is compiled from the canonical template, never duplicated as fixture prose.
- The fixture MCP command addresses the candidate checkout and project-owned Python runtime.
- The candidate MCP inherits `TMUX_TMPDIR`; omission would split session creation from the
  fixture's liveness and cleanup namespace.
- Production starter behavior is not rewritten by this test configuration.
- All repositories and ports are run-local and disposable.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture uses repository-owned task and template contracts as its authority. | `create_fixture` | scripts/e2e_harness/fixture.py:43-165 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture construction returns every run-owned path and canonical task address explicitly. | `E2EFixture` | scripts/e2e_harness/fixture.py:28-112 |
| Codex config binds the deterministic Responses endpoint, candidate MCP server, and fixture tmux namespace. | `_write_codex_config` | scripts/e2e_harness/fixture.py:281-326 |

## Cross-Repo References

No live sibling repository supplies fixture behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| Disposable repositories are initialized inside the run root. | `_initialize_repository` | scripts/e2e_harness/fixture.py:181-250 |

## Update History

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: recorded the explicit Codex MCP
  `TMUX_TMPDIR` whitelist that keeps spawned role sessions, liveness probes, and teardown on one
  fixture-owned tmux server. Verification remains closeout-owned.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 created onboarding for the clean-room fixture constructor. Verification metadata remains closeout-owned.
