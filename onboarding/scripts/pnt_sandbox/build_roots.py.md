# scripts/pnt_sandbox/build_roots.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

This helper runs inside the selected build Python, declares dashboard or MCP process role before load_config, walks absolute configuration paths and derives repository/receipt/report/authority roots through that build. It reports each missing/error root independently and exposes package identity and expected roots for the evaluator. The inline taskless-report path remains a documented coupling.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## 260928-MIK-L96 The product Node and cache roots

`resolve_roots` now adds the two product Node roots (the managed installation and the archive cache) to the roots the safety check resolves, so a missing, outside or symlink-resolved product Node or cache path refuses the start before installation or dashboard spawn.

- The resolver with the product Node and cache roots. [2]
