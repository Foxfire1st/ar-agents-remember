# mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:23:46+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a` |
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout overview](overview.md)

## Purpose

**The cited evidence bytes' named destination, and the read-back that proves they survived.** One
destination is fixed for an assessment's cited bytes:

```text
<task_root>/notes/reports/evidence/<assessment_id>/<filename>
```

Three properties make that the right home, and each is a measurement rather than a preference: it is
the shipped durable precedent for exactly this property (the curator-coherence authority's own route
onto the coordination task root), it is **outside** the worktree group that terminal cleanup removes,
and the terminal enclosure archive **cannot** hold it — that archive's scanner admits a fixed content
set and refuses an unclassifiable canonical-root file with `terminal-archive-unowned-artifact`.

## Code Commentary

### Logic

Historical reading follows the publisher-recorded evidence-bytes destination edges inside the assessment's own directory. It does not reconstruct a basename from the authored citation: an admitted confined alias can resolve to a different source basename. Hash/confinement checks remain strict. `read_retained_evidence_byte` reuses the path/SHA/size value for retained judgment evidence without adding another evidence store.

`evidence_directory_for` derives the destination from the contract and the assessment identity.
`publish_assessment_evidence_bytes` writes each cited byte there, then **reads every one back before
it returns**: it opens the file by the recorded task-root-relative path and compares the recorded
digest. A failed read-back is a **blocked** terminal state — `AssessmentEvidenceBlockedError` carries
the exact destination, the expected digest and the observed state — and is never repaired by writing a
second copy, never re-homed into the terminal archive, and never reported as published.

`read_back_published_bytes` is the same verification as a standalone read, so a later reader can
re-prove survival without republishing. `AssessmentEvidencePublication.bytes` returns one
`PublishedEvidenceByte` per citation, each carrying its **own** citation and its **own** measurement,
so a caller never zips two parallel sequences and hopes the orders match.

The recorded destination is resolved through the **shipped** resolver `resolve_curator_evidence_ref`,
so the bytes a reader opens are the bytes that resolver already confines to a namespace root.

### Conventions

- A published byte is recorded on the assessment as three facts — task-root-relative path, digest and
  size — so `_resolve_recorded` can open it later without guessing.
- `_task_relative` refuses a path that is not task-relative; a byte is never recorded by an absolute
  path or by a path relative to a worktree that cleanup removes.
- Writes go through `atomic_write_bytes`, and `EVIDENCE_DIRECTORY` spells the destination once.

### Invariants And Boundaries

- **The published byte is a copy of the cited bytes, deliberately.** A citation may name a `code:` or
  `memory:` file inside a worktree that terminal cleanup removes, so the only way "the evidence bytes
  survive cleanup" can hold for such a citation is for the surviving tree to hold the bytes. What ties
  the copy to the citation is content: the recorded digest is computed **from the source that was
  read** before the copy is written, so a mismatch is a blocked item rather than a silently different
  file.
- **Survival is proven by reading back, never asserted.** No code path reports a byte published
  without having opened it again by its recorded path.
- **The destination is not a new durable store.** No widened archive, no blob store, no second copy
  and no second authority: this is the same task-root publication the canonical record uses, under the
  same conditions.
- **The record's own digest is not the bytes' read-back.** The assessment's content digest says
  nothing about the cited files, and it is never substituted for reading them.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured. The custody and namespace contract is grounded in the repository owners below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The named destination, derived from the contract and the assessment identity. | `EVIDENCE_DIRECTORY`; `evidence_directory_for` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:61-62; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:63-63; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:128-151 |
| Publication with the mandatory read-back, and the blocked state a failed read-back produces. | `publish_assessment_evidence_bytes`; `AssessmentEvidenceBlockedError` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:66-96; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:154-194 |
| The standalone read-back a later reader uses to re-prove survival. | `read_back_published_bytes` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:197-219 |
| The shipped resolver that confines every recorded destination to a namespace root. | `resolve_curator_evidence_ref` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:37-68 |
| The one terminal-archive admission rule the §6.6 destination is chosen against. | `_is_canonical_artifact` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:533-538 |

## KS-R15@v1 Evidence-Byte Destination

**The leaf that created this module.** `KS-R15@v1` §6.6 fixes the destination and the three recorded
facts; §6.7 requires the destination not to become a new durable store; §7.1–§7.3 require findings and
manifests to survive cleanup with survival **verified** rather than assumed; and §7.4 refuses a second
archive.

The two measurements the choice rests on, recorded so a later reader can re-take them rather than
trust them: terminal cleanup removes only `worktree_group/"reports"` and `worktree_group/".lifecycle"`
(`worktrees/modules/cleanup.py`, `_removed_directories`), so both destinations this leaf uses are
under `task_root` and outside that removal set; and the terminal archive's scanner admits a fixed
artifact set, so it could not hold these bytes even if they were offered to it.

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Recorded publisher destinations, including admitted aliases, are validated directly. | `read_assessment_evidence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:230-254 |
| The existing path, digest and size custody value is read back. | `read_retained_evidence_byte` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:222-227 |

## Cross-Repo References

No separate repository supplies this custody; all admitted namespaces are scoped by the leaf contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History

- 2026-09-27T05:23:46+00:00 — Re-resolved 1 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:58:33+00:00 — Reconciled retained evidence reading with actual publisher destinations and the shared custody value. Verification hashes/dates remain closeout-owned.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the assessment evidence-byte destination the leaf added — the
  `<task_root>/notes/reports/evidence/<assessment_id>/` home and the three reasons for it, the
  mandatory read-back that makes survival proven rather than asserted, the blocked state that never
  re-homes or reports a false publication, and why the published byte is deliberately a copy of the
  cited bytes. Verification metadata remains closeout-owned; no acceptance or certification claim is
  made.
