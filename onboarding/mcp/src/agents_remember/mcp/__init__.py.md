# mcp/src/agents_remember/mcp/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/__init__.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-12T12:07+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

Defines package-level MCP server identity constants used by public payload
builders.

## Code Commentary

The module exposes `SERVER_NAME` and `SERVER_VERSION`. `SERVER_VERSION` is now
derived from the installed package metadata via
`importlib.metadata.version("agents-remember-mcp")`, making `mcp/pyproject.toml`
the single source of truth; a `PackageNotFoundError` fallback hardcodes the
current release version for source checkouts without an install (bumped in
lockstep with pyproject at every release). Payload builders in `mcp.tools` use
those constants for `ping` and `server_info`, so the version no longer needs a
manual bump here — keep `mcp/pyproject.toml` and the source-checkout fallback in
sync at release.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `ping_payload()` and `server_info_payload()` report `SERVER_VERSION`. | `ping_payload`; `server_info_payload` | mcp/src/agents_remember/mcp/tools/core.py:19-28; mcp/src/agents_remember/mcp/tools/core.py:31-51 |
| Tool tests assert the public version reported by `ping_payload()`. | `test_ping_payload` | mcp/tests/test_tools.py:88-97 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 2 citation claims; scoped recheck clean (0 findings).

- 2026-07-12T12:07+02:00 — No content impact: 260712-TRH-L1 bumps the source-checkout
  `SERVER_VERSION` fallback to 3.0.0rc5 in lockstep with `mcp/pyproject.toml`; installed package
  metadata remains the primary version source and resolution order is unchanged.

- 2026-07-08T15:45+02:00 — No content impact: 260707-HFX2-L7 bumps the source-checkout
  `SERVER_VERSION` fallback to 3.0.0rc4 in lockstep with `mcp/pyproject.toml`; installed package
  metadata remains the primary version source and resolution order is unchanged.
- 2026-07-07T21:10+02:00 — No content impact: release 4922146 bumped the SERVER_VERSION source-checkout fallback to 3.0.0rc3; resolution order unchanged. (Reconciliation: direct owner commit between the L17 and L18 closeouts.)
- 2026-07-03T12:05+02:00 — 260703 L4: SERVER_VERSION fallback bumped to 3.0.0rc2 (resolution order
  unchanged); the body's stale `(now 2.7.0)` parenthetical became version-generic so release bumps
  stop drifting it.
- 2026-07-03T11:20+02:00 — No content impact: L14 bumped the SERVER_VERSION source-checkout fallback to 3.0.0rc1; resolution order unchanged.
- 2026-06-22T22:00+02:00 — No content impact: SERVER_VERSION fallback bumped to 2.9.3 in lockstep with pyproject (worktree_name contract-resolution fix release, #90); the version-resolution contract this sidecar describes is unchanged.
- 2026-06-19T13:42 — No content impact: SERVER_VERSION fallback bumped to 2.9.2 in lockstep with pyproject (benchmark provider isolation release, task 260619); the version-resolution contract this sidecar describes is unchanged.
- 2026-06-12T19:06+02:00 — No content impact: SERVER_VERSION fallback bumped to 2.9.1 in lockstep with pyproject (issue #83 closeout committed-range fix release); the version-resolution contract this sidecar describes is unchanged.
- 2026-06-11T15:20+02:00 — No content impact: SERVER_VERSION fallback bumped to 2.9.0 in lockstep with pyproject (carryover artifact coverage release); the version-resolution contract this sidecar describes is unchanged.
- 2026-06-10T10:26+02:00 — No content impact: SERVER_VERSION fallback bumped to 2.8.0 in lockstep with pyproject (GitHub #54 release); the version-resolution contract this sidecar describes is unchanged.
- 2026-06-10T08:15+02:00 — SERVER_VERSION fallback bumped to 2.7.0 in lockstep with pyproject (GitHub #53/#58 release).
- 2026-06-10T06:25+02:00 — Corrected the fallback version named in the commentary to 2.6.0; the release-bump pass had left the parenthetical at 2.5.2.
- 2026-06-10T06:05+02:00 — No content impact: `SERVER_VERSION` fallback bumped to 2.6.0 in lockstep with `mcp/pyproject.toml` (GitHub #56 release); module behavior unchanged.
- 2026-06-10T05:45+02:00 — `SERVER_VERSION` fallback bumped to 2.5.2 in lockstep with `mcp/pyproject.toml`.
- 2026-06-10T05:30+02:00 — `SERVER_VERSION` fallback bumped to 2.5.1 in lockstep with `mcp/pyproject.toml`.
- 2026-06-09T22:10+02:00 — `SERVER_VERSION` fallback bumped to 2.5.0 in lockstep with `mcp/pyproject.toml`.
- 2026-06-09T15:39+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.4.2` for the L-01 lifecycle skill consolidation patch release; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-08T12:22+02:00: Bumped the source-checkout `SERVER_VERSION` fallback
  to `2.4.1` for the runtime asset sync and provider validation patch release;
  pyproject remains the single source of truth. Verification metadata pinned
  until closeout.
- 2026-06-08T08:33+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.4.0` for the harness-local starter renderer and Python hook command rendering release; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-04T23:15+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.3` for the provider watcher rebind and Docker-safe provider identity patch; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-04T18:52+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.2` for the runtime skill refresh patch; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-03T19:25+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.1` for the MCP package README correction patch; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-03T18:58+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.0` for the harness starter-package / package-first install ergonomics release; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-03T04:25+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.2.0` (mcp 2.2.0 release); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-02T18:35+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.1.0` (mcp 2.1.0 release); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-02T05:10+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.0.0` (mcp 2.0.0 — the `l-01-session-job-lifecycle` skill lifecycle reshape, a major/breaking release); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-02T03:30+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `1.0.2` (mcp 1.0.2); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `1.0.1` (mcp 1.0.1); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-05-31T12:30+02:00 — `SERVER_VERSION` now reads from installed package metadata (`importlib.metadata.version`) with a `1.0.0` source-checkout fallback; pyproject is the single source of truth (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Bumped `SERVER_VERSION` to `0.9.6` (MCP 0.9.6); still aligned with `mcp/pyproject.toml`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped `SERVER_VERSION` to `0.9.5` for the S6 token-counter release; still aligned with `mcp/pyproject.toml`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:33+02:00: Verified `SERVER_VERSION` is `0.9.4` after the 0.9.0–0.9.4 run; still aligned with `mcp/pyproject.toml`. Repaired the broken builder reference — the former single `mcp/tools.py` was split into the `mcp/tools/` package at `01f503d`, so `ping_payload`/`server_info_payload` now live in `tools/core.py`.
- 2026-05-29T21:00+02:00: Bumped `SERVER_VERSION` to `0.3.0` for the MCP `0.3.0` release (the act-by-default `dry_run` flip), kept aligned with `mcp/pyproject.toml`.
- 2026-05-28T15:43+02:00: Created while preparing MCP package release `0.2.0`. Verification metadata remains pinned until closeout commits the source change.
