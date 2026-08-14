# test_hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T17:18:47+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Proves pending adapter interactions become durable gates, responses use the exact interaction id,
disappearance expires the matching open gate, and protocol-owned null-requestId/vendor-correlation
completion projects onto the same accepted row while inbox consumption remains pending. The exact
2.1.207, 0.144.3, and 0.80.7 values are fixture/smoke evidence only; production behavior is based
on consumed structured fields.

## Code Commentary
### Conventions

Gate decisions are taken through the parameter-object form: `decide_gate(gate,
GateVerdict(decision="approve", by="developer", via="dashboard", note=...), now=NOW)` — including
the shared `_decided_gate` helper and the structured multi-question case, where the serialized
answer map rides in `GateVerdict.note`. Inbox fixture rows are minted with
`create_operator_inbox_entry(InboxMessage(...), entry_id=…, now=…,
routing=InboxRouting(address=InboxAddress(...)), poster=InboxPoster(...))` before the
`model_copy(update=...)` that stamps the delivered/adapter evidence each completion case needs.

### Invariants And Boundaries
These tests pin the acceptance-versus-consumption boundary and prevent diagnostic pane state from
becoming an action trigger. Missing, non-text, unmatched, and ambiguous correlation evidence fails
loudly. Completion records adapter metadata without consuming the row, and terminal state is
`idle` / `immediate` without a queued replacement; `settling` / `queued` requires an actual one.
R9 remains limited to optional `adapterDeliveryState` and `adapterDeliveryDetail`; R10 remains
queued and unimplemented.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [hosted_interactions.py](../src/agents_remember/serving/hosted_interactions.py)
- [test_operator_inbox.py](test_operator_inbox.py)

## Cross-Repo References
No meaningful cross-repo references.

## 260718-CHATS-L5I Current Delta

Hosted-interaction tests now cover serialized multi-question answers and failure reopening with adapter-decision evidence, preventing a failed delivery from silently consuming an operator decision.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: records the Purpose-line correction made
  earlier in this task, where the pinned Pi evidence version was changed from `0.80.6` to
  `0.80.7` to match the locked helper — the conversation-library helper's
  `PI_CODING_AGENT_VERSION` constant and its `@earendil-works/pi-coding-agent` package pin are
  both `0.80.7`, and its `protocol.test.ts` asserts that exact string; the version never appears
  in this test file itself, so it is provenance only and the surrounding
  acceptance-versus-consumption claims are untouched. Also records this leaf's source change:
  every `decide_gate` call now passes a `GateVerdict` instead of the four loose
  `decision`/`by`/`via`/`note` keywords, and the three inbox fixtures build their rows through
  `InboxMessage`/`InboxAddress`/`InboxRouting`/`InboxPoster`, so a Conventions section was added
  naming both call shapes. No test case or assertion changed; the rest of the diff is
  `ruff format` reflow of the `mock.patch` and set-comprehension lines.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added Codex completion-correlation projection and
  explicit pending/unconsumed plus no-replacement terminal-state coverage.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added durable interaction and non-consumption regression coverage.
