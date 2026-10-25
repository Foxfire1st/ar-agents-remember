# mcp/src/agents_remember/cli/paseo_catalog.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns launcher catalog discovery, host role-profile reads, source-precedence selection resolution and launch choice provenance.

## Code Commentary

The settings role defaults carry origins/sources, host role and useHostDefaultMode through resolve_agent_selection; this is normal catalog-qualified launch resolution rather than a second explainer-specific model catalog.

The cache key is install prefix, home, listen and pin. Only empty cache/explicit refresh discovers; failed discovery never replaces prior cache. `resolve_agent_selection` resolves each choice by source precedence — explicit start call, host role profile, our settings, host default — while keeping lower choices bound to their authored provider/model: an incompatible lower value is omitted with its source and reason rather than reinterpreted. `read_host_role` reads the running host's profiles through a read-only bridge call; the first exact role-name match wins and an unreadable catalog falls back to role settings with the reason recorded. Mode is never a start-call argument. Ordinary resolution uses host profile, then applicable settings, then the explicit least offered working mode. A selected cross-provider/model step-up with no authored mode instead requests the host defaultModeId; concrete defaults must still be offered, and unknown mode catalogs/values refuse by name. Features resolve per offered host metadata: `service_tier` and `fast_mode` are speed choices a start call may state, while permission-bearing and unknown-bearing values are refused and belong in user settings or the host profile. `serviceTier` stays independent of effort, is revalidated for model overrides, maps user fast to native priority, and is never substituted. `launcher_options` publishes resolved values with per-choice sources, and empty feature maps stay out of old request digests.


**L184 — NEW-R192-EXTRA-ARGS.** This is where the launch record is assembled from the plan, so a plan the start did not build leaves the field out of the record. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Current Contract — Scoped Launch And Settings Changes

launcher_options exposes each role’s configured stepUp alternative. resolve_agent_selection still validates the selected provider/model/effort, mode and offered features before creation, then labels selected user-authored alternative values with the step-up source while leaving host defaults and explicit start-call provenance distinct.

Ordinary no-mode launches keep the existing least offered working mode policy. A cross-provider/model step-up without its own mode passes useHostDefaultMode and takes that host’s defaultModeId instead; any non-null result still must be offered. This is not an unconditional least-mode guarantee and does not transfer another harness’s mode/features or authorize permission-bearing start arguments.

Cache identity, explicit refresh, host-profile discovery, per-choice provider/model binding, omitted lower-choice disclosure and fast-to-priority normalization remain with this owner.

## Evidence

- Options include the configured alternative. [6]

- Host catalog validation and step-up provenance share the existing resolver. [7]

- Host-default-mode path is conditional, and all concrete modes are checked. [8]
- Test source contrasts ordinary auto with step-up host default. [9]

- Frozen implementation of launcher_catalog supporting the stated file behavior. [1]

- Frozen implementation of resolve_agent_selection supporting the stated file behavior. [2]


- Frozen implementation of _selection_refusal supporting the stated file behavior. [3]


- Checks reuse, explicit refresh and changed daemon home in the key. [4]


- Checks rejected choices create no receipt, workspace, agent or enclosure. [5]

- The settings role defaults carry origins/sources, host role and useHostDefaultMode through resolve_agent_selection; this is normal catalog-qualified launch resolution rather than a second explainer-specific model catalog. [10]
