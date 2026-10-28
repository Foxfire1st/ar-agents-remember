# mcp/src/agents_remember/serving/explainer_comparison.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Comparison selection and the exact pre-build witnesses for the explainer.

## Code Commentary

A comparison is selected and prepared against exact witnesses taken before the build, and a comparison that moved between selection and build is refused rather than published against inputs it was not prepared for.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- PreparedComparisonResult is what a build is handed, with its witnesses. [1]
