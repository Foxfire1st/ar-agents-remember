# mcp/tests/test_pnt_sandbox.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The safety suite judges outside, missing and defaulted AR roots, exact sandbox values and resolving-build identity. Build-input cases preserve unmarked directories, marker replacement, repeatable incomplete reset, generated layout/settings and exact environment scrub. Port and environment checks use real child processes; failed-rmdir recovery includes a mock. The resolver-success control executes the real `build_roots.py` command and checks the JSON rather than exit zero alone: errors are empty, roots have exactly the expected keys and all values are non-null, including the five repository resolver roots. This protects the existing sandbox script; it does not claim that script was repaired here.

The compact-install fixture files a named whole report and feeds only an overflow/reportPath answer to the sandbox launcher. Provisioning uses its host facts and retains the compact receipt. A second answer with inline host action untouched overrides a disagreeing named report, so the launcher does not mark that host as newly started. This uses prepared Operations/supervisor collaborators, not a live install.

The helper-admission cases now run the real helper module against a recorded transport. Eight cases are added. They assert that the server receives `sandbox_environment` of the named sandbox, with the caller's `PATH`, `HOME` and logins kept but no selector; that a resolved host outside the sandbox, a request that names no sandbox and a port that is not a sandbox port refuse before anything starts; that configured providers refuse after the `server_info` read and before any other call; that a sandbox whose own settings select another host refuses, naming both; and that a sandbox recording no host is admitted with `host: {"state": "no host configured"}` while a foreign resolved host in that state refuses. These are controlled cases with a mocked transport; the Worker's retained no-model runs, not this module, are the real-execution evidence.

## Evidence

- Compact report fallback and inline-host precedence determine started bookkeeping without changing retained receipt bytes. [6]


## 260928-MIK-L96 The public install route and product Node roots

The sandbox tests gained the public install route receipts and admission cases, the foreign-package refusal, the cut/timeout/malformed receipt retirement, and the product Node and cache-root safety cases; their cards' safety and environment rules keep their obligations.

- The safety case for the product Node and cache roots. [2]

- The public install receipt cases. [3]

- The foreign-package admission case. [4]

- The real resolver command must return empty errors, every expected non-null root and five resolver keys. [5]

- The scoped current source carries the module/document behavior described above. [1]
- The tool server is started with the sandbox's own environment, including its own XDG roots, and no runtime selector. [7]
- A resolved host outside the sandbox is refused before any call, naming both hosts. [8]
- A request that names no sandbox is refused before anything starts. [9]

- The admission refuses a server with configured providers after the `server_info` read. [10]
- A sandbox whose own settings select another home or the live port refuses. [11]

- The unconfigured state refuses a foreign resolved host. [12]
- A request port that is not a sandbox port is refused. [13]
- The unconfigured state is admitted and named, and a settings host the build cannot resolve refuses. [14]
