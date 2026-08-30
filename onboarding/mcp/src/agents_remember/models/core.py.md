# mcp/src/agents_remember/models/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/core.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-30T17:08:05+02:00 |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5` |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`core.py` defines response models for the core `ping` MCP tool and `server_info`
tools.

## Code Commentary

`ServingBuildPayload` is the strict shared runtime identity: version and boot time plus optional
source digest, interpreter, package root, checkout commit, dashboard fingerprint, and proven-dirty
evidence. `PingResponse` reports server identity, version, and transport. `ServerInfoResponse` adds
config, coordination, workspace, transcript, allowed repo/provider, public-tool, reserved-tool
metadata, and that payload under `servingBuild`.

## Invariants And Boundaries

- Transport is currently the literal `stdio`.
- `server_info` should report configured authority and public surface, not
  perform runtime mutation.
- `servingBuild` is required on `server_info`; candidate identity cannot collapse to the package
  version string.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Core payload builders serialize these models. | `ping_payload`; `server_info_payload`; `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/mcp/tools/core.py:19-28; mcp/src/agents_remember/mcp/tools/core.py:31-51; mcp/src/agents_remember/models/tools/tool_registry.py:116-179 |

## Update History

- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: co-located `ServingBuildPayload` with the
  core server response contracts, preserving one model authority without overflowing the flat
  models package. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4: `ServerInfoResponse` now requires the same
  `ServingBuildPayload` used by the serving layer. Verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-04T18:15+02:00 — 260731-EFA-L6 S18-B14 curator: repaired the citation row with exact anchors (`ping_payload`/`server_info_payload`/`TOOL_RESPONSE_MODELS`) and ledger-verified ranges spanning the builders and their registry mapping. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-06-06T12:28+02:00: Corrected the core payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-28T19:52+02:00: Created for core MCP response contracts.
