# mcp/tests/test_knowledge_views.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

`KS-R20@v1` §1, §2, §3 and §6 as behaviour: the views, the classification, the bounding, and the mounted surface's own refusals.

## Code Commentary

The tests drive the source_context, invariant and family views over a converted tree and check refusal
of views outside the eleven admitted `knowledge_read` views (`source_context`, `invariant`, `family`,
`record`, `records`, `impact`, `search`, `weakness`, `dependent`, `writers`, `consolidation_proposal`)
before touching a tree. The view vocabulary, the closed rule registry and the ordering pass are pure
functions of their inputs. The mounted family is four operations over a memory tree (read, diff,
integrity check, write): no registered tool takes a database path, and `knowledge_change` and
`knowledge_project` left the registered set with the canonical database. `_RegistrationConfig`
provides `repositories: Mapping[str, Any] = MappingProxyType({})` to satisfy `McpRuntimeConfig`
without weakening production registration, and the registered `knowledge_read` input-schema assertion
covers all 24 admitted parameters (including KNO-L5's `masterId` and the eight KNO-R07 parameters
`compact`, `contractPath`, `files`, `folder`, `kinds`, `query`, `recordIds`, `repo_id`) while keeping
`databasePath` and `repositoryId` absent. The §6 cases drive the registered `knowledge_read`,
`knowledge_diff` and `knowledge_integrity_check` handlers through a real FastMCP server over a
converted memory tree, so those three operations execute rather than merely appearing in the roster;
`knowledge_write` is covered here as roster and schema — its name in the public roster and its
response model — not as an executed handler.

## Evidence

- The file realizes its current contract: eleven admitted `knowledge_read` views (including `consolidation_proposal`), four mounted tools, registered `knowledge_read` schema covering `masterId` and the eight KNO-R07 parameters with no `databasePath`/`repositoryId`, and read, diff and integrity executing through registered handlers. [1]
