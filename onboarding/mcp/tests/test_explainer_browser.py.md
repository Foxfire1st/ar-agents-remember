# mcp/tests/test_explainer_browser.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The browser the explainer publishes with: one product-owned folder under the user's data home, the pinned Playwright module and its Chromium fetched there at the first explanation, a user's `AR_PLAYWRIGHT` used as given, and a refusal that names what is missing and the command that gets it.

## Code Commentary

- The tests drive `ensure` through a substituted runner and a temporary data home, so no test downloads anything and no test reads the developer's own browser folder. The recorded commands are checked as argv lists: the product Node, the product npm, the `--prefix` staging folder, the pinned `playwright@<version>` and Playwright's own `cli.js install chromium`.
- A first fetch is checked to place the module and a Chromium build in the folder and to answer `fetched`; a second call answers `ready` and runs no child. A fetch whose steps succeed but leave no browser answers a refusal rather than a ready folder, and a failure names the missing part and `agents-remember explainer-browser --fetch`.
- `test_the_fetched_version_is_the_checkout_pin` reads `dashboard/package-lock.json` and requires both resolved Playwright and test-runner versions to equal `PLAYWRIGHT_VERSION`. This checks pin equality; Ubuntu installation behavior comes from the separately retained platform measurement.
- The announcement cases show that the sentence is available before the fetch and that the command a seat runs before its first render carries it.

## Relationships

The module under test is `canvas.explainer_browser`; `canvas.prospective` and `canvas.presenter_tools` consume it, and `mcp/tests/test_canvas_prospective.py` and `mcp/tests/test_explainer_server.py` cover those callers at the render path. The version check binds the product pin to the dashboard lockfile’s resolved Playwright and test-runner versions.

## Evidence

- The module and browser live in the product folder and are named to the load by the two variables. [1]
- A missing browser is fetched once, at the pin, through the product Node and npm, into the product folder. [2]
- A failed fetch refuses with what is missing and the command that gets it. [3]
- A named module that is absent refuses before anything is fetched. [4]
- The fetched version is the checkout's pin. [5]
- The first page is announced before the fetch begins. [6]
