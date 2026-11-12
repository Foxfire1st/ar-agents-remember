# dashboard/src/data/directExecutionGrant.test.ts

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Pins the dashboard grant POST adapter.

## Contract

Mocked fetch assertions pin the exact route, method and repository/path/action body, preservation of refusal words, and unreachable-control reporting. These are client-boundary tests, not evidence that a running server or grant store accepted a request.

## Evidence

- Pins the dashboard grant POST adapter [1]
