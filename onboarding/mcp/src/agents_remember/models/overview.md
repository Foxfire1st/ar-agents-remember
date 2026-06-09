# mcp/src/agents_remember/models/ - Response Contract Models Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/models/`          |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-08T09:57+02:00                     |
| lastVerifiedCommitHash | `04f736d5fdaf23002b0e4172b7475a1108da0d9e` |
| lastVerifiedCommitDate | 2026-06-09T22:16:49+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`models/` owns the Pydantic response contracts for public Agents Remember MCP
tools. It turns the public tool surface from loose dictionaries into named,
inspectable models that can be validated at runtime and tested by schema.

## Hot Path Summary

Start with `tool_registry.py`: it maps every `mcp.tools.PUBLIC_TOOLS` entry to
one response model. `base.py` defines strict response envelopes, intentionally
flexible detail envelopes, and token metadata fields. Domain modules then own
contract slices: `context_packet.py` for compact `ContextPacketV2`,
`providers.py` for provider summaries and diagnostics, `worktree.py` for
worktree context/status responses, `memory.py` for memory/onboarding tools,
`runtime.py` for runtime and resolver tools, `benchmarks.py` for Codex
benchmark tools, and `tokens.py` for response token accounting.

## Route Model

- Owned compact contracts should inherit from `StrictResponseModel` or
  `ToolResponse` so unknown fields are rejected.
- Native/detail surfaces that intentionally pass through provider or service
  payloads should inherit from `FlexibleResponseModel` or `FlexibleToolResponse`.
- `ContextPacketV2` keeps startup context compact and points detailed provider
  troubleshooting to `provider_diagnostics`.
- Token metadata fields exist on every modeled response; the final S6 wiring
  fills them from the serialized JSON payload.

## Invariants And Boundaries

- Every public MCP tool must have exactly one declared response model in
  `PUBLIC_TOOL_RESPONSE_MODELS`.
- Do not rely on Pydantic to silently coerce nested raw dictionaries for owned
  contract objects. Construct nested models explicitly, or call
  `NestedModel.model_validate(...)` only at a narrow raw-adapter boundary.
- Keep `context_packet` free of `rawStatus` and duplicate top-level
  `pathRules`; detailed provider state belongs in `provider_diagnostics`.
- Nullable response fields that can be omitted after `exclude_none=True` must
  declare optional defaults (`= None`); otherwise a later public payload
  validation pass treats the missing key as a required-field error.
- Flexible models are for intentionally raw/detail payloads, not a shortcut for
  avoiding a stable public contract.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public MCP payload builders validate through the response model registry. | [mcp/tools/](agents-remember-md/mcp/src/agents_remember/mcp/tools/) |
| The registry maps every public tool name to a response model. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| Contract tests prove public tool coverage and schema generation. | [test_models.py](agents-remember-md/mcp/tests/test_models.py) |

## Update History

- 2026-06-08T09:57+02:00: Re-verified response model guidance after compact provider `ok` fields became optional-null defaults for skipped-provider payload re-validation.
- 2026-06-06T12:15: Re-verified against the current response model package; corrected the payload-builder reference from the deleted `mcp/tools.py` file to the `mcp/tools/` package.
- 2026-05-28T19:52+02:00: Created for the Pydantic public response-contract model package while S2/S4 source changes are still uncommitted in the checkout.
