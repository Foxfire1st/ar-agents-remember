# mcp/tests/evidence_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture's own type and the one entry point that builds it. | `EvidenceFixture`; `build_evidence_fixture` | mcp/tests/evidence_test_support.py:102-139; mcp/tests/evidence_test_support.py:142-190 |
| The namespace's records, built through the production operations rather than by inserting rows. | `_store_invariants`; `_store_realizations`; `_store_facet` | mcp/tests/evidence_test_support.py:198-230; mcp/tests/evidence_test_support.py:233-287; mcp/tests/evidence_test_support.py:290-312 |
| The command and payload builders the two modules share. | `claim_command`; `observation_command`; `claim_payload`; `observation_payload` | mcp/tests/evidence_test_support.py:339-360; mcp/tests/evidence_test_support.py:382-413; mcp/tests/evidence_test_support.py:496-502; mcp/tests/evidence_test_support.py:505-514 |
| The artifact, publication and read-context helpers. | `artifact_reference`; `expect_artifact`; `expect_publication`; `read_context` | mcp/tests/evidence_test_support.py:477-484; mcp/tests/evidence_test_support.py:441-446; mcp/tests/evidence_test_support.py:449-454; mcp/tests/evidence_test_support.py:457-473 |
| The registered owning contract and artifact row that make this file governed evidence: the contract id, its owner and its evidence node, and the artifact's kind and exact consumer scope. | "[[contract]]"; "[[artifact]]"; "shared-support" | mcp/tests/evidence-lifecycle.toml:1304-1326 |
| The unit-regression lane rows for this artifact's two consumers. | "mcp/tests/test_knowledge_evidence_claims.py" | mcp/tests/test-evidence-lanes.toml:73-74 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 2 claim(s) here (1 x citation_claim_reopened, 1 x citation_provenance_invalid). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T04:20:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the shared support module the two evidence case modules build on. It records why the fixture is shared rather than copied, that it is a registered `shared-support` artifact owning the `knowledge-evidence-cases` contract, and that it holds real artifact bytes because a write-time digest check is only meaningful against real bytes. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
