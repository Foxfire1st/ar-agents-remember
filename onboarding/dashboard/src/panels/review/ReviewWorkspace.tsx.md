# dashboard/src/panels/review/ReviewWorkspace.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render a selected subject's own slot around its code, format the subject meta line and coordinate eligible selection focus with the tree's local scroll owner.

## Code Commentary

`SelectedSlot` uses SlotPlaceContext to draw content under the heading, details after code, or the whole read when no code follows. Only an answered current subject receives FamilyReviewCenter, marker-target note and main facts. Pending state shows that requested subject plus a skeleton whose first-read default is 12rem; failure/refusal carries the owner's labelled problem. An older comparison states that statement and judgment belong on the latest comparison and reads neither as this slot's answer.

`SubjectMeta` combines the known subject kind and location/proof populations with answered family context, numeric display revisions and an optional carried-change source chip. Recorded full context can name an invariant's families; confirmed no-family adds none. Partial/unavailable/not-read context gets a compact chip, with a published roster cursor usable when present. Display versions come from the relevant family guarantees or selected invariant rows/revision selection, never raw ID substitution. A moved revision with no own judgment/meaning step is labelled carried only when its recorded writer does not include this leaf; unavailable/unrecorded writers keep those distinctions.

`selectedContext` keeps a chosen family only among the supplied shown entries; rail callers can use the walked union while reading callers use the answer's own context. `walkedTreeOf` exposes retained families, exact last-read subject labels, notice and explicit no-context state. `rosterContinuation` pages directly only when the current payload includes that family; otherwise it asks the selection owner to select that family with the retained cursor. These helpers make no background reads.

`useSelectionFocus` ignores requests from a render at or before their recorded intent number, records a newly arrived answer and waits while pending. An eligible failed/refused selection lands focus once while retaining its request for retry. Answered selection consumes the request; scroll-only refresh waits for an answer and reveals without moving focus. Other landings occur only while focus is still on the selecting control or has fallen to body/null, then use preventScroll and reveal only inside the nearest tree panel. A marker target-state notice takes precedence over the current tree row; there is no page/reading-area scroll in this path.

## Evidence

- ReviewWorkspace.tsx current behavior at this source owner. [62]
- ReviewWorkspace.tsx current behavior at this source owner. [63]
- ReviewWorkspace.tsx current behavior at this source owner. [64]
- ReviewWorkspace.tsx current behavior at this source owner. [65]
- ReviewWorkspace.tsx current behavior at this source owner. [66]
