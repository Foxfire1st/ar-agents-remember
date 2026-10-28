# mcp/test_support/agents_remember_test_support/testing/prepared_comparison.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

An explicit comparison witness for tests whose native producer is an injected fixture.

## Code Commentary

The fixture-backed preparation states its witness explicitly instead of standing in for a native producer silently, so a test that uses it cannot be read as a test of the native path.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- FixturePreparation states the witness a fixture-backed test is prepared under. [1]
