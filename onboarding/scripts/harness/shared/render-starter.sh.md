# scripts/harness/shared/render-starter.sh

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/render-starter.sh` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                     |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The generator that fans this file out verbatim to all eight starter packages. | [sync-harness.py](agents-remember/scripts/sync-harness.py) |
| The program this script launches. | [render_starter.py](agents-remember/scripts/harness/render_starter.py) |
| The PowerShell counterpart. | [render-starter.ps1](agents-remember/scripts/harness/shared/render-starter.ps1) |

## Update History

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for eight
  byte-identical copies (requirement L2-R12). Verification metadata is pinned to the
  leaf's reformat commit until closeout stamps the code commit.
