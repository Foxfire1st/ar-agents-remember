# mcp/src/agents_remember/memory/knowledge/durable_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/durable_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:23:46+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a` |
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Publishing durable evidence, and the post-cleanup read-back that is the only proof it survived. This
module moves bytes to a named destination, records the reference a later reader needs, and reports
what it found when it read them back — a publication mechanism, not a claim about the artifact's
content.

## Code Commentary

### Logic

`publish_durable_evidence` builds its destination **from the task root only** — `_TASK_RELATIVE_REPORTS`
is `("notes", "reports")` under the task root, following the shipped curator-coherence route — hashes
the bytes and returns a `DurableEvidencePublication` carrying the exact destination, the digest, the
byte count and the file name; `reference` and `digest` are the machine-readable publication reference.
`_require_one_file_name` refuses any name that is not one plain file name, so `../escape.md`,
`sub/dir.md`, `..` and `""` are unrepresentable rather than merely discouraged.

`read_back_evidence` re-reads the destination and returns an `EvidenceReadBack` with a **state** —
`matched`, `missing`, `mismatched` or `unreadable` — rather than a boolean, because "the bytes are not
there" and "the bytes are different" are different facts and neither is "published". `blocked_reason`
renders the destination, the expected digest and the observed state for the failure direction.
`enclosure_reports_removed` is the read-back of the enclosure-local directory after cleanup.

`durable_reports_root(task_root)` is the **root itself, exported as a decision rather than a
convenience** (`:58-69`). The single-file publication above stays the route for one artifact; a producer
whose evidence is a **directory** of related files roots that directory here instead of restating the
path, because "the enclosure root and `<worktree_group>/` are both removed by cleanup, so a second module
that spelled this path for itself would be a second place where 'durable' could drift away from the one
that is". Its first consumer is the durable comparison generation, which publishes one directory per
generation under `<task_root>/notes/reports/comparison-generations/<leaf>/<generation-id>`; the function
returns exactly `Path(task_root).joinpath("notes", "reports")`, the same `_TASK_RELATIVE_REPORTS` value the
publisher builds its destination from, so the two cannot diverge.

### Invariants And Boundaries

- **The durable root has exactly one definition, and it is exported.** `durable_reports_root` returns
  `_TASK_RELATIVE_REPORTS` joined onto the task root, and it is the same value the single-file publisher
  builds its destination from; a directory-shaped producer (the comparison generation) roots itself here
  rather than spelling `notes/reports` again. Calling it does not publish anything and grants no name
  validation — that stays with `_require_one_file_name` on the publication path.
- **The destination is `<task_root>/notes/reports/`**, outside the enclosure root and outside
  `<worktree_group>/` by construction. `DURABLE_EVIDENCE_REFUSED_DESTINATIONS` names the two places a
  retention claim may not rest on — the enclosure's own `reports/` (removed at cleanup for a leaf
  contract) and the terminal enclosure archive (fixed content set) — so neither is reachable by
  accident and a case can assert neither is ever produced.
- **Retention is proven by a read-back, not by code inspection.** The measurement is mandatory rather
  than reassuring, which is why the publication records the digest *with* the destination.
- **A failed or mismatching read-back is a blocked terminal state**, never reported as published.
- Nothing here decides *what* the evidence says.

### Todos

- The terminal half of this module's own contract is an owning-seat operation: the post-cleanup
  read-back of a real leaf must be run after cleanup, which no code path can perform for itself. The
  seed half — publication, and the read-back mechanism in both directions — is measured by this
  leaf's cases.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The two destinations a retention claim may not rest on, named so neither is reachable by accident.** | `DURABLE_EVIDENCE_REFUSED_DESTINATIONS` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:50-52 |
| **The durable root, exported as the one decision a directory-shaped producer must root itself at.** | `durable_reports_root`; `_TASK_RELATIVE_REPORTS` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:58-69; mcp/src/agents_remember/memory/knowledge/durable_evidence.py:55-55 |
| **Its first consumer: the comparison generation, which derives its whole layout from this root rather than restating it.** | `comparison_generations_root`; `leaf_generation_root`; `generation_directory` | mcp/src/agents_remember/application/review_comparison_generation.py:524-527; mcp/src/agents_remember/application/review_comparison_generation.py:530-533; mcp/src/agents_remember/application/review_comparison_generation.py:536-539 |
| **The publication record a later reader is given: the exact destination, the digest, the byte count and the machine-readable reference.** | `DurableEvidencePublication` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:73-96 |
| **The publication itself: the destination built from the task root and the digest hashed from the bytes written.** | `publish_durable_evidence` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:137-166 |
| **The read-back result, whose state distinguishes "the bytes are not there" from "the bytes are different", and the blocked reason that renders the failure direction.** | `EvidenceReadBack` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:100-134 |
| **The read-back operation itself.** | `read_back_evidence` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:169-203 |
| The destination rule that makes a traversal or a nested name unrepresentable. | `_require_one_file_name` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:219-229 |
| The enclosure-local read-back the cleanup direction is measured with. | `enclosure_reports_removed` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:206-216 |
| The shipped curator-coherence route that owns "leaf evidence parked where it survives". | `curator_coherence_paths` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:10-19 |
| The cleanup that removes an enclosure-local `reports/` directory, which is why that path is refused. | `ENCLOSURE_REPORTS_DIRECTORY` | mcp/src/agents_remember/worktrees/modules/cleanup.py:53-53 |
| The terminal archive's fixed content set, which is why it is not widened. | `_is_canonical_artifact` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:533-538 |
| **The boundary cases that measure both directions: a published artifact reads back matched, a missing destination is blocked, and changed bytes are mismatched.** | `test_a_published_artifact_reads_back_with_its_published_digest`; `test_a_missing_durable_destination_reads_back_as_a_blocked_state`; `test_a_destination_whose_bytes_changed_reads_back_as_mismatched` | mcp/tests/test_knowledge_citation_boundaries.py:635-649; mcp/tests/test_knowledge_citation_boundaries.py:672-691; mcp/tests/test_knowledge_citation_boundaries.py:694-711 |
| The boundary case that proves the destination is outside the enclosure and the archive by construction. | `test_the_destination_is_outside_the_enclosure_and_the_archive_by_construction` | mcp/tests/test_knowledge_citation_boundaries.py:652-669 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The destination is a path under the
coordination task root, which is outside both the code and the memory repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-27T05:23:46+00:00 — Re-resolved 2 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T20:04:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): body updated for the one addition this leaf made to this module — `durable_reports_root(task_root)` (`58-69`), the durable root **exported as a decision**: the single-file publication stays the route for one artifact, while a producer whose evidence is a *directory* of related files roots that directory here instead of spelling `notes/reports` a second time. The card records why that matters rather than only what was added: the enclosure root and `<worktree_group>/` are both removed by cleanup, so a second spelling would be a second place where "durable" could drift away from the one that is; and the first consumer is the durable comparison generation, whose whole layout (`<task_root>/notes/reports/comparison-generations/<leaf>/<generation-id>`) derives from this function. Two invariants and three Repo-Internal rows were added, and the `DurableEvidencePublication` row's range moved `57-83`→`72-98` because the addition sits above it. **Stamp accounting:** the two fields now name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because the function exists only in this leaf's uncommitted candidate; the recorded working candidates state what was actually read, and closeout owns the real stamp once the code commit exists.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `curator_coherence_paths` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:161-170. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_a_published_artifact_reads_back_with_its_published_digest`; `test_a_missing_durable_destination_reads_back_as_a_blocked_state`; `test_a_destination_whose_bytes_changed_reads_back_as_mismatched` repointed to mcp/tests/test_knowledge_citation_boundaries.py:635-649; mcp/tests/test_knowledge_citation_boundaries.py:672-691; mcp/tests/test_knowledge_citation_boundaries.py:694-711. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_the_destination_is_outside_the_enclosure_and_the_archive_by_construction` repointed to mcp/tests/test_knowledge_citation_boundaries.py:652-669. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: `curator_coherence_paths` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:148-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the durable-evidence publication and its read-back. It records the three things a reader must not get wrong. **The destination is `<task_root>/notes/reports/`**, built from the task root, so the enclosure-local `reports/` directory and the fixed-content terminal archive are not reachable by accident — the module names both as refused destinations and a case asserts neither is ever produced. **Retention is proven by a read-back, not by inspection**, which is why publication records the digest together with the destination and why the read-back returns a state (`matched`/`missing`/`mismatched`/`unreadable`) rather than a boolean: "the bytes are not there" and "the bytes are different" are different facts and neither is "published". And **a failed or mismatching read-back is a blocked terminal state**, never reported as published. The card also records the one part of the contract no code path can perform for itself — the post-cleanup read-back of a real leaf is an owning-seat operation. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
