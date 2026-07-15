# claude_stream_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa`|
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Parses Claude Code's live `list_models` control response into the vendor-neutral capability
snapshot, preserving each installed/auth-visible model's identity, metadata, selectability, and
model-specific effort menu.

## Code Commentary

### Logic

`parse_list_models_response` first validates control-response type, request correlation, success,
and the models array. Each row becomes a `ModelCapability`; `supportsEffort` must agree with the
presence of `supportedEffortLevels`, disabled rows remain catalog evidence but are not selectable,
and duplicate model keys fail. Current selection prefers an exact key, then an unambiguous resolved
model, using the advertised default alias only to disambiguate matching resolved names.

### Conventions

Vendor `value` is the stable normalized key. `resolvedModel` is retained separately as effective
identity evidence. Effort display names intentionally preserve the exact vendor tokens.

### Invariants And Boundaries

- The default path contains no hardcoded model or effort enum.
- Effort options come only from that model's `supportedEffortLevels`; `supportsAutoMode` or other
  adjacent flags do not synthesize an `auto` effort value.
- A current model absent from the live catalog fails loudly instead of selecting a fallback.
- Parsing is pure and owns no subprocess, ACP transport, launch, or session-mutation behavior.

### Todos

None known for L1.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Protocol framing and startup sequencing are separate so catalog parsing remains independently
testable and token-free.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The protocol builds the correlated `list_models` control request. | L64-L69 | [claude_stream_protocol.py](claude_stream_protocol.py) |
| Startup passes the `system/init` current model into this parser before returning the catalog. | L84-L109 | [claude_stream_startup.py](claude_stream_startup.py) |

## Cross-Repo References

No external repository boundary is implemented by this parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: created the one-to-one sidecar for dynamic
  Claude catalog parsing, resolved-current-model validation, disabled rows, and strictly
  model-advertised effort menus. Verification remains empty until closeout stamps the new source.
