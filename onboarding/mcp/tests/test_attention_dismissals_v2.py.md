# mcp/tests/test_attention_dismissals_v2.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins MIK-R200@v2 rules 7 and 2a end to end over the real projection pass and the real acknowledgement store: one acknowledgement hides one occurrence, it survives a page reload and a service restart, it leaves exactly when its own occurrence ends, and the queue lists the newest entry first.

## Code Commentary

The permission case drives one unanswered prompt through `ProjectionInputState` — a fresh instance is what a service restart leaves behind — and requires the row to be published, acknowledged, gone on the next pass and still gone after the restart, with the prompt still unanswered and the record still stored; answering it reclaims the record and publishes the second prompt under its own id (`test_attention_dismissals_v2.py:255-299`). The held case is the same shape over the real held store: the message is still held while hidden, the record leaves when the store drops the message, and a later message is a new row (`:302-340`).

The stall case is the interval one. The deadline passes on the reader's own watch, the published id carries the turn-end stamp the host publication gave (`:359`), a restart still derives that stamp, and dismissing leaves the task's stage, its seats and its document untouched; a bound turn reclaims the record, and the next idle interval is published under the later stamp (`:343-397`). The notice and abandonment cases pin that a notice's record leaves when the bounded store drops the occurrence, that a distinct occurrence is published again, and that an abandonment changes neither the task entry nor the notice store (`:400-464`).

The backend case passes every published row through `evaluate_action` and requires 202 with the row's own kind and a `DismissalIntent` of that kind, 404 `unknown-item` for an id the projection does not publish, and 400 `item-kind-mismatch` for a mismatched kind — there is no dismissibility refusal left to hit (`:467-527`). The bound cases fill the store past `MAX_DISMISSALS` and past `MAX_DISMISSAL_BYTES` with long multibyte identities, then assert the kept count, the rows that left, and that the written document is inside the byte cap (`:533-573`); a `dismiss` that raises leaves the occurrence published (`:576-601`). The ordering case asserts the newest-first list, that an entry without an age counts as zero and sorts by id among the zero-age rows, and that an age-only tick re-orders nothing (`:607-647`).

## Evidence boundary

Source-level pytest cases at the reviewed freeze over real coordination and observer files the product itself writes, through the real pass, store and action evaluator — not a live-page witness and no measurement: the page witnesses of MIK-R200@v2 Expected Evidence 5–6 and the installed check are unrun here, and evidence item 7 (CPU/resource) is unrun.
