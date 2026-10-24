# mcp/src/agents_remember/canvas/explainer_answers.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The answer boundary every explainer tool body passes through, so one refused call becomes data with a named reason rather than an exception reaching its caller.

## Code Commentary

- `refusal` answers `state: refused` with the reason and the detail as fields, which is the shape a page or a tool renders instead of a traceback.
- `answered` runs one tool body and converts the seat's own refusal, the presenter's refusal, a held path, a named `ValueError` and an `OSError` into that same shape, each under its own reason.
- The module imports only the three refusal types and nothing behind them, so a declaration module can reach the boundary without loading the readers, writers and services.
- The two functions are the same objects the access module re-exports, so a caller's import path and a declaration owner's import path cannot diverge.

## Evidence

- A refused call is answered as `state: refused` carrying the reason and the detail [1]
- One tool body's typed refusals, a named `ValueError` and an `OSError` all become the same data shape [2]
- A path the confinement holds is answered as `path-held` with the guard's own text [3]
