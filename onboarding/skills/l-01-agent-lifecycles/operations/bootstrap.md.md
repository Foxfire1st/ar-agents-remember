# skills/l-01-agent-lifecycles/operations/bootstrap.md

## Governing Overview

[overview](../overview.md)

## Purpose

Bootstrap's first-hour operation around the memory repository: it explains Agents Remember, records the developer's setup decisions, initializes settings and memory through their owning surfaces, verifies the result and names the Architect as the next step. Initial onboarding and the knowledge foundation are the Architect's regular work, not stages of this operation.

## Current account

The procedure has eight steps, each run through its owning surface on `agents-remember-task`: (1) explain what the setup changes, including that memory lives in a separate Git repository and that `memory.md` maps memory content to code commits; (2) establish context with `server_info` and `context_packet`; (3) record the spear branch as the memory repository's initial branch; (4) write the initial user settings once with `user_settings_init`, asking which harness each role should use from the harnesses this host runs, leaving model and effort unset, previewing with `dry_run=true`, writing and reading back, and reporting an existing settings file without overwriting, merging or completing it; (5) initialize or repair the memory root with `memory_init` after reading the install and onboarding guide (`docs/guides/onboard-existing-repo.md`) for the scaffold details; (6) read what the baseline will carry and author none of it, an absent `onboarding/` directory being expected; (7) adopt the first attributed baseline with `memory_baseline_adopt` after reading the Adopt Existing Memory guide (`docs/guides/adopt-existing-memory.md`), reading `memory_baseline_status` before and after and putting the drift decision to the developer; (8) read and report the knowledge foundation's state. The developer makes two initial decisions: the spear branch, and whether to scaffold a new memory repository or point to an existing one.

When a step returns a state the seat cannot name, it reads `reference/bootstrap/failure-states.md`, a step detail; before naming the next step it follows `reference/bootstrap/foundation-state.md#name-the-next-step`.

- The eight setup steps run through their owning surfaces, from explaining what the setup changes to reporting the knowledge foundation's state, with first baseline adoption at step 7. [2]
- Fresh setup orders settings, memory root, the baseline and then the Architect handover; onboarding and the foundation are later task work, not setup steps. [4]
- The authored source owns this contract; the distribution copy is not a separate authority. [5]
- The operation keeps all-role marking and named-step details. Setup reads and reports the knowledge foundation state; onboarding and foundation authoring belong to a later Architect task through the Curator route. [6]
- The operation keeps all-role marking and named-step details. Setup reads and reports the knowledge foundation state; onboarding and foundation authoring belong to a later Architect task through the Curator route. [7]
- The operation keeps all-role marking and named-step details. Setup reads and reports the knowledge foundation state; onboarding and foundation authoring belong to a later Architect task through the Curator route. [8]
- The operation keeps all-role marking and named-step details. Setup reads and reports the knowledge foundation state; onboarding and foundation authoring belong to a later Architect task through the Curator route. [9]
- The operation keeps all-role marking and named-step details. Setup reads and reports the knowledge foundation state; onboarding and foundation authoring belong to a later Architect task through the Curator route. [10]
- The step-8 handover in its own words: the knowledge foundation is the Curator's repository-foundation procedure (`skills/l-01-agent-lifecycles/reference/curator/repository-foundation.md`) run inside a task the Architect organises, and this seat reads its state — not-recorded, recorded at an exact identity, unusable, or a refused admission — reports it and authors no record. [11]

## Current composition and authoring contract

The only carrier is taskless Bootstrap, not a leaf seat. Workspace roots, setup state and developer decisions are inputs; missing task documents, briefs and contracts are normal, not gaps to fill. A working attributed installation is not re-entered for maintenance.

The operation is marked for all of its admitted roles (Bootstrap alone). The handover detail is `reference/bootstrap/foundation-state.md`, read before naming the next step, and the failure-state table is `reference/bootstrap/failure-states.md`, read only when a state cannot be named. Authority gates apply the boundaries in `roles/bootstrap.md`: no step orders this seat to write onboarding or knowledge, or to run a citation fixer. The order is settings → memory root → what the baseline carries → baseline → knowledge-foundation report → Architect handover, with no scaffold, fixer or provider stage.

The exit remains a durable surface-derived report: roots, branch, the user settings path and what the initialization did, the harness chosen per role, baseline commit, onboarding present as read or absent, recorded foundation identity or named absence state, and reasons for skipped steps. Its one named next step is the Architect, whose first regular work is the foundation: it opens a registered leaf under a master through the registered-leaf task route of the Curator's repository-foundation detail (`skills/l-01-agent-lifecycles/reference/curator/repository-foundation.md`), where the Curator creates, extends or resumes it; the seat hands over and stops and makes no claim that the foundation was completed. It is completion truth, never independent acceptance.

- The bootstrap carrier is taskless; its first message carries the compiled instructions, and a launch that cannot compile them reports its refusal. [1]


- The seat reads and reports the knowledge foundation but never authors records. [3]

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.
