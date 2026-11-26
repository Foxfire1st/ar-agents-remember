# mcp/test_support/agents_remember_test_support/testing/capsule_audience_fixtures.py

## Governing Overview

[overview](overview.md)

## Purpose

The module is a data-only registry of reviewed lifecycle-skill wording and byte pins for role-capsule audience and delivery checks. `mcp/tests/test_role_capsule_audiences.py` and `mcp/tests/test_l84_unique_detail_pointers.py` import it and own every compilation, identity and negative assertion.

## Code Commentary

The module defines no functions. Its tables hold:

- each role's reference-pointer actions as `(reference path, action prefix)` pairs, and the operation-level pointer actions per operation and role. Current knowledge-use prefixes address whole-record retrieval for the Worker, Curator, Reviewer and Investigator;

- retained historical SHA-256 tables for operation sources and per-role compiled stages, plus the role set each operation addresses;
- exact Curator clauses for message timing and content, the serving-stage boundary and semantic-scope fields;
- role pointer qualifications (the section anchor a role's action must target);
- rule clauses inlined into owning sections, short rules delivered in the shared digest with their recipients, removed short-rule actions, and grouped detail clauses whose one read covers several actions.

The expected recipients and retained hash tables describe a reviewed source snapshot. Current audience tests compare the compiled operation passage with its role-addressed source and derive ordinary detail-link counts from source. The retained D656 and v13 hash chain is not the current audience-test comparison.

The base source at `a2f0fced8896b92d31fd3f78351d01f5302be97e` held `ORDINARY_DETAIL_LINK_COUNTS`: expected counts of ordinary detail links per compiled `role/operation` stage. That fixed table is retired in this candidate. Current audience tests derive the expected link count from the selected source; the old table is not current comparison authority.

## Evidence

- Role pointer actions are pairs of reference path and action prefix. [1]


- Short rules delivered in the shared digest name their owner source, clause and recipient roles. [3]


- D656_OPERATION_SHA256 and D656_STAGE_SHA256 retain historical operation and stage hashes. [2]

- A grouped detail read names several actions and keeps their owner clauses. [4]


- The module is data only; consumer tests own compilation and assertions. [5]


- The current pointer fixtures bind `reference/knowledge/use.md` to compact table-row prefixes for Architect, Worker, Curator, Reviewer, and Investigator, with section qualifications for Architect and Investigator. [7]
