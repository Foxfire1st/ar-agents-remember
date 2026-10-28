# mcp/tests/explainer_server_test_support.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The world the explainer server suites mount: a workspace, two real Git trees, a packet and grants.

## Code Commentary

A World built here mounts the server at the boundary the suites assert on, and its helpers keep returning what they read. It defines no test function of its own: `test_explainer_server.py` (twelve tests) and `test_explainer_authored_claims.py` are the readers, and the assertions are theirs. What must stay true here is what a World mounts and what `code_tree`, the record, the fingerprints and `_server` return, because those are the values the readers assert on.

## Boundaries

The obligation above is about what this file builds and returns; the assertions belong to the suites that read it.

## Evidence

- A World built here mounts the server at the boundary the suites assert on, and its helpers keep returning what they read [1]
