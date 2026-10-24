# mcp/src/agents_remember/canvas/explainer_server.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The seat's tool-server surface: the kept authoring tools, the read surfaces, the two writes the seat adds — its judgment and its report — and the publication path back into the frame store.

## Code Commentary

- `ExplainerJudgment.grade` needs a fingerprint from the product for every block it names; a reference the bound comparison cannot fingerprint is answered as `fingerprint-unavailable` and nothing is written, because a grade without a fingerprint could never go stale.
- `_leaf_lock` takes the same leaf lock a build, an Update and a Retire hold, and answers `explainer-busy` when it cannot, so a grade write never overwrites a store that a build is rewriting at the same moment.
- `_held` re-reads the binding under that lock and re-checks the claim, so a grade made at a comparison the environment has left is refused even though the seat held a valid binding when it was constructed.
- `report` copies the developer's selections and words byte for byte from the developer's filed tray message and takes no argument for them; a second report for the same tray message is refused `already-reported`.
- `_deliver` sends only to the architect the master-to-architect record names, which this module reads and never writes, and keeps the report back for the developer's tray when that record names no seat.
- `render_and_publish` publishes only when the rendered draft loaded and the static readiness check passed; a refusal is reported with its own reason and the previous ready revision stays where it was.

## Evidence

- A block the bound comparison cannot fingerprint is refused and no partial grade is written [1]
- A grade write takes the leaf's one lock and refuses as busy rather than writing beside a build [2]
- The binding and the claim are re-read under the lock before a judgment is written [3]
- One report per filed tray message, with the developer's words copied byte for byte and their digests answered [4]
- A report with no recorded architect goes back to the developer's tray instead of to a seat that would not receive it [5]
- Publication happens only after the draft loaded and the readiness check passed, and a refusal leaves the ready revision untouched [6]
