# claude_stream_capabilities.py

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
and duplicate model keys fail. `_select_current_model` chooses the current selection: it prefers an
exact key match, then — since 260718-CHATS-L5F R2 — the caller-supplied `requested_key` when that
requested alias's `resolved_model` matches the echoed resolution (threaded from
`parse_list_models_response`), then an unambiguous resolved model, using the advertised default alias
only to disambiguate remaining matching resolved names. The requested-key preference stops a
non-default alias whose `resolved_model` equals the default's (e.g. `opus[1m]` and `default` both
resolving to `claude-opus-4-8[1m]`) from silently collapsing onto the `default` key at echo-verify.

### Conventions

Vendor `value` is the stable normalized key. `resolvedModel` is retained separately as effective
identity evidence. Effort display names intentionally preserve the exact vendor tokens.

### Invariants And Boundaries

- The default path contains no hardcoded model or effort enum.
- When several rows share one `resolved_model` and the harness echoes that resolved id, the
  caller's `requested_key` wins the tie (R2) — the selection is not silently reassigned to the
  `is_default` alias, so `verify_effective_launch` compares like-for-like.
- Effort options come only from that model's `supportedEffortLevels`; `supportsAutoMode` or other
  adjacent flags do not synthesize an `auto` effort value.
- A current model absent from the live catalog fails loudly instead of selecting a fallback.
- Parsing is pure and owns no subprocess, ACP transport, launch, or session-mutation behavior.

### Todos

None known for L1.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

Protocol framing and startup sequencing are separate so catalog parsing remains independently
testable and token-free.

- The protocol builds the correlated `list_models` control request. [1]
- Startup passes the `system/init` current model into this parser before returning the catalog. [2]

### Cross-Repo References

No external repository boundary is implemented by this parser.

No meaningful cross-repo references found.
