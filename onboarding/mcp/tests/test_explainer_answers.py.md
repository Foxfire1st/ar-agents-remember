# mcp/tests/test_explainer_answers.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The answer boundary was extracted and not relocated: both import paths name the same function objects, and the light module pulls no reader, writer or service behind it.

## Code Commentary

- Both paths resolve to identical `answered` and `refusal` objects, so a caller's import and a declaration owner's import cannot diverge into two behaviours.
- A fresh interpreter importing only the light module loads none of the access module, server, MCP tools or FastAPI.

## Evidence

- The case `test_the_two_paths_reach_the_same_function_objects` protects the two import paths being one behaviour. [1]
- The case `test_the_light_module_imports_no_service` protects the light module importing no service behind it. [2]
