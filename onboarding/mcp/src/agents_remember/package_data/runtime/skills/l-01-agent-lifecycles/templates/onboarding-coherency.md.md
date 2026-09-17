# l-01-agent-lifecycles/templates/onboarding-coherency.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/onboarding-coherency.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | `304de8e272fd9128d035b805f317da5f3090865c`|
| lastVerifiedCommitDate | 2026-09-17T12:34:11+02:00|

## Purpose

Packaged runtime copy of the onboarding-versus-code coherence report template. The canonical
template owns the review shape; the skill sync process publishes this exact artifact.

## Code Commentary

### Logic

The report compares current code, existing onboarding/entity intent, and ruled task/design intent.
It inventories changed sidecars, missing onboarding, route overviews/indexes, and drift, and records
only the affected scoped diagnostics requested for the handoff. The author field names the analysis
role or bounded fan-out label, not a runtime sub-agent id.

### Conventions

Changed source sidecars and their nearest governing routes need a substantive current-body update
plus newest-first history, or a specific sanctioned no-impact attestation after review. Missing
onboarding and curator-actionable findings are reported with their exact status before handoff;
routine closeout and integration do not require a full memory-quality certificate.

### Invariants And Boundaries

- Verification hashes and entity fingerprints remain real-commit-derived.
- The report is evidence; it neither stamps metadata nor performs closeout.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.


## CCR-R12@v5 Handoff Boundary

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

## Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the reviewer's onboarding-vs-code lens and the orchestrator's memory-quality checks.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Onboarding-Coherency Template` | skills/l-01-agent-lifecycles/templates/onboarding-coherency.md:1-48 |
| The adversarial reviewer's onboarding-vs-code lens cites this report as backing evidence. | `../templates/onboarding-coherency.md`; `## 3 — Normal Workflow` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:147-147; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:100-139 |
| The orchestrator's checks consume this report, written by its own loop or a dispatched role seat while AR mutations stay in the orchestrator main loop; the no-native-sub-agents rule moved into the shared operation block in 260915-CAPS-L1. | "**No native sub-agents**"; `# Operation — Coordination` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:45-45; skills/l-01-agent-lifecycles/operations/coordination.md:1-1 |
| The frame defines the onboarding-vs-code lens as paired read_ar_files + memory_quality_check + drift. | `## The Three Review Lenses` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:212-243 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Replaced the handoff-evidence boilerplate sentence, which still presented full memory quality as an explicit request, with the completed-curation rule; `onboarding-coherency` already carries the full-operation check block this leaf's template now names.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. The reviewer row now cites the live `../templates/onboarding-coherency.md` mention and the Normal Workflow section; the orchestrator row cites the live `**No native sub-agents**` sentence and the operation block that now owns that rule, replacing the removed `## No Native Sub-Agents …` heading and the over-long `:499-526` range.

- 2026-09-10T09:50+02:00 — CCR-R12@v5 transaction-only curation against code commit `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0`: re-read the reviewer backing-evidence row: reviewer.md names this report in its Artifact Obligations instead of citing the template path from a lens. Verification metadata remains closeout-owned.

- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "../templates/onboarding-coherency.md" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `## The Three Review Lenses` repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:212-243. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-11T19:58+02:00 — Reconciled `onboarding-coherency.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` onboarding-coherency report template (leaf 260703-L1) — the reviewer's onboarding-vs-code lens report (paired read_ar_files + memory_quality_check + drift_check) checking same-pass sidecar refresh, new-file missing onboarding, drift/quality, and current overviews, on the "orchestrator quality ∝ memory-repo quality" doctrine. Verification metadata pinned until closeout stamps the L1 commit.
