# scripts/pnt_sandbox/README.md

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

The sandbox manual describes the fixed disposable layout and five command flows, canonicalized directory and lock, owned process records and root-resolution admission. It explicitly retains already-running check bypass, external harness homes/caches, user-level AR servers, linked Eve dependencies/key file and citation cache. Preserve these boundaries when summarizing the tool; the prose is not a guarantee of OS containment.

## User settings isolation

The manual now gives the sandbox its own user settings file at `config/agents-remember/settings.json` (including `paseoRuntime`), runs every process under `XDG_CONFIG_HOME=<sandbox>/config`, and requires the explicit whole-file upgrade for an older sandbox instead of reading the old file as a fallback.

## The tool server

The manual's tool-server section tells an agent how to drive a sandbox: tool calls go through the helper with a request file naming `sandbox`, `hostPort`, `config`, `expect` and `calls`; the caller's environment is not the server's; the helper resolves the host with the build's own code and refuses another home or address, naming both; a fresh build's no-host phase is the one admitted state and its report says so; and the sandbox must be started for its host to answer. The section states this boundary and does not claim OS containment against a sandbox owner rewriting its own files.

## Evidence

## 260928-MIK-L96 The public install route and explicit ports

The sandbox README now documents the public build/check/start/stop commands taking the two ports with defaults 6820/9797, the sandbox start using the public install route instead of the retired direct provision, and the product Node and cache roots the safety check requires inside the sandbox.

- The document the tooling follows. [2]

- The scoped current source carries the module/document behavior described above. [1]
- The tool-server section names the request fields, environment separation, host refusal, the no-host build phase and the start prerequisite. [3]
