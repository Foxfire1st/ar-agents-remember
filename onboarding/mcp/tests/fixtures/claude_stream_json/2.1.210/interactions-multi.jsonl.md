# mcp/tests/fixtures/claude_stream_json/2.1.210/interactions-multi.jsonl

| Field                  | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/tests/fixtures/claude_stream_json/2.1.210/interactions-multi.jsonl` |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-31T15:32+02:00                                             |
| lastVerifiedCommitHash | `00e83791d4d21bf56fd5b3cc0af194bc5e28112a`                         |
| lastVerifiedCommitDate | 2026-07-31T05:07:07+02:00|
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

| Finding | Source Path |
| --- | --- |
| The only consumer. | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| The sibling recordings for the same vendor version. | [2.1.210/](agents-remember/mcp/tests/fixtures/claude_stream_json/2.1.210/) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created the missing sidecar for this
  fixture (a pre-existing 1:1 gap, not introduced by this leaf).
