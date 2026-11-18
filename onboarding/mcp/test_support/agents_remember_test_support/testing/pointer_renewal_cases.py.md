# mcp/test_support/agents_remember_test_support/testing/pointer_renewal_cases.py

## Governing Overview

[Overview](overview.md)

## Purpose

Defines reusable pointer-renewal controls for stable identities, ambiguity and invalid bindings.

## Code Commentary

The cases compare a fresh plan with held wording, reorder actions, change wording and exercise explicit ambiguity decisions. Invalid occurrence, identity, source and competing-binding selections are rejected. Assertions retain authored policy bytes while generated wording changes.

## Relationships

`assert_pointer_wording_is_current` compares a fresh plan with the held derived wording in the real checkout. The binding and ambiguity cases build isolated fixture worlds for their mutations. Source inspection describes these assertions; it is not a test-run result.

## Evidence

- Cases distinguish reorder and wording changes from ambiguous or invalid bindings. [1]
