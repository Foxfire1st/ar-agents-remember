# mcp/src/agents_remember/cli/role_launch_first_run.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Prepare a host that has never run this product in three ordered stages, and report every stage a failure left behind.

## Code Commentary

The stages run in order through the owners that already exist. **Scaffold** — `runtime_install`'s own install pass, run only when the configured coordination root lacks the retained assets the surviving installer writes in every delivery mode (`SCAFFOLD_ENTRIES`: `docs` and `tasks`; the capsule mode withholds `AGENTS.md` and no skill folder is written at all, so neither can be a predicate). A missing memory root, task or repository does not stop it, and a selected delivery mode the installer refuses is answered before anything is written. **Host authority** — the `paseoRuntime` block of the installed MCP settings file, created only when that file has no block, then read back through the reader the rest of the product uses; a configured host is read, never rewritten, so the developer decides when real settings change. **Host** — the existing provisioner in its install intent, so an already serving host keeps its sessions, then one proof that the daemon answers on the configured address and one that the AR plug-in stamped after loading; `configured: false` and a kept-running-but-restart-owed host are never read as launchable. A failed stage raises `FirstRunPreparationError` naming the stage, one clause per stage the call completed (including the installer's observed effects) and the host state it left behind in the provisioner's own words; there is no rollback, only an accurate account. The report travels on the call's own context, is set before the first stage writes, and is cleared with the call, so a later refusal can still carry the preparation it made. A direct call of this preparation helper runs the three converging stages. The public launch admission skips preparation when the same request already has its own receipt or matching message binding, and reconciles that existing execution without starting a second seat.

- A receipt or matching selection binding marks an existing request. [7]
- Public first-run preparation leaves that existing execution alone. [8]

## Evidence

- The three stages in order, and the report that carries what each observed. [1]
- The predicate names the assets every delivery mode writes. [2]
- The post-provision proof: the daemon answers and the plug-in it loaded is the installed one. [3]
- The failure detail names the completed stages, their paths and the retained daemon. [4]
- A provision failure and a plug-in load failure each carry the completed stages and the running daemon. [5]
- The installed scaffold is what the cold path accepts, and a root without it is not prepared. [6]
