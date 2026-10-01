# mcp/tests/test_evidence_catalog_gate_boundaries.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The lane that separates **the two evidence-catalog gates**, which one test used to run inside one
case. `D-19` recorded why the distinction is load-bearing: a leaf can pass the byte pin, pytest,
ruff, format and pyright while the consumer oracle is red, and the four green checks then ship a red
gate.

- **The catalog byte pin** — `LIFECYCLE_CATALOG_SHA256`, `LIFECYCLE_CONTRACT_COUNT` and
  `LIFECYCLE_ARTIFACT_COUNT` in `mcp/tests/test_dependency_ownership_ast_helpers.py`, asserted
  against `mcp/tests/evidence-lifecycle.toml`'s own bytes and populations. It answers *"is this the
  exact catalog file that was measured?"*. **Nothing in the source tree can redden it** — only an
  edit to the catalog's bytes changes it — and its documented repair is a re-pin after the edit was
  reviewed.
- **The consumer-completeness oracle** — `load_evidence_inventory` and its finding
  `<artifact>: consumer proof differs from source-derived ownership`
  (`mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py`). It answers *"does
  the catalog agree with the source tree it describes?"* by deriving the repository's dependency
  graph and requiring every `consumer_scope = "exact"` artifact's declared `consumers` list to equal
  the test modules that actually reach it. It reddens whenever a module starts or stops consuming a
  governed artifact, and its documented repair is a **registry row** — which is *why* the pin moves
  afterwards.

The naming is stated where each reader arrives: this module's own docstring, and the oracle's module
docstring (`evidence_lifecycle.py:1-19`) which was rewritten in the same pass.

## Code Commentary

### Logic

**One case evaluates both gates in one run over one catalog edit**, so the distinction is a
measurement rather than a claim: the oracle is red and the pin is green at the same instant.

`synthetic_repo` (`:49-65`) builds a valid catalog over two real consumers using the shared fixture
`write_synthetic_evidence_catalog` from `_evidence_catalog_fixture`, writes the two consumer modules
and the governed artifact as real files, adds the `[tool.pytest.ini_options]` block the oracle reads,
and runs `git init` + `git add -A`. **The `git init` is not decoration**: the oracle derives its
graph from the repository's tracked files, so a synthetic repository has to be one. The case asserts
`load_evidence_inventory(root)` is non-empty first, so the refusal below is produced by the edit and
not by the fixture.

The edit is the exact shape a landing produces when it adds a test module that imports a governed
support module and does not add the registry row: `SECOND_CONSUMER`'s name is replaced by
`FIRST_CONSUMER`'s in the artifact's `consumers` list while `SECOND_CONSUMER` still consumes it, so
the catalog's bytes are still the ones the pin measured and the tree is no longer the one the catalog
describes. An `assert doctored != catalog.read_text(...)` guard (`:107`) fires before the write if
the replacement did nothing.

`populations` (`:68-76`) returns the pinned catalog's **byte digest, contract count and artifact
count**. The case reads those before the doctoring and asserts them equal afterwards (`:116-118`),
and the assertion carries its own message: *"the oracle's refusal is about the source tree, and it
may not move the pinned bytes"*. That comparison is deliberately **between the file and itself** —
the pin's own constants are asserted in the pin's own test, and duplicating them here would create a
second place that has to be re-pinned. This is also why the module does **not** import the pin
module: it imports `_evidence_catalog_fixture` and the oracle only.

### Conventions

`REPOSITORY_ROOT = Path(__file__).parents[2]` (`:41`) resolves the checkout from the test file, so
the pinned catalog is found without a fixture or an environment variable. `PINNED_CATALOG`,
`ARTIFACT`, `FIRST_CONSUMER` and `SECOND_CONSUMER` are module constants (`:42-46`) rather than
literals repeated in the case. The module carries **no `pytestmark`**; its lane row was **appended**
to the end of the `unit-regression` list in `mcp/tests/test-evidence-lanes.toml:195` — the
single-writer registry apply put all five of this leaf's new case modules there rather than
inserting `architecture-fitness` mid-list, because a mid-list insertion shifts every row below it and
stales every citation into the file (item 16's half (a)). Being in `unit-regression` is what keeps
the module out of the `pytest.mark.integration` population, which sits at exactly **400 / 400**.

### Invariants And Boundaries

- **The oracle's refusal may not move the catalog's bytes.** The single assertion that carries the
  module's meaning is the before/after population comparison, and it is written so a future
  re-pin cannot make this case the second home of the pin.
- **An exact-scope consumer is a precondition, not metadata.** This module consumes
  `mcp/tests/_evidence_catalog_fixture.py` and (transitively, through the oracle) the lane manifest,
  and both registrations are declared — an unregistered exact-scope consumer is a hard collection
  error, which is the failure mode this module exists to make visible.
- **The synthetic repository is a real Git repository.** No case stubs the graph the oracle derives.
- **Boundary.** This is a test module. It owns no production contract and adds no support module.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's own statement of the two gates and how to tell them apart. [1]
- **The consumer-completeness oracle: the one gate the source tree can redden, and the finding it raises.** [2]
- The byte pin's own three constants, asserted in the pin's own test and deliberately not duplicated here. [3]
- The pinned catalog whose bytes the case compares with themselves. [4]
- The shared fixture that writes a valid synthetic catalog. [5]
- The synthetic repository: two real consumers, one governed artifact, and a real Git repository because the oracle derives its graph from tracked files. [6]
- The catalog's own digest and declared populations, read rather than pinned. [7]
- **The case: the oracle refuses the doctored tree while the pinned catalog's bytes and populations are identical.** [8]
- The lane row this module was appended to, in the lane list — appended rather than inserted mid-list. [9]
- The two exact-scope consumer registrations this module obliged. [10]

### Cross-Repo References

No cross-repository behavior is implemented or measured in this file. The synthetic repository is
created under `tmp_path` and never touches the checkout's own Git store.

No meaningful cross-repo references found.
