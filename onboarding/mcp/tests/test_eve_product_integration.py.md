# mcp/tests/test_eve_product_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_product_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:43+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The product-surface evidence for `CAPS-R08@v1` — *eve is selectable and observable through the
existing AR product* — and, since `260915-CAPS-L17`, for `CAPS-R17@v1` behaviour 4's route exclusion.
**72 cases** over **thirteen case-bearing classes** (fifteen module-level classes in all; `_StartedEve`
and `_CatalogProbe` are helpers), each driving a **real owner**: the
settings-vocabulary registry and its readiness probe, the pre-session capability catalog over the real
adapter factory, the real `HarnessSubmissionAuthority`, the per-harness control/telemetry capability
declarations, the conversation projector registry and mapper, the real `HarnessControlBridge` over the
real adapter, and the catalogue's own terminal-evidence lift.

The module's stated discipline is that **nothing monkeypatches the code under test**. The one
deliberate dependency is the eve transport double (`eve_adapter_test_support`, reached through
`test_eve_adapter`'s own helpers): the native *process* is replaced at the transport seam, while the
adapter, event mapper, cursor, transcript and capability surface under test stay the production ones.
A case that needed the real process would be a native-evidence run, which this leaf does not own — and
the module says so rather than implying the coverage.

It is the counter-evidence to the packet's own non-conforming example: the obligation is not satisfied
by a screenshot, a prose claim, or a launch that never exercises its required behaviour.

## Code Commentary

### Logic

The classes are ordered by the surface they attack, and each one names a distinct owner:

- **`EveRegistryTests`** (694) — the curated `eve` row is last and the other three rows are unchanged;
  the row is findable by id like every other harness; it is reachable through the existing adapter
  factory; and it is detected through **its probe, never `PATH`**. *Carried caveat (defect D27, not
  this leaf's file):* `test_the_registry_leaves_the_path_harnesses_on_the_ordinary_lookup` asserts an
  environment fact — `assertFalse(entries["eve"], "no node is resolvable in this environment")` — which
  another test in the same run can falsify. It is now **deterministically reproducible**: setting
  `AR_EVE_NODE` (a node ≥ 24) in the pytest process environment reds the case in isolation, because
  `conftest` scrubs `AR_RUN_*` / `AR_SPAWN_*` / `AR_HOSTED_*` and a named list but **not**
  `AR_EVE_NODE`, which this master's own live-eve recipe sets. The defect is the assertion's **shape**
  (assert the registry's decision, or skip when a node is resolvable), not a regression; the repair
  belongs to whoever next owns that module, not to this leaf.
- **`EveTerminalLaunchTests`** (751) — eve is not PTY-launchable, so a terminal open refuses **by name**
  and yields no argv, while the path harnesses keep their ordinary detection. The distinction the
  cases pin is that the refusal is a truthful not-launchable, not a missing-install.
  `test_the_declared_exclusion_belongs_to_the_route_and_is_owned` (828) is this leaf's addition and
  carries the **named exclusion's reason and owner** in a product artifact: the route deliberately does
  not ask for a session backend, so the terminal question refuses by that decision while the
  session-backend question does not. Its docstring records the four measured route answers
  (`notes/reports/260915-CAPS-L17-evidence/s6-s7.json`), including the operator-taught PATH row that
  returns `200 running` with `instructionMode: legacy` — a green `eve` session that is not the AR
  runtime. Its assertions overlap its two siblings; the distinct content is the recorded reason and
  owner (noted for case-count hygiene, not a defect).
- **`EveReadinessProbeTests`** (710) — both halves of the readiness verdict: a missing application root
  is reported by name, a missing node runtime is reported *separately* from a missing application, the
  verdict depends on the application root and not only the interpreter, and each rejection shape —
  absent, non-executable, below the floor — is refused with its own reason.
- **`EveCapabilityDiscoveryTests`** (866) — `GET /api/harnesses/eve/capabilities` discovers eve through
  the existing factory; a runtime that cannot run refuses by name *before* discovery; an unknown
  harness refuses before discovery; the install fingerprint is the **probed interpreter**, not a
  placeholder command; and the envelope the dashboard reads has the contracted shape.
- **`EveCapabilityHonestyTests`** (1134) — the advertised model is the one the runtime would really use;
  the pinned runtime **consumes** the effort axis and the catalog publishes the axis the client would
  read (`test_the_pinned_runtime_consumes_the_effort_axis_and_the_client_would_read_it`, 1151 — the
  consumer is asserted on the authored TypeScript, the publication on the **serialized** envelope, so
  the dashboard's own read path is what is pinned); the advertised vocabulary **is** the installed
  union rather than a copy (`…the_advertised_effort_vocabulary_is_the_installed_union_not_a_copy`,
  1192 — compared against the module's recorded union constant, so the case runs on a checkout with no
  machine-local install); the effort setter refuses every candidate *including its own launch
  vocabulary*; **every published axis names its runtime consumer** (1222 — the axis-to-consumer map is
  held equal to the published set in **both** directions, so neither a published axis without a
  consumer nor a consumer whose axis was retracted can pass); eve never borrows another harness's
  capability evidence; an unknown harness fails loudly instead of inheriting a catalog; and eve's
  telemetry is declared absent rather than borrowed.
- **`EveEffortVocabularyDriftTests`** (1290) — one case, and the deliberate split that keeps the suite
  green everywhere: it confronts the recorded union constant with the **live installed** declaration
  (`_installed_reasoning_union` reads the AI SDK's own `index.d.ts`), guarded by
  `require_installed_eve_application`, so the machine-local install decides only whether **drift** can
  be observed, never whether the suite passes. The declaration is located by its own prose rather than
  a line number, and an unrecognized shape returns `None` so the case fails loudly instead of quietly
  comparing against a truncated set.
- **`EveEffortConsumerShapeTests`** (1315) —
  `test_the_authored_definition_omits_the_reasoning_key_for_the_sentinel` pins behaviour 1's sentinel
  rule in the authored **source shape**. This is the one claim the provider boundary cannot falsify: the
  AI SDK maps the exact token `provider-default` to an absent key by itself, so an application that
  *forwarded* the literal produces the same request body as one that omits the property. The case
  therefore extracts the object literal handed to `defineAgent`, strips comments, requires `reasoning`
  **not** to be a property key, requires a spread, and requires that spread to name the sentinel — the
  properties a forwarding implementation cannot satisfy.
- **`EveProjectorTests`** (1106) — every registered harness id has a projector; the projector declares
  stream-only evidence; the streaming/revise rule; one tool round trip as one item; the operator
  message preserved without claiming a producer; the two-boundary rule (one settlement per turn, the
  park is a notice); cancellation as interrupted; the missing-envelope-type refusal; the preserved
  unknown event; silence for recognized control state; and the vocabulary/census cases below.
- **`EveAdapterToProjectionIntegrationTests`** (1279) — the same facts on frames the **real adapter and
  real bridge** produced in-process, so the recorded fixture is not the only evidence.
- **`EveConversationCaptureTests`** (1442) — the projection matches the capture the mounted UI renders;
  the capture shows the states the packet names; live and replayed frames project identically; and a
  reconnect replays evidence without duplicating items.
- **`EveInteractionProjectionTests`** (1553) — an input request becomes an answerable interaction item
  and an authorization challenge becomes a waiting approval item.
- **`EveTerminalProjectionTests`** (1670) — the catalogue's real `latest_terminal_evidence` lift over
  recorded pages: cancelled-then-parked lifts as `interrupted`, ordinary-then-parked lifts as
  `completed`, a parked session alone makes **no** terminal claim, and a turn-free session failure still
  settles.
- **`EveAssetAndCredentialBoundaryTests`** (1703) — the adapter is not asset-submit capable; an
  asset-carrying submission is refused by the authority; a provider credential reaches the child that
  needs it and **never** the capability diagnostic the dashboard reads; and the capability snapshot
  model carries no credential field (pinned so a new field able to carry a secret fails a case).

Three module-level tables carry claims that a reader should not have to re-derive:

- **`_PINNED_RUN_CENSUS`** (248) — the 13 event types of the recorded pinned run, transcribed into the
  module because the recording lives in the task's coordination tree. It is a transcription **by
  design and by statement**: the case pins the *provenance labels* against it and cannot re-derive it,
  and the module says plainly that re-verifying the census itself against the recording is a reading
  act, not a test.
- **`_RECORDED_PROVENANCE`** (275) — which of `recorded` / `production-emitted` / `derived` each
  scripted frame is, so `test_every_scripted_frame_carries_an_honest_provenance_label` (1221) is
  falsifiable in five directions: promote a derived label to recorded, drop a label, add a fourth
  label kind, or move the census either way — each fails.
- **`_AUTHORIZATION_REQUIRED_FRAME_PROVENANCE`** (294) — carries the derivation for a frame whose label
  needs its reasoning recorded rather than asserted.

`_stub_interpreter()` (163) builds a REAL executable the probe actually runs, which is why the
below-floor and non-executable refusals are measurements rather than mock expectations. Its docstring
also states the environment's limit honestly: it is not a stand-in for a genuine Node binary, and no
case here claims to exercise one, because the isolated pytest environment exposes no Node at or above
the floor (`conftest` isolates `HOME`, so the nvm candidate list is empty under pytest).

### Conventions

- Every case states the surface it attacks in its name; the class docstrings name the owner driven.
- Provenance of scripted evidence is labelled explicitly, so a reader can tell production-emitted
  frames from recorded ones from derived ones without guessing.
- Fixture substitutions are scoped to the case that needs them; nothing global is patched.
- These are **unit** cases in the evidence-lane manifest (see the lane row), so the default selection
  collects them; the two integration-marked cases elsewhere in the file are deselected by the default
  selection.
- **Every helper that starts the real launch calls `require_installed_eve_application` first** —
  `_start_eve` (574, six callers), `_evidence_frames` (1296) and `_projected` (1579). The transport is
  a double, but `start` is the real launch path and it stages the application, so without the
  machine-local `eve_runtime/node_modules` install there is nothing to stage and the case **cannot run
  on this machine**; it skips by name, stating the missing path and the exact install command, rather
  than failing as though the product were broken.

### Invariants And Boundaries

- **The lane row is load-bearing.** This module's row is
  `mcp/tests/test-evidence-lanes.toml` → `[files] unit-regression` → `"mcp/tests/test_eve_product_integration.py"`.
  The lane loader is fail-closed: it raises `LaneManifestError` for any module under `testpaths`
  without an explicit row, and ordinary pytest never loads the manifest, which is how six historical
  modules shipped unregistered. A new module without a row is invisible to the lane tooling.
- **68 cases, one module, budget-checked by the default selection.** The declared ceiling lives in
  `pyproject.toml` (`unit_case_budget`); this module does not raise it.
- **Nothing here replaces the native-evidence run.** The transport double is the seam; the real
  process round trip belongs to the adapter's own leaf, and the module says so rather than implying
  otherwise.
- **A case must be falsifiable.** The provenance case, the decoder-backed capture cases and the
  terminal-lift cases were each attacked with perturbations during review, and the recorded results
  are in the leaf's evidence package.
- **The census is a transcription, not a check.** Do not read `_PINNED_RUN_CENSUS` as re-verified by
  the suite; the module states the limit in place.
- **A missing machine-local dependency is named, never retried and never silently skipped.** The guard
  says what is absent and how to install it, so an unprovisioned checkout reports `skipped` with a
  reason while a provisioned run executes the cases. Nothing here installs the runtime: a suite whose
  verdict depends on which machine ran it is the defect the guard removes. The production fail-open it
  works around — `stage_runtime_root` stages before it checks the install, so a second staging call in
  the same process passes without it (**D20**) — is **reported, not repaired** here; it belongs to the
  leaf that owns `serving/eve_runtime_launch.py`.

### Todos

None known. The seeded-mutation corpus lives in the task's coordination tree rather than in this
module, because it re-clones the tree per seed.

## Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. The one external authority the module leans on is the pinned eve
release's own event vocabulary, cited through the runtime README.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the recorded event vocabulary is the pinned release's own, cited by the runtime README. | — | — |

## Repo-Internal References

The cases drive production owners across four routes — the registry, the capability catalog, the
projector, and the terminal lift — and the mounted dashboard case consumes the capture this module's
sibling produces.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own purpose statement names the product-integration surface this suite evidences. | "eve is selectable and observable through the existing AR product surface." | mcp/tests/test_eve_product_integration.py:1-12 |
| `CAPS-R17@v1` behaviour 4 is the requirement the declared-exclusion case evidences. | "CAPS-R17 behaviour 4" | mcp/tests/test_eve_product_integration.py:828-850 |
| The registry, readiness and terminal-launch surfaces, including the owned route exclusion. | `EveRegistryTests`; `EveTerminalLaunchTests`; `EveReadinessProbeTests`; `test_the_declared_exclusion_belongs_to_the_route_and_is_owned` | mcp/tests/test_eve_product_integration.py:694-750; mcp/tests/test_eve_product_integration.py:751-861; mcp/tests/test_eve_product_integration.py:862-987; mcp/tests/test_eve_product_integration.py:828-860 |
| The capability catalog's discovery and honesty surfaces, whose effort axis is published at this candidate because its runtime consumer exists. | `EveCapabilityDiscoveryTests`; `EveCapabilityHonestyTests` | mcp/tests/test_eve_product_integration.py:1018-1133; mcp/tests/test_eve_product_integration.py:1134-1289 |
| The two cases that keep the vocabulary honest without making the suite's verdict depend on the machine: the record-vs-vocabulary comparison, and the drift case that reads the live installed declaration when it exists. | `test_the_advertised_effort_vocabulary_is_the_installed_union_not_a_copy`; `EveEffortVocabularyDriftTests`; `_REASONING_UNION_AT_PIN`; `_installed_reasoning_union` | mcp/tests/test_eve_product_integration.py:1192-1221; mcp/tests/test_eve_product_integration.py:1290-1314; mcp/tests/test_eve_product_integration.py:186-205; mcp/tests/test_eve_product_integration.py:206-248 |
| Behaviour 1's sentinel rule, which the provider boundary cannot observe and so is pinned as an authored source shape. | `EveEffortConsumerShapeTests`; `_authored_agent_definition`; `_code_only` | mcp/tests/test_eve_product_integration.py:1315-1361; mcp/tests/test_eve_product_integration.py:256-278; mcp/tests/test_eve_product_integration.py:250-254 |
| The projector surface, including the two-boundary rule and the preserved unknown event. | `EveProjectorTests`; `EveAdapterToProjectionIntegrationTests` | mcp/tests/test_eve_product_integration.py:1366-1536; mcp/tests/test_eve_product_integration.py:1539-1603 |
| The capture, interaction and terminal-lift surfaces. | `EveConversationCaptureTests`; `EveInteractionProjectionTests`; `EveTerminalProjectionTests` | mcp/tests/test_eve_product_integration.py:1703-1813; mcp/tests/test_eve_product_integration.py:1814-1931; mcp/tests/test_eve_product_integration.py:1932-1964 |
| The asset and credential boundary. | `EveAssetAndCredentialBoundaryTests` | mcp/tests/test_eve_product_integration.py:1965-2034 |
| The provenance census and the falsifiable label case over it. | `_PINNED_RUN_CENSUS`; `_RECORDED_PROVENANCE`; `test_every_scripted_frame_carries_an_honest_provenance_label` | mcp/tests/test_eve_product_integration.py:364-390; mcp/tests/test_eve_product_integration.py:391-409; mcp/tests/test_eve_product_integration.py:1481-1496 |
| The real executable the probe actually runs, and the module's honest statement of the environment's limit. | `_stub_interpreter` | mcp/tests/test_eve_product_integration.py:279-294 |
| The module's own lane row, which the fail-closed loader requires. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The authored consumer the source-shape case parses, and the launch input it reads. | `PROVIDER_DEFAULT_EFFORT`; `reasoning`; `EFFORT_ENV` | eve_runtime/agent/agent.ts:25-25; eve_runtime/agent/agent.ts:35-35; mcp/src/agents_remember/serving/eve_runtime_launch.py:87-87 |
| The production projector the projector cases drive. | `map_evidence_frame` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:147-159 |
| The readiness probe the registry cases drive. | `eve_runtime_readiness` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:89-128 |
| The mounted dashboard case consumes the capture produced alongside these cases, decoded through the wire mirror. | `eveConversationItems`; `eveConversationStatus` | dashboard/src/test/fixtures/eveConversationCapture.ts:376-379; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.eve.test.tsx:25-25; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.eve.test.tsx:35-36 |

## Cross-Repo References

The transport double stands in for the pinned third-party eve process, which is a dependency rather
than a sibling Agents Remember repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The transport the double replaces, and the pinned release whose event vocabulary the census records. | `dependencies` | eve_runtime/package.json:14-20; eve_runtime/README.md:10-22 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `EveAssetAndCredentialBoundaryTests` repointed to mcp/tests/test_eve_product_integration.py:1965-2034. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T10:32+02:00 — 260915-CAPS-L17 curator: **substantial body edit — the module gained three
  cases and a route-disposition case, and one honesty case was inverted with the axis it pinned.**
  (1) `EveCapabilityHonestyTests`: `test_the_pinned_runtime_reads_no_effort_value_and_the_catalog_agrees`
  was **replaced** by `test_the_pinned_runtime_consumes_the_effort_axis_and_the_client_would_read_it`
  (1151) — the consumer is now asserted present on the authored TypeScript and the publication read off
  the **serialized** envelope; a new vocabulary case (1192) compares `REASONING_EFFORTS` with the
  module's recorded union constant; `test_no_advertised_control_lacks_a_runtime_consumer` (1222) now
  holds the axis-to-consumer map equal to the published set in **both** directions. (2) Two new classes:
  `EveEffortVocabularyDriftTests` (1290), which reads the **live** installed declaration behind the
  shared install guard so the machine decides only whether drift is observable and never whether the
  suite is green; and `EveEffortConsumerShapeTests` (1315), which pins behaviour 1's sentinel rule in
  the authored source shape because the provider boundary cannot distinguish "omitted" from "forwarded
  and mapped by the SDK". (3) `EveTerminalLaunchTests` gained
  `test_the_declared_exclusion_belongs_to_the_route_and_is_owned` (828), carrying the route
  exclusion's reason and owner as a product artifact. Corrected the Purpose census (was 68 cases over
  thirteen classes; now **72** over thirteen case-bearing classes) and re-anchored **every** reference
  row, all of which had shifted (+119 or more) or gone stale — each new range was read back against the
  candidate's real class and function boundaries. Recorded **D27** as a carried caveat on
  `EveRegistryTests` rather than a repair: the case is environment-sensitive, `AR_EVE_NODE` is the
  confirmed one-variable falsifier (conftest does not scrub it), the defect is the assertion's shape,
  and the repair belongs to whoever next owns that module. **Checker result (post-sync,
  verbatim).** The refusal this entry first recorded was resolved by the leaf's `worktree_sync`:
  the pair is now `leaf-candidate` / `acceptanceEligible:true` on code base `d8ed8c21`, and the
  contract-scoped `memory_quality_check` ran against this worktree. Headline: `ok:false`,
  `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0
  unonboarded). This card's own contribution: one `integrity.onboarding_drift_check.summary`
  finding — `onboarding_drift_drifted`, "Source has local staged changes not represented in
  HEAD", which is the expected shape for documenting a staged, uncommitted candidate rather than
  a claim about the wording. Verification metadata moves to the synced base `d8ed8c21`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit
  and no hash or fingerprint was invented here.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **the launch-dependent reaches now skip by name**
  (defect D19, repaired by this leaf). `require_installed_eve_application` is called from `_start_eve`
  (six callers), `_evidence_frames` and `_projected`, so a checkout without the machine-local
  `eve_runtime/node_modules` install reports `skipped` with the missing path and the exact install
  command instead of failing as a product defect — eight install-dependent cases across this module
  and its sibling were the measured failing set, and the same guard makes the schedule-dependent
  failure set deterministic (its cause, D20's half-staged-destination fail-open in
  `stage_runtime_root`, is **reported and routed, not repaired here**). The body's Conventions and
  Invariants sections now carry the reaches and the "named, never retried, never silently skipped"
  boundary. Verification metadata moves to this leaf's synced base `8997e184`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: created this card for a file added by the eve
  product-integration change set. Records the thirteen classes and the owner each drives, the
  no-monkeypatching discipline and its one declared transport dependency, the transcription status of
  `_PINNED_RUN_CENSUS` (and the module's own statement that the suite does not re-derive it), the five
  ways the provenance-label case is falsifiable, the honest limit of `_stub_interpreter`, and the
  load-bearing lane row. Verification metadata is pinned to the leaf's synced base commit `ff97072c`
  because the candidate is deliberately uncommitted — the governed closeout stamps the real code
  commit, and no hash or fingerprint was invented here.
