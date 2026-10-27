# mcp/tests/test_paseo_bridge.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Exercises the Node bridge from both sides: the Python `bridge_call` wrapper that spawns it, and
`paseo_bridge.mjs` itself against a fake `@getpaseo/client` package installed in a scratch prefix. It
proves a call is pointed at the configured runtime and no other, that every failure carries a name,
and that the script's header declares each command and non-public entry point it uses.

## Code Commentary

### Logic

- **Process-level calls.** `BridgeProcessTests` proves an unconfigured or never-started runtime refuses
  before any process is spawned, that the script is invoked as `/usr/bin/node <paseo_bridge.mjs>
  <command>` against the configured runtime URL and no other, that every failure of a call is a named
  `PaseoBridgeFailure`, that output which is not UTF-8 is an unreadable reply rather than a decoding
  error, and that a call which does not end is stopped and reported as a timeout.
- **The real script.** `BridgeScriptTests` (skipped when `node` is not on `PATH`) runs the script
  against `FAKE_DAEMON_CLIENT`/`FAKE_CLIENT_ROOT`: the catalog lists ready, enabled providers with their
  models and thinking options, script failures are named, and a second daemon is refused.
- **Provider options.** `BridgeProviderOptionsTests` proves `agentCreation` hands the host the provider
  options under the name each client reads, and only those it reads.
- **The header as contract.** `BridgeScriptHeaderTests` reads the script text and requires its header to
  list every command and non-public entry point the script uses; the repository-wide single-path scan of
  bridge callers is `test_paseo_single_path.py`.
- Node's own failure reports are held as `NODE_CRASH_REPORT`, `NODE_OUT_OF_MEMORY_REPORT` and
  `NODE_THROWN_VALUE_REPORT`, so a crash, an out-of-memory exit and a thrown non-error each keep a name.

### Conventions

Cases that spawn Node build a scratch prefix holding the fake client package and capture the script's
stdout, stderr and exit status through the same `bridge_call` boundary production uses.

### Invariants And Boundaries

- The wrapper never reaches a runtime the configuration does not name.
- The fake client is never imported by product code; it exists only under a scratch prefix per case.

## Partial catalog answers

The catalog cases distinguish successful empty listings from unanswered parts. Missing mode, effort or configuration data is named by its part error; failed model listings omit `models`. A deadline reached while a provider is still loading preserves its enabled identity with an unanswered model listing instead of turning the whole catalog into a timeout refusal.

## Evidence

- The wrapper's process boundary: unconfigured refusal, the configured runtime as the only target, named
  failures, undecodable output and an unterminated call. [1]

- Process-level refuse-before-spawn and single-target behaviour of `bridge_call`. [2]



- Catalog shape, script failures and provider-option naming against the real script and fake client. [3]



- The scoped current source carries the module/document behavior described above. [1]
