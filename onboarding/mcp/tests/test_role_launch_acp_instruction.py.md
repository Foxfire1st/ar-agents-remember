# `tests/test_role_launch_acp_instruction.py`

## Governing Overview

[Route overview](overview.md)

The launch-side test for the sentence a seat is given before it can declare: `ACP_WAIT_INSTRUCTION`
is appended to a Paseo runtime's prompt, and only there.

## What it pins

The instruction reaches the seat through the launch, not through the turn-end path, so the test
holds it at the three places a launch is visible:

- the stored prompt is exactly the caller's prompt, a blank line, then `ACP_WAIT_INSTRUCTION`
  (`f"{prompt}\n\n{ACP_WAIT_INSTRUCTION}"`), byte for byte;
- the bytes the ACP runtime receives are the plain launch's bytes plus `b"\n\n"` plus the
  instruction encoded — so the append is additive and changes nothing else about the launch;
- a run that is **not** on a Paseo runtime never sees `WAITING FOR SUBAGENTS` in its saved
  `replayRequest.agent.prompt`, so a non-ACP seat is not invited to declare a wait it cannot keep.

The middle assertion is the one that keeps the feature honest: if the instruction is ever
prepended, re-encoded differently, or merged into the caller's prompt, this test fails on the
byte comparison rather than on someone noticing later that a seat's prompt drifted.

## Frame

The fixture configures a real Paseo runtime through the launch route, so the test exercises the
route rather than a helper: the instruction is appended where the runtime actually builds its
prompt. What a seat does once it has declared is covered by
`server/subagent_wait.test.ts`; who may declare at all by `server/acp_providers.test.ts`.
