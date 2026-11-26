# mcp/tests/test_mik_r196_dashboard_address_truth.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Pins that the answer's dashboard address is published only when something serves it and an unserved origin is reported as a reason instead (L188-B24), and that `chat_address_for` propagates a failed lazy import of `paseo_bridge` instead of masking it while still reporting `PaseoBridgeFailure` as `chatAddressDetail`.

## Code Commentary

Each case monkeypatches the serving daemon's ensure and the address owner's origin probe, then calls the owner's address function for a config with the embed port. An address is answered only after the dashboard owner was asked and the origin answered HTTP 200. When the origin does not answer, the address is absent and the detail names the URL and the owner's outcome, so the answer carries the reason. A raising owner is reported the same way with the exception's name. A 503 page is the origin speaking and not serving, so it is not a continuation; and a failed owner is not published even when the port accepts a connection. Two further cases exercise `owner.chat_address_for` against a minimal `_paseo_config()` stub: removing `agents_remember.cli.paseo_bridge` from `sys.modules` and making `builtins.__import__` raise `ModuleNotFoundError` proves the real `ImportError` surfaces rather than `UnboundLocalError`, while monkeypatching `paseo_bridge.bridge_call` to raise `PaseoBridgeFailure` proves the bridge error is still caught and returned as `{"chatAddress": None, "chatAddressDetail": "daemon offline"}`.

## Invariants And Boundaries

A dead pointer is never published as the address, and the detail always names both what was tried and what came back. The owner is asked before the address is answered, which the recording stub asserts by call. A missing or broken `paseo_bridge` import is never masked behind an `UnboundLocalError` in `chat_address_for`, whereas an expected `PaseoBridgeFailure` still resolves to an absent `chatAddress` with the failure detail.

## Evidence

### Repo-Internal References

- The address is answered only after the owner was asked and the origin answered. [1]
- An unserved origin, a 503 page and a failed owner are reported as reasons, never published as an address. [2]
- `chat_address_for` surfaces a real `ModuleNotFoundError` when lazy-importing `paseo_bridge` fails, and catches `PaseoBridgeFailure` from `bridge_call` as `chatAddressDetail` with `chatAddress: None`. [3]
