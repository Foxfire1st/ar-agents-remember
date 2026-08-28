# mcp/tests/test_harness_control_evidence_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_evidence_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Installed-runtime production-seam capture for the 260718-CHATS-L0E evidence family and codex
resume channel. Opt-in (`AR_RUN_EVIDENCE_INSTALLED=1`) and version-locked to the fixtures in
`mcp/tests/fixtures/conversation_runtime/`: a real installed harness drives the real adapter →
control bridge → IPC server → blocking client path, and the redacted observations land in the
fixtures' `substrate-evidence/*` rows. Skips carry exact reasons on machines without the pinned
runtimes, so CI never spends real LLM turns.

## Code Commentary

### Logic

`CodexInstalledEvidenceTests` (locked 0.144.5) drives one ephemeral thread through the production
seam and asserts evidence frames cross with `bridgeEpoch` while `snapshot.raw` stays free of
`arEvidence`; asserts the ephemeral `thread/read` `includeTurns` refusal crosses typed with the
native reason; then opens a persisted thread, pages it through the native read with typed identity,
builds a second adapter through the factory resume channel, and proves `thread/resume` reopens the
exact persisted thread whose items page identically; a live cockpit submission's source crosses
the provenance batch with exact epoch scoping. Its one test method delegates to two named helpers:
`_assert_evidence_family(page)` owns the whole-family assertion (the `codex-notification` kind, the
typed id-carrying `userMessage`/`agentMessage` items, token usage, turn completion), and
`_assert_resume_channel_reaches_the_persisted_thread(root)` owns the persisted-thread paging and
factory-resume half. `PiInstalledEvidenceTests` (locked 0.80.7) drives
one prompt and asserts live evidence frames, the `get_entries` native page with typed identity, the
provenance batch, and the no-leak guarantee. `ClaudeInstalledHonestyTests` keeps the Claude row
honestly `not-exercised` while the installed version (2.1.214) mismatches the locked 2.1.211 gate,
with the exact reason asserted.

### Conventions

Every captured observation is redacted to the fixture allow-list: counts, kinds, field presence,
and shape descriptors only — never content, paths, native text, or credentials. Version probes use
`--version` subprocesses; live turns use a one-word prompt. The two live classes also carry the
registered `@pytest.mark.ar_run_evidence_installed` marker so the pair can be selected or deselected
by name; `ClaudeInstalledHonestyTests` is unmarked. Cockpit submissions pass one
`ControlSubmission(source=..., request_id=..., expected_bridge_epoch=...)` parameter object.
The `_version_of` probe skips a missing executable. Once the opt-in selects an installed command,
process-start and subprocess failures remain real test failures; they cannot be recast as absent
evidence.

### Invariants And Boundaries

- The opt-in environment variable is the sole activation; without it every live class skips with
  an exact reason.
- Fixture rows record `observed` only for seams actually exercised through production code;
  `enablesCapabilities` stays `false` and version-mismatched harnesses stay `not-exercised`.
- No fixture-shaped canned response can substitute for a live seam: the bridge epoch must be live.
- A missing executable is an unavailable-harness skip; a selected executable that cannot run fails
  the opted-in proof and never produces an observed evidence row.

### Todos

Delta-heavy codex streams and large-thread `thread/read` latency remain unmeasured (worker
confidence register entries 3/9); a later tuning leaf owns realistic pressure evidence.

## Docs References

No Domain Documentation source is configured. The installed production seam is the direct
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The redacted codex `substrate-evidence/*` rows this suite captures and honors. | "substrate-evidence/live-frames-page" | mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:40-40 |
| The redacted pi `substrate-evidence/*` rows this suite captures and honors. | "substrate-evidence/live-frames-page" | mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json:40-40 |
| The claude row whose version-mismatch reason this suite enforces. | "Installed 2.1.214 mismatches the locked 2.1.211 gate;" | mcp/tests/fixtures/conversation_runtime/claude-2.1.211.json:43-43 |
| Foundation tests require non-enablement and a raw-free fixture set across these files. | `test_installed_runtime_fixtures_are_allowlisted_evidence_not_enablement`; `test_runtime_fixtures_contain_no_raw_secret_path_or_conversation_material` | mcp/tests/test_conversation_foundation.py:163-188; mcp/tests/test_conversation_foundation.py:191-202 |
| The deterministic contract suite whose fake-transport claims this file re-proves live. | `test_reserved_key_round_trip_and_no_leak`; `test_native_page_bridge_epoch_stamped_and_frames_validated`; `test_submission_provenance_all_sources_epoch_and_bounds`; `test_fixture_shaped_response_without_live_epoch_fails_validation` | mcp/tests/test_harness_control_evidence.py:361-409; mcp/tests/test_harness_control_evidence_ipc.py:155-198; mcp/tests/test_harness_control_evidence_ipc.py:229-312; mcp/tests/test_harness_control_evidence_ipc.py:314-337 |
| The installed-version probe skips absent commands and executes selected commands strictly. | `_version_of` | mcp/tests/test_harness_control_evidence_installed.py:102-111 |

## Cross-Repo References

No neighboring repository participates; installed harness binaries are local tools, not repo
boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-28T06:28+02:00 — No content impact: extracted the exact Claude fixture path into one
  literal constant so lifecycle consumer discovery can observe it; installed-runtime evidence and
  assertions are unchanged.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 removed broad process-error skipping from the installed evidence probe; only missing executables skip, while a selected but unusable runtime fails the opted-in proof.
- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the unavailable-harness
  skip for version processes that cannot start or complete. Such a skip cannot create observed
  fixture evidence; verification metadata remains pinned until closeout.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T03:11:47+02:00 — W3-B04 curator: curated 5 table citations (5 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: the codex live test was split for C901, so
  the whole-family assertions now live in `_assert_evidence_family(page)` and the persisted-thread
  plus factory-resume half in `_assert_resume_channel_reaches_the_persisted_thread(root)`; both live
  classes gained the registered `@pytest.mark.ar_run_evidence_installed` marker, and the cockpit
  submissions now pass a `ControlSubmission` parameter object. Named the two helpers in Logic and
  recorded the marker and the submission object under Conventions.

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: created the installed-runtime evidence
  capture sidecar (3 opt-in classes: codex 0.144.5 live incl. ephemeral refusal + resume E2E, pi
  0.80.7 live, claude version-honesty). Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
