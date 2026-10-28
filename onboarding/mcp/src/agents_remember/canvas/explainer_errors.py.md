# mcp/src/agents_remember/canvas/explainer_errors.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer's named refusals, kept in a module that imports no workspace or durable state.

## Code Commentary

The explainer refuses by name rather than by a generic failure, and the refusal types live in their own module so that naming a refusal does not pull in the workspace or the durable state. That is what lets a caller distinguish a refusal from a fault without reading the implementation that raised it.

## Boundaries

This module bounds or names; it does not serve a page, publish a revision or read the workspace back.

## Evidence

- ExplainerRefused is the named refusal a caller can distinguish from a fault. [1]

- ExplainerStateError names a durable-state failure separately from a refusal. [2]
