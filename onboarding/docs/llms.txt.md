# docs/llms.txt

## Current operative account — MIK-R199

The inherited source account below is retained verbatim at its earlier source blob `24ae5ecc1c485103ade43601a1a6b742f33be711`; its inline line addresses belong to that source epoch and are detached from current live citation authority. Current numbered clauses below bind the separately specified current source targets.

- The file is the LLM-facing summary of the product documentation, published from the docs root and linked from the
  repository and package READMEs as `https://foxfire1st.github.io/agents-remember/llms.txt`. Its first line pins
  `Version: 2.8.0 | Creation-Date: 2026-06-10T08:42:24Z | Hash: f62c732`, i.e. it is a dated snapshot of documentation
  prose rather than prose whose home this is. No script or config in the tracked tree references this path, so the
  wording is treated here as edited in the file.
Historical source wording retained verbatim (docs/llms.txt blob 24ae5ecc1c485103ade43601a1a6b742f33be711; detached from live citation authority): - The opening summary bullet recasts search: semantic and code-graph lookup "were optional accelerators" over the same
  reviewable Markdown, and "both providers are retired, so by-path reads carry the product". The bullet beneath it in the
  same list still credits "provider indexes that clone into a worktree instead of rebuilding", so the summary list keeps
  the index-cloning claim while retiring the providers that produced the indexes.

The current summary pairs retired-provider/by-path framing with paired publication and a disposable knowledge index.
- The trust paragraph states the same position as history: semantic and graph search "were optional accelerators for
  *finding* a note — both are retired now, and neither was ever the thing you trust." The trust claim itself is unchanged:
  the note, plus Git's answer on whether it still matches the code.
- "Three ways to reach knowledge" keeps by-path as always available and moves the other two routes into the past tense:
  the semantic search "returned a note whose path then named the exact code file" and its provider is retired, the
  code-relationship graph "answered callers, callees, dependencies, complexity, and symbol lookups" and its provider is
  retired too. The paragraph that composes them closes the same way — both provider-backed substrates are retired, so the
  router works on by-path and intent alone.
- The router's own substrate list beneath that paragraph still names `Semantics` and `Relationship` as choices beside
  `Intent`. The retirement is asserted in the prose around the list, not by removing list entries.
- The read-only tool bullet now gives its examples as orienting on a repository, checking drift, and previewing a
  closeout. Provider health summarisation and graph or semantic-index queries are gone from the list.
Historical first-run source wording (old docs/llms.txt blob 24ae5ecc1c485103ade43601a1a6b742f33be711; detached from current authority): - The first-run paragraph says `c-13-install-and-onboard` verifies the MCP server, runs or checks `runtime_install()`,
  initializes or adopts memory, bootstraps onboarding when needed, "and starts nothing provider-side — the two former
  search providers are retired." The by-path claim that follows is unchanged: the core path works without Docker or
  providers.

Current first-run text registers the server, serves packaged skills and starts Bootstrap with one role_start call; optional onboarding and knowledge foundation go to the user-started Architect task, and setup excludes provider indexing and setup-authored knowledge.
- The MCP authority-settings bullet now declares which repositories the server may touch, with "(old provider keys are
  reported once as unused)" as the disposition of the retired keys. Transcript location, timeout caps and root
  containment stay in the bullet unchanged.
- The Providers link in "Learn more" now points at "the retired semantic and code-graph providers, and how leftover state
  from an older install is cleaned up."
- The "Task isolation and disposable indexes" section says each task's paired code and memory worktrees isolate its
  changes, that the former semantic and code-graph providers are retired so worktree setup does not provision their
  stacks, clone their databases or seed their watchers, and that the knowledge index is an SQLite view derived from a
  selected memory text tree, cached by tree identity, rebuilt when absent and never written by knowledge writers.
  "How the pieces fit" now lists "The **disposable knowledge index** is rebuilt from the selected text tree." in place of
  the former index-cloning line; only the table-of-contents entry "Cheap isolation: indexes are cloned, not rebuilt"
  still uses cloning wording.

### Superseded inventory

- Superseded by MIK-R199, in the trust paragraph:

  ```text
  Semantic and graph search still exist — but as opt-in accelerators
  for *finding* a note, never as the thing you trust.
  ```

  It described search as a live opt-in capability. The paragraph now reads "were optional accelerators for *finding* a
  note — both are retired now, and neither was ever the thing you trust."
- Superseded by MIK-R199, in the authority-settings bullet:

  ```text
  - **MCP authority settings** declare which repositories and providers the server
    may touch, where transcripts go, which timeout caps apply, and how configured
    roots stay inside allowed workspace paths.
  ```

  The bullet now scopes authority to repositories and adds that old provider keys are reported once as unused.
- Superseded by MIK-R199, in the read-only tool list:

  ```text
  - **Read-only tools** compute facts with no side effects — orienting on a
    repository, checking drift, summarizing provider health, querying the graph or
    the semantic index, previewing a closeout. The agent can call these freely.
  ```

  The provider-health and index-query examples are removed; the list now runs orienting, drift checking and closeout
  preview.
- Superseded by MIK-R199: `starts provider indexing when providers are enabled`. The current setup paragraph says no
  provider indexing or setup-authored knowledge is part of the setup path.

### Source and authority bounds

- Source comparison: `docs/llms.txt:1-456`, read in full.
- Source comparison: `docs/llms.txt:1-1` (version/creation-date/hash header), `docs/llms.txt:258-267` (the task-isolation
  section), `docs/llms.txt:417-434` (the "How the pieces fit" list, which now names the disposable knowledge index),
  `docs/llms.txt:50-50` (the table-of-contents entry that still names cloned indexes).
- The file names no `providerSetupSeconds` and carries no settings example: the only settings references are the
  authority-settings bullet and the Settings Reference link, and the fenced blocks it does carry are a path mirror and a
  ledger table. This card therefore records nothing about a settings block, a setup timeout, or a setup detector.
- This card records the shipped wording only. It makes no claim about how the retired providers behaved at runtime, and
  none about which settings any install or cleanup path reads.

## Evidence

- The file is a versioned, dated snapshot of documentation prose, published from the docs root. [1]
Historical source account (detached from live reference 2; docs/llms.txt blob 24ae5ecc1c485103ade43601a1a6b742f33be711):

- The product summary says both search providers are retired and by-path reads carry the product, while the same list still credits provider indexes cloned into a worktree.

- The summary still retires semantic/code-graph providers, but its Git-memory bullet now names paired code/memory publication and a disposable knowledge index rebuilt from the selected text tree; the task-isolation section says the retired providers' databases are not cloned, and only the table-of-contents entry still names cloned indexes.

- The trust paragraph keeps the note as the thing trusted and marks search as retired history. [3]

- The retrieval routes are stated in the past tense with their providers retired, while by-path stays always available. [4]

- The read-only tool bullet names orienting on a repository, checking drift and previewing closeout, with no provider-health, graph or semantic-index query. [5]

- First-run setup includes no provider indexing or setup-authored knowledge, and by-path memory needs neither Docker nor providers. Anchor: `provider indexing or setup-authored knowledge is part of this path` [6]

- Authority settings cover repositories and report old provider keys once as unused. Anchor: `old provider keys are reported once as unused` [7]

- The task-isolation section states the former providers are retired, so worktree setup provisions, clones and seeds none of their stacks, and describes the knowledge index as a disposable SQLite view. [8]

- The composition summary now credits the disposable knowledge index rebuilt from the selected text tree; only the table-of-contents entry still names cloned indexes. Anchor: `The **disposable knowledge index** is rebuilt from the selected text tree.` [9]

- The Providers link now describes retired providers and leftover-state cleanup. Anchor: `[Providers](guides/providers.md)` [10]

- The summary retires the semantic and code-graph providers so by-path reads carry the product, and its Git-memory bullet names paired code/memory publication and a disposable knowledge index rebuilt from each selected text tree. [2]
