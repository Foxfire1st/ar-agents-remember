# mcp/tests/fixtures/claude_stream_json/2.1.210/interactions-multi.jsonl

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/tests/fixtures/claude_stream_json/2.1.210/interactions-multi.jsonl` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-31T15:32+02:00                                             |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                         |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../../../overview.md`                                             |

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

One recorded Claude stream-json `control_request` frame: a `can_use_tool` request for
`AskUserQuestion` carrying **two** questions at once — a single-select (`Mode`, with
described options) and a multi-select (`Features`, where one option carries no
description). It is the multi-question shape the single-question recordings in this
directory do not contain.

## Consumers

`test_harness_control_claude.py` loads it via `_load_fixture("interactions-multi.jsonl")`
in two tests, to prove the interaction projection handles a request with several questions
and mixed `multiSelect` / description presence.

## Invariants And Boundaries

- Observed vendor evidence for Claude 2.1.210, recorded under its version directory. It is
  a recording, not a maintained policy file: do not hand-edit it to make a test pass.
- Exactly one line; the loader unpacks a single frame (`(question,) = …`).
- Option descriptions are deliberately inconsistent between the two questions — that is the
  case being covered.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Claude control test asserts that `mode.multi_select` is false. | "(mode.text, mode.header, mode.multi_select)," | mcp/tests/test_harness_control_claude_stream_1.py:555-555 |
| The Claude control test asserts that `features.multi_select` is true. | "(features.text, features.header, features.multi_select)," | mcp/tests/test_harness_control_claude_stream_1.py:563-563 |
| The initialization sibling recording carries the vendor-version field. | `claude_code_version` | mcp/tests/fixtures/claude_stream_json/2.1.210/initialization.jsonl:2-2 |

## Update History

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residual D2 by binding both `multi_select` value predicates to their complete focused assertions; rechecked this card through the locked exact-document fixer/check.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created the missing sidecar for this
  fixture (a pre-existing 1:1 gap, not introduced by this leaf).
