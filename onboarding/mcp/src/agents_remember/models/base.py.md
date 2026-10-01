# mcp/src/agents_remember/models/base.py

## Governing Overview

[models overview](overview.md)

## Purpose

`base.py` defines the shared Pydantic primitives for modeled MCP responses.

## Code Commentary

### Logic

cit:([`StrictResponseModel`], mcp/src/agents_remember/models/base.py:13-16) forbids unknown fields for owned public
contracts. cit:([`FlexibleResponseModel`], mcp/src/agents_remember/models/base.py:19-30) intentionally allows unknown fields
for native/detail payloads that must preserve provider or service output. Its before-validator
recursively rejects the reserved snake_case lifecycle decision keys, retaining the single
camelCase decision vocabulary even inside flexible nested payloads.
cit:([`ResponseModel`], mcp/src/agents_remember/models/base.py:66-88) and cit:([`ToolResponse`], mcp/src/agents_remember/models/base.py:91-94) add the shared `ok`,
`tokens`, `tokenizer`, and `tokenCountExact` fields plus JSON-compatible
`to_payload()` serialization. cit:([`FlexibleResponseEnvelope`], mcp/src/agents_remember/models/base.py:97-114) and
cit:([`FlexibleToolResponse`], mcp/src/agents_remember/models/base.py:117-120) carry the same envelope fields on the flexible
(`extra="allow"`) base.

cit:([`ResponseEnvelope`], mcp/src/agents_remember/models/base.py:123-123) is the PEP 695 type alias naming the union
`ResponseModel | FlexibleResponseEnvelope` — the two families every registered
tool response belongs to. The strict/flexible split is about `extra`, not about
the envelope: both carry the same `ok`/`tokens`/`nextStep`/`agentNotifierBanner`
header. Naming the union is what lets `models.tools.tool_registry` declare
`dict[str, type[ResponseEnvelope]]` instead of `dict[str, type[BaseModel]]`, and
that in turn is what makes the two choke-point fields reachable by type from
`_tool_payload`.

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
response can carry the hint. The application boundary preserves an explicit producer
`nextStep`; otherwise it calls `next_step_for`, which returns the model rather than a dump.
`bound_next_step` then omits guidance whose task address contradicts the response's exact
contract/enclosure address. A `None` field is dropped by `exclude_none=True`.

`agentNotifierBanner: str | None = None` (260707-HFX2-L2 R5, renamed from `supervisorBanner` in
260713-TES-L1) is the second
choke-point field, declared on both envelopes for the same reason `nextStep` is:
cit:([`ResponseModel`, `FlexibleResponseEnvelope`], mcp/src/agents_remember/models/base.py:66-88; mcp/src/agents_remember/models/base.py:97-114).
During the rename window each envelope ALSO declares the legacy `supervisorBanner: str | None =
None` alias and `_attach_lifecycle_tail` writes both keys with the same value; the legacy field is
removed with the window. The field carries the stale-agent-notifier one-liner when the agent-notifier's
heartbeat row has gone quiet past the cutoff, and is absent for a live one. **A
key the choke point writes is a key of THIS envelope.** It was previously
declared nowhere and stamped onto the already-dumped dict, which put the emitted
object outside its own model — a stale supervisor made every response fail its
own `model_validate` — and left the advertised token count short by the whole
`nextStep` object. cit:([`complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:131-145)
sets both fields on the validated response *before* cit:([`finalize_tool_response`], mcp/src/agents_remember/models/tools/tool_response.py:15-26)
performs the single model dump and token pass, so `finalize_payload_tokens` counts them. The
flexible envelope declares it too: `extra="allow"` would have accepted it
undeclared, which is exactly the hole — a tolerated-drift surface tolerates the
PROVIDER's fields, not this package's.

### Conventions

Use the strict family for owned response vocabulary and the flexible family only for provider or
service detail. Both share declared lifecycle fields and the same serialization boundary.

### Invariants And Boundaries

- Default to strict response models for public contracts.
- Use flexible envelopes only for intentionally raw/detail payloads.
- Token fields are part of the contract even before S6 calculates them from
  final serialized output.
- `NextStep` is strict (a real contract); only `summary` is required because
  the non-linear front half of a lifecycle carries prose-only hints.
- `nextStep` and `agentNotifierBanner` (plus the legacy `supervisorBanner` alias during the
  rename window) are optional on both envelopes and excluded
  when `None`. The response boundary attaches the banner; a producer may supply an explicit
  recovery `nextStep`, which takes precedence over ambient guidance after address checking.
- **What this package writes, this package declares.** A field the choke point
  attaches must be a declared field of the envelope, not a key written into the
  dump. That is what keeps a response inside its own contract and inside its own
  token count; `extra="allow"` on the flexible side is not a substitute.
- `NextStep` must subclass the bare `StrictResponseModel`, not `ResponseModel`,
  to avoid a recursive `nextStep` field.
- `ResponseEnvelope` is the type every entry of `TOOL_RESPONSE_MODELS` must
  satisfy; a new envelope base that is not one of the two families would break
  the registry's annotation, which is the intent.

### Todos

No task-independent follow-up was identified in the reviewed response-envelope behavior.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

Current envelope behavior is established by the repository source.

### Repo-Internal References

- Token serialization helpers accept the shared `ResponseModel` family, including concrete tool-response subclasses. [1]
- Public tool payloads validate through concrete subclasses. [2]
- The next-step engine that computes `NextStep` for an active lifecycle; `next_step_for` returns the model, not a dump. [3]
- The application boundary preserves a producer recovery hint or computes one, rejects contradictory task addresses, writes both banner names, and finalizes once. [4]
- The registry whose `dict[str, type[ResponseEnvelope]]` annotation is what `ResponseEnvelope` exists for. [5]

### Cross-Repo References

No cross-repository implementation boundary is owned by these response primitives.

No applicable cross-repository source was found.

## 260821-CLIVE-L2 Current Contract

The current source seams include `StrictResponseModel`, `FlexibleResponseModel`, and `NextStep`.
Strict responses forbid unknown fields; flexible responses retain provider detail while recursively
rejecting reserved snake_case decision keys. This module declares response shapes and token fields;
it does not locate journals or authorize mutation.

### Reconciled Source Evidence

- The current module exposes `StrictResponseModel`, `FlexibleResponseModel`, `NextStep` at this ownership boundary. [6]
