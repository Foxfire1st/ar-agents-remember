# mcp/src/agents_remember/application/skill_resources/operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/skill_resources/operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `../overview.md` |

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

## Docs References

No external documentation governs this internal application seam. The transport it serves is
specified by the MCP skills extension, cited on the package card. No relevant documentation found
after checking live sources.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The capsule entry point re-shapes the flat tool parameters into the enclosure selector the coordination layer accepts. | `role_capsule_compile_tool`; `CapsuleOperationRequest` | mcp/src/agents_remember/application/skill_resources/operation.py:39-52; mcp/src/agents_remember/application/skill_resources/operation.py:68-89 |
| The three skill entry points build one catalog, with the shipped corpus as the default and a caller-supplied tree as the test override. | `skill_catalog_list_tool`; `skill_catalog_read_tool`; `skill_catalog_registry`; `_catalog` | mcp/src/agents_remember/application/skill_resources/operation.py:92-95; mcp/src/agents_remember/application/skill_resources/operation.py:98-107; mcp/src/agents_remember/application/skill_resources/operation.py:110-113; mcp/src/agents_remember/application/skill_resources/operation.py:116-120 |
| Delivery refuses while any discovered skill is unreadable, checked before the read. | `require_servable` | mcp/src/agents_remember/application/skill_resources/catalog.py:104-114 |
| The request records both entry-point families take. | `SkillCatalogRequest`; `CapsuleOperationRequest` | mcp/src/agents_remember/application/skill_resources/operation.py:39-52; mcp/src/agents_remember/application/skill_resources/operation.py:55-65 |
| The frozen operation vocabulary the capsule request carries. | `CAPSULE_OPERATIONS` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-108 |
| The transport envelope these entry points' responses pass through. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/capsule_serving.py:19-19 |
| The consumer obligations recorded for a non-MCP caller of these entry points. | `CapsuleSourceSelectionRequest` | mcp/src/agents_remember/application/skill_resources/capsule.py:156-170 |
| The case that executes the discovery-registry-versus-body separation. | `test_the_discovery_registry_is_not_the_model_visible_catalog` | mcp/tests/test_capsule_serving.py:882-908 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `CAPSULE_OPERATIONS` repointed to mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-108. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T10:40:45+00:00: Generated citation repair: `CAPSULE_OPERATIONS` repointed to mcp/src/agents_remember/models/role_capsules/vocabulary.py:77-86. No content impact: mechanical anchor-range projection bound to citation source snapshot d000fd9192b3f076fd4f39e5e775a368dd70d71b172c679cb9d28176bdc33096; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T10:40:45+00:00: Generated citation repair: `test_the_discovery_registry_is_not_the_model_visible_catalog` repointed to mcp/tests/test_capsule_serving.py:882-908. No content impact: mechanical anchor-range projection bound to citation source snapshot d000fd9192b3f076fd4f39e5e775a368dd70d71b172c679cb9d28176bdc33096; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the two application
  entry-point families. Recorded the enclosure-admits / path-addresses split, the discovery-metadata-
  only listing contract, and the refuse-while-unreadable delivery gate that runs before any read.
  Verification metadata remains closeout-owned; no acceptance claim is made.
