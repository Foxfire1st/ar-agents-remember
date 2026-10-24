# mcp/src/agents_remember/mcp/registration/explainer_surface.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Selects the explainer's surface on the normal AR task server from the launch-owned binding, then registers the explainer's tools for the one leaf that binding names.

## Code Commentary

- There is one server, not two: what makes a process an explainer seat is the binding the launch writes into its environment, and nothing else — a tool argument, repository text or a workspace marker cannot select the surface.
- An absent binding is the ordinary roster only for a process that carries no launch marker; a marker without a binding refuses `explainer-binding-invalid`, because a lost binding must never fall open into ordinary unrestricted access.
- The binding is validated as a whole: the required keys, the capability, a generation that is a count from one upward, and a workspace whose repository, task and leaf it actually is; a disagreement is a forged or stale binding and does not become authority over another leaf.
- Registration binds the tools for the bound leaf only and defers the production report sender to the first report, so discovery stays light and does not load the bridge half.
- A call outside the surface is refused `explainer-tool-not-exposed` naming the tools the seat may call.

## Evidence

- A binding that is present and wrong refuses service rather than falling back to the ordinary roster [1]
- Capability, required keys and the leaf's own task folder are checked before the surface is chosen [2]
- The workspace must be the environment of the leaf and repository the binding names [3]
- A generation is a count from one upward, never a string that could sort as one [4]
- The bound surface is registered for that leaf and no other [5]
- A tool outside the surface is refused by name [6]
