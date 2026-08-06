# l-01-agent-lifecycles/templates/onboarding-coherency.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/onboarding-coherency.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f` |
| lastVerifiedCommitDate | 2026-08-06T05:49:07+02:00|

## Purpose

This template is the **onboarding-vs-code** report of the `l-01-agent-lifecycles` report-template library. A fan-out sub-agent writes it for the **adversarial reviewer's** third lens and for the **orchestrator's** memory-quality checks — the paired `read_ar_files` + `memory_quality_check` + `drift_check` review made durable, since **orchestrator quality ∝ memory-repo quality**.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/onboarding-coherency.md`. It carries a prose header naming its consumers and the paired-check basis, a numbered **Rules** block, and a fenced **Shape**: a metadata table (for / author / scope / written) followed by a *Changed Files — Sidecar Refresh* table, a *New Files — Missing Onboarding* table, a *Drift & Quality* section (`drift_check`, `memory_quality_check`, ledger-maps-HEAD), an *Overviews* section, and a *Bottom Line* that frames gaps as candidate fix leaves.

### Conventions

The report checks that every **changed** source file has its sidecar body updated **in the same pass** (a refreshed `lastVerifiedCommitHash` over stale content silently defeats the drift check and is itself a finding), that every **new** source file has a created sidecar (`check_missing_onboarding` clean), and that route/repository overviews reflect the change set including moved/added/deleted slices.

### Invariants And Boundaries

This is a **report**; the reviewer's verdict or the orchestrator's main loop acts on it — the report does not decide or mutate. A moved/added/deleted slice must be reflected in the governing overview, and a stale overview or an unrefreshed sidecar body is a finding surfaced as a candidate fix leaf.

### Todos

No TODO markers are present in this report template.

### Docs References

No external domain documentation applies to this repository-local report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the reviewer's onboarding-vs-code lens and the orchestrator's memory-quality checks.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Onboarding-Coherency Template` | skills/l-01-agent-lifecycles/templates/onboarding-coherency.md:1-48 |
| The adversarial reviewer's onboarding-vs-code lens cites this report as backing evidence. | "../templates/onboarding-coherency.md" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:92-92 |
| The orchestrator's memory-quality checks consume this report; the analysis is written by the orchestrator's own loop or a dispatched role seat while AR mutations stay in the orchestrator main loop. | `## No Native Sub-Agents — role seats only (doctrine, ruled 2026-08-05)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:388-414 |
| The frame defines the onboarding-vs-code lens as paired read_ar_files + memory_quality_check + drift. | `## The Three Review Lenses` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:76-89 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` onboarding-coherency report template (leaf 260703-L1) — the reviewer's onboarding-vs-code lens report (paired read_ar_files + memory_quality_check + drift_check) checking same-pass sidecar refresh, new-file missing onboarding, drift/quality, and current overviews, on the "orchestrator quality ∝ memory-repo quality" doctrine. Verification metadata pinned until closeout stamps the L1 commit.
