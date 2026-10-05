# scripts/pnt_sandbox/build_roots.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

This helper runs inside the selected build Python, declares dashboard or MCP process role before load_config, walks absolute configuration paths and derives repository/receipt/report/authority roots through that build. It reports each missing/error root independently and exposes package identity and expected roots for the evaluator. The inline taskless-report path remains a documented coupling.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
