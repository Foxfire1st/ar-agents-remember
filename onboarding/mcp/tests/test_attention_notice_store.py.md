# mcp/tests/test_attention_notice_store.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins the notice store's whole contract: one notice per native occurrence, the creation cut that decides what the
store publishes, the byte and count bounds over the exact serialized document, and the three observation states.

## Code Commentary

The occurrence cases pin one published notice per begun-and-confirmed occurrence, an exact retry adding nothing,
a begun intent announcing nothing, the three settle verdicts, an empty store publishing nothing while a reread
keeps what was confirmed, and the dismissal vocabulary admitting every kind this build publishes — the two
notices, the three live native causes and the four surviving operational kinds — while refusing a retired
spelling.

The cut cases pin the baseline the store is created with: a store created over existing terminal records
publishes none of them, a retained notice before the cut is excluded, a publication confirmed after the cut is
admitted even when its intent predates it — because the cut is never retaken — a notice confirmed before the
store existed cannot be invented later, a record published while the store is created is assigned exactly once,
a restart keeps the cut and its pending intents, and a missing store gets a new cut and replays nothing.

The bound cases measure the exact serialization the writer publishes: a fitting pending store is not shed, a
pending-only store of multibyte rows stays inside the byte cap, the byte cap sheds the oldest confirmed rows
before newer intents, a store at exactly the cap is kept while one more byte sheds the oldest, a shed intent
never becomes a notice, and the store keeps at most the newest bounded occurrences contiguously.

The state cases keep missing, empty and present distinct, an unreadable store never settled as empty, an
unreadable store quarantined and created again without replay, and an acknowledged notice surviving a torn store
while a later occurrence still arrives. The legacy cases pin a pending row persisting its native operation
identity and a store written before the cut adopting one cut.

### 20261023-L190-v2 The Vocabulary Admits Every Published Kind

The case name is the claim: `_case_test_every_published_kind_can_be_acknowledged` (:286-314) builds a record for
each of the nine published kinds, then requires `ValidationError` for three retired spellings. It pins the store's
vocabulary rather than the backend's acceptance — the acceptance path is pinned by
`mcp/tests/test_attention_dismissals_v2.py`.

## Evidence boundary

Source-level pytest cases at the reviewed freeze over a real store file with a pinned publication clock, not a
live-page witness and no measurement: MIK-R200 evidence item 6 is unrun and carried to L36, item 7 unrun.
