# mcp/tests/test_memory_mode_removal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_mode_removal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:25+02:00 |
| lastVerifiedCommitHash | `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| lastVerifiedCommitDate | 2026-09-18T18:30:35+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l12`; code candidate landed as `b281bcd68261866be306cc80a48241921b6dd0d2` |
| governingOverview | `../overview.md` |

## Governing Overview

[Test suite overview](../overview.md)

## Purpose

The executable guard for the removal of `internal` memory mode. It pins three properties, and each is
written to name the failure it prevents rather than merely to pass: the mode is **refused by name**
(never silently substituted with `external` or a default), existing state that records it is
**reported and left byte-identical** (never migrated or deleted), and the **supported set is untouched**
(`external` and `disabled` still resolve, write and read through the application layer and the CLI).

## Code Commentary

### Logic

The module is a single file because the three properties belong to one removal; it is not a general
memory test suite. Its cases divide into seven groups.

**Vocabulary and narrowers.** The declared literals are asserted to hold no removed member, the two
narrowers are asserted to refuse the removed token by name, and — the distinction that matters — a case
asserts that an *unknown* token is still an ordinary invalid-argument error rather than being reported as
a removal. Both `_topology` and `_normalize_topology` are exercised with `"internal"`, `"bogus"`,
`"external"` and `None`, because the two flag narrowers previously reported every unknown token as a
removed mode.

**Entry-point refusals.** Worktree start refuses an explicit removed mode and a removed topology
argument; the resolver refuses a requested removed topology; `resolve_context_tool` and the baseline
topology flag refuse it; the contract writer refuses a removed mode request.

**Existing-state reporting.** A repository that still carries the removed root is reported, settings and
an onboarding root inside that root are reported *by their own path*, a configured memory root refuses
the removed layout, and the vocabulary derivation refuses it. The central case writes a contract that
records the removed mode and asserts it is reported **and left byte-identical** — the "reported, not
migrated" property in one assertion.

**Supported paths still work.** A removed token is refused while an unknown token still degrades; an
external selection still resolves; the default memory root is the external root when no removed layout
exists; a disabled contract round-trips.

**CLI surface.** The CLI never advertises the removed member, parses the supported set, and hands a
removed token to the typed refusal. A separate case asserts the worktree-start tool documentation no
longer offers the removed mode.

**Operator reporting (integration).** Eight marked cases drive published enclosures and assert the
operator receives the typed refusal with the artifact named: the worktree-status packet and payload, the
configured admission, the terminal admission on a surviving contract, direct landing and its reader, the
unstarted-evidence fact, and the negative case that a removed-mode answer **never claims publication was
lost**.

**The instruction/documentation plane (`L12R-3`).** Thirteen parametrized surfaces, each pairing
forbidden old-doctrine phrases (asserted absent) with a required corrected phrase (asserted present):
the canonical `c-00`, `c-13`, `c-08` and three `c-03` templates, the package-data copy of `c-00`, five
`docs/` pages and one `system/defaults` example. A final case asserts the generated skill copy is
**byte-identical** to the canonical tree it is generated from. This group exists because the removal's
strongest claim — that nothing still teaches the mode — had no executable guard: a reverted canonical
skill propagated to all nine generated copies left every generator check green, and a wholesale revert of
`docs/architecture.md` left the whole unit population green.

### Conventions

The expected supported set is written out **literally** in the module rather than imported from
`SUPPORTED_MEMORY_MODES`, with a comment stating why: a change to the vocabulary must then be made in two
places, so the test cannot silently agree with a mistake. Both sides of every comparison therefore come
from different sources.

The corpus guard reads files from `_REPO_ROOT` (`parents[2]` of the test file) and fails with the
offending phrase in the message, so a revert names what it re-taught. Parametrized ids are built from the
path so a failure identifies the surface.

Integration-marked cases are separated by the marker rather than by filename, which is why one module
carries both hermetic and published-enclosure cases.

### Invariants And Boundaries

**The module is registered and its evidence lane is declared.** It is registered under
`unit-regression` in `mcp/tests/test-evidence-lanes.toml`, and it is declared in two `consumers` lists in
`mcp/tests/evidence-lifecycle.toml`. The lane loader is fail-closed and is not loaded by ordinary pytest,
so a new module without a row ships unregistered under green suites; this module carries its row.

**46 collected cases**, split 38 unit and 8 integration. The instruction-corpus group is the case class
that fails when the corrected doctrine is reverted, and the operator group is the class that fails when
the typed refusal stops reaching the operator ahead of a generic `ValueError` clause.

**A test module is not authority.** The corpus guard asserts that the *shipped* surfaces do not teach the
removed default; it does not prove that the copies were generated rather than hand-edited, which is what
the generator's own `--check` mode proves.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned refusal,
migration-boundary and instruction-corpus assertions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three pinned properties, each named with the failure it prevents. | "memory mode: refused by name, reported, never substituted." | mcp/tests/test_memory_mode_removal.py:1-1 |
| The expected supported set is written literally, not imported, so a vocabulary change must be made twice. | `EXPECTED_MODES` | mcp/tests/test_memory_mode_removal.py:90-90 |
| The declared vocabulary holds no removed member. | `test_the_declared_vocabulary_has_no_removed_member` | mcp/tests/test_memory_mode_removal.py:119-122 |
| A removed token is refused by name while an unknown token stays an invalid-argument error. | `test_require_supported_topology_keeps_unknown_tokens_distinct_from_the_removal` | mcp/tests/test_memory_mode_removal.py:137-142 |
| Existing state recording the removed mode is reported and left byte-identical. | `test_a_contract_recording_the_removed_mode_is_reported_and_left_byte_identical` | mcp/tests/test_memory_mode_removal.py:318-333 |
| The supported paths are unaffected: external still resolves, disabled still round-trips. | `test_external_selection_still_resolves` | mcp/tests/test_memory_mode_removal.py:354-372 |
| The CLI never advertises the removed member and hands a removed token to the typed refusal. | `test_cli_never_advertises_the_removed_member` | mcp/tests/test_memory_mode_removal.py:393-399 |
| The tool documentation no longer offers the removed mode. | `test_the_start_tool_documentation_no_longer_offers_the_removed_mode` | mcp/tests/test_memory_mode_removal.py:427-433 |
| The operator receives the typed refusal with the recorded value, the supported set and the artifact. | `test_worktree_status_packet_reports_the_removed_mode_to_the_operator` | mcp/tests/test_memory_mode_removal.py:531-544 |
| A removed-mode answer never claims the publication was lost. | `test_a_removed_mode_answer_never_claims_publication_was_lost` | mcp/tests/test_memory_mode_removal.py:649-665 |
| Both flag narrowers distinguish a typo from a removal. | `test_the_flag_narrowers_do_not_report_a_typo_as_a_removal` | mcp/tests/test_memory_mode_removal.py:673-685 |
| Thirteen corpus and documentation surfaces are guarded against re-teaching the removed default. | `CORRECTED_SURFACES` | mcp/tests/test_memory_mode_removal.py:701-785 |
| The generated skill copy must equal the canonical tree it is generated from. | `test_the_generated_skill_copy_carries_the_canonical_correction` | mcp/tests/test_memory_mode_removal.py:802-809 |
| The module's evidence lane is declared under `unit-regression`. | "test_memory_mode_removal.py" | mcp/tests/test-evidence-lanes.toml:125-125 |
| The module is declared in three evidence-lifecycle consumer lists: the shared curator-coherence support artifact's list and two further artifact lists. | "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:384-384 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local refusal and corpus assertions.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T16:13:35+00:00: Generated citation repair: "test_memory_mode_removal.py" repointed to mcp/tests/test-evidence-lanes.toml:125-125. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:384-384. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "test_memory_mode_removal.py" repointed to mcp/tests/test-evidence-lanes.toml:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "test_memory_mode_removal.py" repointed to mcp/tests/test-evidence-lanes.toml:122-122. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_memory_mode_removal.py" repointed to mcp/tests/test-evidence-lanes.toml:120-120. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:380-380. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.


- 2026-09-16T14:25+02:00 — 260915-CAPS-L12 curator (closeout-gate follow-up): the two verification fields above, which this card's creation entry left un-advanced, were populated on the closeout gate's refusal — `external-memory closeout requires onboarding verification metadata before memory commit`. They follow the canonical file-level model (`file-level-onboarding-workflow.md` § Metadata Rules: "use the latest commit that touched the source file once the content has been verified") and now read hash `b281bcd68261866be306cc80a48241921b6dd0d2`, date `2026-09-16T14:24:58+02:00` — the `[260915-CAPS-L12]` code commit that actually contains this source file, matching the value closeout's own `refresh_onboarding_metadata_for_context` writes for every required card. An earlier revision of this entry named the pre-commit base `c1dbebf8`, which does not contain this file; that value was replaced rather than retained, and no earlier history entry was rewritten. The creation entry's sentence that no stamp was advanced is superseded here, added rather than edited because `Update History` is append-only. Closeout re-stamps both fields authoritatively at the real commit.
- 2026-09-16T14:05+02:00 — 260915-CAPS-L12 curator: **created the missing sidecar** for the module
  `CAPS-R12@v1` added. Recorded the three pinned properties, the seven case groups, the 38-unit/8-
  integration split of 46 collected cases, the literal-expected-set convention, the 13 parametrized
  corpus surfaces with their byte-identity case, and the lane row under `unit-regression` at line 78
  plus the two `evidence-lifecycle.toml` consumer entries. Verification metadata remains
  closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.
