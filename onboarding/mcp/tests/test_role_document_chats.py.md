# mcp/tests/test_role_document_chats.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Focused route/reader tests cover correcting single-document discovery, pre-click tree discovery and first-start preparation on the shared stateful fake runtime; they do not contact a live host.

## Code Commentary

`DocumentChatReadTests` drives the real status test runtime: an exact started Projects request is read as itself rather than substituted with an Architect, archived or missing agents are filtered while the document workspace survives, and the Projects walk uses the last started live Architect while paging past old archived records. `FirstStartPreparationTests` covers the preparation owner through the role tools: a master that records its own folder as its parent is read but not fed back, so the enclosure nests under the sprint (MIK-R210 rule 4), while a recorded parent that names another folder is the folder the leaf nests under; a repeated request reuses the enclosure, preparation refusals keep the exact status/reason/repair on `role_start`, a masterless start reports `opened` without a creation guess, and the progress notice serves one request and is cleared through begin/starting/finish (the dispatcher's finally-path reclamation is separate source wiring).

`DocumentChatTreeTests` drives the registered tree endpoint with receipt files and shared runtime state: ordered document answers, one census through 256 selections, 422 above the bound, incomplete/away-host distinctions, own-document corruption isolation, repeated-path one-read reuse and accepted per-record/request byte limits. Padding tests show discarded launch payloads do not grow the retained projection. The single-document damaged-record case separately requires HTTP 409 rather than failure or no chat. Existing preparation and progress checks keep their scope, including the distinction between begin/starting/finish and dispatcher-finally wiring.

## Evidence


- The exact started Projects request is read without substituting an Architect; archived targets disappear. [1]


- Archival and missing-agent filtering keeps only live document agents. [2]

- The taskless walk uses the last started live Architect and pages older records. [3]
- A master recording its own folder as parent is read but not fed back — the enclosure nests under the sprint — and a repeated request reuses it. [9]
- A recorded parent that names another folder is the folder the leaf's enclosure nests under. [10]

- Refusals preserve the native status, reason and owner repair on the role_start answer. [5]


- A masterless start reports the opened Projects workspace without a creation guess. [6]


- The progress notice is single-request and cleared through begin/starting/finish by the cited test; the dispatcher's finally-path reclamation is separate source wiring. [7]


## Current contract evidence


- Focused route/reader tests cover correcting single-document discovery, pre-click tree discovery and first-start preparation on the shared stateful fake runtime; they do not contact a live host. [8]
