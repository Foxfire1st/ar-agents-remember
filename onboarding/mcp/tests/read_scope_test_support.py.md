# mcp/tests/read_scope_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/read_scope_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `a066550591eb3116ae008cc0d57f3558b0af52c5`|
| lastVerifiedCommitDate | 2026-09-18T07:03:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The read-scope fixture: the requirement's `P → I1`, `F1 → {I1, J1}`, `G1 → {J1, K1}` graph.** The
shared branching fixture already carries one invariant with two realizations, but the selective read is
decided by a topology that fixture does not have: a **sibling** invariant that one family shares with a
**second** family the seed never reaches. That shape *is* the stopping rule, so it is built here rather
than bent into the other fixture.

It is registered as the governed artifact **`mcp/tests/read_scope_test_support.py`** under contract
`knowledge-read-scope-cases` in `mcp/tests/evidence-lifecycle.toml`, with exactly three declared consumers
(the three read test modules) — a declared consumer list is checked against the source, so a fourth
importer must be added there in the same change.

## Code Commentary

### Logic

**Built through the public store operations, never by inserting rows**, so every identity in it is one the
real write path produced. The topology, and why each part exists:

- **`I1`** is the second revision of the retry-budget invariant and carries **two realization claims at two
  distinct source locations** (`src/integration.py` and `src/synchronization.py`) — the requirement's own
  conformance example.
- **`J1`** is the first revision of the candidate-batch invariant. It carries **two claims at one
  location** (`src/batch.py`), which is what makes "two claim identities, one distinct source location"
  measurable, and it is the sibling the frontier advertises.
- **`K1`** is the first revision of the source-resolution invariant, reachable **only** through `G1`.
- **`F1` is `{I1, J1}` and `G1` is `{J1, K1}`**, so `J1` is in both and `K1` is in the one the seed does
  not reach. That is the whole stopping rule in one graph.
- **`H1` is `{I1, L1}`**, a **second** family that directly contains `I1`, which is what proves the
  path/invariant rule includes *every* directly containing family rather than only the first.
- **`I1` also has two retained siblings**, `I0` (its predecessor) and `I2`, and **both successors display
  the same `v2` label**, which makes "a display version selects nothing" measurable rather than rhetorical.
- **`absent_anchor`** is a recorded claim whose path exists in no tree, and **`mismatch_anchor`** is a
  claim whose recorded blob identity is deliberately not the one the fixture repository holds at that
  path. Both are authored like any other claim: storage never resolves a source, so whether a path
  resolves is a fact about a snapshot and not a condition for recording it.

**The retry identity's ordering is partly authored, and a consumer must not assume otherwise.** The three
retry revision ids are allocated through `_ordered_revision_id` with deterministic prefixes (`9`, `3`, `6`)
and the predecessor is given `PREDECESSOR_LABEL` (`v3`) instead of `BASE_LABEL` (`v1`); every other
identity keeps random ids and `BASE_LABEL`. This is what makes the ordering case's label-versus-id
comparison deterministic. Before the fix round the assertion was true for only ~2 of 3 fixture draws —
because two successors share the `v2` label and a stable label sort can coincide with the id order — so the
leaf's own unit module was intermittently red. **A case that expected the predecessor to display `v1`, or
that relied on those three ids being random, must be re-read against this fixture.**

The fixture also commits a **real Git tree** beside the database (`src/integration.py`,
`src/synchronization.py`, `src/batch.py`, `src/resolution.py`, `src/anchors.py`, `src/timeout.py`,
`src/retry_adapter.py` and both `src/a1.py` / `src/a[1].py` for the glob-character case), because an anchor
observation is only meaningful against real committed bytes.

Public surface: `build_read_scope_fixture(...)` returns a `ReadScopeFixture` carrying the identity maps,
the paths, the labels, the recorded blob identities and the tree id; `make_read_authorship` builds the
authored provenance; `RevisionSeed` / `RealizationSeed` / `ReadFixtureFamily` / `ReadFixtureRealization`
are the small value types the builders pass around.

### Conventions

- Every write goes through the same public store operations production code uses — `store.py`,
  `families.py`, `memberships.py`, `realizations.py` — so a fixture defect is a storage defect and shows up
  as one.
- The real Git tree is built with `subprocess` against `tmp_path`; nothing touches the checkout.
- Blob identities are read back from the tree rather than hand-written, except where a claim is
  *deliberately* recorded against a different or absent blob.

### Invariants And Boundaries

- **The fixture is one graph, shared by the unit and integration modules**, so both lanes assert the same
  selection rather than two graphs that could drift. That is the artifact's declared permanence rationale.
- **The claims and their anchors are recorded through the typed write path**, so the fixture cannot author
  a spelling the storage boundary would refuse — which is also why the unaddressable-spelling case has to
  build its row outside that path.
- **Boundary.** This is test support. It is not execution evidence, it declares no lane, and it asserts
  nothing.

### Todos

None recorded. **`mcp/tests/read_scope_test_support.py` is 762 lines** — no ceiling applies to a support
module, but a successor adding scenarios should extend the builders rather than fork a second fixture.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The fixture's declared topology and why this graph and not the shared branching one.** | "The read-scope fixture" | mcp/tests/read_scope_test_support.py:1-31 |
| The graph constants: the labels, statements, conditions and the four direct family guarantees. | `RETRY_LABEL`; `BATCH_LABEL`; `RESOLUTION_LABEL`; `SHARED_SUCCESSOR_LABEL`; `FAMILY_LABEL`; `OVERLAPPING_FAMILY_LABEL`; `DIRECT_FAMILY_LABEL` | mcp/tests/read_scope_test_support.py:69-113 |
| The recorded paths, including the two the read is measured against (absent and mismatched). | `INTEGRATION_PATH`; `SYNCHRONIZATION_PATH`; `ABSENT_PATH`; `BATCH_PATH`; `MISMATCH_PATH` | mcp/tests/read_scope_test_support.py:115-131 |
| **The partly-authored retry ordering identity the fix round introduced, and the predecessor label that makes the ordering case deterministic.** | `_ordered_revision_id`; `PREDECESSOR_LABEL`; `_seed_identities` | mcp/tests/read_scope_test_support.py:255-264; mcp/tests/read_scope_test_support.py:102; mcp/tests/read_scope_test_support.py:286-357 |
| The public builder and the value types a case reads. | `build_read_scope_fixture`; `ReadScopeFixture`; `RevisionSeed`; `RealizationSeed`; `ReadFixtureFamily`; `ReadFixtureRealization` | mcp/tests/read_scope_test_support.py:266-284; mcp/tests/read_scope_test_support.py:174-241; mcp/tests/read_scope_test_support.py:142-153; mcp/tests/read_scope_test_support.py:154-164; mcp/tests/read_scope_test_support.py:165-173; mcp/tests/read_scope_test_support.py:133-141 |
| The graph builders, all through the public store operations. | `_build_invariants`; `_build_families`; `_build_realizations` | mcp/tests/read_scope_test_support.py:359-373; mcp/tests/read_scope_test_support.py:519-569; mcp/tests/read_scope_test_support.py:586-762 |
|**The governed-artifact and contract rows that make this module part of the catalog.**|"contract:knowledge-read-scope-cases"| mcp/tests/evidence-lifecycle.toml:1298-1298 |
|The three declared consumers, checked against the source (the row's consumer list names `mcp/tests/test_knowledge_read_paths.py`).|"contract:knowledge-read-scope-cases"| mcp/tests/evidence-lifecycle.toml:1298-1298 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T04:55:18+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1298-1298. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T04:55:18+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1298-1298. No content impact: mechanical anchor-range projection bound to citation source snapshot 116840615150c9097436b691cc4243186059d79f882e7a6c73cd85d688950e12; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1293-1293` -> `mcp/tests/evidence-lifecycle.toml:1294-1294`; `mcp/tests/evidence-lifecycle.toml:1293-1293` -> `mcp/tests/evidence-lifecycle.toml:1294-1294`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-18T02:37:44+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1293-1293. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T02:37:44+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1293-1293. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1292-1292. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1292-1292. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1269-1269. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1239-1239. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_paths.py" repointed to mcp/tests/evidence-lifecycle.toml:1245-1245. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read-scope fixture, and it is the artifact this leaf registered as `knowledge-read-scope-cases` in `mcp/tests/evidence-lifecycle.toml` (which is why the catalog counts moved to 10 contracts and 51 artifacts and the AST helper's pinned digest was re-pinned). The card records the topology and why each part exists (`I1` with two claims at two locations; `J1` with two claims at one location and the sibling role; `K1` reachable only through `G1`; `F1 = {I1, J1}` and `G1 = {J1, K1}`; `H1 = {I1, L1}` as the *second* directly containing family; the three retained retry revisions with two sharing a `v2` label), the real committed Git tree beside the database, and the fix round's partly-authored ordering identity with the forward warning that a case expecting the predecessor to display `v1`, or relying on those three ids being random, must be re-read. Verification metadata remains empty until closeout stamps the code commit.
