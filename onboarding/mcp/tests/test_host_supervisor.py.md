# mcp/tests/test_host_supervisor.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin proved supervisor-exit invalidation and unknown state for absent, stale or failed subscriptions.

## Code Commentary

An unarmed subscription cannot certify old activity or call the snapshot bridge. Native pidfd tests use disposable Python child processes and controlled inspect_record results: identity is checked again after opening, exit invalidates once and closes the subscription, and permission failure drops any retained handle. These are native process-subscription assertions with fake host ownership, not a live Paseo supervisor run.

## Evidence

- No subscription means unknown activity and no bridge call. [1]
- A stale post-open identity refuses the subscription. [2]
- Disposable native child exit emits one invalidation and disarms. [3]
- Permission failure leaves a started but unarmed subscription, not the old proof. [4]
