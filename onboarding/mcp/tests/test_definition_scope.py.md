# mcp/tests/test_definition_scope.py

## Governing Overview

[Tests](overview.md)

## Purpose

Checks call-scoped parser reuse, detached return values and disposal with a counted production parser.

## Code Commentary

Distinct paths, source contents and grammars each receive their own parse. Nested scopes join the current call. Mutation of returned dictionaries or lists does not alter later results, and an exception clears the outer scope. Unscoped calls parse independently.

JavaScript, TypeScript and TSX test-case lookup, refusal diagnostics and exact ranges share their parsed test tree. Ordinary source trees are not retained in that diagnostic cache. Copied worker contexts share the call cache under its lock while keeping returned containers separate.

## Relationships

The tests instrument the production grammar parser. Dispatch and background-worker lifetime tests live in `test_definition_scope_boundaries.py`; this file tests the reusable scope itself.

## Evidence

- Path, contents and grammar all distinguish parse inputs. [1]
- Nested scopes detach returned containers and discard results on error. [2]
- Test diagnostics share their parse without retaining ordinary trees. [3]
- Copied contexts share work but return independent containers. [4]
