# c-04-retrieval-strategy-router/SKILL.md

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-09-21T18:09+02:00                     |
| lastVerifiedCommitHash | `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`             |
| lastVerifiedCommitDate | 2026-09-23T00:33:19+02:00|
| governingOverview      | `../../../../../../../overview.md`                              |

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
tool, so a deeper read is taken by identity. The section's source is the authored root skill
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
their refusal codes, and the continuation limitation as a limitation.

### Todos

None.

## Docs References

No external documentation is cited here. The skill is a repository-local
retrieval contract over installed provider tooling and durable onboarding.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `c-04-retrieval-strategy-router` skill defines Semantics, Relationship, and Intent as the three retrieval substrates and describes when to chain them. | `## Retrieval Substrates` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:12-32 |
| **The Intent bullet now names the published-intent half: the same `read_ar_files` call carries the invariants a previous task already recorded about the requested paths, at their exact snapshot and without needing a task.** | `## Retrieval Substrates` (Intent bullet) | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:12-33 |
| **The route section, which is this leaf's carrier: the publication location the read side declares, and — restated as current truth by `260921-ICR-L20` — the ordinary write side publishing to that same location with `--publish`, the memory-root rule with no fallback, the exact payload spellings, the named `state`s and their refusal codes, the seed-level absences, and the continuation limitation stated as a limitation.** | `## Published Intent Before Planning`; "Where the route reads, and what publishes there." | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:173-232 |
| Semantics requests MCP provider context before using healthy GrepAI provider tools, then shows synthetic broad semantic routing and scoped memory-project search examples. | `## Semantics: GrepAI` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:34-82 |
| Relationship requests MCP provider context before using healthy CGC tools and includes synthetic `analyze calls` and `analyze complexity` examples with sample response shapes. | `## Relationship: CodeGraphContext` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:84-131 |
| The inline GrepAI and CGC examples explicitly forbid copying private repository names, symbols, paths, snippets, or results into reusable skill examples. | `## Semantics: GrepAI`, `## Relationship: CodeGraphContext` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:34-131 |
| The skill points agents to `grepai-high-leverage-usage.md` and `codegraphcontext-high-level-methods.md` for full provider usage catalogs and synthetic example outputs. | "grepai-high-leverage-usage.md", "codegraphcontext-high-level-methods.md" | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:82-82; mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:126-126 |
| Intent preserves route-index, overview, sidecar, and bounded source confirmation as the proof layer after discovery. | `## Intent: Onboarding And Source` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:133-171 |
| The generated route-index semantics close the skill, and are unchanged by this leaf. | `## Route Index Semantics` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:231-239 |
| The sibling GrepAI catalog covers managed invocation, command selection, broad search, project-scoped search, route-scoped snippet search, trace caveats, status, and practical rules using synthetic examples only. | `# GrepAI High-Leverage Usage` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/grepai-high-leverage-usage.md:1-211 |
| The sibling CGC catalog explains the typed `cgc_*` tools and their native `analyze` operations in a Choosing A Method table, then closes with practical selection rules; examples are synthetic only. | `analyze` | mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/codegraphcontext-high-level-methods.md:1-44 |

## Cross-Repo References

The CGC examples in the source docs are synthetic response-shape illustrations.
They do not contain private sibling repository names, symbols, paths, or code.

| Finding | Anchor | Source |
| --- | --- | --- |
| No source-code contract is imported from a sibling repository. | n/a | n/a |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `## Retrieval Substrates` repointed to mcp/src/agents_remember/package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md:12-33. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **body updated — the consequence repair this leaf landed in this mirror's own route paragraph.** `ICR-R20@v1` wired the ordinary write side to the location this skill declares, so the paragraph that said the write side *has to* publish there (and that the wiring was R20's obligation) now states the current route: the ingest command selects that same location with `--publish`, resolving it through **this** read side's declaration and reading the published identity back through the reader's owner, while a run that names no destination still commits without publishing — the reason the flag is a selection rather than a default. `ICR-R25@v1`'s two-consecutive-task journey is unchanged as an outstanding obligation. This is text only: the skill's provider contract, its substrate definitions, its boundary and its refusal vocabulary are all untouched, and the canonical root `skills/` copy carries the identical paragraph (the mirror is produced by `scripts/sync-skills.py`, which this leaf ran together with its `--check`). **Citation accounting:** the carrier row's extent was re-derived from the section's own post-edit lines (`:173-229` → `:173-232`) and the anchor set was extended to name the corrected sentence. No claim and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): **body updated — this generated mirror is one of the ten carriers this leaf's requirement moves.** The Intent bullet now names the published-intent half (`:21-27`) and the skill gained a **Published Intent Before Planning** section (`:173-229`) that states the route, the publication location it declares, the memory-root rule with no fallback, the exact payload field spellings, the three named `state`s with their refusal codes, the seed-level absences and the continuation limitation. The card's Logic records all of it and names the authored owner (`skills/c-04-retrieval-strategy-router/SKILL.md`) and the generator (`scripts/sync-skills.py`, nine targets) rather than implying this copy is authored. **Every citation range on this card was re-derived against the 239-line candidate, not shifted by the 60 added lines**: the section rows now read `## Retrieval Substrates` `:12-32`, `## Semantics: GrepAI` `:34-82`, `## Relationship: CodeGraphContext` `:84-131`, the shared prohibition row `:34-131`, `## Intent: Onboarding And Source` `:133-171`, and the two sibling-catalog literals `:82-82` / `:126-126` (the two rows the checklist flagged as stale); three rows were added — the Intent bullet, the new section, and the unchanged `## Route Index Semantics` close. No claim was re-worded to fit a stale pointer and no anchor was renamed. **Installed copies are not this leaf's:** the seven harness skill roots still carry the 179-line carrier, and installing and verifying them is the orchestrator's acceptance step, not a memory change. **Stamp accounting:** the recorded working candidate names this leaf's candidate; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded, because no commit contains the body as it now stands and the governed closeout owns the real stamp. No commit was made.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 7 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that ran far past the end of the target. `codegraphcontext-high-level-methods.md` is 184 lines, so the sibling-CGC-catalog row moved from `L1-L38, L321-L332` to `L1-L44; L174-L184` (intro plus the Choosing A Method table, then the Practical Rules section). Reworded the claim to name the typed `cgc_*` tools, since the doc now routes through MCP tools rather than raw `cgc analyze` calls.
- 2026-07-06T13:35+02:00 — 260703-L10 round 2 (L10R-2, synced from root `skills/` via `sync-skills.py`): the research-phase rule's "build/job decision" became "build decision" (the l-01 vocabulary) in the Rules list; no strategy, recipe, or routing change. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S5 sync): this generated `c-04` skill mirror was re-synced to carry the `read_ar_files` **research-phase read** doctrine on the Intent strategy — `read_ar_files` is the preferred paired onboarding + bounded source read (the recipe batched), used during the research phase instead of native read, counted as research evidence, with native read reserved as the edit precondition. Generated-mirror note only; the authored skill source owns the wording. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T00:37+02:00: Refreshed verification and line citations after `c-04-retrieval-strategy-router` skill was compacted around MCP provider-tool routing.
- 2026-05-23T13:46+02:00: Updated `c-04-retrieval-strategy-router` skill onboarding to match the MCP provider-tool route and deleted source lifecycle scripts.
- 2026-05-21T23:55+02:00: Switched GrepAI examples from bare binary/environment setup to `provider-lifecycle.py grepai run -- ...`.
- 2026-05-21T16:14+02:00: Added GrepAI high-leverage usage examples, runtime-owned invocation guidance, and a link to the sibling GrepAI catalog.
- 2026-05-21T15:20+02:00: Replaced private-project CGC examples with synthetic response-shape examples and made `analyze complexity` the second inline high-value pattern.
- 2026-05-21T14:10+02:00: Added CGC high-level method examples to the skill, linked the sibling catalog, and refreshed this sidecar to match the current compact skill.
- 2026-05-21T04:09+02:00: Removed provider lifecycle wording from `c-04-retrieval-strategy-router` skill.
- 2026-05-21T03:05+02:00: Rewrote onboarding for the `c-04-retrieval-strategy-router` skill retrieval strategy router, including GrepAI Semantics, CodeGraphContext Relationship, Intent proof, and candidate packets.
- 2026-05-19T04:05+02:00: Clarified that the 80-line confirmation output budget requires shell-level output caps and that `rg -m` alone is not enough across many files. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:58+02:00: Added a general confirmation command-output budget and triage-scope limit so `c-04-retrieval-strategy-router` skill does not enter implementation-mechanism search unless the prompt asks for it. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:40+02:00: Tightened bounded confirmation with filename-first narrowing, route-overview fallback rules, and a hard stop once source evidence is sufficient. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-19T03:12+02:00: Changed fast discovery to read root `overview.index.json` before root `overview.md`, making full root overview prose a fallback when the index is insufficient.
- 2026-05-19T02:45+02:00: Added route-index `hotPath` consumption so discovery can use generated summary, candidate hints, and source-anchor hints before reading full overview prose.
- 2026-05-19T02:21+02:00: Added the generalized source-anchor narrowing step before confirmation-mode `rg`, so route labels and broad domain terms are not reused as source queries after they already selected the route.
- 2026-05-19T02:03+02:00: Clarified that missing sidecars or sparse memory are not packet failures; they stay in bounded source confirmation and use targeted source reads/searches.
- 2026-05-19T01:50+02:00: Condensed the source skill to 98 lines and corrected the bounded confirmation handoff so it consumes the discovery candidate packet instead of replaying overview/index reads.
- 2026-05-19T01:37+02:00: Replaced the normal `deterministic-walkthrough` handoff with `bounded-source-confirmation`.
- 2026-05-19T01:11+02:00: Split read behavior into `fast-memory-discovery` and `deterministic-walkthrough` modes.
- 2026-05-18T21:44+02:00: Created onboarding for the renamed and hardened `c-04-retrieval-strategy-router` skill onboarding read-mode skill after pulling `origin/main`.
