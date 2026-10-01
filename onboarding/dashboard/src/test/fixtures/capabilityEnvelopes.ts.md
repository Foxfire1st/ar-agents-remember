# dashboard/src/test/fixtures/capabilityEnvelopes.ts

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

## Evidence

### Repo-Internal References

- Builders, catalogs, envelopes, snapshots, SetResults, later sequences, and both route-error families. [1]
- The wire mirrors everything is typed against. [2]
- The Python serializers the shapes mirror. [3]
