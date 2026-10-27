# Python Test Evidence Infrastructure Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support/testing` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository-owned pytest isolation and evidence infrastructure. Ordinary pytest bootstrap and certifying startup are distinct. `pytest_bootstrap.py` supplies optional seeded collection ordering, an isolated cache directory for the pytest process, and the check that a test restores owned module-level state. Per-test restored rows, module-boundary reset rows and constant-for-tests rows have distinct treatments in a closed register; the register's collection-reset pass touches only already-loaded product owners. The module fixture separately imports the explicit kernel worktree-service holder and resets that object before and after the module; it is outside the syntactic collection census. The ordinary bootstrap carries no certifying or external-service capability. `certifying_bootstrap.py` admits a Dagger quality process before resolving the candidate test process.

The route also owns instruction-wording registries and readers used to check the shipped instruction corpus. These helpers do not hold an AR seat or author knowledge. Test qualification, completed curation, semantic acceptance and Git publication retain their separate authorities; running a bootstrap or validator does not itself supply acceptance. Canonical skill sources and their sole generated package copy belong to the synchronization owner, `scripts/sync-skills.py`; no harness skill mirror is produced.

The closed product-process register now includes agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED with the default reset treatment and existing _clear resetter between test modules. It is not a per-test-restored lock. The shared guard and treatment rules remain unchanged; registration is not execution of the reset control.

## Hot Path Summary

- **Process setup.** `hermetic_bootstrap.py` sets up the candidate and pytest environment. `global_state.py` snapshots, restores and resets registered module-level state. `random_order.py` shuffles collected items when supplied a seed. `dagger_admission.py` mints the testing-layer capability after matching the Dagger environment nonce to the attestation file.
- **Source facts.** `dependency_facts.py` derives import, pytest-plugin and consumer facts from source; it holds no ownership declarations. Its disposable per-file store keys source bytes and parser identities, while each build reconstructs current population and relations. `consumer_inventory.py` holds the bounded inventory of Python-test evidence consumers.
- **The two test catalogs.** `lane_manifest.py` loads test-file lane membership. `evidence_lanes.py` checks it at collection and exposes category markers; its registry also maps cadence triggers to marker expressions. `evidence_lifecycle.py` validates governed test artifacts and provides the command-line entry for both catalogs. `evidence_governance.py` decides which files are governed. `catalog_canonical.py` supplies canonical-form findings and the rewrite behind `evidence_lifecycle --write`.
- **Candidate-bound evidence.** `candidate_snapshot.py` gives the Git identity of a working candidate for non-certifying evidence routes. `evidence_provenance.py` records candidate and machine provenance for non-accepting Dagger evidence.
- **Selection and reporting.** `retry_selection.py` collects the canonical population and executes only explicitly supplied retry files that were collected. `causal_dependency.py` derives exact-node source dependencies; `causal_failures.py` skips nodes identified by a causal preflight report and classifies observed failures. `cadence_runner.py` supplies non-accepting Dagger evidence for scheduled, provider-bump and migration triggers. `pytest_phase_reporter.py` records node outcomes and phase timings.
- **Condition waits.** `waits.py` supplies synchronous and asynchronous named-condition waits under one shared hang guard. The condition supplies readiness; neither the guard nor the poll interval proves a producer had an opportunity.
- **Instruction corpus.** `curation_doctrine.py` holds retired curation wording, corrected loop-gate field names and required instruction statements. `retired_leaf_handover_wording.py` holds verbatim retired handover sentences with their source carriers. `leaf_instruction_wording.py` holds affirmative clause tables and normalized readers for wording tests.

## Construction And Operating Model

Ordinary local pytest uses the reusable bootstrap. Its random-order option defaults to no seed, so collection is shuffled only when a seed is supplied. Session isolation supplies a temporary cache location; autouse fixtures restore registered mutable mappings after each test and reset registered process state before and after each module. Certifying entry uses `prepare_certifying_pytest_bootstrap`, which obtains Dagger admission before its own candidate setup.

Dependency analysis reconstructs the current file population, module ownership and relationships on each build. Per-file facts can be reused from a disposable store using a key that includes the analysis implementation, Python version, module identity, package identity and source bytes. The lane and lifecycle validators compare declarations with that source-derived population and ownership graph.

The instruction helpers retain retired sentences separately from affirmative wording requirements. `curation_doctrine.py` normalizes readings and confines retired-sentence matches to the sources that carried them, across canonical and generated skill surfaces. It also checks loop-gate field wording and compact curation-policy statements. `retired_leaf_handover_wording.py` supplies source/sentence pairs; `leaf_instruction_wording.py` supplies affirmative clause alternatives and normalized checks used by the wording tests. These are wording checks, not semantic acceptance or knowledge verdicts.

### The Two Test Catalogs

This route reads and rewrites `mcp/tests/evidence-lifecycle.toml`, the governed test-artifact and consumer catalog, and `mcp/tests/test-evidence-lanes.toml`, the test-file lane catalog.

| Check | Where it lives | The question it answers | Its repair |
| --- | --- | --- | --- |
| Consumer oracle | `load_evidence_inventory` in `evidence_lifecycle.py` | Do declared consumers equal source-derived consumers, does every governed file have a row, and does every row identify governed evidence? | `--write` derives consumer lists; adding or retiring a row requires a decision and manual editing. |
| Lane population | `load_lane_manifest` in `lane_manifest.py` | Does every current test file have exactly one lane, and is every listed path a current test file? | Add the lane line manually; `--write` removes lines whose files no longer exist. |
| Canonical form | `catalog_canonical.py`, called by both loaders | Are contract rows ordered by ID, artifact rows by path, and path lists ordered without duplicates and written one path per line? | Run `--write`. |

The repository-catalog test calls both loaders rather than pinning catalog bytes or a row count. The loaders compute the source facts needed for population and consumer checks when they run.

`python -m agents_remember_test_support.testing.evidence_lifecycle --project-root .` validates the lifecycle catalog and then the lane manifest, sharing one cached source graph. With `--write`, it instead computes canonical text for both catalogs before writing either. It orders rows and lists, removes duplicate list lines, replaces the consumers of `exact` and `exact-source` rows when source analysis yields a nonempty set, and removes lane lines whose files no longer exist. For consumer lists without a derived replacement, it removes missing-file lines only when at least one listed consumer still exists. If the source tree yields no consumer, it reports that fact and retains the declared list subject to that missing-file cleanup; a list consisting entirely of missing consumers survives for an explicit retirement decision.

The rewrite adds and removes no row and never assigns a lane. It refuses before writing either catalog when parsing fails, dependency facts are incomplete or ambiguous, or a table header or list cannot be read by its line rewrite. Computing both outputs first protects against those refusals; the two subsequent file writes are sequential.

Git merges both catalogs by union. Such a merge can duplicate or reorder list lines, restore a deleted line, or interleave added rows. The loaders refuse canonical-form defects and stale membership. For a TOML parse error, the shared reader explains that rows may have been interleaved and tells the reader to restore the landed file and add the leaf's row again. Both loaders use that reader; pytest startup reads the lane manifest through it before collection.

The lane loader runs during test collection. The lifecycle loader runs through the validator command, the Git hook's deterministic fast tier (also called by its targeted tier), the quality plan, the dependency selection graph, and `test_the_repository_catalogs_are_in_canonical_form`, whose file is declared in the unit lane. A change adding a test file adds its lane line and runs the canonical rewrite. Catalog rewrite and refusal cases live in `mcp/tests/test_evidence_catalog_canonical_form.py`; `mcp/tests/test_evidence_catalog_gate_boundaries.py` checks a canonical catalog whose declared consumers no longer describe the source tree.

The closed register also gives the existing closeout digest-file stats, lifecycle location cache and lifecycle operation-record cache ordinary `_clear` resets at module boundaries. It adds no scanner exemption or production reset; restored rows retain their per-test treatment.

Those retained lifecycle caches belong to the independent worktree landing chain. The removed ambient-session singleton and lifecycle-log cache are no longer registered, and their ambient heartbeat reset helper is gone. The register's collection-reset pass still visits only already-imported owners; removing retired owners adds neither a scanner exemption nor a production reset. Separately, the pytest fixture explicitly imports and resets the kernel service holder; the old blanket imported-only account does not describe this object reset.

## Local Invariants And Boundaries

- Ordinary pytest setup has no certifying or external-service authority. Dagger admission is mandatory at the certifying composition boundary; neither admission nor running the bootstrap alone establishes acceptance.
- Restored mutable rows are repaired after each test before a detected leak fails the test. Reset rows are cleared at module boundaries, with registered cleanup routines finishing owned workers or resources where required. Constant-for-tests rows retain import-time and deferred registrations. Seeded ordering uses its own random generator and leaves the process-global generator untouched.
- Dependency ownership is derived from source rather than lifecycle declarations. Lifecycle metadata describes governed artifacts and their ownership obligations; it does not establish completed curation, semantic acceptance or publication status.
- The disposable facts store is intended not to replace source truth or hide a source error. The current reader rejects malformed or unusable entries, but a well-shaped cached entry is reused without comparison to newly parsed source. That limits the existing corruption guarantee: a well-shaped incorrect entry under the matching key is not detected by these predicates.
- Lane membership and catalog coverage are exact: missing, stale or conflicting declarations produce findings. Lifecycle consumer lists must equal the derived consumer set.
- Both catalogs must have canonical row and list order, without duplicate list lines and with one path per line. Canonical-form findings identify the rewrite command. Rewriting does not decide row retirement or lane assignment.
- Retry selection validates explicit candidate-relative Python paths against executable items or successful module collection, including zero-body modules. It does not derive ownership itself; the dependency owner supplies the retry paths.
- Causal dependency derivation uses exact source-level node relationships. Runtime suppression consumes the exact nodes in its causal preflight report, rather than suppressing a whole module by filename.
- Condition readiness is separate from the shared hang guard.

## File-Level Onboarding Map

The generated route index lists the source files of this route and their cards.

**L184.** The reset register gains one row: the retained host role records of `serving.projections.host_activity` (`_ROLE_RECORDS`) are forgotten between test modules, so one module's reconciled roles cannot certify the next one's boot. That registration is all this file changes; the provider-limit fixture files and the stamped-end inputs the new cases use stay with the cases and the helpers that build them, and no fixture is constructed or executed here.

## Evidence

- The ordinary bootstrap carries no certifying or external-service capability. [1]
- Certifying setup admits Dagger before it resolves the candidate. [2]
- Retry execution keeps only explicitly supplied files of the collected population; dependency ownership is supplied by the caller. [3]
- The rewrite computes both new catalogs before it writes either. [6]
- The command validates both catalogs on one cached source graph, or rewrites them with `--write`. [7]
- The union merge attribute for both catalogs. [8]
- A leaked change of owned module-level state fails the test after restoration. [9]
- Seeded ordering uses its own random generator. [10]

- The curation-doctrine registry and the statements a canonical instruction source must make. [13]


- The lifecycle loader starts with canonical-form findings and then validates against the source tree. [15]
- The lane loader reports noncanonical lane lists and compares declared files with test modules. [16]

- The registry of retired curation sentences. [17]

- The shared parse refusal explains possible row interleaving and restoration of the landed file. [18]
- Condition readiness is separate from the shared hang guard. [20]
- Content identities reuse per-file facts without freezing current graph membership. [21]
- The rewrite preserves an entirely missing consumer list when no nonempty derived replacement exists. [22]
- Cached facts are checked for shape and reused under their content key, without a fresh-parse equality check. [23]

- Retired handover wording is source/sentence data; affirmative wording uses normalized clause alternatives. [24]


- The deterministic Git hook fast tier invokes the lifecycle-catalog command; the targeted tier calls that same fast tier. [25]


- The closed product-process register now includes agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED with the default reset treatment and existing _clear resetter between test modules. It is not a per-test-restored lock. The shared guard and treatment rules remain unchanged; registration is not execution of the reset control. [26]




- **Historical source-bound reference account, not an operative override:** The register assigns distinct reset, restored and constant treatments. [19]




- The closed register also gives the existing closeout digest-file stats, lifecycle location cache and lifecycle operation-record cache ordinary `_clear` resets at module boundaries. It adds no scanner exemption or production reset; restored rows retain their per-test treatment. [27]




- The current closed register omits retired ambient-session/log owners while retaining closeout and worktree landing-chain cache resets. [28]



- The synchronization owner projects canonical skills to the sole declared package target, preserving every declared-copy check without harness mirrors. [14]

- The collection register and explicit kernel service-holder reset are separate module-isolation paths; new explainer and watcher collections join the closed register. [29]
