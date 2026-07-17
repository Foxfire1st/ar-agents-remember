# dashboard/src/test/fixtures/capabilityEnvelopes.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/capabilityEnvelopes.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**Capability-contract fixtures** (260715-FEUI-L3 R3), typed against the wire mirrors and shaped
by the RECORDED L5 evidence: Claude's five rows with an effortless Haiku, Codex's eight rows with
a hidden entry and per-row default efforts, Pi's two provider-qualified rows — plus envelopes in
all three cache statuses, the fresh-Claude exact-session snapshot, SetResults in every
acceptance, and the verbatim 404/409/503 route-error bodies. FIXTURES ONLY: these keys/menus are
evidence examples for tests — they must never enter production UI constants (dynamic-only
invariant, byte-checked by the L3 review against the L5 conformance reports).

## Code Commentary

### Logic

- Builders `effortOption`/`modelRow` (L20-L52): full-wire-shape rows with overridable defaults
  (`supportsEffort` derived from the supplied menu) — the same extend-don't-fork posture as
  `catalogRows.ts`.
- `CLAUDE_MODEL_ROWS` (L60-L84): the recorded five keys; every effort menu is the five-key
  `low…max` list; `haiku` (L83) advertises NO effort rows — THE fixture the effort-gating tests
  lean on.
- `CODEX_MODEL_ROWS` (L88-L131): eight rows with per-row `defaultEffort` (sol=low, spark=high),
  `ultra` only on sol/terra, and `codex-auto-review` hidden.
- `PI_MODEL_ROWS` (L135-L146): `deepseek/deepseek-v4-flash|pro` — keys stay provider-qualified
  VERBATIM with `provider: "deepseek"` alongside; menu off/high/max.
- `preSessionSnapshot`/`capabilityEnvelope` (L156-L172): pre-session = no selection, empty
  `configOptions`; the fingerprint mimics the recorded sha256-hex SHAPE.
  `ENVELOPES_BY_CACHE_STATUS` (L175-L179) is the same catalog under hit/miss/refreshed.
- `CLAUDE_FRESH_SESSION_SNAPSHOT` (L186-L207): launch model echoed via `system/init` but
  `selectedEffort` NULL — stream-json emits no launch-effort echo (L5) — and only the `model`
  config category.
- `SET_RESULTS` (L211-L247): one per acceptance; `queued`/`unknown`/`unsupported` carry
  `effectiveValue: null` (evidence words, never a success boolean).
- `CAPABILITY_ERROR_BODIES` (L251-L273): 404 `harness not installed: 'codex'`, 409 non-native,
  503 control-unavailable — verbatim server wording with the HTTP status alongside.

### Invariants And Boundaries

- Values mirror recorded evidence: bridge/route-error strings are the server's EXACT wording;
  SetResult detail strings are representative paraphrases of L5-observed behavior, marked as
  fixtures (worker decision 11). Update only against new recorded evidence, never by invention.
- Shared test infrastructure for L3–L6: extend by adding rows/overrides, not by editing recorded
  shapes in place.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Builders, harness rows, envelopes, snapshot, SetResults, error bodies. | L20-L273 | [capabilityEnvelopes.ts](capabilityEnvelopes.ts) |
| The wire mirrors everything is typed against. | L11-L117 | [../../types/harnessCapabilities.ts](../../types/harnessCapabilities.ts) |
| The Python serializers the shapes mirror. | L59-L64, L162-L227 | [harness_capability_catalog.py](../../../../mcp/src/agents_remember/serving/harness_capability_catalog.py), [harness_capabilities.py](../../../../mcp/src/agents_remember/serving/harness_capabilities.py) |
| The conformance suite pinning the pack to the recorded L5 samples. | L31-L161 | [../contractCapabilities.test.ts](../contractCapabilities.test.ts) |
| Store-suite consumer (adopt/refuse/error paths). | — | [../../data/capabilityCatalog.test.ts](../../data/capabilityCatalog.test.ts) |
| Flow-suite consumer (dynamic-only render, re-gating, vendor defaults). | — | [../../panels/session-cockpit/LaunchFlow.test.tsx](../../panels/session-cockpit/LaunchFlow.test.tsx) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3 (capability fixtures): recorded-L5
  Claude/Codex/Pi catalogs (effortless Haiku, hidden codex-auto-review + per-row defaults,
  provider-qualified Pi keys), envelopes in all three cache statuses, the null-selectedEffort
  fresh-Claude snapshot, SET_RESULTS across the five acceptances, and verbatim 404/409/503
  error bodies. Verification metadata pinned to the leaf base until closeout stamps the L3 code
  commit.
