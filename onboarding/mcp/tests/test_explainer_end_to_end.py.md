# mcp/tests/test_explainer_end_to_end.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One in-process run of the whole chain — open the review page's explainer for a task, request an explanation, record a grade, retire the seat — over the real routes, host and stores.

## Code Commentary

- The four steps run once against the real composition with only the model harness stubbed, so nothing about the chain is mocked except what would call a model.
- Each answer is asserted as what the developer would see, which is what makes the composition trustworthy rather than each seam alone.

## Evidence

- The case `test_the_explainer_end_to_end_open_request_grade_retire` protects the whole open, request, grade, retire chain completing in one process. [1]
