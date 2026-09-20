# l-01-agent-lifecycles/templates/onboarding-coherency.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/onboarding-coherency.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|

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
| The adversarial reviewer's onboarding-vs-code lens cites this report as backing evidence, and the reviewer's Outputs section names it among the durable route reports. | `# Reviewer`; "durable sub-agent route reports" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:6-6; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:96-96 |
| The orchestrator's checks consume this report, written by its own loop or a dispatched role seat while AR mutations stay in the orchestrator main loop; the no-native-sub-agents rule moved into the shared operation block in 260915-CAPS-L1. | "No native sub-agents on this seat."; `# Operation — Coordination`; "AR state mutations stay in the owning seat's main loop" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:101-104; skills/l-01-agent-lifecycles/operations/coordination.md:1-1; skills/l-01-agent-lifecycles/operations/coordination.md:68-70 |
| The reviewer's onboarding-vs-code lens pairs `read_ar_files` with `grepai_search`, and the curation exception makes the complete memory-quality operation the reviewer's one non-optional check. | "onboarding against code"; "Curation is the exception" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:56-58; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:62-65 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 1 enforced citation row this card carried (citation_anchor_absent_from_range): its cited range was hand-read against mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md and already held the anchor its claim names — "durable sub-agent route reports" at reviewer.md:96-96 — so no range was changed; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `durable sub-agent route reports`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

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
