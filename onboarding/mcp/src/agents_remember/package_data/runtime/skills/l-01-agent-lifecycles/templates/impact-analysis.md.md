# l-01-agent-lifecycles/templates/impact-analysis.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/impact-analysis.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|

## Purpose

Packaged runtime copy of the bounded impact-analysis report template. The canonical template owns
the report contract; the sync process publishes this exact artifact.

## Code Commentary

### Logic

The report records scope, evidence, affected surfaces, risks, and conclusions for an orchestrator or
reviewer. Its author is an analysis role or bounded fan-out label, not a runtime sub-agent id.

### Conventions

Keep findings evidence-backed and label the analytical responsibility rather than transport
identity. Edit the canonical template and synchronize.

### Invariants And Boundaries

- The report carries analysis, not mutation authority.
- Runtime occupant identifiers are not durable authorship identity.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the orchestrator's integrity bulwark and the reviewer's completion lens.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Impact-Analysis Template` | skills/l-01-agent-lifecycles/templates/impact-analysis.md:1-52 |
| The orchestrator's portfolio integrity bulwark consumes this report; its fan-out sub-agents write it while AR mutations stay in the orchestrator main loop. | `# Lifecycle — Orchestrator` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:1-463 |
| The frame's artifact-obligation doctrine keeps AR mutations in the main loop while sub-agents write templated reports. | `# l-01-agent-lifecycles — The Agent Lifecycles` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-416 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `impact-analysis.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: deleted the unresolvable
  adversarial-reviewer row; exact non-fixing check returns zero findings.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 6 citation findings (3 rows); preserved the deleted adversarial-reviewer source claim as Tier 3; scoped recheck clean except 2 preserved Tier-3 findings.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` impact-analysis report template (leaf 260703-L1) — the integrity-bulwark report over two axes (planned-vs-planned incl. FUTURE masters, and planned-vs-past regression surface), evidence-first and a report not a decision, written by sub-agents while AR mutations stay in the spawning agent's main loop. Verification metadata pinned until closeout stamps the L1 commit.
