# mcp/src/agents_remember/controlplane/interaction_retention.py

## Governing Overview

[controlplane overview](overview.md)

## Purpose

Retained pure gate-record retention utilities, not an operator-inbox/pickup policy or a reader of removed gate stores.

## Code Commentary

gate_keep_ids folds the latest GateRecord per id. _keep_gate preserves applied consumed-approval kinds without using age, drops cancelled/expired snapshots, and applies the bounded age rule to other snapshots, retaining an unknown age. The declared consumed-kind set combines mutating-tool approvals with the master-handover seam kind. These helper semantics do not imply that the removed gate hosting, decision/store reader or inbox retention still runs.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

