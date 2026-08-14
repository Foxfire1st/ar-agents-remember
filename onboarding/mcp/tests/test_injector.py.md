# test_injector.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_injector.py`               |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3 + R5): covers the delivery path's
bound-log acceptance and provenance, diagnostic failure capture, deferred unbound commands, and
isolated reissue behavior through `_Log` and `_Paster` fixtures cit:([`_Log`, `_Paster`], mcp/tests/test_injector.py:15-25; mcp/tests/test_injector.py:28-52).
## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** The current suite binds message acceptance to a matching log entry,
returns provenance from that bound entry, captures diagnostic failures, defers unbound spawn
commands, avoids reissuing successful retroactive commands, and reissues only errored commands
cit:([`test_message_is_acked_from_bound_log_and_returns_provenance`, `test_submitted_message_without_log_entry_fails_with_diagnostic_capture`, `test_failure_capture_may_receive_modal_diagnostic_label`, `test_unbound_spawn_command_is_deferred_not_acked`, `test_successful_retroactive_command_is_not_reissued`, `test_errored_command_reissues_only_that_command`], mcp/tests/test_injector.py:63-74; mcp/tests/test_injector.py:77-88; mcp/tests/test_injector.py:91-101; mcp/tests/test_injector.py:104-119; mcp/tests/test_injector.py:122-143; mcp/tests/test_injector.py:146-168).
### Conventions

`_Log` models the bound event log and `_Paster` supplies deterministic paste and capture outcomes;
the tests keep provenance, deferred commands, and reissue decisions tied to those fixtures
cit:([`_Log`, `_Paster`], mcp/tests/test_injector.py:15-25; mcp/tests/test_injector.py:28-52).
### Invariants And Boundaries

- A submitted message is acknowledged only when the bound log contains its matching entry; an
  unbound command is deferred rather than acknowledged cit:([`test_message_is_acked_from_bound_log_and_returns_provenance`, `test_unbound_spawn_command_is_deferred_not_acked`], mcp/tests/test_injector.py:63-74; mcp/tests/test_injector.py:104-119).
- Successful retroactive evidence is not reissued, while errored evidence reissues only the errored
  command cit:([`test_successful_retroactive_command_is_not_reissued`, `test_errored_command_reissues_only_that_command`], mcp/tests/test_injector.py:122-143; mcp/tests/test_injector.py:146-168).
### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit-test suite for internal control-plane plumbing with no external spec.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The delivery path under test. | `deliver`; `DeliveryRow`; `envelope_text` | mcp/src/agents_remember/serving/injector.py:24-34; mcp/src/agents_remember/serving/injector.py:50-57; mcp/src/agents_remember/serving/injector.py:60-134 |
| The injector obtains a harness adapter for the failure-only handoff: session-command transport failures and absent-log outcomes flow through `_failed_from_capture`, which uses the adapter's blocked-reason diagnostic. | "get_adapter("; "session command transport failed before log binding"; "input absent from the harness session log after bounded recovery"; `_failed_from_capture`; "blocked = adapter.blocked_reason(outcome.capture)"; `blocked_reason` | mcp/src/agents_remember/serving/injector.py:74-74; mcp/src/agents_remember/serving/injector.py:92-92; mcp/src/agents_remember/serving/injector.py:126-126; mcp/src/agents_remember/serving/injector.py:190-210 |
## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Delivery-path-local behavior only. | — | — |

## Update History
- 2026-08-04T16:28:49+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound the failure-only adapter/transport handoff to the packet-specified operative spans, adding the blocked-reason diagnostic use inside `_failed_from_capture`; the two handoffs stay pinned by their unique failure-reason lines inside each call. Verification metadata unchanged.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_injector.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s)
  with no token change whatsoever. Checked by parsing both revisions and comparing the abstract
  syntax trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: rewrote injector tests around bound-log
  message/command evidence and targeted command reissue; removed pane-turn acceptance fixtures.
  Verification metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3 + R5): the
  payload-envelope rendering tests, every `DeliveryOutcome` branch (including the codex-quota-modal
  override and the spinner-corroborated acked case), and an end-to-end injection test against a
  scripted in-memory tmux pane covering both the happy path and a permanently-blocked modal.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
