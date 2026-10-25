# mcp/tests/read_scope_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Constructs a text memory tree and a real Git tree with the topology needed by bounded scope-read tests: the `P -> I1`, `F1 -> {I1, J1}`, `G1 -> {J1, K1}` graph, where the sibling invariant one family shares with a second family the seed never reaches is the whole stopping rule.

## Code Commentary


The fixture retains exact invariant/family/revision identities, source locators, applicability, conditions, exclusions and memberships. Its topology deliberately distinguishes directly containing families, sibling realizations, an advertised unreached family, absent/unparsed/mismatched sources and explicit stopping boundaries. Callers use the returned identities rather than inferring relationships from names.

RowStore and the revision, family, membership and realization constructors are imported from knowledge_rows_test_support and build a text tree through the rows builder, never by inserting database rows — every identity is one the projection produced. Their production-shaped names do not make them shipped authoring operations. A text record holds exactly one revision (rule 3): the predecessor/successor revisions the old fixture authored beside one identity are gone. The Git source and current read owners are real; tree construction is a test fixture.

### Logic

The topology, and why each part exists:

- **`I1`** is the retry-budget record's single revision, with the friendly display label `v2`, and carries
  **two realization claims at two distinct source locations** (`src/integration.py` and
  `src/synchronization.py`) — the requirement's own conformance example. The label does not establish
  a retained predecessor or a second stored revision.

> Retained earlier card wording; superseded by the current account above:
> - **`I1`** is the second revision of the retry-budget invariant and carries **two realization claims at two
>   distinct source locations** (`src/integration.py` and `src/synchronization.py`) — the requirement's own
>   conformance example.

- **`J1`** is the first revision of the candidate-batch invariant. It carries **two claims at one
  location** (`src/batch.py`), which is what makes "two claim identities, one distinct source location"
  measurable, and it is the sibling the frontier advertises.
- **`K1`** is the first revision of the source-resolution invariant, reachable **only** through `G1`.
- **`F1` is `{I1, J1}` and `G1` is `{J1, K1}`**, so `J1` is in both and `K1` is in the one the seed does
  not reach. That is the whole stopping rule in one graph.
- **`H1` is `{I1, L1}`**, a **second** family that directly contains `I1`, which is what proves the
  path/invariant rule includes *every* directly containing family rather than only the first.
- **The retry text record carries one revision.** The old same-identity predecessor/successor population is absent; this fixture does not prove selection or ordering among I0/I1/I2.
- **`absent_anchor`** is a recorded claim whose path exists in no tree, and **`mismatch_anchor`** is a
  claim whose recorded blob identity is deliberately not the one the fixture repository holds at that
  path. Both are authored like any other claim: storage never resolves a source, so whether a path
  resolves is a fact about a snapshot and not a condition for recording it.

**Seed identities are projected by the text-tree builder.** `_seed_identities` allocates fixture UUIDs and the row helpers return the tree's projected identities. `_build_invariants` authors each record's single revision. The removed `_ordered_revision_id`, `PREDECESSOR_LABEL` and shared-successor-label machinery is historical, not an operative ordering guarantee.

Public surface: `build_read_scope_fixture(...)` returns a `ReadScopeFixture` carrying the identity maps,
the paths, the labels, the recorded blob identities and the tree id; `make_read_authorship` builds the
authored provenance; `RevisionSeed` / `RealizationSeed` / `ReadFixtureFamily` / `ReadFixtureRealization`
are the small value types the builders pass around.

### Conventions

- The real Git tree is built with `subprocess` against `tmp_path`; nothing touches the checkout.
- Blob identities are read back from the tree rather than hand-written, except where a claim is
  *deliberately* recorded against a different or absent blob.

### Invariants And Boundaries

- **The fixture is one graph, shared by the unit and integration modules**, so both lanes assert the same
  selection rather than two graphs that could drift. That is the artifact's declared permanence rationale.

- **Boundary.** This is test support. It is not execution evidence, it declares no lane, and it asserts
  nothing.

### Todos

None recorded.

The sizes and catalog line addresses in the following original account are historical observations, not measurements of the present source tip.

None recorded. **`mcp/tests/read_scope_test_support.py` is 762 lines** — no ceiling applies to a support
module, but a successor adding scenarios should extend the builders rather than fork a second fixture.

## Evidence


### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- `build_read_scope_fixture` supplies the current fixture or assertion described above. [11]


- `_create_invariant` supplies the current fixture or assertion described above. [12]


- `_create_revision` supplies the current fixture or assertion described above. [13]


- `_create_realization` supplies the current fixture or assertion described above. [14]


- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]


- RowStore writes text-tree fixture rows without the retired production admission plane. [16]


### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.


- **The fixture's declared topology and why this graph and not the shared branching one.** [17]


- The graph constants: the invariant labels and statements, the applicability, conditions and exclusions, and the three direct family guarantees. [18]

- The recorded paths, including the two the read is measured against (absent and mismatched). [19]
- The current seed allocator supplies identities; removed predecessor/successor ordering helpers are not current fixture owners. [20]

- The public builder and the value types a case reads. [21]





> Retained earlier citation wording: - **The governed-artifact and contract rows that make this module part of the catalog.** Source caption: `read_scope_test_support` [22]




### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- **The governed-artifact and contract rows that make this module part of the catalog.** Source caption: `read_scope_test_support` [22]
