# mcp/src/agents_remember/providers/grepai/context/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T01:15+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/core.py` is a compatibility-free package-local facade for the focused Docker-owned GrepAI context modules.

## Code Commentary

### Logic

It imports public names from `constants.py`, `layout.py`, and `workspace.py`. It keeps `grepai.core` as a local organization point inside the new subpackage, while the public API remains `providers.context`.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| GrepAI lifecycle modules consume these exports through the context package. | "providers.grepai.context" | mcp/src/agents_remember/providers/grepai/lifecycle/core.py:22-22 |

## Update History

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: replaced unanchored module references with exact local anchors and generated final ranges with the scoped fixer.

- 2026-06-02T01:15+02:00: Dropped the `artifacts.py` re-export after the module was removed.
- 2026-05-25T19:33+02:00: Reduced to a facade after GrepAI context responsibilities were split into constants, layout, workspace, and artifact modules.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
