# mcp/src/agents_remember/cli/knowledge_copies.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

CLI adapter for the leftover-copy cleanup.

## Code Commentary

`knowledge-copies` plans or applies MIK-R26 rule 6: it lists every knowledge-schema copy under a coordination root with the rule that decides it, and applies exactly the reviewed dry run. Under MIK-R82 it also applies the completed-task rule (rule 2: copies under the notes of a `Completed` or `abandoned` task delete) and the citation-slot rule (rule 3: unmanaged citation source indexes list and delete with their slot directories).

## Evidence


- The file realizes its current contract at the corrected candidate. [1]
