# scripts/pnt_sandbox/operations.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

All process run/spawn/provision actions pass through the scrubbed environment and exact selected-build interpreter. Ignored Python and dashboard build products can be prepared in the checkout. Root/corpus helpers run in the selected build, provision inherits the command lock, dashboard owns a detached session and tmux stop names only its sandbox socket. No broader child containment is claimed.

The runtime-install request now carries the same `sandbox` and `hostPort` fields as the corpus request, taken from the operations' own layout, so the helper admits the sandbox's host for the install as it does for the corpus. The install path, its lock and its receipt retirement are unchanged.

The runtime-install answer may omit its host block. In that case the helper reads only its named report confined under the sandbox root, requires an object and adds that report's host field while preserving every answer outcome field. An unreadable/outside/non-object report is an explicit install refusal; it is not a reason to synthesize success. This is source documentation, not a sandbox run.

## Evidence


## 260928-MIK-L96 The public install receipts

`Operations.runtime_install` retires the previous current receipt into history before its child runs and records fresh cut, timeout and malformed outcomes with the underlying error and the real receipt and server-log paths, instead of leaving an old success visible.

- The public install receipt owner. [2]

## Current source evidence


- A compact install response reads its confined whole report without overwriting the response outcome. [3]


- The scoped current source carries the module/document behavior described above. [1]

- The runtime-install request names the sandbox and its Paseo port beside its settings file and roots. [4]
