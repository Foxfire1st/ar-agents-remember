# mcp/tests/test_read_cancellation.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for read cancellation.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

A disconnected client stops the read at its next safe point and is answered nothing. Additional cases exercise client disconnect during `POST /api/role-launch/options` (killing and reaping the running Paseo bridge process group, returning HTTP 499, and preserving the prior saved catalog when cancellation is observed before or during catalog-lock acquisition, while preserving an already-published snapshot on late disconnect during receipt liveness reads).

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A disconnected client stops the read at its next safe point and is answered nothing [1]
