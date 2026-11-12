# mcp/src/agents_remember/models/base.py

## Governing Overview

[overview](overview.md)

## Purpose and current response contract

The shared Pydantic response primitives distinguish strict package-owned fields from flexible provider/detail payloads. `StrictResponseModel` forbids extras. `FlexibleResponseModel` allows provider extras but recursively refuses the reserved snake_case decision keys in mappings and non-string sequences.

`NextStep` is typed producer/contract guidance, not a session engine: only `summary` is required; operation, tool, arguments and required-argument names are optional. It subclasses the bare strict base, so it has no recursive response hint.

Both response envelopes declare `ok`, token-accounting fields, optional `nextStep`, answer-carried `next`, `log`, `logError` and `buildCurrentness`, the typed loaded-build reading; the tool-answer boundary attaches it to ordinary answers only when an installed server's loaded build is stale, while `server_info` reports its own reading. They dump JSON with absent optional values omitted. The operation-bearing subclasses add `operation`; `ResponseEnvelope` is the union of the strict and flexible envelope families. No notifier/supervisor banner field or ambient-lifecycle installation is declared here. A response key owned by this package must be declared, even on the flexible envelope.

`StaleBuildRefusalResponse` is a strict envelope with `code` and `error`; it validates the shared `server-build-stale` dispatch refusal in place of a writer's own response model, whose success fields differ.

This card records source definitions, not an executed response, test result or code-review grade.

## Evidence

- Strict/flexible bases and recursive reserved-key refusal. [7]

- Typed optional guidance and both current response-envelope families. [8]

- The strict envelope declares the optional build-currentness reading. [9]
- The flexible envelope declares the same reading. [10]
- The stale-build refusal envelope carries only `code` and `error` beside the shared fields. [11]
