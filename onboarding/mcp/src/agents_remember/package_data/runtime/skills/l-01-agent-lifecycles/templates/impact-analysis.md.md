# l-01-agent-lifecycles/templates/impact-analysis.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/impact-analysis.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73` |
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|

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
| The orchestrator's portfolio integrity bulwark consumes this report, written by its own loop or a dispatched seat while AR mutations stay in the orchestrator main loop. | `# Orchestrator`; "portfolio integrity after the design returns"; "every AR state mutation stays in this seat's main loop" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:6-6; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:101-104; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:180-181 |
| The frame's artifact-obligation doctrine keeps AR mutations in the main loop while sub-agents write templated reports. | `# l-01-agent-lifecycles — The Agent Lifecycles` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-180 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-19T23:20+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b22c34a912f939e27868786818463c3b9c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers, and advanced this card's verification stamp to the code commit whose bytes were actually read.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each was read. The construct is `6-180` of `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` — re-measured on the file, not shifted: the heading's section runs to the line before the next heading of equal or higher level. No claim wording changed; nothing in the body was deleted to clear a finding. Note for a successor: a future landing that moves this file's headings makes the stamp historical again, and the closeout re-stamps.

- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `impact-analysis.md.md:46` (`# Orchestrator`, "portfolio integrity after the design returns", "every AR state mutation stays in this seat's main loop").
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. Also rebased an earlier `SKILL.md:6-416` citation to `:125-142` in this pass. The orchestrator row now cites the role head plus the live portfolio-integrity sentence instead of the pre-rewrite `:1-463`.


- 2026-08-11T19:58+02:00 — Reconciled `impact-analysis.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: deleted the unresolvable
  adversarial-reviewer row; exact non-fixing check returns zero findings.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 6 citation findings (3 rows); preserved the deleted adversarial-reviewer source claim as Tier 3; scoped recheck clean except 2 preserved Tier-3 findings.

- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/ (content unchanged). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` impact-analysis report template (leaf 260703-L1) — the integrity-bulwark report over two axes (planned-vs-planned incl. FUTURE masters, and planned-vs-past regression surface), evidence-first and a report not a decision, written by sub-agents while AR mutations stay in the spawning agent's main loop. Verification metadata pinned until closeout stamps the L1 commit.
