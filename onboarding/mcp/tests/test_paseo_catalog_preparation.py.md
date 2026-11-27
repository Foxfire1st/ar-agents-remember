# mcp/tests/test_paseo_catalog_preparation.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for paseo catalog preparation.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

Startup discovery and a first launch share Paseo's catalog only inside one operation's scope, so neither inherits the other's answer. Additional cases assert that one metadata `POST /api/role-launch/options` call shares `daemonConfig` / `daemonConfigError` with host role profiles and extra-args without spawning standalone `role-profiles` or `daemon-config` bridge calls, and that fresh and saved launcher catalogs omit refused native `antigravity` while keeping `antigravity-acp` and configured-default refusal messaging.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- One operation asks Paseo's catalog once for its preparation and its launch: the modes are metadata then selected, two calls, not four [1]
