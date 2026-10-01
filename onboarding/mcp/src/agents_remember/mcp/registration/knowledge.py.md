# mcp/src/agents_remember/mcp/registration/knowledge.py

## Governing Overview

[mcp/registration route overview](overview.md)

## Purpose

The knowledge operation family module: the one `register_knowledge_tools(server, config)` that declares its family against the server it is handed and delegates every operation to the payload builders in `agents_remember.mcp.tools.knowledge`. It is "**appended** to `TOOL_REGISTRARS`, never inserted: FastMCP publishes tools in registration order, so every existing name keeps the position it was advertised at." It declares the five operation families "spelled as ``Doc13:181-187`` spells them" — `knowledge_read`, `knowledge_change`, `knowledge_diff`, `knowledge_integrity_check` and `knowledge_project`. **It deliberately performs no domain reasoning and mounts nothing for the reviewer**: "``KS-R22@v1`` owns the Intent Reviewer, the cockpit route and the browser client. What this module publishes is the interface L22 mounts -- the five operations, the review-matrix view and the typed models behind them -- and it adds no panel, no route and no client." It also holds no state, validates nothing itself and opens no dataset; the runtime configuration supplies it exactly one thing — "the workspace root a read falls back to when the caller names no repository of its own", handed over as the **default repository** rather than as half of a source-resolution pair — while "Everything else a handler needs -- the dataset path, the namespace and the destination -- is caller-supplied, because the substrate decides nothing about which dataset or which vault is meant."

## Code Commentary

### Logic

**One entry point, five private registrar functions, called in declared order.** `register_knowledge_tools(server, config)` is the family's whole public surface, and its body is the five calls `_register_knowledge_read(server, config)`, `_register_knowledge_change(server)`, `_register_knowledge_diff(server, config)`, `_register_knowledge_integrity_check(server)` and `_register_knowledge_project(server, config)` — read, then change, then diff, then integrity, then projection. The read, diff and project registrars take the config, because those three operations select a dataset and, since MIK-R23, a selection that names a converted memory tree is read through a derived index cached under the coordination root; the read registrar also resolves recorded source anchors against the workspace root. The change and integrity registrars take the server alone, which is the call shape making that boundary visible. The package docstring's rule that a family module's `_register_*` calls are never reordered applies here with the same force as `TOOL_REGISTRARS` itself.

**Each handler validates its wire request, delegates, and returns the typed shape the response model declares.** Every `@server.tool()` body is one construction of a request value object from the flat keyword arguments followed by one call into `mcp/tools/knowledge.py`: `knowledge_read` builds a `ReadToolRequest`, `knowledge_change` a `ChangeToolRequest`, `knowledge_diff` a `DiffToolRequest`, and `knowledge_project` a `ProjectToolRequest`. `knowledge_integrity_check` builds an `IntegrityCheckRequest` too, since MIK-R08 (before that it was the one handler whose builder took keyword arguments directly). No handler computes a classification, infers an effect label, authors a draft or judges a rationale — the module docstring says the surface "performs no domain reasoning", and the code shape is what makes that true rather than aspirational.

**The published docstrings are the operations' own contracts, and each states what it does not do.** `knowledge_read`'s docstring names the five views and states that a value that cannot be classified "is reported as an unresolved limitation rather than returned with an empty class"; its signature also carries `sourcePath`, the optional path-only seed a caller who knows just a file can present, which travels into `ReadToolRequest.source_path` and is why the five views' own front door is reachable through the published schema rather than only through a discovered revision id. `knowledge_change`'s states that "the content is never drafted and its rationale is never judged" and that the operation "adds no gate, no approval and no new authority", and since `260921-ICR-L20` it also names the write plane's ordinary route: the run commits a whole curator hand-off list through the admitted batch **and, on the curator's ordinary route, publishes that candidate to the repository's one declared published dataset location and reads the published identity back**. Since `260921-ICR-L32` it names **both** shipped CLI entry points that reach that one writer — `agents-remember knowledge-ingest` for a leaf enclosure's ordinary route and `agents-remember knowledge-bootstrap` for a repository with no enclosure in scope — which is that leaf's correction of the singular framing `ICR-R20@v1` landed when only one of them existed. The sentence was completed rather than deleted, because a model that cannot tell where the write plane is reachable will guess. `knowledge_diff`'s states that semantic effect labels "are included only when supplied by an identified agent or assessment, never inferred from the diff". `knowledge_integrity_check`'s states that "`compatible` is absent by design, not omitted by accident, and an unresolved assessment stays unresolved", and adds that "the scope selects the recorded run; `runId` or `inputDigest` selects one exact run among several in that scope, and the response names the selected run and its input identities so the conditions cannot be read as belonging to a run they were not measured over." `knowledge_project`'s states that authored explanations "are never invented or reassessed", that Markdown and JSON are sibling views and a JSON projection is not a portable export, and that an externally edited file "is reported and preserved unless the caller authorizes an overwrite for that exact path" — the surface-level spelling of the behaviour the builders and the writer enforce.

**The runtime configuration supplies two values into this family: the workspace root, handed over as a
default REPOSITORY rather than as half of a resolution pair, and (since MIK-R23) the coordination root.**
The read, diff and project handlers pass `coordination_root=str(config.coordination_root)` to their
payload builders, which keep a converted memory tree's derived index under that root's runtime directory
when a caller's `databasePath` names such a tree; the input schemas are unchanged, and no parameter was
added. For the workspace root: `_register_knowledge_read(server,
config)` passes `repository_root=repositoryRoot` — the caller's own value, untouched, with no
substituted default — and `workspace_root=str(config.workspace_root)` as a **separate** argument to
`knowledge_read_payload`. The pair `(repository_root, code_tree_id)` is therefore completed inside the
builder and not here: this module cannot hand over a root without a tree, which is exactly the shape the
`KnowledgeReadContext` model refuses ("source resolution needs both repository_root and code_tree_id;
supplying one without the other is an incomplete resolution request"). The old spelling defaulted the
root to `str(config.workspace_root)` and left `code_tree_id` as the caller supplied it, so a minimal
schema-conformant call reached the context constructor as a half-pair and raised a raw validation error
out of the mounted tool instead of returning a view. `_register_knowledge_change` and
`_register_knowledge_integrity_check` receive no config at all, which is the structural statement that
neither is configured. Since `260928-MIK-L12` the `knowledge_change` docstring also says that on a
**converted** memory tree (it holds `knowledge/layout.json`) both CLI entry points write knowledge files
through the curator file writer (MIK-R12) instead of the database; the tool itself stays registered and
refusing, and removing it from the roster is MIK-R26's (L26).

**The five operations are the interface another leaf mounts, and the reviewer surface is not here.** The review-matrix view is reachable through `knowledge_read`'s `view` argument — the module docstring's phrasing is that what this module publishes is "the five operations, the review-matrix view and the typed models behind them" — and the typed response models behind them are the strict `ToolResponse` subclasses in `models/tools/knowledge_responses.py`, registered by name in `models/tools/tool_registry.py`. The Intent Reviewer, its cockpit route and its browser client belong to `KS-R22@v1`; this module declares no FastMCP resource, no route, no panel and no client, and its only MCP effect is the five `@server.tool()` registrations.

**The registration order is part of the advertised contract, and this family is appended at the tail.** `registration/__init__.py` imports `register_knowledge_tools` and places it as the last entry of `TOOL_REGISTRARS`, after `register_capsule_and_skill_tools`, making it the fourteenth registrar; `models/tools/public_roster.py` gained the five names at its own tail, in the same read-change-diff-integrity-projection order, and `models/tools/tool_registry.py` gained the five response-model rows in the same order. The three surfaces must agree, so the family's position in the tuple, the roster's tail order and the registry's tail order are one decision recorded in three places rather than three independent choices.

### Conventions

The family module follows the package door's contract exactly: one `register_*_tools(server, config)` public function, one private `_register_*` per operation, and every `@server.tool()` definition inside a private registrar — the shape `registration/__init__.py`'s docstring declares for every family module. Requests are assembled by importing the request value objects from the builders module rather than by re-declaring their fields here, so the wire argument names are spelled once in `mcp/tools/knowledge.py` and this module only maps them onto the value objects. Copies of another leaf's vocabulary are imports: `McpRuntimeConfig` comes from `kernel/primitives/runtime_config.py` and `FastMCP` from the SDK, and nothing here restates a view name list, a change-kind tuple, a refusal code or a format tuple. The five published docstrings are the contract carriers — each names what its operation returns and what it refuses to produce — and no module-level constant, `__all__` or helper exists beyond the six functions, so the file's whole surface is the family declaration itself.

### Invariants And Boundaries

- **The family is appended, never inserted.** `register_knowledge_tools` is the last entry of `TOOL_REGISTRARS` (the fourteenth), so no existing tool's advertised registration position moved when this family was mounted.
- **The registration order is read, change, diff, integrity, projection.** Both the five `_register_*` calls in the entry point and the five `@server.tool()` definitions appear in that order, matching the roster tail and the registry tail.
- **The surface performs no domain reasoning.** Every handler validates its wire request, delegates to a payload builder and returns; no classification, effect label, draft, rationale judgement or compatibility verdict is produced here.
- **The runtime configuration supplies two values, and neither selects a dataset.** The read registrar hands
  the workspace root over as the read builder's `workspace_root=` default repository; the read, diff and
  project registrars hand the coordination root over as `coordination_root=`, the cache location for a
  converted memory tree's derived index. The change and integrity registrars take the server alone.
- **A source-resolution pair never leaves this module half-named.** `repositoryRoot` is forwarded exactly
  as the caller supplied it — `None` stays `None` — and the workspace default travels beside it as a
  separate argument, so the read builder is the one place that decides whether a rooted pair can be
  named at all. A context carrying a root without a tree is refused by its own model, so defaulting the
  root here would turn a minimal read into a raised validation error rather than a view.
- **The integrity check publishes the exact-input selector, and the handler passes it straight through.**
  `runId` and `inputDigest` are two optional keyword-only wire arguments forwarded unchanged to
  `knowledge_integrity_check_payload`; the registrar neither validates nor defaults them, and the
  response's five run fields are the builder's answer rather than anything assembled here.
- **The integrity check also names a leaf (MIK-R08 rule 7).** `databasePath` and `repositoryId` became
  optional and `contractPath` was added as a third keyword-only argument; all six are passed unchanged into
  `IntegrityCheckRequest`. The docstring states that `contractPath` adds that leaf's latest
  change-to-knowledge worklist (state, digest, item counts, items and the persisted file's path) and that a
  leaf may be named without a dataset. Which combination is accepted, and the refusal for naming neither, is
  the builder's decision, not this registrar's.
- **Nothing for the reviewer is mounted.** No resource, route, panel or client is declared; the reviewer surface belongs to `KS-R22@v1`, and what this module publishes is the interface that leaf mounts.
- **No state, no validation and no I/O.** The module holds no module-level mutable value, opens no dataset and reads no file; every operation's work happens inside the builder it calls.
- **The default dataset, namespace and destination are always caller-supplied.** No handler falls back to a configured dataset path, repository id or destination root — only the anchor-resolution root has a configured fallback, and the coordination root is only where a caller-named converted tree's index is cached.
- **The read signature's seed is passed through, never interpreted.** `sourcePath` is one optional wire argument forwarded as `source_path` into `ReadToolRequest`; the registrar neither validates it nor defaults it, so what a seed means — and the `PathSeed` rule that decides whether it is a usable one — stays in the models layer where the write path already spells it.

## 260928-MIK-L05 The Read Docstring Names The Route-Chain Rows And The Family Seed

`knowledge_read`'s published docstring now continues the leaf-read sentence (MIK-R05): after the advertised
families come one compact `chain_family` row per family routed at the path's directory or an ancestor, with
`payload.routeChain` stating the chain (`no_governing_family` when none). It also names the family seed:
`source_context` with a family ID in `familyRevisionId` and no `sourcePath` returns that family's full content
(ruling Q1, 2026-09-30 03:32:18). No argument changed: the family seed reuses the existing `familyRevisionId`
argument, and the registrar still forwards it without interpreting it.

- The docstring sentences on the chain rows and the family seed. [1]

## 260928-MIK-L01 The Read Docstring Names The Family-Complete Leaf Read

`knowledge_read`'s published docstring now states that, on a converted tree, `source_context` with
`sourcePath` is the family-complete leaf read (MIK-R01): the path's own invariants, then each containing
family's header (guarantee, routes, members) and its remaining members with their entries, then the
advertised families -- the same selection and `manifestDigest` `read_ar_files` returns (rule 6). It also says
the `invariant` view names the invariant's families in `families` (rule 7). No argument changed: the leaf read
takes `sourcePath` and `continuation`, and a non-default `orderingInput` on a fresh leaf read is refused by
the tree read (ruling Q7, 2026-09-29 23:21:57).

- The docstring sentences on the leaf read and, after MIK-R05's chain sentences, the `invariant` view's families. [2]

## 260928-MIK-L08 The Integrity Check Takes A Leaf's Contract

- The optional dataset pair, the new `contractPath`, the docstring's worklist sentence, and the one request value handed to the builder. [3]
- The builder that decides the accepted combinations. [4]

## 260928-MIK-L03 The Read Docstring Names `currentness`

`knowledge_read`'s published docstring gained one sentence: for a converted memory tree, `currentness` gives
each returned invariant's state (stale, unverifiable, unrealized, current) at the code tree named by
`codeTreeId`; without it they are unverifiable. Since MIK-R02 the sentence says the walk's code tree: the
one named by `codeTreeId`, or the continuation's on a resumed page. The input schema is unchanged. The registrar still passes
the caller's `repositoryRoot` untouched and the workspace root separately, which is what lets
`requested_code_tree` treat a `repositoryRoot` alone as no request (architect ruling 2, 2026-09-29T18:42:37).

- The read docstring's `currentness` sentence, now at the walk's code tree. [5]
- Only a named tree ID (or the continuation's) is the walk's code tree; `HEAD` is never used. [6]

## 260928-MIK-L02 The Read Docstring Names The Page, The Threshold And The Continuation

`knowledge_read`'s published docstring now states, for a converted memory tree (`databasePath` is its
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

- The docstring sentences on the page, the threshold and the cross-surface continuation. [7]
- The ordering argument that is `None` unless the caller names one. [8]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The family module's own statement of its scope — appended rather than inserted, the five operation families in the design's spelling, no domain reasoning and nothing mounted for the reviewer — together with the one entry point whose five `_register_*` calls are made in the declared read, change, diff, integrity, projection order. [9]
- The statement of what the runtime configuration supplies to this family — the workspace root a read falls back to as a **default repository**, never half of a resolution pair, and the coordination root under which a converted memory tree's derived index is cached (MIK-R23) — and the configuration type whose `workspace_root` is the first value. [10]
- The five registered handlers: the read registrar that forwards the caller's own root and the configured workspace root as two separate arguments, the read, diff and project registrars that also forward the configured coordination root, and the change and integrity registrars that take the server alone. [11]
- The published read contract: the five views, the attributed records, the rule that an unclassifiable value is an unresolved limitation rather than an empty class, and the optional `sourcePath` seed the signature carries into `ReadToolRequest.source_path`. [12]
- The family entry point as the package door's contract requires it: one `register_*_tools(server, config)` public function for this family, delegating to the payload builders. [13]
- The record registrar, whose docstring states that the content is never drafted, the rationale never judged, and no gate, approval or new authority added — and, since `260921-ICR-L20`, names the write plane's ordinary route and its read-back; since `260928-MIK-L12` it also says that a converted memory tree is written through the curator file writer. [14]
- The comparison registrar, whose docstring states that semantic effect labels are included only when an identified source supplied them. [15]
- The report registrar, whose docstring records that `compatible` is absent by design rather than by accident, that an unresolved assessment stays unresolved, and that `runId`/`inputDigest` select one exact run among several in the selected scope. [16]
- The projection registrar, whose docstring records sibling Markdown and JSON views, the non-export JSON projection, and the externally edited file that is preserved unless its exact path is authorized. [17]
- The request value objects and payload builders this module delegates to, imported rather than re-declared here. [18]
- The registry the family is appended to, where the import and the fourteenth tuple entry are the family's whole integration, and the live-registration test that compares the resulting order against the advertised roster. [19]
- The five advertised names this registrar publishes, appended at the roster tail in the same order the handlers are registered in. [20]
- The five response-model rows that validate these operations' payloads, added at the registry's own tail. [21]
- The strict response types behind the five operations, including the read payload travelling as the view payload's own JSON and `compatible` typed `None`. [22]
- The review-matrix view this module makes reachable through the read operation's view argument, defined where the view payloads live rather than here. [23]
- The test that pins the advertised roster to the response-model registry, so the five names and their models cannot drift apart. [24]
- The test that pins the advertised roster to the response-model registry, so the five names and their models cannot drift apart. [25]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It declares one tool family against the MCP server instance it is handed, and every operation it publishes addresses a caller-supplied dataset, namespace or destination through payload builders that live in this repository.

No meaningful cross-repo references found.
