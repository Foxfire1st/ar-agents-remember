# mcp/tests/explainer_host_test_support.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The host identities and workspace the explainer host suite mounts.

## Code Commentary

What must stay true here is what it names and builds: the server name, the leaf and the task the host tests address, and a workspace the explainer host can serve. `test_explainer_host.py` is the reader; the assertions are its own, and this module defines no test function.

## Boundaries

The obligation above is about what this file builds and returns; the assertions belong to the suites that read it.

## Evidence

- It names the host identities the tests address - the server name, the leaf and the task - and builds the workspace those tests read, so a host test exercises the same configuration another host test does. [1]
