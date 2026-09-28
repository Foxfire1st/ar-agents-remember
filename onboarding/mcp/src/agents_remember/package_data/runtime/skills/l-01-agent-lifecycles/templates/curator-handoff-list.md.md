# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T23:48:33Z |
| lastVerifiedCommitHash | `eda947325ccbe0791973953265278597e968a34a` |
| lastVerifiedCommitDate | 2026-09-28T18:11:05+02:00|
| governingOverview | `mcp/overview.md` |

## Governing Overview

[mcp route overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the canonical skills/l-01-agent-lifecycles/templates/curator-handoff-list.md. It is synchronized by the existing skill propagation owner and introduces no independent doctrine.

Defines the producer/curator handoff data boundary. Nine producer fields travel unchanged; the curator resolves the outcome and authors semantic scope, family coverage and external-source provenance.

## Code Commentary

### Logic

Producer entries identify one obligation and all its targets together. Target locators are required; evidence locators may be absent. Statements and producer dispositions are preserved rather than paraphrased. Applicability, conditions and exclusions are authored before invariant ingest.

The family plane distinguishes declared guarantees, exact memberships, deliberate no-family and unexamined entries. A successor declaration may include `retain_memberships`, with each item exactly `member_id` and a nonblank `basis`. Read the exact family view first: a family_member row’s subject.record_id is the stored membership ID, and its statement names the invariant revision.

The references must resolve in the selected dataset within an explicitly declared same-family predecessor. Omitted/empty retention keeps none. No current-head lookup or implicit roster inheritance is permitted. Repeated IDs, duplicate new endpoints and retain/retire conflicts refuse. A changed nonempty retention set or basis under an allocated declaration key is a content conflict.

The public writer adds successor edges while leaving old records unchanged. Check `retainedFromMemberId`, measured unchanged-sibling counts and the published exact roster. This syntax extends a declaration carried by a genuine obligation; it is not a standalone family-only operation. External evidence retains document identity and provenance instead of fabricated Git anchors.

Since leaf `260921-ICR-L45` (developer ruling "require rationale"; Architect rulings on reviews R1–R3)
each `target` element is `{path, locator, governing_route, rationale, role}`: `rationale` is the required
authored explanation of why that place carries the obligation, `role` is optional (omit to inherit the
entry's `realization_role`; only when neither level states one is the claim `unclassified`), and an entry
may state `realization_rationale` / `realization_role` as an explicit default. The writer never generates a
rationale. It refuses, per entry and before minting, a target with no rationale
(`realization_rationale_absent`), non-string values (`realization_value_not_text`), unknown role words
including `"absent"` (`realization_role_unknown`), rationales over 20000 characters
(`realization_rationale_too_long`), and the placeholder route word `absent` in any case
(`realization_governing_route_absent_literal`) — a missing route is spelled by omitting the key. An exact
retry of an already committed entry is not checked again. The authority paragraph states that this element
shape supersedes rule 1's `{path, locator, governing_route}` in the external schema note
*260915-KS-curator-handoff-list-schema.md* revision 1 (not edited; it lives outside this repository), while
the rest of rule 1 stands; the verbatim worked examples predate per-target rationale and say so.
This package copy is generated from the canonical root template by `scripts/sync-skills.py`.

### Conventions

Canonical skills own instructions. Generated copies are synchronized artifacts; curate the matching sidecar against its own source path. One output list preserves the producer’s nine fields and fills only curator-owned decisions.

### Invariants And Boundaries

- Ground every record in accepted scope and real source evidence; do not create records to inflate coverage.
- Exact retained revisions are reused without rewriting old meaning or provenance.
- New membership edges are not new invariant revisions or semantic acceptance.
- A refusal or unexamined plane stays explicit; no favorable default substitutes for it.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources cited below. | — | — |

## Repo-Internal References

These references name the current owners and the behavior they establish.

| Finding | Anchor | Source |
| --- | --- | --- |
| Curator-owned semantic scope remains required. | `### Curator-authored semantic scope` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:144-194 |
| The public retention input and exact readback requirements. | `### Retain exact siblings when adding new obligations to a family successor` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:356-424 |
| **Per-target realization rationale and role, and the stated supersession of revision 1's target element shape (generated copy).** | "Realization rationale and role: one authored explanation per target"; "this file's element shape supersedes rule 1's" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:101-140; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:8-18 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History
- 2026-09-28T17:18:24+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): body update — this generated copy now carries the per-target rationale/role element shape, the named refusals and the supersession statement (regenerated by `sync-skills.py`, byte-identical to the canonical template). No stamp advanced.

- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.

- 2026-09-26T21:17:04+00:00: Generated citation repair: "It is not the curator's side." repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:319-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — The generated handoff template makes applicability, conditions and exclusions curator-owned semantic scope. Missing scope remains unfilled curation. Changed scope under an allocated entry key is a content conflict that needs a successor; historical records are never silently migrated.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **body update: the packaged copy carries the canonical template's new section** stating the shape of the two keys the producer never writes, `family` and `external_sources`, beside the unchanged thirteen fields — one declaration per local key, `basis` required wherever the curator decides, reuse by identity, a changed guarantee as a successor under a new key, at most 32 sources per entry, and `external_sources: []` meaning examined-and-none while an omitted key means not examined. Written in `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` and propagated by `scripts/sync-skills.py`. **Citation accounting:** the ranges this card carries into the files this leaf's change set moved were re-derived against the candidate's own bytes rather than shifted by a remembered delta. No claim and no row was dropped, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-20T01:30+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared both enforced `citation_anchor_absent_from_range` rows this card carried, by changing only the two quoted anchor texts.** Both rows failed for the same structural reason: the checker removes backticked code spans from a quoted anchor *including their content* before matching, so a quote holding backticks can never be found in a source that still spells them. Row one's second quote was `"Prefer `symbol` in `target` — it survives a move."`, which can only be searched for as `Prefer in — it survives a move.`; it now reads `"it survives a move."`, verbatim on `...templates/curator-handoff-list.md:116` inside the cited `:116-119` and carrying the same Rule 1 fact (target is identity, so a symbol survives a move). Row two's quote was `"copies root `skills/` into the MCP package-data copy"`, searched for as `copies root into the MCP package-data copy`; it now reads `"into the MCP package-data copy"`, verbatim on `AGENTS.md:106` inside the cited `:105-107` (both verified with `grep -n`) and carrying the same fact (that line is the repository's own statement that the sync script copies root `skills/` into the package-data copy). Each row's other anchor — the `\`target\` is a list …` quote at `:110-114` and the corpus test name at `:604-640` — is untouched and still resolves, every range is unchanged, no Finding text was re-worded, and no citation was dropped. Reviewed against the working candidate `ar/260915-ks-l30-ar`; no commit exists for these bytes and the commit stamp is not advanced.
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared none of the 2 enforced citation rows this card carried (citation_anchor_absent_from_range) — both cited ranges were hand-read and already hold the anchor text their claims name verbatim ("Prefer `symbol` in `target` — it survives a move." at mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:116, and "copies root `skills/` into the MCP package-data copy" at AGENTS.md:106), so the finding comes from the anchor being resolved with its backticked spans removed and no citation edit can clear it. No range was changed here; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `curator-handoff-list.md.md:153` (it survives a move.) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence; `curator-handoff-list.md.md:160` (into the MCP package-data copy) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence.

- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the packaged mirror
  of the curator hand-off list template. It records that the copy is byte-identical to
  `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` (empty `diff`, equal MD5
  `6ab039ac49385760f44a3a50347a8de0`, 230 lines, shared commit
  `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b`), the contract content the copy carries (thirteen fields
  with the nine/four ownership split, the field table, the shape block and locator rules, both rules
  with their measured bars, the honest encodings and the producer-side boundary), and the packaging
  path that generates, serves and installs it: `scripts/sync-skills.py` copying the canonical
  `skills/` tree into `runtime/skills`, the `skill_resources` provider serving the packaged tree and
  admitting the corpus together with its manifest, `runtime_install` syncing it into the coordination
  root, and the `AGENTS.md` rule that forbids editing generated copies directly. Verified against the
  committed source at `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b`.
