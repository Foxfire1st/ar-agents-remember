# mcp/tests/test_agents_remember_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_agents_remember_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the Dagger module itself is pinned, parseable, fail-closed, and builds the intended clean quality graph before live Docker execution is considered trustworthy. Since the root-owned canonical Python bootstrap repair (commit eb05a8727801) it additionally proves the installer and the runtime-directory/symlink linkage are distinct, ordered Dagger exec nodes whose failure cannot be masked.

## Code Commentary

### Logic

In-process fake Dagger objects record container graph construction. The tests cover pinned
manifest/image inputs, targeted and full argument selection, real/fake Codex probe wiring,
export-before-verdict behavior, invalid public inputs, and green/red verification. The public
quality and non-accepting evidence routes must expose their generated Dagger contracts. Tests
load the Dagger package from the explicit `.dagger/src` source root; the surrounding `.dagger`
directory is not an import root.

ARSPAWN-L5 also pins the repository-owned ambient-role harness as a Dagger graph prerequisite. The
test enumerates every harness Python module, requires each one to parse, and requires the quality
graph to invoke `scripts/e2e_harness/run.py` before the ordinary wrapper.
Its focused tmux contract now proves both halves of isolation: server commands use the exact
fixture socket root with server-scoped `exit-empty`, and the generated Codex MCP registration
whitelists `TMUX_TMPDIR` so dispatch cannot create sessions in another server.
The focused discovery-evidence regression also pins Codex's current `Wall time`/`Output` tool-result
envelope: positive and negative structured results retain their meaning, while an arbitrary prefix
cannot masquerade as the canonical envelope.

The graph-result assertions now distinguish attempted, completed, skipped, and failed steps. A
nonzero E2E exit cannot be represented as a completed/passed ambient proof, while the explicit
targeted not-selected exit is recorded as a skip and allows the ordinary wrapper to continue.
`promptSubmitted` and `codexProtocol` are derived from those observed states rather than hardcoded
success values, so a partial graph cannot manufacture real-Codex evidence.

The candidate-construction proof now requires the checksum-bound source-build step to precede
workspace materialization, requires the canonical runtime to create the venv, and requires frozen
uv synchronization before any attempt-specific cache input. A broad container image or version
label cannot stand in for the runtime provenance contract. The 2026-09-03 bootstrap repair sharpened
`test_candidate_setup_precedes_every_attempt_specific_cache_input`: the test
finds the installer exec (needle `install-python-runtime.sh`) and a distinct runtime-directory
symlink exec whose needle is the quoted cpython symlink target carrying the `AR_PYTHON_VERSION`
variable (in the Dagger graph text), asserts the installer node is `bash -euc` with `exec bash`
and no `ln -s`, asserts the link node contains no installer invocation, and requires the exact
order installer < link < workspace source < uv sync < late per-attempt environment.


CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`) reworks the suite around the cost-ordered five-gate
execution and the shared runtime authority: the module-level fake Dagger objects drive the portable
`_execute_gate_rails` profile execution, `runtime_authority_manifest` binds the
admitted `dagger-runtime-authority/v1` digest into execution manifests (`_require_plan_authority`
refuses a missing or mismatched digest), `test_dagger_quality_red_gate_one_still_terminalizes_every_gate_one_sibling`
(lines 956-1027) proves exhaustive same-gate terminalization with zero later-gate starts, gate-four
applicability and real-Codex-rail facts are pinned, a rail runtime outside the
admitted adapter image is refused, and full-mode selection uses the explicit diff
base without targeted flags.

The full-mode browser command must run through `env PLAYWRIGHT_JSON_OUTPUT_FILE=/reports/dashboard-e2e-result.json npm run e2e -- --fail-on-flaky-tests --reporter=line,json`. The graph test checks this complete persisted-result contract while preserving the explicit diff base and absence of targeted flags.

### Conventions

The suite tests graph semantics without a daemon; live field proof remains a separate Dagger run.

### Invariants And Boundaries

- Unit doubles may replace Dagger transport but not command/graph selection.
- Reports must export at the exact completed boundary even for a red run.
- Invalid mode, omitted/blank diff base, or memory inputs refuse.
- Generated Dagger help is tested as part of the public quality-function contract.
- `load_dagger_module` must prepend exactly `DAGGER_SOURCE_ROOT`; broadening the certifying
  container's global `PYTHONPATH` to hide a bad test loader would mix orchestration code into the
  application import surface.
- Runtime build, source materialization, dependency synchronization, and attempt-specific cache
  inputs remain strictly ordered; candidate-specific state cannot contaminate the shared runtime
  or dependency layers.
- The runtime installer exec and the version-suffixed symlink exec are two distinct, ordered nodes;
  only a successful installer can reach the linkage node, so installer failure cannot be masked by
  a preexisting runtime.
- The ambient-role harness may not disappear from the Dagger graph or acquire an unparseable helper
  without failing this structural test before live container execution.
- Tmux isolation is incomplete unless both direct fixture commands and Codex-spawned candidate MCP
  children inherit the same `TMUX_TMPDIR`.
- Failed, skipped, and completed ambient runs must produce different result evidence; graph
  construction alone never implies a prompt was submitted or the ambient protocol completed.
- Discovery success is proven from the structured public result inside the exact current Codex
  envelope, not from assistant completion text or a substring search.

### Todos

None.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Dagger loader uses only the explicit source root. | `load_dagger_module` | mcp/tests/test_agents_remember_quality.py:66-72 |
| Fixture tmux subprocesses stay in their isolated socket namespace. | `test_ambient_role_chat_tmux_commands_use_only_the_fixture_socket_root` | mcp/tests/test_agents_remember_quality.py:258-287 |
| Candidate MCP children receive the declared tmux namespace. | `test_ambient_role_chat_candidate_mcp_inherits_fixture_tmux_namespace` | mcp/tests/test_agents_remember_quality.py:290-309 |
| Only canonical structured discovery results establish success. | `test_ambient_role_chat_discovery_decodes_current_codex_tool_result_envelope` | mcp/tests/test_agents_remember_quality.py:313-324 |
| The runtime installer, link, source, dependencies and attempt-specific cache inputs are ordered. | `test_candidate_setup_precedes_every_attempt_specific_cache_input` | mcp/tests/test_agents_remember_quality.py:327-400 |
| The public Dagger module contract remains pinned and parseable. | `test_agents_remember_quality_module_is_pinned_and_parseable` | mcp/tests/test_agents_remember_quality.py:167-191 |
| Missing or mismatched Dagger admission refuses. | `test_python_suite_refuses_missing_or_mismatched_dagger_attestation` | mcp/tests/test_agents_remember_quality.py:478-505 |
| One profile-declared terminal result remains authoritative. | `test_agents_remember_quality_exports_failures_as_the_only_authoritative_result` | mcp/tests/test_agents_remember_quality.py:520-529 |
| Targeted execution follows the admitted profile commands and metadata. | `test_dagger_quality_executes_the_exact_targeted_profile_plan` | mcp/tests/test_agents_remember_quality.py:591-673 |
| Full execution requires the complete JSON browser reporting command. | `test_dagger_quality_full_uses_explicit_diff_base_without_targeted_flags` | mcp/tests/test_agents_remember_quality.py:919-962 |
| A red first gate terminalizes its siblings and prevents later starts. | `test_dagger_quality_red_gate_one_still_terminalizes_every_gate_one_sibling` | mcp/tests/test_agents_remember_quality.py:965-1011 |
| The graph fixture records files, commands and environment without external transport. | `FakeContainer` | mcp/tests/repository_profile_test_support.py:579-729 |
| The fake client is a same-repository contract fixture. | `FakeDag` | mcp/tests/repository_profile_test_support.py:806-814 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## R39 Guard Wiring Proof

The quality entry-point tests patch the shared production validator through conftest and require
its Dagger refusal to become pytest usage failure. They no longer test a second local attestation
implementation.

## 260824-PDLS Certifying Graph Proof

The suite now exercises `testing.dagger_admission` and the conftest certifying composition instead
of the deleted code-quality validator. Dagger command construction must export
`/reports/pytest-phases.json`, and result timestamps must be ordered. Invalid admission still
refuses before collection; phase output remains observation rather than authority.

## 2026-08-26 Evidence-Graph Reconciliation

The Dagger module contract exposes `quality` for certifying acceptance plus separate non-accepting
cadence, causal, retry, retry-matrix, and route-measurement evidence routes. The quality graph
fetches the candidate bundle, stages the complete candidate, requests the causal-failure report,
and publishes that report reference in its authoritative result. Evidence routes cannot become
acceptance merely because their commands execute successfully.

The retry-matrix graph distinguishes an executing scenario from a plan-only fail-closed scenario
using the wrapper's explicit pytest result. Executing scenarios require `result: pytest PASS`;
plan-only scenarios require `result: pytest SKIPPED ...` and reject an absent result or a real
pytest failure. This prevents the harness from treating its own explicit non-execution marker as
evidence failure.

Candidate construction has one deterministic base boundary: pinned image and dependency caches,
OS/tool installation, exact source and repository-bundle reconstruction, and the editable package
install all precede attempt-specific state. Only after that base is built may the graph mount the
retry-proof cache or bind the attestation nonce, report paths, and other per-attempt environment.
`test_candidate_setup_precedes_every_attempt_specific_cache_input` structurally rejects a graph
that lets a fresh nonce or report destination invalidate the expensive shared candidate base.


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Reconciled the full-mode browser command to its persisted JSON result contract and refreshed current graph-test and shared-fixture reference anchors.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 4 declined citation claims against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated source-path constants from module loading. Selected the two current namespace tests rather than former line ranges. Split four tests and qualified graph execution as fake graph construction, not a live Dagger run. Repointed moved fake definitions to their actual shared support owner. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `test_ambient_role_chat_discovery_decodes_current_codex_tool_result_envelope` repointed to mcp/tests/test_agents_remember_quality.py:312-324. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `test_candidate_setup_precedes_every_attempt_specific_cache_input` repointed to mcp/tests/test_agents_remember_quality.py:327-400. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the five-gate/authority rework of the Dagger-module suite - gate-exhaustion forcing, authority-digest-bound execution manifests, adapter-runtime refusal, and gate-four applicability facts.


- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: rewrote the
  Docs References task-artifact rows as prose (absolute ar-coordination paths are not
  repo-relative citations and carry no verifiable provenance).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): documented the distinct ordered installer/link Dagger exec-node proof in `test_candidate_setup_precedes_every_attempt_specific_cache_input`; refreshed citation anchors (pinned-module, attestation, authoritative-result, and graph-construction tests moved to lines 324/635/677/748; `load_dagger_module` to line 65; the retired `test_dagger_quality_builds_the_real_probe_and_targeted_wrapper_graph` name replaced by `test_dagger_quality_executes_the_exact_targeted_profile_plan`). Verification metadata rebased from `f2b7c648` to the bootstrap repair owning commit.

- 2026-08-31T10:33+02:00 — 260821-ARSPAWN-L5 closeout repair: added the forcing regression
  for strict decoding of Codex's current execution-result envelope after generation 6 reached C09
  with six successful dispatches but zero decoded success rows. Verification remains closeout-owned.

- 2026-08-31T09:55+02:00 — 260821-ARSPAWN-L5 closeout memory repair: realigned the pinned-module,
  Dagger-attestation, authoritative-result, and graph-construction citations to their current exact
  symbol ranges. Behavior and requirement semantics are unchanged; verification remains
  closeout-owned.

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: added the structural proof that
  Codex forwards the fixture tmux namespace into its candidate MCP child and that `exit-empty` is
  set at server scope. Verification remains closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded the structural
  proof for truthful attempted/completed/skipped/failed Dagger evidence and derived prompt/protocol
  claims. Verification remains closeout-owned.

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 recorded structural ownership of the
  real ambient-role harness and its pre-wrapper Dagger stage. Verification remains closeout-owned.

- 2026-08-29T16:27+02:00 — Added structural graph proof that Dagger builds the canonical source
  runtime before materializing the candidate and synchronizes its venv before attempt caches.

- 2026-08-28T02:38+02:00 — Recorded the deterministic candidate-base versus attempt-binding
  boundary and its structural graph regression after repeated evidence runs exposed nonce-driven
  rebuilds of otherwise identical OS, tool, source, and editable-install layers.
- 2026-08-27T22:09+02:00 — Documented the focused regression contract that distinguishes actual
  pytest execution from the wrapper's explicit plan-only `SKIPPED` marker.
- 2026-08-27T14:36+02:00 — Recorded the explicit `.dagger/src` import boundary after clean Dagger
  exposed an off-by-one source-root calculation; refreshed the six-route public contract.
- 2026-08-26T10:44:52+02:00 — Documented the separate non-accepting cadence graph, causal-failure artifact, candidate staging, and exact two-function Dagger public surface.
- 2026-08-24T21:23+02:00 — Updated admission ownership and added Dagger phase/timestamp wiring proof.

- 2026-08-14T11:27+02:00 — R39 curator: recorded one shared environment-authorization owner.
  Verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: replaced the retired verify-method test reference with the
  current Dagger-attestation, single-authoritative-result, and graph-construction tests.
  Verification remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final curator pass: recorded the required explicit diff base and
  generated argument-help contract for both Dagger functions. Focused clean proof covered all 26
  tests with 20 workers; Ruff, formatting, layering, Pyright, CRAP, and all 7 changed coverage lines
  passed. Final commit provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — Created with L23's Dagger graph contract tests; verification provenance remains closeout-owned.
