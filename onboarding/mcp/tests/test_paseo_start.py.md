# mcp/tests/test_paseo_start.py

## Governing Overview

[overview](overview.md)

## Purpose

The start/status state machine cases: a running host (including mismatches and carried session names) is read-only, a live unanswering supervisor never gets a second start, every down state starts at most once and never installs/configures/reloads, missing/wrong installs and an occupied port do not start, two concurrent starts share one home lock, no shared block is a named non-starting state, a contending caller joins the owned outcome, an expired start reports the still-live supervisor, an incomplete configuration cannot start on defaults, and start/status never query npm.

## Code Commentary

The module drives `ensure_host`/`observe_host` through `paseo_runtime_test_support` fakes with per-state file and process evidence.

The running-host case checks both public status paths with a matching executable and an earlier Node while the contract target is present. Only the mismatch names the Node restart requirement and provision remedy; observation changes no host, setting, process signal or file.

## Evidence

- The start-only case. [1]
- The single-owned-start case. [2]

- The join-outcome case. [3]

- The no-npm and discovered-config case. [4]
