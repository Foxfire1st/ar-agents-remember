# scripts/pnt-sandbox.py

## Governing Overview

[Route overview](../overview.md)

## Purpose and current source account

This development entry point puts scripts on the import path and calls the pnt_sandbox namespace package CLI. It exposes build/start/stop/reset/check and does not ship in the wheel. The tooling intentionally has no __init__.py so it does not create a competing repository import root.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
