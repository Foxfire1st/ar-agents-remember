# dashboard/src/test/fixtures/capabilityEnvelopes.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/capabilityEnvelopes.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-11T15:20+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

Capability-contract fixtures are test-only wire-shaped examples for model capability, session,
result, and route-error behavior. They must not enter production UI constants.

## Code Commentary

### Logic

- cit:([`effortOption`; `modelRow`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:20-32; dashboard/src/test/fixtures/capabilityEnvelopes.ts:34-52): Builders create full-wire-shape rows with overridable defaults
  (supportsEffort derived from the supplied menu) — the same extend-don't-fork posture as
  catalogRows.
- cit:([`CLAUDE_MODEL_ROWS`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:60-84): the recorded five keys; every effort menu is the five-key
  low…max list; cit:([`haiku`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:83-83) advertises NO effort rows — THE fixture the effort-gating tests
  lean on.
- cit:([`CODEX_MODEL_ROWS`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:88-131): eight rows with per-row defaultEffort (sol=low, spark=high),
  ultra only on sol/terra, and codex-auto-review hidden.
- cit:([`PI_MODEL_ROWS`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:135-146): the two keys stay provider-qualified
  VERBATIM with provider: "deepseek" alongside; menu off/high/max.
- cit:([`preSessionSnapshot`; `capabilityEnvelope`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:156-158; dashboard/src/test/fixtures/capabilityEnvelopes.ts:160-172): pre-session = no selection, empty
  configOptions; the fingerprint is a synthetic harness-prefixed fixture token, not a sha256-hex digest.
  cit:([`ENVELOPES_BY_CACHE_STATUS`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:175-179) is the same catalog under hit/miss/refreshed.
- cit:([`CLAUDE_FRESH_SESSION_SNAPSHOT`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:186-207): the fresh-session fixture records a launch model,
  null selectedEffort, and only the model config category.
- cit:([`SET_RESULTS`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:211-247): one per acceptance; queued/unknown/unsupported carry
  effectiveValue: null (evidence words, never a success boolean).
- cit:([`SET_RESULT_CLAMP`; `SET_RESULT_ECHO_NO_VALUE`; `QUEUED_THEN_IMMEDIATE_SEQUENCE`; `codexLiveSessionSnapshot`; `UNKNOWN_THEN_READBACK`; `SESSION_CAPABILITY_ERROR_BODIES`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:253-259; dashboard/src/test/fixtures/capabilityEnvelopes.ts:263-269; dashboard/src/test/fixtures/capabilityEnvelopes.ts:273-288; dashboard/src/test/fixtures/capabilityEnvelopes.ts:291-301; dashboard/src/test/fixtures/capabilityEnvelopes.ts:305-319; dashboard/src/test/fixtures/capabilityEnvelopes.ts:322-332): Later extensions cover clamp and echo-without-value results, queued then immediate,
  `codexLiveSessionSnapshot`, confirming/disproving unknown readbacks, and 404/409/503 exact-session
  bodies.
- cit:([`CAPABILITY_ERROR_BODIES`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:336-358): the fixture stores 404 harness-not-installed,
  409 non-native, and 503 control-unavailable bodies with their HTTP statuses.

### Invariants And Boundaries

- cit:([`SET_RESULTS`; `CAPABILITY_ERROR_BODIES`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:211-247; dashboard/src/test/fixtures/capabilityEnvelopes.ts:336-358): The fixture stores SetResult detail strings and the
  404/409/503 route-error bodies; update these fixture values only against new recorded evidence,
  never by invention.
- cit:([`effortOption`; `modelRow`], dashboard/src/test/fixtures/capabilityEnvelopes.ts:20-32; dashboard/src/test/fixtures/capabilityEnvelopes.ts:34-52): Shared test infrastructure across these waves: extend by adding rows/overrides, not by editing recorded
  shapes in place.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Builders, catalogs, envelopes, snapshots, SetResults, later sequences, and both route-error families. | `effortOption`; `modelRow`; `CLAUDE_MODEL_ROWS`; `CODEX_MODEL_ROWS`; `PI_MODEL_ROWS`; `capabilityEnvelope`; `SET_RESULTS`; `CAPABILITY_ERROR_BODIES` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:20-32; dashboard/src/test/fixtures/capabilityEnvelopes.ts:34-52; dashboard/src/test/fixtures/capabilityEnvelopes.ts:60-84; dashboard/src/test/fixtures/capabilityEnvelopes.ts:88-131; dashboard/src/test/fixtures/capabilityEnvelopes.ts:135-146; dashboard/src/test/fixtures/capabilityEnvelopes.ts:160-172; dashboard/src/test/fixtures/capabilityEnvelopes.ts:211-247; dashboard/src/test/fixtures/capabilityEnvelopes.ts:336-358 |
| The wire mirrors everything is typed against. | `EffortOptionWire`; `ModelCapabilityWire`; `CapabilitySnapshotWire`; `CapabilityEnvelope`; `SetResultWire` | dashboard/src/types/harnessCapabilities.ts:16-22; dashboard/src/types/harnessCapabilities.ts:25-39; dashboard/src/types/harnessCapabilities.ts:59-65; dashboard/src/types/harnessCapabilities.ts:68-75; dashboard/src/types/harnessCapabilities.ts:89-96 |
| The Python serializers the shapes mirror. | "def to_json(self) -> dict[str, object]:"; "def capability_snapshot_json(value: CapabilitySnapshot) -> dict[str, object]:"; "def model_capability_json(value: ModelCapability) -> dict[str, object]:"; "def effort_option_json(value: EffortOption) -> dict[str, object]:"; "def set_result_json(value: SetResult) -> dict[str, object]:" | mcp/src/agents_remember/serving/harness_capability_catalog.py:59-68; mcp/src/agents_remember/serving/harness_capabilities.py:162-168; mcp/src/agents_remember/serving/harness_capabilities.py:171-184; mcp/src/agents_remember/serving/harness_capabilities.py:187-194; mcp/src/agents_remember/serving/harness_capabilities.py:216-225 |

## Update History

- 2026-08-11T15:20+02:00 — Replaced generic serializer-name anchors with their exact Python
  declarations so each mirrored wire shape has unique provenance.
- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: applied the adversarial fixture-truth correction; the fingerprint is documented as a synthetic harness-prefixed token, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T18:05+02:00 — 260731-EFA wave 2 curator: re-derived 1 stale self-citation.
  `CAPABILITY_ERROR_BODIES` is declared at the object's opening line and runs through the three verbatim 404/409/503
  bodies it names are unchanged.
- 2026-07-17T08:33+02:00 — 260715-FEUI extension R9 appended the clamp and defensive echo results,
  queued→immediate sequence, live Codex snapshot helper, unknown confirming/disproving readbacks,
  and exact-session 404/409/503 bodies. Verification metadata remains pinned to the contract base
  until code commit.
- 2026-07-17T06:10+02:00 — Created for 260715-FEUI R3 (capability fixtures): recorded
  Claude/Codex/Pi catalogs (effortless Haiku, hidden codex-auto-review + per-row defaults,
  provider-qualified Pi keys), envelopes in all three cache statuses, the null-selectedEffort
  fresh-Claude snapshot, SET_RESULTS across the five acceptances, and verbatim 404/409/503
  error bodies. Verification metadata pinned to the leaf base until closeout stamps the code
  commit.
