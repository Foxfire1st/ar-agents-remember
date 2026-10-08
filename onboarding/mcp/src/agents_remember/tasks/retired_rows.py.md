# mcp/src/agents_remember/tasks/retired_rows.py

## Governing Overview

[tasks overview](overview.md)

## Purpose

Retired rows: what they are, and the one refusal for every route that would change one. A sprint row that carries a retirement proof is the record of a master's retirement. Only `task_doc.retire_master` writes it; every other writer of rows refuses with the text below, which names the row by its number.

## Code Commentary

`records_retirements` answers whether a document holds a retirement proof row; `payload_is_sprint` says whether a payload addresses a sprint; `refuse_retired_row` is the single refusal (`retired_row_message`) every route that would change such a row calls, naming the master is retired. The generic task-document operations therefore cannot add, change or remove a retirement proof.

## Evidence

- Only task_doc.retire_master writes a sprint row that carries a retirement proof; every other row writer refuses by name. [1]
- A task document whose master sync would touch a retired row is refused as a whole with the words the master is retired. [2]
