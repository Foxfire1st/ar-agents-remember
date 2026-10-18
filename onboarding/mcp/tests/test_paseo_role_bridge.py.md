# mcp/tests/test_paseo_role_bridge.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Message send distinguishes idle-turn start, in-flight steering, permission refusal and non-steerable busy providers. Wait follows the turn that consumed the message rather than a later unrelated turn, and reports delivery uncertainty without cancelling work. The native client is replaced by a controlled event/state stub. R71 cases prove creation sends mode and each feature before any prompt, the profile bridge reads only the running host configuration, and the read grant uses exact `server_info` with mutators out.

## Send-decision script cases

`AgentSendScriptTests` covers the steer-or-hold decision the script makes. `test_an_idle_agent_starts_a_turn_and_a_steer_goes_only_to_a_provider_that_takes_one` sends to an idle agent with `{messageId}` alone — no active-turn behaviour is asked for — and steers only when a turn is running for a provider known to take one. `test_a_running_turn_is_steered_or_held_by_the_provider_and_never_cut_off` steers a steering provider and returns `busy` for a provider without steering, with no send in that case, so its turn is untouched; the same provider is still sent to while idle. A send the runtime refuses remains a refused call. These are the controlled script stub's assertions, not a live host.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
