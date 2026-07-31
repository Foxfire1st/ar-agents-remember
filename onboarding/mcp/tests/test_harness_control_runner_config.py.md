# mcp/tests/test_harness_control_runner_config.py

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `mcp/tests/test_harness_control_runner_config.py`  |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-07-31T15:32+02:00                             |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`         |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

| Finding | Source Path |
| --- | --- |
| `parse_runner_config` and its delegated helpers. | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| The round-trip suite this module completes. | [test_harness_control_runner.py](agents-remember/mcp/tests/test_harness_control_runner.py) |
| The hosted-session surface that shows the refusal text. | [test_hosted_readiness.py](agents-remember/mcp/tests/test_hosted_readiness.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new runner-config
  rejection/default suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.
