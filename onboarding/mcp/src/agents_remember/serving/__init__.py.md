# mcp/src/agents_remember/serving/__init__.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/__init__.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-06-14T11:30+02:00                         |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`     |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

`serving/__init__.py` marks the dashboard serving package. It is a docstring only — it
exports nothing — so that `serving.delta` and `serving.projector` stay importable without
pulling in FastAPI (only `app` and `static` import the web stack).

## Code Commentary

No runtime code beyond the module docstring and `from __future__ import annotations`. The
package's surface is reached through its submodules (`app.create_app`, `projector.Projector`,
`delta.diff_projection`, `static.mount_static`).

## Invariants And Boundaries

- Keep this import-free: importing the package must not import FastAPI, so the pure modules
  (`delta`, `projector`) remain testable and importable on their own.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The serving route overview. | [overview.md](agents-remember/mcp/src/agents_remember/serving/overview.md) |

## Update History

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the serving package marker.
  Verification metadata pinned until closeout stamps the 4a code commit.
