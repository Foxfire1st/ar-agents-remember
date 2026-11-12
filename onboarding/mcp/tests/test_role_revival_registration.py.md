# mcp/tests/test_role_revival_registration.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin role re-registration across host restart and stale closed listings until an actual new turn.

## Code Commentary

The fixture runs the real TypeScript HostActivityPublisher in a disposable Node process with injected native listings/events, alongside fake host launch/resume receipts and real role-registration files. Listing-before-warmup, registration-before-listing and explicit revive orders preserve reopened role facts through stale ended listings and concurrent launches. A later turn_started publication produces known works activity; later native close/archive or new-boot ended facts may reclaim the registration. This is mixed native-publisher/fake-host composition, not paid-agent, real-host delivery or acceptance evidence.

## Evidence

- Warmup after the new boot listing preserves reopened registration until native activity. [1]
- Warmup registration before late listing preserves the same role facts. [2]
- Explicit revive before late listing uses the same protection. [3]

- Shared composition drives actual Node publisher, injected listings/resume and first-turn task activity. [4]

- Later close/archive and new-boot ended evidence reclaim the registered role. [5]
