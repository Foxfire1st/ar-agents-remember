# mcp/src/agents_remember/memory/knowledge/requirement_owner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/requirement_owner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `a066550591eb3116ae008cc0d57f3558b0af52c5` |
| lastVerifiedCommitDate | 2026-09-18T07:03:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The one place this record group asks the task plane.** `KS-R19@v1` requirement 2.3 forbids the
substrate from re-implementing the owner's resolution: the owner's answer is *consumed*, never
re-derived. This 82-line module is that consumption and nothing else — it is the entire reason the
task plane and the knowledge plane can meet without either one owning the other's rule.

**Why it is its own module.** The requirement is a boundary, and a boundary stated as a module is
checkable: exactly one import of the task plane exists for this record group
(`from agents_remember.tasks.task_intent import _approved_packet_ref`, line 58), and every other
module in the record group is therefore free of task-plane knowledge by construction.

## Code Commentary

### Logic

- `consume_owner_resolution(task_root, reference)` (61-82) is the whole public surface. It re-types
  the substrate's `RequirementOwnerRef` into the **owner's own**
  `ApprovedRequirementPacketRef(path, stableId, version)` (71-73) so the two sides compare literally
  rather than through a translation that could disagree, then calls the owner's resolver.
- An owner refusal becomes data, not an error: `except TaskIntentError` (74-81) returns
  `RequirementOwnerResolution(state="unresolved", refusal_code=owner_refusal.status,
  refusal_detail=owner_refusal.detail)`, **both verbatim from the owner**. A successful resolution
  returns `state="resolved"` (82). This module constructs no refusal of its own, so there is no
  second place a refusal can be invented.
- **The owner's normalized path is deliberately discarded.** Only the outcome is kept, so the stored
  reference stays the caller's own bytes. That is what makes "the reference is never rewritten" a
  total rule rather than one that holds for a refusal and fails for a success, and it also keeps the
  record's address identical to the address the caller reached it by.

### Conventions

- The private owner resolver `_approved_packet_ref` is imported under its leading-underscore name on
  purpose: the alternative is a second, public resolver whose answer could drift from the owner's, so
  the module takes the real one and pays for it with a private dependency rather than copying the rule.
- The module reads the task-plane packet on disk through the owner's resolver; it holds no connection
  to the knowledge store, takes no lock and starts no transaction.

### Invariants And Boundaries

- **No re-derived answer.** The three owner components are compared by the owner's own resolver against
  the owner's own file, so an absence, a non-Markdown path, a path outside the task root and a
  metadata mismatch are all the owner's refusals with the owner's codes — the substrate never guesses
  which of those facts is true.
- **An unresolved owner is representable and travels as data.** Because the refusal is carried rather
  than raised, a caller can store "the owner refused, for this reason" as the revision's consumed
  resolution, which is what requirement 2.4 asks for; the derived currentness view then reports
  `unresolved-owner` instead of a comparison it could not make.
- **No write, no policy.** This module adds no validation the owner should have made and no
  confinement the payload does not have: a path the owner would refuse is still *representable* in
  the payload, so the refusal can only come from the owner.
- **Boundary.** The record group's operation surface does not call this module — a caller obtains the
  resolution here and passes it into the payload as data (`requirements.py:11` names the module in
  prose only). Nothing here owns the payload shape, the envelope, or the store.

### Todos

None recorded. The reachability fact is worth a reader's attention: **no production module imports
this module**, so an unresolved-owner state reaches storage only when a caller obtained it here
first. There is no MCP tool or serving route for the record group yet.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The whole consumption: the reference re-typed into the owner's own shape, the owner asked, the answer carried as data.** | `consume_owner_resolution` | mcp/src/agents_remember/memory/knowledge/requirement_owner.py:61-82 |
| The single private task-plane import that makes this module the record group's only boundary to the task plane, and the one call site it feeds. | `consume_owner_resolution` | mcp/src/agents_remember/memory/knowledge/requirement_owner.py:61-82 |
|The owner's own reference shape, which is what the two planes are made to compare literally instead of through a translation.|`ApprovedRequirementPacketRef`| mcp/src/agents_remember/models/task_intent/__init__.py:22-38 |
|The owner's refusal carrier, whose `status` and `detail` travel verbatim into the resolution value.|`TaskIntentError`| mcp/src/agents_remember/errors.py:88-97 |
|The substrate's resolution value: one outcome, and a refusal only in the unresolved outcome.|`RequirementOwnerResolution`| mcp/src/agents_remember/models/knowledge/requirement.py:140-171 |
|The three components the owner reference carries, which this module re-types rather than re-spells.|`RequirementOwnerRef`| mcp/src/agents_remember/models/knowledge/requirement.py:116-139 |
| **The case that makes "the reference is never rewritten" total: four real owner refusals carried verbatim, with the stored reference byte-identical.** | "test_each_owner_refusal_is_carried_verbatim_and_leaves_the_reference_unrewritten" | mcp/tests/test_knowledge_requirement_reference_contract.py:435-499 |
| The case that keeps the refusal the owner's: paths the owner would refuse are still representable, so the answer cannot come from the substrate. | "test_the_payload_does_not_police_the_reference_the_owner_owns" | mcp/tests/test_knowledge_requirement_reference_contract.py:259-276 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): created this one-to-one card for the record group's task-plane boundary. It records the boundary as the module's whole subject — one private import of the owner's resolver, an answer consumed rather than re-derived — and the two decisions a future reader would otherwise have to guess at: the reference is **re-typed into the owner's own `ApprovedRequirementPacketRef` so the planes compare literally** rather than through a translation that could disagree, and **the owner's normalized path is deliberately discarded** so the stored reference is byte-identical to the caller's under every outcome, refusal and success alike. It also records the reachability fact that keeps this module's role honest: no production module imports it, so an unresolved-owner state reaches storage only when a caller obtained it here and passed it in as payload data. Verification metadata advances to the leaf's base commit `e963a01c` because the body was read against the current source; the code commit does not exist yet and closeout owns that stamp.
