# docs/llms.txt

## Current operative account — MIK-R199

- The file is the LLM-facing summary of the product documentation, published from the docs root and linked from the
  repository and package READMEs as `https://foxfire1st.github.io/agents-remember/llms.txt`. Its first line pins
  `Version: 2.8.0 | Creation-Date: 2026-06-10T08:42:24Z | Hash: f62c732`, i.e. it is a dated snapshot of documentation
  prose rather than prose whose home this is. No script or config in the tracked tree references this path, so the
  wording is treated here as edited in the file.
- The opening summary bullet recasts search: semantic and code-graph lookup "were optional accelerators" over the same
  reviewable Markdown, and "both providers are retired, so by-path reads carry the product". The bullet beneath it in the
  same list still credits "provider indexes that clone into a worktree instead of rebuilding", so the summary list keeps
  the index-cloning claim while retiring the providers that produced the indexes.
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
- The first-run paragraph says `c-13-install-and-onboard` verifies the MCP server, runs or checks `runtime_install()`,
  initializes or adopts memory, bootstraps onboarding when needed, "and starts nothing provider-side — the two former
  search providers are retired." The by-path claim that follows is unchanged: the core path works without Docker or
  providers.
- The MCP authority-settings bullet now declares which repositories the server may touch, with "(old provider keys are
  reported once as unused)" as the disposition of the retired keys. Transcript location, timeout caps and root
  containment stay in the bullet unchanged.
- The Providers link in "Learn more" now points at "the retired semantic and code-graph providers, and how leftover state
  from an older install is cleaned up."
- The cheap-isolation section and its summary line are untouched: the section still narrates the providers in the
  present tense — re-crawling a code graph, re-embedding a semantic index, exporting and re-importing a graph bundle,
  cloning a vector database, streaming an embedding model between containers, and giving each worktree "its own isolated,
  namespaced provider stack". It closes by saying providers "can be created alongside a worktree and thrown away with
  it", and "How the pieces fit" still lists "**Index cloning** makes that isolation cheap enough to use by default." So
  the removal lands in the framing and history sentences; the isolation mechanism is still described as live machinery.

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
- Superseded by MIK-R199: `starts provider indexing when providers are enabled`. The first-run paragraph now says the
  skill starts nothing provider-side and that the former search providers are retired.

### Source and authority bounds

- Source comparison: `docs/llms.txt:1-484`, read in full.
- Source comparison: `docs/llms.txt:1-1` (version/creation-date/hash header), `docs/llms.txt:259-294` (the isolation
  section left in present tense), `docs/llms.txt:444-453` (the summary list that still credits index cloning).
- The file names no `providerSetupSeconds` and carries no settings example: the only settings references are the
  authority-settings bullet and the Settings Reference link, and the fenced blocks it does carry are a path mirror and a
  ledger table. This card therefore records nothing about a settings block, a setup timeout, or a setup detector.
- This card records the shipped wording only. It makes no claim about how the retired providers behaved at runtime, and
  none about which settings any install or cleanup path reads.

## Evidence

- The file is a versioned, dated snapshot of documentation prose, published from the docs root. [1]
- The product summary says both search providers are retired and by-path reads carry the product, while the same list still credits provider indexes cloned into a worktree. [2]
- The trust paragraph keeps the note as the thing trusted and marks search as retired history. [3]
- The retrieval routes are stated in the past tense with their providers retired, while by-path stays always available. [4]
- The read-only tool list no longer includes provider health, graph or semantic-index queries. [5]
- First-run setup starts nothing provider-side, and by-path memory needs neither Docker nor providers. [6]
- Authority settings cover repositories and report old provider keys once as unused. [7]
- The isolation section still describes provider indexes as live machinery and says providers can be created with a worktree. [8]
- The composition summary still credits index cloning as what makes isolation cheap. [9]
- The Providers link now describes retired providers and leftover-state cleanup. [10]
