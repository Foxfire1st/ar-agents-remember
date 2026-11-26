# mcp/src/agents_remember/serving/explainer_inventory.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

This module projects saved revision inventory and omission metadata into optional serving fields.

## Code Commentary

The manifest route resolves the guarded frame once. A caller with a resolved frame can use the revision reader directly. Only the addressed revision’s stored fields reach the response.

## Relationships

The serving routes own the enclosing response, and the dashboard places the fields beside their corresponding saved frame.

## Evidence

- The inventory view shares a frame lookup and reads the same revision for both fields. [1]
