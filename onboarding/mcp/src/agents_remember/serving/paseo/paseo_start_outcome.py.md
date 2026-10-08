# mcp/src/agents_remember/serving/paseo/paseo_start_outcome.py

## Governing Overview

[overview](../overview.md)

## Purpose

One bounded outcome receipt for callers that joined the same owned host-start attempt.

## Code Commentary

The home lock owns the receipt and each attempt replaces it. `joined_outcome` accepts a receipt only when its settings key matches and it finished after the caller began waiting, so a contending caller converges on the owner's result instead of starting a second host; ordinary status and later starts always observe the host itself.

## Evidence

- The settings-bound attempt key. [1]
- The join rule for a contending caller. [2]
