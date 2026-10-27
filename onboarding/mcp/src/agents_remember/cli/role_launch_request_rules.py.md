# mcp/src/agents_remember/cli/role_launch_request_rules.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Apply the two request rules a role launch owes before it writes: the caller's own harness, and the warning for requirement files the leaf does not hold.

## Code Commentary

`with_caller_harness` gives the free seat the harness of the chat that made the call, at that harness's default model and effort, unless the call names an agent itself. The identity comes from the MCP client's own name; a client that names nothing, or a harness absent from a known host offering, is refused with the harnesses the host can run instead of being replaced by the first provider listed. A wholly unknown provider inventory preserves the caller’s named harness unchecked. Known offerings match IDs before labels without case. A start that is not the free agent, or that did not come from a chat, is returned unchanged. `missing_copies_receipt_warning` keeps a start succeeding while naming the requirement files the leaf lacks: the receipt — and through it the answer and handover — carries the missing names, either alone or beside a step-up warning. `bridge_http_error` maps a failed bridge call to the route status its code names, and every other bridge failure to a bad gateway.

## Evidence

- The free seat bound to the caller's harness, or refused with the list the host runs. [1]

- The missing-copy warning that keeps the start succeeding. [2]

- A harness the host does not run is refused by name. [3]

- The bridge status mapping the route answers with. [4]
