# mcp/tests/evidence_test_support.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The supporting-record cases' shared fixture: one admitted candidate namespace with resolvable links, its
commands and payload helpers, and a real artifact directory under a temporary root.

## Code Commentary

### Logic

Every case in this leaf's two test modules needs the same starting point, and it is a specific one rather
than a convenient one. An evidence claim resolves four links — a subject, an evidence anchor and every
claimed-coverage endpoint — and an observation records a candidate that some other operation already
established. A per-module copy of that topology would let the two modules disagree about which identity is
the facet revision and which is the invariant revision, which is exactly the property the refusal cases
assert; so it is built once, here, through the production application seam rather than by inserting rows.

`build_evidence_fixture` returns an `EvidenceFixture`: the admitted candidate namespace, the identities the
cases cite, the artifact root, and the context the read cases use. `_store_invariants`,
`_store_realizations` and `_store_facet` build the namespace's records through the production operations,
so a fixture never fabricates a row the write path would refuse.

The helpers are deliberately thin and total: `claim_command` and `observation_command` build commands from
`ClaimOptions` and `ObservationOptions`; `claim_payload` and `observation_payload` build the payloads;
`artifact_reference`, `expect_artifact` and `expect_publication` build the reference values; `read_context`
builds the read context; `default_environment` is the run environment; `schema_names`, `record_kinds`,
`recorded_at`, `digest_of` and `expect_refusal` are the small shared conveniences.

**This file is a registered durable artifact, not an unregistered helper.** It is
`contract:knowledge-evidence-cases` with an owning contract row and an artifact row in
`mcp/tests/evidence-lifecycle.toml` — kind `shared-support`, authority `internal-canonical`, category
`unit-regression`, fidelity `in-process`, cadence `affected`, `introduced_by = "260915-KS-L12"`, lifetime
`permanent`, `consumer_scope = "exact"` with exactly its two consuming modules named. Its executable
evidence node is
`mcp/tests/test_knowledge_evidence_claims.py::test_a_claim_reads_back_with_every_field_including_an_empty_limitations`,
and the artifact is why the evidence catalogue's own pinned count and digest moved when this leaf landed.

### Conventions

A shared support module builds state through the production seam, exposes small builders rather than
pre-built rows, and names its consumers in the catalog so its blast radius is measured rather than assumed.
A fixture that acquires a new consumer must be re-pinned in the catalog.

### Invariants And Boundaries

- **The fixture holds real bytes.** The artifact directory contains a real file under a temporary root,
  because a digest checked against bytes at write time is only meaningful against real bytes.
- **Provenance comes from the admission**, never from an authored payload, which is why the namespace is
  built through the application seam.
- **Both identities exist and are distinguishable.** The namespace holds an invariant revision and a facet
  revision, so the subject-kind discrimination is asserted against a topology where either could resolve.
- **The fixture is not a test module.** It defines no `test_` function, so it contributes no case to any
  population and cannot be counted as coverage.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The fixture's own type and the one entry point that builds it. [1]
- The namespace's records, built through the production operations rather than by inserting rows. [2]
- The command and payload builders the two modules share. [3]
- The artifact, publication and read-context helpers. [4]
- The registered owning contract and artifact row that make this file governed evidence: the contract id, its owner and its evidence node, and the artifact's kind and exact consumer scope. [5]
- The unit-regression lane rows for this artifact's two consumers. [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
