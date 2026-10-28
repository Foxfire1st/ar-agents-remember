# mcp/src/agents_remember/mcp/registration/explainer_surface.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Selects the explainer's four tools on the normal AR task server from the launch-owned binding, and registers them for the one leaf that binding names.

## Code Commentary

- There is one server, not two: what makes a process an explainer seat is the binding the launch writes into its environment, and nothing else — a tool argument, repository text or a workspace marker cannot select the four.
- An absent binding is the ordinary roster only for a process that carries no launch marker; a marker without a binding refuses `explainer-binding-invalid`, because a lost binding must never fall open into the ordinary roster.
- An empty binding is refused on the same ground: an unset or empty binding is not a launch.
- The binding is validated as a whole: the required keys, the capability, the workspace whose repository, task and leaf it actually is, a generation that is a count from one upward, and — when a runtime config is supplied — the leaf's task folder, which must exist.
- A refusal at this boundary is answered with the explainer's own name: the authority error a wider build would raise for a root it cannot serve is the same fact as an invalid binding here.
- Registration resolves the task folder from the canonical `tasks/<repository>/<task>` path when that is a directory and from the configured root otherwise, then registers the four with the workspace, the seat and that folder; `binds_explainer` answers whether the process is bound without parsing the binding twice. The explainer surface is four tools - `render`, `define_category`, `remove_category` and `grade` - and no tool that reads the workspace back: an answer names files on disk and is bounded, so a long answer or a picture is written to the workspace and cited rather than returned in full.

## Evidence

- A binding that is present and wrong refuses service rather than falling back to the ordinary roster [1]
- Capability, required keys and the leaf's own task folder are checked before the surface is chosen [2]
- The workspace must be the environment of the leaf and repository the binding names [3]
- A generation is a count from one upward, never a string that could sort as one [4]
- The bound surface is registered for that leaf and no other [5]
