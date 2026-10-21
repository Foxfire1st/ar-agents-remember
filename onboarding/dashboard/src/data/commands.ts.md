# dashboard/src/data/commands.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Give review command identities stable human-facing names for key help without duplicating chord bindings or traversal handlers.

## Code Commentary

The readonly COMMANDS array registers `review.nextChange` as Next block and `review.previousChange` as Previous block. The command IDs stay stable so stored keymap overrides still address them. Command has only id and label; no shortcut, zone or executable callback lives here. ReviewKeys reads effective keymap bindings for the review zone and joins their commandId to this array for display names. The chord-table consistency test checks registration completeness; registration is not proof that a shortcut was exercised or enabled in every context.

Changing bindings belongs to the keymap; changing what a step does belongs to traversal. Do not treat this label catalogue as a dispatcher or a second preference store.

## Evidence

- Reviewer help joins effective bindings to command labels. [2]
- Source test rejects a chord whose commandId is not registered; not an executed result. [3]

- Command records contain identity and label only, including the two review traversal names. [1]
