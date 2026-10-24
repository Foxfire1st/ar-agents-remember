# mcp/src/agents_remember/cli/role_agent_override.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Decide the launch override one start hands to the selection owner, and bind a model-only free-agent choice to the caller's own harness.

## Code Commentary

`agent_override` keeps the agent, model, effort and feature values a call names. A model or an effort given without the agent it belongs to is refused for every role but the free agent, whose provider is the calling chat's own harness: its override therefore carries no agent id, and the binding supplies the provider the model is validated against. `bound_to_caller_harness` runs on the start path before dispatch prepares anything: it preserves an explicit agent, binds a model- or effort-only choice through the caller-harness owner, and validates the resulting selection against the configured host's catalog, returning the refusal's own sentence so the launch refuses under it. A cold root is the one case it cannot decide — the providers a host offers exist only once it runs — so there the binding and the model check stay where the launch makes them, after preparation, and the first-run report names what that preparation already did.

## Evidence

- The override rule, with the free agent alone admitting a model or effort without an agent. [1]
- The pre-dispatch binding and validation on a configured host. [2]
- Every other role still refuses a model given without its agent. [3]
- Bootstrap overrides are validated before dispatch when a host is configured. [4]
