# mcp/src/agents_remember/application/task_docs/task_retirement_records.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

Where a master's retirement stands on disk: its record, its folder, the sprints that name it. Read-only: the retire operation decides every step from this observation and never from the document a request happened to be addressed to.

## Code Commentary

`observe` reads the master's document, its folder at the live and archived locations, its proof file and the sprints that name it into `Observed`. `require_addressed_readable` refuses a request addressed to an unreadable document by its file name. `sprints_naming` resolves the sprint documents that command the master. `read_proof` reads `master-retirement.json` (`PROOF_NAME`) and `retirement_recorded` answers whether one exists; `_retired_rows` reads the plain rows a sprint carries for retired masters. Every existing unreadable canonical proof entry is sent to its required reader and refused by that path before preview or publication, and its object is preserved.

## Evidence

- Retirement sends every existing unreadable canonical proof entry to its required reader and refuses by that path before preview or publication. [1]
- A request addressed to an unreadable document is refused by the file's name before anything else. [2]
- A master has one retirement record at one canonical place, and a second record at the other place is refused with both named. [3]
