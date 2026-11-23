# dashboard/src/cockpit/roleChatModelOptions.test-utils.ts

## Governing Overview

[Dashboard source](../overview.md)

## Purpose

Supplies selected-model response fixtures to launcher tests.

## Code Commentary

The helper looks up the requested provider and model in the local fixture and returns that pair’s features and service tiers with fresh provenance. This keeps fixture metadata and the separate selected-model reply aligned.

## Evidence

- The local response fixture selects exactly the requested pair. [1]
