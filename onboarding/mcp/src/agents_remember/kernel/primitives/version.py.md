# mcp/src/agents_remember/kernel/primitives/version.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/kernel/primitives/version.py`         |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-12T22:04+02:00                                        |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/version.py` is the installed package identity (moved from the `mcp` package
root by 260731-EFA-L9). Every layer above kernel may name the server/version without importing
the `mcp` package.

## Code Commentary

### Logic

Defines `SERVER_NAME = "agents-remember"` (cit:([`SERVER_NAME`], mcp/src/agents_remember/kernel/primitives/version.py:11-11)).
`_resolve_server_version` reads the installed `agents-remember-mcp` distribution metadata and
returns the committed `3.0.0rc7` identity only when that metadata is unavailable in a source
checkout. `SERVER_VERSION` is computed through that function seam, which keeps reload-based
fallback tests deterministic and gives every upper layer one kernel-owned value.

### Invariants And Boundaries

- Kernel stays importable by every layer; version identity must not drag `mcp` into kernel.
- Installed package metadata is authoritative; the literal fallback is only the matching source-release identity.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Package metadata and source-checkout fallback are selected through the explicit resolver. | `_resolve_server_version` | mcp/src/agents_remember/kernel/primitives/version.py:14-23 |
| Version fallback behavior is pinned by the structural-coverage suite. | `test_version_fallback` | mcp/tests/test_leaf_structural_coverage.py:189-189 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T22:04+02:00 — 260731-EFA-L23 post-code curator: replaced the stale `__version__` description with the committed `_resolve_server_version` seam and its installed-metadata-first, `3.0.0rc7` source fallback. Final verification stamping remains closeout-owned.

- 2026-08-12T10:08+02:00 — Advanced the source-checkout fallback to `3.0.0rc7` and extracted
  the existing installed-metadata/fallback branch into `_resolve_server_version()`. Behavior and
  kernel layering are unchanged; the named function makes a constant-only release delta
  non-vacuously measurable by targeted CRAP. Verification metadata remains pinned until closeout.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: re-anchored the version fallback
  proof after the structural test split; documented behavior is unchanged.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the kernel version-identity
  extraction. Verification metadata pinned until closeout stamps the L9 code commit.
