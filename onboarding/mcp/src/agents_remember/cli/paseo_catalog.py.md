# mcp/src/agents_remember/cli/paseo_catalog.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns launcher catalog discovery, host role-profile reads, source-precedence selection resolution and launch choice provenance.

## Code Commentary

The cache key is install prefix, home, listen and pin. Only empty cache/explicit refresh discovers; failed discovery never replaces prior cache. `resolve_agent_selection` resolves each choice by source precedence — explicit start call, host role profile, our settings, host default — while keeping lower choices bound to their authored provider/model: an incompatible lower value is omitted with its source and reason rather than reinterpreted. `read_host_role` reads the running host's profiles through a read-only bridge call; the first exact role-name match wins and an unreadable catalog falls back to role settings with the reason recorded. Mode is never a start-call argument: resolution uses host profile, then our settings, then the explicit least offered working mode, and refuses unknown mode offerings by name. Features resolve per offered host metadata: `service_tier` and `fast_mode` are speed choices a start call may state, while permission-bearing and unknown-bearing values are refused and belong in user settings or the host profile. `serviceTier` stays independent of effort, is revalidated for model overrides, maps user fast to native priority, and is never substituted. `launcher_options` publishes resolved values with per-choice sources, and empty feature maps stay out of old request digests.

## Evidence

- Frozen implementation of launcher_catalog supporting the stated file behavior. [1]
- Frozen implementation of resolve_agent_selection supporting the stated file behavior. [2]
- Frozen implementation of _tier_refusal supporting the stated file behavior. [3]
- Checks reuse, explicit refresh and changed daemon home in the key. [4]
- Checks rejected choices create no receipt, workspace, agent or enclosure. [5]
