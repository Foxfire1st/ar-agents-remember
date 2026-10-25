# mcp/tests/test_knowledge_read_boundary_roster.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R74 rule 6: the complete protected-read roster with per-route outcomes.** Split whole from `test_knowledge_read_boundary.py` under the Owner line-bound disposition: every case, assertion and negative control is preserved; only the address changes. The oracle lives in `read_boundary_oracle_test_support.py`.

## Code Commentary

The roster names every read-described route with its constructor, call and outcome. Terminal and harness GETs read against concrete lifetimes inside the snapshotted roots — no live PTY, actor or driver. The cockpit boundary names its outcomes without a live lifetime. The five terminal/harness GETs (sessions, harnesses, unknown capabilities, both unknown-session selectors) assert product statuses with closing classification over every concrete file in both bundles.

## Evidence


- Every route names its outcome [1]

- Cockpit boundary needs no live lifetime [2]
