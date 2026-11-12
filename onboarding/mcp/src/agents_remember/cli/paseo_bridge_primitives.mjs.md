# mcp/src/agents_remember/cli/paseo_bridge_primitives.mjs

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Share the bridge's literal non-empty-string and daemon-server-identity primitives without introducing a new host command.

## Code Commentary

`nonEmpty` and `serverIdOf` remain the literal string/server-identity helpers. `requiredText`, `optionalText` and `failure` are shared with the workspace owner: absent/null optional text becomes null, non-text is refused, whitespace-only text is empty, and nonempty text is preserved rather than trimmed. Required text refuses an empty result. Typed errors retain their code and `bridgeFailure: true`; extraction introduces no second validation policy or host command.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Shared primitives preserve nonempty text and server identity and now share required/optional text validation and typed bridge errors with the workspace owner. [1]
