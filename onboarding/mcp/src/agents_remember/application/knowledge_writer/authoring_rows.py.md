# mcp/src/agents_remember/application/knowledge_writer/authoring_rows.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](../overview.md)

## Purpose

The writer's history-row authoring.

## Code Commentary

It validates and writes every judgment row kind -- invariant, family, onboarding trace, unexplained change, planned and reconsideration -- and fills each row's items, revisions and anchors.

## The Family Row Constructor (MIK-R48)

`HistoryRowAuthoring._family_row` is the single constructor
for family history rows: it resolves the candidate family record, stores that
record's own revision with the curator's authored effect label, and refuses
unsupported input (missing or invalid effect, curator-supplied revision, member
revision, effect on another disposition) before anything is written.

- One constructor stores the family revision with the authored effect. [2]

## Evidence

- The file realizes its current contract at the corrected candidate. [1]
