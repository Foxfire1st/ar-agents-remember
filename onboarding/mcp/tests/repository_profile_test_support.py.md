# mcp/tests/repository_profile_test_support.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

One typed builder for repository-profile contract tests and their fixture repositories: it
declares Node and Rust fixture source inventories, installs the Agents Remember certification profile and
repository-matched fixture profiles, and composes complete `RepositoryCertificationProfile` instances with the
exact selector, executor, decoder, rail, and artifact declarations the profile validator requires.

## Code Commentary

### Logic

`FixtureRepository` declares the language root, locked image reference, and rail specs;
`NODE_FIXTURE`/`RUST_FIXTURE` carry the two non-Python fixtures. `fixture_profile`
builds a complete profile with four code gates and the repository-test selector. L19 upgraded
that selector to `schemaVersion="repository-selector-result/v2"`, version `2.0.0`, an empty
declared `externalInputs` tuple, and a command that consumes
`{selector-output}`, `{selection-mode}`, `{diff-base}`, `{candidate-kind}`,
`{candidate-value}`, `{selector-id}`, `{selector-version}`, and
`{selector-configuration-digest}` — matching the v2 fixture scripts.


The CCR-R12@v4 extensions (260831-CCR-L12, commit `cfd09381`) introduced gate/wave placement,
runtime image identity and execution-manifest fixtures. The current `dagger_runtime_digest`
recomputes the Dagger source digest recursively across the module and its subpackages.
`fixture_execution_manifest` compiles the `repository-certification-admission/v1` manifest with a
fixture `dagger-runtime-authority/v1` snapshot. `FakeContainer`/`FakeFile`/`FakeDag` double the
Dagger graph so portable profile execution functions can run without a daemon.
`install_fixture_profile` writes a repository-matched generic profile and recomputes its digest;
`install_agents_remember_profile` copies the real profile into a temporary repository root.
`agents_remember_profile_execution` admits that profile with an explicit synthetic source-selection
fixture except for local precommit. This is compiler input, not an observation of a Git checkout.
`write_source_selection_artifacts` reads the exact plan's frozen applicability decisions and writes
each declaration's evidence path as canonical UTF-8 JSON. It does not replace a not-applicable
decision with an executed rail. The generic adapter declares retained-report transport, while the
fixture execution manifest carries an explicit placeholder comparison base and test runtime authority.

The fixture profile now declares a finite per-rail `rail-evidence/<identity>.log` publication with `application/octet-stream` media type; capture bytes need not form UTF-8 text. `FakeContainer` supplies known producer fixture files for graph interpretation, copies `FakeFile` contents into output paths and exposes actual empty stdout/stderr values. Hash reads use a detached fake container so inspecting a file does not append a hash command to the subsequent rail history. These marker files, including the causal-preflight report, are explicitly fixture output, not live acceptance artifacts.

`fixture_environment_census` loads the production census owner and calls `build_census` over real
temporary dependency files in each declared directory scope. The SDK double uses this helper for
census creation and reconstruction comparison. Census execution returns a detached container with
a copied file map, so the retained census file does not appear on the parent used by later rails.
Reconstruction compares the original census with a fresh census; a mismatch yields exit code 66
and no verification output, while equality emits the matching census and declaration digests.

### Conventions

Keep repository-source literal readers visible to dependency ownership. The ambient runner path used by the producer fixture causes its importers to join the exact test-consumer closure.

### Invariants And Boundaries

- Generic profiles declare their own language rails and source inventories; copying the real repository profile is an explicit fixture choice.
- Selector commands bind every identity placeholder the v2 contract requires (L19).
- Source-selection and runtime-authority fixtures are explicit compiler inputs, not live Git or engine observations.
- The census builder reads actual temporary dependency files; ordinary rail commands and their marker output remain SDK doubles.
- Census output belongs to its detached file map, while source-applicability evidence comes from the supplied frozen plan.

### Todos

None recorded.

## Evidence

### Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

No configured external domain source.

### Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

- Tests copy the real profile into an isolated fixture repository. [1]
- Portable fixture installation retains a canonical profile digest. [2]
- Each language fixture declares source inventory, runtime and artifact identities. [3]
- The profile builder includes complete selectors, adapters, decoder and finite binary capture publications. [4]
- Runtime source identity is recomputed from the actual Dagger module files. [5]
- Portable execution receives an explicit comparison-base placeholder and test runtime-authority manifest. [6]
- The SDK graph double records operations and separates detached hash output from rail execution. [7]
- Known producer marker bytes are populated for interpreter tests only. [8]
- File operations expose the retained fixture value. [9]
- The fake client supplies the graph container without a daemon. [10]
- The real profile is admitted with explicit synthetic source-selection input outside local precommit. [11]
- Frozen applicability decisions are emitted at their exact declared paths as canonical JSON. [12]
- The production census owner reads actual tiny dependency files in each declared scope. [13]
- Census and reconstruction output use a detached file map and preserve the parent container. [14]

### Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

No cross-repository evidence is required.
