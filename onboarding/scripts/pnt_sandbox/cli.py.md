# scripts/pnt_sandbox/cli.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

The CLI dispatches five development commands to one canonical SandboxLayout and Operations object. Exit 0 reports success, 1 reports step/check failure and 2 reports refusal. A start refusal means no process was started; build preparation can already have changed the sandbox or ignored checkout outputs before a late refusal.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## 260928-MIK-L96 Explicit ports with preserved defaults

The public parser now takes the host and dashboard ports for build, check, start and stop with 6820/9797 as defaults; `_port` rejects out-of-range values and the live ports 9785/9786 at parse time, and `_run` refuses an equal host/dashboard pair before any action; an occupied chosen pair is valid for owned-process adoption and stop, while only a foreign listener refuses the start. No port is ever selected automatically.

- The parser with the explicit port arguments. [2]
- The controller passing the chosen pair. [3]
