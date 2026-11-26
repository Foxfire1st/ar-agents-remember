# skills/l-01-agent-lifecycles/reference/message-handover.md

## Governing Overview

[overview](../overview.md)

## Purpose

Owns the message payload rule, full-store refusal handling, the location of filed messages and receipts, and single-turn step/wave continuation for the seven roles that send handovers.

## Code Commentary

Messages carry the request and artifact locations; files carry evidence and verdicts. A full-store refusal is recorded as pending, independent work continues, the message is resent once before the turn ends, and a second refusal is reported through the role's own route and left pending; held receipts and withdrawal of superseded held messages are governed by `core/authority.md`. Filing uses the narrowest shared task, and receipt searches preserve enclosure and transcript-root scope; delivery and turn end establish no semantic acceptance. Under `## Continue through steps and waves in one turn`, seats work step to step and wave to wave in one turn, collecting helpers' results, ending only at the verdict/handover, a named wait, or a nearly full context, and continuing admitted repairs, checks, and handover steps without waiting for a new Manager go (with an Investigator ending at its report, when no independent work remains, or at nearly full context).

## Evidence

- A message says what is asked or handed over and names its files; the full text goes in `body` and the files in `attach`. [1]

- A full-store refusal is recorded pending, resent once and, if refused again, reported through the role's route and left pending. [2]

- Filing and receipt searches use their actual shared-task and transcript scopes. [3]

- Held receipts and withdrawal of a superseded held message are governed by the shared authority file. [4]

- Seats continue step to step and wave to wave in one turn without waiting for a new Manager go, ending only at verdict/handover, a named wait, or nearly full context. [5]
