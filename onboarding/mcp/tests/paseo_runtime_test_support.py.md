# mcp/tests/paseo_runtime_test_support.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

FakePaseo substitutes npm and native runtime commands while keeping the real temporary home config file. It models start-only settings, live reload and loaded plugin contents separately, so file convergence is distinguishable from the fake daemon's applied state. It is an in-process stand-in rather than a real Paseo qualification.

## Evidence

`write_shared_runtime` obtains the shared guard's path before creating the settings parent or writing
runtime settings. The `settings=None` branch is guarded before unlink too: support cannot remove the
account's real settings file. Refusal names the temporary `XDG_CONFIG_HOME` remedy. The existing fake
runtime behavior and settings bytes in a moved configuration folder remain unchanged.

- The source retains the fake-runtime model and guards the shared settings path before both writing and removal. [1]
