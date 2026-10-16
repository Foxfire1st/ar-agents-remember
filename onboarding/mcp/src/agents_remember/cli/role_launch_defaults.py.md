# mcp/src/agents_remember/cli/role_launch_defaults.py

## Purpose

Project per-use role settings and exact field provenance into launcher defaults.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

role_defaults resolves the selected repository from context.effective_task, reads user plus optional repository settings per use, and asks resolved_role_knobs for this role’s altitude. It returns agent/spawn fallback, model/effort/tier/mode/features/notes, settings sources, serialized origins and the supplied host-role read.

An optional stepUp is projected from RoleStepUp choices to the public spelling of non-null fields, with afterTries where counted and None when absent. It neither selects the alternative nor counts reviews, validates host offerings, mutates settings or creates a seat.

role_launch_preparation._role_defaults retains its patchable seam and reads the host profile before delegating here. User-only authority and effective no-op refusal remain loader/core responsibilities.

## Evidence

- Repository/altitude defaults and alternative projection are one per-use read. [1]
- Preparation keeps the host-read wrapper. [2]
- Loader validates authority and effective alternative distinctness. [3]
