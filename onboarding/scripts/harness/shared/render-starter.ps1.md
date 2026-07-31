# scripts/harness/shared/render-starter.ps1

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/render-starter.ps1` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `00e83791d4d21bf56fd5b3cc0af194bc5e28112a` |
| lastVerifiedCommitDate | 2026-07-31T05:07:07+02:00|
| governingOverview      | `../../../overview.md`                     |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The generator that fans this file out verbatim to all eight starter packages. | [sync-harness.py](agents-remember/scripts/sync-harness.py) |
| The program this script launches. | [render_starter.py](agents-remember/scripts/harness/render_starter.py) |
| The POSIX counterpart. | [render-starter.sh](agents-remember/scripts/harness/shared/render-starter.sh) |

## Update History

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for eight
  byte-identical copies (requirement L2-R12). Verification metadata is pinned to the
  leaf's reformat commit until closeout stamps the code commit.
