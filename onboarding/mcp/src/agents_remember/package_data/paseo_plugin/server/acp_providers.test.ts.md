# `server/acp_providers.test.ts`

## Governing Overview

[Route overview](../overview.md)

The package test for the provider verdict: it drives the loader over a recorded copy of the installed Paseo 0.16.2 distribution and asserts which providers the plugin reads as ACP.

## What it establishes

The test supplies a copied Paseo installation and a temporary `<PASEO_HOME>/config.json`. Discovery reads the installed server package metadata, provider registry, provider manifest and imported provider classes. A resolved class is ACP when its ancestry reaches `ACPAgentClient`. The plugin uses the in-memory verdict for wake decisions and publishes the per-provider results to `<PASEO_HOME>/agents-remember/acp-providers.json`. The test reads that product output. Role launch reads the publication and adds the helper-wait instruction for a provider marked ACP.

The fixture under `server/fixtures/paseo-0-16/` supplies the provider classes, `plugin-process.js`, and the provider manifest. The integrity case checks the recorded host version, each copied file's size and SHA-256, and that all copied files appear in `fixture.json`.

A failure can identify fixture drift or an incorrect provider verdict. The case over a
real installed Paseo is skipped, not failed, when none is installed or when the installed version
is not the pinned one that `paseo_host/contract.json` names.

## Reading it beside the others

`server/acp_providers.ts` states the rules; this file is where they are exercised. The wait
itself — the declaration, the three-minute check and the ending — is covered by
`server/subagent_wait.test.ts`, and the sentence a seat is given before it declares by
`mcp/tests/test_role_launch_acp_instruction.py`.

## Evidence

- The fixture is a recorded copy of the pinned distribution, and the test checks its recorded version, file list, sizes and hashes. [1]
- The installed-host case skips absent installations and installations at a different version. [2]

- The classifier reads the installed package files and host configuration. The test checks the resulting provider verdicts in the JSON the plugin publishes. [3]
- Role launch reads the published verdict from the configured Paseo home and selects the helper-wait instruction for a provider marked ACP. [4]
- The plugin passes the classifier’s in-memory verdict to the turn-end wake decision. [5]
