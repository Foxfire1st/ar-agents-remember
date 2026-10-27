# docs/tool-details.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

Long-form tool explanations shared with the packaged runtime documentation; the document is explanatory text, not the callable-signature owner.

## Code Commentary

The tool reference now states that skills are served from the package as MCP resources: `server_info` no longer reports `harnessSkillRoot`, `runtime_install` replaces the managed scaffold (`docs/` and the applicable `AGENTS.md` targets) and creates no installed skill tree, and the `role-capsules` experiment installs no skill copy in either mode. Host provisioning reads `paseoRuntime` from the active MCP authority file selected by `--config`, and this maintenance call never writes that authority. The citation-repair explanation refuses old-format memory and directs conversion or crossing sync before repair, instead of advertising source-snapshot acquisition and caller exclusion options. Converted repair still authors citation rows into sidecar references and re-records moved anchors. Named document selection scopes the operation to those cards; the full result remains in logged detail, rather than the inline status sample. The retained document-scoped repair explanation does not restore an `expected_snapshot` dependency. The document now also explains `citation_note_revision`: revising one reference's note in place under a `(sidecar path, references key)` identity, keeping every target, anchor and other reference unchanged, minting no number, and refusing a key the sidecar does not hold, a stale `base_digest`, an empty note and an operand outside the admitted memory tree; the publication guard judges anchors, not whether a note is true.

## Evidence

### Repo-Internal References








## Citation preview and concurrent calls

Citation repair keeps synchronous preview and writes, and adds background preview through the quality run registry. Its flat start call names the repository, optional candidate contract and optional document selection, with `mode="start", dry_run=true`; poll uses `mode="poll", run_id=...`, the same scope and no selectors. Capacity, run ownership, terminal eviction and worker-failure handling are shared with quality checks. The completed preview preserves the synchronous result apart from run state/identity. Background mode never applies repairs.

Synchronous tool bodies run off the event loop so other reads and polls can answer while they run. Potentially mutating synchronous calls keep one server-local ordering lock until the worker stops; existing asynchronous handlers retain their original path. This is not a blanket guarantee that every tool is side-effect-free or that a timeout cancels a worker.


- The reference publishes the flat preview modes beside the request-object quality modes. [2]


- The detailed contract describes shared preview runs and synchronous write ordering. [3]





- The source describes the current instructions summarized above. [1]
