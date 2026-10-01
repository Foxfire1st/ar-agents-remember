# scripts/harness/shared/render-starter.ps1

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The canonical PowerShell launcher for a harness starter package's `render-starter.py`.
`scripts/sync-harness.py` copies this file **verbatim** into all eight starter packages,
replacing eight byte-identical copies.

## Code Commentary

### Logic

Sets `$ErrorActionPreference = "Stop"`, resolves the script's own directory from
`$MyInvocation.MyCommand.Path`, and runs the sibling `render-starter.py` through the
Windows Python launcher (`py -3`), splatting `@args` so caller arguments pass through.

`py -3` rather than `python` is the Windows-correct choice: the launcher resolves an
installed Python 3 without depending on `PATH` order.

### Invariants And Boundaries

- This is a **verbatim** shared source: the generator copies it with no substitution, so
  it must contain nothing harness-specific.
- It is the Windows half of a pair; the POSIX half is `render-starter.sh`. Windows is a
  supported platform through WSL for the repository itself, but a starter package is
  copied into a user's workspace and may be rendered on native Windows, which is why this
  file exists.
- Editing a generated copy is caught by `sync-harness.py --check` in both hook tiers and
  by `mcp/tests/test_sync_harness.py`.

## Evidence

### Repo-Internal References

- The generator that fans this file out verbatim to all eight starter packages. [1]
- The PowerShell wrapper launches `render-starter.py`. [2]
- The renderer implementation defines `main`. [3]
- The POSIX counterpart. [4]
