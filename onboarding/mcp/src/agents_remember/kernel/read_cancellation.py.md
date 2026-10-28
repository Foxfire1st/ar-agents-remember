# mcp/src/agents_remember/kernel/read_cancellation.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A read whose client went away stops computing.

## Code Commentary

Work behind a read yields when the client is gone: the cancellation token is checked between steps, and a page read takes priority over background building, so an abandoned read stops rather than finishing into a socket nobody is holding.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- CancellationToken is what a read checks between steps. [1]

- YieldsToPageReads lets a page read take priority over background building. [2]
