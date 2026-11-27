# mcp/src/agents_remember/cli/paseo_catalog.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns launcher catalog discovery, host role-profile reads, source-precedence selection resolution and launch choice provenance.

## Code Commentary

The explainer's settings role supplies launch choices, the host profile, settings sources and field origins to the shared role-launch resolver.

A metadata request lists provider and model choices. The panel queries the direct model-options route for the shown pair and keeps its answer in the pane. Start validates its resolved pair when needed. Its operation-local catalog (`launcher_catalog_question`, which also enters `paseo_bridge.launcher_daemon_configuration`) shares metadata, memoizes selected-pair answers, and records the metadata reply's `daemonConfig` / `daemonConfigError` via `record_operation_daemon_config` after `raise_if_read_cancelled()`. The durable store is scoped by `paseo_bridge.paseo_catalog_scope` (install prefix, home, listen and version) and supplies only unanswered parts from their last successful answer. `resolve_agent_selection` resolves each choice by source precedence — explicit start call, host role profile, our settings, host default — while keeping lower choices bound to their authored provider/model: an incompatible lower value is omitted with its source and reason rather than reinterpreted. `read_host_role` reuses `operation_role_profiles` within an active catalog question before falling back to a read-only `role-profiles` bridge call, and formats matches through `role_launch_defaults.host_role_profile`; the first exact role-name match wins and an unreadable catalog falls back to role settings with the reason recorded. `is_role_launch_provider_offered` excludes `NATIVE_ANTIGRAVITY` (`"antigravity"`) from the offered `"agents"` lists of `launcher_options` and `saved_launcher_catalog` as well as `_default_agent` fallback selection, while an explicitly configured `antigravity` default in `launcher_options` surfaces `native_antigravity_role_start_refusal()`. The resolver applies a launcher-chosen mode first, then the applicable host profile's mode and the settings row's mode on its own harness. With no applicable named mode, it uses the host-advertised default when the selected harness's modes are known and the host advertises one. Without an applicable choice the start omits mode. A matching listed name or label resolves to its ID. An unmatched named mode passes through for the host to handle. With unknown offers, the named choice or its absence is preserved. Features resolve per offered host metadata: `service_tier` and `fast_mode` are speed choices a start call may state, while permission-bearing and unknown-bearing values are refused and belong in user settings or the host profile. `serviceTier` stays independent of effort, is revalidated for model overrides, matches offered IDs before labels without case, and is never replaced with a different offered choice. There is no local fast-to-priority alias. `launcher_options` accepts an optional prefetched `catalog` and publishes resolved values with per-choice sources. The request-digest owner removes empty override feature maps before hashing.


The resolver adds `extraArgs` to the launch options only when the selected harness has a nonempty plan.

## Current Contract — Scoped Launch And Settings Changes

launcher_options exposes each role’s configured stepUp alternative. The resolver validates provider, model, effort and selected features against each known catalog part. It resolves mode by the shared host-owned rule. It labels selected authored alternative values with the step-up source and keeps host-default and launcher provenance distinct.

Explicit provider refresh, host-profile discovery, per-choice provider/model binding, omitted lower-choice disclosure, and role-launch provider offering filtering remain with this owner; `paseo_catalog_scope` is imported from `paseo_bridge`. The host’s IDs and labels govern spelling normalization; disk persistence belongs to paseo_catalog_store.

## Evidence

- Launcher options expose metadata, resolved sources and any configured step-up alternative. [6]




- Catalog validation and step-up provenance share the role-start resolver. [7]




- Known mode offers can supply the host's advertised default. An unmatched named mode passes through for the host to handle. [8]



- A cross-model alternative with no mode uses the host default while the base keeps its configured mode. [9]





- The metadata reader shares its answer within an operation. Start validation memoizes selected-pair answers. The direct model-options branch queries its supplied pair and the pane keeps its answer. [1]





- The shared resolver binds each launch choice to its source and the selected harness. [2]





- Provider, model and effort offers govern selection refusals. [3]





- Two independent views request metadata. Start reads metadata and its selected pair, and Refresh requests provider rediscovery. [4]





- Catalog validation rejects disallowed selections. A refused model stops before workspace resolution. [5]




- The explainer's settings role supplies the choices, host profile, settings sources and field origins to the common resolver. [10]

- The mode follows launcher, applicable host profile and matching settings-row precedence. The create request includes a mode only when resolution supplies one. [11]
- The digest excludes an empty feature override map. [12]
