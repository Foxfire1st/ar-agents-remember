# mcp/src/agents_remember/memory/knowledge/realizations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/realizations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../../overview.md)

## Purpose

The realization relation: **what an exact source location does for an exact obligation.** A
realization claim cites one invariant revision and one source anchor and carries the author's role and
rationale. Neither is inferred — the role comes from the authored vocabulary and the rationale is the
author's sentence — so a graph-valid claim is still only a claim, and no reader may promote it into a
semantic verdict.

This module owns the `realization_claim` table and both read directions over it: by invariant revision
(forward) and by anchor (reverse). That is the requirement's falsifier made structural — the two
directions have to answer with the same claim identities because they are the same rows.

## Code Commentary

### Logic

- `create_realization_claim` computes the anchor identity before taking the lock, so a lock refusal
  still names it. Inside the transaction the endpoint check runs first, then `_record_anchor` decides
  the anchor's provenance: an existing anchor named by identity is looked up and refused if absent; a
  new anchor is constructed through `anchors.source_anchor_from_draft` and written by
  `anchors.insert_anchor_row` **inside this same transaction**. Since `KS-R03` the claim's own write is
  the in-transaction helper `insert_realization_claim`, which the candidate-change batch composes as
  well; it returns `None` for the one case that is a no-op (the identical claim already stored) and
  raises `KnowledgeRefused` for every other conflict, so the operation and the batch each decide what
  a no-op means in their own vocabulary (`no_change` for the single-record result, no receipt entry for
  the batch).
- The anchor write deliberately precedes the claim's own duplicate checks. A newly authored anchor and
  the claim about it are one act of authorship, so a refusal raised after that write rolls the anchor
  back instead of leaving an orphan location behind.
- The claim's own checks follow the package order: an identical re-declaration is `no_change`; the same
  `claim_id` sealing a different row is `duplicate_identity`; the same
  (invariant revision, anchor) pair is `relationship_constraint`; then the insert and the
  referential-integrity check.
- `list_claims_for_invariant_revision` and `list_claims_for_anchor` select the same claim columns from
  the same table. There is no derived store, no cache and no second list anywhere in the package.
- `remove_realization_claim` requires the caller's expected row digest; a mismatch is
  `stale_precondition`, and the earlier dataset keeps the removed row. Both checks live in the
  in-transaction `delete_realization_claim`, which the batch composes.

### Conventions

- `_requested_anchor_id` is what makes "name an existing anchor" and "record a new one" different
  inputs to the same operation: the request carries an `AnchorEndpoint` union, and this helper
  resolves which arm it is without duplicating the union's meaning.
- Role and rationale are copied from the draft into the stored row verbatim; the module never
  normalizes, defaults or completes them.
- The two `detail` strings for the duplicate-pair refusal are supplied by this module, because the
  same factory serves both relation kinds and only the caller knows which pair it is refusing.

### Invariants And Boundaries

- **A graph-valid claim is not a semantic verdict.** The role is authored vocabulary with an explicit
  `unclassified` member, the rationale is authored prose, and nothing in the read path derives either
  from the source file.
- **A new anchor and its claim are one transaction.** A late refusal leaves no anchor row behind; this
  is proven by table counts rather than asserted.
- **One claim per (invariant revision, anchor) pair**, guaranteed by the declared unique tuple and
  pre-checked so the refusal names the stored identity.
- **The reverse read is the same rows.** The `claim_id` values returned from either direction are the
  stored identities, which is why the two can be compared as sets.
- **Removal is explicit and never repoints**, and the baseline dataset retains the removed claim.
- **The in-transaction helpers assume the caller's transaction.** `insert_realization_claim` and
  `delete_realization_claim` write through `store.write` and are composed by the single-record
  operation and by the batch; nothing enforces that a caller holds the lock and the transaction.
- **A claim that records its own anchor is two written rows.** The batch's receipt reports both (the
  claim and the anchor), and the anchor's digest is read from the stored row rather than derived from
  the request.
- **Not this module's job.** The anchor's own lifetime and removal (`anchors.py`), memberships
  (`memberships.py`), and anchor *resolution* against a selected snapshot (`KS-R07`). Nothing here
  decides behavioral relevance or traverses the graph; the finite traversal policy is `KS-R07` and the
  before/after union is `KS-R08`.

### Todos

None recorded for this slice. The five `remove_*`/`create_*` operations are reachable from the
application seam but have no non-test importer above it yet, which is the correct `KS-R03` position
rather than a debt of this module.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The claim operation, including the anchor endpoint decision and the anchored transaction grouping. | `create_realization_claim`; `_insert_claim` | mcp/src/agents_remember/memory/knowledge/realizations.py:61-83; mcp/src/agents_remember/memory/knowledge/realizations.py:84-91 |
| The in-transaction claim insert both the operation and the batch command compose, with its `None`-means-no-op answer. | `insert_realization_claim` | mcp/src/agents_remember/memory/knowledge/realizations.py:93-141 |
| The in-transaction anchor recording (existing lookup, absent refusal, new-anchor write). | `_record_anchor` | mcp/src/agents_remember/memory/knowledge/realizations.py:144-179 |
| The endpoint-union resolution that separates naming an anchor from recording one. | `_requested_anchor_id` | mcp/src/agents_remember/memory/knowledge/realizations.py:321-326 |
| The forward read (invariant revision to claims). | `list_claims_for_invariant_revision` | mcp/src/agents_remember/memory/knowledge/realizations.py:271-286 |
| The reverse read (anchor to claims) over the same rows. | `list_claims_for_anchor` | mcp/src/agents_remember/memory/knowledge/realizations.py:288-301 |
| The explicit removal with its expected-row-digest contract, and the in-transaction helper the batch composes. | `remove_realization_claim`; `_delete_claim`; `delete_realization_claim` | mcp/src/agents_remember/memory/knowledge/realizations.py:181-201; mcp/src/agents_remember/memory/knowledge/realizations.py:203-210; mcp/src/agents_remember/memory/knowledge/realizations.py:212-244 |
| The batch command that composes the claim insert and reports its two written rows. | `_add_claim` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:435-457 |
| The stored anchor construction and narrow write hook the claim transaction reuses. | `source_anchor_from_draft`; `insert_anchor_row` | mcp/src/agents_remember/memory/knowledge/anchors.py:82-97; mcp/src/agents_remember/memory/knowledge/anchors.py:99-119 |
| The row codec and expected-row digest for the claim relation. | `claim_row`; `claim_row_digest`; `decode_claim_row` | mcp/src/agents_remember/memory/knowledge/records.py:429-440; mcp/src/agents_remember/memory/knowledge/records.py:441-462; mcp/src/agents_remember/memory/knowledge/records.py:463-483 |
| The closed authored role vocabulary and the explicit unclassified member. | `RealizationRole`; `UNCLASSIFIED_ROLE` | mcp/src/agents_remember/models/knowledge/graph.py:36-44; mcp/src/agents_remember/models/knowledge/graph.py:46-46 |
| The claim vocabulary and its two read shapes. | `RealizationClaimDraft`; `RealizationClaim`; `RealizationClaims`; `AnchorRealizations` | mcp/src/agents_remember/models/knowledge/graph.py:65-85; mcp/src/agents_remember/models/knowledge/graph.py:87-94; mcp/src/agents_remember/models/knowledge/graph.py:112-118; mcp/src/agents_remember/models/knowledge/graph.py:120-129 |
| The declared `realization_claim` table, its two indexes and its no-rewrite trigger. | `realization_claim`; `realization_claim_invariant_revision`; `realization_claim_anchor`; `realization_claim_no_rewrite` | mcp/src/agents_remember/memory/knowledge/schema.py:297-315; mcp/src/agents_remember/memory/knowledge/schema.py:329-331; mcp/src/agents_remember/memory/knowledge/schema.py:330-331; mcp/src/agents_remember/memory/knowledge/schema.py:395-399 |
| The requirement this module's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it. | — | — |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **extended this card for the batch composition it enabled.** The claim's write is now the in-transaction helper `insert_realization_claim`, returning `None` for the identical-claim no-op and refusing every other conflict, and the removal's two checks moved into `delete_realization_claim`; the card records the `None`-means-no-op contract because the two callers translate it differently (a `no_change` result versus no receipt entry), and that a claim recording its own anchor produces **two** written rows in the batch receipt. Also recorded that both helpers assume the caller's lock and transaction, with nothing enforcing it. Citation ranges were re-derived; the `governingOverview` link was repaired from `../../overview.md` to the three-level path. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new realization module. It records the authored-not-inferred rule as the module's central boundary (a graph-valid claim stays a claim), the anchored transaction grouping that makes an orphan anchor impossible on a refusal path, the one-claim-per-pair guarantee, and the structural reason the forward and reverse reads cannot disagree — they select the same claim columns from the same table. Verification metadata remains empty until closeout stamps the code commit.
