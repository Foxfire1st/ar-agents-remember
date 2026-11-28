# dashboard/package.json

## Governing Overview

[repository overview](../overview.md)

## Purpose

The dashboard’s npm manifest declares its dependency ranges, development tools and scripts. Runtime dependencies include React, CodeMirror and Zustand; development dependencies include Vite, Vitest, oxlint, TypeScript 7, Panda and Playwright’s test runner.

## Code Commentary

- `@playwright/test` declares the range `^1.65.0`. The lockfile resolves it to 1.65.0, and the browser unit test compares resolved Playwright and test-runner versions with the product fetch pin.
- `dependencies` contains dashboard runtime libraries (CodeMirror core `@codemirror/merge`, `@codemirror/state`, `@codemirror/view` — with all hardcoded `@codemirror/lang-*`, `@codemirror/language`, and `@lezer/highlight` packages removed in favor of server-computed tree-sitter highlights) as well as testing packages; `devDependencies` declares development tools. Scripts define development, build, checking, formatting and test commands. A published Python installation does not run a dashboard npm dependency installation; the explainer browser fetch has its own product-owned path.
- `scripts.lint` runs `oxlint .` against `dashboard/.oxlintrc.json`; `scripts.typecheck` and `scripts.build` run `tsc -b` on `typescript` (`^7.0.2`). `typescript-compiler-api` (`npm:typescript@^6.0.3`) is a temporary compatibility alias restricted by `dashboard/.oxlintrc.json` to three compiler-API test files (`src/test/wireFixtureGuard.ts`, `src/test/fixtureOverrides.test.ts`, and `src/test/loadIndependence.test.ts`) until TypeScript 7's programmatic API leaves `unstable/`.

## Relationships

`dashboard/package-lock.json` records resolved versions for this manifest, and `dashboard/.oxlintrc.json` configures `oxlint` and restricts `typescript-compiler-api`. `canvas.explainer_browser` defines the product fetch pin; `test_the_fetched_version_is_the_checkout_pin` compares that constant with resolved lockfile versions.

## Evidence

- The manifest declares `@playwright/test` at `^1.65.0`. [1]

- The manifest separates dashboard dependencies (without `@codemirror/lang-*` packs), development dependencies and executable scripts. [2]
- Linting delegates to `oxlint .` (`^1.95.0`); typechecking and build run `tsc -b` on `typescript` (`^7.0.2`), while `typescript-compiler-api` aliases `npm:typescript@^6.0.3` under `.oxlintrc.json`'s three-file restriction. [3]
