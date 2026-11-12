# mcp/src/agents_remember/canvas/explainer_comparison_inputs.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The inputs one explainer comparison is a function of, and the witness that they are still current.

## Code Commentary

A comparison's inputs are captured together with a native witness that says they are still the ones the tree holds, so a prepared packet cannot be served from inputs that have moved underneath it. The scope, the leaf facts and the bound comparison are the parts a caller supplies; the packet is what readiness checks.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- ComparisonWitness is the currentness witness carried beside the captured inputs. [1]

- PreparedPacket is the bound result readiness checks before an answer is served. [2]
