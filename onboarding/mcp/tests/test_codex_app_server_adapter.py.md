# mcp/tests/test_codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Fake Codex transport, pinned protocol fixture and async event helpers.

## Code Commentary

### Logic

FakeCodexTransport records requests and deep-copies queued results and incoming frames; BlockingTurnStartTransport exposes the before-write and response window. Builders create launch/request identities and prime startup. make_adapter accepts the production settings value, and event helpers wait for specific frames or verify already-settled notifications are inert.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This support-only module contains no retained conformance test methods. The pinned protocol JSON is fixture data, not a production version selector or static fallback catalog.

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
| Fakecodextransport. | `FakeCodexTransport` | mcp/tests/test_codex_app_server_adapter.py:47-110 |
| Blockingturnstarttransport. | `BlockingTurnStartTransport` | mcp/tests/test_codex_app_server_adapter.py:113-139 |
| Fixture. | `fixture` | mcp/tests/test_codex_app_server_adapter.py:142-143 |
| Fixture object. | `fixture_object` | mcp/tests/test_codex_app_server_adapter.py:146-152 |
| Fixture list. | `fixture_list` | mcp/tests/test_codex_app_server_adapter.py:155-161 |
| Add model. | `add_model` | mcp/tests/test_codex_app_server_adapter.py:164-184 |
| Identity. | `identity` | mcp/tests/test_codex_app_server_adapter.py:187-192 |
| Launch. | `launch` | mcp/tests/test_codex_app_server_adapter.py:195-202 |
| Request. | `request` | mcp/tests/test_codex_app_server_adapter.py:205-217 |
| Prime start. | `prime_start` | mcp/tests/test_codex_app_server_adapter.py:220-230 |
| Make adapter. | `make_adapter` | mcp/tests/test_codex_app_server_adapter.py:247-255 |
| Settle. | `settle` | mcp/tests/test_codex_app_server_adapter.py:258-260 |
| Drain events. | `drain_events` | mcp/tests/test_codex_app_server_adapter.py:263-270 |
| Assert notification is inert. | `assert_notification_is_inert` | mcp/tests/test_codex_app_server_adapter.py:273-282 |
| Next event of kind. | `next_event_of_kind` | mcp/tests/test_codex_app_server_adapter.py:285-290 |
| Turn start result. | `turn_start_result` | mcp/tests/test_codex_app_server_adapter.py:293-298 |
| Turn completed notification. | `turn_completed_notification` | mcp/tests/test_codex_app_server_adapter.py:301-304 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T21:13:21+02:00 — W2-B07 curator: repaired 16 repository-reference citations and normalized 2 prose citations after bounded source reads; all 16 surviving rows use exact anchors and generated ranges. Under the 2026-08-02 14:10 R27 ruling, deleted 1 legacy reviewer-verdict row because it is true legacy review evidence rather than a semantic Tier-3 source-code claim, and no resolver-supported code/memory mirror exists.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The turn-start
  override material is now split across two methods in `codex_app_server_adapter.py`: `_start_turn`
  plus `_turn_start_params` at L528-L593 (which carries `evidence.model.model` / `evidence.effort` and
  rejects a `failed`/`interrupted` start status), and `_accept_started_turn` at L657-L701 (which calls
  `self._session.accept_settings_selection(...)` — the promotion). Was the single range L519-L615.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the suite's own fixture surface changed, so
  the Conventions section was rewritten rather than attested. `make_adapter` no longer takes the
  seven keywords it used to assemble into a settings object; it takes one
  `CodexAppServerSettings` defaulting to the new module-level `TEST_SETTINGS`, and the resume,
  submission-limit, and approval/sandbox/config cases vary a single field with
  `dataclasses.replace(TEST_SETTINGS, ...)`. Three extracted helpers — `drain_events`,
  `assert_notification_is_inert`, and `next_event_of_kind` — replace the inline queue-draining
  and `while True` event loops the correlation cases repeated, and are now named alongside a
  reference row at L225-L284. That 31-line block plus the `AdapterEvent` import shifted every
  test below it, so all eight own-file reference ranges were re-verified against the current
  definitions and re-anchored (for example the experimental-request row from L1078-L1118 to
  L1091-L1129 and the discovery row from L294-L357 to L388-L454), and the fixture-path row was
  re-pointed from the long-stale L27-L29 to the current `FIXTURE_PATH` at L34 plus the
  schema-pinning test at L1251-L1259. The Logic paragraph's experimental-case name was also
  corrected to the source's actual
  `test_unknown_server_request_is_declined_while_experimental_history_stays_enabled`. No test
  was added, removed, or renamed, and every decline/degrade, promotion, and validation claim
  still holds.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: corrected the adapter-suite capability
  record to experimental history opt-in without overclaiming method or server-request support.
  Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the deliberately changed
  experimental-request failure contract — the decline is unchanged (`respond_error` -32601, no
  experimental API), but an unknown/experimental request METHOD now degrades to preserved evidence
with the bridge `ready` instead of marking it `failed` — and added the matching invariant plus a
reference row. Re-anchored the four adapter-source citations the remediation
  shifted (L88-L126 → L137-L190; L153-L208 → L226-L313; L220-L272 → L314-L355; L344-L415 →
  L519-L615). Verification metadata stays pinned at the file's last committed touch; the adapter
  change itself is uncommitted.
- 2026-07-17T21:39+02:00 — FEUI-L5: replaced busy-queue/steer expectations with fresh-turn,
  exact-ref, early-completion, cleanup, id-reuse, and bounded-correlation proofs.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented queued desired-versus-effective
  state, same-thread turn overrides, prompt selection epochs, successful-status-only promotion,
  reversal collapse, model-local validation, and deliberate-notification drift guarding.
  Verification metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added the configured and roleless Codex
  `thread/start` launch contract, including model-local default effort and resume preservation.
  Verification metadata remains pinned until closeout stamps the L2 code commit.

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented cached current-session
  advertisement, paginated hidden-model discovery, model-gated effort metadata, thread/turn-free
  enumeration, and repeated-cursor cleanup; corrected the governing overview backlink while
  preserving existing verification metadata.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented null-requestId correlation, same-row
  completion projection, loud failure cases, and no-replacement terminal state assertions.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented negotiated-version acceptance and loud rejection
  coverage.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for fake-protocol
  conformance, R11 strictness, server requests, busy policy, terminal mapping, and no-resend
  reconnect coverage. Verification remains unset until closeout stamps the code commit.
