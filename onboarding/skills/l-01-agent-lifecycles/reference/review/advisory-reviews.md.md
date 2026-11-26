# skills/l-01-agent-lifecycles/reference/review/advisory-reviews.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Architect-only Tier-2 procedure for commissioning optional advisory Investigators alongside a leaf's normal Reviewer to obtain independent second views of a freeze.

## Code Commentary

Defines an explicit routing exception: the Architect commissions advisory Investigators via taskless `role_start` (no leaf seat; Manager relays no findings), gives each the exact freeze, packets, rulings, and Worker evidence plus isolated output folders, clean copies, and separate ports while forbidding access to Reviewer, Curator, or other advisory files or naming already-noticed issues. Once reports arrive, the Architect compares findings, sends the Reviewer one questions file with unraised items (explicitly instructing the Reviewer to rule on each), notifies the Manager once for gate/round hold (Architect grants any extra round), and confirms every advisory finding has a ruling before landing. Launch settings follow `orchestration.roles`/`rolesPerLevel`, and permission prompts link `operations/orientation.md#formal-permissions`.

## Relationships

Linked from `operations/review.md` (`<!-- ar:roles architect -->`) and `roles/architect.md` Reference index. Registered in `composition-manifest.json` (`step_detail: true`), mirrored under `package_data/runtime/skills/`, and verified by `test_role_instruction_corpus_policies.py`.

## Evidence

- Advisory reviews are commissioned only by the Architect via taskless `role_start`, keeping the leaf's single Reviewer seat and Manager non-relay rule. [1]
- Isolation rules supply identical freeze inputs with separate folders/clean copies/ports and forbid reading Reviewer, Curator, Manager, or peer advisory artifacts. [2]
- Advisory reports alter no verdict alone: the Architect sends one questions file to the Reviewer, tells the Manager once, grants any extra round, and checks every ruling before landing; permissions follow `#formal-permissions`. [3]
