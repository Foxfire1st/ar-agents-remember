# c-04-retrieval-strategy-router/SKILL.md

## Governing Overview

[overview.md](../../../../../../../overview.md)

## Purpose

`c-04-retrieval-strategy-router` skill is the retrieval strategy router for context-backed source work. It chooses
between semantic search, relationship graph queries, and intent-oriented
onboarding/source confirmation before broad source reads.

## Code Commentary

### Logic

The skill defines three retrieval substrates. `Semantics` is for fuzzy concepts
whose route, structure, or source location is unknown and prefers GrepAI over
direct memory repo search when available. `Relationship` is for known anchors
whose callers, callees, dependencies, ownership, inheritance, or impact
neighborhoods are unknown and prefers CodeGraphContext when available. `Intent`
is for known anchors or locations where the missing truth is a contract,
invariant, branch-valid behavior, or fix direction; it uses onboarding plus
bounded source confirmation as the proof layer. This generated runtime mirror now
also carries the slice-07 **research-phase read** doctrine attached to the Intent
strategy: the `read_ar_files` MCP tool is the preferred paired onboarding + bounded
source read (mirroring how Semantics prefers GrepAI and Relationship prefers CGC) —
one batch call returns each source file with its sidecar plus the repository and
governing route overviews; during the research phase (up to the build decision —
the 260703-L10 sweep retired the pre-convergence "build/job" compound here)
read managed-repo source with `read_ar_files` rather than native read, count those
calls as research evidence alongside the Semantics/Relationship queries, and reserve
native read as the edit precondition once building begins.

Since 260921-ICR-L19@v1 the Intent substrate also carries the repository's **published intent**: the
Intent bullet names it beside the paired read, and the skill gained a **Published Intent Before Planning**
section stating the route end to end. That section records where the route reads and what has to publish
there (`<memory_root>/knowledge.sqlite`, declared by the read side because no shipped owner defaults a
publication destination), the memory-worktree-versus-canonical-root rule with no fallback between the
two, the payload's own field spellings (`kind`, `item_id`, `invariant_id`, `record_id`, `revision_id`,
`counts.primary_items_total`, `counts.primary_items_remaining`), the three named `state`s with their
refusal codes, the seed-level absences (`registration_absent`, `selector_absent`), and the limitation that
a bounded page's `continuation` continues the selective scope read rather than the mounted `knowledge_read`
tool, so a deeper read is taken by identity. **Since 260928-MIK-L02 (MIK-R02) that limitation holds only for
a block read from a database.** The section now teaches the taught route of MIK-R02 rule 6: when the block's
`memoryTree` is present, the whole knowledge block is cut to one shared threshold (`threshold`, 8,000
`tiktoken:o200k_base` tokens), each page's `page` states `total`, `returned` and `remaining`, and a page's
`continuation` is followed through `knowledge_read` (`continuationOperation: "knowledge_read"`), passing the
value of `memoryTree.memoryRoot` as `databasePath`, `repositoryId`, the `continuationView` as `view` and the
token as `continuation`, and nothing else; naming a different `orderingInput` or `codeTreeId` is refused, and
`repositoryRoot` is named only when the code repository is not the mount's workspace. It explains deferred
seeds and the collapsed deferred entry with its `seeds`, `page.headerReference`, `oversized_row`, and the two
refusals (`continuation_binding_mismatch`: restart from the seed; `continuation_unreadable`). The consumer
note of review R2-2 is taught here: follow `continuation`, not `enumerationComplete`, through a collapsed
walk (accepted by the architect, ruling 2026-09-29 21:32:34). The database paragraph keeps the by-identity
read. **Since 260928-MIK-L01 (MIK-R01) the section names the family-complete leaf read** (rule 6: "Skill c-04
names this view"): on a converted tree each path's entry is the leaf read (`page.selectionPolicy:
"family-complete-leaf"`), and a new paragraph teaches its row kinds in order -- the path's own `member` rows
with their `realization` and `proof` rows, each containing family's `family_header` and remaining members (a
member returned earlier is a `member_reference`), then one `advertised_family` row per further family with
`via` -- the `counts`, `memoryTreeId`, and `knowledge_read` `source_context` with `sourcePath` as the same
selection under the same `manifestDigest`, plus the `invariant` view's `families`. The paging paragraph now
says a leaf page that continues a family starts with a `family_header_reference` row (a view page still names
it in `page.headerReference`), and that a tail too long for one continuation's queue is refused
`seed_queue_exceeded`, to be read in smaller requests. The lines were rewrapped (ruling N9 of 2026-09-30
00:08:39), and all 10 copies are synced. **Since 260928-MIK-L05 (MIK-R05) a paragraph "Route-chain families
come last"** follows the family-complete one (ruling Q5 of 2026-09-30 03:32:18): each path lists one compact
`chain_family` row per family routed at its directory or an ancestor (ID, title, guarantee, `routes`,
`memberCount`, `via`, `memberAtSeed`), `routeChain` states the mechanical chain or `no_governing_family`, a
path with no entries but a governing family returns these rows and states `registration_absent`, a chain
family is read whole by following the row's `expand` (`knowledge_read` `source_context` with
`familyRevisionId` and no `sourcePath`), and only `read_ar_files` may return a repeated row as a short
`served_earlier` row. No new line exceeds 100 characters, and `sync-skills.py` re-synced the 9 generated
copies (10 `SKILL.md` files changed). The section's source is the authored root skill
`skills/c-04-retrieval-strategy-router/SKILL.md`, and this generated mirror is one of the nine copies the
repository's own `scripts/sync-skills.py` writes from it.

The Semantics section first requests MCP `context_packet(...,
include_providers=true)` when the server is configured, then uses GrepAI only
when provider state is healthy and a matching MCP provider tool is exposed. It
shows high-value synthetic response shapes for broad semantic routing and scoped
memory-project search, and links to the sibling `grepai-high-leverage-usage.md`
catalog for full usage notes.

The Relationship section teaches CGC as a structural tool rather than a
file-line locator. It first requests the MCP context packet and then uses CGC
only when provider state and tool exposure allow it. It shows two high-value
synthetic response shapes: `analyze calls` for downstream impact tracing and
`analyze complexity` for risk triage. The examples deliberately use placeholder
repo ids, symbols, and paths so reusable docs do not expose private project
code. The skill links to the sibling `codegraphcontext-high-level-methods.md`
catalog for the full command set and synthetic example outputs.

### Conventions

Use MCP provider tools for GrepAI so the server supplies provider authority and
the provider-owned workspace environment:

```text
context_packet(repo_id="<repoId>", include_providers=true)
grepai_search(query="<query>", dry_run=false)
```

Use MCP provider tools for CGC so native CGC commands run with the managed
FalkorDB-backed provider environment:

```text
context_packet(repo_id="<repoId>", include_providers=true)
cgc_query(repo_id="<repoId>", query_type="find", arguments=["name", "<anchor>"], dry_run=false)
```

After a CGC locator query, prefer `analyze calls`, `callers`, `chain`, `deps`,
`tree`, `complexity`, `dead-code`, `overrides`, or `variable` for structure.
Treat CGC output as discovery and confirm selected anchors with bounded source
reads before editing.

### Invariants And Boundaries

Provider output is never final proof. `c-04-retrieval-strategy-router` skill must confirm selected candidates with
source and/or verified onboarding before answering or editing. If optional
providers are not available, the skill continues with Intent using route
indexes, governing overviews, sidecars, and bounded source reads. Route indexes
remain availability metadata, not proof: `coveredFiles` means a sidecar exists,
while a source path inside `sourceScope` but absent from `coveredFiles` means
skip sidecar probing and read source first.

The skill does not check, install, repair, or reindex providers.

**One paragraph of the route section was corrected by `260921-ICR-L20`, and it is the paragraph that
matters most to this skill's own boundary.** The section used to say the ordinary write side *had to be*
wired to the location this route declares, with the wiring named as `ICR-R20@v1`'s obligation; the change
restates it as current truth: the ingest command selects that same location with `--publish`,
**resolving it through this read side's own declaration** and reading the published identity back
through the reader's owner, while a run that names no destination and passes no `--publish` still commits
without publishing — which is why the flag stays a selection rather than a default. The remaining
`ICR-R25@v1` obligation is unchanged (the two-consecutive-task journey that has to prove task A's
publication lands where task B's planner looks). Nothing else in the mirror moved: the same section
still states the memory-root rule with no fallback, the exact payload spellings, the named `state`s and
their refusal codes, and the continuation limitation as a limitation (for a database block only, since
260928-MIK-L02).

### Todos

None.

## Evidence

### Docs References

No external documentation is cited here. The skill is a repository-local
retrieval contract over installed provider tooling and durable onboarding.

No relevant external documentation found.

### Repo-Internal References

- `c-04-retrieval-strategy-router` skill defines Semantics, Relationship, and Intent as the three retrieval substrates and describes when to chain them. [1]
- **The Intent bullet now names the published-intent half: the same `read_ar_files` call carries the invariants a previous task already recorded about the requested paths, at their exact snapshot and without needing a task.** [2]
- **The route section, which is this leaf's carrier: the publication location the read side declares, and — restated as current truth by `260921-ICR-L20` — the ordinary write side publishing to that same location with `--publish`, the memory-root rule with no fallback, the exact payload spellings, the named `state`s and their refusal codes, the seed-level absences, and the continuation limitation stated as a limitation.** [3]
- **MIK-R02 rule 6, the taught route: a memory tree's bounded page, deferred or collapsed seeds (and, since MIK-R01, `seed_queue_exceeded` and the literal reference row of a leaf page), and every continuation followed through `knowledge_read`.** [4]
- **MIK-R01 rule 6: the skill names the family-complete leaf read, its row kinds in order, its counts, and `source_context` as the same selection under the same manifest.** [5]
- **MIK-R05 (ruling Q5): the skill teaches the route-chain rows, `routeChain`, the family seed through `expand`, and the `served_earlier` rendering only `read_ar_files` uses.** [6]
- Semantics requests MCP provider context before using healthy GrepAI provider tools, then shows synthetic broad semantic routing and scoped memory-project search examples. [7]
- Relationship requests MCP provider context before using healthy CGC tools and includes synthetic `analyze calls` and `analyze complexity` examples with sample response shapes. [8]
- The inline GrepAI and CGC examples explicitly forbid copying private repository names, symbols, paths, snippets, or results into reusable skill examples. [9]
- The skill points agents to `grepai-high-leverage-usage.md` and `codegraphcontext-high-level-methods.md` for full provider usage catalogs and synthetic example outputs. [10]
- Intent preserves route-index, overview, sidecar, and bounded source confirmation as the proof layer after discovery. [11]
- The generated route-index semantics close the skill, and are unchanged by this leaf. [12]
- The sibling GrepAI catalog covers managed invocation, command selection, broad search, project-scoped search, route-scoped snippet search, trace caveats, status, and practical rules using synthetic examples only. [13]
- The sibling CGC catalog explains the typed `cgc_*` tools and their native `analyze` operations in a Choosing A Method table, then closes with practical selection rules; examples are synthetic only. [14]

### Cross-Repo References

The CGC examples in the source docs are synthetic response-shape illustrations.
They do not contain private sibling repository names, symbols, paths, or code.

No source-code contract is imported from a sibling repository.
