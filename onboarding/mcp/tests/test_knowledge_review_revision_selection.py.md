# mcp/tests/test_knowledge_review_revision_selection.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Declare selected revision/head operands, display versions and side-specific recorded writers without inferring an owner from the reviewed leaf.

## Code Commentary

The original cases use text-backed test builders to create one retained revision on each side, invoke the shipped diff and exact selection helper, and check compared heads, a known-empty after removal and the composition payload own statements. _build_pair requires both counts to be1: these fixtures test neither sorted multi-revision populations nor predecessor traversal. Fixed STATEMENTS and projection-returned UUIDs give the assertions their identities.

The new display-version case checks r1 on both selected sides from the text index. It does not depend on a family roster or test a rendered browser meta line.

Writer tests use converted Git-tree worlds at revision2, explicit ar-history/v1 files and real canonical candidate resolution/compose_review. A carried changed row names its closed carrier owner, while before revision1 names its origin introduction. An open changed row owned by the reviewed leaf names that leaf. A no_impact row at revision2 yields not_recorded with no owners; it is not treated as authorship. An incomplete after index yields unavailable rather than no writer.

The small statement-pair fixtures use test-only row/revision builders, not production writer admission. The pane fixture creates and commits tiny disposable code trees with an explicit Git environment. Converted writer fixtures author their own history bytes before invoking production reads; they do not establish curation acceptance or a native host session.

## Invariants And Boundaries

These are source-declared assertions and controlled fixture construction, with no fresh execution claimed. The current eight declared test functions cover one revision per side, display version and four writer outcomes; they do not test conflicting duplicate writers, family guarantees, malformed arbitrary history or live browser chips. Existing support and lane declarations are selection/fixture ownership, not an execution verdict.

## Evidence

- Text-backed snapshot pairs require one retained revision per side and use projected identities. [35]
- One head pair and per-side r1 display versions are declared directly. [36]
- A known-empty after side remains a removal; real composition renders each selected operand. [37]
- Converted writer fixtures resolve the actual task and compose from explicit history files. [38]
- Carried and own changed rows name their writer while introduction names origin. [39]
- A no-impact row is not a writer, and incomplete history coverage stays unavailable. [40]
