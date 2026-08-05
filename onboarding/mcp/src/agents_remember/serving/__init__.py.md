# mcp/src/agents_remember/serving/__init__.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/__init__.py`  |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-06-14T11:30+02:00                         |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`     |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The serving route overview. | `# mcp/src/agents_remember/serving/ — Dashboard Serving Layer Overview` | onboarding/mcp/src/agents_remember/serving/overview.md:1-2198 |

## Update History
- 2026-08-03T03:00:33+02:00 — W3-B05 curator: resolved 1 Tier-2 table finding with an exact route-overview heading and memory-repository source path; fixer generated the final range.

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the serving package marker.
  Verification metadata pinned until closeout stamps the 4a code commit.
