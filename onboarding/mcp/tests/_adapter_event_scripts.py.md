# mcp/tests/_adapter_event_scripts.py

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

## Evidence

### Docs References

Provider frame provenance is carried by the lifecycle catalog; no separate live documentation
source is configured.

### Repo-Internal References

- The replay port and Codex, Pi, and Claude scripts own only external frames. [1]
- The lifecycle catalog identifies this support file as provider-derived and binds it to conversation-provider event conformance with an exact consumer list. [2]
- The real composition remains in the structural control port. [3]

### Cross-Repo References

No sibling repository owns these checked-in replay helpers.
