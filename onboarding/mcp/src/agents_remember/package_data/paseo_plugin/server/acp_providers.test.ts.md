# `server/acp_providers.test.ts`

## Governing Overview

[Route overview](../overview.md)

The package test for the provider verdict: it drives the loader over the vendored Paseo 0.12
host tree and asserts which providers the plugin reads as ACP.

## What it establishes

The verdict is what decides whether a seat may declare a helper wait at all, so the test pins
both halves of it: which provider modules the loader finds in a host's `acp-providers.json` and
which of those the classifier calls ACP. It runs against the synthetic host tree under
`server/fixtures/paseo-0-12/` rather than a real Paseo install, so the same fixture set answers
for every provider the leaf names — `acp-agent`, `claude`, `codex-app-server`, `copilot-acp`,
`cursor-acp`, `generic-acp`, `kimi-acp`, `kiro-acp`, the two mock agents, `omp`, `opencode`,
`pi` and `trae-acp`, with `plugin-process.js` and the manifest supplying the rest of the host's
shape.

A test here that fails means a seat either loses the right to declare a wait it should have, or
gains one it should not — which is the failure the declaration path was reproached for in
production, not a cosmetic difference in a loader.

## Reading it beside the others

`server/acp_providers.ts` states the rules; this file is where they are exercised. The wait
itself — the declaration, the three-minute check and the ending — is covered by
`server/subagent_wait.test.ts`, and the sentence a seat is given before it declares by
`mcp/tests/test_role_launch_acp_instruction.py`.
