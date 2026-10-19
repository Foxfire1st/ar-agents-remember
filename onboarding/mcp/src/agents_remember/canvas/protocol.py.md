# mcp/src/agents_remember/canvas/protocol.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The narrow host protocol one admitted page speaks: one registered version, a closed operation set, and an envelope every request carries. It validates a request against the session's binding before the host acts.

## Code Commentary

- `parse_frame_message` refuses by name from `REFUSAL_REASONS` those a parser can see — malformed, oversized, wrong-version, unknown-op, foreign-session, stale-revision and foreign-comparison; the rest belong elsewhere: `RequestLedger.admit` refuses `replayed`, `rate-limited` and `exhausted` after `charge` took the token, and the session refuses `revoked`, while `wrong-window` is the panel's own.
- `RequestLedger.charge` debits the session's rate before the caller parses, so refusal work is bounded as well as effects.
- The four frame operations are `ready`, `status`, `open-evidence` and `request-explanation`, each with a bounded payload; no operation names a command, route, path or URL.

## Evidence

- One protocol version validates an envelope against the session's binding before any effect. [1]
- A request is debited from the session's rate before the caller parses it. [2]
