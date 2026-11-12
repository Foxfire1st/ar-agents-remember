# mcp/tests/test_knowledge_views.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

`KS-R20@v1` §1, §2, §3 and §6 as behaviour: the views, the classification, the bounding, and the mounted surface's own refusals.

## Code Commentary

The tests drive the source_context, invariant and family views over a converted tree — since MIK-R118
the admitted set is six (`source_context`, `invariant`, `family`, `record`, `weakness`, `dependent`),
and a view outside it is refused before it touches a tree. The view vocabulary, the closed rule
registry and the ordering pass are pure functions of their inputs. The mounted family is four
operations over a memory tree (read, diff, integrity check, write): no registered tool takes a
database path, and `knowledge_change` and `knowledge_project` left the registered set with the
canonical database. The §6 cases drive the registered `knowledge_read`, `knowledge_diff` and `knowledge_integrity_check`
handlers through a real FastMCP server over a converted memory tree, so those three operations execute
rather than merely appearing in the roster; `knowledge_write` is covered here as roster and schema — its
name in the public roster and its response model — not as an executed handler.

## Evidence

- The file realizes its current contract at the corrected candidate: six admitted views, four mounted names, and read, diff and integrity executing through the registered handlers. [1]
