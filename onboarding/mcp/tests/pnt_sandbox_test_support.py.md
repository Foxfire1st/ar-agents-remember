# mcp/tests/pnt_sandbox_test_support.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

SandboxCase and FakeOperations share disposable directories, real child dashboards/supervisors/listeners and real proc observations between two sandbox suites. Only actions that would run the selected build, npm or Paseo are replaced. Temporary port selection can race a concurrently started test run; the fixture is not an OS isolation boundary.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
