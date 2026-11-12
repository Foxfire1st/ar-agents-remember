# mcp/src/agents_remember/serving/write_guard.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Refuses the requests a generated page or another site must never get through. The dashboard is local and unauthenticated, which is a deployment posture rather than a write authorization, so a guard sits in front of every route.

## Code Commentary

- `RefuseCrossOriginWrites` refuses a state-changing browser request that is not from the dashboard's own page: `Sec-Fetch-Site` other than `same-origin`, or, with that header absent, a foreign or `null` `Origin`. A refusal answers 403 and never reaches a route.
- A request carrying neither header comes from no browser page, which is why CLI and tool-server calls pass.
- `RefuseForeignHosts` refuses every request, reads included, whose `Host` names another host or port, against DNS rebinding.

- `host_refusal` resolves an omitted ASGI server port from the scheme (`http` 80, `https` 443), as it does an omitted port in the Host header. An explicit bound port must still match; another host or port is refused.

## Evidence

- A state-changing browser request from another page is refused before any route. [1]
- Every request answers only the dashboard's own host and port. [2]
- The origin fallback is consulted only when no Fetch Metadata header was sent. [3]

- An omitted bound port uses the scheme default, while foreign hosts and mismatching explicit ports still refuse. [4]
