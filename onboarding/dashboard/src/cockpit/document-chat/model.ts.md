# dashboard/src/cockpit/document-chat/model.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Pure selection and record-reading model for the document chat: which roles a selection admits, which recorded agent matches a document, and how a record answer is read.

## Code Commentary

`documentBindings` indexes served entries by entry.key and follows their ordered children to emit canonical sprint, master and leaf selections. It does not reconstruct topology from document/series joins. `bindingInTree` resolves an exact reference or names the missing relationship; Projects and explicit Investigator admission retain their existing owners.

`documentChatAgent` matches canonical labels to the exact selected document, rejects archival/missing workspace, excludes Investigator and system-specialist from primary discovery, and chooses newest creation time with stable agent-ID tiebreak. `documentAgents` returns null for an unreadable answer, distinct from an empty confirmed array. The same bindings feed both batch preknowledge and fresh selected-document reads.
## Evidence



- The reader validates the declared record fields instead of trusting an untyped answer. [3]

## Investigator scope and request identity

Projects, sprint, commanded master and leaf roles retain explicit selection admission. Investigator is an additional explicit sprint/master launch choice, with leaf refusal and its own request identity; default documentChatAgent continues to select the Manager or Orchestrator rather than an Investigator.



- The current source implements this file’s stated Investigator boundary. [4]



## Refreshed current evidence


- An unsupported selection admits no start, and the ordinary Projects selection keeps its own role set. [5]


- The agent pick matches the document key, skips archived records and picks the newest stable record. [2]
