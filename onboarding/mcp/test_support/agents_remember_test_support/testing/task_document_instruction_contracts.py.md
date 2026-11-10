# mcp/test_support/agents_remember_test_support/testing/task_document_instruction_contracts.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks that task-authoring entry points in the lifecycle skill point to the task-document authoring detail, that the detail states the current field conventions, and that the task and packet templates carry their required headings.

## Code Commentary

`assert_contract` runs over `skills/` and each generated skill copy the caller passes. It requires each pointer sentence in the Architect role and the leaf, master and requirement-packet templates outside fenced code, rejects retired "not tool-managed" wording, requires the authoring heading once and every field clause in the authoring detail, requires the `task_doc` editing clauses in the orientation operation, and checks the composition-manifest entries' source, roles, `injected: false` and `step_detail`. Each clause is also checked to fail when removed. Its reader is `mcp/tests/test_role_instruction_corpus.py`, which passes the generated copies from `curation_doctrine.GENERATED_SKILL_COPIES`.

## Evidence

- The four authoring entry points and their exact pointer sentences. [1]
- The field conventions the authoring detail must state. [2]
- Pointers, clauses, template headings and manifest entries are checked on the canonical and generated surfaces. [3]
