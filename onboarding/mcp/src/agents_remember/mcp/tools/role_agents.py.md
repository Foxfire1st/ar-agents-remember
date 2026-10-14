# mcp/src/agents_remember/mcp/tools/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Builds single-start, leaf-set-start and role-message payloads at the shared response-model/token boundary.

## Code Commentary

Each function forwards the typed call to the existing role tool owner and wraps its dictionary in _tool_payload under the matching public operation name. It adds no recipient resolution, launch authority, polling or compatibility state of its own.

`role_start_payload` and `role_message_payload` keep `call_target_role` set through both the producer call and `_tool_payload` completion; `finally` resets it afterward, including on exceptions. For id addressing the sender owns receipt-derived role resolution. This module does not add a role field to the answer or relocate observer ownership.

A held result supplies its complete mapping as the explicit `answer` override, bypassing the default role row projection; non-held results retain that projection path. Explicit override still crosses validation, logging and the generic delivered-token guard, but is dict-copied rather than passing through the default `truncate_lists` branch; an under-bound held mapping has no common automatic list-cap guarantee. Long held narrative and null/nonscalar values are not guaranteed to survive the short form; the whole detail is the custody surface when retained.

`role_start_set_payload` forwards to the one Manager-owned set entry and crosses `_tool_payload` once under its own operation. A set has three seats, so it supplies no invented single target role to the event context. Each single-role/message response completes inside its own target-role context before that context is reset.

## Evidence

- The start builder brackets its producer and response choke with role context and resets that context afterward. [1]
- Message completion retains the addressed-role context through the choke, with a held-answer override and reset afterward. [2]
