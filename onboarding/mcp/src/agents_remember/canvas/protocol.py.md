# mcp/src/agents_remember/canvas/protocol.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The narrow host protocol one admitted page speaks: one registered version, a closed operation set, and an envelope every request carries. It validates a request against the session's binding before the host acts.

## Code Commentary

- `parse_frame_message` refuses by name from `REFUSAL_REASONS` those a parser can see — malformed, oversized, wrong-version, unknown-op, foreign-session, stale-revision and foreign-comparison; the rest belong elsewhere: `RequestLedger.admit` refuses `replayed`, `rate-limited` and `exhausted` after `charge` took the token, and the session refuses `revoked`, while `wrong-window` is the panel's own.
- `RequestLedger.charge` debits the session's rate before the caller parses, so refusal work is bounded as well as effects.
- The five frame operations are `ready`, `status`, `open-evidence`, `request-explanation` and `offer-selections`, each with a bounded payload; no operation names a command, route, path or URL. An offer contains at most twelve exact question/choice rows; it offers confirmed text to the trusted tray and starts no turn.
- The host may initiate only `stale-parts`, bound to this session, revision and comparison. Its payload carries at most thirty-two admissible part ids and the true total, without claim-basis reasons.

## Evidence

- One protocol version validates an envelope against the session's binding before any effect. [1]
- A request is debited from the session's rate before the caller parses it. [2]

- The current implementation extends FRAME_OPS with offer-selections and adds a separately validated host stale-parts operation, so the four-operation account is false. [3]
