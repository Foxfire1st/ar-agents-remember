# mcp/tests/test_agent_doctrine_plane_identity.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_agent_doctrine_plane_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Machine-enforces the ban on agent instructions that require models to retain or submit
control-plane identifiers, and pins packaged lifecycle doctrine to the canonical source exactly.

## Code Commentary

### Logic

The test enumerates all agent instruction files, rejects forbidden id-addressing phrases, and
compares the packaged lifecycle tree byte-for-byte with the canonical skill tree.

### Conventions

The phrase set is intentionally narrow and architectural; legitimate plane-internal source and
historical provenance are outside this agent-instruction scan.

### Invariants And Boundaries

- Public doctrine cannot regress to exact agent/session/lifecycle targeting.
- Packaged runtime doctrine cannot drift from the canonical source.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests scan canonical instructions and compare packaged copies. | `test_agent_doctrine_contains_no_control_plane_address_instructions` | mcp/tests/test_agent_doctrine_plane_identity.py:37-63 |

## Cross-Repo References


## Update History

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 replaced the temporary findings accumulator with direct per-file assertions; the doctrine and canonical/package identity contract documented above is unchanged.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the public doctrine/runtime-id machine guard.
