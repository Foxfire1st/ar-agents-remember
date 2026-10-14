# mcp/src/agents_remember/mcp/tools/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Builds single-start, leaf-set-start, role-message and native seat-retirement payloads at the shared response-model/token boundary.

## Code Commentary

Each function forwards the typed call to the existing role tool owner and wraps its dictionary in _tool_payload under the matching public operation name. It adds no recipient resolution, launch authority, polling or compatibility state of its own.

`role_start_payload` and `role_message_payload` keep `call_target_role` set through both the producer call and `_tool_payload` completion; `finally` resets it afterward, including on exceptions. For id addressing the sender owns receipt-derived role resolution. This module does not add a role field to the answer or relocate observer ownership.

A held result supplies its complete mapping as the explicit `answer` override, bypassing the default role row projection; non-held results retain that projection path. Explicit override still crosses validation, logging and the generic delivered-token guard, but is dict-copied rather than passing through the default `truncate_lists` branch; an under-bound held mapping has no common automatic list-cap guarantee. Long held narrative and null/nonscalar values are not guaranteed to survive the short form; the whole detail is the custody surface when retained.

`role_start_set_payload` forwards to the one Manager-owned set entry and crosses `_tool_payload` once under its own operation. A set has three seats, so it supplies no invented single target role to the event context. Each single-role/message response completes inside its own target-role context before that context is reset.

retire_child_payload calls the existing retire_native_seat owner with the typed request and optional environment override, then wraps its answer under retire_child. It introduces no second retirement store or caller authority.

## Evidence

- The start builder brackets its producer and response choke with role context and resets that context afterward. [1]
- Message completion retains the addressed-role context through the choke, with a held-answer override and reset afterward. [2]

- Native retirement delegates to the existing receipt owner and wraps its answer under retire_child. [3]
