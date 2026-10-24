# dashboard/src/panels/review/explainer/RevisionSelector.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Lists the retained revisions with their binding, time and kind, marks the agreed pinned one, offers Compare, and offers the one removal control solely when the task total refused a new revision.

## Code Commentary

- Each row shows the binding label, the time in the reader's own clock, the kind and its focus, and the revision number; a removed revision stays as a disabled receipt rather than disappearing.
- Compare is enabled only while two retained revisions exist and no press is running; when it is on, its label names both bindings and a second press stops comparing.
- A refusal is stated with its name first; only the task total's refusal offers removal, and any other refusal says removing others would not help and offers nothing.
- The removal choices list only unpinned revisions, so the agreed page is never offered, and a set with no unpinned revision says nothing may be removed.
- Selecting a revision only reports the choice upward, and removal only reports the ticked numbers; the selector reads and writes nothing itself.

## Evidence

- The selector states the agreed revision, lists every retained row and hands both presses upward [1]
- A row carries its binding, kind, time, pin and removal state, and a removed revision cannot be shown again [2]
- Compare needs two retained revisions and switches between starting and stopping the pair [3]
- Only the task total's refusal offers removal; another refusal says why removal would not help [4]
- The removal list never contains the pinned revision and says so when nothing may be removed [5]
