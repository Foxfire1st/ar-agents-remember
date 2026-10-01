# mcp/src/agents_remember/application/skill_resources/operation.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The **application entry points** for the capsule operation and the skill surface. The MCP
registration layer calls these; each one validates its typed request, composes the owner that decides
the answer, and returns the response contract the wire declares. Nothing here formats protocol output
or reads MCP types — that is the `mcp` layer's job.

This is also the seam a non-MCP consumer uses: a sibling leaf or an internal caller can import these
three functions instead of going through the tool payloads.

## Code Commentary

### Logic

- `CapsuleOperationRequest` is a flat typed record: `enclosure_contract_path`, `task_path`, `role`,
  `operation`, and an optional `code_repository_root`. The enclosure and the task path are separate
  because the enclosure **admits the seat** while the task path is what the seat is **addressed at**;
  the task layer resolves the reference key from the enclosure's own repository identity.
- `role_capsule_compile_tool(config, request, *, sources=None)` builds the enclosure selector and the
  `CapsuleCompileRequest`, delegates to `compile_task_capsule`, and renders the outcome through
  `role_capsule_response`. Note that the registered tool's four flat parameters are re-shaped here
  into `EnclosureSelector(contract_path=...)` — the wire never sees an enclosure object.
- `SkillCatalogRequest(origin, root)` defaults both halves to the shipped corpus. A caller supplies
  them only to serve a different tree, which is how the test module drives a synthetic corpus without
  touching the shipped one.
- `skill_catalog_list_tool`, `skill_catalog_read_tool` and `skill_catalog_registry` all build the
  catalog through one private `_catalog(request)`: it opens `shipped_skill_tree()` and substitutes a
  caller-supplied root when one is given, so the shipped default and the test override take the same
  path. `skill_catalog_read_tool` calls `require_servable` **before** reading, so a tree with an
  unreadable skill refuses delivery rather than serving the rest.

### Conventions

Both entry-point families return the strict response contract rather than a dict; the payload builders
in `mcp/tools/capsule_serving.py` add the transport envelope. `unreadable_skills` is re-exported here
even though it is defined in `catalog.py`, because the application boundary is where a consumer looks
for it.

### Invariants And Boundaries

- **`skill_catalog_list_tool` carries discovery metadata only.** The listing returns no body; a caller
  that wants content must make a second, selected call. `M3` of the leaf's mutation probe injects
  bodies into the listing and the dedicated case fails.
- **Reading refuses while any discovered skill is unreadable.** The gate is `require_servable`, not a
  per-skill try/except, so a tree edit that breaks one skill is visible instead of partially served.
- The `origin`/`root` pair travels together: supplying a root without its origin is what makes two
  servers serving one skill name collapse into one identity.
- No formatting, no protocol types, no permission decision lives here.

### Todos

None recorded.

## Evidence

### Docs References

No external documentation governs this internal application seam. The transport it serves is
specified by the MCP skills extension, cited on the package card. No relevant documentation found
after checking live sources.

### Repo-Internal References

- The capsule entry point re-shapes the flat tool parameters into the enclosure selector the coordination layer accepts. [1]
- The three skill entry points build one catalog, with the shipped corpus as the default and a caller-supplied tree as the test override. [2]
- Delivery refuses while any discovered skill is unreadable, checked before the read. [3]
- The request records both entry-point families take. [4]
- The frozen operation vocabulary the capsule request carries. [5]
- The transport envelope these entry points' responses pass through. [6]
- The consumer obligations recorded for a non-MCP caller of these entry points. [7]
- The case that executes the discovery-registry-versus-body separation. [8]

### Cross-Repo References

No meaningful cross-repository reference applies.
