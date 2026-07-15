# harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585`|
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the normalized own-adapter capability vocabulary shared by Claude stream-json, Codex
app-server, and Pi RPC. It carries live model catalogs with model-local effort choices, projects the
ACP Sense 1 category-keyed select shape without ACP transport, and establishes launch/set result
types for later leaves.

## Code Commentary

### Logic

`ModelCapability` nests `EffortOption` rows under one model and retains optional resolved identity,
description, default, visibility, selectability, and provider facts. `CapabilitySnapshot` carries the
catalog and current selection. Its config projection emits a `model` select only when the current
model is known and a `thought_level` select only when current effort is known. The selected model is
always retained in model options—even if hidden or no longer selectable—so `currentValue` remains
honest and belongs to the option set. `LaunchKnobs` carries additive native argv/env/session config
plus the argv options and config keys exclusively owned by that adapter. The launch boundary uses
those ownership declarations to reject a competing free-form selector instead of silently choosing
one. `SetResult` carries explicit mutation acceptance evidence. Serializer helpers expose stable
camel-case serving shapes.

### Conventions

Normalized keys preserve vendor tokens rather than inventing aliases. ACP-inspired config ids and
categories use `model` and `thought_level`; this is shape adoption only. Config `currentValue` is
always a string when a select is emitted.

### Invariants And Boundaries

- Effort is model-gated; there is no global effort list or hardcoded default catalog path.
- The only set acceptance values are `echo-verified`, `immediate`, `queued`, `unknown`, and
  `unsupported`; callers must not fabricate success.
- Unknown current model/effort values are omitted from the ACP-style projection rather than guessed.
- Adapter-owned launch selectors are explicit data; callers must conflict-check them before native
  discovery or startup rather than relying on argument order.
- This module has no vendor subprocess, session lifecycle, ACP transport, composer-paste, daemon, or
  settings ownership.

### Todos

L3 implements the remaining mutation methods; L2 now consumes `LaunchKnobs` for native initial
configuration.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The adapter boundary consumes these data types, and each native adapter exposes cached advertise
plus transient discovery through that boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The protocol, discovery, and launchable adapter ports consume `CapabilitySnapshot`, `LaunchKnobs`, and `SetResult`. | L31-L76 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The launch boundary consumes owned selectors before token-free discovery and runtime construction. | L149-L182 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| Claude produces native model/effort flags. | L188-L202 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Codex declares session config plus owned CLI/config selectors. | L128-L146 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| Pi declares provider-qualified model and thinking flags. | L181-L191 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |

## Cross-Repo References

No external repository or ACP transport dependency is implemented by the normalized type layer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented adapter-owned argv/config selectors
  on `LaunchKnobs` and the fail-loud duplicate-authority contract they enable.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: created the normalized capability sidecar for
  model-local effort, ACP Sense 1 select projection, selected-hidden-model honesty, additive launch
  knobs, and the exact mutation-acceptance vocabulary. Verification remains empty until closeout
  stamps the new source.
