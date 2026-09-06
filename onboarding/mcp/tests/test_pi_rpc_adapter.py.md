# mcp/tests/test_pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pi RPC framing/model contracts and shared fake transport.

## Code Commentary

### Logic

The fake transport and launch/operation builders support adapter consumers. Three retained protocol cases preserve Unicode line separators under LF framing, accept CRLF, refuse malformed or overlong frames and retain provider-qualified model identity with model-gated thinking options.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Historical adapter launch, setter and reconnect scenarios no longer run in this file. Protocol fixtures are not an installed Pi conformance run or a static fallback model catalog.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Lf only decoder preserves unicode separators and accepts crlf. | `test_lf_only_decoder_preserves_unicode_separators_and_accepts_crlf` | mcp/tests/test_pi_rpc_adapter.py:418-423 |
| Malformed and overlong frames refuse loudly. | `test_malformed_and_overlong_frames_refuse_loudly` | mcp/tests/test_pi_rpc_adapter.py:425-431 |
| Available models preserve provider identity and model gated thinking. | `test_available_models_preserve_provider_identity_and_model_gated_thinking` | mcp/tests/test_pi_rpc_adapter.py:433-469 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: narrowed the launch row to its exact protocol owner and reissued the whole claim for same-reviewer closure.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The row's
  four claims live in `PiRpcConfiguration.set_model` / `set_effort` at
  `pi_rpc_configuration.py` L70-L153 — `_provider_model` identity validation, the selected model's
  `session_settable` effort vocabulary, the `async with self._lock` serialization, and the
  `_commit(state, capabilities)` that runs only after the `get_state` readback agrees — plus the
  `_provider_model` parser itself at L196-L203. The old L27-L131 started in the module imports.
  No claim text changed.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the offline capability-recording
  guard (version-addressed path, exactly-one-recording assertion, dialog/fire-and-forget
  agreement) and removed the stale `0.80.6` fixture reference from Conventions. Metadata
  fields left at their FEUI-L5 verification pins; the rest of this card was re-read against
  the file and remains true. Closeout stamps the code commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: corrected timeout-release assumptions and added fresh-state,
  token, no-native-queue, certificate, and exact-settlement proof.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented exact provider/model mutation,
  vendor-error mapping, model-gated exact/clamped thinking readback, one finite mutation/readback
  budget, queue release, and catalog-coherent no-promotion behavior. Verification metadata remains
  pinned until closeout stamps the L3 code commit.
- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented provider-qualified dynamic
  catalogs, model-gated thinking, token-free discovery, strict startup/discovery cleanup, retry
  reset, safe state-model sanitization, and preserved native launch flags; corrected the governing
  overview backlink while preserving existing verification metadata.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi startup coverage.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for Pi fake adapter,
  protocol, activity, extension UI, disconnect, and reconciliation coverage.
