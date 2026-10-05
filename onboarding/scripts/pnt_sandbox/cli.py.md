# scripts/pnt_sandbox/cli.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

The CLI dispatches five development commands to one canonical SandboxLayout and Operations object. Exit 0 reports success, 1 reports step/check failure and 2 reports refusal. A start refusal means no process was started; build preparation can already have changed the sandbox or ignored checkout outputs before a late refusal.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
