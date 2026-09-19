# mcp/tests/test_eve_effort_runtime.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-17T10:43+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| path | `mcp/tests/test_eve_effort_runtime.py` |
| doc_type | `file-level-onboarding` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The effort axis, **executed**: the shipped application's own consumer, read at the provider boundary.
`CAPS-R17@v1` behaviour 1 asserts that `eve_runtime/agent/agent.ts` reads `AR_EVE_EFFORT` and applies it
through eve's own `defineAgent({ reasoning })`, so that a settings-selected level arrives at the
provider the runtime actually calls.

No Python case can observe that: the consumer is TypeScript inside the pinned application, and the
field under test is the request body a direct provider receives. So these three cases start the **real
runtime** with a complete verified capsule binding and read the body verbatim. The claim being
falsified is narrow and load-bearing, and this module exists so that the catalogue's advertisement
rests on a measurement rather than on documentation.

**Integration-marked** (`pytestmark = pytest.mark.integration`, 65), so the default unit selection
deselects it; its lane row is `integration` (`mcp/tests/test-evidence-lanes.toml:148`, with this
module's path at `:173`).

## Code Commentary

### Logic

Three cases, all in `EveEffortConsumerTests` (175), each starting its own application root and process:

| Case | What it proves |
| --- | --- |
| `test_every_advertised_level_is_the_body_the_provider_receives` (178) | **the whole accepted vocabulary, not an example**: for every `REASONING_EFFORTS` member except the sentinel, the recorded body must carry exactly that level. A level the menu advertises but the runtime cannot apply fails here. |
| `test_the_sentinel_sends_no_reasoning_key_at_all` (194) | `provider-default` means **no explicit reasoning**, so the key must be **absent** from the body — not present with the token, and not present as `null`. Asks `"reasoning_effort" not in request.body` directly, because the support module's `reasoning_effort` property collapses absent and null to `None`. |
| `test_the_model_the_selection_names_is_the_one_the_provider_receives` (206) | the **control** for the case above: the *same* runtime and the same body, so a case that passed on an empty or defaulted request rather than on the effort key would fail here. |

`_one_level` (the helper the three cases share) starts **one** configured level and returns what the
provider saw. Two properties make the measurement trustworthy rather than self-confirming, and both are
stated in the module docstring:

- the application root each case starts is the **checkout's own** `eve_runtime/agent` tree, linked into
  a scratch root by `staged_runtime_root` because `node_modules` is machine-local — and the staged copy
  is compared **byte for byte** against that tree before the assertion is read, plus the authored
  `agent.ts` is asserted to contain `AR_EVE_EFFORT`, so the case cannot pass against a reduced
  application written for it;
- **one application root and one process per case.** The authored definition is read when the runtime
  boots, so a shared root would measure the previous case's source — a failure mode observed while
  building this measurement and invisible in a summary table.

`_admitted_workspace` (80) builds a real git worktree on an admitted branch with a carrier through the
capsule seam's own fixture support: the runtime refuses every session route without a complete verified
binding, so this is what makes the cases observe the **production** consumer rather than a stub. Only
the transport's peer is a recording server.

`_node_executable` (166) skips by name when this host has no Node at or above the floor;
`require_installed_eve_application` (called first in `_one_level`) skips by name when the machine-local
`eve_runtime/node_modules` install is absent. Both are named skips, never retries.

### Conventions

- The provider is the support module's **recording HTTP server**, deliberately **not** the product's
  deterministic fixture model: the fixture traces a normalized projection of the request, and a
  projection is exactly what must not be trusted when the request body is the value under test.
- The module asserts its own premises before reading a verdict — the staged copy equals the authored
  tree, and the authored source contains the consumer — so a green case cannot come from measuring the
  wrong bytes.
- `START_TIMEOUT_SECONDS` (240) and `CALL_TIMEOUT_SECONDS` (120) are generous because a real hermetic
  Node application boots and compiles per case; the poll loop has a deadline rather than a fixed sleep.

### Invariants And Boundaries

- **One level, one root, one process.** Sharing an application root across levels would measure the
  source the first boot compiled, so a case that reuses a root is measuring the wrong thing even when
  it is green.
- **The staged bytes must be the repository's own.** The byte comparison against the authored tree is
  what keeps the measurement about this repository's shipped application; a copy or a reduction would
  make the claim vacuous.
- **The absence of the key is asserted on the body, not on the convenience property.** For the sentinel
  the distinction between "not sent" and "sent as `null`" is the rule being pinned.
- **This module proves the launch *preparation* and the runtime's own request, not the whole dispatch
  chain.** It resolves a spec through `resolve_runtime_spec` with a real binding and starts
  `EveRuntimeProcess` directly; the runner **process** hop (tmux → runner → adapter) is exercised by the
  settings-chain evidence, not here. Read the two together before claiming an end-to-end seat launch.
- The cases need a machine-local install and a Node at or above the floor; without them they **skip by
  name**, so a green run on a bare checkout is not coverage of this consumer.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the external authority the consumer is written against is eve's own published `defineAgent`/reasoning typing, reached through the pinned package rather than a specification in this repository. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The vocabulary the cases iterate and the sentinel they single out — the adapter's one declaration, which the launch gate validates against and the catalogue publishes. | `REASONING_EFFORTS`; `PROVIDER_DEFAULT_EFFORT` | mcp/src/agents_remember/serving/eve_adapter.py:100-110; mcp/src/agents_remember/serving/eve_adapter.py:91-91 |
| The real runtime process the cases start, and the launch environment the selected level is carried into. | `EveRuntimeProcess`; `resolve_runtime_spec`; `EveLaunchSelection`; `EveWorkspaceBinding` | mcp/src/agents_remember/serving/eve_runtime_client.py:133-372; mcp/src/agents_remember/serving/eve_runtime_launch.py:312-347; mcp/src/agents_remember/serving/eve_runtime_launch.py:90-372 |
| The recording provider boundary and the staged application root, which are what make the body the evidence. | `RecordedModelRequest`; `serve_recording_provider`; `staged_runtime_root`; `EVE_APPLICATION_ROOT`; `require_installed_eve_application` | mcp/tests/eve_adapter_test_support.py:440-465; mcp/tests/eve_adapter_test_support.py:467-574; mcp/tests/eve_adapter_test_support.py:580-599; mcp/tests/eve_adapter_test_support.py:37-37; mcp/tests/eve_adapter_test_support.py:42-61 |
| The complete verified capsule binding the runtime refuses to start without, built through the capsule seam's own fixture support. | `FixtureCarrierRequest`; `fixture_carrier_for`; `binding_env`; `repository_with_commit` | mcp/tests/eve_capsule_test_support.py:559-572; mcp/tests/eve_capsule_test_support.py:573-628; mcp/tests/eve_capsule_test_support.py:630-641; mcp/tests/eve_capsule_test_support.py:155-171 |
| The consumer under measurement: the authored application reads the effort input and applies it through eve's own definition, omitting the property for the sentinel. | `PROVIDER_DEFAULT_EFFORT`; `reasoning` | eve_runtime/agent/agent.ts:25-25; eve_runtime/agent/agent.ts:35-35 |
| The catalogue whose advertisement rests on this measurement, and the case that reads the axis off the serialized envelope. | `_capability_snapshot`; `test_the_pinned_runtime_consumes_the_effort_axis_and_the_client_would_read_it` | mcp/src/agents_remember/serving/eve_adapter.py:699-748; mcp/tests/test_eve_product_integration.py:1151-1191 |
| The sentinel rule in its other form, which the provider boundary cannot observe and so is pinned as an authored source shape. | `EveEffortConsumerShapeTests` | mcp/tests/test_eve_product_integration.py:1315-1361 |
| The module's own lane row, which the fail-closed loader requires. | `integration`; `mcp/tests/test_eve_effort_runtime.py` | mcp/tests/test-evidence-lanes.toml:205-205 |

## Cross-Repo References

The controlled application is the pinned published `eve` package started as a real Node process; it is
a dependency rather than a sibling Agents Remember repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned runtime the cases start, the exact dependency pins, and the machine-local install command that the README documents and the guard enforces. | `EveEffortConsumerTests`; `_one_level` | eve_runtime/package.json:15-20; eve_runtime/README.md:25-25; mcp/tests/test_eve_effort_runtime.py:175-215; mcp/tests/test_eve_effort_runtime.py:108-163 |

## Update History
- 2026-09-18T19:54:18+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The lane row's `integration` cell walked the module's neighbours and the previous lane's closing `]` at `196` but stopped short of the lane key itself at `201`; that range was widened to `196-201`. Claim, anchors and the other nine ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T10:32+02:00 — 260915-CAPS-L17 curator: created this card for the module this leaf adds. It
  is the leaf's **executed** half of `CAPS-R17@v1` behaviour 1: no Python case can observe a TypeScript
  consumer inside the pinned application, so the three cases start the real runtime per level and read
  the request body a recording provider received. Records the two properties that keep the measurement
  from being self-confirming — the staged copy is compared byte for byte against the checkout's own
  authored tree, and each case gets **one application root and one process** because the definition is
  read at boot — and the module's stated reason for a recording server rather than the product's
  fixture model, whose traced projection is exactly what must not be trusted when the body is the value
  under test. States the boundary plainly: this proves the launch preparation and the runtime's own
  request, **not** the whole dispatch chain (the runner process hop is the settings-chain evidence's),
  and the cases skip by name without the machine-local install or a Node at the floor, so a green run
  on a bare checkout is not coverage. Lane row `integration`. **Checker result (post-sync,
  verbatim).** The refusal this entry first recorded was resolved by the leaf's `worktree_sync`:
  the pair is now `leaf-candidate` / `acceptanceEligible:true` on code base `d8ed8c21`, and the
  contract-scoped `memory_quality_check` ran against this worktree. Headline: `ok:false`,
  `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0
  unonboarded). This card's own contribution: one `claim_reopen` error at `:116`:
  `RecordedModelRequest` "did not exist at code commit `0346da9c…` and resolves in the working
  tree". This is the **D11 uncommitted-candidate signature** the brief predicted for cards this
  leaf writes — the checker resolves citations against the code base commit and the anchor is a
  construct this leaf adds. Per the master's rule it is **recorded, not "fixed"**: no stamp is
  advanced onto an uncommitted tree and the claim is not deleted; the closing evidence is the
  post-closeout state of the same range. The card is also the census's only `preExisting: false`
  row, which is the expected shape for a module this leaf adds. Verification metadata moves to
  the synced base `d8ed8c21`; the candidate is deliberately uncommitted, so the governed
  closeout stamps the real code commit and no hash or fingerprint was invented here.
