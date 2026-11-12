# mcp/tests/test_task_authoring_templates.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves task-authoring boundaries at their existing model owners: multi-paragraph prose in leaf and master task documents survives rendering, a master takes examples as freeform sections and refuses the leaf-only `codeExamplesNote`, and the shipped requirement-packet template keeps every heading the packet parser injects.

## Code Commentary

The document cases validate `TaskDocument` models of kind `subTask` and `master` and render them with `render_markdown`: objective, design and a freeform section keep both paragraphs under their headings, non-goals and acceptance appear, and rendering is deterministic. A master with `codeExamplesNote` fails validation with "a master document has no steps, codeExamples", while a leaf renders the note under "Proposed Code Examples". The packet case parses `skills/l-01-agent-lifecycles/templates/requirement-packet.md` with `parse_packet` and finds a non-empty section for every role in `INJECTED_PACKET_ROLES`; renaming the "Expected Evidence" heading drops only that role and leaves the others unchanged. These are model and template checks, not authored-task or tool-call evidence.

## Evidence

- Rich leaf and master prose survives rendering [1]
- Master examples are freeform prose and the leaf absence field is refused on a master [2]
- The packet template retains every parsed obligation heading [3]
- The injected packet roles [4]
