# dashboard/src/panels/detail-panel/taskEntries.recorded.l168.json

## Purpose

Native entry/body recording and explicit regeneration provenance.

## Code Commentary

recordedFrom names the prior source-document recording, its digest and read_task_sources + build_task_entries + read_task_document_body producer chain. optionalAbsent explicitly removes optional input review/status/header/step fields. Regenerated entries/bodies are not an old wire-envelope capture or fresh acceptance.

## Governing Overview

[Area overview](../overview.md)

## Evidence

- Implementation [1]
