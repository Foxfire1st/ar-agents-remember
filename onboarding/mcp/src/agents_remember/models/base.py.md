# mcp/src/agents_remember/models/base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/base.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-27T18:43+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`base.py` defines the shared Pydantic primitives for modeled MCP responses.

## Code Commentary

`StrictResponseModel` forbids unknown fields for owned public contracts.
`FlexibleResponseModel` intentionally allows unknown fields for native/detail
payloads that must preserve provider or service output. `ResponseModel` and
`ToolResponse` add the shared `ok`, `tokens`, `tokenizer`, and
`tokenCountExact` fields plus JSON-compatible `to_payload()` serialization.
`FlexibleResponseEnvelope` and `FlexibleToolResponse` carry the same envelope
fields on the flexible (`extra="allow"`) base.

`NextStep` (task 27) is the lifecycle next-step hint: a strict model
(`StrictResponseModel` subclass) carrying a required `summary` plus optional
`nextOperation` / `nextTool` / `nextArgs` (`dict[str, Any]`) /
`nextRequiredArgs` (`list[str]`). It mirrors the worktree
`guidance.lifecycle_guidance` dict shape, so operational hints and gate-raise
hints share one vocabulary — a gate junction is just
`nextTool="lifecycle_gate"` with `nextArgs={"kind": ...}`. It is defined before
`ResponseModel` and subclasses the bare `StrictResponseModel` (NOT
`ResponseModel`), so it has no recursive `nextStep` field. Both envelope bases —
`ResponseModel` (strict) and `FlexibleResponseEnvelope` (flexible) — gain an
optional `nextStep: NextStep | None = None` field, so every modeled tool
response can carry the hint. It is populated at the
`mcp/tools/base.py::_tool_payload` choke point (via `next_step_for` from
`mcp.tools.next_step`) and dropped when `None` by `to_payload`'s
`exclude_none=True`, leaving lifecycle-less calls unchanged.

## Invariants And Boundaries

- Default to strict response models for public contracts.
- Use flexible envelopes only for intentionally raw/detail payloads.
- Token fields are part of the contract even before S6 calculates them from
  final serialized output.
- `NextStep` is strict (a real contract); only `summary` is required because
  the non-linear front half of a lifecycle carries prose-only hints.
- `nextStep` is optional on both envelopes and excluded when `None`; it is set
  only at the `_tool_payload` choke point, never by individual tool models.
- `NextStep` must subclass the bare `StrictResponseModel`, not `ResponseModel`,
  to avoid a recursive `nextStep` field.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Token serialization helpers consume `ToolResponse` instances. | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| Public tool payloads validate through concrete subclasses. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| The next-step engine that computes `NextStep` for an active lifecycle. | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| `_tool_payload` choke point that attaches `nextStep` to every in-lifecycle response. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |

## Update History

- 2026-06-27T18:43+02:00: Added the `NextStep` model (lifecycle next-step hint mirroring `guidance.lifecycle_guidance`; strict, `summary` + optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`) and an optional `nextStep` field on both `ResponseModel` and `FlexibleResponseEnvelope`, populated at `mcp/tools/base.py::_tool_payload` and excluded when `None` (task 27).
- 2026-05-28T19:52+02:00: Created for the shared Pydantic response primitives added during the response-contract work.
