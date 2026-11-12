# dashboard/src/panels/review/ReviewRefresh.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Render the reader’s explicit refresh action and the generation notice describing the comparison actually displayed.

## Code Commentary

A refresh re-reads the same task/subject question carrying the displayed comparison identity; it does not select a dataset or substitute a carried identity for the server’s resolved comparison. Whole-payload replacement and failed-read retention belong to the read-cycle owner.

`generationOf` first requires a reviewed answer, a carried digest, a shown payload and its binding digest. Otherwise it returns null and makes no currentness claim. Equality produces `current`; inequality produces `superseded`, with both identities named. A retained payload after a failed/refused read cannot by itself establish that the candidate is still current.

`ReviewRefresh` holds no local state or effects. The real button invokes `onRefresh` and then the separate task-entry revalidation callback, carries busy state and remains the reader’s explicit action. Without a provider that callback is a no-op. The notice is absent for null generation; otherwise its label, sentence and data attributes describe the displayed generation. A superseded notice says that the panes contain the current comparison, and names the moved previous input.

Button and notice are sibling items in the top line. The notice consumes a full-width row after the controls; above 40rem it ellipsizes with the full label and sentence in its tooltip, and on narrow pages it wraps inside the available width. The generation sentence keeps its semantic-content marker rather than becoming a separate closed disclosure.

The existing outcome tests declare same-question/carry identity, whole-generation notice agreement and failed-refresh retention checks. Their fixtures qualify those controlled paths; this card records no fresh test execution or native-host result.

## Invariants And Boundaries

Only an answered read can produce a generation claim. Both digest meanings come from the displayed payload and the identity that read carried. This component owns the control/sentence, while read sequencing, stale-response isolation and retained payloads belong to ReviewReadCycle/ReviewSurface and refusal rendering to the outcome owner. It starts no timer, polling loop or direct client request.

## Evidence

- The refresh action revalidates the entry and exposes a conditional, source-bound generation notice. [17]
- Only a reviewed carried comparison with a shown digest can make a current/superseded claim. [18]
- The notice takes its own responsive row and preserves the full tooltip sentence. [19]
- The caller supplies refresh, read phase and actual shown/carried identities. [20]
- The controlled outcome test declares same-question carry and DOM/generation agreement. [21]
- The failed-refresh case retains the old label and suppresses a generation claim. [22]
- Entry revalidation is local context with a no-op default. [23]
