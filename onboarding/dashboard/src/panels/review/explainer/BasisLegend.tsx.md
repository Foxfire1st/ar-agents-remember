# dashboard/src/panels/review/explainer/BasisLegend.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Draws the claim-basis legend and the revision's claim map beside the explanation page, so every claim's basis can be checked without trusting anything the page draws for itself.

## Code Commentary

- The legend and the chips take their labels from one registry in the model, so the four bases — recorded fact, mechanical signal, inference and intended — cannot drift apart.
- `ClaimChip` colours one basis and states its name; the bar lists all four with their meanings, and inference is marked as inference.
- `ClaimList` groups the revision's claims by the product-written part map, one block per part, and a part with no claims draws nothing.
- A revision that returned no claim map renders one sentence saying so, rather than an empty list.
- A claim's link is a button that hands the block identity to the page's selection owner; this module opens nothing itself.

## Evidence

- The legend names all four bases, each with its meaning, from one registry [1]
- Every basis has its own chip class, so a basis cannot render without its own mark [2]
- A chip states its basis name and carries it as an attribute [3]
- The claim map is listed part by part, and a missing map is stated instead of drawn empty [4]
