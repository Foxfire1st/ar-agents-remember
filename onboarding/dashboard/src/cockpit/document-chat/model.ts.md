# dashboard/src/cockpit/document-chat/model.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pure selection and record-reading model for the document chat: which roles a selection admits, which recorded agent matches a document, and how a record answer is read.

## Code Commentary

`documentChatBinding` walks the document tree with the launcher's own option helpers: nothing admits Architect and System Specialist, a sprint admits its Orchestrator, a sprint-commanded master admits its Manager, and a leaf of such a master admits Worker, Reviewer and Curator; every other selection admits none and names the missing relationship instead of offering a start. `documentChatAgent` matches the record labels to the exact document key, rejects archived records without a workspace, prefers an Architect only when it has no task reference, and takes the newest by creation time with the agent id as the stable tiebreak. `documentAgents` reads the declared record fields and rejects an answer that does not hold them.

## Evidence

- The binding returns exactly the roles the selection admits, or none with the missing-relationship reason. [1]
- The agent pick matches the document key, skips archived records and picks the newest stable record. [2]
- The reader validates the declared record fields instead of trusting an untyped answer. [3]
