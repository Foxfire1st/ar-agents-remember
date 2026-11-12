# dashboard/src/cockpit/stepUp.test-utils.ts

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Shared local catalog and projected receipt fixtures for step-up pane tests.

## Code Commentary

stepUpOptions deliberately separates Codex base mode/plan_mode/speed/notes from Claude alternative mode/auto_accept capabilities. stepUpReceipt binds the caller request ID and reports only running state, an observed model and source; it does not report applied mode, features or instructions.

## Evidence Boundaries

- This module supplies discriminating test inputs; it contains no assertions of its own. The mounted consumer asserts the non-applied preview boundary.
- These choices and claude-observed are fixtures, not actual catalog discovery, host observation or model availability.

This card describes assertion/support/document source, not a test invocation, independent verdict or publication.

## Evidence

- The source declares the qualified helper/document contract above; no execution is inferred. [1]
