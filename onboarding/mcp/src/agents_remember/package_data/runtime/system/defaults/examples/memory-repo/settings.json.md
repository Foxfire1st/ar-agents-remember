# settings.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.json` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

This JSON example models machine-readable settings for a external memory repo.

## Code Commentary

### Logic

The example uses settings version 2, `memory-repo` onboarding storage, include/exclude path rules with common generated/vendor/build/local excludes, and a branch-gated `crossRepo.allow` entry.

### Conventions

This file demonstrates memory-owned policy, not coordinator routing.

### Invariants And Boundaries

`onboarding.storage` decides where eligible onboarding lives, `onboarding.pathRules` decides eligibility, the standard excludes prevent common generated or local-machine artifacts from being selected, and `crossRepo.allow` opts into adjacent repositories.

### Todos

None.

### Docs References

No external documentation is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The JSON example declares version 2 memory-repo storage and path-rule include/exclude filters with common generated/vendor/build/local exclusions. | "version" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.json:2-2 |
| The JSON example shows a branch-gated cross-repo allowance with code and memory inclusion flags. | "crossRepo" | mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.json:35-35 |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 2 repo-internal citation rows and preserved verification metadata.

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T21:38+02:00: Refreshed after the example gained the standard path-rule exclusion baseline for generated/vendor/build/local artifacts. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T13:38: Created onboarding for the memory-repo settings JSON example.
