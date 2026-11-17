# mcp/src/agents_remember/canvas/explainer_browser.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The one owner of the Playwright module and Chromium that the explainer loads a prospective page with: where they live, how they get there at the first explanation, and which of them is missing when a load cannot run. Nothing here runs at installation; `ensure` is called at the render path and only when something is missing.

## Code Commentary

- Three facts fix the design. The product already installs a Node of its own for the host, and no explainer can start without that host, so the fetch runs the product's Node and npm and never a Node of the user's own. What it fetches lives in one product-owned folder under the user's data home — `<data>/agents-remember/explainer-browser` — beside that Node, named in the answer and removable by the user. A user who sets `AR_PLAYWRIGHT` keeps working exactly as before: their module wins and nothing is fetched or replaced behind it.
- `ensure` answers one of three states. `environment` is a module `AR_PLAYWRIGHT` names; such a module is used as given, with the browser folder Playwright's own defaults name, and an absent file refuses `browser-missing` before any fetch. `ready` is this installation's own folder already holding the module and a Chromium build. `fetched` is the folder placed by this call, and only that state carries the elapsed seconds in the record.
- The fetch is one bounded child per step: `npm install --prefix <staging> playwright@<pin>` and then Playwright's own `cli.js install chromium` with `PLAYWRIGHT_BROWSERS_PATH` pointing inside the staging folder. Both parts land in the hidden sibling `.<folder>.staging`, are checked there, and the whole folder is renamed into place, so a failed or half-finished fetch is never read as a ready browser; the staging folder is removed on every path out. A second seat that reaches its first render at the same time waits on one exclusive file lock and then reads the folder rather than downloading again.
- A missing executable and a child that runs out of time are answers, not exceptions: `run_bounded` returns exit 127 or 124, and the caller turns either into a named refusal. The refusal names what is missing, the folder it belongs in, and `agents-remember explainer-browser --fetch`; the version and browser name come from this module so the package fetch and a checkout's pin cannot drift apart.
- `browser_missing` is the caller's question in the answer's own words: it returns the missing parts and no text when nothing is missing, and it consults `AR_PLAYWRIGHT` first so a user-named module is never answered from this installation's folder.

## Relationships

`canvas.prospective.BrowserProspectiveLoad` calls `ensure` before it stages a run, so a missing browser leaves no half-run behind, and it calls `browser_environment` for the child's two names and `node_executable` for the Node the load runs on. `canvas.presenter_tools` reads `browser_missing` and `BROWSER_NOTICE` to answer the first render's announcement and keeps the failure the page draws. `serving.explainer` reads `BROWSER_COMMAND` for the same message, and `cli.paseo_explainer_host` reads `module_file` to hand a seat the installed module. `cli.explainer_browser` exposes the same two operations as a command. The module imports nothing from `serving.paseo`: the host's command names stay in the host adapter, and this fetch runs its own bounded child in the canvas tier.

## Evidence

- The module and its browser live in one product-owned folder under the user's data home. [1]
- A first fetch installs the pinned module and its Chromium into staging and moves the folder in whole, under one lock. [2]
- The fetch runs the product's own Node and npm and refuses by name when that Node is not installed. [3]
- A failed fetch refuses with what is missing and the command that gets it. [4]
- A module named in AR_PLAYWRIGHT is used as given, and an absent one refuses before any fetch. [5]
- One Playwright version is the pin the checkout lock and the fetch share. [6]
- The fetch's child runs bounded in the canvas tier, and a missing or timed-out child is an answer. [7]
