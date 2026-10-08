# mcp/tests/test_dependency_ownership_ast_helpers.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Holds the repository's real-boundary census over the evidence-lifecycle catalog and the guard of the
retained headless production-chain proof, `mcp/tests/test_lifecycle_owned_completion_relay.py`. The
guard says three things about that proof: it is ordinary `test_` source, it owns no governed
evidence artifact and no contract, and the catalog stays closed over the governed files.

Every property is computed from the catalog and the source tree when the test runs. The module
writes down no byte digest, no row count and no file count of a catalog, so a change that adds a
test file does not edit this module.

## Current master-retirement registration

The catalog is computed from the source tree by the canonical writer command, so this module states no digest, no line count and no contract or artifact count of it; the registration adds the consumer rows of `test_abandoned_series_closeout.py`, `test_master_retirement.py` and `test_standalone_master_retirement.py`. Dated L40/R47 rationale and earlier history remain; the source-derived consumer proof checks the actual union rather than replacing historical digests.

## Code Commentary

### The census

`test_repository_inputs_reach_their_supported_consumers` (integration marker) builds the real
`DependencyOwnershipGraph` for the repository; building it loads the whole artifact catalog through
`load_evidence_inventory`. It then resolves three kinds of input:

- `.codex/config.toml` resolves completely with no test and the single decision
  `verified-repository-input-no-consumers`;
- an unknown path under `unknown/settings/` does not resolve completely;
- the ambient role runner and the layers contract each resolve completely, without global
  invalidation, to a named consumer test (`test_agents_remember_quality.py` and `test_layering.py`)
  for the reason kind `declared-consumer`.

The catalog's contract `synthetic-test-evidence-candidate` names this test as its evidence node, so
renaming the test needs the same change in the catalog.

### The production-proof guard

`test_production_proof_adds_no_governed_evidence_artifact` (integration marker) reads
`mcp/tests/evidence-lifecycle.toml` through the shared `read_catalog` and runs five checks:

1. `_assert_the_proof_is_ordinary_test_source`: the proof module exists, its name starts with
   `test_`, and `governed_artifact_paths` does not list it.
2. `_assert_the_proof_is_selected_by_the_lane_manifest`: exactly one lane of
   `mcp/tests/test-evidence-lanes.toml` lists the proof module.
3. `_assert_the_governed_inventory_is_closed`: the governed files, discovered with the catalog's own
   `large_fixture_bytes`, equal the cataloged paths in both directions, and
   `load_evidence_inventory` accepts the real catalog. A file that escaped into the governed tree
   without a row and a row whose file is gone both fail here.
4. `_assert_the_catalog_keeps_its_identities`: the schema version is
   `ar-test-evidence-lifecycle/v3`; the identity
   `lifecycle-owned-completion-relay-production-chain` is not a declared contract; and the declared
   contract ids equal the ids that artifacts reference through `contract:` replacement contracts.
5. `proof_ownership(catalog, proof)` returns an empty list.

`proof_ownership` names every row or contract that the proof module would own. It reports an
artifact row whose `path` is the proof, whose `owner` is the proof, or whose `consumers` list is the
proof alone, and a contract whose `owner` is the proof or whose `evidence_node` lies in the proof
module. A proof that is one of several consumers of an artifact owns nothing; the real catalog has
such rows.

`test_proof_ownership_is_computed_from_the_catalog` drives `proof_ownership` over a small synthetic
catalog, one parameter set per case: the clean catalog, each of the five ways of owning (path,
owner, sole consumer, contract owner, contract evidence node), and the proof among several
consumers. `test_a_catalog_that_does_not_parse_fails_these_checks_with_the_recovery_sentence`
shows that a catalog that does not parse fails these checks with the shared reader's sentence and
not with a bare parser error.

### Boundaries

- The module does not check the catalogs' canonical form or their merging; those cases are in
  `test_evidence_catalog_canonical_form.py`.
- The module does not judge the descriptive fields of a catalog row (`kind`, `authority`,
  `category`, `fidelity`, `cadence`, `lifetime`, `introduced_by`). The loader checks that each value
  belongs to its vocabulary (`introduced_by` only has to be a non-empty string); which value a row
  carries is read in the diff of the catalog.

## Evidence

- The module states that every property is computed and that no byte, row count or file count is written down. [1]
- The module's constants: the repository root, the proof module, the two catalog paths, the schema and the rejected standalone identity. [2]
- The census builds the real graph and resolves the three kinds of input. [3]
- The guard runs the four structural checks and requires that the proof owns nothing. [4]
- What owning means: path, owner, sole consumer, contract owner, contract evidence node. [5]
- The synthetic cases for each way of owning, the clean catalog and the proof among several consumers. [6]
- The proof must stay `test_` source outside the governed inventory. [7]
- Exactly one lane lists the proof module. [8]
- The governed files equal the cataloged paths and the real catalog validates. [9]
- The schema, the rejected identity and declared equals referenced. [10]
- The discovery rule for governed files that the guard uses. [12]


- A catalog that does not parse fails these checks with the recovery sentence of the shared reader. [14]
