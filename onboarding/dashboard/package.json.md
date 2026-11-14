# dashboard/package.json

## Governing Overview

[repository overview](../overview.md)

## Purpose

The dashboard’s npm manifest declares its dependency ranges, development tools and scripts. Runtime dependencies include React, CodeMirror, Zustand and Three; development dependencies include Vite, Vitest, ESLint, Panda and Playwright’s test runner.

## Code Commentary

- `@playwright/test` declares the range `^1.65.0`. The lockfile resolves it to 1.65.0, and the browser unit test compares resolved Playwright and test-runner versions with the product fetch pin.
- `dependencies` contains dashboard runtime libraries as well as testing and type packages; `devDependencies` declares development tools. Scripts define development, build, checking, formatting and test commands. A published Python installation does not run a dashboard npm dependency installation; the explainer browser fetch has its own product-owned path.

## Relationships

`dashboard/package-lock.json` records resolved versions for this manifest. `canvas.explainer_browser` defines the product fetch pin; `test_the_fetched_version_is_the_checkout_pin` compares that constant with resolved lockfile versions.

## Evidence

- The manifest declares `@playwright/test` at `^1.65.0`. [1]
- The manifest separates dashboard dependencies, development dependencies and executable scripts. [2]
