# curator-review-template.md

| Field                  | Value                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- |
| repository             | agents-remember                                                                      |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/curator-review-template.md` |
| doc_type               | `file-level-onboarding`                                                                 |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff`                                                                                      |
| lastVerifiedCommitDate |                                                                                         2026-06-02T16:24:22+02:00|

## Purpose

This template defines the review artifact used after route-overview or file-onboarding waves.

## Code Commentary

### Logic

The curator review records wave status, files reviewed, compliance checks, reference health issues, bucket corrections, required fixes, developer questions, and next-wave recommendation.

### Conventions

Curator reviews are quality gates. They verify route-local placement, strict one-to-one file onboarding, backlinks, reference buckets, source evidence, no absolute paths, append-only history, and low-confidence handling.

### Invariants And Boundaries

Automated bootstrap mode may skip pauses, but it must not skip curator review artifacts. A curator review may require fixes before a wave is treated as complete.

### Todos

Fill verification metadata after the source file is committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The curator template records wave metadata, reviewed files, and a compliance checklist for placement, references, links, history, low-confidence claims, and state updates. | `# Curator Review — <wave>` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/curator-review-template.md:1-62 |
| The template captures reference-health issues, bucket corrections, required fixes, developer questions, and next-wave recommendations. | `## Reference Health`; `## Bucket Corrections`; `## Required Fixes`; `## Developer Questions`; `## Next-Wave Recommendation` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/templates/curator-review-template.md:40-62 |
| `c-03-repo-bootstrap` skill Phase 4I requires a curator review after each overview or onboarding wave. | `### 4I — Curator Review` | mcp/src/agents_remember/package_data/runtime/skills/c-03-repo-bootstrap/SKILL.md:1021-1048 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-14T18:00+02:00: Created onboarding for the curator review template. Verification metadata remains blank until the source file is committed.
