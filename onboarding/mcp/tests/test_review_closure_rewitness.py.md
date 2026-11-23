# mcp/tests/test_review_closure_rewitness.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for review closure rewitness.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

The native request test checks reuse of a valid saved proof, a freshened object checked inside the same request, and renewed traversal after the aggregate witness changes on a later request. A missing required object refuses the read.

With a kept proof and a stable enclosing storage witness, rechecking a freshened object reads its body without walking the rest of that closure.

## Evidence

- A held proof whose object Git freshened reads that body and never traverses [1]
