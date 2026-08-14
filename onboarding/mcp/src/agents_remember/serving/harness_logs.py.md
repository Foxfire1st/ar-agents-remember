# harness_logs.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/harness_logs.py`       |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T13:03+02:00                                  |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving overview](overview.md)

## Purpose

`harness_logs.py` supplies deterministic dispatch-acceptance evidence from harness-owned session
JSONL. It discovers recent Claude/Codex logs for one spawn cwd, binds the session on an existing
unique delivery id in a real user-message record, and reuses that exact path for later message and
Claude local-command checks.

## Code Commentary

### Logic

`HarnessSessionLog` normalizes cwd/time/roots and optionally accepts a catalog-restored bound path.
Before binding it searches only recent candidates: Claude's cwd-keyed project directory or Codex's
spawn-day/adjacent/today date partitions plus legacy root files, filtered by mtime and newest first.
`message_present` requires both cwd identity and the unique id inside a real user-message shape;
Claude meta/command records are excluded, while Codex supports both `response_item` input-text and
`event_msg.user_message` records. `command_evidence` is intentionally Claude-only and requires the
matching command name/args followed within a small record window by non-error local-command stdout.
The parser ignores only an unterminated final append that may be concurrently written; malformed
completed/interior JSONL fails closed.

### Conventions

Harness record shapes are parsed by declared keys/event types rather than terminal rendering or
serialized substring heuristics. Candidate discovery is bounded before the 100 ms acceptance poll.

### Invariants And Boundaries

- Cwd must match before any message or command evidence is credited.
- A command record is not success without non-error stdout.
- Command records cannot self-accept an id-bearing message.
- A bound path is durable catalog provenance; later checks do not rediscover another session.
- Screen text, turn state, composer contents, and knob labels are outside this module.

### Todos

- Reviewer N1: Claude project-key sanitization currently replaces `/` only; cwd names containing
  `.` or `_` need a real-key-derived mapping before production starts spawning from such paths.
- Reviewer N2: Codex session commands have no command-evidence parser. Current settings use argv for
  Codex effort and configure no Codex session commands; a future surface must add real-record
  evidence or refuse that shape.

## Docs References

The resolved source registry has no Domain Documentation entries, and this repository-local parser
is defined by the real harness records and regression fixtures inspected for L15.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external/domain source defines this local record parser. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parser binds recent cwd-matching logs and distinguishes user messages from Claude command evidence. | `HarnessSessionLog` | mcp/src/agents_remember/serving/harness_logs.py:39-120 |
| The injector supplies the unique message id or command text and chooses calibrated acceptance windows. | `deliver` | mcp/src/agents_remember/serving/injector.py:60-134 |
| Real-shape fixtures cover Claude message/command success and error, Codex cwd binding, and partial final appends. | `test_claude_log_binding_and_command_evidence` | mcp/tests/test_harness_logs.py:15-64 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Session JSONL is local harness-owned state read by this repository's serving process. | — | — |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260731-EFA-L2 Current Delta

The per-harness "is this record developer-typed input?" test is now one named reader per harness:

- `_claude_user_text(record)` — the developer-typed text of one Claude `user` record, or `None`.
  Meta records and the `<command-name>` / `<local-command-*>` wrappers are harness bookkeeping
  rather than submitted input; a delivery id found inside one of those would not prove acceptance.
- `_codex_user_text(record)` — the developer-typed text of one Codex rollout record, or `None`.
  Codex writes the same submission twice under different envelopes (a `response_item` message and an
  `event_msg` `user_message`) and **both** are accepted here.

The acceptance-evidence semantics are unchanged; what changed is that each harness's exclusion rule
is stated once, where it is decided.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 4 citation findings (3/3 anchored and sourced; the no-source documentation row was normalized; scoped citation check clean).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `_claude_user_text` / `_codex_user_text` readers and the exclusion rules they carry.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T13:03+02:00 — Created for 260707-HFX2-L15 FIX-H-prime: bounded recent-log discovery,
  cwd verification, unique-id message binding, Claude command+stdout evidence, real Codex/Claude
  record shapes, and fail-closed malformed-record handling. Verification metadata is blank until
  closeout stamps the eventual L15 code commit.
