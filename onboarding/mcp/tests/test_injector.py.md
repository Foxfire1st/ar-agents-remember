# test_injector.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_injector.py`               |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00                     |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3 + R5): covers the ONE delivery path
(`serving/injector.py::deliver`) — the standardized payload envelope, every branch of the four-way
`DeliveryOutcome` contract, and an end-to-end injection test against a scripted in-memory tmux pane
(R5's explicit ask).

## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** Scripted harness logs prove id-envelope message acceptance and returned
binding provenance; absence fails with diagnostic capture even when the pane moves. Separate tests
pin deferred pre-bind commands, successful retroactive verification without reissue, isolated
reissue after errored evidence, draft behavior, and failure-only modal labeling.

Four test classes:

- `EnvelopeTests` — `envelope_text` renders the header + ack line when `envelope=True`, ships the
  body verbatim when `envelope=False`, and omits the `ack:` line when no `ack_instruction` is given.
- `DeliveryOutcomeMappingTests` — drives `deliver` against a `_StubPaster` returning a canned
  `PasteResult`, one test per outcome branch: delivered+submitted → `acked`; `submit=False` →
  `landed-unacked`; submitted-but-no-advance-and-no-spinner → `landed-unacked`; submitted-with-a-
  spinner-in-the-capture-but-no-advance → `acked` (the harness-aware corroboration); never
  capture-verified → `failed`; a codex quota-modal capture (even with `delivered=True`) → `blocked`
  with reason `"codex-quota-limit"`; a permission-prompt capture → `blocked` with reason
  `"permission-prompt"` (pinning the two are DISTINCT reasons); `test_envelope_text_is_what_gets_
  pasted` pins that the rendered envelope (not the bare body) is what actually reaches
  `paster.paste`.
- `_ScriptedPane` / `_Clock` / `_scripted_paster` — a minimal in-memory codex-shaped pane (mirroring
  `test_terminal_paste.py`'s `_FakePane` conventions: injected buffers/keys/capture, no real tmux, no
  real sleeping) driving a REAL `TerminalPaster`.
- `ScriptedTmuxE2ETests` — `test_brief_lands_and_the_turn_starts`: a full paste+submit sequence
  against the scripted pane resolves `acked`. `test_quota_modal_already_on_the_pane_blocks_delivery`:
  a pane whose paste is permanently swallowed (a modal that never clears) and whose initial content
  already shows the quota text resolves `blocked` with reason `"codex-quota-limit"` — not a bare
  `failed` — even though the paste itself never capture-verified as landed.

### Conventions

`_StubPaster` intentionally does NOT drive `TerminalPaster`'s internal loop — it is a pure
outcome-mapping fixture (fast, exact control per branch). The scripted-pane class is a SEPARATE,
narrower fixture than `test_terminal_paste.py`'s `_FakePane` family (this file does not import it —
tests should not cross-import another test module's private fixtures); it exists only to prove the
full stack (`TerminalPaster` + `harness_adapters` + `injector.deliver`) composes correctly
end-to-end, not to re-cover `TerminalPaster`'s own capture-verify semantics (that suite already
does).

### Invariants And Boundaries

- Every `deliver(...)` call against a fake/stub paster carries a `# type: ignore[arg-type]` comment
  (the fakes are structurally compatible but not nominally `TerminalPaster` — the same convention
  `test_operator_inbox.py` already uses for its paster fakes).
- The blocked-modal e2e test proves the R2 requirement directly: a modal trap is `blocked(reason)`,
  never silent non-delivery, even under the worst case (the paste literally never lands).

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit-test suite for internal control-plane plumbing with no external spec.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines the delivery-outcome contract; the leaf task doc (R1, R3, R5) is the source of truth this suite pins. | whole module | [test_injector.py](test_injector.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The delivery path under test. | `deliver`; `DeliveryRow`; `envelope_text` | [../src/agents_remember/serving/injector.py](../src/agents_remember/serving/injector.py) |
| The harness adapter `deliver` reads for the blocked-check and turn-started corroboration. | `get_adapter` | [../src/agents_remember/serving/harness_adapters.py](../src/agents_remember/serving/harness_adapters.py) |
| `TerminalPaster` is the real transport the scripted-pane e2e tests drive; its own fixture conventions (`_FakePane`, injected clock/sleep) are the pattern this file's narrower `_ScriptedPane` mirrors without importing. | `TerminalPaster` | [../src/agents_remember/serving/terminal_paste.py](../src/agents_remember/serving/terminal_paste.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Delivery-path-local behavior only. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: rewrote injector tests around bound-log
  message/command evidence and targeted command reissue; removed pane-turn acceptance fixtures.
  Verification metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3 + R5): the
  payload-envelope rendering tests, every `DeliveryOutcome` branch (including the codex-quota-modal
  override and the spinner-corroborated acked case), and an end-to-end injection test against a
  scripted in-memory tmux pane covering both the happy path and a permanently-blocked modal.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
