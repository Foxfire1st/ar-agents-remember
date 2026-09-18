# mcp/tests/knowledge_graph_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_graph_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec`|
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

Shared builders and probes for the graph test modules. Three focused test modules exercise the
family, anchor, membership and realization behaviour, and they all build their inputs the same way:
**through the public typed operations**, with the fixture's own provenance envelope. This module owns
that construction plus the two probing helpers a refusal case needs — whole-database row counts, and
the raw write that can construct a state the operation forbids.

It is test support, not production code: it decides nothing, and the seed objects exist so a call site
reads as one authored record rather than as a row of positional arguments.

## Code Commentary

### Logic

- The four seed dataclasses (`FamilySeed`, `ClaimSeed`, `MemberSeed`, `AnchorSeed`) carry the values a
  case varies; the `*_draft` / `*_request` builders turn a seed into the model the public operation
  takes. Each seed has a `field(default_factory=uuid4)` identity, so a case that does not care about
  the identity still gets a fresh one.
- `family_draft` and `sealed_family` are the two family construction paths: the draft for an operation
  call, the sealed revision when a case needs the exact stored bytes.
- `claim_request` and `member_request` go through the fixture's admitted application seam, so a case
  cannot accidentally bypass the provenance rule the seam enforces.
- `table_counts` reads every declared canonical table's row count in one pass, which is how a refusal
  case proves "nothing was written" instead of asserting it.
- `insert_raw_family_revision` and `insert_raw_family_edge` write the raw rows a *refusal* case needs:
  the operation cannot construct a stored cycle (admission requires every predecessor to exist and the
  vocabulary refuses a self-referencing payload), so the cyclic state the lineage rule is exercised
  against has to be written by hand.
- `build_removed_relation_successor` produces a real before/after pair: it clones the closed database,
  removes one claim through the public removal operation, and returns both handles, so a case can show
  the same claim present in the baseline and absent from the successor.

### Conventions

- The module is registered with the evidence-lifecycle registry as `knowledge-graph-case-support`
  (`mcp/tests/evidence-lifecycle.toml`), with an exact consumer list of the three graph modules. A new
  importer must be added to that registry row, and `load_evidence_inventory` refuses the mismatch.
- Imports of the fixture come from `knowledge_fixture_test_support` rather than from a local copy, so
  the graph half extends L1's one builder instead of forking it.
- `DEFAULT_CLAIM_RATIONALE` exists so a case that is not about the rationale still authors a real one,
  which keeps the "rationale is authored" rule visible at every call site.

### Invariants And Boundaries

- **Every fixture value is built through the public typed operations**, except the two raw writes whose
  entire purpose is to construct a state the operations forbid. Support that built rows directly would
  prove only that a hand-written row decodes.
- **The raw writes are the only place a cycle can be created**, and they exist for the refusal cases on
  both lineage graphs.
- **The backup clone is a copy, not a snapshot mechanism.** It is fixture-local support for a
  before/after comparison; the real snapshot and publication machinery is `KS-R04`'s. A later leaf
  replacing it must keep the "baseline handle and successor handle" shape the read nodes expect.
- **Test support decides nothing about the graph.** No production module imports this file, and it must
  not become a place where a graph rule is defined.
- **Boundary.** This module is not a production seam and is not part of the storage package's ownership
  boundary; it lives under `mcp/tests/**` because that is the governed artifact root the registry
  discovers.

### Todos

None recorded for this slice. The clone helper is deliberately fixture-local and is the piece a later
snapshot leaf is expected to supersede.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The through-the-public-operations rule this support module exists to enforce. | "through the public typed operations" | mcp/tests/knowledge_graph_test_support.py:4-5 |
| The four seed shapes a case varies. | `FamilySeed`; `ClaimSeed`; `MemberSeed`; `AnchorSeed` | mcp/tests/knowledge_graph_test_support.py:65-74; mcp/tests/knowledge_graph_test_support.py:75-85; mcp/tests/knowledge_graph_test_support.py:86-94; mcp/tests/knowledge_graph_test_support.py:95-102 |
| The draft builders each case calls. | `anchor_draft`; `family_draft`; `sealed_family` | mcp/tests/knowledge_graph_test_support.py:103-120; mcp/tests/knowledge_graph_test_support.py:121-135; mcp/tests/knowledge_graph_test_support.py:136-145 |
| The request builders that go through the admitted seam. | `claim_request`; `member_request` | mcp/tests/knowledge_graph_test_support.py:146-161; mcp/tests/knowledge_graph_test_support.py:162-175 |
| The whole-database probe a refusal case uses to prove nothing was written. | `table_counts` | mcp/tests/knowledge_graph_test_support.py:176-184 |
| The two raw writes that construct the state the operations forbid. | `insert_raw_family_revision`; `insert_raw_family_edge` | mcp/tests/knowledge_graph_test_support.py:185-190; mcp/tests/knowledge_graph_test_support.py:191-201 |
| The before/after pair builder and the clone it is built on. | `build_removed_relation_successor`; `_clone_closed_database` | mcp/tests/knowledge_graph_test_support.py:217-265; mcp/tests/knowledge_graph_test_support.py:269-286 |
| The shared L1 fixture this module extends rather than forks. | `BranchingKnowledgeFixture`; `build_branching_knowledge_fixture` | mcp/tests/knowledge_fixture_test_support.py:160-186; mcp/tests/knowledge_fixture_test_support.py:203-261 |
|The registry contract and artifact row that declare this module's owner, fidelity and exact consumers.|"contract:knowledge-graph-case-support"| mcp/tests/evidence-lifecycle.toml:1212-1212 |
| The lane registration that keeps this support module's consumers collectable. | "mcp/tests/test_knowledge_family_revision.py" | mcp/tests/test-evidence-lanes.toml:96-96 |
|  The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. | "contract:knowledge-graph-case-support" | mcp/tests/evidence-lifecycle.toml:1212-1212  |
| The lane registration that keeps this support module's consumers collectable. | "mcp/tests/test_knowledge_family_revision.py" | mcp/tests/test-evidence-lanes.toml:96-96 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
|  The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. | "contract:knowledge-graph-case-support" | mcp/tests/evidence-lifecycle.toml:1212-1212  |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:96-96. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:96-96. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:94-94. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:94-94. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-graph-case-support" repointed to mcp/tests/evidence-lifecycle.toml:1212-1212. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:92-92. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-graph-case-support" repointed to mcp/tests/evidence-lifecycle.toml:1212-1212. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:92-92. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-graph-case-support" repointed to mcp/tests/evidence-lifecycle.toml:1212-1212. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:79-79. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:knowledge-graph-case-support" repointed to mcp/tests/evidence-lifecycle.toml:1085-1085. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_revision.py" repointed to mcp/tests/test-evidence-lanes.toml:79-79. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 9 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_knowledge_family_revision.py`, `contract:knowledge-graph-case-support`, `BranchingKnowledgeFixture`, `build_branching_knowledge_fixture`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_family_revision.py`, `BranchingKnowledgeFixture`, `build_branching_knowledge_fixture`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1061-1078` -> `mcp/tests/evidence-lifecycle.toml:1079-1079`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new shared graph support module. It records the through-the-public-operations rule and the two deliberate exceptions (the raw writes that construct the cyclic state the operations forbid), the whole-database count probe that makes "a refusal wrote nothing" checkable, the fixture-local status of the backup clone that `KS-R04` is expected to supersede, and the registry contract that fixes this module's owner and exact consumers. Verification metadata remains empty until closeout stamps the code commit.
