# mcp/tests/test_l192_root_instruction_parameter.py

## Governing Overview

[overview](overview.md)

## Purpose

Refuse instruction advice that calls a `context_packet` parameter the shipped request model does
not admit.

## Code Commentary

`include_providers` is admitted neither by `ContextPacketRequest` nor by the shipped tool schema, so
advice naming it directs an invalid invocation. The case derives the admitted names from the request model rather than from a list
written in the test, then reads every `context_packet(...)` example out of the one named carrier,
the root `AGENTS.md`, skipping it if it does not exist. It fails in both directions: an example naming an unadmitted parameter is an
offender reported as `path:line`, and a scan that found no example at all fails rather than passes.
The carriers' current text is not reproduced here; the card states what the scan requires of any
example it finds. The call pattern is applied per line and stops at the first `)`, so an example
spanning lines is read only up to that point.

## Evidence

- The admitted parameter names are the request model's own fields.
  `test_every_documented_context_packet_call_names_only_admitted_parameters`
- The root `AGENTS.md` is read, a missing file is skipped, and at least one example must be found.
  `test_every_documented_context_packet_call_names_only_admitted_parameters`
