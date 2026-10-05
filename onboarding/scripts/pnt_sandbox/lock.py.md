# scripts/pnt_sandbox/lock.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

Build/start/stop/reset take a nonblocking exclusive lock beside the resolved sandbox and name its holder. The extant inode is checked after acquisition; HeldLock records the command and provision child and supplies the inherited descriptor. Check takes no lock; build/stop children do not inherit it after abrupt parent death.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
