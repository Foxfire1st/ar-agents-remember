# mcp/src/agents_remember/models/base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/base.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:05+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`base.py` defines the shared Pydantic primitives for modeled MCP responses.

## Code Commentary

`StrictResponseModel` (L10-L13) forbids unknown fields for owned public
contracts. `FlexibleResponseModel` (L16-L19) intentionally allows unknown fields
for native/detail payloads that must preserve provider or service output.
`ResponseModel` (L41-L60) and `ToolResponse` (L63-L66) add the shared `ok`,
`tokens`, `tokenizer`, and `tokenCountExact` fields plus JSON-compatible
`to_payload()` serialization. `FlexibleResponseEnvelope` (L69-L84) and
`FlexibleToolResponse` (L87-L90) carry the same envelope fields on the flexible
(`extra="allow"`) base.

`ResponseEnvelope` (L93-L101) is the `TypeAlias` naming the union
`ResponseModel | FlexibleResponseEnvelope` — the two families every registered
tool response belongs to. The strict/flexible split is about `extra`, not about
the envelope: both carry the same `ok`/`tokens`/`nextStep`/`supervisorBanner`
header. Naming the union is what lets `models.tool_registry` declare
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
response can carry the hint (`ResponseModel.nextStep` L51,
`FlexibleResponseEnvelope.nextStep` L77). It is populated at the
`mcp/tools/base.py::_tool_payload` choke point (via `next_step_for` from
`mcp.tools.next_step`, which now returns the MODEL rather than a dump of it) and
dropped when `None` by `exclude_none=True`, leaving lifecycle-less calls
unchanged.

`supervisorBanner: str | None = None` (260707-HFX2-L2 R5) is the second
choke-point field, declared on both envelopes for the same reason `nextStep` is:
`ResponseModel.supervisorBanner` L52-L57, `FlexibleResponseEnvelope.supervisorBanner`
L78-L81. It carries the stale-supervisor one-liner when the supervisor's
heartbeat row has gone quiet past the cutoff, and is absent for a live one. **A
key the choke point writes is a key of THIS envelope.** It was previously
declared nowhere and stamped onto the already-dumped dict, which put the emitted
object outside its own model — a stale supervisor made every response fail its
own `model_validate` — and left the advertised token count short by the whole
`nextStep` object. `mcp/tools/base.py::_attach_lifecycle_tail` (L99-L130) now
sets both fields on the validated response *before* the single `model_dump` in
`_tool_payload` (L132-L148), so `finalize_payload_tokens` counts them. The
flexible envelope declares it too: `extra="allow"` would have accepted it
undeclared, which is exactly the hole — a tolerated-drift surface tolerates the
PROVIDER's fields, not this package's.

## Invariants And Boundaries

- Default to strict response models for public contracts.
- Use flexible envelopes only for intentionally raw/detail payloads.
- Token fields are part of the contract even before S6 calculates them from
  final serialized output.
- `NextStep` is strict (a real contract); only `summary` is required because
  the non-linear front half of a lifecycle carries prose-only hints.
- `nextStep` and `supervisorBanner` are optional on both envelopes and excluded
  when `None`; both are set only at the `_tool_payload` choke point, never by
  individual tool models.
- **What this package writes, this package declares.** A field the choke point
  attaches must be a declared field of the envelope, not a key written into the
  dump. That is what keeps a response inside its own contract and inside its own
  token count; `extra="allow"` on the flexible side is not a substitute.
- `NextStep` must subclass the bare `StrictResponseModel`, not `ResponseModel`,
  to avoid a recursive `nextStep` field.
- `ResponseEnvelope` is the type every entry of `TOOL_RESPONSE_MODELS` must
  satisfy; a new envelope base that is not one of the two families would break
  the registry's annotation, which is the intent.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Token serialization helpers consume `ToolResponse` instances. | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| Public tool payloads validate through concrete subclasses. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| The next-step engine that computes `NextStep` for an active lifecycle; `next_step_for` (L260) returns the model, not a dump. | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| `_attach_lifecycle_tail` (L99-L130) sets `nextStep` + `supervisorBanner` on the validated response; `_tool_payload` (L132-L148) then does the single `model_dump` and token pass. Both are annotated `ResponseEnvelope`. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The registry whose `dict[str, type[ResponseEnvelope]]` annotation (L116, L181) is what `ResponseEnvelope` exists for. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: body corrected. The Code Commentary listed the
  envelope as `ok`/`tokens`/`tokenizer`/`tokenCountExact` + `nextStep` and named no
  `supervisorBanner` — because the field was declared nowhere in the source either: the choke
  point stamped it onto the already-dumped dict, so a stale supervisor produced a response that
  failed its own `model_validate`. Both envelopes now declare `supervisorBanner: str | None = None`
  (`ResponseModel` L52-L57, `FlexibleResponseEnvelope` L78-L81), and `mcp/tools/base.py`'s new
  `_attach_lifecycle_tail` (L99-L130) sets it and `nextStep` on the validated response before the
  single `model_dump` in `_tool_payload` (L132-L148) — which also puts `nextStep` inside
  `finalize_payload_tokens`' count for the first time (`next_step_for` L260 now returns the model,
  not a dump). Recorded the new `ResponseEnvelope: TypeAlias = ResponseModel |
  FlexibleResponseEnvelope` (L93-L101) and why it exists: it is the annotation
  `models.tool_registry` needs so the two choke-point fields are reachable by type. Added the
  "what this package writes, this package declares" invariant and the `ResponseEnvelope`
  invariant. Citations: every class in this file gained a line range (`StrictResponseModel`
  L10-L13, `FlexibleResponseModel` L16-L19, `ResponseModel` L41-L60, `ToolResponse` L63-L66,
  `FlexibleResponseEnvelope` L69-L84, `FlexibleToolResponse` L87-L90, `ResponseEnvelope`
  L93-L101), the `mcp/tools/base.py` reference row was re-pointed from the bare `_tool_payload`
  to `_attach_lifecycle_tail` L99-L130 / `_tool_payload` L132-L148, and a `tool_registry.py`
  L116/L181 row was added. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-27T18:43+02:00: Added the `NextStep` model (lifecycle next-step hint mirroring `guidance.lifecycle_guidance`; strict, `summary` + optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`) and an optional `nextStep` field on both `ResponseModel` and `FlexibleResponseEnvelope`, populated at `mcp/tools/base.py::_tool_payload` and excluded when `None` (task 27).
- 2026-05-28T19:52+02:00: Created for the shared Pydantic response primitives added during the response-contract work.
