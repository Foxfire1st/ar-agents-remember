# harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa`|
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
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
honest and belongs to the option set. `LaunchKnobs` carries additive native argv/env/session config;
`SetResult` carries explicit mutation acceptance evidence. Serializer helpers expose stable
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
- This module has no vendor subprocess, session lifecycle, ACP transport, composer-paste, daemon, or
  settings ownership.

### Todos

L2 and L3 implement the declared launch and mutation behavior on each adapter; L1 owns only the
contract and advertise/discover foundation.

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
| The protocol, discovery, and progressive capability ports consume `CapabilitySnapshot`, `LaunchKnobs`, and `SetResult`. | L31-L67 | [harness_control_adapter.py](harness_control_adapter.py) |
| Claude, Codex, and Pi expose cached running capabilities and transient native discovery. | L145-L159 | [harness_control_claude.py](harness_control_claude.py) |
| Codex delegates discover/advertise to its retained session catalog. | L119-L126 | [codex_app_server_adapter.py](codex_app_server_adapter.py) |
| Pi discovers with state/catalog only and revalidates current state for advertise. | L137-L156 | [pi_rpc_adapter.py](pi_rpc_adapter.py) |

## Cross-Repo References

No external repository or ACP transport dependency is implemented by the normalized type layer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: created the normalized capability sidecar for
  model-local effort, ACP Sense 1 select projection, selected-hidden-model honesty, additive launch
  knobs, and the exact mutation-acceptance vocabulary. Verification remains empty until closeout
  stamps the new source.
