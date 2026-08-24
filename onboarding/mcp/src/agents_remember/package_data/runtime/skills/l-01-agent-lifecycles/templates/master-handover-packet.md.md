# l-01-agent-lifecycles/templates/master-handover-packet.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/master-handover-packet.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-24T13:51:26+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the durable manager-to-orchestrator master handover. The canonical template
owns its shape; the sync process publishes this exact artifact.

## Code Commentary

### Logic

After independent master-exit review, the manager records the master task document, manager role,
integration branch/base, verdict or delegated-decision evidence, landed change set, carry-over
state, and follow-ups. Candidate tree, code ancestry, memory ancestry, and every leaf's exact
ledger/commit row are cited through canonical stable refs; their maps are not copied into the
packet. The receiving orchestrator resolves each ref and revalidates that it names the proposed
candidate. Terminal/finalizer truth wakes the current orchestrator. The packet carries neither an
orchestrator occupant address nor a gate id; `message_parent` is only for clarification or a
blocking issue.

### Conventions

Write the durable packet after the verdict exists and keep its evidence sufficient for integration
and memory carry-over without re-derivation. Edit the canonical template, then synchronize.

### Invariants And Boundaries

- `(master task document, manager)` remains reachable across occupant replacement.
- Structural gate resolution is plane-owned and does not use packet-carried transport identity.
- A summary never substitutes for canonical candidate/ancestry/ledger evidence, and the packet
  never becomes a second mutable lineage or commit map.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Repo-Internal References

This bundle copy is the shape the manager job posts at master exit; it references the master-exit verdict artifact and feeds the orchestrator's C-11 integration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Master-Handover-Packet Template` | skills/l-01-agent-lifecycles/templates/master-handover-packet.md:1-77 |
| The manager posts this packet to the orchestrator at master exit. | `# Lifecycle — Manager` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:1-319 |
| The required verdict slot references the independent master-exit adversarial verdict artifact bound to the proposed candidate. | `# Verdict Template (adversarial reviewer)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/verdict.md:1-188 |
| The frame lists the master-handover packet among the per-role artifact obligations. | `# l-01-agent-lifecycles — The Agent Lifecycles` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:1-456 |

## Cross-Repo References

No sibling repository evidence is needed for this report template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L2 Nature-Aware Handover

The handover names `executionNature`, prior landed organizational leaf refs plus the proposed final
leaf, and the exact proposed candidate tree/ref; an atomic handover names its isolated branch and
tree. The one full gate boundary is before the final organizational ref movement or during atomic
block landing. Candidate/code/memory ancestry and per-leaf ledger/commit evidence use canonical
stable refs with row ids or JSON pointers, never branch names, bare assertions, or copied maps.
Carry-over remains a documented recovery fact, never the normal landing strategy.

## 260821-DAGQC-L4 Canonical Evidence References

The packet's table indexes the authoritative ledger/commit rows without repeating their commit
values. The receiving orchestrator must resolve every candidate-tree, code-ancestry,
memory-ancestry, verdict, and per-leaf ledger ref and confirm that it belongs to the same proposed
candidate. Missing, stale, unresolvable, or candidate-mismatched evidence blocks handover; packet
summary prose cannot override it.

## Update History

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: replaced copied lineage/ledger-map implications
  with canonical candidate, code-ancestry, memory-ancestry, verdict, and per-leaf ledger/commit
  refs plus receiver-side candidate revalidation. Canonical/generated sync is complete; Dagger
  acceptance remains closeout-owned and pending.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: added nature-aware scope, exact proposed candidate, and
  one-full-gate boundary fields. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `master-handover-packet.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 8 citation findings for the canonical handover template, manager role, verdict template, and lifecycle skill references.

- 2026-07-05T19:10+02:00 - L8 builder cycle 6: the manager row became `manager seat | <master's coordination leaf / chat ref>` — no lifecycle ids in model-authored artifacts (AR3-6d). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the shape gains the handover gateId row — the packet is the decider's address for the gate.. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: re-homed under l-01-agent-lifecycles/templates/; role-file reference now roles/manager.md. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: documented the `master-handover` inbox
  message-kind convention for manager-to-orchestrator delivery. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:00+02:00: Created file-level onboarding for the new `l-01-agent-lifecycles` master-handover-packet report template (leaf 260703-L1) — the manager → orchestrator master-exit hand-off (integration branch, change-set summary, verdict ref, C-11 carry-over), posted only after the master-exit verdict exists. Verification metadata pinned until closeout stamps the L1 commit.
