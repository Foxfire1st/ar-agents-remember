# scripts/harness/shared/render-starter.ps1

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/render-starter.ps1` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator that fans this file out verbatim to all eight starter packages. | `STARTER_SHARED`; `HARNESSES`; `generated_files`; `read_shared` | scripts/sync-harness.py:157-160; scripts/sync-harness.py:202-408; scripts/sync-harness.py:576-621; scripts/sync-harness.py:624-628 |
| The PowerShell wrapper launches `render-starter.py`. | "render-starter.py" | scripts/harness/shared/render-starter.ps1:4-4 |
| The renderer implementation defines `main`. | "def main(" | scripts/harness/render_starter.py:270-270 |
| The POSIX counterpart. | "render-starter.py" | scripts/harness/shared/render-starter.sh:5-5 |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: anchored generator fan-out, launched
  program, and POSIX counterpart references to exact symbols/literals; bound the PowerShell launch
  claim to its wrapper literal and renderer entrypoint.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for eight
  byte-identical copies (requirement L2-R12). Verification metadata is pinned to the
  leaf's reformat commit until closeout stamps the code commit.
