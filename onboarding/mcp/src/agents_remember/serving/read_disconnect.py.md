# mcp/src/agents_remember/serving/read_disconnect.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The routes' one watch for a read whose client went away.

## Code Commentary

One disconnect watch serves the routes: a read runs while its client is connected and is abandoned when it is not, so an abandoned read stops computing instead of finishing into a closed stream.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- read_while_connected stops a read when its client disconnects. [1]
