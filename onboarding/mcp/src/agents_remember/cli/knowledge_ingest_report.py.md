# mcp/src/agents_remember/cli/knowledge_ingest_report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest_report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T23:48:33Z |
| lastVerifiedCommitHash | `c114deaca13555f3c5121a7f5b803233b6bd866c` |
| lastVerifiedCommitDate | 2026-09-27T02:50:14+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Renders the ordinary knowledge-ingest report as JSON or human-readable text. It exposes per-entry outcomes, candidate/source identity, publication selection and independent published-identity readback; an exit status is not a publication result.

## Code Commentary

### Logic

`payload` preserves the report’s typed outcomes and both authored planes. `summary` renders the same facts for a reader, including absent publication and the chosen destination rather than silently treating either as success.

`_family_block` exposes guarantees, membership endpoints, no-family bases and coverage limits. Membership rows include `retainedFromMemberId`: a retained sibling can have state `added` because the successor edge is new while the invariant revision is unchanged. `_family_line` reports the count of retained revisions separately from added/reused/retired edge counts.

The renderer does not recompute the roster or publish knowledge. Null measured counts and recorded/projected/not-recorded states arrive from the coverage owner and retain their meaning. `publishedIdentity` may be absent, confirmed, mismatched or unavailable; those outcomes are not interchangeable.

### Conventions

The CLI entry resolves authorization and destination; this module only renders its report. Family and source report types are imported rather than redefined. JSON field additions propagate the measured vocabulary without introducing a store schema.

### Invariants And Boundaries

- Read every committed, ruling and refused entry; process exit is insufficient.
- Retention provenance identifies an old membership, while edge state describes the new one.
- Projected coverage cannot become a measured zero or publication success.
- Report rendering creates no record, assessment or acceptance authority.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| Render the complete structured operation and publication outcome. | `payload` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:79-128 |
| Render the human-readable report without inferring acceptance. | `summary` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:34-76 |
| Expose retainedFromMemberId beside each membership’s exact endpoints. | `_family_block` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:131-181 |
| Count retained revisions separately from added/reused/retired edges. | `_family_line` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:242-257 |
| Coverage owns the measured sibling arithmetic. | `_guarantee_outcomes` | mcp/src/agents_remember/application/curator_family_coverage.py:160-229 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): **one payload key renamed because its own name had
  become false, and this card's stale ranges re-derived against the candidate.** `contractPath` /
  `contract_path` became **`admissionSource` / `admission_source`** (`:44-44`, `:96-96`): the document
  a run is admitted under is a leaf enclosure contract for `knowledge-ingest` but a **settings
  document** for a taskless bootstrap, so a field called "contractPath" was a false statement about
  one of the two runs that produce this report. No test and no consumer read the old key. The card's
  Logic section was re-derived from each construct's own declaration on the 328-line candidate (the
  module was 205 lines at the extraction): `summary` `:34-76`, `payload` `:79-128`, the two plane
  blocks `:131-182`/`:183-214`, `_identity_line` `:215-223`, `_read_back_block` `:224-240`,
  `_family_line` `:241-257`, `_source_line` `:258-269`, `_targets` `:270-276`, `_counts` `:277-291`
  and `_outcome` `:294-328`. The invariant that a payload key is added rather than renamed was
  **corrected rather than left standing**, because this leaf is the one case where the old key's name,
  not its meaning, was the defect. **No verification stamp was advanced** — the candidate is
  uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed
  closeout owns the real code and memory commits.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **the report renders both planes.** `payload` gained a `family` block and a `sources` block and `summary` gained one line for each, and every plane carries its **own** state — `recorded`, `projected` or `not-recorded` — so a run that wrote nothing reports null counts rather than zeroes that would read as measured. The source block claims a path and a digest only for the state that actually wrote the manifest.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): created this one-to-one card for the new module. The 135-line report renderer moved out of `cli/knowledge_ingest.py` when `ICR-R20@v1` added two facts to the run's answer, and the extraction is what keeps both files under the repository's size rail: the command module keeps the *decision* surface (which invocation may proceed, which destination it selected) and this module owns the *shape* of what it says. The card records the two new payload fields and why `publishedIdentity`'s absence is a different fact from a `mismatch`, the unconditional publication-route line in the human rendering, the two explicit counts the requirement's boundary case reads, and the string-not-boolean rule the module's own docstring states for `reviewBaseline` and `publicationRoute`. Every range was derived from its construct's own extent in this candidate rather than carried. **Verification metadata:** the card names the production line it was read against — `71a4433e686b3380af97a0836bb82bab2c8f2aad`, this leaf's base — because the module exists only in this leaf's uncommitted candidate, so no commit contains the content a stamp would claim to have verified. That is a statement of *what the reading was against*; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp.

