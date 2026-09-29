# mcp/tests/test_knowledge_ingest_publication_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_ingest_publication_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T18:09+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba` |
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The ordinary authoring and publication route, driven through the real command line** — the
regression surface for `ICR-R20@v1`, and the case set that makes the requirement's forbidden inference
measurable instead of stated.

The ingest exists, it writes, and its publication owner is real. What these cases measure is the
*route*: whether the curator's ordinary run reaches that owner at the repository's one published
location, what the run admits is standing there, and whether a reader then selects the dataset the
write reported. Every case drives `agents-remember knowledge-ingest` through the umbrella `main` —
the surface the canonical curator instructions carry — over a **production-shaped enclosure**: a real
code line with its own work branch, a real external memory repository, a real Git memory **worktree**
cut from it, and a contract recording all of them under a real coordination root. The declared
location is resolved by the read route's own owner rather than restated in the fixture
(`_declared_location` `:226-234`), so the fixture cannot quietly agree with the implementation about a
path neither of them should be computing.

**Eleven cases, and the six user operations plus one refusal family they cover**, each named in the
module's own docstring:

| Operation | Case |
| --- | --- |
| the ordinary first publication | `test_the_ordinary_route_publishes_to_the_declared_location_and_reads_it_back` (`:263-312`) |
| a custom candidate is the one reviewed **and** published | `test_a_custom_candidate_is_the_one_the_ordinary_route_publishes` (`:315-350`) |
| a partial refusal names each entry and publishes only what committed | `test_a_partial_refusal_names_each_entry_and_publishes_only_what_committed` (`:353-400`) |
| the explicit update, and the earlier truth surviving into the successor | `test_an_explicit_update_replaces_the_dataset_the_run_forked_from` (`:403-484`) |
| the exact retry: `no_change`, bytes unmoved, identity still confirmed | `test_an_exact_retry_republishes_no_change_and_still_reads_back_confirmed` (`:487-530`) |
| no destination named — exit zero is not a publication claim | `test_a_run_that_names_no_destination_states_that_it_published_nothing` (`:533-557`) |
| a refused publication leaves the destination untouched and reads nothing back | `test_a_refused_publication_leaves_the_destination_and_reads_nothing_back` (`:560-605`) |
| two contradictory destination selections refused by name before anything is read | `test_two_destination_selections_are_refused_by_name_before_anything_is_read` (`:608-641`) |
| a destination selected without a publication says which reason it was | `test_a_destination_selected_without_a_publication_says_so_in_the_route_line` (`:644-699`) |
| an expectation with no destination selector refused by name | `test_an_expected_destination_without_a_destination_is_refused_by_name` (`:702-732`) |
| an unresolvable declared location refused rather than guessed | `test_a_declared_location_that_cannot_be_resolved_is_refused_rather_than_guessed` (`:735-756`) |

## Code Commentary

### Logic

Module surface (ranges are this candidate's extents):

- Module docstring (lines 1-38) — the six operations and the refusal family, stated as the user
  operations they are.
- Import block (lines 40-82) — the two declared-route owners the fixture resolves through
  (`published_dataset_path`, `resolve_published_intent`, `contract_context`), the shipped CLI `main`,
  the mounted read surface (`knowledge_read_payload`, `ReadToolRequest`) and the real store reader
  (`open_read_only_database`), and **the ingest-list fixture module's own helpers** (`:63-82`) rather
  than a second support module.
- `OrdinaryEnclosure` (dataclass, lines 94-112) — the four roots the contract really records:
  `memory_repo` is the canonical **external** memory repository and `memory_worktree` is a real Git
  worktree of it on this leaf's work branch. That pair is the point of the fixture: the coordination
  context resolves the first as the memory layer and the contract's own worktree as the effective
  memory root, so the declared location is the memory line the task can actually commit rather than a
  scratch directory that merely looks like one.
- `_ordinary_enclosure` (function, lines 115-155) — builds that world and then the contract recording
  it, including the leaf's own commit on its work branch (a leaf always stands on work the base
  commit does not hold, and the ingest resolves its citations against that line).
- `_contract_text` (function, lines 158-204) — the one leaf contract carrying exactly the cells this
  enclosure has.
- `_ordinary_argv` (function, lines 207-223) — the shipped invocation the canonical curator
  instructions carry, aimed at this enclosure.
- `_declared_location` (function, lines 226-234) — the location this route must publish to, resolved
  by the **read** route's own owner.
- `_labels` (function, lines 237-244) — every obligation label a dataset actually holds, read from the
  file itself rather than from the report.
- `_statements` (function, lines 247-260) — the statements the **mounted** read surface answers with,
  at the dataset's own snapshot.
- `test_*` cases (lines 263-756) — as tabled above.

**The measurement order is the route's own order.** The first case measures four facts in sequence:
the destination the run selected is the one the read route declares, the publication owner reported
`published` for it, the route's independent read-back confirms that exact identity, and the mounted
read surface answers from that dataset. Each later case moves one variable — the candidate directory,
the entry set, the baseline, the retry, the destination selection — and measures the same four facts
where they apply.

### Conventions

Ordinary `unit-regression` evidence-unit module: `pytestmark = pytest.mark.evidence_unit` (`:84`), no
integration marker, no docker, no network — a `tmp_path` world with real Git repositories and real
APSW databases. It imports the existing ingest-list fixture module instead of introducing a third
support module, which is why its catalog delta is a *consumer* change only (see below).

### Invariants And Boundaries

- **Nothing asserts a prebuilt payload in place of the production composition.** Every case runs the
  shipped entry point and reads the report it printed, the dataset on disk, or the mounted read
  surface's answer.
- **The declared location is derived, never restated.** `_declared_location` calls the read route's
  own owner, so a fixture that drifted from the implementation would fail rather than agree.
- **A refusal is measured, not assumed.** The invocation refusals assert the exit code, the named
  message and that no candidate was created on the way; the refused publication asserts the
  destination bytes are unchanged.
- **`None` is a fact with a reason.** The two "selected a destination, published nothing" runs assert
  both the null `publication`/`publishedIdentity` and the route line's own reason, and that the
  location was never created.
- **No artifact and no contract of its own.** The module composes
  `mcp/tests/snapshot_lifecycle_test_support.py` (reached through the fixture module it imports) and
  the existing ingest-list fixtures, so the evidence census population stays at **sixteen contracts /
  sixty-six artifacts** and only the two `consumer_scope = "exact"` rows gained the path.

### Todos

None requested of this card. One boundary recorded rather than carried as a task: the case set is
ordinary unit evidence, so the pinned Dagger certification graph and the browser acceptance path are
outside it, and the two-consecutive-task assembled journey is `ICR-R25@v1`'s rather than this module's
— the continuity it measures here (task B forking A's published dataset and republishing onto it) is
the same operation at one enclosure's scale.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one ordinary run: the declared destination receives the candidate, the read-back confirms the exact identity, and the mounted read surface answers from that dataset.** | `test_the_ordinary_route_publishes_to_the_declared_location_and_reads_it_back` | mcp/tests/test_knowledge_ingest_publication_route.py:266-315 |
| **The requirement's forbidden inference made measurable: a committed entry beside exit zero, and a report that states the absence in its own field rather than leaving it to be inferred from a null.** | `test_a_run_that_names_no_destination_states_that_it_published_nothing`; `test_a_destination_selected_without_a_publication_says_so_in_the_route_line` | mcp/tests/test_knowledge_ingest_publication_route.py:536-560; mcp/tests/test_knowledge_ingest_publication_route.py:647-702 |
| **The boundary case: one list, one committed and one refused entry, both named, only what committed published.** | `test_a_partial_refusal_names_each_entry_and_publishes_only_what_committed` | mcp/tests/test_knowledge_ingest_publication_route.py:356-403 |
| **The explicit update — the identity replaced is the one this run read from its own baseline, and the earlier truth survives into the successor.** | `test_an_explicit_update_replaces_the_dataset_the_run_forked_from` | mcp/tests/test_knowledge_ingest_publication_route.py:406-487 |
| The safe retry, measured on the file rather than asserted from the exit code. | `test_an_exact_retry_republishes_no_change_and_still_reads_back_confirmed` | mcp/tests/test_knowledge_ingest_publication_route.py:490-533 |
| The custom candidate that must be the one reviewed and published, with no conventional path invented. | `test_a_custom_candidate_is_the_one_the_ordinary_route_publishes` | mcp/tests/test_knowledge_ingest_publication_route.py:318-353 |
| The refusal family: a refused publication, two contradictory selections, an absorbed expectation, and an unresolvable location. | `test_a_refused_publication_leaves_the_destination_and_reads_nothing_back`; `test_two_destination_selections_are_refused_by_name_before_anything_is_read`; `test_an_expected_destination_without_a_destination_is_refused_by_name`; `test_a_declared_location_that_cannot_be_resolved_is_refused_rather_than_guessed` | mcp/tests/test_knowledge_ingest_publication_route.py:563-608; mcp/tests/test_knowledge_ingest_publication_route.py:611-644; mcp/tests/test_knowledge_ingest_publication_route.py:705-735; mcp/tests/test_knowledge_ingest_publication_route.py:738-759 |
| **The production-shaped enclosure and the contract that records it, including the leaf's own commit on its work branch.** | `OrdinaryEnclosure`; `_ordinary_enclosure`; `_contract_text` | mcp/tests/test_knowledge_ingest_publication_route.py:97-115; mcp/tests/test_knowledge_ingest_publication_route.py:118-158; mcp/tests/test_knowledge_ingest_publication_route.py:161-207 |
| **The four helpers that keep the fixture from agreeing with the implementation, and the shipped invocation the canonical instructions carry.** | `_ordinary_argv`; `_declared_location`; `_labels`; `_statements` | mcp/tests/test_knowledge_ingest_publication_route.py:210-226; mcp/tests/test_knowledge_ingest_publication_route.py:229-237; mcp/tests/test_knowledge_ingest_publication_route.py:240-247; mcp/tests/test_knowledge_ingest_publication_route.py:250-263 |
| **The read route's owners the fixture resolves the declared location and the read-back through — the same owners the production route uses, which is what makes the fixture an independent side.** | `published_dataset_path`; `resolve_published_intent`; `PublishedIntentSelection`; `contract_context` | mcp/src/agents_remember/application/published_intent.py:239-255; mcp/src/agents_remember/application/published_intent.py:175-189; mcp/src/agents_remember/application/published_intent.py:258-282; mcp/src/agents_remember/worktrees/modules/context.py:38-77 |
| The shipped entry point every case drives, and the two real readers it measures through. | `main`; `build_parser`; `knowledge_read_payload`; `ReadToolRequest`; `open_read_only_database` | mcp/src/agents_remember/cli/__main__.py:95-97; mcp/src/agents_remember/cli/__main__.py:29-92; mcp/src/agents_remember/mcp/tools/knowledge.py:337-342; mcp/src/agents_remember/mcp/tools/knowledge.py:130-159; mcp/src/agents_remember/memory/knowledge/connection.py:52-63; mcp/src/agents_remember/mcp/tools/knowledge.py:343-351 |
| **The existing fixture module this one composes instead of introducing a third support module — the reason its catalog delta is a consumer change only.** | `_one_entry_list`; `_cli_json`; `_commit`; `_git`; `_write_files`; `_cycle01_hand_off`; `_cycle01_candidate_revisions`; `_cycle01_revisions_of` | mcp/tests/test_knowledge_curator_ingest_list.py:1702-1722; mcp/tests/test_knowledge_curator_ingest_list.py:1661-1666; mcp/tests/test_knowledge_curator_ingest_list.py:272-277; mcp/tests/test_knowledge_curator_ingest_list.py:280-291; mcp/tests/test_knowledge_curator_ingest_list.py:265-269; mcp/tests/test_knowledge_curator_ingest_list.py:2765-2770; mcp/tests/test_knowledge_curator_ingest_list.py:2913-2928; mcp/tests/test_knowledge_curator_ingest_list.py:2931-2948 |
| **The lane row this module occupies, and the two governed consumer rows it joined.** | "mcp/tests/test_knowledge_ingest_publication_route.py" | mcp/tests/test-evidence-lanes.toml:110-110 |
| **The catalog digest the two consumer rows moved, and the counts they do not move.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:44-45 |
| The production route these cases are the regression surface for. | `declared_publication_location`; `admitted_destination`; `published_identity_read_back` | mcp/src/agents_remember/application/knowledge_publication_route.py:115-132; mcp/src/agents_remember/application/knowledge_publication_route.py:135-199; mcp/src/agents_remember/application/knowledge_publication_route.py:202-250 |

## Cross-Repo References

No meaningful cross-repo references found: the whole fixture world is built inside one `tmp_path`, and
the enclosures it builds are this repository's own.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. `PublishedIntentSelection` gained an optional `memory_tree` field (MIK-R23); the claim that the fixture resolves the declared location and the read-back through the production owners was re-read and still holds, and the class range was re-measured to `:175-189`. Other ranges into `published_intent.py` and `test-evidence-lanes.toml` that this change set moved were re-pointed by the fixer or by exact base-to-working line mapping.
- 2026-09-29T05:55:41+00:00: Generated citation repair: "mcp/tests/test_knowledge_ingest_publication_route.py" repointed to mcp/tests/test-evidence-lanes.toml:110-110. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines, and `cli/__main__.py`, where the `knowledge-validate` subparser moved `main` down six lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T05:02:25+00:00: Generated citation repair: "mcp/tests/test_knowledge_ingest_publication_route.py" repointed to mcp/tests/test-evidence-lanes.toml:107-107. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the `main`/`build_parser` sources re-pointed to `cli/__main__.py:81-83` and `:27-78` after MIK-R21's registration shifted the umbrella module. Claim meaning unchanged; no stamp advanced.
- 2026-09-29T02:55:02+00:00: Generated citation repair: "mcp/tests/test_knowledge_ingest_publication_route.py" repointed to mcp/tests/test-evidence-lanes.toml:104-104. No content impact: mechanical anchor-range projection bound to citation source snapshot 2eb2ea9eedcea065d08ac926c00a066bf53846ee3aa35f06aeeb6a9d076a86de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/tests/test-evidence-lanes.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`, `mcp/tests/test_knowledge_curator_ingest_list.py`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the write plane is named by both its entry points (D55).** **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): created this one-to-one card for the new test module. Eleven cases drive the shipped `knowledge-ingest` entry point over a production-shaped enclosure (a real external memory repository with a real Git memory worktree) and read the result from the report, the file, and the mounted read surface — never from a prebuilt payload. The card records the six user operations plus the refusal family, the fixture's own reason for existing (the declared location is resolved by the read route's owner so the fixture cannot agree with the implementation about a path neither computes), the four helpers, the two real readers, and the census fact that makes this module's catalog delta a consumer change only: it composes the existing ingest-list fixture module rather than adding a support artifact, so the population stays at sixteen contracts and sixty-six artifacts and the digest re-pins for the two consumer rows alone. Every range was derived from its construct's own extent in this candidate rather than carried. **Verification metadata:** the card names the production line it was read against — `71a4433e686b3380af97a0836bb82bab2c8f2aad`, this leaf's base — because the module exists only in this leaf's uncommitted candidate, so no commit contains the content a stamp would claim to have verified. That is a statement of *what the reading was against*; the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates, and that remains the real stamp.
