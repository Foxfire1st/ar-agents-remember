# mcp/src/agents_remember/canvas/explainer_server.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The implementations behind the four kept tools: the three grade writes through the leaf's one lock, and `render`'s run in the workspace with the publication into the task's frame store.

## Code Commentary

- A grade needs the fingerprint the block's kind is defined by; a reference the bound comparison cannot fingerprint is answered `fingerprint-unavailable` and nothing is written, because a grade without a fingerprint could never be marked stale.
- `_leaf_lock` takes the leaf's one lock — `state/leaf`, the resource a build, an Update and a Retire hold — and answers busy when it cannot, so a grade write never lands beside a build that is rewriting the same store.
- `_held` reads the binding before the lock and again under it and re-checks the claim there, so a call made at a comparison the environment has left is refused `binding-moved` even though the seat was constructed while that binding was current; the early read also means a removed environment's refusal comes before any lock file is made.
- The one grade store per leaf lies with the task's records rather than in the workspace, which is why it outlives the workspace's removal; a server built without the task folder refuses `grades-unavailable` instead of writing elsewhere.
- `render_and_publish` renders the draft in `drafts/assets/` and publishes only when the task folder is known, the page loaded and the static readiness check passed; a refusal names its own reason in the report and the ready revision stays where it was.
- The run's whole report is filed in its own folder `renders/run-NNN/` beside `page.png` and `interactions/`, and its error list and summary are computed once into that report, so an answer that quotes them cannot disagree with the file.
- Publication is made under a request identity built from the page's own bytes and its coverage: rendering the same bytes again is the same draft and is answered `unchanged`, while a resumed run that reaches more is a successor revision that says so.
- Publishing copies the new revision into the workspace's `revisions/<n>/` at once and the answer says which folder was refreshed, so the workspace never states less than the task holds.
- A render with no interaction report records no passes and an incomplete coverage, so a revision says what was not checked rather than implying a coverage it does not have.
- `page_revision` answers the highest ready revision the leaf holds from the frames' ready pointers, skipping a symlinked or unreadable one, so a cancellation can say whether a revision appeared while it ran. The explainer surface is four tools - `render`, `define_category`, `remove_category` and `grade` - and no tool that reads the workspace back: an answer names files on disk and is bounded, so a long answer or a picture is written to the workspace and cited rather than returned in full.

## Evidence

- A block the bound comparison cannot fingerprint is refused and no partial grade is written [1]
- A grade write takes the leaf's one lock and refuses as busy rather than writing beside a build [2]
- The binding and the claim are re-read under the lock before a judgment is written [3]
- Publication happens only after the draft loaded and the readiness check passed, and a refusal leaves the ready revision untouched [6]
