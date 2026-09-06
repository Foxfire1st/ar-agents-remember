# mcp/tests/test_codex_native_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_native_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash |  `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate |  2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Bounded native-history paging and typed refusal propagation.

## Code Commentary

### Logic

Opaque continuation consumes each source page once with one-item bounded requests. A two-cursor cycle terminates before re-requesting a page. A recognized bounded-RPC failure does not silently fall back; oversized materialized responses and both IPC clients retain the typed limit outcome.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Materialization ceilings are distinct from transport fuses. The remaining cases do not separately establish expired-cursor or legacy fallback behavior.

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
| Bounded items are probed and opaque cursor consumes each source page once. | `test_bounded_items_are_probed_and_opaque_cursor_consumes_each_source_page_once` | mcp/tests/test_codex_native_history.py:105-136 |
| Two cursor cycle terminates typed without re requesting a source page. | `test_two_cursor_cycle_terminates_typed_without_re_requesting_a_source_page` | mcp/tests/test_codex_native_history.py:140-173 |
| Recognized bounded rpc failure never silently falls back. | `test_recognized_bounded_rpc_failure_never_silently_falls_back` | mcp/tests/test_codex_native_history.py:177-192 |
| Source response over post transport materialization ceiling is typed. | `test_source_response_over_post_transport_materialization_ceiling_is_typed` | mcp/tests/test_codex_native_history.py:196-211 |
| Native history limit outcome survives both control ipc clients. | `test_native_history_limit_outcome_survives_both_control_ipc_clients` | mcp/tests/test_codex_native_history.py:214-231 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated the unavailable and bounded-materialization exception definitions. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the native-history errors.py citations (390-397/398-410 to 423-428/431-443) shifted by the CCR-R08 +33-line errors.py insertion. Citation-only re-anchor; no content impact.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:13:21+02:00 — W2-B07 curator: repaired 2 repository-reference citations and normalized 1 historical prose citation after bounded source reads; the scoped citation check is clean.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation whose end ran
  14 lines past `serving/codex_app_server_history.py`, which is 681 lines. Narrowed it to L41-L681
  and read both ends: L41 is still the `SourceContract` literal that opens the contract vocabulary
  and L681 is the last line of `_decode_bounded_cursor`'s walk-id validation, so the range covers
  the whole reader — constants, `_BoundedWalk`/`_OutputWindow`/`BoundedPageRequest`,
  `CodexNativeHistoryReader`, and the cursor codec.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  native-history unit/resource suite. Verification metadata remains blank because the new test is
  uncommitted.
