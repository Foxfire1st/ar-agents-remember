# mcp/src/agents_remember/canvas/explainer_claims.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The explainer's authored claim map, admitted from the captured revision assets.

## Code Commentary

The immutable evidence input stays unchanged: claims are authored output, checked by the existing models and by readiness against that input, and then carried into the published revision. The immutable evidence input stays unchanged. Claims are authored output: the existing models check their shape and readiness checks them against that input, and an admitted map is carried into the published revision rather than rewriting what the page was generated from.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- with_authored_claims carries an admitted claim map into the published revision without touching the evidence input. [1]
