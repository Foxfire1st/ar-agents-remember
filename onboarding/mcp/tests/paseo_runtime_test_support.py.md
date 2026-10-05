# mcp/tests/paseo_runtime_test_support.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

FakePaseo substitutes npm and native runtime commands while keeping the real temporary home config file. It models start-only settings, live reload and loaded plugin contents separately, so file convergence is distinguishable from the fake daemon's applied state. It is an in-process stand-in rather than a real Paseo qualification.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
