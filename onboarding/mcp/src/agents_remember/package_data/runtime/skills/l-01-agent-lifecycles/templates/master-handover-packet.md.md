# l-01-agent-lifecycles/templates/master-handover-packet.md

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

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

## Evidence

### Repo-Internal References

This bundle copy is the shape the manager job posts at master exit; it references the master-exit verdict artifact and feeds the orchestrator's C-11 integration.

- Sync-propagated bundle copy of the canonical templates source. [1]
- The manager posts this packet to the orchestrator at master exit; the manager's durable handoff artifact is this packet, validated by the orchestrator. [2]
- The required verdict slot references the independent master-exit adversarial verdict artifact bound to the proposed candidate. [3]
- The router lists the master-handover packet among the templates the spawning seats compile from. [4]
- This template and `verdict.md` are both declared among the manager's templates in the composition manifest. [5]

### Cross-Repo References

No sibling repository evidence is needed for this report template.

No meaningful cross-repo references found.

### 260821-DAGQC-L4 Canonical Evidence References

The packet's table indexes the authoritative ledger/commit rows without repeating their commit
values. The receiving orchestrator must resolve every candidate-tree, code-ancestry,
memory-ancestry, verdict, and per-leaf ledger ref and confirm that it belongs to the same proposed
candidate. Missing, stale, unresolvable, or candidate-mismatched evidence blocks handover; packet
summary prose cannot override it.

## 260815-DAG-L2 Nature-Aware Handover

The handover names `executionNature`, prior landed organizational leaf refs plus the proposed final
leaf, and the exact proposed candidate tree/ref; an atomic handover names its isolated branch and
tree. The one full gate boundary is before the final organizational ref movement or during atomic
block landing. Candidate/code/memory ancestry and per-leaf ledger/commit evidence use canonical
stable refs with row ids or JSON pointers, never branch names, bare assertions, or copied maps.
Carry-over remains a documented recovery fact, never the normal landing strategy.
