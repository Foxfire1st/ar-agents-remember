# mcp/src/agents_remember/serving/knowledge_reader.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: 200 for typed answers, 400 for invalid requests, 503 unwired. [1]
- The route path. [2]
- One reader question, and the port type. [3]
- The GET handler: 503 unwired, 400 for `invalid-request`, 200 otherwise. [4]
- The collaborator field that carries the port. [5]
- The registration in `create_app`. [6]
- The route cases: every view served, 503 unwired, nothing written; bad requests 400. [7]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
