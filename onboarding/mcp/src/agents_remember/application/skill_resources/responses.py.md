# mcp/src/agents_remember/application/skill_resources/responses.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Builds the three wire responses the capsule and skill surfaces return. One place where compiled values
become the response contract, so the MCP adapter stays a registration layer and the payload shape has
a single definition. **Every field here is copied from a value an owner already produced** — nothing
in this module decides a selection, a permission or a trust level.

## Code Commentary

### Logic

- `role_capsule_response(outcome)` always sets `ok` and `explanation`; the remaining admitted facts
  (`role`, `seatAltitude`, `operationName`, `taskReference`, `taskDocumentDigest`, `repositoryId`,
  `workBranch`, `grantedTools`) are `None`/empty until a binding exists. On a refusal it also sets
  `refusalStatus` and `refusalNextAction`. `grantedTools` is the **sorted admitted policy**, which is
  why a caller can see the whole authorized surface even on a refusal that got as far as the binding.
- `_fill_manifest` (called in both shapes) fills `compositionOrder`, `instructionIdentities`,
  `conflictKinds` and `sources` from the compilation's diagnostic manifest, then — only when a result
  exists — `semanticDigest`, `instructions`, `skillReferences`, `requestedTools` and `taskContext`
  from the capsule. It returns early on `None` at either step, so a refusal keeps the manifest facts it
  does have and no fabricated capsule content.
- `skill_catalog_list_response(catalog)` renders discovery rows through `_entry_payload` and the
  recorded unreadable rows; it carries `indexUri` so a caller can find the well-known index resource.
- `skill_catalog_read_response(served, skill_revision=...)` renders one file. `skillRevision` is
  passed in rather than derived, because the entry's root revision and this file's revision are two
  different facts: on a supporting file they differ, and on `SKILL.md` they coincide. It refuses a
  non-UTF-8 body (`ValueError`), because an MCP text resource cannot carry it.
- `_entry_payload` renders a skill's `files` as **relative paths only** — the listing names files, it
  never carries their bytes.

### Conventions

Response construction is explicit keyword-by-keyword; there is no dictionary spreading and no
`model_dump` here. Refusal information travels in the same envelope as success information rather than
in a separate error type, which is what lets one response model serve both shapes.

### Invariants And Boundaries

- **`contentTrust` is a constant, not an input.** Every served skill file states
  `server-supplied-data`; no code path can set a trust level from content, and a resource read grants
  no tool permission. `M2` of the leaf's mutation probe targets the related guarantee on the grant
  side.
- **`declaredAllowedTools` is copied from the observed frontmatter and never applied.** A host MUST NOT
  honor a skill's tool declaration; the field exists so a reader that wants to refuse or gate the skill
  can see what it declared.
- **A refusal is not an empty success.** `ok` is false, a typed `refusalStatus` is present, and
  whatever was still true about the seat travels with it.
- This module reads no MCP types and formats no protocol output; it produces the strict `models`
  contracts that the transport envelope then carries.

### Todos

None recorded.

## Evidence

### Docs References

The trust statement this module stamps on every served file is the extension's own security posture:
skill content is server-supplied data, a host must not honor mechanisms declared in it, and a resource
read is not an activation.

- A declared tool set is an observation, never a permission channel. [1]
- Provenance travels with the bytes: origin, identity, this file's revision, and the trust statement. [2]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

### Repo-Internal References

- The response builders, and the admitted facts that are present in a refusal as well as a success. [3]
- A refusal keeps the manifest facts it has and never fabricates capsule content. [4]
- The listing names files and carries no body; `skillRevision` and this file's revision are two facts. [5]
- The trust statement every served file carries, as a constant rather than an input. [6]
- The strict response contracts these builders produce. [7]
- The case that executes the no-grant guarantee these builders render. [8]
- The case that executes the no-body-in-a-listing guarantee these builders render. [9]
- These builders serve this server's own tool surface; the extension's enumeration result is produced by the `skills/list` handler. [10]

### Cross-Repo References

No meaningful cross-repository reference applies.
