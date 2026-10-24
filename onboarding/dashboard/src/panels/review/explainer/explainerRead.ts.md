# dashboard/src/panels/review/explainer/explainerRead.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The explanation view's single read and its presses — state, retained revisions, Update, selective regeneration and removal — plus the resolution of a claim link or a frame's evidence destination to a native review selection.

## Code Commentary

- Opening the view reads the state and the retained revisions together and nothing else; a failed read becomes a named problem, and an answer for a replaced or unmounted read is dropped.
- The two reads share one sequence token, so an older answer can never overwrite a newer one.
- Update re-reads after it answers and clears the moved frame; a press that answered nothing is reported as unreachable rather than as success.
- Regeneration keeps one request id per identical press and re-reads after it succeeds, and a refusal becomes the view's named problem.
- A moved stream event writes its notice into the held state, and a cleared event clears it without re-reading.
- A claim or an evidence destination resolves only against the comparison on screen, and an unresolved reference yields no selection rather than a guess.

## Evidence

- The two reads drop stale answers by sequence and take a moved event into the held state [1]
- Only the newest answer for a mounted view is allowed to land [2]
- Update and removal report a named refusal and re-read after every press [3]
- An identical regeneration press reuses its request id, and a success re-reads [4]
- A claim link resolves to a location, hunk or subject selection, or to nothing [5]
- A frame's evidence destination resolves only against the shown comparison [6]
