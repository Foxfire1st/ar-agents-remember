# mcp/src/agents_remember/kernel/memory_ignore.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

Prepares the tracked briefs ignore rule and checks that Git excludes the derived folder.

## Code Commentary

A writer's preparation recognizes equivalent declarations, preserves the other ignore text and uses an atomic write when the rule is absent. Brief publication requires both a declared rule in the root ignore file and effective Git exclusion of the whole directory.

## Evidence


- The publication check verifies the root declaration and asks Git whether it excludes the directory. [2]
- The helper adds the canonical ignore rule once and retains the existing text. [1]
