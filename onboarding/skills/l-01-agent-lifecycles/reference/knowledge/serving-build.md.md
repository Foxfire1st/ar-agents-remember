# skills/l-01-agent-lifecycles/reference/knowledge/serving-build.md

## Governing Overview

[overview](../../overview.md)

## Purpose

How a Curator or other admitted command-line user binds a deciding or writing CLI run to the serving build. Serving-build authority itself stays with the orientation operation.

## Code Commentary

The mounted `knowledge_write` tool is preferred; a CLI run that decides or writes is first bound to the starting server's `server_info.servingBuild`. The original interpreter comes from `toolServer.command[0]` in the role-launch receipt or from `command` in the selected server's startup definition, with its spelling preserved, because the resolved `servingBuild.pythonExecutable` may follow a virtual-environment link to an interpreter without dependencies. If the admitted launch command is unavailable, the binding is reported unavailable rather than inferred or replaced by another build.

The file gives a shell recipe that sets the admitted interpreter and package parent and prints the CLI's serving identity; `version`, `sourceDigest`, `packageRoot`, `pythonExecutable` and `commit` are compared with the starting stamp before deciding or writing. A missing identity or mismatch does not establish the serving build: it is reported and the mounted tool is used where it admits the operation, and an unreported commit stays unknown. Public CLI commands such as `knowledge-worklist` and `knowledge-ingest` (with contract, list, authorization reference, `--commit` and `--json`) run with the same interpreter and explicit package path. The Curator role, `refused-write.md`, `curator/knowledge-ingest.md` and `curator/card-formats-and-citations.md` point here before such runs; the manifest lists the Worker and Curator as readers.

## Evidence

- The mounted tool is preferred, and CLI work binds to the starting server's serving build; orientation owns the authority. [1]
- The admitted interpreter comes from the launch receipt or server definition, and an unavailable command is reported, not inferred. [2]
- The identity is printed and compared with the starting stamp; a mismatch is reported and does not establish the serving build. [3]
- Public CLI commands run with the same interpreter and package path. [4]
- The Curator role points here before a command-line run that decides or writes. [5]
