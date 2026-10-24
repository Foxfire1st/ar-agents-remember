# dashboard/src/tray/traySend.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Sends one immutable collection snapshot separately to each chosen target.

## Code Commentary

### Logic

Builds structured wire picks, reads image bytes, chooses a repository from page/reference/target context and posts one message per target; parses named delivered/held/refused results and settles only the snapshot IDs/text.

### Invariants And Boundaries

Held counts as sent and is never resent. One target refusal does not stop others. Missing image, invalid answer and network errors are explicit per-target refusals.


**L184 — INV-4DQMNE.** This parser is where a delivery's fields arrive from the server, so the reset has to survive here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence


Before a native send, sendTray separates archived/placeholder explainer targets from live recipients. The first archived target opens its leaf's first-request form with the current text; when no live target remains it returns without wiring picks or posting, preserving the collection. In a mixed selection, the remaining live targets still post and their ordinary settlement applies; this module does not report the first-request handoff as a delivered message. Mixed selections follow ordinary live-target settlement, which can consume the shared picks for successful live recipients.

- Before a native send, sendTray separates archived/placeholder explainer targets from live recipients. The first archived target opens its leaf's first-request form with the current text; when no live target remains it returns without wiring picks or posting, preserving the collection. In a mixed selection, the remaining live targets still post and their ordinary settlement applies; this module does not report the first-request handoff as a delivered message. Mixed selections follow ordinary live-target settlement, which can consume the shared picks for successful live recipients. [4]

- messageRepository chooses the message filing repository from the shown page, the first structured reference or the recipient’s task; it does not post or decide whether an archived explainer target is diverted. [1]

- parseDelivery accepts named delivered, held or refused answers and retains message-file identity, reason, detail and a supplied provider-limit reset without treating other answers as a delivery. [2]

- serverDetail reads a textual server detail or joins validation error locations and messages so a refused ordinary send retains the host’s stated reason. [3]
