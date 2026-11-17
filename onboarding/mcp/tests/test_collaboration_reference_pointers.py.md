# mcp/tests/test_collaboration_reference_pointers.py

## Governing Overview

[overview](overview.md)

## Purpose

The tests compare the composition manifest's generated routing for `tasks/collaboration-method` and `tasks/document-authoring` with the step and audiences derived from their instruction pointers. They read effective references through `compose_manifest`, mutate audiences in `derived.references` for refusal cases, and direct a mismatch to the renewal command.

## Code Commentary

`_assert_collaboration_reference_matches_pointers` keeps the mismatches `manifest_mismatches` reports for those two references and requires none. It reads the collaboration method through `compose_manifest` and requires a nonblank effective step. Both assertions name `Run {RENEW_COMMAND}` on failure. The derivation reads the role files, operations, `SKILL.md` and `core/every-role.md`.

The positive case reads the collaboration method through `compose_manifest` and also requires its authored source to be `reference/tasks/collaboration-method.md`, an existing file that is neither injected, nor a step detail, nor among the shipped detail references. The refusal cases add an unpointed role to the collaboration method's `derived.references` audience, move the inbound `core/every-role.md` pointer into the method itself in a copied corpus, and remove the Worker from the document-authoring `derived.references` audience; each must fail the assertion.

## Relationships

The derivation is `manifest_mismatches` in `agents_remember_test_support.testing.manifest_step_derivation`; the shipped detail list comes from `_shipped_parsed` in `test_l84_capsule_delivery_proofs.py`. `test_l84_unique_detail_pointers.py` covers the detail pointers of every compiled role and operation pair.

## Evidence



- The collaboration method has its own source file and is neither injected, a step detail nor a shipped detail. [2]

### Repo-Internal References (renewed)

- Only mismatches of the two keyed references are kept, none is allowed, and the collaboration method must have a nonblank composed step. Both assertions name the renewal command. [1]
- Adding an unpointed role to the derived collaboration audience and moving its inbound pointer into the method itself both fail. [3]
- Removing the Worker from the derived document-authoring audience fails. [4]
