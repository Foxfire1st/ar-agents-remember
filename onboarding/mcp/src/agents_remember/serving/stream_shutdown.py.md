# mcp/src/agents_remember/serving/stream_shutdown.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The open streams end cleanly the moment the server begins to shut down.

## Code Commentary

Open streams end when shutdown begins, not when the process is killed, so a client learns the server is going away from the stream's own end.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- StreamShutdown ends open streams at the start of shutdown. [1]
