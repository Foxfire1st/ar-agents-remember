# scripts/harness/shared/render-starter.sh

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The canonical POSIX-shell launcher for a harness starter package's `render-starter.py`.
`scripts/sync-harness.py` copies this file **verbatim** into all eight starter packages,
replacing eight byte-identical copies.

## Code Commentary

### Logic

Five lines: `set -eu`, resolve the script's own directory in a `CDPATH`-proof way
(`CDPATH= cd -- "$(dirname -- "$0")" && pwd`), then `exec python3` the sibling
`render-starter.py` forwarding `"$@"`.

Resolving the directory from `$0` rather than assuming the working directory is what lets
a user run the starter from anywhere in their workspace. `exec` replaces the shell so the
Python exit status is the script's exit status.

### Invariants And Boundaries

- This is a **verbatim** shared source: the generator copies it with no substitution, so
  it must contain nothing harness-specific.
- Generated copies are mode `0o644` and are invoked as `sh render-starter.sh`, not
  `./render-starter.sh`.
- Editing a generated copy is caught by `sync-harness.py --check` in both hook tiers and
  by `mcp/tests/test_sync_harness.py`.
- The Windows counterpart is `render-starter.ps1`, shared the same way.

## Evidence

### Repo-Internal References

- The generator that fans this file out verbatim to all eight starter packages. [1]
- The program this script launches. [2]
- The PowerShell counterpart. [3]
