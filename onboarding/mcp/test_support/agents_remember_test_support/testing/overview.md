# Python Test Evidence Infrastructure Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support/testing` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository-owned pytest isolation and evidence infrastructure. Ordinary pytest bootstrap and certifying startup are distinct. `pytest_bootstrap.py` supplies optional seeded collection ordering, an isolated cache directory for the pytest process, and the check that a test restores owned module-level state. The closed register gives per-test restored, module-boundary reset, constant-for-tests and owner-quiescent states separate treatments. Only reset rows for already-loaded product owners are reset at module boundaries. The module fixture separately imports the explicit kernel worktree-service holder and resets that object before and after the module; it is outside the syntactic collection census. The ordinary bootstrap carries no certifying or external-service capability. `certifying_bootstrap.py` admits a Dagger quality process before resolving the candidate test process.

The route also owns the instruction-wording registries, readers, delivery and pointer checks, and capsule audience and budget fixtures used to check the shipped instruction corpus, plus a few single-regression helpers. The [tool-answer fixture helper](tool_answer_fixtures.py.md) owns real temporary paths of controlled width and temporary XDG settings for row measurements. These helpers do not hold an AR seat or author knowledge. Test qualification, completed curation, semantic acceptance and Git publication retain their separate authorities; running a bootstrap or validator does not itself supply acceptance. Canonical skill sources and their sole generated package copy belong to the synchronization owner, `scripts/sync-skills.py`; no harness skill mirror is produced.

The closed product-process register now includes agents_remember.kernel.primitives.runtime_config._LEGACY_GATE_DELEGATION_WARNED with the default reset treatment and existing _clear resetter between test modules. It is not a per-test-restored lock. The shared guard and treatment rules remain unchanged; registration is not execution of the reset control.

## Hot Path Summary

- **Process setup.** `hermetic_bootstrap.py` sets up the candidate and pytest environment. `global_state.py` snapshots, restores and resets registered module-level state. `random_order.py` shuffles collected items when supplied a seed. `dagger_admission.py` mints the testing-layer capability after matching the Dagger environment nonce to the attestation file.
- **Source facts.** `dependency_facts.py` derives import, pytest-plugin and consumer facts from source; it holds no ownership declarations. Its disposable per-file store keys source bytes and parser identities, while each build reconstructs current population and relations. `consumer_inventory.py` holds the bounded inventory of Python-test evidence consumers.
- **The two test catalogs.** `lane_manifest.py` loads test-file lane membership. `evidence_lanes.py` checks it at collection and exposes category markers; its registry also maps cadence triggers to marker expressions. `evidence_lifecycle.py` validates governed test artifacts and provides the command-line entry for both catalogs. `evidence_governance.py` decides which files are governed. `catalog_canonical.py` supplies canonical-form findings and the rewrite behind `evidence_lifecycle --write`.
- **Candidate-bound evidence.** `candidate_snapshot.py` gives the Git identity of a working candidate for non-certifying evidence routes. `evidence_provenance.py` records candidate and machine provenance for non-accepting Dagger evidence.
- **Selection and reporting.** `retry_selection.py` collects the canonical population and executes only explicitly supplied retry files that were collected. `causal_dependency.py` derives exact-node source dependencies; `causal_failures.py` skips nodes identified by a causal preflight report and classifies observed failures. `cadence_runner.py` supplies non-accepting Dagger evidence for scheduled, provider-bump and migration triggers. `pytest_phase_reporter.py` records node outcomes and phase timings.
- **Condition waits.** `waits.py` supplies synchronous and asynchronous named-condition waits under one shared hang guard. The condition supplies readiness; neither the guard nor the poll interval proves a producer had an opportunity.
- **Instruction corpus.** `curation_doctrine.py` holds retired curation wording, corrected loop-gate field names and required instruction statements. `retired_leaf_handover_wording.py` holds verbatim retired handover sentences with their source carriers. `leaf_instruction_wording.py` holds affirmative clause tables and normalized readers for wording tests, and `delivered_step`, which reads a named detail through real admission, compilation and launch delivery. `capsule_wording.py` resolves each leaf clause on its delivered role, operation or owning detail section. `coordination_wording.py` and `curator_contracts.py` hold expected coordination and Curator clauses; `curator_instruction_delivery.py` checks the delivered Curator, Reviewer-intake and refused-write wording. `pointer_uniqueness.py` checks that each first message points to a lifecycle file once per action, `manifest_step_derivation.py` collects action and reader-role associations for classified Markdown references from first-message and detail pointers, and `task_document_instruction_contracts.py` checks the task-authoring pointers, conventions, templates and manifest entries. `instruction_consistency.py` checks that commands, tools, `task_doc` operations and paths named in skills, docs and README exist.
- **Renewed instruction facts.** `instruction_renewal.py` supplies the canonical renewal command and loads the instruction tooling belonging to this checkout. `digest_map.py` composes authored map decisions with generated bindings and checks source/digest traceability. `pointer_policy.py` joins stable admission policy with separately generated wording; `pointer_sentences.py` resolves link targets and derives sentence actions without loading admission policy. `pointer_renewal_cases.py` checks current checkout wording and supplies explicit fixture controls for identity binding, ambiguity and unchanged admissions. `capsule_audience_structure.py` independently projects operation source for the addressed role, selects foreign-role passages for test controls and counts detail-link occurrences.
- **Capsule audience and budgets.** capsule_audience_fixtures.py holds reviewed pointer and clause tables and retained historical hashes; the v13 modules retain historical inverse records. Current audience tests compare compiled passages with role-addressed source and derive ordinary detail-link counts from source. `capsule_budget_snapshot.py` holds the frozen capsule-budget measurements; `capsule_budget_d694.py` checks the frozen `capsule-budgets-d694.json` record, and `capsule_budget_d695.py` checks the current `capsule-budgets-current.json` record.
- **Single-regression helpers.** `agent_eval_checkout_provisioning.py` asserts that agent-eval trial provisioning declares test mode and that the scratch CLI child loads the trial's own settings. `memory_orphan_checkpoint.py` crashes a parked-candidate sync before its journal publish and requires recovery to keep every parked memory file.

## Construction And Operating Model

The reset register names the process owners for TypeScript anchor inputs and lifecycle journal records. Tests of native calls observe separate request scopes that clear their own state.

Ordinary local pytest uses the reusable bootstrap. Pytest configuration installs the shared test loop factory for Runner and the public asyncio loop constructor. Cleanup restores both aliases. The factory caps idle selector waits at 50 milliseconds so a denied wake-up send cannot leave a queued callback waiting for a socket event. Test-authored dashboard and historical-review children use the same factory. Its random-order option defaults to no seed, so collection is shuffled only when a seed is supplied. Session isolation supplies a temporary cache location; autouse fixtures restore registered mutable mappings after each test and reset registered process state before and after each module. Certifying entry uses `prepare_certifying_pytest_bootstrap`, which obtains Dagger admission before its own candidate setup.

Dependency analysis reconstructs the current file population, module ownership and relationships on each build. Per-file facts can be reused from a disposable store using a key that includes the analysis implementation, Python version, module identity, package identity and source bytes. The lane and lifecycle validators compare declarations with that source-derived population and ownership graph.

The instruction helpers retain retired sentences separately from affirmative wording requirements. `curation_doctrine.py` normalizes readings and confines retired-sentence matches to the sources that carried them, across canonical and generated skill surfaces. It also checks loop-gate field wording and compact curation-policy statements. `retired_leaf_handover_wording.py` supplies source/sentence pairs; `leaf_instruction_wording.py` supplies affirmative clause alternatives and normalized checks used by the wording tests. The delivery checks read instructions through the product's own admission, compilation and launch composition rather than concatenating source files, and they start no role. These are wording checks, not semantic acceptance or knowledge verdicts.

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

Fixture Git commands use a repository-local home and disable system configuration. The shared crossing fixture builds selected revisions, records closed review facts and checks state and writer credit after retention and conversion. Both helpers operate on test-owned repositories.

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

## Retained Evidence Context

- Retired handover wording is source/sentence data; affirmative wording uses normalized clause alternatives.

## Evidence

### Repo-Internal References

- Retired handover wording is source/sentence data. Affirmative wording uses normalized clause alternatives. Each retired sentence is detected only on its own source, and a removed source stays absent. [24]

- The ordinary bootstrap carries no certifying or external-service capability. [1]

- Certifying setup admits Dagger before it resolves the candidate. [2]

- Retry execution keeps only explicitly supplied files of the collected population; dependency ownership is supplied by the caller. [3]

- The rewrite computes both new catalogs before it writes either. [6]

- The command validates both catalogs on one cached source graph, or rewrites them with `--write`. [7]

- The union merge attribute for both catalogs. [8]

- A leaked change of owned module-level state fails the test after restoration. [9]

- Seeded ordering uses its own random generator. [10]

- The curation-doctrine registry of retired statements. The statements a compact canonical instruction source must make. [13]

- The lifecycle loader starts with canonical-form findings and then validates against the source tree. [15]

- The lane loader reports noncanonical lane lists and compares declared files with test modules. [16]

- The registry of retired curation sentences. [17]

- The shared parse refusal explains possible row interleaving and restoration of the landed file. [18]

- Condition readiness is separate from the shared hang guard. [20]

- Content identities reuse per-file facts without freezing current graph membership. [21]

- The rewrite preserves an entirely missing consumer list when no nonempty derived replacement exists. [22]

- Cached facts are checked for shape and reused under their content key, without a fresh-parse equality check. [23]

- The deterministic Git hook fast tier invokes the lifecycle-catalog command; the targeted tier calls that same fast tier. [25]


- The closed process registry gives _LEGACY_GATE_DELEGATION_WARNED the default _clear reset between test modules when its owner is already loaded. [26]



- The process register declares separate reset, restored, constant-for-tests and quiescent treatments. [19]



- The closeout digest-file stats, lifecycle location cache and process-owned lifecycle operation-record memo use ordinary _clear resets between test modules. [27]



- The process register retains closeout and worktree landing-chain cache resets. It omits the former ambient session and log owners. [28]


- The synchronization owner projects canonical skills to the sole declared package target, preserving every declared-copy check without harness mirrors. [14]


- The collection register and explicit kernel service-holder reset are separate module-isolation paths. The collection register includes the explainer and watcher collections. [29]


- Six instruction helpers own checkout-local renewal loading, digest traceability, policy/wording projection, pointer parsing and binding controls, and source-derived audience/link comparisons. [30]
- Manifest step derivation collects actions and reader-role associations for classified Markdown references from first-message and detail pointers. [31]

- The shared factory bounds selector idle waits, and pytest restores its two factory aliases at cleanup. [32]
- Fixture Git uses a private HOME and captures command failure output. [38]
- Crossing fixture controls compare attributed state and writer before and after selecting or converting bytes. [39]
