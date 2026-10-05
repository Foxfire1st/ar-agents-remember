# mcp/src/agents_remember/cli/paseo_catalog.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns launcher catalog discovery, cache identity, defaults projection and selection admission.

## Code Commentary

The cache key is install prefix, home, listen and pin. Only empty cache/explicit refresh discovers; failed discovery never replaces prior cache. Provider/model/effort/tier defaults remain configured even when unavailable and are validated before creation. serviceTier is independent of effort, revalidated for model overrides, maps user fast to native priority, and is never substituted to an offered alternative.

## Evidence

- Frozen implementation of launcher_catalog supporting the stated file behavior. [1]
- Frozen implementation of resolve_agent_selection supporting the stated file behavior. [2]
- Frozen implementation of _tier_refusal supporting the stated file behavior. [3]
- Checks reuse, explicit refresh and changed daemon home in the key. [4]
- Checks rejected choices create no receipt, workspace, agent or enclosure. [5]
