# mcp/tests/test_knowledge_registered_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_registered_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:25+02:00 |
| lastVerifiedCommitHash |  `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate |  2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The 14 `unit-regression` cases that pin `KS-R16@v1` §1: the construction of the registered review
scope from recorded links and one declared policy version.** The module owns that construction in use —
the declaration vocabulary, the followed edges with the snapshot each was read from, the resolved policy
identity, the resolved membership, and the refusals that name an exact missing input — and it owns the
negative half of the same act: a declaration whose input cannot be resolved is a refusal, never a
smaller scope reported as the declared one. **It deliberately owns nothing about a run *over* the
scope.** What a detection run could not resolve is `KS-R14@v1`'s record; no case here drives the
retrieval read, asserts a pipeline outcome, or adds a refusal code. Every case is hermetic: one
module-scoped two-snapshot fixture, built in a temporary directory through the production writers over
in-process knowledge stores, and no process, publication or Git object.

## Code Commentary

### Logic

The file is a fixture and then two groups of cases, and it says so with a section comment above each
group. The fixture is the module's own two-snapshot construction. `POLICY_ID` is taken from the shipped
policy module rather than spelled, and `DECLARED_VERSION` pins the version string the fixture writes.
The module-scoped `scopes` fixture builds one base dataset with the shared read-scope builder, copies
that dataset's bytes into a second candidate path, opens the copy through `open_knowledge_store`, and
writes into it exactly the two rows a traversal can find: a policy version with `direction="forward"`,
`depth_bound=1` and `widened_scope=REGISTERED_REVIEW_SCOPE`, and one composition edge joining the base
fixture's family revision to its direct family revision under that version. **The policy row and the
edge live in the candidate dataset only**, which is what makes the provenance case's
`("composition", "candidate")` assertion a fact about where the row was read rather than a restatement
of the fixture's own shape. `_ScopeFixture` then holds the base fixture, the candidate path, the policy
version id and the authored edge id; `request(**overrides)` is the one declaration each case varies,
declaring `scope-B-M` over both sides with the two changed paths the shared read-scope support names;
`sources()` opens one store per declared side and returns the sources a construction is handed; and
`_construct` closes every store it opened in a `finally`, so a refusal case leaves no handle open
either.

**Six acceptance cases, one per clause group.** The construction case asserts the manifest records its
construction version, the resolved three-part policy identity, the declared scope id, the composition
edge it followed and non-empty membership in three recorded kinds. The provenance case asserts every
recorded-link edge kind on **both** sides and the composition edge on the candidate, then constrains
every mapping side to the declared pair — §1.6's historical-lookup fact, made checkable rather than
argued. Determinism is asserted as an equality between two whole manifests, field for field, plus the
tuple identity of the edge list, rather than by inspecting one field. The no-policy case is the
acceptance of an absence: a declaration naming no policy constructs, reports `policy_identity is None`
and follows no composition edge, while the family membership the recorded links reached survives — §1.2's
"absence never widens" and §1.1's membership in one case. The prefix case declares a directory where an
anchor path is stored: the declaration is accepted and selects nothing, so both membership tuples it
reads and the edge list are empty. And the frontier case is a derivation over the construction module's
own text — it reads `mcp/src/agents_remember/memory/knowledge/registered_scope.py` and requires the
shipped selection surface's four names, and the retrieval read's import, to be absent from it.

**Eight refusal cases, and none of them falls back to anything.** A declared snapshot the run cannot
produce is refused with `missing_input_kind == "declared_snapshot"`, the declared digest as the missing
input and the construction's own operation on the typed refusal. A dataset that is not the declared
snapshot is refused with the *declared* digest named, so the declaration is compared against the bytes
handed over rather than accepted as a claim. A seed no snapshot records is refused by name under
`seed_family_revision` instead of being dropped into a silently smaller scope. A policy version nobody
declared is refused under `traversal_policy` with the shared traversal's own `invalid_payload` code and
its own "not a declared policy version" sentence, so this module re-words no neighbour's fact. Three
refusals happen earlier, in the declaration vocabulary itself: two snapshots for one side are an
ambiguous common base, half a policy identity is not a declared policy, and a seed without a policy
"follows no composition edge" — each refused where the caller can still fix the declaration. The edge
model refuses the two mislabels in one place: a recorded lookup carrying a policy identity is "a
recorded lookup rather than a traversal", and a composition edge without one is "widening without a
recorded policy". Finally the path helper accepts a plain repository-relative spelling unchanged and
refuses blank, absolute, pathspec-magic and parent-escaping spellings, which is what keeps the lookup an
identity comparison.

**The boundary the module does not cross** is stated in its own docstring and enforced by what it does
not import. It protects the construction — what a scope records about its own inputs, and which missing
input a refusal names — and it makes no claim about a detection run, no claim about the selective read
(the frontier case asserts the read's *absence* from the construction module rather than exercising any
part of it), and no acceptance claim about the requirement. Its refusals are read as data: each case
asserts the kind, the exact identity and, where the refusal is typed, the code and operation the shipped
refusal vocabulary already had.

### Conventions

- **Refusals are asserted with their facts.** The construction refusals read `missing_input_kind` and the
  exact identity — a dataset digest, a seed uuid, a policy version — and the missing-snapshot case asserts
  `manifest is None` beside `state == "refused"`, so no case can pass on a construction that returned a
  partial scope with a complaint attached.
- **Case docstrings name the failure, not the assertion.** Thirteen of the fourteen cases carry a
  "Catches …" paragraph naming the defect they exist to prevent, which is how a reader separates two
  adjacent refusal cases; the frontier case instead states in its docstring that it is a derivation over
  the module's own text rather than an assurance.
- **Determinism is asserted over whole records.** Two constructions are compared as manifests rather
  than by sampling a field, and the edge list is asserted to equal a tuple of itself.
- **Hermetic and production-seamed.** One temporary directory, in-process stores opened through
  `open_knowledge_store`, and the production writers
  (`composition_policies.insert_policy_version`, `compositions.insert_composition`) rather than raw SQL;
  the two family revisions the edge joins come from the shared read-scope fixture.
- **The lane is declared in the file.** `pytestmark = pytest.mark.evidence_unit` is set once at module
  scope, and the module docstring names the `unit-regression` lane its cases occupy.
- **Exactly one case reads a file** — the frontier derivation; every other case drives the public
  constructors (`construct_registered_scope`, `snapshot_source`, `scope_path_is_recorded`) and the
  pydantic models.

### Invariants And Boundaries

- **Construction is total or it is a refusal.** The outcome is `constructed` or `refused`, and the case
  that refuses a declared snapshot asserts `manifest is None` — a scope that quietly holds less than its
  declaration says is not an answer any case here accepts.
- **Every followed edge names the side it was read from.** The provenance case asserts both sides for
  each recorded-link kind and the candidate side for the authored composition edge, and no mapping side
  outside the declared pair appears in the manifest.
- **Absence never widens.** A declaration with no policy is a successful construction with no policy
  identity and no composition edge, asserted in the same case as the family membership that survives.
- **A path prefix is not a membership.** The declared directory selects no realization claim, no source
  anchor and no followed edge; membership arrives only through recorded rows.
- **The read frontier is excluded by derivation, not by promise.** The construction module's own text is
  read, and four selection-surface names plus the retrieval read's import are required to be absent from
  it — an assertion about that module, deliberately not an assurance about the read.
- **No authority is minted for the scope.** Every acceptance assertion addresses the scope by its
  declared id, and no assertion reads a content address, digest or fingerprint *of the scope itself*.
- **Nothing is certified.** The module writes no record outside its temporary stores and makes no
  requirement-acceptance claim; it protects behavior only.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring states the clause group, the lane, and the six failures every case names — including the ambiguous common base resolved by picking one. | "an ambiguous common base resolved by picking one" | mcp/tests/test_knowledge_registered_scope.py:1-12 |
| The two module constants pin the shipped registered-composition policy id and the declared version the fixture's policy row carries. | "DECLARED_VERSION = "2026-09-18.1"" | mcp/tests/test_knowledge_registered_scope.py:52-53 |
| The module-scoped fixture builds the base dataset through the shared read-scope builder and copies it to a second candidate path. | "base = build_read_scope_fixture(directory / "base")" | mcp/tests/test_knowledge_registered_scope.py:56-71 |
| The one declaration each case varies declares `scope-B-M` over both sides with the read-scope fixture's two changed paths. | ""scope_id": "scope-B-M"," | mcp/tests/test_knowledge_registered_scope.py:89-102 |
| Each snapshot declaration records the dataset's own identity and the selector policy version it was read under. | "selector_policy_version="recorded-family-frontier/v1"," | mcp/tests/test_knowledge_registered_scope.py:118-123 |
| The fixture's policy version is a forward, depth-one traversal that widens to the registered review scope. | "widened_scope=REGISTERED_REVIEW_SCOPE," | mcp/tests/test_knowledge_registered_scope.py:126-143 |
| The authored composition edge joins the fixture's family revision to its direct family revision under that policy version. | "from_family_revision_id=base.family.revision_id," | mcp/tests/test_knowledge_registered_scope.py:146-162 |
| **The acceptance case: construction version, resolved three-part policy identity, declared scope id, followed composition edge and non-empty membership in three kinds.** | `test_a_declared_scope_is_constructed_with_its_policy_identity_and_resolved_membership` | mcp/tests/test_knowledge_registered_scope.py:180-200 |
| **The provenance case asserts both mapping sides for each recorded-link kind and the candidate side for the authored edge.** | "assert ("source_to_invariant", "candidate") in recorded" | mcp/tests/test_knowledge_registered_scope.py:203-218 |
| Determinism is asserted as two whole manifests comparing equal, with the edge list a tuple of itself. | "assert first == second" | mcp/tests/test_knowledge_registered_scope.py:221-235 |
| **The no-policy case is a successful construction with no policy identity and no composition edge, and the reached family membership survives.** | "assert outcome.manifest.policy_identity is None" | mcp/tests/test_knowledge_registered_scope.py:238-250 |
| **The prefix case: a declared directory where an anchor path is stored selects no claim, no anchor and no edge.** | "assert outcome.manifest.followed_edges == ()" | mcp/tests/test_knowledge_registered_scope.py:253-266 |
| The frontier case reads the construction module's own text and requires the selection surface's names to be absent from it. | ""select_recorded_scope"," | mcp/tests/test_knowledge_registered_scope.py:269-286 |
| **The declared-snapshot refusal names the exact declared digest and carries the construction's own operation on the typed refusal.** | "assert outcome.refusal.refusal.operation == CONSTRUCT_SCOPE_OPERATION" | mcp/tests/test_knowledge_registered_scope.py:293-311 |
| Two declarations for one side are refused as an ambiguous common base at declaration time rather than resolved by a tie-break. | "with pytest.raises(ValidationError, match="ambiguous common base"):" | mcp/tests/test_knowledge_registered_scope.py:370-379 |
| The path helper refuses absolute, pathspec-magic and parent-escaping spellings, so the declared path stays an identity to compare. | "for bad in ("/src/integration.py", ":(exclude)src/x.py", "../src/x.py"):" | mcp/tests/test_knowledge_registered_scope.py:425-437 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every dataset it builds is an in-process knowledge
store under a temporary directory, and the two family revisions the fixture's edge joins are the shared
read-scope fixture's own — same-repository test data, not another repository's state.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T14:25+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the registered-scope suite. It records the two-snapshot fixture whose policy row and authored edge live in the candidate dataset only, the six acceptance cases (construction identity and membership, per-side edge provenance, field-for-field determinism, the no-policy absence, the prefix that selects nothing, and the frontier exclusion asserted as a derivation over the construction module's text), the eight refusals that each name an exact missing input and fall back to nothing, and the boundary the module does not cross: it protects the construction and asserts nothing about a run over the scope or about the retrieval read. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
