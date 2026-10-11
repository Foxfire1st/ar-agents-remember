# mcp/src/agents_remember/cli/providers_remove.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

## Purpose

The explicit `agents-remember providers-remove` CLI removes leftover provider runtime
folders under the selected coordination root. It is not an MCP tool, normal install
cleanup, provider recovery, or permission to delete memory repositories.

## Code Commentary

`run` resolves trusted settings explicitly or through normal CLI discovery. The fixed
folder list is `providers/{runners,data,logs,_venvs,_bin}`; `memory-repos/` is outside it.
Discovery reports existing non-symlink directories and measured apparent file bytes.
An empty population succeeds without stopping watchers. `--dry-run` reports it and
returns before stop/removal; it still refuses an escaped provider root.

The physical provider root must equal `resolve(coordinationRoot)/providers`. A provider
root alias into another tree refuses before stopping anything; a consistent alias of
the coordination root can still identify its owned providers directory. Each target
must remain inside that root and is revalidated immediately before `rmtree`.

Apply stops configured watchers first. A failed stop refuses deletion. A best-effort
Linux `/proc` scan checks process cwd/open fds under each target and reports pid,
command and folder on a busy refusal. It is not a portable or atomic proof that no
process can open a folder later. Containment is also point-in-time, not a filesystem
transaction. Successful removals report the previously measured bytes; partial failures
can leave earlier removals complete and return failure. Configuration/root/busy/stop/
removal failures return 1, success or no remaining folders returns 0.

## Boundaries

Normal runtime installation stops old watchers and preserves provider data; only this
separately requested destructive command removes the listed folders. Its stop-failure
refusal differs from the installer's report-and-continue behavior. This card describes
source control flow, not a cleanup invocation on the user's system.

## Evidence

- The complete file owns the behavior and limits described above; documentation/tests are not fresh execution evidence. [1]

## External and cross-repository evidence

No Domain Documentation entries are configured in the resolved source registry.
This card claims only the package-local source contract; no external runtime or
cross-repository acceptance evidence is inferred.
