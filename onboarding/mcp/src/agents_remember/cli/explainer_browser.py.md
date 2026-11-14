# mcp/src/agents_remember/cli/explainer_browser.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The command-line adapter over the explainer's browser: report what this installation holds and what is missing, or fetch the missing part into the product's folder. It is not an installation step and the product does not need it to publish — the render path fetches by itself — but it is the way to see where that fetch put things, and to run it again or ahead of time when a render could not.

## Code Commentary

- `run` selects the two modes with one flag. Without `--fetch` the command reports only: the pinned version, the folder, the module path and the browser folder, plus the missing parts, the sentence the user is owed and the remedy when something is absent. With `--fetch` it calls the browser owner's `ensure`, so the code path, the lock, the staging folder and the version pin are the same ones a render takes.
- Every run is one JSON document on standard output. Exit status is 1 when the browser is missing or the fetch failed and 0 when it is there or was fetched, so a caller can test the fact rather than parse the wording.
- A refusal from the browser owner is reported as data — `{ok: false, error: {code, message}}` — rather than raised, because its message already names what is missing and the command that gets it.

## Relationships

`cli.__main__` registers it as `explainer-browser` beside the knowledge commands. Both modes call `canvas.explainer_browser`; this module holds no browser logic, no path of its own and no version. The guide to the review page and the install page name the same command as the way to fetch ahead of a render, and `serving.explainer` names it in the review page's own failure message.

## Evidence

- The command selects reporting or fetching with one flag and delegates the fetch to the browser owner. [1]
- A fetch reports the browser owner's record and answers 1 on a named refusal. [2]
- Reporting names the pin, the folder, the module, the browsers folder and what is missing, with the remedy. [3]
- A refusal is reported as data with its code and message. [4]
