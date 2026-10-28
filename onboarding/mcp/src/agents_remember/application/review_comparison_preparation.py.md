# mcp/src/agents_remember/application/review_comparison_preparation.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The native comparison admission shared by the reviewer projection and the explainer build.

## Code Commentary

One admission decides whether a comparison may be prepared, and both the reviewer projection and the explainer build go through it, so the two surfaces cannot disagree about which comparison is current. The witness is captured with the inputs and the packet is served only while it still holds.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- SharedComparisonPreparation is the single admission both surfaces use. [1]

- ComparisonInputWitness is the currentness witness a prepared comparison is served under. [2]
