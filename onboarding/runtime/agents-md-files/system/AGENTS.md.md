# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/agents-md-files/system/AGENTS.md`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-18T21:44+02:00                     |
| lastVerifiedCommitHash | `590df5a74eac6e213ae95c24f60656c4f1eb9841` |
| lastVerifiedCommitDate | 2026-05-18T17:15:39+02:00|

## Purpose

This file is the package-owned template for installed
`ar-coordination/system/AGENTS.md`. It defines the hard onboarding maintenance
gate and the read/update discipline agents must follow around memory-backed
onboarding.

## Code Commentary

### Logic

The template requires C-08 context resolution and C-02 drift detection before
agents rely on repository onboarding for any task, including read-only
analysis. It defines the developer decision point when drift exists, the C-05
maintenance route for approved refreshes, and the second C-02 check after
maintenance. It then separates post-gate planning from implementation.
For onboarding-backed source reading, use `C-04-onboarding-read-mode`. C-04 owns
the overview-to-route-to-candidate source/sidecar paired-read protocol.
Implementation updates or creates onboarding when code changes current-state
knowledge.

### Conventions

The system template is strict because it protects trust in durable memory. It
uses numbered gates for the startup workflow and clearer headings for
single-repo, cross-repo, planning, and implementation phases. The template now
keeps the trust and maintenance gates here while routing read behavior to C-04,
so the read-mode contract has one owning document.

### Invariants And Boundaries

C-08 and C-02 are mandatory before trusting onboarding. C-02 detects drift but
does not update onboarding; C-05 owns approved onboarding maintenance. The drift
report is temporary coordination state and should be deleted after the gate is
complete. C-04 owns the post-gate source/onboarding read protocol.

### Todos

None.

### Docs References

No external domain documentation is needed for this repository-local runtime
template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding                                                                                                                     | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| The start-of-task trust gate requires C-08 context resolution, C-02 drift detection, developer review of drift, approved C-05 refresh, a second C-02 check, and drift report deletion. | L1-L30 | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |
| Cross-repository drift handling runs the first three gates for every allowed repo before asking about onboarding refresh. | L32-L38 | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |
| Post-gate planning and research routes onboarding-backed source reading to `C-04-onboarding-read-mode`, which owns the overview, route overview, candidate source, and sidecar paired-read protocol. | L42-L50 | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |
| Post-gate implementation updates or creates onboarding through C-05 when changed source files alter current-state knowledge. | L49-L61 | [runtime/agents-md-files/system/AGENTS.md](agents-remember-md/runtime/agents-md-files/system/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this runtime template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-18T21:44+02:00: Refreshed after pulling the committed C-04 onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed system template, removing unlanded C-04 read-mode wording and updating verification metadata.
- 2026-05-18T17:03+02:00: Reduced the system onboarding description to the trust and maintenance gates plus C-04 routing for post-gate read behavior, matching the updated runtime template.
- 2026-05-18T15:32+02:00: Tightened onboarding-led discovery into an ordering rule: candidate pairs must precede source discovery search, onboarding tree enumeration is fallback-only, and source search must stay route-local before broad fallback.
- 2026-05-18T14:48+02:00: Renamed the system gate headings and added the onboarding-led source discovery path so warm-memory agents use overview and route maps to choose candidate files before broad source search.
- 2026-05-15T00:38+02:00: Created onboarding after the former root `system/AGENTS.md` guidance moved to the installable system template path. Verification metadata remains pinned to the last committed source until closeout.
