# scripts/pnt_sandbox/README.md

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

The sandbox manual describes the fixed disposable layout and five command flows, canonicalized directory and lock, owned process records and root-resolution admission. It explicitly retains already-running check bypass, external harness homes/caches, user-level AR servers, linked Eve dependencies/key file and citation cache. Preserve these boundaries when summarizing the tool; the prose is not a guarantee of OS containment.

## User settings isolation

The sandbox user-settings path remains config/agents-remember/settings.json under XDG_CONFIG_HOME=<sandbox>/config, with an explicit whole-file upgrade for an older layout and no fallback reader. The qualified manual and current builder place paseoRuntime in settings/agents-remember-settings.json, the sandbox MCP authority file; the tool-call helper reads that same authority. The user-settings path remains separate from host authority.

## The tool server

The manual's tool-server section tells an agent how to drive a sandbox: tool calls go through the helper with a request file naming `sandbox`, `hostPort`, `config`, `expect` and `calls`; the caller's environment is not the server's; the helper resolves the host with the build's own code and refuses another home or address, naming both; a fresh build's no-host phase is the one admitted state and its report says so; and the sandbox must be started for its host to answer. The section states this boundary and does not claim OS containment against a sandbox owner rewriting its own files.

## Evidence

## 260928-MIK-L96 The public install route and explicit ports

The sandbox README now documents the public build/check/start/stop commands taking the two ports with defaults 6820/9797, the sandbox start using the public install route instead of the retired direct provision, and the product Node and cache roots the safety check requires inside the sandbox.




- The tool-server section names the request fields, environment separation, host refusal, the no-host build phase and the start prerequisite. [3]

- Current sandbox setup writes the host block to MCP authority, separately from the protected user-settings path. [4]

- The scoped current source carries the module/document behavior described above. [1]
- The manual documents the selected ports and the public install, host-authority and retained-session boundaries. [2]
