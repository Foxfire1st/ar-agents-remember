# mcp/src/agents_remember/serving/master_preparation.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Event-driven, app-owned preparation of exact master counter generations.

## Code Commentary

Preparation is owned by the app and driven by events for an exact generation, so a page that asks for a generation gets that generation's preparation rather than whatever was being built. A key that no longer matches is not served from the older job.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- MasterPreparation runs one job per exact key and does not serve another key's result. [1]
