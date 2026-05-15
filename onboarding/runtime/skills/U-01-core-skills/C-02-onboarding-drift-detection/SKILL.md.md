# C-02-onboarding-drift-detection/SKILL.md

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember-md                                                 |
| path                   | `runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-05-15T12:57+02:00                                             |
| lastVerifiedCommitHash | `810a54351caa86a8e7f13677d284bd5e03147296`                         |
| lastVerifiedCommitDate | 2026-05-15T13:31:02+02:00|

## Purpose

This skill defines C-02, the drift-detection gate for onboarding. It checks whether onboarding metadata still matches source files, overview source routes, inline digests, and repo entity catalog fingerprints, including inventory-to-fingerprint coverage, then routes actionable maintenance to C-05.

## Code Commentary

### Logic

The skill instructs agents to use C-08 for memory/coordination context resolution, run the drift helper with `--code-repository-root`, inspect classifications, and treat drifted, missing-verification, orphaned, unsupported, or missing units as trust problems before relying on onboarding. It defines deterministic checks for `repo-overview`, `route-local-overview`, and `repo-entity-catalog` artifacts in addition to existing file-level and inline checks. Entity catalog checks reconcile `## Entity Inventory` headings with `## Entity Fingerprints` rows before trusting catalog entries.

### Conventions

C-02 reports trust state; it does not rewrite onboarding. It supports sidecar and inline storage models under the resolved onboarding root and writes Markdown reports as local coordination artifacts under C-08's resolved `temp_root` by default. Overview checks are route-based through `sourceRoute`; entity checks are fingerprint-based through `git-blob-set-v1` evidence rows, with missing inventory rows flagged as missing verification and unmatched fingerprint rows flagged as orphaned.

### Invariants And Boundaries

C-02 must stay read-only with respect to onboarding content. Any content update belongs to C-05. Drift reports are temporary evidence, not durable onboarding, and explicit report paths inside a durable memory repo should be redirected back to the resolved coordination temp area.

### Todos

Add tests for C-02 against a migrated external memory repo once such a fixture exists.

### Docs References

No external domain documentation applies to this repository-local maintenance skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

C-02 is the trust gate used before implementation and after onboarding maintenance.

| Finding                                                                                                                                                                                                                                    | Citations | Source Path                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------- |
| The skill outputs classifications and a C-05 handoff worklist.                                                                                                                                                                             | L16-L21   | [C-02 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| The helper takes `--code-repository-root`, writes a report under `<coordination_root>/temp/drift-reports/<repo-name>/` by default, keeps explicit report paths out of the resolved `memory_root`, and supports JSON, CSV, and text output. | L34-L54   | [C-02 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| Resolution must use C-08 and handle file-level sidecars, overviews, entity catalogs, and inline storage, including inventory-to-fingerprint reconciliation for repo entity catalogs. | L58-L66   | [C-02 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| Metadata extraction now includes file-level metadata, overview `sourceRoute` verification fields, entity inventory headings, entity fingerprint rows, and inline digest metadata. | L68-L97   | [C-02 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| Metadata comparison and classification rules establish which onboarding can be trusted, including route-based overview checks, missing entity fingerprint rows, orphaned fingerprint rows, and `git-blob-set-v1` entity checks. | L99-L114  | [C-02 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |
| C-02 hands content maintenance to C-05 rather than editing onboarding directly, including overview route drift, missing entity fingerprint rows, orphaned rows, and fingerprint evidence drift details. | L153-L177 | [C-02 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) |

## Cross-Repo References

No cross-repo evidence is needed for the current skill contract.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T12:57+02:00: Documented entity catalog inventory-to-fingerprint reconciliation, including missing fingerprint rows and orphaned fingerprint rows. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Refreshed after C-02 added route-overview checks and deterministic repo-entity fingerprints. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `c-02-onboarding-drift-detection` name.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the C-02 helper command examples adopted `--code-repository-root`.
- 2026-05-10T03:11: Updated after C-02 documented that explicit report paths inside `memory_root` are redirected to coordination temp.
- 2026-05-10T00:36: Refreshed verification metadata after the temp-root drift report behavior landed on main.
- 2026-05-09T23:22: Updated after C-02 moved default drift reports under C-08's temporary artifact root.
- 2026-05-09T21:15: Created first file-level onboarding baseline for C-02 skill documentation.
- 2026-05-09T21:59: Updated after C-08 split memory roots from coordination roots.
- 2026-05-09T22:57: Refreshed verification metadata and clarified that reports are coordination artifacts.
