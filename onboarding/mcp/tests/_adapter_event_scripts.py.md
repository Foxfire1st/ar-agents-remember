# mcp/tests/_adapter_event_scripts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_adapter_event_scripts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Owns independently specified Codex, Pi, and Claude terminal event scripts replayed through the
real conversation-control composition.

## Code Commentary

### Logic

`AdapterReplayPort` is the minimum caller-scripted surface. Replay helpers emit observed provider
frames, optional transcript entries, idle snapshots, and the already-current operation reference.
The caller chooses the terminal outcome; this module does not derive settlement policy.

### Conventions

Provider vocabulary remains external-spec-derived while product state/snapshot models remain
canonical imports.

### Invariants And Boundaries

- No socket, bridge, catalog, route, or service behavior is duplicated here.
- Event scripts do not decide provider outcomes or product transitions.
- Consumers are exactly the two cataloged control suites.

### Todos

None.

## Docs References

Provider frame provenance is carried by the lifecycle catalog; no separate live documentation
source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The replay port and Codex, Pi, and Claude scripts own only external frames. | `AdapterReplayPort` | mcp/tests/_adapter_event_scripts.py:19-156 |
| The lifecycle catalog identifies this support file as provider-derived and binds it to conversation-provider event conformance with an exact consumer list. | "conversation-provider-event-conformance"; "caller-owned Codex, Pi, and Claude terminal frame scripts" | mcp/tests/evidence-lifecycle.toml:144-161 |
| The real composition remains in the structural control port. | `ControlHarness` | mcp/tests/_control_plane.py:300-383 |

## Cross-Repo References

No sibling repository owns these checked-in replay helpers.

## Update History

- 2026-08-25T01:56+02:00 — Created when provider event scripts were extracted from the structural
  control composition to remove mixed authority.
