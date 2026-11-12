# mcp/src/agents_remember/mcp/registration/knowledge.py

## Governing Overview

[mcp/registration route overview](overview.md)

## Current operative account — MIK-R109

`register_knowledge_tools(server, config)` registers read, diff, integrity and write in that order: `_register_knowledge_write` mounts `knowledge_write`, the writer's own route — the same function the CLI write commands run — beside the reader. The mounted read's description names both public writer commands, `agents-remember knowledge-ingest` and `agents-remember knowledge-bootstrap`, inside the unchanged 600-character description bound. Read rows are text ID, record kind, computed state and memory-file location; those of the tree and record views carry no record prose, while the two marks views hold what MIK-R118 rule 6 and MIK-R124 rule 7 name — a weakness row its one-sentence statement and measurement, a dependent row the document and the links that moved. Read admits six views: `source_context`, `invariant`, `family`, `record`, `weakness` and `dependent`, with `recordId` taking any record's text ID (`INV-…`, `WKN-…`, `DPD-…`) and the mark filters `sourcePath`, `weaknessKind`, `includeClosed`, `staleOnly` and `standsOn` forwarded unread. Paging and the internal family-complete selection remain, while mounted `read_ar_files` no longer supplies a matching inline manifest or continuation. `_worktree_relative_locations` compares the requested root with configured memory checkouts: non-configured roots use memoryRoot-relative row files, configured/no-config roots use absolute files; the payload includes commit/dirtiness provenance. Both read and diff registrars now receive config: read uses workspace/cache/location mode; diff uses coordination_root for the full comparison report. `knowledge_diff` answers compared trees, change counts, bounded decision record names/count and report location, not patches. The rich comparison remains available to the dashboard reviewer. Integrity remains the converted-tree validator and persisted leaf-worklist read; change/project remain unregistered. Handler argument forwarding and record/anchor semantics remain with their domain owners; the registration's location-mode helper is real local policy, not a new dataset selector.

## Current source contract evidence

- The current candidate source supports the operative account — the four registrations and the mounted read's description naming both public writer commands — while the historical sections grant no current tool or execution acceptance.

## Historical original card — all remaining original prose and evidence are non-operative

The complete original account below, including Purpose, Commentary, invariants, dated notes and evidence captions, is retained only for custody. It grants no current callable tool, inline-text result, session deduplication, database read or execution acceptance.

## Purpose

The knowledge operation family module: the one `register_knowledge_tools(server, config)` that declares its family against the server it is handed and delegates every operation to the payload builders in `agents_remember.mcp.tools.knowledge`. It is "**appended** to `TOOL_REGISTRARS`, never inserted: FastMCP publishes tools in registration order, so every existing name keeps the position it was advertised at." **It declares four operations: `knowledge_read`, `knowledge_diff`, `knowledge_integrity_check` and `knowledge_write`,** through `_register_knowledge_read`, `_register_knowledge_diff`, `_register_knowledge_integrity_check` and `_register_knowledge_write`. **`knowledge_change` and `knowledge_project` are no longer registered**: `knowledge_write` is the write plane's mounted route and runs the same file writer as the CLI, and no projection renderer is registered. It deliberately performs no domain reasoning, holds no state, validates nothing itself and opens no dataset; the runtime configuration supplies it the workspace root a read falls back to when the caller names no repository, and the coordination root.

**Historical (retired by MIK-R26).** The earlier five-operation description below — including the registrars for `knowledge_change` and `knowledge_project` and their dataset-selection routes — is retained as the record of the removed registrations; the current module's four registrars are those named above.

## Code Commentary

Knowledge read/write/diff/integrity handlers resolve the existing request classes and payload builders through the lazy tools adapter at call time. No second writer or schema is introduced.

### Logic

**One entry point, four private registrar functions, called in declared order.** `register_knowledge_tools(server, config)` is the family's whole public surface, and its body is the four calls `_register_knowledge_read(server, config)`, `_register_knowledge_diff(server)`, `_register_knowledge_integrity_check(server)` and `_register_knowledge_write(server, config)` — read, then diff, then integrity, then write. The read and write registrars take the config, because each resolves recorded source anchors and memory trees through it; the diff and integrity registrars take the server alone, which is the call shape making that boundary visible. The package docstring's rule that a family module's `_register_*` calls are never reordered applies here with the same force as `TOOL_REGISTRARS` itself.

**Each handler validates its wire request, delegates, and returns the typed shape the response model declares.** Every `@server.tool()` body is one construction of a request value object from the flat keyword arguments followed by one call into `mcp/tools/knowledge.py`: `knowledge_read` builds a `ReadToolRequest`, `knowledge_diff` a `DiffToolRequest`. `knowledge_integrity_check` builds an `IntegrityCheckRequest` too, since MIK-R08 (before that it was the one handler whose builder took keyword arguments directly). No handler computes a classification, infers an effect label, authors a draft or judges a rationale — the module docstring says the surface "performs no domain reasoning", and the code shape is what makes that true rather than aspirational.

**The published docstrings are the operations' own contracts.** `knowledge_read` names the three views, attributed records, unresolved limitations and the optional `sourcePath` seed forwarded into `ReadToolRequest.source_path`. `knowledge_diff` returns the knowledge files' Git diff with grouped patches and no inferred semantic effect label. `knowledge_integrity_check` returns the converted-tree validator's counts and bounded violations, plus a leaf's persisted change-to-knowledge worklist when `contractPath` is named. The old recorded-run selectors `runId`/`inputDigest`, dataset pair and `compatible` response field do not survive on this registered surface (MIK-R26).

**Only the read registrar consumes runtime configuration.** It forwards the caller's `repositoryRoot` unchanged and supplies `workspace_root` separately as the default repository, alongside `coordination_root` for the derived-index cache. The builder completes a source-resolution pair or names neither half; this registrar does not substitute a root without a code tree. The caller names the converted memory tree with `memoryRoot`, never `databasePath` or a caller-selected index namespace. Diff and integrity take the server alone. The removed `knowledge_change` and `knowledge_project` registrations remain historical only; their authoring route is the CLI file writer, not a refusing mounted tool.

**The three operations are the interface another leaf mounts, and the reviewer surface is not here.** The Intent Reviewer, its cockpit route and its browser client belong to `KS-R22@v1`; this module declares no FastMCP resource, no route, no panel and no client, and its only MCP effect is the three `@server.tool()` registrations.

**The registration order is part of the advertised contract, and this family is appended at the tail.** The roster tail order and the registry tail order record the same decision as the handler order rather than independent choices.

### Conventions

The family module follows the package door's contract exactly: one `register_*_tools(server, config)` public function, one private `_register_*` per operation, and every `@server.tool()` definition inside a private registrar — the shape `registration/__init__.py`'s docstring declares for every family module. Requests are assembled by importing the request value objects from the builders module rather than by re-declaring their fields here, so the wire argument names are spelled once in `mcp/tools/knowledge.py` and this module only maps them onto the value objects. The three published docstrings are the contract carriers — each names what its operation returns and what it refuses to produce — and no module-level constant, `__all__` or helper exists beyond the four functions, so the file's whole surface is the family declaration itself.

### Invariants And Boundaries

- **The family is appended, never inserted.** `register_knowledge_tools` is the last entry of `TOOL_REGISTRARS`, so no existing tool's advertised registration position moved when this family was mounted.
- **The registration order is read, diff, integrity.** The three `_register_*` calls in the entry point appear in that order, matching the roster tail and the registry tail.
- **The surface performs no domain reasoning.** Every handler validates its wire request, delegates to a payload builder and returns; no classification, effect label, draft, rationale judgement or compatibility verdict is produced here.
- **The runtime configuration supplies two values, and neither selects a dataset.** The read registrar hands
  the workspace root over as the read builder's `workspace_root=` default repository and the coordination root over as `coordination_root=`, the cache location for a
  converted memory tree's derived index. The diff and integrity registrars take the server alone.
- **A source-resolution pair never leaves this module half-named.** `repositoryRoot` is forwarded exactly
  as the caller supplied it — `None` stays `None` — and the workspace default travels beside it as a
  separate argument, so the read builder is the one place that decides whether a rooted pair can be
  named at all. A context carrying a root without a tree is refused by its own model, so defaulting the
  root here would turn a minimal read into a raised validation error rather than a view.
- **The integrity inputs identify trees and comparison bases, not a recorded run.** `memoryRoot`, `codeRoot`, `baseCommits` and `contractPath` are forwarded into `IntegrityCheckRequest`; the list of bases becomes a tuple when supplied.
- **A leaf contract adds its latest persisted worklist (MIK-R08 rule 7).** The response reports state, digest, counts, items and the persisted path. Alternatively the caller names the memory tree and paired code checkout directly. Input-combination refusals belong to the builder, not this registrar.
- **Nothing for the reviewer is mounted.** No resource, route, panel or client is declared; the reviewer surface belongs to `KS-R22@v1`, and what this module publishes is the interface that leaf mounts.
- **No state, no validation and no I/O.** The module holds no module-level mutable value, opens no dataset and reads no file; every operation's work happens inside the builder it calls.
- **The memory tree is caller-supplied and the index namespace is server-supplied.** No registered tool accepts a database path or authoring destination; the anchor-resolution repository has a workspace fallback, and the coordination root holds only the derived-index cache.
- **The read signature's seed is passed through, never interpreted.** `sourcePath` is one optional wire argument forwarded as `source_path` into `ReadToolRequest`; the registrar neither validates it nor defaults it, so what a seed means — and the `PathSeed` rule that decides whether it is a usable one — stays in the models layer where the write path already spells it.

## 260928-MIK-L05 The Read Docstring Names The Route-Chain Rows And The Family Seed

`knowledge_read`'s published docstring now continues the leaf-read sentence (MIK-R05): after the advertised
families come one compact `chain_family` row per family routed at the path's directory or an ancestor, with
`payload.routeChain` stating the chain (`no_governing_family` when none). It also names the family seed:
`source_context` with a family ID in `familyRevisionId` and no `sourcePath` returns that family's full content
(ruling Q1, 2026-09-30 03:32:18). No argument changed: the family seed reuses the existing `familyRevisionId`
argument, and the registrar still forwards it without interpreting it.




## 260928-MIK-L01 The Read Docstring Names The Family-Complete Leaf Read

`knowledge_read`'s published docstring now states that, on a converted tree, `source_context` with
`sourcePath` is the family-complete leaf read (MIK-R01): the path's own invariants, then each containing
family's header (guarantee, routes, members) and its remaining members with their entries, then the
advertised families -- the same selection and `manifestDigest` `read_ar_files` returns (rule 6). It also says
the `invariant` view names the invariant's families in `families` (rule 7). No argument changed: the leaf read
takes `sourcePath` and `continuation`, and a non-default `orderingInput` on a fresh leaf read is refused by
the tree read (ruling Q7, 2026-09-29 23:21:57).




## 260928-MIK-L08 The Integrity Check Takes A Leaf's Contract


- The integrity handler names a leaf contract or an explicit memory/code tree with comparison bases, forwards one IntegrityCheckRequest, and returns the validator report and persisted leaf worklist; no database pair or recorded-run selector survives.



- The builder that decides the accepted combinations.



## 260928-MIK-L03 The Read Docstring Names `currentness`

`knowledge_read`'s published docstring gained one sentence: for a converted memory tree, `currentness` gives
each returned invariant's state (stale, unverifiable, unrealized, current) at the code tree named by
`codeTreeId`; without it they are unverifiable. Since MIK-R02 the sentence says the walk's code tree: the
one named by `codeTreeId`, or the continuation's on a resumed page. The input schema is unchanged. The registrar still passes
the caller's `repositoryRoot` untouched and the workspace root separately, which is what lets
`requested_code_tree` treat a `repositoryRoot` alone as no request (architect ruling 2, 2026-09-29T18:42:37).





- Only a named tree ID (or the continuation's) is the walk's code tree; `HEAD` is never used.



## 260928-MIK-L02 The Read Docstring Names The Page, The Threshold And The Continuation

`knowledge_read`'s published docstring now states, for a converted memory tree (`memoryRoot` is its
root), that every response is a page within one token threshold (`page`, and `threshold` on a refusal),
that `continuation` accepts the token any page minted, including the published-intent block of
`read_ar_files` (pass it with its `continuationView` as `view` and no other subject; the token binds its
ordering and code tree; `repositoryRoot` relocates the code repository), and that `currentness` is taken at
the walk's code tree: the one named by `codeTreeId`, or the continuation's on a resumed page.

- **`orderingInput` now defaults to `None`** (published default `null`), and the docstring says it defaults
  to `stable_ordering`. The effective behaviour is unchanged; "not supplied" is what lets a resumed walk keep
  its own ordering, and an empty string is still refused `unadmitted_ordering_input` (architect rulings Q5 of
  2026-09-29 19:56:40 and F1 of 20:40:40).
- The registrar still passes `workspace_root` separately, and the converted-tree read uses it as the object
  store when the caller names no `repositoryRoot` (ruling F4, 20:40:40).




- The ordering argument that is `None` unless the caller names one.


## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References



- The family module's own statement of its scope — appended rather than inserted, the three operations in the design's spelling, no domain reasoning and nothing mounted for the reviewer — together with the one entry point whose four `_register_*` calls are made in the read, diff, integrity, write order. [9]




- The statement of what the runtime configuration supplies to this family — the workspace root a read falls back to as a **default repository**, never half of a resolution pair, and the coordination root under which a converted memory tree's derived index is cached — and the configuration type whose `workspace_root` is the first value. [10]




- The four registered handlers: the read registrar that forwards the caller's own root and the configured workspace root as two separate arguments plus the configured coordination root, the write and diff registrars that take the configuration beside the server, and the integrity registrar that takes the server alone. [11]




- The published read contract: the named views with their filters, rows that name ID, kind, state and location and never text, and the optional `sourcePath` seed the signature carries into `ReadToolRequest.source_path`. [12]




- The family entry point as the package door's contract requires it: one `register_*_tools(server, config)` public function for this family, delegating to the payload builders. [13]




- The comparison registrar and handler return the knowledge files' Git diff, grouped by record and source path, without inferring a semantic effect label. [14]



- The integrity registrar and handler report validator counts and violations and add a leaf's latest worklist when contractPath is named; runId, inputDigest and compatible are not fields of the current registered contract. [15]



- The request value objects and payload builders this module delegates to, imported rather than re-declared here. [16]




- The registry the family is appended to, where the import and the tail tuple entry are the family's whole integration, and the live-registration test that compares the resulting order against the advertised roster. [17]



- The three advertised names this registrar publishes, appended at the roster tail in the same order the handlers are registered in. [18]


- The three response-model rows that validate these operations' payloads, added at the registry's own tail. [19]



- The strict response classes preserve the read view's payload, the diff's file changes and the validator's report/worklist as distinct responsibilities; the current integrity response has no compatible field. [20]



### Cross-Repo References

No cross-repository behavior is implemented in this file. It declares one tool family against the MCP server instance it is handed; every operation addresses a caller-supplied memory tree through this repository's payload builders, with no mounted authoring destination.

No meaningful cross-repo references found.

- Knowledge read/write/diff/integrity handlers resolve the existing request classes and payload builders through the lazy tools adapter at call time. No second writer or schema is introduced. [22]
