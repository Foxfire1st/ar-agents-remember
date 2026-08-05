# claude_stream_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Protocol framing and startup sequencing are separate so catalog parsing remains independently
testable and token-free.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol builds the correlated `list_models` control request. | `list_models` | mcp/src/agents_remember/serving/claude_stream_protocol.py:156-160 |
| Startup passes the `system/init` current model into this parser before returning the catalog. | `_negotiate`; `negotiate_claude_catalog`; `parse_list_models_response` | mcp/src/agents_remember/serving/harness_control_claude.py:176-223; mcp/src/agents_remember/serving/claude_stream_startup.py:84-111; mcp/src/agents_remember/serving/claude_stream_capabilities.py:15-32 |

## Cross-Repo References

No external repository boundary is implemented by this parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: widened the correlated list-model request input so the fixer retains the complete protocol construction span.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/claude_stream_capabilities.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s), touching only redundant
  grouping parentheses. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R2 — `_select_current_model` gains a
  `requested_key` parameter so a requested alias whose `resolved_model` matches the echoed resolution
  wins the selection tie instead of collapsing onto the `is_default` alias. This is the parser seam of
  the claude `opus[1m]` refused-pair fix (`opus[1m]` and `default` share
  `resolved_model=claude-opus-4-8[1m]`); `harness_control_claude`/`claude_stream_startup` thread the
  requested key in. Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: created the one-to-one sidecar for dynamic
  Claude catalog parsing, resolved-current-model validation, disabled rows, and strictly
  model-advertised effort menus. Verification remains empty until closeout stamps the new source.
