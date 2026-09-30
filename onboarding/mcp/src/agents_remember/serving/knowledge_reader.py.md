# mcp/src/agents_remember/serving/knowledge_reader.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/knowledge_reader.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

**The knowledge reader's route (MIK-R29): `GET /api/knowledge/reader/{view}`, read-only views of a
repository's knowledge at any memory tree.** Transport only, like the reviewer routes: it takes the
repository (`repo`), the memory tree (`commit`: `published` by default, a memory commit, or `leaf:<scope>`) and
the view's subject (`path`, `id`, `census`, `locator` and `blob` for code, `continuation` for the next
`subtree` page), calls the port the composition root wires (`application/knowledge_reader`), and serializes
its answer once.

## Code Commentary

### Logic

- **Status codes.** Every typed answer is a 200 (a view, `not-converted`, `not-found`, `unavailable`, and a
  subtree `refused`), because each is a fact about the tree, not a transport failure. `invalid-request` is a
  400. Only a process composed without the port answers 503 with a named `unavailable` body and a next
  action, because then no answer exists at all.
- **The query.** `KnowledgeReaderQuery` carries one field per addressable subject; the application's
  `ReaderQuery` is this type, so the route never imports the application.
- **The port.** `KnowledgeReaderPort` is a plain callable from query to answer; `ServingCollaborators`
  carries it as `knowledge_reader`, and `create_app` registers the route after the review routes and before
  the greedy static mount.

### Conventions

- The handler takes one keyword per query parameter (`# noqa: PLR0913`), matching the reviewer routes.
- GET only; the route never writes.

### Invariants And Boundaries

- **The reader never writes a repository** (a candidate invariant recorded on the package entry card): the
  route is GET-only and only calls the port.
- A process without the port refuses by name (503), never with an empty view.
- Inert on the installed runtime until MIK-R37: the installed dashboard does not serve this route yet.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: 200 for typed answers, 400 for invalid requests, 503 unwired. | "Every typed answer is a 200" | mcp/src/agents_remember/serving/knowledge_reader.py:1-13 |
| The route path. | `KNOWLEDGE_READER_ROUTE` | mcp/src/agents_remember/serving/knowledge_reader.py:31-31 |
| One reader question, and the port type. | `KnowledgeReaderQuery`; `KnowledgeReaderPort` | mcp/src/agents_remember/serving/knowledge_reader.py:35-46; mcp/src/agents_remember/serving/knowledge_reader.py:49-49 |
| The GET handler: 503 unwired, 400 for `invalid-request`, 200 otherwise. | `register_knowledge_reader_route` | mcp/src/agents_remember/serving/knowledge_reader.py:61-93 |
| The collaborator field that carries the port. | "knowledge_reader: KnowledgeReaderPort" | mcp/src/agents_remember/serving/_app_common.py:510-510 |
| The registration in `create_app`. | "register_knowledge_reader_route(app, collaborators.knowledge_reader)" | mcp/src/agents_remember/serving/app.py:307-307 |
| The route cases: every view served, 503 unwired, nothing written; bad requests 400. | `test_the_route_serves_every_view_and_the_reader_writes_nothing`; `test_bad_requests_are_400_and_large_or_binary_code_is_a_bounded_notice` | mcp/tests/test_knowledge_reader.py:1092-1126; mcp/tests/test_knowledge_reader.py:1142-1182 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new route MIK-R29 adds, recording rulings 09:42:58 F3 and 10:44:14 F15 (a bad request answers 400 before any Git call) and the accepted open point that a subtree refusal is a typed 200. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
