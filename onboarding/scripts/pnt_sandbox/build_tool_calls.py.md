# scripts/pnt_sandbox/build_tool_calls.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

This helper starts the selected build's MCP server over stdio in the sandbox's own environment, checks the admission before the first call, and skips a creation only when its public probe succeeds; a failed call ends the sequence with a bounded report. The request names the sandbox it belongs to; a `hostPort` it states must be a sandbox port, and an omitted one defaults to the sandbox's 6820. A request that names no sandbox, or names a port outside 1–65535 or one of the live ports 9785/9786, is refused and nothing starts.

The server's environment is built from the named sandbox with `sandbox_environment`, which removes the variables that select another runtime and adds the sandbox's own, whatever selectors the caller's environment holds; the caller's `PATH`, `HOME` and harness logins stay, as the tooling's environment rule says. The result is read back through the tooling's own `foreign_variables` judgment before the server exists — the scrub, not the read-back, is what removes `PASEO_*`. Under that environment the helper resolves the Paseo home and listen address with the build's own settings resolution and compares them with the layout's own pair, `<sandbox>/paseo/home` on `127.0.0.1:<hostPort>`; a resolved host or address that differs refuses before any call, naming both. A settings file inside the sandbox that points at another runtime refuses the same way.

One state is admitted with no host: the sandbox records no host and the build resolves none. The fresh build's asset bootstrap is the occasion this exists for; a built sandbox whose `paseoRuntime` block was removed reaches the same state, as the Worker's real proof did. Then the report's `host` says `"no host configured"`, and a call that needs a host fails inside the build without reaching any Paseo home or address outside the sandbox. In the configured phase `host` names the sandbox's pair, beside the four keys `ok`, `packageRoot`, `results` and `error`. The admission also checks the selected build's coordination root, workspace root, repository scope and configured providers — the field `server_info` actually sends, `unusedProviderKeys` — after the `server_info` read and before any corpus call.

The request also supplies the `expect` roots and `config`/`cwd` the helper passes on, and any absolute directory is accepted as `sandbox`; the admission therefore does not bind the server's coordination and workspace roots to the named sandbox. That is pre-existing behaviour, outside this requirement's scope.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
- The request's sandbox is required, absolute, and its port must be a sandbox port other than the live ports. [2]
- The tool server's environment is the sandbox's, and a surviving selector refuses before the server starts. [3]
- The build's own settings resolution is read under the server's environment, so the comparison is not made with the caller's environment. [4]
- The sandbox's layout pair is the admitted host; a recorded settings host that differs, or a resolved host that differs, refuses before any call. [5]
- A request refused by the admission answers with no host and no call; a refusal from the `server_info` checks is returned after that read, with the admitted host in the report. [6]
- The provider check reads the field `server_info` sends for configured providers. [7]

- The unconfigured state is admitted and named by condition, not by build freshness, and a foreign resolved host refuses. [8]
