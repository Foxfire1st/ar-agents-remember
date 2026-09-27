# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:23:46+00:00 |
| lastVerifiedCommitHash |  `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`|
| lastVerifiedCommitDate |  2026-09-27T07:57:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns exact candidate-to-judgment set validation and lifecycle capture/revalidation of each cited
evidence file's digest.

## Code Commentary

### Logic

The publication owner copies admitted judgment evidence into its existing content-addressed task artifact root and stamps `evidenceArtifact` with path, SHA-256 and size. Authored `evidenceRef` and `evidenceSha256` remain unchanged. `read_judgment_evidence` validates that exact custody; an old explicit task citation can still be read at its durable address, while legacy code/memory without custody refuses rather than reading today's bytes. `require_recorded_judgments_current` separately rechecks original inputs for live readiness.

`exact_curator_judgments` rejects duplicates, missing tuples, and extra tuples, restores the
attestation's deterministic order, resolves every explicit evidence reference, and returns recorded
judgments with lifecycle-computed SHA-256 digests. `require_recorded_judgments_current` repeats the
digest observation inside the publication CAS window and refuses evidence races.

### Conventions

This module validates and binds agent-owned decisions; it never chooses a disposition or writes a
rationale. Evidence-read failures are translated into the coherence error family.

### Invariants And Boundaries

- Set equality is exact over all three candidate identity cells.
- Evidence content, not merely the path string, is candidate-bound.
- Missing or unreadable evidence fails publication; no alternate root is attempted.

### Todos

None recorded.

## Docs References

No configured external documentation applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-owned evidence contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact set coverage and lifecycle-computed digests are established together. | `exact_curator_judgments` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py:23-58 |
| CAS revalidation catches task evidence that changes independently of candidate trees. | `require_recorded_judgments_current` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py:130-148 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Publication retains exact admitted bytes without rewriting their authored citation. | `retain_judgment_evidence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py:61-92 |
| Historical reading uses recorded custody or the explicit legacy task address. | `read_judgment_evidence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py:95-127 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Evidence remains confined to contract-owned roots. | `resolve_curator_evidence_ref` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:37-68 |

## Update History

- 2026-09-27T05:23:46+00:00 — Re-resolved 2 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:56:35+00:00 — Documented owner-stamped evidence custody and preserved authored citations, legacy seals and strict live checks. Verification hashes/dates remain closeout-owned.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:614-645` -> `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:714-745`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `resolve_curator_evidence_ref` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:614-645. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-29T08:52+02:00 — Created for exact judgment coverage and evidence-byte CAS validation.
  Verification remains closeout-owned.
