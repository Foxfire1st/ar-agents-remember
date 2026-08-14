# l-01-agent-lifecycles/templates/onboarding-coherency.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/onboarding-coherency.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|

## Purpose

Packaged runtime copy of the onboarding-versus-code coherence report template. The canonical
template owns the review shape; the skill sync process publishes this exact artifact.

## Code Commentary

### Logic

The report compares current code, existing onboarding/entity intent, and ruled task/design intent.
It inventories changed sidecars, missing onboarding, route overviews/indexes, drift, and full memory
quality. The author field names the analysis role or bounded fan-out label, not a runtime sub-agent
id.

### Conventions

Changed source sidecars and their nearest governing routes need a substantive current-body update
plus newest-first history, or a specific sanctioned no-impact attestation after review. Missing
onboarding and curator-actionable quality findings must reach zero before handoff.

### Invariants And Boundaries

- Verification hashes and entity fingerprints remain real-commit-derived.
- The report is evidence; it neither stamps metadata nor performs closeout.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the reviewer's onboarding-vs-code lens and the orchestrator's memory-quality checks.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Onboarding-Coherency Template` | skills/l-01-agent-lifecycles/templates/onboarding-coherency.md:1-48 |
| The adversarial reviewer's onboarding-vs-code lens cites this report as backing evidence. | "../templates/onboarding-coherency.md" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:101-101 |
| The orchestrator's memory-quality checks consume this report; the analysis is written by the orchestrator's own loop or a dispatched role seat while AR mutations stay in the orchestrator main loop. | `## No Native Sub-Agents — role seats only (doctrine, ruled 2026-08-05)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:408-435 |
| The frame defines the onboarding-vs-code lens as paired read_ar_files + memory_quality_check + drift. | `## The Three Review Lenses` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:76-89 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `onboarding-coherency.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` onboarding-coherency report template (leaf 260703-L1) — the reviewer's onboarding-vs-code lens report (paired read_ar_files + memory_quality_check + drift_check) checking same-pass sidecar refresh, new-file missing onboarding, drift/quality, and current overviews, on the "orchestrator quality ∝ memory-repo quality" doctrine. Verification metadata pinned until closeout stamps the L1 commit.
