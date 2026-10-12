# dashboard/src/panels/lifecycle-list/rowState.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure presentation facts for one Operations row: the mark, single priority word, need band, numeric progress and complete hover text.

## Code Commentary

A lifecycle inferred without any last event is not a report of pause: the document status speaks, or waiting when no document exists. Reported lifecycles speak their own state and eligible age; completed and abandoned states use document-style marks. askingWord handles only outside attention: gate, overdue inbox, pending acknowledgment, then chat needing input. rowWord consumes that result, then gives a band-zero asking/blocked state precedence, then a working chat, and finally the state text with an eligible age. A gate never consumes independent overdue inbox dismissal. Hover text preserves every signal, original lifecycle facts, document status and abandoned/discarded progress even when the compact line omits them. Short IDs are derived from an exact master-folder/id prefix, not guessed filename numbering.

## Evidence

- State and priority are derived without mutating lifecycle, document, inbox or chat state. [1]


- Outside attention is selected by askingWord; rowWord owns the remaining state and working-chat choices. [2]
