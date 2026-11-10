# mcp/test_support/agents_remember_test_support/testing/capsule_audience_fixtures.py

## Governing Overview

[overview](overview.md)

## Purpose

The module is a data-only registry of reviewed lifecycle-skill wording and byte pins for role-capsule audience and delivery checks. `mcp/tests/test_role_capsule_audiences.py` and `mcp/tests/test_l84_unique_detail_pointers.py` import it and own every compilation, identity and negative assertion.

## Code Commentary

The module defines no functions. Its tables hold:

- each role's reference-pointer actions as `(reference path, action prefix)` pairs, and the operation-level pointer actions per operation and role;
- expected counts of ordinary detail links per compiled `role/operation` stage;
- SHA-256 pins of each operation source and each per-role compiled stage, plus the role set each operation addresses;
- exact Curator clauses for message timing and content, the serving-stage boundary and semantic-scope fields;
- role pointer qualifications (the section anchor a role's action must target);
- rule clauses inlined into owning sections, short rules delivered in the shared digest with their recipients, removed short-rule actions, and grouped detail clauses whose one read covers several actions.

The expected recipients and pins come from a reviewed source snapshot; tests do not derive them from current audience markers. The stage and operation pins are the end of a chain: `capsule_audience_v13_fixtures.py` first restores current bytes to these pinned bytes before comparison.

## Evidence

- Role pointer actions are pairs of reference path and action prefix. [1]

- Operation sources and per-role compiled stages carry SHA-256 pins. [2]

- Short rules delivered in the shared digest name their owner source, clause and recipient roles. [3]
- A grouped detail read names several actions and keeps their owner clauses. [4]
- The module is data only; consumer tests own compilation and assertions. [5]
