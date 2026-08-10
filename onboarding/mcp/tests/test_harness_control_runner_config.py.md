# mcp/tests/test_harness_control_runner_config.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_harness_control_runner_config.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-07-31T15:32+02:00                             |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`         |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Payload-level tests for `parse_runner_config` and the helpers it delegates to.

`test_harness_control_runner.py` exercises the happy round trip and three malformed tokens.
This module owns the arms that round trip cannot reach:

- **every rejection message** the parser can raise,
- the **additive-field defaults**, and
- the **two resolved-launch agreement refusals** that keep a contradictory payload from ever
  reaching a vendor process.

## Why The Message Is Asserted, Not Just The Type

Each case asserts the **exact** parsed value or the **exact** refusal text, because the
message is the evidence a hosted session surfaces when a launch is refused. A refusal whose
text does not name what disagreed is a refusal an operator cannot act on.

## Classes

| Class | Arms |
| --- | --- |
| `RunnerConfigRejectionTests` | Every rejection the parser can raise, by message. |
| `RunnerConfigDefaultTests` | The additive-field defaults, so a payload written before a field existed still parses to the documented value. |

Helpers: `_encode`, `_payload`, `_launch`.

## Invariants And Boundaries

- Additive fields must default; an older payload must not become unparseable.
- A payload whose resolved launch contradicts its declared fields is refused **before**
  anything is spawned.
- Refusal text is part of the contract, not incidental.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `parse_runner_config` and its delegated helpers. | `parse_runner_config` | mcp/src/agents_remember/serving/harness_control_runner.py:72-97 |
| The round-trip suite this module completes. | `test_command_round_trip_and_malformed_payloads` | mcp/tests/test_harness_control_runner.py:60-75 |
| The hosted-session surface that shows the refusal text. | `test_an_unreachable_bridge_is_not_ready_and_keeps_the_adapter_refusal` | mcp/tests/test_hosted_readiness.py:182-199 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:03:00+02:00 — Curator W3-B02 repaired 2 Repo-Internal citation rows, resolving 4 manifest findings with exact runner-config and hosted-readiness regression anchors; verification metadata was preserved.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new runner-config
  rejection/default suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.
