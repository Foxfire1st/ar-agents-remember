# mcp/tests/test_master_retirement_refusals.py

## Governing Overview

[tests overview](overview.md)

## Purpose

Refusals of the retire operation: each names its file or its action, and the action works. A request addressed to a document that cannot be read is refused by the file's name; a refusal that tells the operator to take a master out of a sprint names the edit that works on that sprint. A refused request leaves nothing behind, a directory included, and a master has one retirement record at one place.

## Code Commentary

`_carry_out_removals` performs the named edits and repeats the request. The cases cover unreadable canonical proof objects, an unreadable master document, a malformed list field, a request addressed to an unreadable document, an unreadable task folder, a master put back without a typed row, a lone master's record, several commanding sprints, an entry that names two masters, a refused first phase that leaves no directory, two retirement records, a row number already in use, and a folder recorded at both places.

## Evidence

- A refused first phase of a master that no sprint commands leaves no directory it made for the record. [1]
- A request addressed to an unreadable document is refused by the file's name before anything else. [2]
- A master with two retirement records is refused with both named, and a new retirement row never takes a number that is in use. [3]
