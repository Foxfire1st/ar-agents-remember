# docs/architecture.md

## Current operative account — MIK-R199

- The retrieval-substrates section keeps by-path (Intent) as "always available; needs no
  provider", and says the by-meaning route's "provider is retired; the route has no engine now"
  while the by-relationship route's "provider is retired as well" (`docs/architecture.md:85-89`).
- The same section states that GrepAI served semantic memory search and CodeGraphContext served the
  code graph, that they are retired, that "no product path installs, enables, starts, indexes, or
  queries them", and that the `providers/` tree in the layout above "holds only what an older
  installation left behind" (`docs/architecture.md:91`).
- It frames the providers as accelerators for *finding* knowledge, says they "were never the
  source of truth", keeps durable memory as Markdown + Git, drift-checked and approval-gated, and
  assigns the surviving work: "`runtime_install` stops a leftover provider watcher and reports old provider
  keys once as unused; deleting leftover folders takes the explicit `providers-remove` command".
  The Providers guide is described as "now a retirement and old-install cleanup account"
  (`docs/architecture.md:93`).
- The Ownership Boundaries section repeats the split at a different altitude: "Provider leftovers —
  a stale watcher, old settings keys, leftover runtime folders — are handled by `runtime_install`
  and the explicit `providers-remove` command, not by the memory or workflow skills", and "No
  provider lifecycle (images, watchers, indexing) belongs to anything now: it is retired"
  (`docs/architecture.md:115`).
- The installed-runtime section says MCP tools and package-local modules own "runtime install,
  provider-leftover cleanup, worktree, memory, and benchmark operations", with no parallel
  `scripts/` route (`docs/architecture.md:47`).
- The layout block still draws a `providers/` subtree with `requirements/`, `patches/`, `runners/`,
  `data/`, and `logs/` (`docs/architecture.md:28-44`); the retrieval section is the place that
  characterizes that tree as leftover-only (`docs/architecture.md:91`).
- The page states no provider install, prepare, seed, start, query, watch, provider-status or
  provider-lane obligation. It names no command flag, gives no folder sizes, does not name the
  unused-key field, and is silent on Docker or Ollama requirements, on a periodic safety check over
  leftovers, and on any provider panel (`docs/architecture.md:1-140`).

### Superseded inventory

- Superseded by MIK-R199: "The installed runtime does not keep a parallel `scripts/` execution
  route; MCP tools and package-local modules own runtime install, provider lifecycle, worktree,
  memory, and benchmark operations." The ownership item is now "provider-leftover cleanup"
  (`docs/architecture.md:47`).
- Superseded by MIK-R199: "**By meaning (Semantics)** — semantic search over the memory, for when
  the concept is known but the file is not." Replaced by the same sentence with "Its provider is
  retired; the route has no engine now" appended (`docs/architecture.md:88`).
- Superseded by MIK-R199: "The meaning and relationship substrates are served by **opt-in
  providers** — GrepAI for semantic memory search, CodeGraphContext for the code graph. They run as
  local Docker services under `ar-coordination/providers/` (shown above) and index code and memory
  in the background." Replaced by the past-tense service account, the retirement of both providers,
  and the leftover-only reading of the `providers/` tree (`docs/architecture.md:91`).
- Superseded by MIK-R199: "These providers are accelerators for *finding* knowledge; they are not
  the source of truth." Replaced by "were accelerators" and "were never the source of truth", with
  the watcher stop and the `providers-remove` boundary added in the same paragraph
  (`docs/architecture.md:93`).
- Superseded by MIK-R199: "Provider lifecycle — building images, watchers, and indexing — is owned
  by the MCP provider tools and `runtime_install`, not by the memory or workflow skills." Replaced
  by the leftovers-only ownership statement and the sentence that no provider lifecycle belongs to
  anything now (`docs/architecture.md:115`).

### Source and authority bounds

- Document read in full: `docs/architecture.md:1-140`.
- Changed regions read in the current file: `docs/architecture.md:26-47`,
  `docs/architecture.md:83-93`, `docs/architecture.md:95-115`.
- Superseded wording was read from the supplied diff hunks for this exact path.
- These bounds record what the page states. They supply no build, test, publication, review or
  acceptance claim for the page or the product.

## Evidence

- By-path needs no provider; by-meaning has a retired provider and no engine, and by-relationship has a retired provider. [1]
- GrepAI and CodeGraphContext are named as retired, with no product path installing, enabling, starting, indexing or querying them. [2]
- `runtime_install` stops a leftover provider watcher and reports old provider keys once; folder deletion belongs to the explicit `providers-remove` command. [3]
- Provider leftovers are handled by `runtime_install` and `providers-remove`, not by memory or workflow skills, and no provider lifecycle belongs to anything now. [4]
- Runtime ownership names provider-leftover cleanup and keeps no parallel `scripts/` route. [5]
- The layout block still draws a `providers/` subtree. [6]
- The page is silent on Docker/Ollama requirements, command flags, the unused-key field name, the safety detector and any provider panel. [7]
