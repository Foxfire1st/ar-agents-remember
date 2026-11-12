# mcp/src/agents_remember/serving/paseo/paseo_lock.py

## Governing Overview

[overview](../overview.md)

## Purpose

One bounded exclusion per host home, shared by install, start and explicit stop.

## Code Commentary

`runtime_lock` takes an exclusive `flock` on `<home>/agents-remember/runtime.lock` and waits at most until the caller's deadline; the wait past the first try is returned so a joined start knows it may reuse an attempt's outcome. Timeout is the named `host_operation_busy` refusal.

## Evidence

- The bounded home lock and its busy refusal. [1]
