# mcp/tests/test_eve_product_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_product_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The product-surface evidence for `CAPS-R08@v1` — *eve is selectable and observable through the
existing AR product*. 68 cases over thirteen test classes, each driving a **real owner**: the
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

- **`EveRegistryTests`** (575) — the curated `eve` row is last and the other three rows are unchanged;
  the row is findable by id like every other harness; it is reachable through the existing adapter
  factory; and it is detected through **its probe, never `PATH`**.
- **`EveTerminalLaunchTests`** (632) — eve is not PTY-launchable, so a terminal open refuses **by name**
  and yields no argv, while the path harnesses keep their ordinary detection. The distinction the
  cases pin is that the refusal is a truthful not-launchable, not a missing-install.
- **`EveReadinessProbeTests`** (710) — both halves of the readiness verdict: a missing application root
  is reported by name, a missing node runtime is reported *separately* from a missing application, the
  verdict depends on the application root and not only the interpreter, and each rejection shape —
  absent, non-executable, below the floor — is refused with its own reason.
- **`EveCapabilityDiscoveryTests`** (866) — `GET /api/harnesses/eve/capabilities` discovers eve through
  the existing factory; a runtime that cannot run refuses by name *before* discovery; an unknown
  harness refuses before discovery; the install fingerprint is the **probed interpreter**, not a
  placeholder command; and the envelope the dashboard reads has the contracted shape.
- **`EveCapabilityHonestyTests`** (982) — the advertised model is the one the runtime would really use;
  the pinned runtime reads no effort value and the catalog agrees; the effort setter refuses every
  candidate *including its own launch vocabulary*; no advertised control lacks a runtime consumer; eve
  never borrows another harness's capability evidence; an unknown harness fails loudly instead of
  inheriting a catalog; and eve's telemetry is declared absent rather than borrowed.
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
| `CAPS-R08@v1` is the requirement this module evidences, and the packet's non-conforming example is what it exists to refute. | `CAPS-R08` | requirements/CAPS-R08-v1-eve-capabilities-and-product-integration.md:12-14 |
| The registry, readiness and terminal-launch surfaces. | `EveRegistryTests`; `EveTerminalLaunchTests`; `EveReadinessProbeTests` | mcp/tests/test_eve_product_integration.py:575-629; mcp/tests/test_eve_product_integration.py:632-707; mcp/tests/test_eve_product_integration.py:710-816 |
| The capability catalog's discovery and honesty surfaces, including the retired effort axis. | `EveCapabilityDiscoveryTests`; `EveCapabilityHonestyTests` | mcp/tests/test_eve_product_integration.py:866-979; mcp/tests/test_eve_product_integration.py:982-1103 |
| The projector surface, including the two-boundary rule and the preserved unknown event. | `EveProjectorTests`; `EveAdapterToProjectionIntegrationTests` | mcp/tests/test_eve_product_integration.py:1106-1276; mcp/tests/test_eve_product_integration.py:1279-1338 |
| The capture, interaction and terminal-lift surfaces. | `EveConversationCaptureTests`; `EveInteractionProjectionTests`; `EveTerminalProjectionTests` | mcp/tests/test_eve_product_integration.py:1442-1532; mcp/tests/test_eve_product_integration.py:1553-1667; mcp/tests/test_eve_product_integration.py:1670-1700 |
| The asset and credential boundary. | `EveAssetAndCredentialBoundaryTests` | mcp/tests/test_eve_product_integration.py:1703-1772 |
| The provenance census and the falsifiable label case over it. | `_PINNED_RUN_CENSUS`; `_RECORDED_PROVENANCE`; `test_every_scripted_frame_carries_an_honest_provenance_label` | mcp/tests/test_eve_product_integration.py:248-264; mcp/tests/test_eve_product_integration.py:275-292; mcp/tests/test_eve_product_integration.py:1221-1236 |
| The real executable the probe actually runs, and the module's honest statement of the environment's limit. | `_stub_interpreter` | mcp/tests/test_eve_product_integration.py:163-178 |
| The module's own lane row, which the fail-closed loader requires. | `unit-regression` | mcp/tests/test-evidence-lanes.toml:52-52 |
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

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: created this card for a file added by the eve
  product-integration change set. Records the thirteen classes and the owner each drives, the
  no-monkeypatching discipline and its one declared transport dependency, the transcription status of
  `_PINNED_RUN_CENSUS` (and the module's own statement that the suite does not re-derive it), the five
  ways the provenance-label case is falsifiable, the honest limit of `_stub_interpreter`, and the
  load-bearing lane row. Verification metadata is pinned to the leaf's synced base commit `ff97072c`
  because the candidate is deliberately uncommitted — the governed closeout stamps the real code
  commit, and no hash or fingerprint was invented here.
