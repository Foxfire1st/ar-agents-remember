# skills/l-01-agent-lifecycles/templates/curator-handoff-list.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T23:48:33Z |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64` |
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

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

Since leaf `260928-MIK-L21` (MIK-R21) the template ends its producer-facing part with **"Where an entry
lands once knowledge is text (MIK-R21)"**: an informational map from today's hand-off fields to the text
knowledge format — records as `knowledge/<kind-dir>/<ID>-<slug>.json` that never list their own
locations, tests, families or decisions; writer-minted IDs (`INV-7K3F9Q`, 8-character derived IDs for
exported legacy records); each target becoming a `realizes` entry in `onboarding/<path>.json` with an
anchor that omits its own path; test evidence becoming a `proves` entry; `origin`; and the canonical
formatting applied by `agents-remember knowledge-format`. It says explicitly that **nothing changes what
a producer emits before MIK-R37**, and that `incidental` has no spelling in the file format (its mapping
is MIK-R12's to decide).

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
| **The informational MIK-R21 section: where an entry lands once knowledge is text, and that nothing changes before MIK-R37.** | `## Where an entry lands once knowledge is text (MIK-R21)`; "Nothing here changes what a producer emits today." | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:425-457 |
| Curator-owned semantic scope remains required. | `### Curator-authored semantic scope` | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:144-194 |
| The public retention input and exact readback requirements. | `### Retain exact siblings when adding new obligations to a family successor` | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:356-424 |
| **Per-target realization rationale and role, the value/vocabulary/length/route rules, the committed-retry exemption, and the stated supersession of revision 1's target element shape.** | "Realization rationale and role: one authored explanation per target"; "this file's element shape supersedes rule 1's" | skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:101-140; skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:8-18 |

## Cross-Repo References

No sibling repository defines this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): **body update — the template gains the informational section "Where an entry lands once knowledge is text (MIK-R21)".** The Logic paragraph above records what it maps and that it changes nothing a producer emits before MIK-R37; one reference row cites it (`:425-457`). No verification stamp was advanced.
- 2026-09-28T17:18:24+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): body update — Logic states the per-target `{path, locator, governing_route, rationale, role}` element shape, the required authored rationale, the named refusals and the supersession of the external schema note revision 1's rule-1 element shape; new reference row. Other ranges re-pointed through the exact base-to-candidate line map. No stamp advanced.

- 2026-09-26T23:48:33Z — L39: reconciled exact sibling-retention input, immutable endpoint behavior and reporting against the frozen source. Preserved prior history and existing verification metadata; actual source commit stamping remains closeout-owned.

- 2026-09-26T21:21:26+00:00: Generated citation repair: "It is not the curator's side." repointed to skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:319-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled authored scope, explicit installed invocation and ordinary comparison recording where this source owns them.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-20T02:27+02:00 — 260915-KS-L33 curator, reopened-claim re-read (uncommitted change set on `ar/260915-ks-l33-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **re-read the reopened blob-identity row (line 206) and retained its wording unchanged, with one range repointed.** The row names `_TargetPlan` and `citation`, and its wording is still true of the candidate: the curator's target plan still builds the stored anchor with the tree-read `source_identity`, and the citation still carries that anchor plus the claim citing it. Its second range `:443-451` no longer reached `citation`, though — this leaf's CYCLE-04 repair changed `_TargetPlan.citation()`'s body, and the method is now declared at `463-471` — so that range was regenerated to the method's own extent, `mcp/src/agents_remember/application/knowledge_curator_ingest.py:463-471`. The first range `:398-446` was left exactly as written: `_TargetPlan`'s own declaration still sits at `421` inside it. No anchor was renamed, no second range was added, no citation was dropped and no claim wording was changed. This decision is recorded rather than left implicit because the claim's evidence changed structurally after its verification stamp, and the honest reading of that is "re-read, wording retained, range regenerated", not "re-stamped". the recorded working candidate was recorded as this leaf's candidate `ar/260915-ks-l33-ar` on the same base, because that is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded. No commit, no verification stamp advanced, no acceptance claim made.
- 2026-09-20T01:02+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 3 enforced citation rows this card carried (citation_claim_reopened, citation_anchor_absent_from_range). Two were verified against the working tree and needed no edit: the `_TargetPlan` row's projected range `mcp/src/agents_remember/application/knowledge_curator_ingest.py:398-446` still contains the class's own declaration (the module has since grown, so the declaration now sits at 421 inside that range) and the reopened claim is current there. The third was fixed by hand in the Anchor cell only: the checker reads a quoted anchor that embeds code spans as the blanked join of its fragments, so `"Prefer \`symbol\` in \`target\` — it survives a move."` could never be found in any range; the quote now reads `"it survives a move."`, the verbatim clause the cited `skills/l-01-agent-lifecycles/templates/curator-handoff-list.md:116-119` actually holds. No claim wording was changed, both ranges are untouched, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `_TargetPlan`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `curator-handoff-list.md.md:198` (it survives a move.) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `curator-handoff-list.md.md:205` (`_TargetPlan`, `citation`).

- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the curator
  hand-off list template. It records the document's role as the producer's output shape, the
  authority split with the revision-1 schema note and the 41-entry fixture it prices, the thirteen
  fields and their nine-producer/four-curator ownership, the per-field table, the required target
  locator and the permitted null evidence locator, Rule 1 (co-resolution, with the measured 20-of-40
  and 6-of-20 counts) and Rule 2 (no paraphrase, with the 41-in/41-out bar), the honest encodings for
  a ruling that applies nowhere and an unrecorded governing route, the template's own boundary that
  it is not the curator's side, the four seats that emit or ingest it, the four registry lists that
  declare it, and the fact that the blob identity is attached downstream by the curator's own ingest
  rather than carried by the producer. Verified against the committed source at
  `7e6936c0d3b87f2fa0f462c5c63d6d86441ef10b`.
