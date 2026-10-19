# docs/design/canvas-kit.md

## Governing Overview

[governing route overview](overview.md)

## Purpose

The design of record for the pinned offline presentation kit (MIK-R104 rule 13): which libraries ship, under which licences, how a page loads them from an admitted revision, what is deliberately not shipped, how the manifest is verified, and which limits remain.

## Code Commentary

- The entries section names each pinned library with its version and the licence read for it, which is the inventory the manifest carries and the host verifies.
- The licence readings record that every dependency inside a bundle has its own text beside it, so a page's rendering libraries are traceable to licence terms.
- How a page loads the kit is stated as product behaviour: a page names a kit file by its contract path inside its own revision, and the bytes are compared with the manifest when the file is carried into an attempt; nothing refuses a kit path later, so a presenter may publish its own bytes there.
- The "what is not shipped" section is the honest half: no package manager, no network fetch, no second copy of a library the page could substitute.
- Verification and known limits name the manifest's size-and-digest accounting at carry, that no later check refuses a kit path, and the fact that the kit is product data rather than a container.

## Evidence

- The kit's entries and their licences are stated once as the inventory the manifest verifies. [1]
- A page loads a kit file from its own admitted revision, its bytes compared with the manifest when carried and refused by no later check. [2]
- What is deliberately not shipped is named rather than implied. [3]
- The remaining limits are stated, so the kit is not read as a container. [4]
