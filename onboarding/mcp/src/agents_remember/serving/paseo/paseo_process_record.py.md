# mcp/src/agents_remember/serving/paseo/paseo_process_record.py

## Governing Overview

[overview](../overview.md)

## Purpose

Proves that the home process record names that home's Paseo supervisor.

## Code Commentary

inspect_record combines recorded PID with live process facts: its command line and the `PASEO_HOME` of its own environment. A record that names no live process, no Paseo supervisor or another home's supervisor is classified stale and may be removed only under that classified state; a live process whose identity cannot be read is refused. This protects home-addressed native stop/start, whose upstream PID check alone does not prove home ownership.

In the pinned Paseo 0.16.2, `stopDaemonInstance` checks boot identity first and abandons a record from another boot. When boot identities cannot decide the check, the host uses process liveness and record age. That upstream liveness rule still does not prove that a reused PID belongs to this home; the product's independent process-identity check remains necessary.

`read_process` also records the process executable (`/proc/<pid>/exe`), the carried session-variable names through the product's `carried_session_variables`, which the start/status outcomes report without values, and the values of the harness-home variables that `paseo_harness_homes` catalogues. Those values stay out of the facts' representation; status reports only their names, and only the `harness-home-would-change` refusal names a value.

## Evidence

- The home record trust rule remains an independent check of the recorded PID's actual home and process. [1]

- The process facts include the executable, carried session-variable names without values, and the values of the catalogued harness-home variables. [2]


- The 0.16.2 host's stop predicate checks boot identity first. The product separately verifies the recorded process's identity and home. [3]


- Harness-home values are kept out of the process facts' representation. [4]
