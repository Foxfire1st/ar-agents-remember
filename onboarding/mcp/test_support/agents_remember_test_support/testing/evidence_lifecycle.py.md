# mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Owns the typed metadata of durable test evidence (fixtures, recordings, recording generators,
migration proofs and shared support) and the complete validation of the catalog that declares it,
`mcp/tests/evidence-lifecycle.toml`. It is also the command-line entry that validates both test
catalogs, and with `--write` rewrites both to canonical form.

The module is the consumer-completeness oracle: `load_evidence_inventory` derives the repository's
dependency facts from source and requires every declared `consumers` list to equal the consumers
the source tree shows. It reports a difference whenever a module starts or stops consuming a
governed artifact, without any change to the catalog.

## Code Commentary

### Types

`EvidenceKind`, `EvidenceAuthority`, `EvidenceCategory`, `EvidenceFidelity`, `EvidenceCadence`,
`EvidenceLifetime` and `ConsumerScope` are closed vocabularies; an unknown value makes a row
invalid. `ConsumerScope` has three values: `exact` (the listed test modules), `exact-source` (the
listed source files; for support whose consumers are not test modules, such as the harness under
`scripts/e2e_harness`) and `all-tests` (no list; the loader fills in every current test module).
`EvidenceContract` is one `[[contract]]` row: an identity, an owner path and an evidence node.
`EvidenceMetadata` is one `[[artifact]]` row. `EvidenceInventory` is the validated result;
`payload()` renders it for the JSON output.

### `load_evidence_inventory`

The loader collects every finding and raises one `EvidenceLifecycleError` that lists them all
(`test evidence lifecycle has N finding(s)`). It returns an inventory only when there is none.

1. It reads the catalog. A file that cannot be read or parsed is refused at once with the text of
   `unreadable_catalog` from `catalog_canonical.py` (`cannot read evidence catalog <path>`). When
   the cause is a TOML parse error, the refusal ends with the sentence that two rows may have been
   interleaved by a merge and that the file is restored from the landed commit.
2. Canonical form comes first: `_canonical_form_findings` reports each `consumers` list that is not
   written with one path per line and a table header that the write command does not read
   (`layout_findings`), each contract row that sorts before the row above it by `id`, each artifact
   row that sorts before the row above it by `path`, and each `consumers` list that is out of order
   or holds a duplicate. The order, duplicate and layout findings name the row and the `--write`
   command.
3. The schema version must be `ar-test-evidence-lifecycle/v3` and `large_fixture_bytes` a positive
   integer.
4. Contract rows may hold only `id`, `owner` and `evidence_node`, each a non-empty string.
5. Artifact rows may hold only the known fields. An `exact` or `exact-source` row needs a non-empty
   list of consumer strings; an `all-tests` row must not list consumers.
6. `_validate_contracts`: no identity twice, the owner is an existing file, the evidence node names
   an existing file and an exact `::` selector that exists exactly once as a top-level function or
   as a method of a class, and every contract is referenced by at least one artifact's
   `replacement_contract`.
7. Per artifact: the path is repository-relative and confined and is listed once. An artifact whose
   file does not exist is a finding that says the command removes no row and that the row is
   deleted when the artifact is retired. A declared consumer whose file does not exist is a finding
   that names the `--write` command when the command repairs the row; for a row whose every listed
   consumer is gone and whose source-derived set is empty, the finding says that the command does
   not repair the row, which is retired by hand if the artifact is retired. The declared consumers
   must equal the observed ones
   (`consumer proof differs from source-derived ownership; missing=..., unsupported=...`). The two
   sides are compared as sets, so a duplicate line is not found here; the canonical-form finding of
   step 2 reports it. Because an `all-tests` row declares every test module, changing a row to
   `all-tests` is refused here unless every test module consumes the artifact.
8. Lifetime and authority: temporary evidence needs `expires_after`, must not be expired, must not
   claim permanence and needs a `node:` replacement; other evidence must not declare
   `expires_after` and needs a `permanence_rationale`; migration evidence must be temporary;
   versioned evidence must have an external authority.
9. `replacement_contract` starts with `contract:` (a registered identity) or `node:` (an existing
   file and selector).
10. Coverage in both directions: `_validate_catalog_coverage` compares the cataloged paths with
    `governed_artifact_paths` from `evidence_governance.py`. A governed file without a row and a row
    that points outside the governed files are both findings.

Incomplete dependency facts (a source file that cannot be parsed, ambiguous module names) are
findings too, so a catalog is never accepted against a graph that could not be derived.

The keyword `build_facts` replaces `RepositoryDependencyFacts.build`. A caller that runs both
catalog loaders passes one memoising builder to both, so the source graph is derived once. Without
the keyword the loader builds the facts itself. The loader asks for the facts only after it has
parsed its catalog.

### The command

`main` parses `--project-root`, `--json-output` and `--write`.

- Without `--write` it is the validator. It loads the lifecycle catalog and then the lane manifest
  (`load_lane_manifest`), so a missing, stale or non-canonical lane line fails the same command.
  Both loaders get the same cached builder, so one run derives the source graph once. It prints the
  error and returns 1, or prints `evidence-lifecycle: PASS (N governed artifacts)` and returns 0.
  `lane_manifest` is imported inside the function because that module imports this one.
- With `--write` it calls `write_canonical_catalogs` from `catalog_canonical.py`. A refusal prints
  `evidence-lifecycle: nothing written: <reason>` and returns 1. Otherwise it prints one line per
  change, or that both catalogs were already canonical, and returns 0.

The validator command is run by the Git hook gate (`.githooks/_gate.sh`), by the quality plan's
`evidence-lifecycle` step and by the certification profile (`mcp/certification-profile-v1.json`).
`load_evidence_inventory` is also called by the dependency-ownership graph and the cadence runner.

## Evidence

- The module names itself the consumer-completeness oracle and states that the catalog must be in canonical form. [1]
- Contract owners and exact evidence selectors must name real source nodes, and every contract must be referenced. [3]
- Discovery of the governed files is delegated to one owner and compared in both directions. [4]
- The layout findings, then one finding per contract row, artifact row and consumers list that is out of canonical form. [5]
- An exact or exact-source row needs a non-empty consumer list; an all-tests row must not list consumers and declares every test module. [8]
- Lifetime rules for temporary and retained evidence. [9]
- Migration evidence must be temporary and versioned evidence must have external authority. [10]
- A replacement is a registered contract or an existing node selector. [11]
- The validator loads the lifecycle catalog and then the lane manifest on one cached source graph; `--write` goes to the rewrite. [12]
- A refused rewrite prints that nothing was written and returns 1. [13]
- The Git hook gate runs the validator command. [14]
- The quality plan's evidence-lifecycle step runs the validator command. [15]

- The loader collects every finding and raises one error that lists them; `build_facts` lets a caller supply the source graph. [16]
- A catalog that cannot be read or parsed is refused with the shared refusal text. [17]
- An artifact or consumer whose file is gone is a finding (the consumer finding names the command only where the command repairs the row), and declared and observed consumers are compared as sets. [18]
