# mcp/test_support/agents_remember_test_support/testing/pointer_sentences.py

## Governing Overview

[Overview](overview.md)

## Purpose

Extracts normalized local pointer-action sentences for instruction checks.

## Code Commentary

The helper recognizes local detail placeholders and relative skill targets, excluding external and mail links. It normalizes table cells and action prefixes and suffixes. Extraction is syntactic and grants no action admission.

## Relationships

The pointer planner and policy tests use the extracted actions alongside their separately authored policy.

## Evidence

- Extraction selects local pointer targets and normalizes their action text. [1]
