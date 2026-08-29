# mcp/src/agents_remember/models/base.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/base.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-29T17:23+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[models overview](overview.md)

## Purpose

`base.py` defines the shared Pydantic primitives for modeled MCP responses.

## Code Commentary

cit:([`StrictResponseModel`], mcp/src/agents_remember/models/base.py:10-13) forbids unknown fields for owned public
contracts. cit:([`FlexibleResponseModel`], mcp/src/agents_remember/models/base.py:16-19) intentionally allows unknown fields
for native/detail payloads that must preserve provider or service output.
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
response can carry the hint (`ResponseModel.nextStep` L51,
`FlexibleResponseEnvelope.nextStep` L77). It is populated at the
`mcp/tools/base.py::_tool_payload` choke point (via `next_step_for` from
`application.next_step`, which returns the model rather than a dump of it) and
dropped when `None` by `exclude_none=True`, leaving lifecycle-less calls
unchanged.

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
`nextStep` object. cit:([`complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:49-61)
sets both fields on the validated response *before* cit:([`finalize_tool_response`], mcp/src/agents_remember/models/tools/tool_response.py:15-26)
performs the single model dump and token pass, so `finalize_payload_tokens` counts them. The
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
- `nextStep` and `agentNotifierBanner` (plus the legacy `supervisorBanner` alias during the
  rename window) are optional on both envelopes and excluded
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Token serialization helpers accept the shared `ResponseModel` family, including concrete tool-response subclasses. | `ResponseModel` | mcp/src/agents_remember/models/tokens.py:18-18 |
| Public tool payloads validate through concrete subclasses. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:148-227 |
| The next-step engine that computes `NextStep` for an active lifecycle; `next_step_for` returns the model, not a dump. | `next_step_for` | mcp/src/agents_remember/application/next_step.py:260-281 |
| The application response boundary completes the validated response after attaching lifecycle-wide fields (writing both `agentNotifierBanner` and the legacy `supervisorBanner`) and finalizing its payload. | `complete_tool_response` | mcp/src/agents_remember/application/tool_response.py:53-67 |
| The registry whose `dict[str, type[ResponseEnvelope]]` annotation is what `ResponseEnvelope` exists for. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:148-227 |

## 260821-CLIVE-L2 Current Contract

The current source seams include `StrictResponseModel`, `FlexibleResponseModel`, `NextStep`. The model change keeps public vocabulary closed and validates nonblank identity/evidence fields. Models describe state but do not locate journals, authorize mutation, or supply compatibility fallbacks.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `StrictResponseModel`, `FlexibleResponseModel`, `NextStep` at this ownership boundary. | `StrictResponseModel`; `FlexibleResponseModel`; `NextStep` | mcp/src/agents_remember/models/base.py:13-16; mcp/src/agents_remember/models/base.py:19-30; mcp/src/agents_remember/models/base.py:47-63 |

## Update History

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 type-alias syntax migration for `ResponseEnvelope` and confirmed that the strict/flexible response families remain as documented. Verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: recorded the `agentNotifierBanner` rename and
  the legacy `supervisorBanner` alias declared on both envelopes, written by
  `_attach_lifecycle_tail` with the same value during the rename window. Verification metadata
  pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04: corrected the next-step module owner and
  widened the token-serialization claim from `ToolResponse` to the shared `ResponseModel` family.

- 2026-08-02T20:43+02:00 — W2-B08: converted 5 model-base prose citations to current `cit:` form, anchored 4 reference claims, and repointed the next-step and response-boundary references to their current application/model modules; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: body corrected. The Code Commentary listed the
  envelope as `ok`/`tokens`/`tokenizer`/`tokenCountExact` + `nextStep` and named no
  `supervisorBanner` — because the field was declared nowhere in the source either: the choke
  point stamped it onto the already-dumped dict, so a stale supervisor produced a response that
  failed its own `model_validate`. Both envelopes now declare `supervisorBanner: str | None = None`
  cit:([`ResponseModel`, `FlexibleResponseEnvelope`], mcp/src/agents_remember/models/base.py:66-88; mcp/src/agents_remember/models/base.py:97-114), and the application response boundary's
  cit:([`_attach_lifecycle_tail`, `complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:34-44; mcp/src/agents_remember/application/tool_response.py:47-61)
  sets it and `nextStep` on the validated response before the single model dump — which also puts
  `nextStep` inside the token count for the first time (cit:([`next_step_for`], mcp/src/agents_remember/application/next_step.py:260-281) now returns the model,
  not a dump). Recorded the new `ResponseEnvelope: TypeAlias = ResponseModel |
  FlexibleResponseEnvelope` cit:(["type ResponseEnvelope = ResponseModel | FlexibleResponseEnvelope"], mcp/src/agents_remember/models/base.py:123-123) and why it exists: it is the annotation
  `models.tool_registry` needs so the two choke-point fields are reachable by type. Added the
  "what this package writes" invariant and the `ResponseEnvelope`
  invariant. Citations: every class in this file gained a line range
  cit:([`StrictResponseModel`, `FlexibleResponseModel`, `ResponseModel`, `ToolResponse`, `FlexibleResponseEnvelope`, `FlexibleToolResponse`, `ResponseEnvelope`], mcp/src/agents_remember/models/base.py:13-16; mcp/src/agents_remember/models/base.py:19-30; mcp/src/agents_remember/models/base.py:66-88; mcp/src/agents_remember/models/base.py:91-94; mcp/src/agents_remember/models/base.py:97-114; mcp/src/agents_remember/models/base.py:117-120; mcp/src/agents_remember/models/base.py:123-123), the response-boundary reference row was re-pointed to
  cit:([`_attach_lifecycle_tail`, `complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:34-44; mcp/src/agents_remember/application/tool_response.py:47-61), and the registry row was added with
  cit:([`TOOL_RESPONSE_MODELS`], mcp/src/agents_remember/models/tools/tool_registry.py:149-229). Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-27T18:43+02:00: Added the `NextStep` model (lifecycle next-step hint mirroring `guidance.lifecycle_guidance`; strict, `summary` + optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`) and an optional `nextStep` field on both `ResponseModel` and `FlexibleResponseEnvelope`, populated at the application response boundary (cit:([`complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:47-61)) and excluded when `None` (task 27).
- 2026-05-28T19:52+02:00: Created for the shared Pydantic response primitives added during the response-contract work.
