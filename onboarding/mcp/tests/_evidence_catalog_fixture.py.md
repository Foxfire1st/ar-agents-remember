# mcp/tests/_evidence_catalog_fixture.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

One builder that writes a valid evidence-lifecycle catalog, in canonical form, for a synthetic
repository that a test created. Tests that drive the catalog loader, the selection graph or the
retry proof over a scratch repository call it instead of copying the catalog schema by hand.

## Code Commentary

`write_synthetic_evidence_catalog(root, artifacts)` takes a mapping from each governed artifact path
to the test modules that consume it and returns the path of the catalog it wrote,
`<root>/mcp/tests/evidence-lifecycle.toml`.

- It refuses an empty mapping and an artifact without a consumer with a `ValueError`.
- It first makes every consumer observable from source: `_write_observable_consumers` appends to
  each consumer module a tuple `_AR_EVIDENCE_INPUTS` that names the artifact paths as string
  literals, plus a small function that reads them. The consumer oracle counts a test module that
  holds an artifact's path as a string literal as a consumer of that artifact, so the declared lists
  and the source tree agree.
- It writes the schema version it imports from `evidence_lifecycle.py` (`CATALOG_SCHEMA`) and
  `large_fixture_bytes = 25000`.
- It writes one `[[contract]]` row, `synthetic-test-evidence`. Its owner is the first artifact path
  in sorted order. Its evidence node is the first `test_` function, or `test_` method of a class,
  found in that artifact's consumers (`_first_test_node`); when none exists the builder raises a
  `ValueError`.
- It writes one `[[artifact]]` row per artifact, in sorted path order. The kind is `shared-support`
  for a `.py` path and `fixture` otherwise. Every other field is a fixed value: internal-canonical
  authority, the `unit-regression` category, a permanent lifetime with a rationale, the synthetic
  contract as replacement contract, and `consumer_scope = "exact"`.
- Each `consumers` list is written with one path per line, sorted and without duplicates.

The output is in the canonical form that `load_evidence_inventory` requires: one contract row,
artifact rows ordered by `path`, and every `consumers` list ascending, without duplicates and with
one path per line. A test that needs a catalog that is not canonical edits the written file
afterwards.

The module is test support. It does not write the lane manifest, and it is not the repository's
catalog authority; the loader in `evidence_lifecycle.py` decides what a valid catalog is.

## Evidence

- The builder refuses an empty mapping, writes the schema line, the one contract row and one artifact row per artifact in sorted order, and returns the catalog path. [1]
- Each consumers list is written one path per line, sorted and without duplicates. [3]
- Each consumer module gets the literal tuple of the artifacts it reads, so the oracle observes it. [4]
- The contract's evidence node is the first test function or test method found in the consumers. [5]

- The loader that decides what a valid, canonical catalog is. [6]
