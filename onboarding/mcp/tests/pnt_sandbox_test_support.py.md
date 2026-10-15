# mcp/tests/pnt_sandbox_test_support.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

SandboxCase and FakeOperations share disposable directories, real child dashboards/supervisors/listeners and real proc observations between two sandbox suites. Actions that would run the selected build, npm or Paseo use fakes. Temporary port selection can race a concurrently started test run; the fixture is not an OS isolation boundary.

SandboxCase hides named harness configuration markers at ancestors outside its owned fixture through a scoped Path.exists view. Existence inside the fixture and for all other paths uses the real filesystem; production location guards, lexical harness-path refusal and unsafe-project/symlink/escape checks remain active.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

- SandboxCase hides named harness configuration markers at ancestors outside its owned fixture through a scoped Path.exists view. Existence inside the fixture and for all other paths uses the real filesystem; production location guards, lexical harness-path refusal and unsafe-project/symlink/escape checks remain active. [2]
