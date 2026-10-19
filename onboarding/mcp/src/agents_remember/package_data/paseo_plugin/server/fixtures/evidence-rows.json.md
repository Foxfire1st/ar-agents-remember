# mcp/src/agents_remember/package_data/paseo_plugin/server/fixtures/evidence-rows.json

## Governing Overview

[Area overview](../../overview.md)

## Purpose

Test data for the row-shape tests: five rows captured from the live host on 2026-10-19 and copied verbatim, with the digest of each source file they came from.

## Code Commentary

`sources` names each evidence file and its SHA-256; `rows` holds the row object itself for the L104 Curator's `role_message` (its escaped answer), a Hermes `role_message`, a Codex `role_message`, a Hermes `task_doc` and a Hermes `delegate_task`. `turn_ended.test.ts` reads the file and feeds these rows to the recogniser and to the hand-off and return tests, so the shapes under test are the captured bytes rather than reconstructions; rows of other forms that the tests build themselves stay in the test file and are labelled synthetic. The file holds no code, rule or behaviour of its own, and nothing outside the tests reads it.

## Boundaries

The digests are of the evidence files as captured, not of any later copy; a re-captured row is a new evidence file with its own digest, never an edit of this one.

## Evidence

- The five captured rows are consumed verbatim by the row-shape tests, with each source file's digest recorded beside it. [1]
