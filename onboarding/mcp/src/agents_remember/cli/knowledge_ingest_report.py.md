# mcp/src/agents_remember/cli/knowledge_ingest_report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest_report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T09:20+02:00 |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

**How one `knowledge-ingest` run is rendered — the report IS the product.** The ingest's outcome is a
report, not an exit code: a refusal per entry is a *result*, and a caller that branches on the process
status loses it. This module is the whole answer the run prints, in the two forms its caller may ask
for, and it was extracted from `cli/knowledge_ingest.py` when `ICR-R20@v1`'s ordinary publication
route added two more facts to that answer — the destination the run selected, and the identity a read
of it found back.

The split the extraction made is the module's boundary: the surface that decides **whether** a run may
proceed stays in the command module, and the shape of **what it says** lives here, so neither grows
past the rail by absorbing the other. `knowledge_ingest.py` is 692 lines and this module was 205 at the
extraction; it is **328** lines now, because `ICR-R28@v2` added the two plane blocks and
`ICR-R29@v1` renamed one payload key and added the held-operation fields.

## Code Commentary

### Logic

- `summary` (function, lines 34-76) — the human-readable rendering: the mode and **the admission
  source** (`:44-44`), the candidate (`:45-45`), lane and repository (`:46-46`), the held-operation
  count beside the allocation journal that holds them (`:47-48`), the code tree with its source and
  recorded base commit and the memory tree (`:49-51`), the batch state with its refusal when there is
  one (`:52-53`), the counts (`:54-54`), and **the run's publication route line** (`:55-55`), which is
  printed unconditionally because "this run named no destination" is itself the fact a reader needs.
  The publication result is added only when the report holds one (`:57-63`), the read-back only when
  the route made one (`:64-65`), the review baseline only when the handoff stated one (`:66-67`), then
  the family and source lines (`:68-69`), and one line per outcome (`:70-75`).
- `payload` (function, lines 79-128) — the machine-readable report and therefore *the contract*: every
  tuple becomes a list and every dataclass a mapping, nothing is summarised away, because a caller
  that has to re-read the database to learn what happened has been given a message rather than a
  result. `admissionSource` (`:96-96`) names the document this run was admitted under — a leaf
  enclosure contract **or** the settings document a bootstrap was admitted from — and it replaced the
  former `contractPath`/`contract_path`, which was simply false for a bootstrap admission whose source
  is a settings document. `publicationRoute` (`:117-117`) is the run's own line about the destination
  it selected — the declared published location, a caller-named path, or the fact that it named none;
  `publishedIdentity` (`:121-121`) is the read-back, and it is `None` when this run published nothing
  to read back, which is a different fact from a read-back that found the wrong dataset. The two plane
  blocks follow (`:123-124`), each carrying its own state.
- `_family_block` (function, lines 131-182) and `_source_block` (function, lines 183-214) — the two
  authored planes as JSON objects, each with its own state and its own sentence.
- `_identity_line` (function, lines 215-223) — one read-back as the single line a reader scans it on:
  the state, the digest (or `-` when there is none), the path, and the refusal code when the state is
  `unavailable`.
- `_read_back_block` (function, lines 224-240) — the read-back as the smallest owned object, carrying
  the reader's own sentence in `detail` and, for `unavailable`, the shipped `refusalCode`.
- `_family_line` (function, lines 241-257) and `_source_line` (function, lines 258-269) — the two
  plane lines the human rendering appends.
- `_targets` (function, lines 270-276) — how one resolved target (path plus its symbol or line range)
  is rendered per entry.
- `_counts` (function, lines 277-291) — the entry arithmetic: the operation's own ten counters plus
  `committed` and `refused` (`:289-290`), which are the two figures that let a caller see a partial
  hand-off without re-deriving it from the lists.
- `_outcome` (function, lines 294-328) — one entry's whole outcome, including the state the operation
  itself assigned it and every route and target it touched.
- `__all__` (line 31) — `payload` and `summary` are the module's whole surface; everything else is
  private.

**Two fields are strings rather than booleans or objects, and for the same reason.** `reviewBaseline`
and `publicationRoute` both state what this run did about a handoff that can also have several reasons
for not happening. "Not placed" and "not selected" are not `false`; they are facts whose reason a
caller acts on, and a caller that has to guess which reason is being handed a message instead of a
result.

### Conventions

Follows the CLI package's conventions: a private `_`-prefixed helper per rendering concern, no
argument parsing and no operation logic, and public names declared in `__all__`. It imports the
operation's own report types rather than re-declaring them, so the renderer cannot drift from what the
operation produced.

### Invariants And Boundaries

- **The report is the result.** Nothing here infers anything from an exit status, and nothing rounds a
  partial outcome up: every entry appears in exactly one of `committed` / `rulings` / `refused`.
- **Rendering only.** This module decides no destination, runs no operation and performs no I/O beyond
  building strings and mappings; it is a pure function of the report plus the two facts the caller
  resolved.
- **`None` and "wrong" are different facts.** An absent `publishedIdentity` means this run published
  nothing to read back; a present one whose `state` is `mismatch` means the location holds a different
  dataset. Both are printed as what they are.
- **The JSON payload is the contract.** The human summary may be extended; the payload's keys are what
  a curator and the canonical carrier instructions consume. A key is **added** rather than renamed —
  unless the old key's own name had become false, which is what happened once and only once:
  `contractPath`/`contract_path` became `admissionSource`/`admission_source` in `ICR-R29@v1`, because
  the document a run is admitted under is a settings document for a taskless bootstrap and calling it
  "the contract" was false about it. No test and no consumer read the old key.
- **Both entry points take the same two extra facts positionally-in-name.** `publicationRoute` and
  `publishedIdentity` are keyword-only on both renderers (`:35-37`, `:76-78`), so a caller cannot
  supply one and forget the other.

### Todos

None requested of this card. One fact a later reader may want to know rather than re-derive: the
counts block gained `committed` and `refused` in this same change, because the requirement's boundary
case — a hand-off with both committed and refused entries — must be readable from the report's own
arithmetic and not only from the two lists.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The human rendering, including the one line that is printed whether or not anything was published.** | `summary` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:34-76 |
| **The machine-readable report, and the two facts `ICR-R20@v1` added: the destination the run selected and the identity an independent read found there.** | `payload`; `publicationRoute`; `publishedIdentity` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:79-128 |
| **The key this leaf renamed, because the document a run is admitted under is not always a contract.** | `admissionSource`; `report.admission_source` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:44-44; mcp/src/agents_remember/cli/knowledge_ingest_report.py:96-96 |
| The two authored planes the payload carries, each with its own state and sentence. | `_family_block`; `_source_block`; `family`; `sources` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:131-182; mcp/src/agents_remember/cli/knowledge_ingest_report.py:183-214 |
| The entry arithmetic, including the explicit `committed` / `refused` counts the boundary case reads. | `_counts` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:277-291 |
| One read-back as a scannable line, and as the smallest owned object carrying the reader's own sentence. | `_identity_line`; `_read_back_block` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:215-221; mcp/src/agents_remember/cli/knowledge_ingest_report.py:224-238 |
| The two plane lines the human rendering appends. | `_family_line`; `_source_line` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:241-255; mcp/src/agents_remember/cli/knowledge_ingest_report.py:258-267 |
| One entry's whole outcome, and how a resolved target is rendered per entry. | `_outcome`; `_targets` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:294-328; mcp/src/agents_remember/cli/knowledge_ingest_report.py:270-274 |
| The declared exports that make this module's two renderings its public surface. | `__all__` | mcp/src/agents_remember/cli/knowledge_ingest_report.py:31-31 |
| **The caller that supplies both facts, and the surface that stayed behind in the command module: whether a run may proceed at all.** | `_print_report`; `_publication_route`; `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:603-616; mcp/src/agents_remember/cli/knowledge_ingest.py:627-658; mcp/src/agents_remember/cli/knowledge_ingest.py:661-693 |
| **The operation's own report types this module renders rather than re-declares, including the held operations and the admission source.** | `IngestReport`; `HeldOperation`; `EntryOutcome` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:421-432; mcp/src/agents_remember/application/knowledge_curator_ingest.py:459-483; mcp/src/agents_remember/application/knowledge_curator_ingest.py:486-541 |
| **The read-back value the payload carries, whose three states are the reader's own vocabulary rather than this module's.** | `PublishedIdentityReadBack` | mcp/src/agents_remember/application/knowledge_publication_route.py:97-112 |
| The subparser registrations that make `knowledge-ingest` and `knowledge-bootstrap` reachable surfaces whose report vocabulary this module's spellings are shared with. | "knowledge-ingest"; "knowledge-bootstrap" | mcp/src/agents_remember/cli/__main__.py:41-48; mcp/src/agents_remember/cli/__main__.py:50-58 |

## Cross-Repo References

No meaningful cross-repo references found: this module renders one command's report and touches no
repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): **one payload key renamed because its own name had
  become false, and this card's stale ranges re-derived against the candidate.** `contractPath` /
  `contract_path` became **`admissionSource` / `admission_source`** (`:44-44`, `:96-96`): the document
  a run is admitted under is a leaf enclosure contract for `knowledge-ingest` but a **settings
  document** for a taskless bootstrap, so a field called "contractPath" was a false statement about
  one of the two runs that produce this report. No test and no consumer read the old key. The card's
  Logic section was re-derived from each construct's own declaration on the 328-line candidate (the
  module was 205 lines at the extraction): `summary` `:34-76`, `payload` `:79-128`, the two plane
  blocks `:131-182`/`:183-214`, `_identity_line` `:215-223`, `_read_back_block` `:224-240`,
  `_family_line` `:241-257`, `_source_line` `:258-269`, `_targets` `:270-276`, `_counts` `:277-291`
  and `_outcome` `:294-328`. The invariant that a payload key is added rather than renamed was
  **corrected rather than left standing**, because this leaf is the one case where the old key's name,
  not its meaning, was the defect. **No verification stamp was advanced** — the candidate is
  uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed
  closeout owns the real code and memory commits.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **the report renders both planes.** `payload` gained a `family` block and a `sources` block and `summary` gained one line for each, and every plane carries its **own** state — `recorded`, `projected` or `not-recorded` — so a run that wrote nothing reports null counts rather than zeroes that would read as measured. The source block claims a path and a digest only for the state that actually wrote the manifest.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): created this one-to-one card for the new module. The 135-line report renderer moved out of `cli/knowledge_ingest.py` when `ICR-R20@v1` added two facts to the run's answer, and the extraction is what keeps both files under the repository's size rail: the command module keeps the *decision* surface (which invocation may proceed, which destination it selected) and this module owns the *shape* of what it says. The card records the two new payload fields and why `publishedIdentity`'s absence is a different fact from a `mismatch`, the unconditional publication-route line in the human rendering, the two explicit counts the requirement's boundary case reads, and the string-not-boolean rule the module's own docstring states for `reviewBaseline` and `publicationRoute`. Every range was derived from its construct's own extent in this candidate rather than carried. **Verification metadata:** the card names the production line it was read against — `71a4433e686b3380af97a0836bb82bab2c8f2aad`, this leaf's base — because the module exists only in this leaf's uncommitted candidate, so no commit contains the content a stamp would claim to have verified. That is a statement of *what the reading was against*; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp.

