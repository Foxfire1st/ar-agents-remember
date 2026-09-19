# test_role_instruction_corpus.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_role_instruction_corpus.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678` |
| lastVerifiedCommitDate | 2026-09-19T12:15:35+02:00|
| governingOverview      | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

The shipped behavioral check for the canonical role-instruction corpus at
`skills/l-01-agent-lifecycles/`. It protects the properties a consumer depends on: every role in the
registry has exactly one readable role source; every role source carries the agreed six-section order and
its machine-readable knob block; the composition manifest resolves to files that exist for every role and
every operation; the role registry is exactly nine roles and the ambient launcher is a routing condition
rather than a tenth role; the manifest is a metadata plane that copies no payload; **every** relative path
the corpus cites resolves; a manifest that points at a missing source is reported rather than silently
accepted; and a repo-relative anchor pointed at nothing is reported by the link check itself rather than
passing silently.

**Six cases, not the four first landed.** The module was extended by the owning seat during this leaf's
curation window; this card describes the current shipped module (`:598` lines, six `test_*` functions).

## Code Commentary

### Logic

The module resolves its subject from the repository root (`REPOSITORY_ROOT` → `SKILLS_ROOT` →
`LIFECYCLE_ROOT` → `MANIFEST_PATH`), so it always tests the worktree it runs from. Its declared
vocabulary is the corpus contract in miniature: `ROLE_ORDER` (nine roles), `REQUIRED_SECTIONS` (the six
readable sections every role file must carry in order), `OPERATION_KEYS` (the frozen eight operations),
and `MACHINE_SECTION` (the knob block that must follow § 6).

The resolver is deliberately split into small cohesive helpers — `_check_core`, `_check_operations`,
`_check_roles` (with `_check_role_order` and `_check_one_role`), and `_check_launcher_and_references` —
because the earlier single-function version tripped ruff's complexity limits. That split is the point:
`_resolve_sources` returns a list of human-readable problems rather than a boolean, so a manifest entry
that names a missing source, an unknown core block, an unknown operation, or a missing criteria catalog is
**reported**, never skipped.

`test_manifest_resolves_every_role_and_operation_source` additionally asserts the router still registers
every `roles/<role>.md`, that `launcher` is absent from `manifest["roles"]`, that `ambient-launcher` is one
of the routing conditions, and that the manifest carries no prose lines.

`test_manifest_carries_routing_metadata_not_copied_payloads` is the metadata-plane case: it walks every
JSON string in the manifest (`_iter_json_strings`), applies the `manifest_copy_indicators` heuristics, and
fails on copied payload content, so the manifest cannot quietly become a second copy of a source section.
It is staged against a `tmp_path` copy so it can also prove the detector fires on a deliberately copied
payload without failing the healthy tree.

`test_every_role_source_carries_the_readable_order_and_knob_block` asserts each role file is longer than a
stub, opens YAML frontmatter declaring `l-01-agent-lifecycles-role-<role>` plus a description, carries
`**Inherits:**` naming every core block the manifest assigns it, presents the six required headings in
order, places the knob block after them, and declares its `harness`/`model`/`effort`/`dispatch`/`tools`
rows plus its `orchestration.rolesPerLevel` override keys. Its final loop is the corpus's independence
rule made executable: a role may name a sibling role file **only** under
`SANCTIONED_SIBLING_REFERENCES` (the architect's designer hat, the orchestrator's strategist and designer
dispatches, the strategist's and reviewer's manager references); anything else fails.

`test_manifest_reports_a_missing_source_instead_of_accepting_it` stages a copy of the tree in `tmp_path`
and breaks the manifest several ways — a renamed role file, a moved operation source, an unknown
operation, an unknown core block, a missing criteria catalog — asserting each is reported, then
re-resolving the healthy staged copy so the negatives are not false alarms. That last assertion is the
load-bearing negative: a validator that would silently accept a missing source would make every other
manifest assertion meaningless.

`test_every_relative_path_the_corpus_cites_resolves` walks every Markdown file under the lifecycle root,
extracts path tokens through `cited_paths` (backticked paths plus `PATH_TOKEN` matches, filtered by
`NON_LOCATION_RE` and `SYMBOLIC_FILE_NAMES`), and resolves each either relative to the citing file or
against `CORPUS_LOCATIONS`. It caught a real defect during the consolidation — a
`../w-02-light-task-workflow/requirement-packet-template.md` reference in `core/loop.md` that resolved
inside the wrong skill until it was corrected to `../../`. A new `COORDINATION_ROOT_RE` guard keeps
paths that belong to the coordination tree (`system/`, `tasks/`, `notes/`, `runtime/`, `worktrees/`,
`memory-repos/`) out of the repository-relative resolution space instead of reporting them as dangling.

`test_link_check_reports_a_repo_relative_anchor_pointed_at_nothing` is that check's own negative: it
stages a tree whose document cites a repo-relative path that exists nowhere and asserts
`unresolved_references` reports it, so the link check cannot silently pass by resolving nothing.

### The Complete-Curation Guard (CAPS-R18@v1)

Two cases were added for the master's own doctrine change: `CurationIsCompleteOnEveryLeafTests` sweeps the
canonical tree **and** all nine generated copies for the eleven retired optional-curation sentences and
asserts that every canonical source which must state the rule still does, and `CurationGuardTeethTests` is
the falsifiability half — re-inserting one retired sentence on its own surface must be reported, the
preserved developer-request doctrine (full code quality and full tests) must read clean, and a statement
must be reported only on a surface that shipped it. Both read the registry and readers in the new support
module `mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py`. The module grew from
6 to 14 cases and stays in its existing `unit-regression` lane, so no lane row and no case budget key was
touched. The guard's declared limit travels with it: it matches whole retired sentences restricted to the
files that shipped them, so a restatement of the defect in fresh vocabulary is out of its reach.

### Conventions

Six cases plus their module-level helpers, no fixtures beyond `tmp_path`, and no network or provider
access: the module reads the canonical tree and the manifest directly. A new corpus invariant belongs
here as a new assertion rather than in a separate ad-hoc script.

### Invariants And Boundaries

- The check reads the canonical `skills/` tree only; generated copies are verified by
  `scripts/sync-skills.py --check`, not here.
- Each positive case has a paired negative (a broken manifest, a copied payload, a dangling anchor), so a
  check that resolves nothing cannot pass as green.
- Assertions are property-based on the corpus, so they stay valid as role prose changes; only a change to
  the corpus **shape** should require editing this module.
- The module must never weaken `SANCTIONED_SIBLING_REFERENCES` to accommodate a new cross-reference — a
  new sibling reference is a corpus design change, not a test fix.
- A manifest that names a missing source must keep failing: that assertion is what makes the manifest
  trustworthy.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local corpus check.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolver under test and the six shipped cases. | "the resolver under test" | mcp/tests/test_role_instruction_corpus.py:153-153 |
| The corpus this module is the behavioral check for: the canonical root `skills/l-01-agent-lifecycles/` tree, whose declared contract is `ROLE_ORDER`, `REQUIRED_SECTIONS`, `MACHINE_SECTION` and `OPERATION_KEYS`. | "Focused behavioral check for the consolidated role-instruction corpus" | mcp/tests/test_role_instruction_corpus.py:1-116 |
| The manifest this module resolves, and the corpus it governs. | `schema`; `entry_router`; `routing_conditions` | skills/l-01-agent-lifecycles/composition-manifest.json:2-2; skills/l-01-agent-lifecycles/composition-manifest.json:4-4; skills/l-01-agent-lifecycles/composition-manifest.json:18-18 |
| Generated copies are checked by the propagation owner, not by this module. | "[sync-skills] run: python3 scripts/sync-skills.py" | scripts/sync-skills.py:188-201 |

## Cross-Repo References

No sibling-repository contract defines this corpus check.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: "the resolver under test" repointed to mcp/tests/test_role_instruction_corpus.py:153-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: this module was extended by the leaf's own change (6 → 14 cases, 602 → 773 lines) with the complete-curation corpus guard and its falsifiability teeth, which read the new `testing/curation_doctrine.py` registry. Body updated with what the two new classes protect, the nine generated copies they sweep, the lane and budget facts, and the matcher's declared limit. The leaf's citation rows that pointed `SANCTIONED_SIBLING_REFERENCES` at the old :84-89 were re-pointed to :110 in the three role cards that cite it. Verification metadata remains closeout-owned; no stamp was advanced.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body rebased after the module was extended mid-curation.** The code worktree was not frozen while this pass ran: the module grew from 362 to 598 lines and from four to six cases, adding `test_manifest_carries_routing_metadata_not_copied_payloads` (with `manifest_copy_indicators`, `_iter_json_strings`, `manifest_prose_lines`) and `test_link_check_reports_a_repo_relative_anchor_pointed_at_nothing` (with `unresolved_references`), plus the `cited_paths` / `PATH_TOKEN` / `NON_LOCATION_RE` / `SYMBOLIC_FILE_NAMES` / `COORDINATION_ROOT_RE` machinery. This card now describes the current shipped module and cites the six cases at their current line ranges. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for the focused check the leaf added with the role-instruction corpus consolidation. It is a **shipped repository test**, not a task-local fixture: its cases are the executable form of the corpus's shape contract (nine roles, six readable sections, the frozen eight-operation vocabulary, a metadata-only manifest, every cited relative path resolving, and a missing manifest source reported rather than accepted). Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
