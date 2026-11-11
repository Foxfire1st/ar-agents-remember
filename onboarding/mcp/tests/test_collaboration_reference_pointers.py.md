# mcp/tests/test_collaboration_reference_pointers.py

## Governing Overview

[overview](overview.md)

## Purpose

The test proves that the composition manifest's `tasks/collaboration-method` and `tasks/document-authoring` references declare exactly the step and audiences that their pointers in the first-message texts derive, and that a change on either side is caught.

## Code Commentary

`_assert_collaboration_reference_matches_pointers` keeps the mismatches `manifest_mismatches` reports for those two references and requires none, and requires the collaboration method to declare a step. The derivation reads the role files, operations, `SKILL.md` and `core/every-role.md`.

The positive case also requires the collaboration method's source to be `reference/tasks/collaboration-method.md`, an existing file that is neither injected, nor a step detail, nor among the shipped detail references. The refusal cases add an audience the pointers do not give, move the inbound `core/every-role.md` pointer into the method itself in a copied corpus, and remove the Worker from the document-authoring audience; each must fail the assertion.

## Relationships

The derivation is `manifest_mismatches` in `agents_remember_test_support.testing.manifest_step_derivation`; the shipped detail list comes from `_shipped_parsed` in `test_l84_capsule_delivery_proofs.py`. `test_l84_unique_detail_pointers.py` covers the detail pointers of every compiled role and operation pair.

## Evidence

- Only mismatches of the two keyed references are kept, none is allowed, and the method declares a step. [1]
- The collaboration method has its own source file and is neither injected, a step detail nor a shipped detail. [2]
- An extra audience and a pointer moved into the method itself both fail. [3]
- Removing the Worker from the document-authoring audience fails. [4]
