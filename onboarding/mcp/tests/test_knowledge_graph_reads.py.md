# mcp/tests/test_knowledge_graph_reads.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_graph_reads.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

Focused behaviour of the graph reads: **one relation, two directions, one set of identities.** Each
case protects a read contract — the forward query from an invariant revision and the reverse query from
an anchor must answer with the same stored claim identities, a family query must return the same
membership rows from either side, a recorded location whose source is unavailable must still read back
in full, and a removed relation must remain observable on the side that still has it. There is no
second index behind these reads, and that is what the identity comparisons check.

## Code Commentary

### Logic

- `test_two_realizations_resolve_from_either_direction_with_the_same_claim_ids` is the requirement's
  own demonstration: one invariant with two recorded implementations, enumerated from the invariant and
  from each anchor, compared as **identity sets** rather than by count. Its docstring names the failure
  it exists for — two independently maintained lists answering the same question with different
  identities, or a reverse view that invents its own copy of an edge.
- `test_overlapping_families_answer_both_directions_with_the_same_member_ids` is the frontier case:
  F={I1,J1} and G={J1,K1} mean the invariant-to-families direction returns memberships from two
  families, and the case compares the same stored `member_id` set from both sides.
- The two locator cases (`..._an_absent_source_anchor_is_retained_exactly_as_authored` and
  `..._a_symbol_locator_is_stored_and_read_back_while_no_resolver_supports_it`) are the
  storage-versus-resolution separation made executable: a path that exists in no snapshot and a
  `symbol` locator both round-trip byte-for-byte, and no resolver is reachable from either path.
- `test_a_removed_claim_stays_in_the_baseline_and_is_absent_from_the_successor` is the historical-
  meaning node: the same claim is present in the baseline handle and absent from the cloned successor,
  which is what makes an "always current" pointer unnecessary.
- `test_a_family_revision_read_reports_the_family_it_belongs_to` covers the revision-to-family read the
  endpoint and predecessor checks depend on.

### Conventions

- Every case reopens the database and compares **sets of stored identities**; none compares counts as
  a proxy for agreement, because a count can agree while the identities differ.
- The successor dataset comes from `knowledge_graph_test_support.build_removed_relation_successor`, so
  the before/after pair is built by one shared path rather than per case.
- Locator cases use the shared `AnchorSeed`/`anchor_draft` builders so the locator kind is the only
  varying input.

### Invariants And Boundaries

- **Both directions read the same rows.** The read models return stored claim and member rows, so
  identity equality across directions is structural rather than maintained.
- **A recorded location is retained exactly as authored.** A missing source changes what a later
  resolver reports, never what the store returns.
- **A removal is visible as a difference between datasets**, not as a mutation of the earlier one.
- **Boundary.** This module owns the read contract. The write rules are
  `test_knowledge_relation_rules.py`, the family revision rules are
  `test_knowledge_family_revision.py`, and the payload seals are `test_knowledge_revision_seals.py`.
  Anchor *resolution* is unimplemented by design and is `KS-R07`'s, so nothing here asserts a resolved
  match.

### Todos

None recorded for this slice. The two locator cases assert the current honest behaviour (stored, not
resolved); when `KS-R07` adds resolution, the assertions belong in that leaf's own module rather than
being retrofitted here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The read contract this module's cases protect, stated as one relation with two directions. | "one relation, two directions, one set of identities" | mcp/tests/test_knowledge_graph_reads.py:1-1 |
| The requirement's own demonstration node, compared as identity sets. | "test_two_realizations_resolve_from_either_direction_with_the_same_claim_ids" | mcp/tests/test_knowledge_graph_reads.py:35-65 |
| The overlapping-family frontier node. | "test_overlapping_families_answer_both_directions_with_the_same_member_ids" | mcp/tests/test_knowledge_graph_reads.py:66-99 |
| The two storage-versus-resolution nodes. | "test_an_absent_source_anchor_is_retained_exactly_as_authored"; "test_a_symbol_locator_is_stored_and_read_back_while_no_resolver_supports_it" | mcp/tests/test_knowledge_graph_reads.py:100-121; mcp/tests/test_knowledge_graph_reads.py:122-158 |
| The historical-meaning node over a real before/after pair. | "test_a_removed_claim_stays_in_the_baseline_and_is_absent_from_the_successor" | mcp/tests/test_knowledge_graph_reads.py:159-194 |
| The revision-to-family read node. | "test_a_family_revision_read_reports_the_family_it_belongs_to" | mcp/tests/test_knowledge_graph_reads.py:195-220 |
| The forward and reverse reads the cases compare. | `list_claims_for_invariant_revision`; `list_claims_for_anchor`; `list_members`; `list_families_for_invariant_revision` | mcp/src/agents_remember/memory/knowledge/memberships.py:255-267; mcp/src/agents_remember/memory/knowledge/memberships.py:270-284; mcp/src/agents_remember/memory/knowledge/realizations.py:271-285; mcp/src/agents_remember/memory/knowledge/realizations.py:288-300 |
| The before/after pair builder this module consumes. | `build_removed_relation_successor` | mcp/tests/knowledge_graph_test_support.py:217-265 |
| The locator union whose kinds the cases vary. | `SymbolLocator`; `FileLocator`; `LineRangeLocator` | mcp/src/agents_remember/models/knowledge/source.py:58-78; mcp/src/agents_remember/models/knowledge/source.py:37-42; mcp/src/agents_remember/models/knowledge/source.py:43-57 |
| The unit-regression lane row this module is registered by. | "mcp/tests/test_knowledge_graph_reads.py" | mcp/tests/test-evidence-lanes.toml:98-98 |
|  The fixture contract that names this module as an exact consumer. | "contract:knowledge-identity-branching-fixture" | mcp/tests/evidence-lifecycle.toml:1192-1192  |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1192-1192. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 1 enforced `citation_anchor_absent_from_range` row in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1190-1190` → `mcp/tests/evidence-lifecycle.toml:1190-1191` (row 99). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1190-1190. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1187-1187. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_graph_reads.py" repointed to mcp/tests/test-evidence-lanes.toml:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_graph_reads.py" repointed to mcp/tests/test-evidence-lanes.toml:96-96. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_graph_reads.py" repointed to mcp/tests/test-evidence-lanes.toml:94-94. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1183-1183. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_graph_reads.py" repointed to mcp/tests/test-evidence-lanes.toml:81-81. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_knowledge_graph_reads.py`, `list_claims_for_invariant_revision`, `list_claims_for_anchor`, `list_members`, `list_families_for_invariant_revision`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_graph_reads.py`, `list_claims_for_invariant_revision`, `list_claims_for_anchor`, `list_members`, `list_families_for_invariant_revision`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/memory/knowledge/realizations.py:271 to the row 95 of this card as the citation for `list_claims_for_invariant_revision`: no cited file carried the construct, and the checker named line(s) [271, 373] in this file as its live location; added mcp/src/agents_remember/memory/knowledge/memberships.py:255 to the row 95 of this card as the citation for `list_members`: no cited file carried the construct, and the checker named line(s) [255, 348] in this file as its live location

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `list_claims_for_invariant_revision` in the row 95 of this card from mcp/src/agents_remember/memory/knowledge/realizations.py:288-289 to mcp/src/agents_remember/memory/knowledge/realizations.py:271-273, the extent of the construct the claim is about (the checker named line(s) [271, 373] as its live location); re-pointed `list_members` in the row 95 of this card from mcp/src/agents_remember/memory/knowledge/memberships.py:270-272 to mcp/src/agents_remember/memory/knowledge/memberships.py:255-256, the extent of the construct the claim is about (the checker named line(s) [255, 348] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `list_claims_for_anchor` in the row 95 of this card from mcp/src/agents_remember/memory/knowledge/realizations.py:271-273 to mcp/src/agents_remember/memory/knowledge/realizations.py:288-289, the extent of the construct the claim is about (the checker named line(s) [288, 372] as its live location); re-pointed `list_families_for_invariant_revision` in the row 95 of this card from mcp/src/agents_remember/memory/knowledge/memberships.py:255-256 to mcp/src/agents_remember/memory/knowledge/memberships.py:270-272, the extent of the construct the claim is about (the checker named line(s) [270, 347] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/memory/knowledge/memberships.py:270-272 in the row 95 of this card; the repetition added no pooled evidence; kept one copy of the repeated citation mcp/src/agents_remember/memory/knowledge/realizations.py:288-289 in the row 95 of this card; the repetition added no pooled evidence

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new graph-read test module. It records that the falsifier is identity-set equality rather than a count comparison, the overlapping-family frontier case, the two nodes that make storage-versus-resolution executable, and the before/after pair that shows a removal without inventing an always-current pointer. Verification metadata remains empty until closeout stamps the code commit.
