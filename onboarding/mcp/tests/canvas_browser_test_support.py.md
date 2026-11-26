# mcp/tests/canvas_browser_test_support.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

The shared test helper discovers a Playwright module and Chromium browser cache.

## Code Commentary

An explicit environment setting is checked first. The helper can also use the product’s installed browser or the dashboard test dependency. It configures the environment for a test and skips when the Playwright module is unavailable.

## Relationships

The canvas test suites use this discovery helper. The production loader owns its own browser installation and ready-state behavior.

## Evidence

- The helper resolves the installed module and configures the test process. [1]
