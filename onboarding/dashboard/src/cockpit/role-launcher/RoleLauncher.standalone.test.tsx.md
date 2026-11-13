# dashboard/src/cockpit/role-launcher/RoleLauncher.standalone.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Focused mounted tests for the launcher's standalone-master selection: a manager or task crew names a master that no sprint commands, through the free launcher and through a document's “Launch role” binding.

## Code Commentary

The suite mounts the real `RoleLauncher` over one served tree holding a sprint → master → leaf branch and a master outside every sprint with its own leaf. It asserts that a manager, worker, reviewer or curator selection keeps the Master field available with no sprint, that the Sprint field's empty choice is “No sprint”, and that the master field then lists the standalone master; that the same selection for a sprint-commanded master still lists that sprint's own master and task; that a leaf task of the standalone master binds without a sprint; that the Orchestrator alone still needs a sprint before Start; and that `documentChatBinding` offers the admitted roles for the standalone master and its task while the unsupported selection names only the missing master relationship. Fixtures are consumer-authored TaskEntry values; the suite proves selection composition, not a live dashboard run or accepted landing.

## Boundaries

The mounted cases use supplied options and a mocked launch callback. They do not measure layout, start a native agent, or certify the dashboard build; the sandbox walk in the task evidence owns the end-to-end start.

## Evidence

- A standalone master is chosen with no sprint and the Master field offers it; a sprint-commanded master keeps its own master and task. 
- A leaf task of a standalone master binds without a sprint, and the Orchestrator alone still requires its sprint.
- The document binding admits the standalone master and its task, and the unsupported selection names only the missing master relationship.

The probe's paths and the sandbox walk are task evidence, not claims of a committed review or landing.
