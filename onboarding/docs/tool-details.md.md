# docs/tool-details.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

Long-form tool explanations shared with the packaged runtime documentation; the document is explanatory text, not the callable-signature owner.

## Code Commentary

The tool reference now states that skills are served from the package as MCP resources: `server_info` no longer reports `harnessSkillRoot`, `runtime_install` replaces the managed scaffold (`docs/` and the applicable `AGENTS.md` targets) and creates no installed skill tree, and the `role-capsules` experiment installs no skill copy in either mode. Host provisioning reads `paseoRuntime` from the active MCP authority file selected by `--config`, and this maintenance call never writes that authority. The citation-repair explanation refuses old-format memory and directs conversion or crossing sync before repair, instead of advertising source-snapshot acquisition and caller exclusion options. Converted repair still authors citation rows into sidecar references and re-records moved anchors. Named document selection scopes the operation to those cards; the full result remains in logged detail, rather than the inline status sample. The retained document-scoped repair explanation does not restore an `expected_snapshot` dependency. The document now also explains `citation_note_revision`: revising one reference's note in place under a `(sidecar path, references key)` identity, keeping every target, anchor and other reference unchanged, minting no number, and refusing a key the sidecar does not hold, a stale `base_digest`, an empty note and an operand outside the admitted memory tree; the publication guard judges anchors, not whether a note is true.

The document also explains three CLI commands. `knowledge-census` has two required subcommands: `inventory` writes `baseline.json` and `inventory.json` under `knowledge/census/ID/` of a converted memory working tree, pins the code and memory commits (both default to `HEAD`), selects code directories with repeatable `--scope`, refuses an unreadable baseline or an invalid census write and does not overwrite a completed census; `report` only reads the working tree or the selected `--revision` and prints measurements and route status (exit `0` success, `1` invalid census files or refused write, `2` unreadable inputs or baseline). `knowledge-copies` inventories copies of the retired knowledge database and unmanaged citation source indexes without deleting anything unless `--apply` is given with a `--reviewed` dry-run report from the same coordination root; a changed review digest or an unreadable controlling document refuses deletion, tracked files, managed citation indexes and active tasks' copies stay protected, and the result names deleted, kept and failed paths (exit `0` completed, `1` deletion failures, `2` invalid root or refused apply). `memory-backfill` plans code-attribution trailers for memory commit history from a required `--contract` and writes nothing by default; `--apply` needs `--expected-digest` from the reviewed plan and refuses a changed plan, keeps a rescue ref (default `refs/backup/memory-pre-migration`), checks every rewritten tree through the repository's commit-check runner and moves the named refs in one transaction, so a failed tree check moves no named ref (exit `0` nothing left or applied, `1` plan has work left, `2` refusal).

## Evidence

### Repo-Internal References








## Citation preview and concurrent calls

Citation repair keeps synchronous preview and writes, and adds background preview through the quality run registry. Its flat start call names the repository, optional candidate contract and optional document selection, with `mode="start", dry_run=true`; poll uses `mode="poll", run_id=...`, the same scope and no selectors. Capacity, run ownership, terminal eviction and worker-failure handling are shared with quality checks. The completed preview preserves the synchronous result apart from run state/identity. Background mode never applies repairs.

Synchronous tool bodies run off the event loop so other reads and polls can answer while they run. Potentially mutating synchronous calls keep one server-local ordering lock until the worker stops; existing asynchronous handlers retain their original path. This is not a blanket guarantee that every tool is side-effect-free or that a timeout cancels a worker.


Historical source account (detached from live reference 2; docs/reference/mcp-tools.md blob fb21b7c177ee42cdcd3cbdc8e1e9ee2acf7b8302):

- The reference publishes the flat preview modes beside the request-object quality modes.

- The public tool reference puts citation_fix flat sync/start/poll preview arguments beside the discriminated quality request and states leaf/official/pre-baseline scope boundaries.


- The detailed contract describes shared preview runs and synchronous write ordering. [3]





- The source describes the current instructions summarized above. [1]

- The public tool reference puts citation_fix flat sync/start/poll preview arguments beside the discriminated quality request and states leaf/official/pre-baseline scope boundaries. [2]
