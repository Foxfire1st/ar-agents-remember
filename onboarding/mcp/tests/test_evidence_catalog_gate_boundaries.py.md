# mcp/tests/test_evidence_catalog_gate_boundaries.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Shows that the consumer-completeness oracle (`load_evidence_inventory`) refuses a catalog that no
longer describes the source tree, and that this refusal is about the source tree and not about the
catalog's form. The catalog's canonical form is a separate refusal with its own command; this module
holds the one case where the catalog stays canonical and only the oracle objects.

## Code Commentary

`synthetic_repo` builds a small repository under the test's temporary directory: two test modules
(`mcp/tests/test_alpha.py`, `mcp/tests/test_beta.py`), one governed artifact
(`mcp/tests/_catalog_anchor.py`), a catalog written by the shared builder
`write_synthetic_evidence_catalog` with both modules as consumers, and a `pyproject.toml` that names
`mcp/tests` as the test path. It then runs `git init` and `git add -A`, because the oracle derives
its facts from Git's file listing.

`test_the_oracle_refuses_a_tree_the_catalog_no_longer_describes` is the only case.

1. It loads the fresh catalog and asserts that it is valid, so the refusal in step 3 comes from the edit
   and not from the fixture.
2. It removes the line of the second consumer from the artifact's `consumers` list and asserts that
   the text changed. The module still consumes the artifact. This is the state a change leaves when
   it adds a test module that reads a governed support module and does not register it. The list
   that remains is still in canonical form.
3. It loads again and expects an `EvidenceLifecycleError` whose text holds
   `consumer proof differs from source-derived ownership`, names the removed module under
   `missing=`, reports exactly one finding, and does not mention `--write`.

The last two assertions carry the boundary: the oracle's finding is the only one, and no
canonical-form finding (which would name the `--write` command) is raised for a catalog that is
merely incomplete.

The module is a plain test module without a marker. It imports the builder from
`_evidence_catalog_fixture.py` and the loader from `evidence_lifecycle.py`, and it reads no file of
the real repository.

## Evidence

- The module states that the oracle reddens on the source tree and that canonical form is a separate refusal. [1]
- The shared builder that writes the valid, canonical synthetic catalog. [5]
- The synthetic repository: two consumers, one governed artifact, and a real Git repository. [6]
- The case: one consumer line removed, one finding, and no mention of the write command. [8]

- The oracle's finding when declared and observed consumers differ. [9]
### Cross-Repo References

No cross-repository behavior is implemented or measured in this file. The synthetic repository is
created under `tmp_path` and never touches the checkout's own Git store.

No meaningful cross-repo references found.
### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.
### Repo-Internal References

- The lane row this module was appended to, in the lane list — appended rather than inserted mid-list.
- The two exact-scope consumer registrations this module obliged.

- **The consumer-completeness oracle: the one gate the source tree can redden, and the finding it raises.** [22]
- The shared fixture that writes a valid synthetic catalog. [23]
- The synthetic repository: two real consumers, one governed artifact, and a real Git repository because the oracle derives its graph from tracked files. [24]
- The lane row this module was appended to, in the lane list — appended rather than inserted mid-list. [25]
- The two exact-scope consumer registrations this module obliged. [26]




- The lane row this module holds in the sorted `unit-regression` list.  Anchor: "mcp/tests/test_evidence_catalog_gate_boundaries.py" [27]





> Retained earlier citation wording: - The catalog declares test_evidence_catalog_gate_boundaries.py as an exact consumer on the evidence-catalog fixture, settings-guard and Node-lockfile artifact rows. These three declarations do not establish invocation. [28]

- The catalog declares test_evidence_catalog_gate_boundaries.py as an exact consumer on the evidence-catalog fixture, settings-guard and Node-lockfile artifact rows. These three declarations do not establish invocation. [28]
