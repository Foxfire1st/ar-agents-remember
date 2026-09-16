# l-01-agent-lifecycles/templates/master-handover-packet.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/master-handover-packet.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba` |
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the durable manager-to-orchestrator master handover. The canonical template
owns its shape; the sync process publishes this exact artifact.

260915-CAPS-L1 corrected this template's completion wording to the shipped truth boundary: the artifact
is durable and terminal/finalizer truth wakes the current orchestrator, but that terminal outcome
**attests only that the manager's turn ended** — it does not attest that the packet is complete or
correct. The orchestrator validates the packet, and rule 4's receiver-side revalidation is what accepts
it. The template now names `../core/acceptance.md` as the single home of that boundary.

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


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, full memory quality, certification, and review are explicit requests rather than automatic template gates.

## Repo-Internal References

This bundle copy is the shape the manager job posts at master exit; it references the master-exit verdict artifact and feeds the orchestrator's C-11 integration.

| Finding | Anchor | Source |
| --- | --- | --- |
| Sync-propagated bundle copy of the canonical templates source. | `# Master-Handover-Packet Template` | skills/l-01-agent-lifecycles/templates/master-handover-packet.md:1-77 |
| The manager posts this packet to the orchestrator at master exit; the manager's durable handoff artifact is this packet, validated by the orchestrator. | `# Lifecycle — Manager`; `## Which artifact each seat hands over, and who validates` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md:1-16; skills/l-01-agent-lifecycles/core/acceptance.md:27-42 |
| The required verdict slot references the independent master-exit adversarial verdict artifact bound to the proposed candidate. | `# Verdict Template (adversarial reviewer)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/verdict.md:1-188 |
| The router lists the master-handover packet among the templates the spawning seats compile from. | `## Companion Files` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:125-142 |
| This template and `verdict.md` are the manager's two artifact templates in the composition manifest. | `composition-manifest.json` — `roles.manager.templates` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |

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

- 2026-09-16T20:45+02:00 — owning-seat merge resolution (source-line convergence): the
  `governingOverview` field and its link were restored to `../../../../../../../overview.md`.
  The 2026-09-16T08:01 metadata repair above dropped one path level — this card sits one directory
  below the skill's `SKILL.md` card, so the target it names (the MCP package overview,
  `onboarding/mcp/overview.md`) needs seven levels up, not five. The five-level value resolved to
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist, so the card pointed at a
  missing file while its own text claimed the MCP package overview. No content claim changed; only
  the path. Verification metadata is unchanged and stays closeout-owned.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.** The
  canonical template's completion wording was corrected in this leaf: terminal/finalizer truth attests
  only that the manager's turn ended, the orchestrator validates the packet, and rule 4's receiver-side
  revalidation is what accepts it — with `../core/acceptance.md` named as the boundary's single home.
  The card now records that correction, and two citations with dead ranges (`roles/manager.md:1-319`,
  `SKILL.md:1-456`) were repointed to current anchors. **Metadata repair:** `governingOverview` pointed at `../../../../../../../overview.md` (the repository root overview) while its link text said "MCP package overview"; corrected to `../../../../../overview.md`, and the missing blank line between the metadata table and `## Governing Overview` was restored. Verification metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/master-handover-packet.md`
  changed since the recorded verification commit. Re-read the card against the frozen on-disk source
  and re-checked its claims and cited ranges: nothing this card asserts is falsified by the change,
  so no wording changed. Verification metadata remains closeout-owned; no verification stamp
  advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (one template line drops the `/replay` spelling). Re-read the
  card: it names no replay vocabulary and its byte-identity claim with the canonical skill copy
  still holds. No wording changed; verification metadata remains closeout-owned.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

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
