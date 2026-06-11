# codegraphcontext-0.4.10-cgcignore-runtime-root.patch

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/patches/codegraphcontext/codegraphcontext-0.4.10-cgcignore-runtime-root.patch` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
| governingOverview      | `../../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

This patch asset documents the CodeGraphContext v0.4.10 monkey patch required for Agents Remember managed provider mode. It prevents CGC from unconditionally creating `.cgcignore` in the indexed source repo when an explicit runtime ignore path is available.

## Code Commentary

### Logic

The patch targets `codegraphcontext/core/cgcignore.py`. In the unpatched code, `local_cgcignore_path` defaults directly to `ignore_root / ".cgcignore"` and CGC writes the default ignore file there. The patch changes that branch to prefer `explicit_cgcignore_path` when provided, falling back to `ignore_root / ".cgcignore"` only when no explicit path exists. This lets Agents Remember place `.cgcignore` under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/` instead of dirtying the indexed code repository.

### Conventions

The patch is version-specific. Lifecycle tooling should apply it only after installing the pinned CGC provider version and should verify the marker before indexing.

### Invariants And Boundaries

Managed CGC provider mode is not acceptable if indexing creates `.cgcignore`, `.codegraphcontext`, `CGC_REPORT.md`, database files, or logs in the source repo. This patch addresses the `.cgcignore` case for CGC v0.4.10.

## Docs References

No external documentation is needed for this local patch asset.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The patch replaces CGC's direct repo-local `.cgcignore` default with a branch that prefers `explicit_cgcignore_path`. | L1-L13 | [patch](agents-remember/mcp/src/agents_remember/package_data/runtime/providers/patches/codegraphcontext/codegraphcontext-0.4.10-cgcignore-runtime-root.patch) |
| The package provider helper carries the same patch marker and idempotent source replacement used by the lifecycle service. | n/a | [context.py](agents-remember/mcp/src/agents_remember/providers/context.py) |

## Cross-Repo References

No sibling repository evidence is needed for this patch asset.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T19:16+02:00: Updated the provider helper reference after `context_providers.py` was replaced by `providers.context` and context modules.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T17:50+02:00: Updated references after provider helpers became MCP package modules and the old source shared route was removed.
- 2026-05-23T05:32+02:00: Updated managed CGC runner-path commentary after provider instances moved under `providers/runners/codegraphcontext`.
- 2026-05-20T19:11+02:00: Created onboarding for the CGC `.cgcignore` runtime-root patch asset.
