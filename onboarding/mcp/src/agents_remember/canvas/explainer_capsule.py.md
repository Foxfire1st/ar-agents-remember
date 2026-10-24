# mcp/src/agents_remember/canvas/explainer_capsule.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The explainer's instructions, read once from the capability text an installed build ships, so a seat starts with the text it was promised or with a named reason it could not.

## Code Commentary

- `CAPABILITY` is the one capability word the settings role and the registered capability use for this seat's text, so the seat's name has a single spelling.
- `capability_text` reads through the loader that enforces the finite word budget and the clauses the capability may not lose, and it reads the generated copy an installed build ships rather than a checkout-only source file.
- A loader refusal becomes the seat's own typed refusal `capsule-unavailable`, so a build names why no seat could be instructed instead of starting one with no instructions.

## Evidence

- The seat's text is addressed by one capability word shared with the registered capability [1]
- The text is read through the loader that bounds its length and its required clauses [2]
- A loader refusal becomes the seat's own refusal instead of an uninstructed seat [3]
